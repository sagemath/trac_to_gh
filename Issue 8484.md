# Issue 8484: incremental improvements to prove_BSD

archive/issues_008484.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8484\n\n",
    "created_at": "2010-03-10T02:19:10Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "incremental improvements to prove_BSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8484",
    "user": "rlm"
}
```
Assignee: AlexGhitza



Issue created by migration from https://trac.sagemath.org/ticket/8484





---

archive/issue_comments_076458.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-10T02:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76458",
    "user": "rlm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076459.json:
```json
{
    "body": "Changing component from algebra to elliptic curves.",
    "created_at": "2010-03-10T05:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76459",
    "user": "rlm"
}
```

Changing component from algebra to elliptic curves.



---

archive/issue_comments_076460.json:
```json
{
    "body": "Attachment [trac_8484.patch](tarball://root/attachments/some-uuid/ticket8484/trac_8484.patch) by rlm created at 2010-03-11 01:17:43",
    "created_at": "2010-03-11T01:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76460",
    "user": "rlm"
}
```

Attachment [trac_8484.patch](tarball://root/attachments/some-uuid/ticket8484/trac_8484.patch) by rlm created at 2010-03-11 01:17:43



---

archive/issue_comments_076461.json:
```json
{
    "body": "It would have been nice to have had some description of what the patch contains!\n\nI am happy with the main part: applies fine to 4.3.4.alpha1, and all tests in sage/schemes/elliptic_curves pass.\n\nBut I am puzzled about the need for your small_rank_curves function:  we already have cremona_curves() and cremona_optimal_curves(), as defined in ell_rational_field but using an iterator defined in sage/databases/cremona.  Would it not be more sensible to add an option to that (specifically, to iter_optimal(), list_optimal()) which gives optional filtering data such as a list of ranks?  (Other posibilities, in addition:  list of possible torsion, etc).\n\nIf you can justify this function's existence, then it should go in another place, probably in ell_rational_field just after cremona_optimal_curves.\n\nBut for that I would give this a positive review!",
    "created_at": "2010-03-13T17:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76461",
    "user": "cremona"
}
```

It would have been nice to have had some description of what the patch contains!

I am happy with the main part: applies fine to 4.3.4.alpha1, and all tests in sage/schemes/elliptic_curves pass.

But I am puzzled about the need for your small_rank_curves function:  we already have cremona_curves() and cremona_optimal_curves(), as defined in ell_rational_field but using an iterator defined in sage/databases/cremona.  Would it not be more sensible to add an option to that (specifically, to iter_optimal(), list_optimal()) which gives optional filtering data such as a list of ranks?  (Other posibilities, in addition:  list of possible torsion, etc).

If you can justify this function's existence, then it should go in another place, probably in ell_rational_field just after cremona_optimal_curves.

But for that I would give this a positive review!



---

archive/issue_comments_076462.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n> But I am puzzled about the need for your small_rank_curves function\n\nThat was entirely for my own convenience in doing my research. I didn't want to have to keep typing so much, so I made a short name for it... I can pull that out of the patch and just keep it on my local queue if you'd prefer.",
    "created_at": "2010-03-13T19:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76462",
    "user": "rlm"
}
```

Replying to [comment:3 cremona]:
> But I am puzzled about the need for your small_rank_curves function

That was entirely for my own convenience in doing my research. I didn't want to have to keep typing so much, so I made a short name for it... I can pull that out of the patch and just keep it on my local queue if you'd prefer.



---

archive/issue_comments_076463.json:
```json
{
    "body": "Attachment [trac_8484-wo-src.patch](tarball://root/attachments/some-uuid/ticket8484/trac_8484-wo-src.patch) by rlm created at 2010-03-13 19:19:59\n\nSame as other patch, minus small_rank_curves function",
    "created_at": "2010-03-13T19:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76463",
    "user": "rlm"
}
```

Attachment [trac_8484-wo-src.patch](tarball://root/attachments/some-uuid/ticket8484/trac_8484-wo-src.patch) by rlm created at 2010-03-13 19:19:59

Same as other patch, minus small_rank_curves function



---

archive/issue_comments_076464.json:
```json
{
    "body": "Replying to [comment:4 rlm]:\n> Replying to [comment:3 cremona]:\n> > But I am puzzled about the need for your small_rank_curves function\n> \n> That was entirely for my own convenience in doing my research. I didn't want to have to keep typing so much, so I made a short name for it... I can pull that out of the patch and just keep it on my local queue if you'd prefer.\n\nI guessed that.  If you agree that it would be good to have options to the existing database iterators, we could open up a new ticket for that.\n\nNow I should really test the new patch, just in case...",
    "created_at": "2010-03-13T20:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76464",
    "user": "cremona"
}
```

Replying to [comment:4 rlm]:
> Replying to [comment:3 cremona]:
> > But I am puzzled about the need for your small_rank_curves function
> 
> That was entirely for my own convenience in doing my research. I didn't want to have to keep typing so much, so I made a short name for it... I can pull that out of the patch and just keep it on my local queue if you'd prefer.

I guessed that.  If you agree that it would be good to have options to the existing database iterators, we could open up a new ticket for that.

Now I should really test the new patch, just in case...



---

archive/issue_comments_076465.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-14T14:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76465",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076466.json:
```json
{
    "body": "The new patch passes all tests in sage/schemes/elliptic_curves.  positive review!",
    "created_at": "2010-03-14T14:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76466",
    "user": "cremona"
}
```

The new patch passes all tests in sage/schemes/elliptic_curves.  positive review!



---

archive/issue_comments_076467.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76467",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_076468.json:
```json
{
    "body": "Merged \"trac_8484-wo-src.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-15T23:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8484#issuecomment-76468",
    "user": "jhpalmieri"
}
```

Merged "trac_8484-wo-src.patch" into 4.4.alpha0.
