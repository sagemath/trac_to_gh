# Issue 5376: [with patch, needs review] minor problems with ReST in plot.py

Issue created by migration from https://trac.sagemath.org/ticket/5376

Original creator: jhpalmieri

Original creation time: 2009-02-26 00:32:42

Assignee: jhpalmieri

This fixes the last few issues from #4923.



---

Attachment

REFEREE REPORT



The patch *plot-rst.patch* applied OK against 3.4.alpha0 and all doctests passed with the options

```
-t -long -optional
```

The reference manual built OK with the command

```
sage -docbuild reference html
```

Checking the relevant HTML file

```
/path/to/html/en/reference/sage/plot/plot.html
```

I see that the patch fixes the formatting and typo issues. Positive review.


---

Comment by mabshoff created at 2009-02-28 16:25:52

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-28 16:25:52

Resolution: fixed
