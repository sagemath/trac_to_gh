# Issue 4912: convert sage.geometry.* docstrings to Sphinx

Issue created by migration from https://trac.sagemath.org/ticket/4912

Original creator: mhansen

Original creation time: 2009-01-01 22:51:30

Assignee: tba




---

Attachment


---

Attachment


---

Comment by jhpalmieri created at 2009-02-22 00:09:37

lattice_polytope.py, line 2677: "codeLatticePolytope" should be something like ```LatticePolytope``` (not your fault: the original said code{...} instead of \code{...})

same three other places: lines 2715, 2769, 2801

line 3182: change `mn` to something like ``m>n``

Otherwise, it looks good to me.


---

Comment by mabshoff created at 2009-02-24 18:52:49

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 18:52:49

Merged in Sage 3.4.alpha0.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-02-26 15:23:57

See #5375.


---

Comment by mabshoff created at 2009-02-26 16:17:53

Thanks John.

Cheers,

Michael
