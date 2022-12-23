# Issue 647: create a quaternion algebra element class

Issue created by migration from https://trac.sagemath.org/ticket/647

Original creator: was

Original creation time: 2007-09-13 14:07:10

Assignee: somebody

From Alex Ghitza:


```
I fiddled a bit more with the quaternion algebras, this time with
elements.  This is still warm-up for doing something more serious with
orders and ideals, starting with implementing the code by
Rodriguez-Villegas et al.
```


See attached patch.


---

Attachment


---

Comment by was created at 2007-09-13 14:08:02

The main thing that needs to happen to close this ticket is that 1-2 people need to look at this patch
and say "yep, looks good".


---

Comment by was created at 2007-09-13 14:08:59

OK, I just looked at it, and it *has* no doctests at all for the new functions it introduces.  Please add these.


---

Attachment

I inserted doctests and attached the new version newquatalgelm.hg.


---

Comment by was created at 2007-09-20 23:48:15

Resolution: fixed
