# Issue 4770: [with patch, needs review] implement maxima.cputime()

Issue created by migration from https://trac.sagemath.org/ticket/4770

Original creator: malb

Original creation time: 2008-12-12 16:34:29

Assignee: malb

This should work:


```
sage: t = maxima.cputime()
sage: _ = maxima.de_solve('diff(y,x,2) + 3*x = y', ['x','y'], [1,1,1])
sage: maxima.cputime(t)
0.568913
```



---

Attachment


---

Comment by SimonKing created at 2009-01-24 16:37:05

Changing keywords from "" to "maxima, cputime".


---

Comment by SimonKing created at 2009-01-24 16:37:05

The patch applies cleanly, the doc test example works as expected, and it provides a useful functionality.

Hence, positive review!


---

Comment by mabshoff created at 2009-01-28 16:16:11

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 16:16:11

Merged in Sage 3.3.alpha3.

Cheers,

Michael
