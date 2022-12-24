# Issue 7836: Clean up the CRT_* functions

archive/issues_007836.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  cremona rlm\n\nFrom #7595:\n\nReplying to [comment:10 cremona]:\n> I have some problems with the CRT* functions though.\n> \n>    1. CRT_list does not check that the two lists have the same length;  if the moduli list is shorter you get an IndexError, but it would be better to catch that and raise a more informative error.\n> \n>    2. CRT_basis is rather silly.   It calls CRT_list n times with the same moduli, which must be wasteful.  It would be better to call plain CRT n times with suitable moduli (exercise for the reader).\n> \n> Of course, I don't think that these issues should delay the current patch, but deserve a ticket of their own to make sure they are tided up.\n}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/7836\n\n",
    "created_at": "2010-01-03T21:37:37Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Clean up the CRT_* functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7836",
    "user": "mhansen"
}
```
Assignee: AlexGhitza

CC:  cremona rlm

From #7595:

Replying to [comment:10 cremona]:
> I have some problems with the CRT* functions though.
> 
>    1. CRT_list does not check that the two lists have the same length;  if the moduli list is shorter you get an IndexError, but it would be better to catch that and raise a more informative error.
> 
>    2. CRT_basis is rather silly.   It calls CRT_list n times with the same moduli, which must be wasteful.  It would be better to call plain CRT n times with suitable moduli (exercise for the reader).
> 
> Of course, I don't think that these issues should delay the current patch, but deserve a ticket of their own to make sure they are tided up.
}}}

Issue created by migration from https://trac.sagemath.org/ticket/7836





---

archive/issue_comments_067885.json:
```json
{
    "body": "Applies to 4.3 + patches at #7595",
    "created_at": "2010-01-04T17:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7836#issuecomment-67885",
    "user": "cremona"
}
```

Applies to 4.3 + patches at #7595



---

archive/issue_comments_067886.json:
```json
{
    "body": "Attachment [trac_7836-CRT.patch](tarball://root/attachments/some-uuid/ticket7836/trac_7836-CRT.patch) by cremona created at 2010-01-04 17:22:50\n\nThe attached patch is based on 4.3 + the patches at #7595.  I tested all files which use either CRT_list or CRT_basis.",
    "created_at": "2010-01-04T17:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7836#issuecomment-67886",
    "user": "cremona"
}
```

Attachment [trac_7836-CRT.patch](tarball://root/attachments/some-uuid/ticket7836/trac_7836-CRT.patch) by cremona created at 2010-01-04 17:22:50

The attached patch is based on 4.3 + the patches at #7595.  I tested all files which use either CRT_list or CRT_basis.



---

archive/issue_comments_067887.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-04T17:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7836#issuecomment-67887",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067888.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-01-04T17:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7836#issuecomment-67888",
    "user": "cremona"
}
```

Changing priority from major to minor.



---

archive/issue_comments_067889.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-04T18:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7836#issuecomment-67889",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067890.json:
```json
{
    "body": "I've tested in `sage/rings`, and the changes look good to me.",
    "created_at": "2010-01-04T18:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7836#issuecomment-67890",
    "user": "rlm"
}
```

I've tested in `sage/rings`, and the changes look good to me.



---

archive/issue_comments_067891.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T05:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7836#issuecomment-67891",
    "user": "rlm"
}
```

Resolution: fixed
