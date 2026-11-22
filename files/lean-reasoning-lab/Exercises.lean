-- Keep this file outside the default library target.
-- Complete these proofs, then audit their axioms.
theorem witnessAfter (n : Nat) : ∃ C : Nat, n < C := by
  sorry

theorem noLargestNatural : ¬ ∃ C : Nat, ∀ n : Nat, n ≤ C := by
  sorry

#print axioms witnessAfter
#print axioms noLargestNatural
