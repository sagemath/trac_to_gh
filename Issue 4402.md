# Issue 4402: Sage 3.1.4: magma related optional doctest failure in tut.tex

Issue created by migration from https://trac.sagemath.org/ticket/4402

Original creator: mabshoff

Original creation time: 2008-10-30 17:34:25

Assignee: was


```
sage -t -long -optional devel/doc/prog/prog.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/prog.py", line 520:
    sage: E._magma_init_() # optional -- requires Magma
Expected:
    'EllipticCurve([_sage_[1]|GF(41)!0,GF(41)!0,GF(41)!0,GF(41)!2,GF(41)!5])'
Got:
    'EllipticCurve([GF(41)|GF(41)!0,GF(41)!0,GF(41)!0,GF(41)!2,GF(41)!5])'
**********************************************************************
```


Trivial to fix since this is just a printing issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-28 09:34:40

William,

this one is still there since the TeX documentation isn't run per default. Unless you beat me to it I will fix this tomorrow.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-11-30 07:48:48

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 08:24:17

Resolution: fixed


---

Comment by mabshoff created at 2008-11-30 08:24:17

Merged in Sage 3.2.1.rc1
