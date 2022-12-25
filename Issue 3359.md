# Issue 3359: [with patch, positive review] bug/inconsistency in multivariate polynomial substitution

archive/issues_003359.json:
```json
{
    "body": "Assignee: @malb\n\n```\nDear Andrey,\n\nOn Jun 4, 7:21 am, Andrey Novoseltsev <novos...@gmail.com> wrote:\n> What is wrong with the code below and how to fix it?\n\nI don't know what precisely is wrong with that code, but a very\nsimilar code works.\n\nFirst, i can reproduce the trouble:\nsage: Rt.<t> = PolynomialRing(QQ,1)\nsage: p = 1+t\nsage: R.<u,v> = PolynomialRing(QQ, 2)\nsage: p(u/v)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call\nlast)\n...\n\nThe following works:\nsage: Rt2.<t> = PolynomialRing(QQ)\nsage: p2 = 1+t\nsage: p2(u/v)\n(u + v)/v\n\nThe difference is that Rt is a Multivariate Polynomial Ring (with one\nvariable, though), but Rt2 is a genuine Univariate Polynomial Ring.\n\nSo, at least there is a work-around.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3359\n\n",
    "closed_at": "2008-08-26T23:17:47Z",
    "created_at": "2008-06-04T15:46:35Z",
    "labels": [
        "component: commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, positive review] bug/inconsistency in multivariate polynomial substitution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3359",
    "user": "https://github.com/williamstein"
}
```
Assignee: @malb

```
Dear Andrey,

On Jun 4, 7:21 am, Andrey Novoseltsev <novos...@gmail.com> wrote:
> What is wrong with the code below and how to fix it?

I don't know what precisely is wrong with that code, but a very
similar code works.

First, i can reproduce the trouble:
sage: Rt.<t> = PolynomialRing(QQ,1)
sage: p = 1+t
sage: R.<u,v> = PolynomialRing(QQ, 2)
sage: p(u/v)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call
last)
...

The following works:
sage: Rt2.<t> = PolynomialRing(QQ)
sage: p2 = 1+t
sage: p2(u/v)
(u + v)/v

The difference is that Rt is a Multivariate Polynomial Ring (with one
variable, though), but Rt2 is a genuine Univariate Polynomial Ring.

So, at least there is a work-around.
```

Issue created by migration from https://trac.sagemath.org/ticket/3359





---

archive/issue_comments_023339.json:
```json
{
    "body": "Attachment [trac_3359.patch](tarball://root/attachments/some-uuid/ticket3359/trac_3359.patch) by @malb created at 2008-08-18 13:54:46\n\nThe attached patch fixes this issue.",
    "created_at": "2008-08-18T13:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3359#issuecomment-23339",
    "user": "https://github.com/malb"
}
```

Attachment [trac_3359.patch](tarball://root/attachments/some-uuid/ticket3359/trac_3359.patch) by @malb created at 2008-08-18 13:54:46

The attached patch fixes this issue.



---

archive/issue_comments_023340.json:
```json
{
    "body": "was, can I ask you to review the patch since you reported the issue?",
    "created_at": "2008-08-24T12:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3359#issuecomment-23340",
    "user": "https://github.com/malb"
}
```

was, can I ask you to review the patch since you reported the issue?



---

archive/issue_comments_023341.json:
```json
{
    "body": "Attachment [trac_3359-2.patch](tarball://root/attachments/some-uuid/ticket3359/trac_3359-2.patch) by @mwhansen created at 2008-08-26 22:20:44\n\nLooks good to me.  Apply both patches.",
    "created_at": "2008-08-26T22:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3359#issuecomment-23341",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3359-2.patch](tarball://root/attachments/some-uuid/ticket3359/trac_3359-2.patch) by @mwhansen created at 2008-08-26 22:20:44

Looks good to me.  Apply both patches.



---

archive/issue_comments_023342.json:
```json
{
    "body": "Merged both patches in Sage 3.1.2.alpha1",
    "created_at": "2008-08-26T23:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3359#issuecomment-23342",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.1.2.alpha1



---

archive/issue_comments_023343.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-26T23:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3359#issuecomment-23343",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007537.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-26T23:17:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3359",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3359#event-7537"
}
```
