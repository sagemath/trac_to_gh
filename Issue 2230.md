# Issue 2230: sage-2.10.2.alpha1 -- linear algebra hash not implemented

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-20 07:04:30

Assignee: was

This was my fault, caused by me not having a 64-bit install to test on when I implemented the patch.  Just fix it by putting the correct answer in under #64-bit

```
         [1.3 s]
sage -t  devel/sage-main/sage/modules/quotient_module.py    **********************************************************************
File "quotient_module.py", line 130:
    sage: hash(Q)
Expected:
    fixme
Got:
    -5856620741060301410
**********************************************************************
File "quotient_module.py", line 135:
    sage: hash((V, W))
Expected:
    fixme
Got:
    -5856620741060301410
**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_3
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_quotient_module.py
         [1.7 s]

```



---

Attachment


---

Comment by mabshoff created at 2008-02-21 18:37:44

Patch is simple enough, positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 18:52:27

Merged in Sage 2.10.2.rc0


---

Comment by mabshoff created at 2008-02-21 18:52:27

Resolution: fixed
