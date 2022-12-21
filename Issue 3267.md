# Issue 3267: Sage 3.0.2.alpha1: doctest failure in sage/server/support.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-21 13:55:51

Assignee: failure


```
sage -t -long devel/sage/sage/server/support.py             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.2.rc0/tmp/support.py", line 85:
    sage: sage.server.support.help(numpy.linalg.norm)
Expected:
    <html><table notruncate notracebacks bgcolor="#386074" cellpadding=10 cellspacing=10><tr><td bgcolor="#f5f5f5"><font color="#37546d">
    Help on function norm in module numpy.linalg.linalg:
    ...
    For values ord < 0, the result is, strictly speaking, not a
    mathematical 'norm', but it may still be useful for numerical purposes.
    </font></tr></td></table></html>
Got:
    <html><table notracebacks bgcolor="#386074" cellpadding=10 cellspacing=10><tr><td bgcolor="#f5f5f5"><font color="#37546d">
    &nbsp;&nbsp;&nbsp;<a target='_new' href='cell://docs-1.html'>Click to open help window</a>&nbsp;&nbsp;&nbsp;
    <br></font></tr></td></table></html>
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.2.rc0/tmp/.doctest_support.py
         [2.4 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage/sage/server/support.py
Total time for all tests: 2.4 seconds
```



---

Comment by mabshoff created at 2008-05-21 14:12:00

prototype patch [actually only a diff]


---

Comment by mabshoff created at 2008-05-21 14:14:43

Changing assignee from failure to mabshoff.


---

Comment by mabshoff created at 2008-05-21 14:14:43

Changing status from new to assigned.


---

Attachment

After talking to William in IRC I changed the test to the new, expected error message since we now post a link to the error message instead of the error message itself. I add "..." since the number depends if other help files have been produced since they are not deleted, i.e. "sage/server/docs-0.html" sticks around. See #3265 for that issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 06:08:28

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 06:08:28

Merged in Sage 3.0.2.rc0
