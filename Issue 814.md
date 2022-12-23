# Issue 814: bug in number field printing

Issue created by migration from https://trac.sagemath.org/ticket/814

Original creator: craigcitro

Original creation time: 2007-10-03 19:36:43

Assignee: was

Notice the following printing bug with `NumberField`:


```

sage: K .<a,b>= NumberField([x^3-2,x^2+1])
sage: K
Number Field in a with defining polynomial x^3 + -2 over its base field

```





---

Comment by was created at 2007-10-04 18:32:16

Changing type from defect to enhancement.


---

Comment by was created at 2007-10-04 18:32:16

NOt a bug.  Changing the + -2 to + 2 would be a nice enhancement.  The issue would be making
poly's over number fields print even more nicely.


---

Comment by was created at 2007-10-19 01:29:34

Resolution: fixed


---

Comment by was created at 2007-10-19 01:29:34

Fixed by making the + - to - substitution more generally, since there are parenthesis.
