# Issue 2445: algebras module lacks many docstrings and tests (score 15.7%)

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-03-09 21:22:10

Assignee: malb

Keywords: algebras modules

Most files in sage/algebras have little or no docstrings and almost no doctests.  This patch makes a start on remedying this, but there is a lot more to be done.



---

Attachment


---

Comment by gfurnish created at 2008-03-10 08:26:33

This does not pass sage -t algebra.py


---

Comment by gfurnish created at 2008-03-10 08:34:34

This just needs a True statement added in the doctest in algebra.py


---

Attachment

Fix for trivial algebra.py failure


---

Comment by mabshoff created at 2008-03-10 13:50:06

Merged both patches in Sage 2.10.3.rc4


---

Comment by mabshoff created at 2008-03-10 13:50:06

Resolution: fixed
