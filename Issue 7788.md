# Issue 7788: followup patch to #5396

archive/issues_007788.json:
```json
{
    "body": "Assignee: was\n\nCC:  craigcitro cremona ylchapuy robertwb\n\nI am attaching  patchs which adds to the documentation that the derivatives loose about half the precision. There is additional documentation to guide how many dirichlet coefficients are needed, at least for computing near the real axis.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7788\n\n",
    "created_at": "2009-12-29T16:45:25Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "followup patch to #5396",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7788",
    "user": "rishi"
}
```
Assignee: was

CC:  craigcitro cremona ylchapuy robertwb

I am attaching  patchs which adds to the documentation that the derivatives loose about half the precision. There is additional documentation to guide how many dirichlet coefficients are needed, at least for computing near the real axis.

Issue created by migration from https://trac.sagemath.org/ticket/7788





---

archive/issue_comments_067213.json:
```json
{
    "body": "Attachment [minor_change_lcalc-1.patch](tarball://root/attachments/some-uuid/ticket7788/minor_change_lcalc-1.patch) by rishi created at 2009-12-29 16:45:42",
    "created_at": "2009-12-29T16:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67213",
    "user": "rishi"
}
```

Attachment [minor_change_lcalc-1.patch](tarball://root/attachments/some-uuid/ticket7788/minor_change_lcalc-1.patch) by rishi created at 2009-12-29 16:45:42



---

archive/issue_comments_067214.json:
```json
{
    "body": "Attachment [minor_change_lcalc-combined.patch](tarball://root/attachments/some-uuid/ticket7788/minor_change_lcalc-combined.patch) by rishi created at 2009-12-29 18:24:14",
    "created_at": "2009-12-29T18:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67214",
    "user": "rishi"
}
```

Attachment [minor_change_lcalc-combined.patch](tarball://root/attachments/some-uuid/ticket7788/minor_change_lcalc-combined.patch) by rishi created at 2009-12-29 18:24:14



---

archive/issue_comments_067215.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-29T18:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67215",
    "user": "rishi"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067216.json:
```json
{
    "body": "I finally figured out how to combine several commits",
    "created_at": "2009-12-29T18:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67216",
    "user": "rishi"
}
```

I finally figured out how to combine several commits



---

archive/issue_comments_067217.json:
```json
{
    "body": "I'm giving this a positive review, though the formatting of the docstrings in  lcalc_Lfunction.pyx is not correct so that sphinx would choke on these.  But at the moment this file is not included in the reference manual.  So rather than delay the merging of the lcalc wrapping, it seems reasonable to pass this as is and create a new TODO ticket for that.",
    "created_at": "2009-12-30T16:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67217",
    "user": "cremona"
}
```

I'm giving this a positive review, though the formatting of the docstrings in  lcalc_Lfunction.pyx is not correct so that sphinx would choke on these.  But at the moment this file is not included in the reference manual.  So rather than delay the merging of the lcalc wrapping, it seems reasonable to pass this as is and create a new TODO ticket for that.



---

archive/issue_comments_067218.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-30T16:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67218",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067219.json:
```json
{
    "body": "I don't think it's helpful to have this tagged as \"positive review\" when it depends on #5396 which is still being worked on.  So I am switching it back to \"needs work\" and it can go to \"needs review\" after #5396 is positively reviewed.",
    "created_at": "2010-01-17T18:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67219",
    "user": "cremona"
}
```

I don't think it's helpful to have this tagged as "positive review" when it depends on #5396 which is still being worked on.  So I am switching it back to "needs work" and it can go to "needs review" after #5396 is positively reviewed.



---

archive/issue_comments_067220.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-17T18:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67220",
    "user": "cremona"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_067221.json:
```json
{
    "body": "John,\n\nI put a new spkg in [#5396](http://trac.sagemath.org/sage_trac/ticket/5396)\n\nI tested it on my computer and on sage.math. I believe this should work.\n\nRishi",
    "created_at": "2010-01-17T19:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67221",
    "user": "rishi"
}
```

John,

I put a new spkg in [#5396](http://trac.sagemath.org/sage_trac/ticket/5396)

I tested it on my computer and on sage.math. I believe this should work.

Rishi



---

archive/issue_comments_067222.json:
```json
{
    "body": "This patch is superseded by #8623. This ticket can be discarded.",
    "created_at": "2010-07-11T02:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67222",
    "user": "rishi"
}
```

This patch is superseded by #8623. This ticket can be discarded.



---

archive/issue_comments_067223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-11T02:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67223",
    "user": "rishi"
}
```

Resolution: fixed



---

archive/issue_comments_067224.json:
```json
{
    "body": "Resolution changed from fixed to duplicate",
    "created_at": "2010-07-11T03:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7788",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7788#issuecomment-67224",
    "user": "mhansen"
}
```

Resolution changed from fixed to duplicate
