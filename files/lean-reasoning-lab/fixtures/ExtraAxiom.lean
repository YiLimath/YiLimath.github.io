axiom inventedBound : ∃ C : Nat, ∀ n : Nat, n ≤ C
theorem assumedBound : ∃ C : Nat, ∀ n : Nat, n ≤ C := inventedBound
#print axioms assumedBound
