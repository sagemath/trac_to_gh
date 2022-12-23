# Issue 2596: Sage 2.11.alpha0: sage/plot/plot.py doctest failure

Issue created by migration from https://trac.sagemath.org/ticket/2596

Original creator: mabshoff

Original creation time: 2008-03-19 13:31:01

Assignee: failure


```
sage -t -long devel/sage/sage/plot/plot.py
----------------------------------------------------------------------
Total time for all tests: 965.6 seconds
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha0$ ./sage -t -long devel/sage/sage/plot/plot.py
sage -t -long devel/sage-main/sage/plot/plot.py
**********************************************************************
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



---

Comment by mabshoff created at 2008-03-22 22:19:14

Mmh, somehow I opened the same ticket twice. This is a dupe of #2583.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 22:19:14

Resolution: duplicate


---

Comment by mabshoff created at 2008-03-22 22:27:52

Resolution changed from duplicate to 


---

Comment by mabshoff created at 2008-03-22 22:27:52

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-03-22 22:27:52

Ooops, I ended up pasting the wrong doctest failure into the description. Since it now has the corrected version I am reopening this.

Cheers,

Michael


---

Comment by jason created at 2008-03-24 14:11:46

The returned output is correct, so it should be included in the doctest.

"99 points" should be replaced with "...", I think, since sometimes it will be "100 points" (due to random shifts in the points).  We could just set randomize=False, but that would make for a more confusing example, I think.


---

Attachment


---

Comment by mabshoff created at 2008-03-28 07:24:21

Patch looks good to me. Positive review.


---

Comment by mabshoff created at 2008-03-28 07:25:28

Resolution: fixed


---

Comment by mabshoff created at 2008-03-28 07:25:28

Merged in Sage 2.11.alpha2
