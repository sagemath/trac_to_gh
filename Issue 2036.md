# Issue 2036: maxima is off by -5 with it's charpoly

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-02-03 04:18:45

Assignee: was


```
sage: matrix(SR, 5, [1..5^2]).charpoly().expand()
-x^5 + 65*x^4 + 250*x^3
sage: matrix(QQ, 5, [1..5^2]).charpoly()
x^5 - 65*x^4 - 250*x^3
```



---

Comment by jason created at 2008-02-04 16:57:32

Maxima defines the charpoly as:

determinant (M - diagmatrix (length (M), x))

See http://maxima.sourceforge.net/docs/manual/en/maxima_25.html#SEC81


---

Comment by was created at 2008-02-04 18:18:22

That's a nonstandard definition so we have to work around it.

William


---

Attachment


---

Comment by mhansen created at 2008-02-07 10:13:24

Looks good to me.


---

Comment by mabshoff created at 2008-02-07 10:27:07

Resolution: fixed


---

Comment by mabshoff created at 2008-02-07 10:27:07

Merged in Sage 2.10.2.alpha0
