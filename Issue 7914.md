# Issue 7914: Implementation of triangular morphisms for modules with basis

archive/issues_007914.json:
```json
{
    "body": "Assignee: @jbandlow\n\nCC:  sage-combinat adrien.boussicault@univ-mlv.fr\n\nTitle says it all\n\nIssue created by migration from https://trac.sagemath.org/ticket/7914\n\n",
    "created_at": "2010-01-12T20:46:47Z",
    "labels": [
        "categories",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Implementation of triangular morphisms for modules with basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7914",
    "user": "@jbandlow"
}
```
Assignee: @jbandlow

CC:  sage-combinat adrien.boussicault@univ-mlv.fr

Title says it all

Issue created by migration from https://trac.sagemath.org/ticket/7914





---

archive/issue_comments_068855.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T20:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68855",
    "user": "@jbandlow"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068856.json:
```json
{
    "body": "Attachment [trac_7914_triangular-morphisms-jb.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_triangular-morphisms-jb.patch) by @jbandlow created at 2010-01-12 20:53:54\n\nDepends on #7729.",
    "created_at": "2010-01-12T20:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68856",
    "user": "@jbandlow"
}
```

Attachment [trac_7914_triangular-morphisms-jb.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_triangular-morphisms-jb.patch) by @jbandlow created at 2010-01-12 20:53:54

Depends on #7729.



---

archive/issue_comments_068857.json:
```json
{
    "body": "Apply only the second patch (sorry about the first one).  This was tested on top of sage-4.3.1 +\n#7976, #7921, #7938, #8028, #8001, #5524.",
    "created_at": "2010-01-28T23:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68857",
    "user": "@jbandlow"
}
```

Apply only the second patch (sorry about the first one).  This was tested on top of sage-4.3.1 +
#7976, #7921, #7938, #8028, #8001, #5524.



---

archive/issue_comments_068858.json:
```json
{
    "body": "> Title says it all\n\nActually, it doesn't: what's a triangular morphism?  A definition (or at the very least a reference) should be in the documentation somewhere.",
    "created_at": "2010-01-31T00:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68858",
    "user": "@jhpalmieri"
}
```

> Title says it all

Actually, it doesn't: what's a triangular morphism?  A definition (or at the very least a reference) should be in the documentation somewhere.



---

archive/issue_comments_068859.json:
```json
{
    "body": "Attachment [trac_7914_triangular_morphisms-jb.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_triangular_morphisms-jb.patch) by @jbandlow created at 2010-02-19 19:49:25",
    "created_at": "2010-02-19T19:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68859",
    "user": "@jbandlow"
}
```

Attachment [trac_7914_triangular_morphisms-jb.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_triangular_morphisms-jb.patch) by @jbandlow created at 2010-02-19 19:49:25



---

archive/issue_comments_068860.json:
```json
{
    "body": "Attachment [trac_7914_triangular_morphisms-doc-jb.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_triangular_morphisms-doc-jb.patch) by @jbandlow created at 2010-02-19 19:51:04",
    "created_at": "2010-02-19T19:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68860",
    "user": "@jbandlow"
}
```

Attachment [trac_7914_triangular_morphisms-doc-jb.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_triangular_morphisms-doc-jb.patch) by @jbandlow created at 2010-02-19 19:51:04



---

archive/issue_comments_068861.json:
```json
{
    "body": "Attachment [trac_7914_folded.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_folded.patch) by @jbandlow created at 2010-02-19 20:11:30\n\nNicolas,  I added the patch trac_7914_triangular_morphisms-doc-jb.patch on top of your reviewer patch to fix some documentation issues (replacing 'maximal' with 'minimal' and that sort of thing).  Since the patches got out of order on the ticket, I created trac_7914_folded.patch.  This is all that needs to be applied.  It applies cleanly to sage 4.3.2. and passes tests.  I approve of Nicolas' reviewer changes (which are part of the folded patch), and believe this is ready for merging.  Note: John Palmieri's comments were useful, and have been addressed in the documentation.",
    "created_at": "2010-02-19T20:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68861",
    "user": "@jbandlow"
}
```

Attachment [trac_7914_folded.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_folded.patch) by @jbandlow created at 2010-02-19 20:11:30

Nicolas,  I added the patch trac_7914_triangular_morphisms-doc-jb.patch on top of your reviewer patch to fix some documentation issues (replacing 'maximal' with 'minimal' and that sort of thing).  Since the patches got out of order on the ticket, I created trac_7914_folded.patch.  This is all that needs to be applied.  It applies cleanly to sage 4.3.2. and passes tests.  I approve of Nicolas' reviewer changes (which are part of the folded patch), and believe this is ready for merging.  Note: John Palmieri's comments were useful, and have been addressed in the documentation.



---

archive/issue_comments_068862.json:
```json
{
    "body": "I've rebased the patch on the sage-combinat queue. since there was a conflict with #8492. Please check are re-upload.",
    "created_at": "2010-03-20T11:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68862",
    "user": "@hivert"
}
```

I've rebased the patch on the sage-combinat queue. since there was a conflict with #8492. Please check are re-upload.



---

archive/issue_comments_068863.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-22T20:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68863",
    "user": "@nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068864.json:
```json
{
    "body": "Hi!\n\nSorry it took me so long to get on this one. Your changes are good. All test pass on sag.math.\nPositive review!\n\nAnd thanks so much for your work on this feature.",
    "created_at": "2010-03-22T20:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68864",
    "user": "@nthiery"
}
```

Hi!

Sorry it took me so long to get on this one. Your changes are good. All test pass on sag.math.
Positive review!

And thanks so much for your work on this feature.



---

archive/issue_comments_068865.json:
```json
{
    "body": "Apply only this one (includes the rebasing by Florent)",
    "created_at": "2010-03-24T09:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68865",
    "user": "@nthiery"
}
```

Apply only this one (includes the rebasing by Florent)



---

archive/issue_comments_068866.json:
```json
{
    "body": "Attachment [trac_7914_folded_rebased.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_folded_rebased.patch) by @jbandlow created at 2010-04-03 00:01:29\n\nI found a small but critical bug when actually trying to use this.  The __invert__ method incorrectly defines 'domain' and 'codomain'.  Fix coming shortly.",
    "created_at": "2010-04-03T00:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68866",
    "user": "@jbandlow"
}
```

Attachment [trac_7914_folded_rebased.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_folded_rebased.patch) by @jbandlow created at 2010-04-03 00:01:29

I found a small but critical bug when actually trying to use this.  The __invert__ method incorrectly defines 'domain' and 'codomain'.  Fix coming shortly.



---

archive/issue_comments_068867.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-03T00:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68867",
    "user": "@jbandlow"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068868.json:
```json
{
    "body": "Attachment [trac_7914_rebased_fixed.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_rebased_fixed.patch) by @jbandlow created at 2010-04-03 00:04:46\n\nApply only this patch.",
    "created_at": "2010-04-03T00:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68868",
    "user": "@jbandlow"
}
```

Attachment [trac_7914_rebased_fixed.patch](tarball://root/attachments/some-uuid/ticket7914/trac_7914_rebased_fixed.patch) by @jbandlow created at 2010-04-03 00:04:46

Apply only this patch.



---

archive/issue_comments_068869.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-03T00:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68869",
    "user": "@jbandlow"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068870.json:
```json
{
    "body": "Fixed.  The only change between the new patch and the previous one is line 1076 of modules_with_basis.py, in the `invert` method:\n\n\n```\n-                 domain = self.domain(),               codomain = self.codomain(), \n+                 domain = self.codomain(),             codomain = self.domain(), \n```\n",
    "created_at": "2010-04-03T00:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68870",
    "user": "@jbandlow"
}
```

Fixed.  The only change between the new patch and the previous one is line 1076 of modules_with_basis.py, in the `invert` method:


```
-                 domain = self.domain(),               codomain = self.codomain(), 
+                 domain = self.codomain(),             codomain = self.domain(), 
```




---

archive/issue_comments_068871.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-03T08:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68871",
    "user": "@nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068872.json:
```json
{
    "body": "Replying to [comment:8 jbandlow]:\n> Fixed.  The only change between the new patch and the previous one is line 1076 of modules_with_basis.py, in the `invert` method:\n> \n> {{{\n> -                 domain = self.domain(),               codomain = self.codomain(), \n> +                 domain = self.codomain(),             codomain = self.domain(), \n> }}}\n\nYes, Adrien had noticed this, and was about to fix it in the Sage-Combinat\nqueue. Since this patch is not yet in Sage, I agree that it's best to\ninclude the fix right away in it. Positive review!",
    "created_at": "2010-04-03T08:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68872",
    "user": "@nthiery"
}
```

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

archive/issue_comments_068873.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T06:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68873",
    "user": "@jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_068874.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n- trac_7914_rebased_fixed.patch",
    "created_at": "2010-04-15T06:00:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7914#issuecomment-68874",
    "user": "@jhpalmieri"
}
```

Merged in 4.4.alpha0:

- trac_7914_rebased_fixed.patch
