# Issue 1364: 2.8.15.alpha2: sage/modules/quotient_module.py doctest failure

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-02 05:27:03

Assignee: roed


```
sage -t  devel/sage-main/sage/modules/quotient_module.py 
**********************************************************************
File "quotient_module.py", line 130:
    sage: hash(Q)
Expected:
    -1880683406
Got:
    2870563926094318706
**********************************************************************
File "quotient_module.py", line 134:
    sage: hash((V, W))
Expected:
    -1880683406
Got:
    2870563926094318706
**********************************************************************
File "quotient_module.py", line 159:
    sage: cmp(Q1, 5)
Expected:
    1
Got:
    -1
**********************************************************************



---

Attachment


---

Comment by mabshoff created at 2007-12-02 05:49:39

Merged in 2.8.15.alpha2.


---

Comment by mabshoff created at 2007-12-02 05:49:39

Resolution: fixed
