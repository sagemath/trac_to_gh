# Issue 1881: Sage 2.10.1.alpha0: tut.tex doctes failure with factorize()

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-21 22:00:18

Assignee: mabshoff

Initially reported by Jaap:

```
sage -t  tut.tex                                            
**********************************************************************
File "tut.py", line 3574:
    : factor(f)
Expected:
    9 * (-x^5 + y^2)^2 * (x^6 - 2*x^3*y^2 - x^2*y^3 + y^4)
Got:
    (9) * (-x^5 + y^2)^2 * (x^6 - 2*x^3*y^2 - x^2*y^3 + y^4)
**********************************************************************
```




---

Comment by was created at 2008-01-21 22:16:36

This is likely the "fault" of Ncalexan's recent changes to factorize.py.  
I'm not sure this change is bad though -- it's probably good using parens for
the unit part.  Though it looks dumb in this case.


---

Attachment

You are right, it does look dumb, but this seems to be fallout from #1391, i.e. "bug in unit part of factorizations of multivariate polynomials". At least malb did fix a doctest in that patch in the same fashion. Care to review this trivial patch?

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-22 01:44:26

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-22 01:44:26

Resolution: fixed
