# Issue 2111: [with patch, needs review] Gröbner bases over any field

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-08 12:17:23

Assignee: malb

CC:  zimmerma

This now works (but is very very slow):


```
sage: R.<x,y> = PolynomialRing(GF(2147483659),order='lex')
sage: ideal([x^3-2*y^2,3*x+y^4]).groebner_basis()
[x + 1431655773*y^4, y^12 + 54*y^2]
```



---

Attachment


---

Attachment

misc additional improvements, apply after first patch


---

Comment by ncalexan created at 2008-02-15 03:54:47

Both patches look good, there's a lot to like in the first patch.  Apply!

I personally prefer long outputs of doctests to be all one line -- I find it makes it easier to find errors -- but that's no reason to reject a good patch :)


---

Comment by mabshoff created at 2008-02-15 04:54:47

Merged in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-15 04:54:47

Resolution: fixed
