# Issue 3966: The ode cython example gives errors

archive/issues_003966.json:
```json
{
    "body": "Assignee: jkantor\n\nThe gsl ode_solver Cython/Pyrex example gives errors because the jacobian isn't passed (and doesn't need to be!).  This patch fixes the code and also changes the %pyrex to %cython\n\nIssue created by migration from https://trac.sagemath.org/ticket/3966\n\n",
    "created_at": "2008-08-27T15:47:56Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "The ode cython example gives errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3966",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jkantor

The gsl ode_solver Cython/Pyrex example gives errors because the jacobian isn't passed (and doesn't need to be!).  This patch fixes the code and also changes the %pyrex to %cython

Issue created by migration from https://trac.sagemath.org/ticket/3966





---

archive/issue_comments_028433.json:
```json
{
    "body": "Attachment [ode-cython.patch](tarball://root/attachments/some-uuid/ticket3966/ode-cython.patch) by @jasongrout created at 2008-08-27 16:12:58",
    "created_at": "2008-08-27T16:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3966#issuecomment-28433",
    "user": "https://github.com/jasongrout"
}
```

Attachment [ode-cython.patch](tarball://root/attachments/some-uuid/ticket3966/ode-cython.patch) by @jasongrout created at 2008-08-27 16:12:58



---

archive/issue_comments_028434.json:
```json
{
    "body": "This looks good to me.  All doctests still pass, and the cython example in the docs now works, although it is still not automatically tested.",
    "created_at": "2008-08-28T02:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3966#issuecomment-28434",
    "user": "https://github.com/jicama"
}
```

This looks good to me.  All doctests still pass, and the cython example in the docs now works, although it is still not automatically tested.



---

archive/issue_comments_028435.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-29T03:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3966#issuecomment-28435",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_comments_028436.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T03:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3966#issuecomment-28436",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
