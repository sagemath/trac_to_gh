# Issue 2564: Sage 2.10.4.rc0: fix numerical noise doctest failure in numerical/optimize.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-17 03:35:40

Assignee: mabshoff

Alex Ghitza reported:

```
sage -t  devel/sage-main/sage/numerical/optimize.py
**********************************************************************
File "optimize.py", line 309:
~    sage: minimize_constrained(f, [[None,None],[4,10]],[5,5])
Expected:
~    (4.854..., 4.854...)
Got:
~    (4.83976831157, 4.83976831157)
**********************************************************************
1 items had failures:
~   1 of  11 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_optimize.py
~         [2.3 s]
exit code: 256 
```


Patch coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-17 03:39:05

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-03-17 03:52:51

For the record: I am not happy that we have to dial down the precision for this computation so much. So if anybody can come up with a numerically more stable example it would be great.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-17 03:53:42

Resolution: fixed


---

Comment by mabshoff created at 2008-03-17 03:53:42

Merged in Sage 2.10.4.final
