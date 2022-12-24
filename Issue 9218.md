# Issue 9218: add a finance chapter to the sage reference manual

archive/issues_009218.json:
```json
{
    "body": "Assignee: mvngu\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9218\n\n",
    "created_at": "2010-06-11T18:19:19Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "add a finance chapter to the sage reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9218",
    "user": "was"
}
```
Assignee: mvngu



Issue created by migration from https://trac.sagemath.org/ticket/9218





---

archive/issue_comments_086376.json:
```json
{
    "body": "Attachment [trac_9218-finance_doc.patch](tarball://root/attachments/some-uuid/ticket9218/trac_9218-finance_doc.patch) by was created at 2010-06-11 18:44:06\n\nThe first patch adds the documentation.  However the docstrings are all pre-rest, so look like crap.  E.g., see \n\n    http://sage.math.washington.edu/home/wstein/build/sage-4.4.4.alpha0/devel/sage/doc/output/html/en/reference/finance.html\n\nor just apply the patch, then do `sage -docbuild reference html` and look at `output/html/en/reference/` for yourself.\n\nA second patch will fix all the formatting.",
    "created_at": "2010-06-11T18:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9218#issuecomment-86376",
    "user": "was"
}
```

Attachment [trac_9218-finance_doc.patch](tarball://root/attachments/some-uuid/ticket9218/trac_9218-finance_doc.patch) by was created at 2010-06-11 18:44:06

The first patch adds the documentation.  However the docstrings are all pre-rest, so look like crap.  E.g., see 

    http://sage.math.washington.edu/home/wstein/build/sage-4.4.4.alpha0/devel/sage/doc/output/html/en/reference/finance.html

or just apply the patch, then do `sage -docbuild reference html` and look at `output/html/en/reference/` for yourself.

A second patch will fix all the formatting.



---

archive/issue_comments_086377.json:
```json
{
    "body": "Attachment [trac_9218-reviewer.patch](tarball://root/attachments/some-uuid/ticket9218/trac_9218-reviewer.patch) by mvngu created at 2010-06-12 21:55:16",
    "created_at": "2010-06-12T21:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9218#issuecomment-86377",
    "user": "mvngu"
}
```

Attachment [trac_9218-reviewer.patch](tarball://root/attachments/some-uuid/ticket9218/trac_9218-reviewer.patch) by mvngu created at 2010-06-12 21:55:16



---

archive/issue_comments_086378.json:
```json
{
    "body": "Replying to [comment:1 was]:\n> The first patch adds the documentation.  However the docstrings are all pre-rest, so look like crap. \n\nNot any more.\n\n\n\n\n> A second patch will fix all the formatting. \n\nSee my reviewer patch.",
    "created_at": "2010-06-12T22:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9218#issuecomment-86378",
    "user": "mvngu"
}
```

Replying to [comment:1 was]:
> The first patch adds the documentation.  However the docstrings are all pre-rest, so look like crap. 

Not any more.




> A second patch will fix all the formatting. 

See my reviewer patch.



---

archive/issue_comments_086379.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-12T22:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9218#issuecomment-86379",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086380.json:
```json
{
    "body": "Attachment [trac_9218-typo.patch](tarball://root/attachments/some-uuid/ticket9218/trac_9218-typo.patch) by kcrisman created at 2010-06-18 18:15:58\n\nApply this last.",
    "created_at": "2010-06-18T18:15:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9218#issuecomment-86380",
    "user": "kcrisman"
}
```

Attachment [trac_9218-typo.patch](tarball://root/attachments/some-uuid/ticket9218/trac_9218-typo.patch) by kcrisman created at 2010-06-18 18:15:58

Apply this last.



---

archive/issue_comments_086381.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-18T18:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9218#issuecomment-86381",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086382.json:
```json
{
    "body": "Looks good!  Apply in the order `finance_doc`, `reviewer`, and `typo`.  Also added Minh as an author, considering his patch is two orders of magnitude bigger than the original one.",
    "created_at": "2010-06-18T18:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9218#issuecomment-86382",
    "user": "kcrisman"
}
```

Looks good!  Apply in the order `finance_doc`, `reviewer`, and `typo`.  Also added Minh as an author, considering his patch is two orders of magnitude bigger than the original one.



---

archive/issue_comments_086383.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T09:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9218#issuecomment-86383",
    "user": "mpatel"
}
```

Resolution: fixed
