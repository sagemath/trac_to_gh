# Issue 2252: sage 2.10.2.rc0: rings/number_field/number_field_ideal.py failure

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-21 19:33:49

Assignee: craigcitro


```
sage -t -long devel/sage-main/sage/rings/number_field/number_field_ideal.py
**********************************************************************
File "number_field_ideal.py", line 868:
    sage: I.prime_factors()
Expected:
    [Fractional ideal (w)]
Got:
    [Fractional ideal (-w)]
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_32
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_number_field_ideal.py
         [6.6 s]
exit code: 256
```



---

Attachment


---

Comment by craigcitro created at 2008-02-22 00:05:38

The answer is still mathematically correct, and it's what sage is producing, so there's nothing "wrong" with it. However, there's something slightly unsavory (for me) about this -- tracing through the code, Pari doesn't seem to be producing the minus sign. I'm not sure where it's coming from.


---

Comment by craigcitro created at 2008-02-22 00:05:38

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-22 00:26:16

Resolution: fixed


---

Comment by mabshoff created at 2008-02-22 00:26:16

Merged in Sage 2.10.2.rc0
