# Issue 2644: doctest failures in matrix_real_double_dense

archive/issues_002644.json:
```json
{
    "body": "Assignee: @williamstein\n\nOn 2.11alpha0, the doctest for `__invert__` randomly fails\n\nIssue created by migration from https://trac.sagemath.org/ticket/2644\n\n",
    "created_at": "2008-03-22T14:39:47Z",
    "labels": [
        "component: linear algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "doctest failures in matrix_real_double_dense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2644",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @williamstein

On 2.11alpha0, the doctest for `__invert__` randomly fails

Issue created by migration from https://trac.sagemath.org/ticket/2644





---

archive/issue_comments_018137.json:
```json
{
    "body": "Attachment [2644.patch](tarball://root/attachments/some-uuid/ticket2644/2644.patch) by @dfdeshom created at 2008-03-22 15:36:24\n\npatch against 2.11alpha",
    "created_at": "2008-03-22T15:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18137",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2644.patch](tarball://root/attachments/some-uuid/ticket2644/2644.patch) by @dfdeshom created at 2008-03-22 15:36:24

patch against 2.11alpha



---

archive/issue_comments_018138.json:
```json
{
    "body": "Here is a patch against 2.11alpha0",
    "created_at": "2008-03-22T15:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18138",
    "user": "https://github.com/dfdeshom"
}
```

Here is a patch against 2.11alpha0



---

archive/issue_comments_018139.json:
```json
{
    "body": "Changing assignee from @williamstein to @dfdeshom.",
    "created_at": "2008-03-22T15:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18139",
    "user": "https://github.com/dfdeshom"
}
```

Changing assignee from @williamstein to @dfdeshom.



---

archive/issue_comments_018140.json:
```json
{
    "body": "Looks good and tests fine.",
    "created_at": "2008-03-22T15:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18140",
    "user": "https://github.com/aghitza"
}
```

Looks good and tests fine.



---

archive/issue_comments_018141.json:
```json
{
    "body": "Yep, I think this is the right way to fix this. It is clear from the context that the inversion of the matrix should fail and am somewhat surprised that the numerical noise is large enough that the determinant of a rank deficient matrix like A in this example is not even close to zero.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T19:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18141",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yep, I think this is the right way to fix this. It is clear from the context that the inversion of the matrix should fail and am somewhat surprised that the numerical noise is large enough that the determinant of a rank deficient matrix like A in this example is not even close to zero.

Cheers,

Michael



---

archive/issue_comments_018142.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-22T19:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18142",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_events_006195.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-22T19:14:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2644#event-6195"
}
```



---

archive/issue_comments_018143.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T19:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18143",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
