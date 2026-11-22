"""Research workbench: policy and provenance, not mathematical verification.
Python 3.9+, standard library only. Run: python workbench.py
"""
from dataclasses import dataclass, asdict
from hashlib import sha256
from pathlib import Path
import json
import os


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                             separators=(",", ":")).encode()).hexdigest()


@dataclass(frozen=True)
class Statement:
    text: str
    assumptions: tuple = ()


@dataclass(frozen=True)
class Argument:
    conclusion: str
    premises: tuple
    justification: str
    source: str


@dataclass(frozen=True)
class Review:
    argument: str
    argument_hash: str
    kind: str
    report: str
    reviewer: str


class Workbench:
    """Caller supplies reviews. No authentication or truth oracle is provided."""
    kinds = {"source-checked", "informal-reviewed", "formal-checked"}

    def __init__(self):
        self.statements = {}
        self.arguments = {}
        self.reviews = {}
        self.withdrawn = set()
        self.events = []

    def statement(self, key, text, assumptions=()):
        if key in self.statements:
            raise ValueError("Statement identifier is immutable")
        if not text.strip():
            raise ValueError("Statement text required")
        self.statements[key] = Statement(text, tuple(assumptions))
        self.events.append({"event": "statement", "id": key})

    def argument(self, key, conclusion, premises, justification, source):
        if key in self.arguments:
            raise ValueError("Argument identifier is immutable")
        if conclusion not in self.statements or any(p not in self.statements for p in premises):
            raise ValueError("Declare every statement first")
        if not justification.strip() or not source.strip():
            raise ValueError("Justification and provenance required")
        self.arguments[key] = Argument(conclusion, tuple(premises), justification, source)
        self.events.append({"event": "argument", "id": key})

    def argument_hash(self, key):
        a = self.arguments[key]
        return digest({"argument": asdict(a), "statements": {
            k: asdict(self.statements[k]) for k in (a.conclusion,) + a.premises}})

    def review(self, key, argument_hash, kind, report, reviewer):
        if key not in self.arguments or argument_hash != self.argument_hash(key):
            raise ValueError("Review must bind to the exact argument and statement versions")
        if key in self.withdrawn:
            raise ValueError("Withdrawn argument requires a new version")
        if kind not in self.kinds or not report.strip() or not reviewer.strip():
            raise ValueError("Evidence kind, report, and reviewer required")
        self.reviews.setdefault(key, []).append(Review(key, argument_hash, kind, report, reviewer))
        self.events.append({"event": "review", "id": key, "kind": kind})

    def withdraw(self, key, reason):
        if key not in self.arguments or not reason.strip():
            raise ValueError("Known argument and withdrawal reason required")
        self.withdrawn.add(key)
        self.events.append({"event": "withdraw", "id": key, "reason": reason})

    def closure(self, allowed=("source-checked", "informal-reviewed"), assumptions=()):
        """Least fixed point. Unsupported cycles never bootstrap themselves.
        Each returned support is (argument id, explicitly used assumptions).
        For clarity this chooses one witness, not every minimal support set.
        """
        allowed = set(allowed)
        if not allowed <= self.kinds:
            raise ValueError("Unknown evidence policy")
        assumptions = set(assumptions)
        if not assumptions <= self.statements.keys():
            raise ValueError("Unknown assumption")
        known = {k: (None, frozenset([k])) for k in assumptions}
        changed = True
        while changed:
            changed = False
            for key, a in self.arguments.items():
                if a.conclusion in known or key in self.withdrawn:
                    continue
                if not any(v.kind in allowed and v.argument_hash == self.argument_hash(key)
                           for v in self.reviews.get(key, [])):
                    continue
                if not all(p in known for p in a.premises):
                    continue
                used = set(self.statements[a.conclusion].assumptions)
                for premise in a.premises:
                    used.update(known[premise][1])
                # Statement-level assumptions are obligations too.
                if not used <= assumptions:
                    continue
                known[a.conclusion] = (key, frozenset(used))
                changed = True
        return known

    def report(self, target, **policy):
        if target not in self.statements:
            raise ValueError("Unknown target")
        known = self.closure(**policy)
        if target in known:
            argument, assumptions = known[target]
            return {"target": target, "status": "conditional" if assumptions else "usable",
                    "argument": argument, "assumptions": sorted(assumptions)}
        candidates = []
        for key, a in self.arguments.items():
            if a.conclusion == target:
                candidates.append({"argument": key, "withdrawn": key in self.withdrawn,
                                   "missing": [p for p in a.premises if p not in known]})
        return {"target": target, "status": "unresolved", "candidates": candidates}

    def save(self, path):
        path = Path(path)
        data = {"format": 1, "statements": {k: asdict(v) for k,v in self.statements.items()},
                "arguments": {k: asdict(v) for k,v in self.arguments.items()},
                "reviews": {k: [asdict(v) for v in vs] for k,vs in self.reviews.items()},
                "withdrawn": sorted(self.withdrawn), "events": self.events}
        temp = path.with_name(path.name + ".tmp")
        with temp.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp, path)

    @classmethod
    def load(cls, path):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        if data.get("format") != 1:
            raise ValueError("Unknown file format")
        w = cls()
        for k,v in data["statements"].items():
            w.statements[k] = Statement(v["text"], tuple(v["assumptions"]))
        for k,v in data["arguments"].items():
            w.arguments[k] = Argument(v["conclusion"], tuple(v["premises"]), v["justification"], v["source"])
        w.reviews = {k:[Review(**v) for v in vs] for k,vs in data["reviews"].items()}
        w.withdrawn = set(data["withdrawn"])
        w.events = data["events"]
        if any(k not in w.arguments or v.argument_hash != w.argument_hash(k)
               for k,vs in w.reviews.items() for v in vs):
            raise ValueError("Saved review does not match its artifact")
        return w


def case_a():
    w = Workbench()
    for key,text in [("setup", "Exact sequence for the fixed X, S, L and section s"),
                     ("vanishing", "H1(X,L(-S)) vanishes"),
                     ("obstruction", "delta(s)=0"), ("lift", "The chosen section s lifts")]:
        w.statement(key,text)
    def add(key, target, premises, reason):
        w.argument(key,target,premises,reason,"Case A teaching fixture")
        w.review(key,w.argument_hash(key),"informal-reviewed",reason,"fixture author")
    add("setup-evidence","setup",[],"Ideal sequence tensored with an invertible sheaf")
    add("vanishing-evidence","vanishing",[],"Stipulated assumption for this fixture, not a computation")
    add("via-vanishing","lift",["setup","vanishing"],"Exactness and zero obstruction group")
    add("direct-obstruction","obstruction",[],"Stipulated direct obstruction calculation")
    add("via-obstruction","lift",["setup","obstruction"],"Exactness: delta(s)=0")
    return w


if __name__ == "__main__":
    w = case_a()
    print(json.dumps(w.report("lift"), indent=2))
    w.withdraw("vanishing-evidence", "The proposed vanishing theorem was inapplicable")
    print(json.dumps(w.report("lift"), indent=2))
    w.withdraw("direct-obstruction", "The calculation used a different section")
    print(json.dumps(w.report("lift"), indent=2))
    print("These are evidence-policy outcomes, not machine-checked mathematics.")
