# Issue 7316: notebook: default values for variables are printed incorrectly in docstrings

Issue created by migration from https://trac.sagemath.org/ticket/7316

Original creator: jhpalmieri

Original creation time: 2009-10-26 23:31:35

Assignee: boothby

CC:  was

From [sage-notebook](http://groups.google.com/group/sage-notebook/browse_frm/thread/28a506759aac37ae):

```
> I notice that in Sage 4.2, the version of sageinspect in the notebook 
> doesn't match the one in sage.misc -- the one in sagenb/misc is 
> missing the fix from Trac #6848.  As a result, 
> {{{ 
> RDF.random_element? 
> }}} 
> produces incorrect output, as noted on the ticket.  Should this be 
> fixed, or was the fix intentionally omitted because it uses "eval"? 
```

For the fix, see the patch at #6848, especially the new lines 269-270 (and the associated doctest fixes).



---

Attachment

Fix Cython docstring "Definition". Rebase of sageinspect part of #6848. Apply to sagenb repository.


---

Comment by mpatel created at 2009-10-27 02:53:36

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-10-27 02:53:36

All doctests pass, if I copy the patched `sagenb.misc.sageinspect.py` to `$SAGE_ROOT/devel/sage/sage`, say, and run `sage -t sageinspect.py` in that directory.

To the extent that it counts, my review is positive.


---

Comment by jhpalmieri created at 2009-10-29 17:22:36

Is this now a duplicate of #7349?


---

Comment by timdumol created at 2009-10-29 18:12:14

Doctests count and the the bugs are fixed. Positive review.


---

Comment by timdumol created at 2009-10-29 18:12:14

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-11 19:49:27

merged into sagenb-0.4.2 (sage-4.2.1)


---

Comment by was created at 2009-11-11 19:49:27

Resolution: fixed
