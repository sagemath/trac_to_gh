# Issue 6136: (Combinatorial) Free modules: cleanup, abstraction into categories, and functorial constructions

Issue created by migration from https://trac.sagemath.org/ticket/6136

Original creator: nthiery

Original creation time: 2009-05-27 05:11:16

Assignee: nthiery

CC:  sage-combinat

Keywords: free modules, categories, tensor, direct sum

See: http://combinat.sagemath.org/patches/file/tip/categories-freemodule-nt.patch


---

Attachment


---

Comment by nthiery created at 2009-10-24 13:38:20

Changing status from new to needs_review.


---

Attachment

Adds TestSuite.run call, and implements equality for PoorManMap's. Apply only this one.


---

Comment by hivert created at 2009-11-06 15:53:24

Last version of the file from combinat patch server.


---

Comment by hivert created at 2009-11-06 15:53:44

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by hivert created at 2009-11-06 15:56:35

Apply only the last patch trac_6136-categories-freemodule-nt.2.patch

Note: it breaks some doctests which are corrected in #6137 (See http://sagetrac.org/sage_trac/wiki/CategoriesRoadMap)

Ready to go.

Cheers,

 Florent


---

Attachment

Correct version


---

Comment by mhansen created at 2009-11-19 16:59:21

Resolution: fixed
