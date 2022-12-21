# Issue 8084: fix "show" in the notebook for strings

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-01-26 21:28:05

Assignee: tbd

From [this thread in sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f7961d6de8646b26?tvc=2):

```
when doing in notebook 
sage: show('x^2') 
or 
sage: show(type(factor)) 
I get error Unknown control sequence '\texttt' 
```

There are other problems, too; for example, from the command line (not the notebook), 

```
sage: view(type(factor))
sage: view(identity_matrix)
```

produce odd-looking output -- see the attached pngs.  (The old versions are before the patch, the new ones afterwards.  If you wanted output like the old version of `view(identity_matrix)`, it's probably better to do `browse_sage_doc(identity_matrix)` instead.)

The attached patch should fix these problems.


---

Attachment

output of view(type(factor)) before the patch


---

Comment by jhpalmieri created at 2010-01-26 21:29:05

output of view(type(factor)) after the patch


---

Attachment


---

Comment by jhpalmieri created at 2010-01-28 21:15:57

Changing status from new to needs_review.


---

Comment by robert.marik created at 2010-01-28 22:54:28

Changing status from needs_review to positive_review.


---

Comment by robert.marik created at 2010-01-28 22:54:28

Changing keywords from "" to "latex, jsmath".


---

Comment by robert.marik created at 2010-01-28 22:54:28

Works for me and fixes the problem in Sage 4.3.1. Tests passed. Thanks for the patch.


---

Comment by mvngu created at 2010-01-30 23:47:44

Merged [trac_8084-show.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8084/trac_8084-show.patch).


---

Comment by mvngu created at 2010-01-30 23:47:44

Resolution: fixed
