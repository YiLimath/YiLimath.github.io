theorem witnessAfter (n : Nat) : ∃ C : Nat, n < C := by
  exact ⟨Nat.succ n, Nat.lt_succ_self n⟩

theorem noLargestNatural : ¬ ∃ C : Nat, ∀ n : Nat, n ≤ C := by
  intro h
  cases h with
  | intro C hC =>
    exact Nat.not_succ_le_self C (hC (Nat.succ C))

#print axioms witnessAfter
#print axioms noLargestNatural
