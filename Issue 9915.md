# Issue 9915: Change Shafarevich-Tate in BSD.py (also fixes doctests)

archive/issues_009915.json:
```json
{
    "body": "Assignee: leif\n\nCC:  cremona kcrisman mpatel wuthrich\n\nDue to #9330, some doctests have to be adapted (and also the documentation).\n\nI've **not** changed the name in the in the references' titles of course.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9916\n\n",
    "created_at": "2010-09-16T09:41:21Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Change Shafarevich-Tate in BSD.py (also fixes doctests)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9915",
    "user": "leif"
}
```
Assignee: leif

CC:  cremona kcrisman mpatel wuthrich

Due to #9330, some doctests have to be adapted (and also the documentation).

I've **not** changed the name in the in the references' titles of course.

Issue created by migration from https://trac.sagemath.org/ticket/9916





---

archive/issue_comments_098655.json:
```json
{
    "body": "Apply to Sage library. Based on (not yet released) Sage 4.6.alpha1.",
    "created_at": "2010-09-16T09:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98655",
    "user": "leif"
}
```

Apply to Sage library. Based on (not yet released) Sage 4.6.alpha1.



---

archive/issue_comments_098656.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-16T09:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98656",
    "user": "leif"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098657.json:
```json
{
    "body": "Attachment [trac_9916-fix_Shafarevich-Tate_in_BSD.py.patch](tarball://root/attachments/some-uuid/ticket9916/trac_9916-fix_Shafarevich-Tate_in_BSD.py.patch) by leif created at 2010-09-16 09:46:49\n\nPatch is up.",
    "created_at": "2010-09-16T09:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98657",
    "user": "leif"
}
```

Attachment [trac_9916-fix_Shafarevich-Tate_in_BSD.py.patch](tarball://root/attachments/some-uuid/ticket9916/trac_9916-fix_Shafarevich-Tate_in_BSD.py.patch) by leif created at 2010-09-16 09:46:49

Patch is up.



---

archive/issue_comments_098658.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-09-16T21:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98658",
    "user": "mpatel"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_098659.json:
```json
{
    "body": "I can still merge this into 4.6.alpha1, while I wait for a response to a build error at #4000.",
    "created_at": "2010-09-16T22:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98659",
    "user": "mpatel"
}
```

I can still merge this into 4.6.alpha1, while I wait for a response to a build error at #4000.



---

archive/issue_comments_098660.json:
```json
{
    "body": "Are the stack size warnings expected here:\n\n```python\nsage -t -long  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\n  ***   Warning: new stack size = 1003360 (0.957 Mbytes).\n  ***   Warning: new stack size = 1003360 (0.957 Mbytes).\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\", line 4805:\n    sage: S\nExpected:\n    Shafarevich-Tate group for the Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field\nGot:\n    Tate-Shafarevich group for the Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field\n```\n\n?",
    "created_at": "2010-09-16T23:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98660",
    "user": "mpatel"
}
```

Are the stack size warnings expected here:

```python
sage -t -long  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
  ***   Warning: new stack size = 1003360 (0.957 Mbytes).
  ***   Warning: new stack size = 1003360 (0.957 Mbytes).
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py", line 4805:
    sage: S
Expected:
    Shafarevich-Tate group for the Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
Got:
    Tate-Shafarevich group for the Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
```

?



---

archive/issue_comments_098661.json:
```json
{
    "body": "Ooops, some kind of \"recursive\" doctest failure? I must have tested just those files that *previously* failed.\n\nI can upload a second patch for that, too, which in addition fixes one occurrence (documentation only) in `.../elliptic_curves/padic_lseries.py` as well.\n\nJust let me know if you already fixed that elsewhere.\n\n(I've seen those stack warnings before, but only when a doctest fails IIRC.)",
    "created_at": "2010-09-17T00:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98661",
    "user": "leif"
}
```

Ooops, some kind of "recursive" doctest failure? I must have tested just those files that *previously* failed.

I can upload a second patch for that, too, which in addition fixes one occurrence (documentation only) in `.../elliptic_curves/padic_lseries.py` as well.

Just let me know if you already fixed that elsewhere.

(I've seen those stack warnings before, but only when a doctest fails IIRC.)



---

archive/issue_comments_098662.json:
```json
{
    "body": "By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.",
    "created_at": "2010-09-17T00:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98662",
    "user": "mpatel"
}
```

By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.



---

archive/issue_comments_098663.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> I can upload a second patch for that, too, which in addition fixes one occurrence (documentation only) in `.../elliptic_curves/padic_lseries.py` as well.\n\nCould you add the patch?  I haven't fixed this elsewhere.  Thanks for opening this ticket.",
    "created_at": "2010-09-17T00:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98663",
    "user": "mpatel"
}
```

Replying to [comment:7 leif]:
> I can upload a second patch for that, too, which in addition fixes one occurrence (documentation only) in `.../elliptic_curves/padic_lseries.py` as well.

Could you add the patch?  I haven't fixed this elsewhere.  Thanks for opening this ticket.



---

archive/issue_comments_098664.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.\n\n? What do you think mine came from? ;-) Or did you mean the **absent reviewers**?\n\n(Cron ignores \"README_first\"...)\n\nSo I'll upload a second patch in a few seconds.",
    "created_at": "2010-09-17T00:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98664",
    "user": "leif"
}
```

Replying to [comment:8 mpatel]:
> By the way, the unofficial, trial 4.6.alpha1 is in `/home/release/sage-4.6.alpha1` on the Sage cluster.

? What do you think mine came from? ;-) Or did you mean the **absent reviewers**?

(Cron ignores "README_first"...)

So I'll upload a second patch in a few seconds.



---

archive/issue_comments_098665.json:
```json
{
    "body": "Attachment [trac_9916-fix_Shafarevich-Tate_in_ell_rat_field_and_padic_lseries_too.patch](tarball://root/attachments/some-uuid/ticket9916/trac_9916-fix_Shafarevich-Tate_in_ell_rat_field_and_padic_lseries_too.patch) by leif created at 2010-09-17 01:06:57\n\nApply to Sage library. Based on (not yet released) Sage 4.6.alpha1.",
    "created_at": "2010-09-17T01:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98665",
    "user": "leif"
}
```

Attachment [trac_9916-fix_Shafarevich-Tate_in_ell_rat_field_and_padic_lseries_too.patch](tarball://root/attachments/some-uuid/ticket9916/trac_9916-fix_Shafarevich-Tate_in_ell_rat_field_and_padic_lseries_too.patch) by leif created at 2010-09-17 01:06:57

Apply to Sage library. Based on (not yet released) Sage 4.6.alpha1.



---

archive/issue_comments_098666.json:
```json
{
    "body": "Second patch is up; now passes *all* doctests in `sage/schemes/elliptic_curves` (for me).\n\n(Apply both.)",
    "created_at": "2010-09-17T01:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98666",
    "user": "leif"
}
```

Second patch is up; now passes *all* doctests in `sage/schemes/elliptic_curves` (for me).

(Apply both.)



---

archive/issue_comments_098667.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T03:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98667",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098668.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-17T03:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98668",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_098669.json:
```json
{
    "body": "Apologies for my bad work on #9330 which caused all this to happen. Thanks for fixing it.\n\n-- Chris.",
    "created_at": "2010-09-17T17:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98669",
    "user": "wuthrich"
}
```

Apologies for my bad work on #9330 which caused all this to happen. Thanks for fixing it.

-- Chris.



---

archive/issue_comments_098670.json:
```json
{
    "body": "Replying to [comment:16 wuthrich]:\n> Apologies for my bad work on #9330 which caused all this to happen. Thanks for fixing it.\n\nNever mind. If only all doctest failures (or bugs) were that trivial to fix...\n\nI just cc'ed all of you to get this reviewed as quick as possible, not to blame anyone.",
    "created_at": "2010-09-17T18:49:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98670",
    "user": "leif"
}
```

Replying to [comment:16 wuthrich]:
> Apologies for my bad work on #9330 which caused all this to happen. Thanks for fixing it.

Never mind. If only all doctest failures (or bugs) were that trivial to fix...

I just cc'ed all of you to get this reviewed as quick as possible, not to blame anyone.



---

archive/issue_comments_098671.json:
```json
{
    "body": "Replying to [comment:17 leif]:\n> Replying to [comment:16 wuthrich]:\n> > Apologies for my bad work on #9330 which caused all this to happen. Thanks for fixing it.\n> \n> Never mind. If only all doctest failures (or bugs) were that trivial to fix...\n\nHey, I reviewed that patch, and it was merged!  So there are at least three to blame :)\n\nI wonder why it didn't cause any failures for me...  Anyway, thanks for looking into this so quickly.",
    "created_at": "2010-09-17T19:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98671",
    "user": "kcrisman"
}
```

Replying to [comment:17 leif]:
> Replying to [comment:16 wuthrich]:
> > Apologies for my bad work on #9330 which caused all this to happen. Thanks for fixing it.
> 
> Never mind. If only all doctest failures (or bugs) were that trivial to fix...

Hey, I reviewed that patch, and it was merged!  So there are at least three to blame :)

I wonder why it didn't cause any failures for me...  Anyway, thanks for looking into this so quickly.



---

archive/issue_comments_098672.json:
```json
{
    "body": "For what it's worth: I was aware of the doctest errors here and that at #9924, when I merged their \"parent\" tickets into a trial 4.6.alpha1.  Were it not for the more serious build errors caused by #9733 and #4000, I would have announced this as alpha1 on sage-release with links to new tickets for known problems.",
    "created_at": "2010-09-17T23:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9915#issuecomment-98672",
    "user": "mpatel"
}
```

For what it's worth: I was aware of the doctest errors here and that at #9924, when I merged their "parent" tickets into a trial 4.6.alpha1.  Were it not for the more serious build errors caused by #9733 and #4000, I would have announced this as alpha1 on sage-release with links to new tickets for known problems.
