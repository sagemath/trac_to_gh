# Issue 2538: Sage 2.10.4.rc0: server/notebook/interact.py is broken due to #2530

Issue created by migration from https://trac.sagemath.org/ticket/2538

Original creator: mabshoff

Original creation time: 2008-03-16 01:24:51

Assignee: wstein


```
sage-2.10.4.rc0$ ./sage -t -long devel/sage/sage/server/notebook/interact.py
sage -t -long devel/sage-main/sage/server/notebook/interact.py
**********************************************************************
File "interact.py", line 1641:
    sage: selector([1,2,7], default=2).default()
Expected:
    2
Got:
    1
**********************************************************************
1 items had failures:
   1 of   1 in __main__.example_70
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_interact.py
         [2.9 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:
```



---

Comment by was created at 2008-03-16 02:57:52

The new output, i.e., 1 is definitely now correct.   Feel free to
make this change and close this ticket.


---

Attachment


---

Comment by mabshoff created at 2008-03-16 05:28:04

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-16 05:28:04

Changing assignee from wstein to mabshoff.


---

Comment by mhansen created at 2008-03-16 06:07:17

Looks okay to me.


---

Comment by mabshoff created at 2008-03-16 06:45:28

Resolution: fixed


---

Comment by mabshoff created at 2008-03-16 06:45:28

Merged in Sage 2.10.4.rc0
