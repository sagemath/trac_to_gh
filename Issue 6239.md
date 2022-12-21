# Issue 6239: fix ReST formatting for pydesign module ext_rep

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-06-07 06:11:40

Assignee: tba

CC:  carlohamalainen wdj

Keywords: ReST, ext_rep.py

This is a follow up to #6093. The patch on that ticket adds documentation to the pydesign module ext_rep. However, some of the formatting of the docstrings doesn't follow ReST formatting, hence doesn't show up nicely in the HTML and PDF versions. The module `sage/combinat/designs/ext_rep.py` should also be added to the reference manual.


---

Attachment


---

Comment by carlohamalainen created at 2009-06-15 09:53:19

Changing assignee from tba to carlohamalainen.


---

Comment by carlohamalainen created at 2009-06-15 09:53:19

The patch applies cleanly to 4.0.1, the formatting looks good, and "sage -docbuild reference html" worked.


---

Comment by carlohamalainen created at 2009-06-15 09:53:19

Changing status from new to assigned.


---

Comment by rlm created at 2009-06-24 09:58:45

Resolution: fixed
