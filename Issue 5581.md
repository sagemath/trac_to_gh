# Issue 5581: Face lattices and f-vectors for polytopes; bug fixes for polyhedra.py

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-03-21 17:12:27

Assignee: mhampton

Keywords: polyhedra, face lattice, geometry

This patch adds the important functionality of computing face lattices and f-vectors of polytopes.  In the course of adding these, I found a number of bugs that occur for polyhedra of lower dimensions that are embedded in higher dimensions, which I believe I have fixed.


---

Attachment

adds face lattices and f-vectors to polytopes


---

Comment by mhampton created at 2009-05-20 18:48:37

rebased against 3.4.2 and improved doctests.


---

Attachment

I applied trac_5581_rebase.patch to Sage Version 4.0.alpha0, Release Date: 2009-05-15.  All doctests in sage/geometry passed, and I tried several other examples.  

This patch works with trac_4875_1.patch: the two work together regardless of the order in which they are applied.


---

Comment by mabshoff created at 2009-05-21 02:07:30

Resolution: fixed


---

Comment by mabshoff created at 2009-05-21 02:07:30

Merged trac_5581_rebase.patch only in Sage 4.0.rc0.

Cheers,

Michael
