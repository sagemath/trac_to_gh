# Issue 713: [with patch] Interrupting Singular doesn't work

archive/issues_000713.json:
```json
{
    "body": "Assignee: @williamstein\n\nConsider\n\n```\nsage: P = PolynomialRing(QQ,10,'x')\nsage: I = sage.rings.ideal.Katsura(P)\nsage: I.groebner_basis() # forever!\n```\nCtrl-C does not interrupt nor kill the Singular process doing the hard work. The attached patch fixes that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/713\n\n",
    "closed_at": "2007-09-20T18:57:02Z",
    "created_at": "2007-09-20T18:31:26Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "[with patch] Interrupting Singular doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/713",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

Consider

```
sage: P = PolynomialRing(QQ,10,'x')
sage: I = sage.rings.ideal.Katsura(P)
sage: I.groebner_basis() # forever!
```
Ctrl-C does not interrupt nor kill the Singular process doing the hard work. The attached patch fixes that.

Issue created by migration from https://trac.sagemath.org/ticket/713





---

archive/issue_comments_003725.json:
```json
{
    "body": "Attachment [6404.patch](tarball://root/attachments/some-uuid/ticket713/6404.patch) by @malb created at 2007-09-20 18:31:36",
    "created_at": "2007-09-20T18:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/713#issuecomment-3725",
    "user": "https://github.com/malb"
}
```

Attachment [6404.patch](tarball://root/attachments/some-uuid/ticket713/6404.patch) by @malb created at 2007-09-20 18:31:36



---

archive/issue_comments_003726.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-20T18:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/713",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/713#issuecomment-3726",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001906.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-20T18:57:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/713",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/713#event-1906"
}
```
