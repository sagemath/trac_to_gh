# Issue 4016: [with patch, needs review] improve doctests to schemes/generic/scheme.py

Issue created by migration from https://trac.sagemath.org/ticket/4016

Original creator: AlexGhitza

Original creation time: 2008-08-31 07:52:18

Assignee: mabshoff

Brings coverage up to 96% (sorry, I have no idea what's going on with the one remaining function).




---

Comment by robertwb created at 2008-08-31 08:11:40

All the doctests look sane to me, and mabshoff is verifying that they all pass.


---

Comment by mabshoff created at 2008-08-31 08:29:54

One slight problem in tut.tex:

```
sage -t -long devel/doc/tut/tut.tex
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/tmp/tut.py", line 2178:
    : D
Expected:
    Affine Curve over Rational Field defined by
       x^5 + x^3*y^2 + x^2*y^3 + y^5 - x^3 - y^3 - x^2 - y^2 + 1
Got:
    Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
      x^5 + x^3*y^2 + x^2*y^3 + y^5 - x^3 - y^3 - x^2 - y^2 + 1
**********************************************************************
```



---

Attachment


---

Comment by AlexGhitza created at 2008-08-31 12:08:35

Sorry Michael, I should have tested the docs as well...  anyway, it just required a small fix in plane_curves/curve.py.  I have replaced the patch with one that adds that small fix.


---

Comment by mabshoff created at 2008-09-01 02:18:03

Thanks Alex, I see it is the same fix as in sage/schemes/generic/algebraic_scheme.py. I know that Robert won't be online today, but hopefully he can take a quick look on Monday. Assuming it passes doctests I plan to merge this patch in the near future.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 02:56:07

Merged in Sage 3.1.2.alpha4


---

Comment by mabshoff created at 2008-09-01 02:56:07

Resolution: fixed
