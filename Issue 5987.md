# Issue 5987: fix a few more bad comparison doctests

archive/issues_005987.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  embray\n\nTo make up for my past mistakes, here's a simple patch that modifies or removes a few bad comparison doctests (not all of which were introduced by me).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5987\n\n",
    "created_at": "2009-05-05T07:35:47Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "title": "fix a few more bad comparison doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5987",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

CC:  embray

To make up for my past mistakes, here's a simple patch that modifies or removes a few bad comparison doctests (not all of which were introduced by me).


Issue created by migration from https://trac.sagemath.org/ticket/5987





---

archive/issue_comments_047579.json:
```json
{
    "body": "Attachment [trac_5987.patch](tarball://root/attachments/some-uuid/ticket5987/trac_5987.patch) by AlexGhitza created at 2009-05-05 07:37:08",
    "created_at": "2009-05-05T07:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47579",
    "user": "AlexGhitza"
}
```

Attachment [trac_5987.patch](tarball://root/attachments/some-uuid/ticket5987/trac_5987.patch) by AlexGhitza created at 2009-05-05 07:37:08



---

archive/issue_comments_047580.json:
```json
{
    "body": "This patch is wrong. Instead of deleting the tests they should either be rewritten as \n\n```\nsage: f !=g\nTrue\n```\n\nor\n\n```\nsage: f<g in [-1,1]\nTrue\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T07:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47580",
    "user": "mabshoff"
}
```

This patch is wrong. Instead of deleting the tests they should either be rewritten as 

```
sage: f !=g
True
```

or

```
sage: f<g in [-1,1]
True
```


Cheers,

Michael



---

archive/issue_comments_047581.json:
```json
{
    "body": "And I forgot to mention: In some cases these comparisons are deterministic, so it needs to be dealt with on a case by case basis. I am not sure what applies in this case.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T07:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47581",
    "user": "mabshoff"
}
```

And I forgot to mention: In some cases these comparisons are deterministic, so it needs to be dealt with on a case by case basis. I am not sure what applies in this case.

Cheers,

Michael



---

archive/issue_comments_047582.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-12-17T19:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47582",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_047583.json:
```json
{
    "body": "let us close this old one as obsolete",
    "created_at": "2018-12-17T19:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47583",
    "user": "chapoton"
}
```

let us close this old one as obsolete



---

archive/issue_comments_047584.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-12-18T03:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47584",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047585.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47585",
    "user": "embray"
}
```

Resolution: invalid



---

archive/issue_comments_047586.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47586",
    "user": "embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.
