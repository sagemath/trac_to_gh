# Issue 2744: make symbolicequations deal with logical combinations

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-31 21:10:09

Assignee: was

It would be nice if the following worked


```
sage: f=(x<0) | (x>5)
sage: f.subs(x=6)
(6<0) | (6>5)
sage: bool(f.subs(x=6))
True
sage: f= ~(x==2)
sage: bool(f.subs(x=0))
True


---

Comment by burcin created at 2009-04-16 11:26:47

#2778 was a duplicate of this.
