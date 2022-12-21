# Issue 5375: [with patch, needs review] minor problems with ReST in geometry/lattice_polytope.py

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-02-26 00:22:43

Assignee: jhpalmieri

This fixes the few open problems from ticket #4912.


---

Attachment


---

Comment by jhpalmieri created at 2009-02-26 00:37:33

Changing component from geometry to documentation.


---

Comment by mvngu created at 2009-02-27 07:34:43

REFEREE REPORT



The patch *geom-rst.patch* applied cleanly against 3.4.alpha0 and all doctests passed with the options `-t -long -optional`. The reference manual built fine with

```
sage -docbuild reference html
```

Looking at the relevant HTML file

```
/path/to/reference/sage/geometry/lattice_polytope.html
```

the suggested patch fixed the problem it's intends to. So positive review on my part. Note that there are still a large number of typos in the file that *geom-rst.patch* touches, namely

```
sage/geometry/lattice_polytope.py
```

But please open another ticket for that.


---

Comment by mabshoff created at 2009-02-28 16:24:29

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-28 16:24:29

Resolution: fixed
