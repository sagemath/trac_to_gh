# Issue 6325: optional doctest failure -- linear algebra constructions.rst

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 14:56:17

Assignee: tbd


```
sage -t -long --optional devel/sage/doc/en/constructions/linear_algebra.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/linear_algebra.rst", line 461:
    sage: octave.solve_linear_system(A,b)    # requires optional octave
Expected:
    [-0.33333299999999999, 0.66666700000000001, -3.5236600000000002e-18]
Got:
    [-0.33333299999999999, 0.66666700000000001, 0]
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_21
***Test Failed*** 1 failures.
```



---

Comment by wdj created at 2009-06-16 23:29:52

I'm not sure how to fix this. Should I add "# random numerical noise" in addition to "# requires optional octave"? By the way, octave is not strictly speaking an optional package is it?


---

Comment by wdj created at 2009-06-17 12:56:10

Reply by email:

> I'm ok for now with just changing the output to 0 since I'm only
> running optional doctests on sage.math, with the output is 0.
> William

The attached patch does this.

Patch applies fine to 4.0.2.rc1 and passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds sage -docbuild constructions html (resp., pdf) went fine.


---

Attachment

applies to 4.0.2.rc1


---

Comment by mhansen created at 2009-09-08 23:04:11

Looks good to me.


---

Comment by mvngu created at 2009-09-09 11:13:53

Resolution: fixed
