theorem pointwiseBound : ∀ n : Nat, ∃ C : Nat, n ≤ C := by
  intro n
  exact ⟨n, Nat.le_refl n⟩

theorem noUniformBound : ¬ ∃ C : Nat, ∀ n : Nat, n ≤ C := by
  intro h
  cases h with
  | intro C hC =>
    exact Nat.not_succ_le_self C (hC (Nat.succ C))

#print axioms pointwiseBound
#print axioms noUniformBound
