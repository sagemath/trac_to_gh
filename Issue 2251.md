# Issue 2251: sage 2.10.2.rc0: rings/number_field/number_field.py doctest failure

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-21 19:32:46

Assignee: craigcitro


```
sage -t -long devel/sage-main/sage/rings/number_field/number_field.py
**********************************************************************
File "number_field.py", line 2619:
    sage: [Plist[i]==K.ideal(pilist[i]) for i in range(len(Plist))]
Expected:
    [True, False, False]
Got:
    [True, False, True]
**********************************************************************
1 items had failures:
   1 of  13 in __main__.example_78
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_number_field.py
         [20.4 s]
exit code: 256
```



---

Attachment

Fixes the doctest to the answer that sage was producing, which is correct. (One can check it within sage, i.e. it's easy to check that the two ideals are equal to one another, and I even double-checked in Pari to make sure we weren't missing something in moving the answer from Pari to Sage.)


---

Comment by craigcitro created at 2008-02-21 23:13:49

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-02-21 23:14:47

Note that the patch says 2252.patch, but it's really for this ticket.


---

Comment by mabshoff created at 2008-02-22 00:59:07

Merged in Sage 2.10.2.rc0


---

Comment by mabshoff created at 2008-02-22 00:59:07

Resolution: fixed
