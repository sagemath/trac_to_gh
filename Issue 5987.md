# Issue 5987: fix a few more bad comparison doctests

archive/issues_005987.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @embray\n\nTo make up for my past mistakes, here's a simple patch that modifies or removes a few bad comparison doctests (not all of which were introduced by me).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5987\n\n",
    "created_at": "2009-05-05T07:35:47Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fix a few more bad comparison doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5987",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

CC:  @embray

To make up for my past mistakes, here's a simple patch that modifies or removes a few bad comparison doctests (not all of which were introduced by me).


Issue created by migration from https://trac.sagemath.org/ticket/5987





---

archive/issue_comments_047488.json:
```json
{
    "body": "Attachment [trac_5987.patch](tarball://root/attachments/some-uuid/ticket5987/trac_5987.patch) by @aghitza created at 2009-05-05 07:37:08",
    "created_at": "2009-05-05T07:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47488",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5987.patch](tarball://root/attachments/some-uuid/ticket5987/trac_5987.patch) by @aghitza created at 2009-05-05 07:37:08



---

archive/issue_comments_047489.json:
```json
{
    "body": "This patch is wrong. Instead of deleting the tests they should either be rewritten as \n\n```\nsage: f !=g\nTrue\n```\n\nor\n\n```\nsage: f<g in [-1,1]\nTrue\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T07:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47489",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_047490.json:
```json
{
    "body": "And I forgot to mention: In some cases these comparisons are deterministic, so it needs to be dealt with on a case by case basis. I am not sure what applies in this case.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T07:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47490",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And I forgot to mention: In some cases these comparisons are deterministic, so it needs to be dealt with on a case by case basis. I am not sure what applies in this case.

Cheers,

Michael



---

archive/issue_comments_047491.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-12-17T19:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47491",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_047492.json:
```json
{
    "body": "let us close this old one as obsolete",
    "created_at": "2018-12-17T19:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47492",
    "user": "https://github.com/fchapoton"
}
```

let us close this old one as obsolete



---

archive/issue_comments_047493.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-12-18T03:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47493",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_047494.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47494",
    "user": "https://github.com/embray"
}
```

Resolution: invalid



---

archive/issue_comments_047495.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5987#issuecomment-47495",
    "user": "https://github.com/embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.
