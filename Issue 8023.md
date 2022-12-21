# Issue 8023: doctest in combinat/words/morphism.py creates a file "test.sobj" not in a temporary directory

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-01-21 06:34:37

Assignee: sage-combinat

Doctests in Sage should only create files in temporary directories, like SAGE_TMP.  The attached patch fixes a doctest in sage/combinat/words/morphism.py.


---

Comment by jhpalmieri created at 2010-01-21 06:35:52

Changing status from new to needs_review.


---

Attachment


---

Comment by mhansen created at 2010-01-21 18:17:50

#5155 has a similar fix along with other stuff for preventing stuff to be written to $SAGE_ROOT


---

Comment by jhpalmieri created at 2010-01-21 21:04:51

Replying to [comment:2 mhansen]:
> #5155 has a similar fix along with other stuff for preventing stuff to be written to $SAGE_ROOT

Okay, I'll mark this as a duplicate.


---

Comment by jhpalmieri created at 2010-01-21 21:54:14

Resolution: duplicate
