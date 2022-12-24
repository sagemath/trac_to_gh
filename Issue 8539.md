# Issue 8539: EllipticCurve('6006j1').sha().p_primary_bound(3) ignores CTRL-C

archive/issues_008539.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  robertwb was\n\nWhen reproducing this, make sure to wait about 10 seconds before trying to interrupt, as it takes time earlier in the function elsewhere, which handles the interruption properly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8539\n\n",
    "created_at": "2010-03-15T04:01:18Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.5",
    "title": "EllipticCurve('6006j1').sha().p_primary_bound(3) ignores CTRL-C",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8539",
    "user": "rlm"
}
```
Assignee: cremona

CC:  robertwb was

When reproducing this, make sure to wait about 10 seconds before trying to interrupt, as it takes time earlier in the function elsewhere, which handles the interruption properly.

Issue created by migration from https://trac.sagemath.org/ticket/8539





---

archive/issue_comments_077189.json:
```json
{
    "body": "Changing component from elliptic curves to linear algebra.",
    "created_at": "2010-03-15T23:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77189",
    "user": "rlm"
}
```

Changing component from elliptic curves to linear algebra.



---

archive/issue_comments_077190.json:
```json
{
    "body": "Changing assignee from cremona to was.",
    "created_at": "2010-03-15T23:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77190",
    "user": "rlm"
}
```

Changing assignee from cremona to was.



---

archive/issue_comments_077191.json:
```json
{
    "body": "Attachment [trac_8539.patch](tarball://root/attachments/some-uuid/ticket8539/trac_8539.patch) by rlm created at 2010-03-15 23:42:25",
    "created_at": "2010-03-15T23:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77191",
    "user": "rlm"
}
```

Attachment [trac_8539.patch](tarball://root/attachments/some-uuid/ticket8539/trac_8539.patch) by rlm created at 2010-03-15 23:42:25



---

archive/issue_comments_077192.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-15T23:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77192",
    "user": "rlm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077193.json:
```json
{
    "body": "I'm not sure if using dense matrices here was an oversight, or if there was a reason for it...\n\nhttp://hg.sagemath.org/sage-main/annotate/8df7435d1864/sage/matrix/matrix_integer_sparse.pyx#241",
    "created_at": "2010-03-16T00:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77193",
    "user": "robertwb"
}
```

I'm not sure if using dense matrices here was an oversight, or if there was a reason for it...

http://hg.sagemath.org/sage-main/annotate/8df7435d1864/sage/matrix/matrix_integer_sparse.pyx#241



---

archive/issue_comments_077194.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-26T21:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77194",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077195.json:
```json
{
    "body": "Enthusiastic positive review!!!!!!!!!! \n\nThis totally rocks, leading to massive speedups in modular symbols (susprisingly).",
    "created_at": "2010-03-26T22:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77195",
    "user": "was"
}
```

Enthusiastic positive review!!!!!!!!!! 

This totally rocks, leading to massive speedups in modular symbols (susprisingly).



---

archive/issue_comments_077196.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-03-26T22:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77196",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_077197.json:
```json
{
    "body": "this is a referee patch that fixes a doctest (which was wrong).",
    "created_at": "2010-03-27T01:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77197",
    "user": "was"
}
```

this is a referee patch that fixes a doctest (which was wrong).



---

archive/issue_comments_077198.json:
```json
{
    "body": "Attachment [trac_8539-part2.patch](tarball://root/attachments/some-uuid/ticket8539/trac_8539-part2.patch) by was created at 2010-03-29 22:08:01\n\nMerged into sage-4.3.5",
    "created_at": "2010-03-29T22:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77198",
    "user": "was"
}
```

Attachment [trac_8539-part2.patch](tarball://root/attachments/some-uuid/ticket8539/trac_8539-part2.patch) by was created at 2010-03-29 22:08:01

Merged into sage-4.3.5



---

archive/issue_comments_077199.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-29T22:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8539#issuecomment-77199",
    "user": "was"
}
```

Resolution: fixed
