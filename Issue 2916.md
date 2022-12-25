# Issue 2916: [with patch; needs review] invalid coercion between non-prime finite fields

archive/issues_002916.json:
```json
{
    "body": "Assignee: @williamstein\n\nAs reported by Kiran Kedlaya on sage-devel:\n\n\n```\nsage: F9.<a> = GF(9); F81.<b> = GF(81); F81(a)\n0\n```\n\n\nThis is caused by a missing 'else' in the `FiniteField_givaro` constructor. The attached patch throws a `TypeError` in this case and adds this example as a doctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2916\n\n",
    "created_at": "2008-04-14T14:57:13Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] invalid coercion between non-prime finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2916",
    "user": "https://github.com/wjp"
}
```
Assignee: @williamstein

As reported by Kiran Kedlaya on sage-devel:


```
sage: F9.<a> = GF(9); F81.<b> = GF(81); F81(a)
0
```


This is caused by a missing 'else' in the `FiniteField_givaro` constructor. The attached patch throws a `TypeError` in this case and adds this example as a doctest.

Issue created by migration from https://trac.sagemath.org/ticket/2916





---

archive/issue_comments_020044.json:
```json
{
    "body": "Attachment [finite_field_coercion.patch](tarball://root/attachments/some-uuid/ticket2916/finite_field_coercion.patch) by @wjp created at 2008-04-14 14:57:38",
    "created_at": "2008-04-14T14:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2916#issuecomment-20044",
    "user": "https://github.com/wjp"
}
```

Attachment [finite_field_coercion.patch](tarball://root/attachments/some-uuid/ticket2916/finite_field_coercion.patch) by @wjp created at 2008-04-14 14:57:38



---

archive/issue_comments_020045.json:
```json
{
    "body": "The patch passes doctests on sage.math. Hopefully someone will review this soon.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-14T20:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2916#issuecomment-20045",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch passes doctests on sage.math. Hopefully someone will review this soon.

Cheers,

Michael



---

archive/issue_comments_020046.json:
```json
{
    "body": "Patch looks good and \n\n\n```\n[21:20] <mabshoff> Can you referee #2916?\n[21:20] <mabshoff> It passes doctests on sage.math\n```\n\n\n=> **positive review**",
    "created_at": "2008-04-14T20:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2916#issuecomment-20046",
    "user": "https://github.com/malb"
}
```

Patch looks good and 


```
[21:20] <mabshoff> Can you referee #2916?
[21:20] <mabshoff> It passes doctests on sage.math
```


=> **positive review**



---

archive/issue_comments_020047.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T20:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2916#issuecomment-20047",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003118.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-14T20:36:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2916",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2916#event-3118"
}
```



---

archive/issue_comments_020048.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-14T20:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2916#issuecomment-20048",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha5
