# Issue 4195: [with patch, needs review] implicit plotting for multivariate polynomial ideals

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-09-25 12:09:01

Assignee: was

CC:  wdj

Keywords: plotting, ideal, polynomial

This now works without having surf installed:

```
sage: R.<x,y> = PolynomialRing(QQ,2)
sage: I = R.ideal([y^3 - x^2])
sage: I.plot()
sage: I = R.ideal([y^2 - x^2 - 1])
```



---

Attachment

I'm CCing wdj as he wrote the original plotting code.


---

Comment by mhansen created at 2008-09-25 19:10:27

Looks good to me.


---

Comment by mabshoff created at 2008-09-26 05:08:24

Merged in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-26 05:08:24

Resolution: fixed
