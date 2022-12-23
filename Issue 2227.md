# Issue 2227: sage-2.10.2.alpha1 -- doctest broken in sageinspect.py because I added a new option

Issue created by migration from https://trac.sagemath.org/ticket/2227

Original creator: was

Original creation time: 2008-02-20 07:01:40

Assignee: failure


```
	 [8.8 s]
sage -t  devel/sage-main/sage/misc/sageinspect.py           **********************************************************************
File "sageinspect.py", line 412:
    sage: sage_getdef(sage.rings.integer.Integer.factor, obj_name='factor')
Expected:
    "factor(algorithm='pari', proof='True')"
Got:
    "factor(algorithm='pari', proof='True', limit='None')"
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_10
***Test Failed*** 1 failures.

```


FIX -- just change the doctest -- this makes perfect sense.
(I added a new limit option to factor).


---

Comment by mabshoff created at 2008-02-20 13:38:28

Changing assignee from failure to mabshoff.


---

Comment by mabshoff created at 2008-02-20 13:38:28

Changing status from new to assigned.


---

Attachment

Fix doctest as indicated by William


---

Comment by jason created at 2008-02-20 14:34:07

looks good.


---

Comment by mabshoff created at 2008-02-20 14:36:44

Merged in Sage 2.10.2.alpha2


---

Comment by mabshoff created at 2008-02-20 14:36:44

Resolution: fixed
