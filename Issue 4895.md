# Issue 4895: bug in pattern avoiding permutations

archive/issues_004895.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  jbandlow sage-combinat\n\nKeywords: pattern avoiding permutations\n\nThe following behavior is clearly bad:\n\n```\nsage: [p for p in Permutations(4,avoiding=[2,3,1]) if p.has_pattern([2,3,1])]               \n[[2, 3, 1, 4], [4, 2, 3, 1]]\n```\n\n\nSimilar behavior occurs when avoiding [1,3,2], [2,1,3], and [3,1,2].\n\nIssue created by migration from https://trac.sagemath.org/ticket/4895\n\n",
    "created_at": "2008-12-31T01:54:19Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "bug in pattern avoiding permutations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4895",
    "user": "jbandlow"
}
```
Assignee: mhansen

CC:  jbandlow sage-combinat

Keywords: pattern avoiding permutations

The following behavior is clearly bad:

```
sage: [p for p in Permutations(4,avoiding=[2,3,1]) if p.has_pattern([2,3,1])]               
[[2, 3, 1, 4], [4, 2, 3, 1]]
```


Similar behavior occurs when avoiding [1,3,2], [2,1,3], and [3,1,2].

Issue created by migration from https://trac.sagemath.org/ticket/4895





---

archive/issue_comments_037115.json:
```json
{
    "body": "Attachment [4895.patch](tarball://root/attachments/some-uuid/ticket4895/4895.patch) by jbandlow created at 2009-01-15 07:55:44\n\nThe problem was a simple typo in an initial condition (combined with a bunch of doctests that tested for incorrect behavior).  Warning: I've been travelling and not had an opportunity to upgrade sage recently, so this patch is based off 3.2.1.  I don't expect this to be a problem, but if the patch does not apply, let me know and I will fix it as soon as possible.",
    "created_at": "2009-01-15T07:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4895#issuecomment-37115",
    "user": "jbandlow"
}
```

Attachment [4895.patch](tarball://root/attachments/some-uuid/ticket4895/4895.patch) by jbandlow created at 2009-01-15 07:55:44

The problem was a simple typo in an initial condition (combined with a bunch of doctests that tested for incorrect behavior).  Warning: I've been travelling and not had an opportunity to upgrade sage recently, so this patch is based off 3.2.1.  I don't expect this to be a problem, but if the patch does not apply, let me know and I will fix it as soon as possible.



---

archive/issue_comments_037116.json:
```json
{
    "body": "Changing assignee from mhansen to jbandlow.",
    "created_at": "2009-01-15T07:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4895#issuecomment-37116",
    "user": "jbandlow"
}
```

Changing assignee from mhansen to jbandlow.



---

archive/issue_comments_037117.json:
```json
{
    "body": "Nice work Jason.",
    "created_at": "2009-01-24T03:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4895#issuecomment-37117",
    "user": "mhansen"
}
```

Nice work Jason.



---

archive/issue_comments_037118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T02:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4895#issuecomment-37118",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037119.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T02:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4895#issuecomment-37119",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2.

Cheers,

Michael
