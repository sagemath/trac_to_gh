# Issue 2228: sage-2.10.2.alpha1 -- fractional ideal doctest failure -- output is equivalent

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-20 07:02:49

Assignee: was


```
sage -t  devel/sage-main/sage/rings/number_field/number_field_ideal.py**********************************************************************
File "number_field_ideal.py", line 203:
    sage: I = K.factor_integer(17)[0][0]; I
Expected:
    Fractional ideal (100*a^2 - 730*a + 5329)
Got:
    Fractional ideal (-100*a^2 + 730*a - 5329)
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctes
```


The output above is completely valid.  Just change the output.


---

Comment by mabshoff created at 2008-02-20 13:38:23

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-02-20 13:38:23

Changing status from new to assigned.


---

Attachment

Fix doctest as indicated by William


---

Comment by jason created at 2008-02-20 14:34:29

looks good.


---

Comment by mabshoff created at 2008-02-20 14:37:37

Merged in Sage 2.10.2.alpha2


---

Comment by mabshoff created at 2008-02-20 14:37:37

Resolution: fixed
