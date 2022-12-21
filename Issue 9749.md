# Issue 9749: huge performance regression in computing with level one modular forms

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-08-14 19:06:36

Assignee: craigcitro

CC:  alexghitza craigcitro

I was working on the Ribet-Stein book, and a computation that is trivial in Magma, and must have been trivial in Sage until recently is now impossibly hard.


```
sage: M = ModularForms(1,512)
sage: time M.hecke_matrix(5)
[This is the Trac macro *takes a very, very long time indeed.* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#takes a very, very long time indeed.-macro)
```

This is very sad, since M has dimension only 43. Also, it is easy to get the answer directly --from start to finish in less than a second! -- as follows:

```
sage: time B = victor_miller_basis(512,5*43+1)
CPU times: user 0.21 s, sys: 0.00 s, total: 0.21 s
Wall time: 0.21 s
sage: time t5 = hecke_operator_on_basis(B, 5, 512)
CPU times: user 0.61 s, sys: 0.00 s, total: 0.61 s
Wall time: 0.61 s
```




---

Attachment


---

Comment by AlexGhitza created at 2010-08-31 08:56:48

The attached patch makes ambient spaces of level 1 modular forms use the Victor Miller basis for Hecke matrix computations.


---

Comment by AlexGhitza created at 2010-08-31 08:56:48

Changing status from new to needs_review.


---

Comment by was created at 2010-09-07 17:16:36

Positive review.  Note -- I made a new patch that fixes a typo: "Endusers" --> "End users".


---

Comment by was created at 2010-09-07 17:16:36

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-09-07 17:16:57

apply this one only.


---

Comment by mpatel created at 2010-09-15 10:39:46

Resolution: fixed


---

Attachment
