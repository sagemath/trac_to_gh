# Issue 5785: bug in norm of vectors over CDF

archive/issues_005785.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: CDF vector norm\n\n\n```\nsage: v = vector(CDF, [2, 2])\nsage: v - v\n(0, 0)\nsage: (v - v).norm()\nnan\nsage: v = vector(CC, [2, 2])\nsage: (v - v).norm()\n0.000000000000000\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5785\n\n",
    "created_at": "2009-04-14T15:55:27Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "bug in norm of vectors over CDF",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5785",
    "user": "@ncalexan"
}
```
Assignee: @williamstein

Keywords: CDF vector norm


```
sage: v = vector(CDF, [2, 2])
sage: v - v
(0, 0)
sage: (v - v).norm()
nan
sage: v = vector(CC, [2, 2])
sage: (v - v).norm()
0.000000000000000
```


Issue created by migration from https://trac.sagemath.org/ticket/5785





---

archive/issue_comments_045280.json:
```json
{
    "body": "Changing assignee from @williamstein to somebody.",
    "created_at": "2009-04-15T05:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5785#issuecomment-45280",
    "user": "@jasongrout"
}
```

Changing assignee from @williamstein to somebody.



---

archive/issue_comments_045281.json:
```json
{
    "body": "The problem is this:\n\n\n```\nsage: RDF(0)^(1/2)\nNaN\n```\n",
    "created_at": "2009-04-15T05:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5785#issuecomment-45281",
    "user": "@jasongrout"
}
```

The problem is this:


```
sage: RDF(0)^(1/2)
NaN
```




---

archive/issue_comments_045282.json:
```json
{
    "body": "Changing component from linear algebra to basic arithmetic.",
    "created_at": "2009-04-15T05:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5785#issuecomment-45282",
    "user": "@jasongrout"
}
```

Changing component from linear algebra to basic arithmetic.



---

archive/issue_comments_045283.json:
```json
{
    "body": "Does #5782 fix this?",
    "created_at": "2009-04-16T17:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5785#issuecomment-45283",
    "user": "@jasongrout"
}
```

Does #5782 fix this?



---

archive/issue_comments_045284.json:
```json
{
    "body": "Attachment [5785-cdf-norm.patch](tarball://root/attachments/some-uuid/ticket5785/5785-cdf-norm.patch) by @robertwb created at 2009-04-16 19:12:23\n\nAdded a doctest.",
    "created_at": "2009-04-16T19:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5785#issuecomment-45284",
    "user": "@robertwb"
}
```

Attachment [5785-cdf-norm.patch](tarball://root/attachments/some-uuid/ticket5785/5785-cdf-norm.patch) by @robertwb created at 2009-04-16 19:12:23

Added a doctest.



---

archive/issue_comments_045285.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n> Does #5782 fix this?\n\nIt looks like the same bug, having a doctest added ought to be enough to close this ticket once it is merged.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T21:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5785#issuecomment-45285",
    "user": "mabshoff"
}
```

Replying to [comment:2 jason]:
> Does #5782 fix this?

It looks like the same bug, having a doctest added ought to be enough to close this ticket once it is merged.

Cheers,

Michael



---

archive/issue_comments_045286.json:
```json
{
    "body": "Positive review. I changed the double colon after AUTHORS to a single colon. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T00:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5785#issuecomment-45286",
    "user": "mabshoff"
}
```

Positive review. I changed the double colon after AUTHORS to a single colon. 

Cheers,

Michael



---

archive/issue_comments_045287.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-18T00:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5785#issuecomment-45287",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045288.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc4.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T00:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5785#issuecomment-45288",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc4.

Cheers,

Michael
