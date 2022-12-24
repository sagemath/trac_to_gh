# Issue 4773: determinants of non-square matrices over GF(p) (p odd) should raise an error -- instead they silently give nonsense

archive/issues_004773.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: w = random_matrix(GF(3),3,4)\nsage: w.determinant()\n0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4773\n\n",
    "created_at": "2008-12-12T19:34:29Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "determinants of non-square matrices over GF(p) (p odd) should raise an error -- instead they silently give nonsense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4773",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
sage: w = random_matrix(GF(3),3,4)
sage: w.determinant()
0
```


Issue created by migration from https://trac.sagemath.org/ticket/4773





---

archive/issue_comments_036148.json:
```json
{
    "body": "Attachment [trac_4773.patch](tarball://root/attachments/some-uuid/ticket4773/trac_4773.patch) by @aghitza created at 2008-12-12 22:27:38\n\nTrivial patch is attached.",
    "created_at": "2008-12-12T22:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4773#issuecomment-36148",
    "user": "@aghitza"
}
```

Attachment [trac_4773.patch](tarball://root/attachments/some-uuid/ticket4773/trac_4773.patch) by @aghitza created at 2008-12-12 22:27:38

Trivial patch is attached.



---

archive/issue_comments_036149.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T06:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4773#issuecomment-36149",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_036150.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-13T09:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4773#issuecomment-36150",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036151.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-13T09:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4773#issuecomment-36151",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha2
