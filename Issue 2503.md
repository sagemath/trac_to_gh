# Issue 2503: Sage 2.10.4.alpha4: doctest failout in sage/misc/functional.py from #2421

Issue created by migration from https://trac.sagemath.org/ticket/2503

Original creator: mabshoff

Original creation time: 2008-03-12 21:19:49

Assignee: failure

The following doctest failure in sage/misc/functional.py happends due to #2421:

```
sage -t -long devel/sage-main/sage/misc/functional.py
**********************************************************************
File "functional.py", line 848:
    sage: round(b)
Expected:
    5.0000000000000000
Got:
    5
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_52
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_functional.py
         [5.0 s]
exit code: 256

----------------------------------------------------------------------
```

The fix is obvious - patch coming up.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-03-13 02:54:57

Works for me.


---

Comment by mabshoff created at 2008-03-13 06:01:46

Resolution: fixed


---

Comment by mabshoff created at 2008-03-13 06:01:46

Merged in Sage 2.10.4.alpha0
