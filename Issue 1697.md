# Issue 1697: two polynomial_modn_dense_ntl.pyx memleaks

archive/issues_001697.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe classes Polynomial_dense_modn_ntl_zz and Polynomial_dense_modn_ntl_ZZ construct a zz_pX_c resp. ZZ_pX_c object, but have no __dealloc__ method to destruct them.\n\nPatch attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1697\n\n",
    "created_at": "2008-01-05T23:53:45Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.3",
    "title": "two polynomial_modn_dense_ntl.pyx memleaks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1697",
    "user": "https://github.com/wjp"
}
```
Assignee: mabshoff

The classes Polynomial_dense_modn_ntl_zz and Polynomial_dense_modn_ntl_ZZ construct a zz_pX_c resp. ZZ_pX_c object, but have no __dealloc__ method to destruct them.

Patch attached.

Issue created by migration from https://trac.sagemath.org/ticket/1697





---

archive/issue_comments_010740.json:
```json
{
    "body": "Attachment [7953.patch](tarball://root/attachments/some-uuid/ticket1697/7953.patch) by @wjp created at 2008-01-05 23:54:03",
    "created_at": "2008-01-05T23:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1697#issuecomment-10740",
    "user": "https://github.com/wjp"
}
```

Attachment [7953.patch](tarball://root/attachments/some-uuid/ticket1697/7953.patch) by @wjp created at 2008-01-05 23:54:03



---

archive/issue_comments_010741.json:
```json
{
    "body": "Looks good to me, extensively tested (6+ hours of valgrinding)\n\nCheers,\n\nMichael",
    "created_at": "2008-01-06T13:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1697#issuecomment-10741",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me, extensively tested (6+ hours of valgrinding)

Cheers,

Michael



---

archive/issue_comments_010742.json:
```json
{
    "body": "Merged in 2.9.3",
    "created_at": "2008-01-06T13:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1697#issuecomment-10742",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.3



---

archive/issue_comments_010743.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-06T13:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1697#issuecomment-10743",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
