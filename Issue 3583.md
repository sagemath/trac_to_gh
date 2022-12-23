# Issue 3583: randomness in some worksheet doctests

Issue created by migration from https://trac.sagemath.org/ticket/3583

Original creator: was

Original creation time: 2008-07-07 15:19:22

Assignee: failure

On Debian 64-bit vmware:


```
File "/home/was/build/sage-3.0.4.alpha2/tmp/worksheet.py", line 2677:
    sage: W.interrupt()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/worksheet.py", line 2681:
    sage: W.check_comp()
Expected:
    ('e', None)
Got:
    ('w', Cell 0; in=factor(2^997-1), out=)
**********************************************************************
1 items had failures:
   2 of  10 in __main__.example_85
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/was/build/sage-3.0.4.alpha2/tmp/.doctest_worksheet.py
```





---

Attachment


---

Comment by ncalexan created at 2008-07-07 18:51:34

After brief discussion with wstein in #sage-devel, this looks fine.


---

Comment by was created at 2008-07-07 21:50:02

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 21:51:25

Merged in Sage 3.0.4.rc0
