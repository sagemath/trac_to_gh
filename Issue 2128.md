# Issue 2128: bug in random_prime (trivial to fix!)

Issue created by migration from https://trac.sagemath.org/ticket/2128

Original creator: was

Original creation time: 2008-02-09 19:26:29

Assignee: was


```
The function

 random_prime(n)

returns differing types of objects. When n is 2, it returns a Sage
integer. When n is > 2, it returns a Python integer. A look at the
source code gives the impression that it should return a Sage
integer.

Perhaps devel/sage-main/sage/rings/arith.py line 907 should be
changed from
   return p
to
   return integer_ring.ZZ(p)

 -- Kate Minola
```



---

Comment by AlexGhitza created at 2008-02-17 01:51:47

Implemented the change in the patch.


---

Comment by mabshoff created at 2008-02-17 17:26:10

The patch looks good, but I would suggest a doctest that checks the type of the return value for n=2 and some n>2.

Cheers,

Michael


---

Attachment

I've added the doctests and replaced the patch.


---

Comment by mabshoff created at 2008-02-17 23:36:09

Updated patch looks good.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 23:36:25

Resolution: fixed


---

Comment by mabshoff created at 2008-02-17 23:36:25

Merged in Sage 2.10.2.alpha1
