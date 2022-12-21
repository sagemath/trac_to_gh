# Issue 7677: sage-4.3.rc0: powerpc g5 doctest blockers

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-13 19:19:28

Assignee: tbd


```
I did a build test on OS X 10.5 PPC and there are some problems I think not mentioned elsewhere.  The first is a badly written doctest by somebody who didn't think about hash values being architecture dependent, and the second is valid numerical noise:

pdlc424:sage-4.3.rc0 wstein$         sage -t -long "devel/sage/sage/numerical/mip.pyx"
**********************************************************************
File "/Users/wstein/build/sage-4.3.rc0/devel/sage/sage/numerical/mip.pyx", line 987:
    sage: p._NormalForm(v[0] + v[1])
Expected:
    {0: 0, x1: 1, x0: 1}
Got:
    {x1: 1, 0: 0, x0: 1}


pdlc424:sage-4.3.rc0 wstein$         sage -t -long "devel/sage/sage/rings/complex_double.pyx"
**********************************************************************
File "/Users/wstein/build/sage-4.3.rc0/devel/sage/sage/rings/complex_double.pyx", line 2046:
    sage: z^2 - z + 1
Expected:
    -4.4408920985e-16
Got:
    -2.22044604925e-16 - 2.22044604925e-16*I
```



---

Attachment


---

Comment by mhansen created at 2009-12-14 17:13:47

Changing status from new to needs_review.


---

Comment by was created at 2009-12-24 07:58:52

Merged in 4.3.rc2.


---

Comment by was created at 2009-12-24 07:58:52

Resolution: fixed
