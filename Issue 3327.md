# Issue 3327: missing .divides() implementation for FieldElement

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-05-29 03:18:28

Assignee: somebody

The generic .divides() implementation doesn't work for FieldElement; this causes the following problem:

```
  R.<a,b> = NumberField(x^2-3,'g')[]
  S.<y> = R.fraction_field()[]
  xgcd(y^2, a*y+b) 
```

goes BOOM (as reported by Gaëtan Bisson here: http://groups.google.com/group/sage-support/browse_thread/thread/5338608bd7508b00/76dd56341dc29b1b#76dd56341dc29b1b)

The attached patch adds the missing method and some doctests.


---

Attachment


---

Comment by was created at 2008-05-29 03:29:36

I tried it out and it works.  I read the code and it looks great!


---

Comment by cremona created at 2008-05-29 08:04:05

Agreed.  ++


---

Comment by mabshoff created at 2008-05-29 13:44:53

Resolution: fixed


---

Comment by mabshoff created at 2008-05-29 13:44:53

Merged in Sage 3.0.3.alpha1
