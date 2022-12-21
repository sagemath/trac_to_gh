# Issue 6019: [with patch, needs review] speed up new_subspace by a factor of > 100

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-05-11 10:16:52

Assignee: craigcitro

CC:  craigcitro

I forgot to disable the automatic Hecke-invariance check, and to use the already-calculated dual free module, when calling the submodule constructor to constructing new subspaces of modular forms spaces. 

That meant that the very time-consuming functions `_is_hecke_invariant_free_module` and `dual_free_module` were getting called, which slowed down the computation *ridiculously*.

Before:

```
sage: C = CuspForms(12, 8)
sage: time C.new_submodule()
CPU times: user 217.98 s, sys: 0.39 s, total: 218.37 s
Wall time: 229.00 s
Modular Forms subspace of dimension 2 of Modular Forms space of dimension 17 for Congruence Subgroup Gamma0(12) ofweight 8 over Rational Field
```


After:

```
sage: time C.new_submodule()
CPU times: user 1.55 s, sys: 0.02 s, total: 1.57 s
Wall time: 1.58 s
Modular Forms subspace of dimension 2 of Modular Forms space of dimension 17 for Congruence Subgroup Gamma0(12) ofweight 8 over Rational Field
```


So that's a speedup by a factor of 139 in this example.


---

Attachment


---

Comment by davidloeffler created at 2009-05-11 18:51:12

Craig: I'm ccing you on this as it's a followup to #4357, which you reviewed. It's a one-line change.


---

Comment by craigcitro created at 2009-05-11 18:51:51

Nice catch. `:)`


---

Comment by davidloeffler created at 2009-05-11 18:56:44

Wow, that was quick - thanks!


---

Comment by mabshoff created at 2009-05-12 04:55:29

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 04:55:29

Resolution: fixed
