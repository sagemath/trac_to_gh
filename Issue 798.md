# Issue 798: [with patch] MPolynomial_libsingular.subs

archive/issues_000798.json:
```json
{
    "body": "Assignee: somebody\n\nThis used to be broken:\n\n```\nsage: P.<x,y,z> = PolynomialRing(GF(2),3)\nsage: f = x + y + 1\nsage: f.subs(x=y+1)\n0 # used to return 1\n```\n\nthe attached two patches fixes this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/798\n\n",
    "created_at": "2007-10-03T03:04:29Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "[with patch] MPolynomial_libsingular.subs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/798",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

This used to be broken:

```
sage: P.<x,y,z> = PolynomialRing(GF(2),3)
sage: f = x + y + 1
sage: f.subs(x=y+1)
0 # used to return 1
```

the attached two patches fixes this.

Issue created by migration from https://trac.sagemath.org/ticket/798





---

archive/issue_comments_004801.json:
```json
{
    "body": "Attachment [subs.patch](tarball://root/attachments/some-uuid/ticket798/subs.patch) by @malb created at 2007-10-03 03:04:48",
    "created_at": "2007-10-03T03:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/798#issuecomment-4801",
    "user": "https://github.com/malb"
}
```

Attachment [subs.patch](tarball://root/attachments/some-uuid/ticket798/subs.patch) by @malb created at 2007-10-03 03:04:48



---

archive/issue_events_002212.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T18:11:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/798",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/798#event-2212"
}
```



---

archive/issue_comments_004802.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T18:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/798#issuecomment-4802",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
