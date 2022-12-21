# Issue 2064: foo?? doesn't know about cpdef from the command line

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-02-05 21:38:25

Assignee: ncalexan

CC:  jhpalmieri robertwb

If you cpdef a function foo, and do foo?? from the command line, it displays both foo and the next function after it.


---

Comment by AlexGhitza created at 2008-02-16 17:28:45

Changing component from algebraic geometry to misc.


---

Comment by AlexGhitza created at 2009-01-23 02:46:02

Changing type from defect to enhancement.


---

Comment by mpatel created at 2010-02-02 04:49:29

Recognize Cython tokens in source-code introspection.  *sage* repository.


---

Comment by mpatel created at 2010-02-02 04:57:40

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-02 04:57:40

Changing type from enhancement to defect.


---

Attachment

I've attached a patch uses a modified `inspect.BlockFinder` to recognize the `cdef` and `cpdef` tokens.  This appears to work for me, but I'm not a Cython expert.

Currently, the notebook has its own `sagenb.misc.sageinspect` and this has diverged in several places from `sage.misc.sageinspect`.  If the approach here is OK, I'll open a separate ticket to reconcile the files and fixes this problem in the notebook.


---

Comment by mpatel created at 2010-02-06 03:01:10

Changing component from misc to documentation.


---

Comment by jhpalmieri created at 2010-02-07 19:52:17

This seems to fix the problem for me (I tried `sage.rings.integer.Integer._act_on??` before and after the patch), but I'm not a Cython expert either.  Robert: can you look at it or suggest some else?


---

Comment by roed created at 2010-02-09 20:02:20

Changing status from needs_review to needs_work.


---

Comment by roed created at 2010-02-09 20:02:20

I looked at the Python inspect module, and this seems like a sane modification.  It works for all of us.  

My main suggestion would be to remove "cdef" from the list of keywords you're looking for.  Since this is introspection, you can't ever see cdef'd functions, and I'm slightly worried that there's some use case where the other uses of that keyword in Cython could trip you up.

Other than that, I'm happy to give it a positive review.


---

Comment by mpatel created at 2010-02-16 21:20:27

Removes "cdef" from keyword list.  Apply only this patch.


---

Attachment

V2 adds only "cpdef" to the token search (or search for tokens).


---

Comment by mpatel created at 2010-02-16 21:23:47

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-02-16 21:31:10

Yep.  Looks fine to me now.


---

Comment by roed created at 2010-02-16 21:31:10

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-17 20:39:46

Resolution: fixed


---

Comment by mvngu created at 2010-02-17 20:39:46

Merged [trac_2064-sage_cpdef_inspect.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/2064/trac_2064-sage_cpdef_inspect.2.patch).
