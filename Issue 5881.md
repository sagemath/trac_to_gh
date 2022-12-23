# Issue 5881: __cmp__ is random-ish in root_system/type_dual.py also (analog to #5811)

Issue created by migration from https://trac.sagemath.org/ticket/5881

Original creator: mabshoff

Original creation time: 2009-04-23 21:10:28

Assignee: mhansen

This is happening with gcc 4.3.3:

```
sage -t  "devel/sage/sage/combinat/root_system/type_dual.py"
**********************************************************************
File "/home/mariah/sage/sage-3.4.1-x86_64-Linux-fc/devel/sage/sage/combinat/root
_system/type_dual.py", line 43:
   sage: [[x.__cmp__(y) for x in ct] for y in ct]
Expected:
   [[0, 1, -1], [-1, 0, -1], [1, 1, 0]]
Got:
   [[0, 1, 1], [-1, 0, 1], [1, 1, 0]]
**********************************************************************
File "/home/mariah/sage/sage-3.4.1-x86_64-Linux-fc/devel/sage/sage/combinat/root
_system/type_dual.py", line 45:
   sage: sorted(ct)
Expected:
   [['A', 4], A1xB2, B2xA1]
Got:
   [A1xB2, B2xA1, ['A', 4]]
**********************************************************************
```



---

Comment by mhansen created at 2009-04-30 07:52:32

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2009-04-30 09:43:14

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 09:43:28

Resolution: fixed


---

Comment by mabshoff created at 2009-04-30 09:43:28

Mrged in Sage 3.4.2.rc0.

Cheers,

Michael
