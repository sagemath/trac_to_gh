# Issue 4288: _magma_init_ bug elliptic curve points

Issue created by migration from https://trac.sagemath.org/ticket/4288

Original creator: robertwb

Original creation time: 2008-10-14 21:11:19

Assignee: was

CC:  was

a test is failing, with _magma_init_(), and I wasn't able to fix it, it seems the _magma_().name() implementation is buggy:

```
File "/usr/local/sage-3.1.2/sage/tmp/ell_point.py", line 1289:
    sage: P._magma_init_()
Expected:
    'EllipticCurve([GF(17)!1,GF(17)!16])![13,4]'
Got:
    '_sage_[2]![_sage_[3],_sage_[4]]'
```



---

Comment by zimmerma created at 2008-10-15 07:08:53

This is related to #4277.


---

Attachment

The attached patch seems to do the trick.  It's wrong to use "magma_name" since that just gives somethin like "sage[0]", while "_magma_init_()" return a string which can be passed to a fresh magma session to create the equivalent object.

#4277 is ok now too.


---

Comment by zimmerma created at 2008-10-19 20:23:14

Note for the release manager: that patch should be applied after that for #4277.


---

Comment by mabshoff created at 2008-10-20 14:03:54

Resolution: fixed


---

Comment by mabshoff created at 2008-10-20 14:03:54

Merged in Sage 3.2.alpha0
