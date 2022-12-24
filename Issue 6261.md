# Issue 6261: Add multiplicative order for matrices over finite fields

archive/issues_006261.json:
```json
{
    "body": "Assignee: was\n\nFor the algorithm used, see\nFrank Celler and Charles R. Leedham-Green, \"Calculating the Order of an Invertible Matrix\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/6261\n\n",
    "created_at": "2009-06-11T16:54:34Z",
    "labels": [
        "linear algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Add multiplicative order for matrices over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6261",
    "user": "ylchapuy"
}
```
Assignee: was

For the algorithm used, see
Frank Celler and Charles R. Leedham-Green, "Calculating the Order of an Invertible Matrix".

Issue created by migration from https://trac.sagemath.org/ticket/6261





---

archive/issue_comments_049993.json:
```json
{
    "body": "Attachment [trac-6261.patch](tarball://root/attachments/some-uuid/ticket6261/trac-6261.patch) by ylchapuy created at 2009-06-11 16:57:25",
    "created_at": "2009-06-11T16:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6261#issuecomment-49993",
    "user": "ylchapuy"
}
```

Attachment [trac-6261.patch](tarball://root/attachments/some-uuid/ticket6261/trac-6261.patch) by ylchapuy created at 2009-06-11 16:57:25



---

archive/issue_comments_049994.json:
```json
{
    "body": "This looks good to me.  One question:  in the line\n\n```\nppart = p**Integer(a).exact_log(p)\n```\n\ndo you really mean ppart to be the largest power of p which is <= a, rather than the pargest power which divides a?\nIf so, please change this to \"positive review\".\n\nRemark:  I have a Magma implementation of an algorithm to determine when a polynomial over ZZ is cyclotomic (algorithm of Smyth and Beukers).  That could be used to extend this function to matrices over ZZ, at least.",
    "created_at": "2009-06-14T16:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6261#issuecomment-49994",
    "user": "cremona"
}
```

This looks good to me.  One question:  in the line

```
ppart = p**Integer(a).exact_log(p)
```

do you really mean ppart to be the largest power of p which is <= a, rather than the pargest power which divides a?
If so, please change this to "positive review".

Remark:  I have a Magma implementation of an algorithm to determine when a polynomial over ZZ is cyclotomic (algorithm of Smyth and Beukers).  That could be used to extend this function to matrices over ZZ, at least.



---

archive/issue_comments_049995.json:
```json
{
    "body": "Replying to [comment:2 cremona]:\n> This looks good to me.  One question:  in the line\n> {{{\n> ppart = p**Integer(a).exact_log(p)\n> }}}\n> do you really mean ppart to be the largest power of p which is <= a, rather than the pargest power which divides a?\n> If so, please change this to \"positive review\".\n\nYes, it's what I mean. Thanks for the review.",
    "created_at": "2009-06-16T20:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6261#issuecomment-49995",
    "user": "ylchapuy"
}
```

Replying to [comment:2 cremona]:
> This looks good to me.  One question:  in the line
> {{{
> ppart = p**Integer(a).exact_log(p)
> }}}
> do you really mean ppart to be the largest power of p which is <= a, rather than the pargest power which divides a?
> If so, please change this to "positive review".

Yes, it's what I mean. Thanks for the review.



---

archive/issue_comments_049996.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6261#issuecomment-49996",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_049997.json:
```json
{
    "body": "\"Merged in: Yann Laigle-Chapuy\"? Hang on a minute! Which version was this actually merged in?",
    "created_at": "2009-06-27T08:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6261#issuecomment-49997",
    "user": "davidloeffler"
}
```

"Merged in: Yann Laigle-Chapuy"? Hang on a minute! Which version was this actually merged in?
