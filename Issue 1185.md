# Issue 1185: Coercion trouble

Issue created by migration from Trac.

Original creator: ifti

Original creation time: 2007-11-16 10:39:30

Assignee: was

I run into some coercion trouble when I reduce a fourier coefficient
of a cusp form modulo a prime ideal.

Any idea how I can avoid this?


```
sage: M = ModularSymbols(77, 2)

sage: s = M.cuspidal_subspace().new_subspace()

sage: N = s.decomposition()

sage: f = N[3].q_eigenform()

sage: R = f.base_ring()

sage: K = R.number_field()

sage: O = K.ring_of_integers()

sage: I = O.ideal(7)

sage: F = O.residue_field(I)

sage: F(f[2])
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call
last)

/home/burhanud/tau_nov14_07/<ipython console> in <module>()

/home/burhanud/tau_nov14_07/residue_field.pyx in
sage.rings.residue_field.ResidueFiniteField_givaro.__call__()

/home/burhanud/tau_nov14_07/finite_field_givaro.pyx in
sage.rings.finite_field_givaro.FiniteField_givaro.__call__()

<type 'exceptions.TypeError'>: unable to coerce
```



---

Comment by ifti created at 2007-11-16 10:59:33

This was an email posted to the sage-devel mailing list on 11/05/07. Consult thread for the discussion.


---

Comment by mabshoff created at 2007-11-16 11:13:32

David Roe filed another ticket on that, so please also look at #1183.

Cheers,

Michael


---

Comment by was created at 2007-12-15 10:09:16

The correct way is this, which works with #1183 applied.

```
sage: M = ModularSymbols(77, 2)
sage: s = M.cuspidal_subspace().new_subspace()
sage: N = s.decomposition()
sage: f = N[3].q_eigenform()
sage: R = f.base_ring()
sage: K = R.number_field()
sage: O = K.ring_of_integers()
sage: I = O.ideal(7)
sage: F = O.residue_field(I)
sage: F(f[2].lift())
alphabar
```



---

Comment by mabshoff created at 2007-12-15 13:44:05

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 13:44:05

resolved due to patch set from #1183
