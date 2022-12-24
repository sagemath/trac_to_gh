# Issue 8260: valuation of zero is wrong for Qq

archive/issues_008260.json:
```json
{
    "body": "Assignee: roed\n\nCC:  roed robertwb\n\nThis is ok:\n\n\n```\nsage: K = Qp(5)\nsage: x = K(0)\nsage: x.valuation()\n+Infinity\n```\n\n\nThis is bad:\n\n\n```\nsage: K.<a> = Qq(25)\nsage: x = K(0)\nsage: x.valuation()\n1073741823\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8260\n\n",
    "created_at": "2010-02-14T02:25:43Z",
    "labels": [
        "padics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "valuation of zero is wrong for Qq",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8260",
    "user": "dmharvey"
}
```
Assignee: roed

CC:  roed robertwb

This is ok:


```
sage: K = Qp(5)
sage: x = K(0)
sage: x.valuation()
+Infinity
```


This is bad:


```
sage: K.<a> = Qq(25)
sage: x = K(0)
sage: x.valuation()
1073741823
```



Issue created by migration from https://trac.sagemath.org/ticket/8260





---

archive/issue_comments_073105.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-21T03:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8260#issuecomment-73105",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073106.json:
```json
{
    "body": "Attachment [8260-Qq-valuation.patch](tarball://root/attachments/some-uuid/ticket8260/8260-Qq-valuation.patch) by robertwb created at 2010-02-21 03:40:44\n\nThere were inconsistent definitions of maxordp.",
    "created_at": "2010-02-21T03:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8260#issuecomment-73106",
    "user": "robertwb"
}
```

Attachment [8260-Qq-valuation.patch](tarball://root/attachments/some-uuid/ticket8260/8260-Qq-valuation.patch) by robertwb created at 2010-02-21 03:40:44

There were inconsistent definitions of maxordp.



---

archive/issue_comments_073107.json:
```json
{
    "body": "Yep, that should do it.  Doctests all pass.",
    "created_at": "2010-02-21T18:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8260#issuecomment-73107",
    "user": "roed"
}
```

Yep, that should do it.  Doctests all pass.



---

archive/issue_comments_073108.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-21T18:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8260#issuecomment-73108",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073109.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8260#issuecomment-73109",
    "user": "mvngu"
}
```

Resolution: fixed
