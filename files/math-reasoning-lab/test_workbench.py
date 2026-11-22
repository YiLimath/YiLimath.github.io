import tempfile
import unittest
from pathlib import Path
from workbench import Workbench, case_a

class WorkbenchTests(unittest.TestCase):
    def add_review(self,w,key):
        w.review(key,w.argument_hash(key),"informal-reviewed","Fixture evidence","test")

    def test_alternative_survives_then_both_fail(self):
        w=case_a()
        self.assertEqual(w.report("lift")["status"],"usable")
        w.withdraw("vanishing-evidence","bad applicability")
        self.assertEqual(w.report("lift")["argument"],"via-obstruction")
        w.withdraw("direct-obstruction","bad calculation")
        self.assertEqual(w.report("lift")["status"],"unresolved")

    def test_unsupported_cycle_cannot_bootstrap(self):
        w=Workbench()
        for k in ["A","B"]:w.statement(k,k)
        w.argument("a","A",["B"],"proposed implication","fixture")
        w.argument("b","B",["A"],"proposed implication","fixture")
        self.add_review(w,"a");self.add_review(w,"b")
        self.assertEqual(w.closure(),{})
        w.argument("base","A",[],"independent proof","fixture")
        self.add_review(w,"base")
        self.assertEqual(set(w.closure()),{"A","B"})

    def test_assumptions_remain_visible(self):
        w=Workbench();w.statement("P","P");w.statement("Q","Q")
        w.argument("step","Q",["P"],"P implies Q","fixture");self.add_review(w,"step")
        self.assertEqual(w.report("Q")["status"],"unresolved")
        result=w.report("Q",assumptions=["P"])
        self.assertEqual(result["status"],"conditional");self.assertEqual(result["assumptions"],["P"])

    def test_evidence_types_are_not_interchangeable(self):
        self.assertEqual(case_a().report("lift",allowed=["formal-checked"])["status"],"unresolved")

    def test_stale_review_rejected(self):
        w=case_a()
        with self.assertRaises(ValueError):w.review("via-vanishing","stale","informal-reviewed","report","reviewer")
        with self.assertRaises(ValueError):w.statement("lift","different statement")

    def test_save_reload_and_tamper(self):
        w=case_a();w.withdraw("vanishing-evidence","incorrect")
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/"state.json";w.save(p)
            self.assertEqual(Workbench.load(p).report("lift"),w.report("lift"))
            s=p.read_text();p.write_text(s.replace("The chosen section s lifts","Changed conclusion"))
            with self.assertRaises(ValueError):Workbench.load(p)

    def test_missing_joint_premise(self):
        w=case_a();w.withdraw("setup-evidence","wrong sheaf")
        self.assertEqual(w.report("lift")["status"],"unresolved")

    def test_wrong_math_can_pass_policy(self):
        w=Workbench();w.statement("false","Every continuous function on (0,1) attains a maximum")
        w.argument("bad","false",[],"An incorrect argument","fixture");self.add_review(w,"bad")
        self.assertEqual(w.report("false")["status"],"usable")
        # This test documents the trust boundary, not a desired theorem-proving result.

if __name__ == "__main__":unittest.main()
