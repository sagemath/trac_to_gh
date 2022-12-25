# Issue 7758: doctest failure on OS X 10.5 intel due to randomization

archive/issues_007758.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long \"devel/sage/sage/numerical/mip.pyx\"**********************************************************************\nFile \"/Users/wstein/build/sage-4.3.rc1/devel/sage/sage/numerical/mip.pyx\", line 364:\n    sage: p.show()\nExpected:\n    Maximization:\n      x0 + x1\n    Constraints:\n      -3*x0 + 2*x1 <= 2\n    Variables:\n      x1 is a real variable (min=0.0, max=+oo)\n      x0 is a real variable (min=0.0, max=+oo)\nGot:\n    Maximization:\n      x0 + x1\n    Constraints:\n      -3*x0 + 2*x1 <= 2\n    Variables:\n      x0 is a real variable (min=0.0, max=+oo)\n      x1 is a real variable (min=0.0, max=+oo)\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7758\n\n",
    "created_at": "2009-12-24T07:52:44Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "doctest failure on OS X 10.5 intel due to randomization",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7758",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
sage -t -long "devel/sage/sage/numerical/mip.pyx"**********************************************************************
File "/Users/wstein/build/sage-4.3.rc1/devel/sage/sage/numerical/mip.pyx", line 364:
    sage: p.show()
Expected:
    Maximization:
      x0 + x1
    Constraints:
      -3*x0 + 2*x1 <= 2
    Variables:
      x1 is a real variable (min=0.0, max=+oo)
      x0 is a real variable (min=0.0, max=+oo)
Got:
    Maximization:
      x0 + x1
    Constraints:
      -3*x0 + 2*x1 <= 2
    Variables:
      x0 is a real variable (min=0.0, max=+oo)
      x1 is a real variable (min=0.0, max=+oo)

```


Issue created by migration from https://trac.sagemath.org/ticket/7758





---

archive/issue_comments_066690.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-24T07:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7758#issuecomment-66690",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066691.json:
```json
{
    "body": "Attachment [sagelib_7758.patch](tarball://root/attachments/some-uuid/ticket7758/sagelib_7758.patch) by @williamstein created at 2009-12-24 07:55:47",
    "created_at": "2009-12-24T07:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7758#issuecomment-66691",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagelib_7758.patch](tarball://root/attachments/some-uuid/ticket7758/sagelib_7758.patch) by @williamstein created at 2009-12-24 07:55:47



---

archive/issue_comments_066692.json:
```json
{
    "body": "I merged this into 4.3.rc2 anyways, since 4.3 is lingering forever.   I'm leaving this as \"needs review\" though.",
    "created_at": "2009-12-24T07:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7758#issuecomment-66692",
    "user": "https://github.com/williamstein"
}
```

I merged this into 4.3.rc2 anyways, since 4.3 is lingering forever.   I'm leaving this as "needs review" though.



---

archive/issue_comments_066693.json:
```json
{
    "body": "Attachment [sagelib_7758-part2.patch](tarball://root/attachments/some-uuid/ticket7758/sagelib_7758-part2.patch) by @nathanncohen created at 2009-12-24 22:26:16",
    "created_at": "2009-12-24T22:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7758#issuecomment-66693",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [sagelib_7758-part2.patch](tarball://root/attachments/some-uuid/ticket7758/sagelib_7758-part2.patch) by @nathanncohen created at 2009-12-24 22:26:16



---

archive/issue_comments_066694.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-24T22:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7758#issuecomment-66694",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066695.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-25T10:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7758#issuecomment-66695",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
