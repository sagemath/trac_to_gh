# Issue 9833: LaTeX representation of fractions still broken

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2010-08-28 20:21:05

Assignee: burcin

CC:  burcin

Keywords: latex, fraction, pynac

Similarly as in #9314


```
sage: latex(-(x+1)/(x+2))
\frac{-x + 1}{x + 2}
```


note the minus sign :(


---

Comment by burcin created at 2010-08-28 20:54:57

I fixed this while working on #9394 a while ago. I should have posted a new version of pynac before going on vacation, but couldn't find the time. Hopefully in the next days I'll push my changes to trac for review.


---

Comment by burcin created at 2010-09-12 12:30:17

There is a new pynac version that fixes this at #9901, corresponding doctest fixes are included in the patch at #9394.

This ticket should be closed when those are merged.


---

Comment by kcrisman created at 2010-09-22 17:59:06

With inclusion of #9901, positive review.  Do not merge until #9901 is merged.  Doctests are at #9394.


---

Comment by kcrisman created at 2010-09-22 17:59:06

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-09-22 17:59:15

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-06 03:19:44

Resolution: duplicate
