# Issue 5705: [with patch, needs review] homogenize() does not respect the rule that parents are unique

Issue created by migration from https://trac.sagemath.org/ticket/5705

Original creator: malb

Original creation time: 2009-04-07 11:33:45

Assignee: malb

so far `homogenize()` would always create a new parent if the variable was not in the current parent. It should make sure that it reuses a previously created parent if available.


---

Attachment

Indeed, without the patch, we have

```
sage: R=PolynomialRing(QQ,'x',5)
sage: p=R.random_element()
sage: q1=p.homogenize()
sage: q2=p.homogenize()
sage: q1.parent() is q2.parent()
False
```


With the patch, that cleanly applies, we have

```
sage: R=PolynomialRing(QQ,'x',5)
sage: p=R.random_element()
sage: q1=p.homogenize()
sage: q2=p.homogenize()
sage: q1.parent() is q2.parent()
True
```


So, I give it a positive review.


---

Comment by mabshoff created at 2009-04-09 07:33:51

Hmm, I am happy to merge this provided someone post a doctest. With this patch applied doctests do pass. 3.4.1.rc2 will drop in about 18 hours, so there should be plenty of time.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-04-09 08:17:59

Apply the new patch after the old one.  It just adds Simon's test as a doctest.


---

Comment by AlexGhitza created at 2009-04-09 08:18:25

apply after the first patch


---

Attachment

Merged both patches in Sage 3.4.1.rc2. Thanks Alex.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 08:45:36

Resolution: fixed


---

Comment by malb created at 2009-04-09 08:47:02

Thanks Alex
