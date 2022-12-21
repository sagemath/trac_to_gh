# Issue 7938: 'term' and 'monomial' are inconsistently used in some Category and combinat code

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2010-01-15 18:50:38

Assignee: AlexGhitza

CC:  sage-combinat

I'm including a patch, but will rebase it against 3.4.1 once it is released.


---

Attachment


---

Comment by jbandlow created at 2010-01-15 18:51:38

Changing status from new to needs_work.


---

Comment by jbandlow created at 2010-01-15 18:51:38

Changing component from algebra to categories.


---

Comment by nthiery created at 2010-01-17 21:34:51

This change has been discussed and approved on sage-devel and sage-combinat-devel. I went through the current patch and it looks good. This is a conditional positive review, pending a rebase on 4.3.1 (if at all needed), a recheck of all tests passing, and two little details:

 - Renaming the patch to trac_7938_swap_term_and_monomial-jb.patch
 - Adding a short description on top of it; say something like: "#7938: swap term and monomial in category and combinat code for consistency with the rest of sage"

Thanks Jason!


---

Comment by nthiery created at 2010-01-17 21:44:38

Replying to [comment:2 nthiery]:
Oops, I forgot the following:

  - Removing the spurious change to sage/combinat/crystals/affine.py
  - Adding a default value (the one of the coeff ring) for coeff in the new self.term, to make it backward compatible
  - Only if easy, make the new monomial accept a second optional coeff argument, to make it backward compatible. This could be a bit tricky, since self.monomial is a Map. It is also not as important as for term, since I expect the later to have been used far more more extensively than the former.


---

Attachment

The patch called 'trac_7938_...' is all that should be applied.  In response to Nicolas' comments:
  * Rename patch: done
  * Add description: done
  * Remove spurious change to affine.py: done, but see #7978
  * Add default value for coeff in self.term: done
  * Add optional coeff argument to monomial: Not done yet. I'll look more (but maybe not much more) at this later.


---

Comment by nthiery created at 2010-01-18 21:18:23

Replying to [comment:4 jbandlow]:
> ...

Thanks much!

>   * Add description: done

Sorry for bothering you again. Please also remove the [mq] line, and put the rest on one line (hg treats the first line specifically).

Cheers,


---

Comment by nthiery created at 2010-01-21 18:21:44

It does need a rebase w.r.t. #7729 (iwahori hecke algebra) whose file was renamed.

Please update the queue accordingly (including the #7729 patch).


---

Comment by nthiery created at 2010-01-22 22:13:14

Replying to [comment:6 nthiery]:
> It does need a rebase w.r.t. #7729 (iwahori hecke algebra) whose file was renamed.
> 
> Please update the queue accordingly (including the #7729 patch).

Done!


---

Comment by nthiery created at 2010-01-23 10:06:14

Rebased for 4.3.1


---

Comment by nthiery created at 2010-01-23 10:07:04

Changing status from needs_work to needs_review.


---

Attachment

> Sorry for bothering you again. Please also remove the [mq] line, and put the rest on one line (hg treats the first line specifically).

Done. Patch ready for merging into Sage.


---

Comment by nthiery created at 2010-01-23 10:07:21

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-23 10:50:36

Resolution: fixed


---

Comment by mvngu created at 2010-01-23 10:50:36

Merged [trac_7938_swap_term_and_monomial-jb.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7938/trac_7938_swap_term_and_monomial-jb.2.patch).
