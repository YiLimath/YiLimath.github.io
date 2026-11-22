"""Teaching ledger: dependency policy, NOT mathematical verification.
Run: python ledger.py
A review is supplied externally; this code cannot judge its correctness.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Claim:
    statement: str
    premises: tuple = ()

class Ledger:
    def __init__(self):
        self.claims = {}
        self.reviewed = set()
        self.withdrawn = set()

    def add(self, key, statement, premises=()):
        if key in self.claims:
            raise ValueError("Immutable identifier: create a new version")
        self.claims[key] = Claim(statement, tuple(premises))
        try:
            self._check_cycles()
        except ValueError:
            del self.claims[key]
            raise

    def _check_cycles(self):
        active, done = set(), set()
        def visit(key):
            if key in active:
                raise ValueError("Circular dependency")
            if key in done or key not in self.claims:
                return
            active.add(key)
            for premise in self.claims[key].premises:
                visit(premise)
            active.remove(key)
            done.add(key)
        for key in self.claims:
            visit(key)

    def usable(self, key):
        if key not in self.claims or key not in self.reviewed or key in self.withdrawn:
            return False
        return all(self.usable(p) for p in self.claims[key].premises)

    def review(self, key):
        if key not in self.claims:
            raise ValueError("Unknown version")
        if key in self.withdrawn:
            raise ValueError("Withdrawn version: create a replacement")
        self.reviewed.add(key)

    def withdraw(self, key):
        if key not in self.claims:
            raise ValueError("Unknown claim")
        self.withdrawn.add(key)


def expect_rejection(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError("Expected rejection")


def demo():
    ledger = Ledger()
    ledger.add("maximum-v1", "f attains a maximum on K",
               ("continuous-v1", "compact-v1", "evt-v1"))
    ledger.review("maximum-v1")
    assert not ledger.usable("maximum-v1")  # missing premises
    for key, statement in [
        ("continuous-v1", "f is continuous on K"),
        ("compact-v1", "K is nonempty and compact"),
        ("evt-v1", "Extreme value theorem applies to real-valued f")]:
        ledger.add(key, statement)
        ledger.review(key)
    assert ledger.usable("maximum-v1")
    ledger.withdraw("compact-v1")
    assert not ledger.usable("maximum-v1")  # downstream use suspended
    assert "maximum-v1" in ledger.claims  # record preserved, not declared false
    expect_rejection(lambda: ledger.add("maximum-v1", "Changed statement"))
    expect_rejection(lambda: ledger.review("unknown-v2"))
    expect_rejection(lambda: ledger.review("compact-v1"))
    ledger.add("A", "Candidate A", ("B",))
    expect_rejection(lambda: ledger.add("B", "Candidate B", ("A",)))
    assert "B" not in ledger.claims  # rejected write rolled back
    print("PASS: missing premises, conjunction, withdrawal, immutable versions,")
    print("unknown review, withdrawn review, cycle detection, rollback.")
    print("No mathematical theorem was verified by these tests.")

if __name__ == "__main__":
    demo()
