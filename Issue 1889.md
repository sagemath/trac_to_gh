# Issue 1889: 2.10.1.alpha2 doctest failure in crypto/mq/sr.py

Issue created by migration from https://trac.sagemath.org/ticket/1889

Original creator: mabshoff

Original creation time: 2008-01-23 07:47:30

Assignee: malb

This is probably related to merging #1817:

```
sage -t  devel/sage-main/sage/crypto/mq/sr.py
**********************************************************************
File "sr.py", line 1364:
    sage: F.groebner_basis()[:4]
Expected:
    [k003 + 1, k001, k000 + k001 + 1, s003 + k002]
Got:
    [k003 + 1, k001, k000 + 1, s003 + k002]
**********************************************************************
File "sr.py", line 1500:
    sage: _= A = sr.random_state_array(); A
Expected nothing
Got:
    [a^3 + 1]
**********************************************************************
File "sr.py", line 1874:
    sage: _= A = sr.random_state_array(); A
Expected nothing
Got:
    [a^3]
**********************************************************************
3 items had failures:
```


Cheers,

Michael


---

Attachment


---

Comment by malb created at 2008-01-23 17:06:07

Yes, it was related to #1817


---

Comment by malb created at 2008-01-23 17:06:07

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-23 22:11:53

Patch looks good to me.


---

Comment by mabshoff created at 2008-01-23 22:12:39

Merged in Sage 2.10.1.alpha2


---

Comment by mabshoff created at 2008-01-23 22:12:39

Resolution: fixed
