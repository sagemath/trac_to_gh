# Issue 1171: _new() method for quadratic field elements

Issue created by migration from https://trac.sagemath.org/ticket/1171

Original creator: dmharvey

Original creation time: 2007-11-14 22:37:20

Assignee: somebody

`NumberFieldElement_quadratic` should override `_new()` to copy the D attribute from the source object; currently every call to _new() actually calls the base class implementation and then D is copied manually.



---

Attachment


---

Comment by robertwb created at 2007-12-02 09:32:20

Changing status from new to assigned.


---

Comment by robertwb created at 2007-12-02 09:32:20

Changing assignee from somebody to robertwb.


---

Comment by cwitty created at 2007-12-02 20:29:42

Applying this after #1141 means that `NumberFieldElement_quadratic` values will have uninitialized `__fld_numerator` and `__fld_denominator` members.  While this seems not to be a problem now (the doctests do pass), it seems like it could be a problem in the future.  This should either be documented (`"watch out!  __fld_numerator is not initialized in NumberFieldElement_quadratic values!"`) or fixed.

Also, you could remove the TODO from the top of the file :)


---

Comment by robertwb created at 2007-12-03 20:32:58

Currently quadratic field elements don't have __numerator or __denominator (or any other ntl variables) defined, so I'm not sure if this is really an issue. 

See, however, #1385


---

Comment by cwitty created at 2008-02-16 02:04:20

Robert convinced me in email that the patch is fine as-is, but he said it wasn't worth merging this code since #1385 would happen soon and the code would all be rewritten anyway.

Since it's been two months and #1385 hasn't happened, it's time to go ahead and merge this patch; I'm changing my review to positive.  (Note that my positive review is, essentially, from early December; I have not tested that doctests still pass, or even that the patch still applies to a current Sage.)


---

Comment by mabshoff created at 2008-02-16 02:10:58

Merged in Sage 2.10.2.alpha1. Patch applies with minimal offset, running doctests now.


---

Comment by mabshoff created at 2008-02-16 02:10:58

Resolution: fixed


---

Comment by mabshoff created at 2008-02-16 02:14:53

Mmmh, maybe I was too optimistic: This patch does cause some doctest failures in `tut.tex` that potentially indicate much more trouble than it is worth for 2.10.2, so I might still revert the patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 14:17:29

The doctest failure I saw in `tut.tex` seems unrelated to this patch, at least it didn't cause any other doctest failures.

Cheers,

Michael
