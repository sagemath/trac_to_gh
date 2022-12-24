# Issue 1183: Residue fields are broken

archive/issues_001183.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe current implementation of residue fields for number fields is broken.  It just takes the defining polynomial for the number field, factors it over Z/pZ, picks one factor and creates an extension using that factor.  This breaks because elements of the ring of integers, when expressed in terms of the power basis of the number field can have denominators divisible by p.\n\nThe solution is to create a p-maximal order and do some linear algebra to come up with a map that doesn't break on denominators divisible by p.  Pari's nfinit has a way to give it a partial factorization of the discriminant that will produce a p-maximal order.\n\nIf you want to implement this, talk to William Stein or David Roe for more details.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1183\n\n",
    "created_at": "2007-11-16T02:35:39Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "Residue fields are broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1183",
    "user": "@roed314"
}
```
Assignee: @williamstein

The current implementation of residue fields for number fields is broken.  It just takes the defining polynomial for the number field, factors it over Z/pZ, picks one factor and creates an extension using that factor.  This breaks because elements of the ring of integers, when expressed in terms of the power basis of the number field can have denominators divisible by p.

The solution is to create a p-maximal order and do some linear algebra to come up with a map that doesn't break on denominators divisible by p.  Pari's nfinit has a way to give it a partial factorization of the discriminant that will produce a p-maximal order.

If you want to implement this, talk to William Stein or David Roe for more details.

Issue created by migration from https://trac.sagemath.org/ticket/1183





---

archive/issue_comments_007300.json:
```json
{
    "body": "Ifti did open #1185 for his specific problem. So in case this is solved and the status of #1183 remains unchanged please resolve that ticket, also.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-16T11:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1183#issuecomment-7300",
    "user": "mabshoff"
}
```

Ifti did open #1185 for his specific problem. So in case this is solved and the status of #1183 remains unchanged please resolve that ticket, also.

Cheers,

Michael



---

archive/issue_comments_007301.json:
```json
{
    "body": "Attachment [trac-1183-supportforquo-step1and2.patch](tarball://root/attachments/some-uuid/ticket1183/trac-1183-supportforquo-step1and2.patch) by @williamstein created at 2007-12-02 09:48:36",
    "created_at": "2007-12-02T09:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1183#issuecomment-7301",
    "user": "@williamstein"
}
```

Attachment [trac-1183-supportforquo-step1and2.patch](tarball://root/attachments/some-uuid/ticket1183/trac-1183-supportforquo-step1and2.patch) by @williamstein created at 2007-12-02 09:48:36



---

archive/issue_comments_007302.json:
```json
{
    "body": "Attachment [trac-1183-through_step_3.patch](tarball://root/attachments/some-uuid/ticket1183/trac-1183-through_step_3.patch) by @williamstein created at 2007-12-02 10:40:03",
    "created_at": "2007-12-02T10:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1183#issuecomment-7302",
    "user": "@williamstein"
}
```

Attachment [trac-1183-through_step_3.patch](tarball://root/attachments/some-uuid/ticket1183/trac-1183-through_step_3.patch) by @williamstein created at 2007-12-02 10:40:03



---

archive/issue_comments_007303.json:
```json
{
    "body": "further work, but still some issues....",
    "created_at": "2007-12-02T13:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1183#issuecomment-7303",
    "user": "@williamstein"
}
```

further work, but still some issues....



---

archive/issue_comments_007304.json:
```json
{
    "body": "Attachment [trac-1138-throughstep4.patch](tarball://root/attachments/some-uuid/ticket1183/trac-1138-throughstep4.patch) by @williamstein created at 2007-12-02 13:15:59\n\nNOT ready to be released yet.",
    "created_at": "2007-12-02T13:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1183#issuecomment-7304",
    "user": "@williamstein"
}
```

Attachment [trac-1138-throughstep4.patch](tarball://root/attachments/some-uuid/ticket1183/trac-1138-throughstep4.patch) by @williamstein created at 2007-12-02 13:15:59

NOT ready to be released yet.



---

archive/issue_comments_007305.json:
```json
{
    "body": "NOTE!!  Be sure to also apply\n\nhttp://trac.sagemath.org/sage_trac/ticket/1494",
    "created_at": "2007-12-13T22:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1183#issuecomment-7305",
    "user": "@williamstein"
}
```

NOTE!!  Be sure to also apply

http://trac.sagemath.org/sage_trac/ticket/1494



---

archive/issue_comments_007306.json:
```json
{
    "body": "Attachment [trac-1183-step5.patch](tarball://root/attachments/some-uuid/ticket1183/trac-1183-step5.patch) by @williamstein created at 2007-12-14 11:43:14",
    "created_at": "2007-12-14T11:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1183#issuecomment-7306",
    "user": "@williamstein"
}
```

Attachment [trac-1183-step5.patch](tarball://root/attachments/some-uuid/ticket1183/trac-1183-step5.patch) by @williamstein created at 2007-12-14 11:43:14



---

archive/issue_comments_007307.json:
```json
{
    "body": "Attachment [trac-1183-step6.patch](tarball://root/attachments/some-uuid/ticket1183/trac-1183-step6.patch) by @craigcitro created at 2007-12-15 13:01:48",
    "created_at": "2007-12-15T13:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1183#issuecomment-7307",
    "user": "@craigcitro"
}
```

Attachment [trac-1183-step6.patch](tarball://root/attachments/some-uuid/ticket1183/trac-1183-step6.patch) by @craigcitro created at 2007-12-15 13:01:48



---

archive/issue_comments_007308.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T13:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1183#issuecomment-7308",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_007309.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T13:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1183#issuecomment-7309",
    "user": "mabshoff"
}
```

Resolution: fixed
