# Issue 7914: Implementation of triangular morphisms for modules with basis

Issue created by migration from https://trac.sagemath.org/ticket/7914

Original creator: jbandlow

Original creation time: 2010-01-12 20:46:47

Assignee: jbandlow

CC:  sage-combinat adrien.boussicault@univ-mlv.fr

Title says it all


---

Comment by jbandlow created at 2010-01-12 20:53:54

Changing status from new to needs_review.


---

Attachment

Depends on #7729.


---

Comment by jbandlow created at 2010-01-28 23:45:43

Apply only the second patch (sorry about the first one).  This was tested on top of sage-4.3.1 +
#7976, #7921, #7938, #8028, #8001, #5524.


---

Comment by jhpalmieri created at 2010-01-31 00:08:10

> Title says it all

Actually, it doesn't: what's a triangular morphism?  A definition (or at the very least a reference) should be in the documentation somewhere.


---

Attachment


---

Attachment


---

Attachment

Nicolas,  I added the patch trac_7914_triangular_morphisms-doc-jb.patch on top of your reviewer patch to fix some documentation issues (replacing 'maximal' with 'minimal' and that sort of thing).  Since the patches got out of order on the ticket, I created trac_7914_folded.patch.  This is all that needs to be applied.  It applies cleanly to sage 4.3.2. and passes tests.  I approve of Nicolas' reviewer changes (which are part of the folded patch), and believe this is ready for merging.  Note: John Palmieri's comments were useful, and have been addressed in the documentation.


---

Comment by hivert created at 2010-03-20 11:20:26

I've rebased the patch on the sage-combinat queue. since there was a conflict with #8492. Please check are re-upload.


---

Comment by nthiery created at 2010-03-22 20:39:00

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-03-22 20:39:00

Hi!

Sorry it took me so long to get on this one. Your changes are good. All test pass on sag.math.
Positive review!

And thanks so much for your work on this feature.


---

Comment by nthiery created at 2010-03-24 09:11:34

Apply only this one (includes the rebasing by Florent)


---

Attachment

I found a small but critical bug when actually trying to use this.  The __invert__ method incorrectly defines 'domain' and 'codomain'.  Fix coming shortly.


---

Comment by jbandlow created at 2010-04-03 00:01:29

Changing status from positive_review to needs_work.


---

Attachment

Apply only this patch.


---

Comment by jbandlow created at 2010-04-03 00:08:18

Changing status from needs_work to needs_review.


---

Comment by jbandlow created at 2010-04-03 00:08:18

Fixed.  The only change between the new patch and the previous one is line 1076 of modules_with_basis.py, in the `invert` method:


```
-                 domain = self.domain(),               codomain = self.codomain(), 
+                 domain = self.codomain(),             codomain = self.domain(), 
```



---

Comment by nthiery created at 2010-04-03 08:47:20

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-04-03 08:47:20

Replying to [comment:8 jbandlow]:
> Fixed.  The only change between the new patch and the previous one is line 1076 of modules_with_basis.py, in the `invert` method:
> 
> {{{
> -                 domain = self.domain(),               codomain = self.codomain(), 
> +                 domain = self.codomain(),             codomain = self.domain(), 
> }}}

Yes, Adrien had noticed this, and was about to fix it in the Sage-Combinat
queue. Since this patch is not yet in Sage, I agree that it's best to
include the fix right away in it. Positive review!


---

Comment by jhpalmieri created at 2010-04-15 06:00:16

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 06:00:16

Merged in 4.4.alpha0:

 - trac_7914_rebased_fixed.patch
