# Issue 753: derivative alias for diff

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-09-25 18:30:04

Assignee: was

For all polynomials and mpolynomials


---

Comment by mhansen created at 2007-11-30 23:36:18

Changing status from new to assigned.


---

Comment by mhansen created at 2007-11-30 23:36:18

Changing assignee from was to mhansen.


---

Comment by dmharvey created at 2008-01-02 19:12:18

arrggh this is a bit of a mess currently. All the types seem to behave differently at the moment. Some standardisation is really needed here, and things pulled back closer to the base classes. Examples:


```
sage: x = var("x")
sage: type(x)
<class 'sage.calculus.calculus.SymbolicVariable'>
sage: x.diff()
1
sage: x.derivative()
1
sage: x.differentiate()
1

sage: R.<x> = PolynomialRing(ZZ)
sage: x.derivative()
1
sage: x.diff()
[boom]

sage: R.<x> = PolynomialRing(QQ)
sage: x.diff()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/dmharvey/<ipython console> in <module>()

<type 'exceptions.TypeError'>: diff() takes at least 2 arguments (1 given)
sage: x.derivative()
1
```



---

Comment by dmharvey created at 2008-02-28 02:58:04

Attached patch revamps all derivative functions in sage, and also covers #756 and #1578.

This has been tested (sort of) on 2.10.2.

I'm now going to try against mabshoff's pseudo-2.10.3.rc0.

I'm not sure whether this should be targeted at 2.10.3 or 2.10.4.


---

Comment by dmharvey created at 2008-02-28 02:58:04

Changing status from assigned to new.


---

Comment by dmharvey created at 2008-02-28 02:58:04

Changing assignee from mhansen to dmharvey.


---

Comment by dmharvey created at 2008-02-28 02:58:04

Changing priority from minor to major.


---

Attachment


---

Attachment

I've added an additional file derivative2.patch which incorporates a missing file (derivative.pyx)


---

Attachment

Looks good to me!  "sage -testall" passes, code and doctests look good.  I added a patch that changes some indirect doctests to direct doctests, and fixes a 1-character typo.

Apply all three patches.


---

Comment by mhansen created at 2008-03-02 02:54:22

All doctests pass for me too.


---

Comment by mabshoff created at 2008-03-02 18:32:22

Merged all three patches in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-02 18:32:22

Resolution: fixed
