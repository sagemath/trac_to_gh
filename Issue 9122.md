# Issue 9122: conversions between simplicial and cubical complexes

Issue created by migration from https://trac.sagemath.org/ticket/9122

Original creator: jhpalmieri

Original creation time: 2010-06-03 04:08:25

Assignee: jhpalmieri

CC:  mhampton

This patch implements conversions between simplicial and cubical complexes.  It also implements the following: if you call

```
sage: SimplicialComplex(X)
```

it tests to see if X has a `_simplicial_` method, and if it does, it calls that and returns the answer.  So if anyone wants to convert their favorite Sage object to a simplicial complex, they just have to write a `_simplicial_` method for it; then `SimplicialComplex(blah)` will work.  Same for a `_cubical_` method and cubical complexes.



---

Comment by jhpalmieri created at 2010-06-03 04:14:47

Changing status from new to needs_review.


---

Comment by mhampton created at 2011-03-29 03:37:11

Maybe I am building the docs incorrectly, but it seems kind of sad that the documentation for _simplicial_ and _cubical_ does not show up in the reference manual, and if you look at it in the notebook it is not currently rendered correctly.

Otherwise the functionality appears to be correctly implemented (although I have very little expertise in this area).  The flaws in rendering are probably the fault of the notebook code rather than this patch.


---

Comment by mhampton created at 2011-03-29 03:37:11

Changing status from needs_review to needs_info.


---

Comment by jhpalmieri created at 2011-03-29 03:56:31

Changing status from needs_info to needs_review.


---

Comment by jhpalmieri created at 2011-03-29 03:56:31

Oh, I think it's partly the fault of the patch: the docstrings should start with `r"""`, not just `"""`.  Try this new patch.


---

Attachment


---

Comment by mhampton created at 2011-04-27 21:39:25

All homology tests passed and the documentation looks fixed, so I think this is OK now.


---

Comment by mhampton created at 2011-04-27 21:39:25

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-06-07 08:34:58

Resolution: fixed
