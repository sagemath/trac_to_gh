# Issue 6291: Missing identity function in AbelianGroup

archive/issues_006291.json:
```json
{
    "body": "Assignee: joyner\n\nKeywords: AbelianGroup\n\nMissing identity function\n\nAbelianGroup patch\nSince we can do;\n\n```\nsage: G = DihedralGroup(10)\nsage: G.identity()\n()\nsage: G = SymmetricGroup(5)\nsage: G.identity()\n()\n```\n\nI thought we should be able to do the following\n\n```\nsage: G = AbelianGroup([2,2])\nsage: G.identity()\n1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6291\n\n",
    "created_at": "2009-06-15T03:30:39Z",
    "labels": [
        "group theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Missing identity function in AbelianGroup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6291",
    "user": "jlefebvre"
}
```
Assignee: joyner

Keywords: AbelianGroup

Missing identity function

AbelianGroup patch
Since we can do;

```
sage: G = DihedralGroup(10)
sage: G.identity()
()
sage: G = SymmetricGroup(5)
sage: G.identity()
()
```

I thought we should be able to do the following

```
sage: G = AbelianGroup([2,2])
sage: G.identity()
1
```


Issue created by migration from https://trac.sagemath.org/ticket/6291





---

archive/issue_comments_050227.json:
```json
{
    "body": "Attachment [6291identityFuction.patch](tarball://root/attachments/some-uuid/ticket6291/6291identityFuction.patch) by jlefebvre created at 2009-06-15 04:05:26\n\nThe identity Function",
    "created_at": "2009-06-15T04:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6291#issuecomment-50227",
    "user": "jlefebvre"
}
```

Attachment [6291identityFuction.patch](tarball://root/attachments/some-uuid/ticket6291/6291identityFuction.patch) by jlefebvre created at 2009-06-15 04:05:26

The identity Function



---

archive/issue_comments_050228.json:
```json
{
    "body": "Good idea.\n\nApplies, builds, functions, docs build, passes long tests.\n\nPositive review.",
    "created_at": "2009-10-05T05:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6291#issuecomment-50228",
    "user": "rbeezer"
}
```

Good idea.

Applies, builds, functions, docs build, passes long tests.

Positive review.



---

archive/issue_comments_050229.json:
```json
{
    "body": "Changing keywords from \"AbelianGroup\" to \"AbelianGroup, identity\".",
    "created_at": "2009-10-05T05:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6291#issuecomment-50229",
    "user": "rbeezer"
}
```

Changing keywords from "AbelianGroup" to "AbelianGroup, identity".



---

archive/issue_comments_050230.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-06T19:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6291#issuecomment-50230",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050231.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-06T19:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6291#issuecomment-50231",
    "user": "jason"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050232.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-19T05:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6291#issuecomment-50232",
    "user": "mhansen"
}
```

Resolution: fixed
