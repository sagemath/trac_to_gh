# Issue 2583: Sage 2.11.a0: doctest failure in plot.py due to #2580

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-18 11:27:43

Assignee: rlm


```
sage -t -long devel/sage/sage/plot/plot.py
----------------------------------------------------------------------
Total time for all tests: 965.6 seconds
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha0$ ./sage -t -long devel/sage/sage/plot/plot.py
sage -t -long devel/sage-main/sage/plot/plot.py             **********************************************************************
File "plot.py", line 3860:
    sage: networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=0)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_118[17]>", line 1, in <module>
        networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=Integer(0))###line 3860:
    sage: networkx_plot(C._nxg, pos=C.get_pos(), edge_colors=edge_colors, vertex_labels=False, vertex_size=0)
    AttributeError: 'Graph' object has no attribute '_nxg'
**********************************************************************
1 items had failures:
   1 of  18 in __main__.example_118
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_plot.py
         [68.5 s]
exit code: 256
```


As a reminder: Ye Shall doctest the all of Sage before submitting any patch that changes fundamental things.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-03-19 00:38:54

Patch looks good to me and fixes the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-19 00:39:38

Merged in Sage 2.11.alpha0


---

Comment by mabshoff created at 2008-03-19 00:39:38

Resolution: fixed


---

Comment by mabshoff created at 2008-03-19 10:13:22

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-03-19 10:13:22

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-03-19 10:13:22

But it causes a new doctest failure:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha0$ ./sage -t -long devel/sage/sage/plot/plot.py
sage -t -long devel/sage-main/sage/plot/plot.py             File "plot.py", line 3513:
    sage: plot(x^(1/3), (x,-1,1))
Expected nothing
Got:
    WARNING: When plotting, failed to evaluate function at 99 points.
    Last error message: 'negative number cannot be raised to a fractional power'
    <BLANKLINE>
**********************************************************************
1 items had failures:
   2 of  28 in __main__.example_111
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_plot.py
         [70.3 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:

```

so I am reopening it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-19 13:29:34

This is unrelated to this patch and hence we will close it and open another ticket for it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-19 13:29:34

Resolution: fixed
