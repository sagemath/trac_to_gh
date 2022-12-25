# Issue 4768: magma -- speed up conversion of integer, rational and modn matrices from sage to magma

archive/issues_004768.json:
```json
{
    "body": "Assignee: @williamstein\n\nBy writing a little specialized code, I can probably speed up some of these conversions by an order of magnitude, and also make them way more efficient memory-wise.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4768\n\n",
    "created_at": "2008-12-12T06:59:56Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "magma -- speed up conversion of integer, rational and modn matrices from sage to magma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4768",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

By writing a little specialized code, I can probably speed up some of these conversions by an order of magnitude, and also make them way more efficient memory-wise.

Issue created by migration from https://trac.sagemath.org/ticket/4768





---

archive/issue_comments_036053.json:
```json
{
    "body": "Here is a before and after over ZZ:\nBEFORE:\n\n```\nsage: v = random_matrix(ZZ,1000)\nsage: time k = magma(v)\nCPU times: user 17.03 s, sys: 0.43 s, total: 17.47 s\nWall time: 18.88 s\n```\n\nAFTER:\n\n```\nsage: m = random_matrix(ZZ,1000,x=0,y=17)\nsage: time w = magma(m)\nCPU times: user 0.18 s, sys: 0.10 s, total: 0.28 s\nWall time: 1.68 s\n```\n\nHere is a before/after over the rational numbers:\nBEFORE:\n\n```\nsage: m = random_matrix(QQ,1000)\nsage: time k = magma(m)\nCPU times: user 9.41 s, sys: 0.39 s, total: 9.80 s\nWall time: 11.60 s\n```\nAFTER:\n\n```\nge: m = random_matrix(QQ,1000)\nsage: time k = magma(m)\nCPU times: user 0.48 s, sys: 0.16 s, total: 0.64 s\nWall time: 1.16 s\n```",
    "created_at": "2008-12-12T07:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4768#issuecomment-36053",
    "user": "https://github.com/williamstein"
}
```

Here is a before and after over ZZ:
BEFORE:

```
sage: v = random_matrix(ZZ,1000)
sage: time k = magma(v)
CPU times: user 17.03 s, sys: 0.43 s, total: 17.47 s
Wall time: 18.88 s
```

AFTER:

```
sage: m = random_matrix(ZZ,1000,x=0,y=17)
sage: time w = magma(m)
CPU times: user 0.18 s, sys: 0.10 s, total: 0.28 s
Wall time: 1.68 s
```

Here is a before/after over the rational numbers:
BEFORE:

```
sage: m = random_matrix(QQ,1000)
sage: time k = magma(m)
CPU times: user 9.41 s, sys: 0.39 s, total: 9.80 s
Wall time: 11.60 s
```
AFTER:

```
ge: m = random_matrix(QQ,1000)
sage: time k = magma(m)
CPU times: user 0.48 s, sys: 0.16 s, total: 0.64 s
Wall time: 1.16 s
```



---

archive/issue_comments_036054.json:
```json
{
    "body": "Attachment [trac_4768.patch](tarball://root/attachments/some-uuid/ticket4768/trac_4768.patch) by @malb created at 2008-12-12 14:39:58\n\nPatch applies cleanly, doctests in sage/matrix pass, reads good.",
    "created_at": "2008-12-12T14:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4768#issuecomment-36054",
    "user": "https://github.com/malb"
}
```

Attachment [trac_4768.patch](tarball://root/attachments/some-uuid/ticket4768/trac_4768.patch) by @malb created at 2008-12-12 14:39:58

Patch applies cleanly, doctests in sage/matrix pass, reads good.



---

archive/issue_comments_036055.json:
```json
{
    "body": "The matrix_rational_dense.pyx doctest around line 225 needs the line\n\n```\nsage: m = matrix(QQ,2,3,[1,2/3,-3/4,1,-2/3,-45/17])\n```\nadded for the doctest to pass.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-12T15:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4768#issuecomment-36055",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The matrix_rational_dense.pyx doctest around line 225 needs the line

```
sage: m = matrix(QQ,2,3,[1,2/3,-3/4,1,-2/3,-45/17])
```
added for the doctest to pass.

Cheers,

Michael



---

archive/issue_comments_036056.json:
```json
{
    "body": "Attachment [trac_4768_referee.patch](tarball://root/attachments/some-uuid/ticket4768/trac_4768_referee.patch) by mabshoff created at 2008-12-12 16:04:31\n\nMerged both patches in Sage 3.2.2.alpha2",
    "created_at": "2008-12-12T16:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4768#issuecomment-36056",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4768_referee.patch](tarball://root/attachments/some-uuid/ticket4768/trac_4768_referee.patch) by mabshoff created at 2008-12-12 16:04:31

Merged both patches in Sage 3.2.2.alpha2



---

archive/issue_comments_036057.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-12T16:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4768#issuecomment-36057",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010897.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-12T16:04:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4768",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4768#event-10897"
}
```
