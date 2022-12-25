# Issue 3005: [with patch, positive review] modabar -- failure to compute endomorphism ring

archive/issues_003005.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThis is an example of computing an endomorphism ring of a J1 modular abelian variety -- it fails because of some mysterious issue in sage-3.0. \n\n```\nage: J = J1(17)\nsage: D = J.decomposition(); D\n[\nSimple abelian subvariety 17aG1(1,17) of dimension 1 of J1(17),\nSimple abelian subvariety 17bG1(1,17) of dimension 4 of J1(17)\n]\nsage: Phi, _ = D[0].intersection(D[1]); Phi\nFinite subgroup with invariants [2, 2] over QQ of Simple abelian subvariety 17aG1(1,17) of dimension 1 of J1(17)\nsage: E = D[1].endomorphism_ring(); E\nEndomorphism ring of Simple abelian subvariety 17bG1(1,17) of dimension 4 of J1(17)\nsage: E.gens()\nTraceback (most recent call last):\n...\nTypeError: Cannot coerce element into this number field\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3005\n\n",
    "closed_at": "2008-04-24T14:38:04Z",
    "created_at": "2008-04-23T13:08:04Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch, positive review] modabar -- failure to compute endomorphism ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3005",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

This is an example of computing an endomorphism ring of a J1 modular abelian variety -- it fails because of some mysterious issue in sage-3.0. 

```
age: J = J1(17)
sage: D = J.decomposition(); D
[
Simple abelian subvariety 17aG1(1,17) of dimension 1 of J1(17),
Simple abelian subvariety 17bG1(1,17) of dimension 4 of J1(17)
]
sage: Phi, _ = D[0].intersection(D[1]); Phi
Finite subgroup with invariants [2, 2] over QQ of Simple abelian subvariety 17aG1(1,17) of dimension 1 of J1(17)
sage: E = D[1].endomorphism_ring(); E
Endomorphism ring of Simple abelian subvariety 17bG1(1,17) of dimension 4 of J1(17)
sage: E.gens()
Traceback (most recent call last):
...
TypeError: Cannot coerce element into this number field
```

Issue created by migration from https://trac.sagemath.org/ticket/3005





---

archive/issue_comments_020624.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-04-24T07:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3005#issuecomment-20624",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_020625.json:
```json
{
    "body": "Bug was actually with modular symbols -- when finding eigenvalues, there was a place where the name parameter didn't get passed along. As a result, the eigenvalue getting returned couldn't be coerced into the number field, and all hell broke loose. \n\nFixed, added a doctest to catch it (to modular symbols, not abelian varieties).",
    "created_at": "2008-04-24T07:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3005#issuecomment-20625",
    "user": "https://github.com/craigcitro"
}
```

Bug was actually with modular symbols -- when finding eigenvalues, there was a place where the name parameter didn't get passed along. As a result, the eigenvalue getting returned couldn't be coerced into the number field, and all hell broke loose. 

Fixed, added a doctest to catch it (to modular symbols, not abelian varieties).



---

archive/issue_comments_020626.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-24T07:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3005#issuecomment-20626",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020627.json:
```json
{
    "body": "Attachment [trac-3005.patch](tarball://root/attachments/some-uuid/ticket3005/trac-3005.patch) by @williamstein created at 2008-04-24 12:30:55\n\nThis is obviously right.",
    "created_at": "2008-04-24T12:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3005#issuecomment-20627",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-3005.patch](tarball://root/attachments/some-uuid/ticket3005/trac-3005.patch) by @williamstein created at 2008-04-24 12:30:55

This is obviously right.



---

archive/issue_events_006833.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-24T14:38:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3005",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3005#event-6833"
}
```



---

archive/issue_comments_020628.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-24T14:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3005#issuecomment-20628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020629.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-24T14:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3005#issuecomment-20629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha0
