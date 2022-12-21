# Issue 2248: [with patch, needs trivial review] sage-2.10.2.alpha2: multi_polynomial.pyx doctest failure

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-21 19:01:42

Assignee: failure


```
sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx
**********************************************************************
File "multi_polynomial.pyx", line 256:
    sage: R(S.0)
Expected:
    BROKEN -- FIX ME
Got:
    p
**********************************************************************
```



---

Comment by mabshoff created at 2008-02-21 19:05:29

fixed the failure as suggested by William


---

Attachment


---

Comment by mabshoff created at 2008-02-21 19:23:31

Merged in Sage 2.10.2.rc0


---

Comment by mabshoff created at 2008-02-21 19:23:31

Resolution: fixed
