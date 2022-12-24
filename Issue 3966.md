# Issue 3966: The ode cython example gives errors

archive/issues_003966.json:
```json
{
    "body": "Assignee: jkantor\n\nThe gsl ode_solver Cython/Pyrex example gives errors because the jacobian isn't passed (and doesn't need to be!).  This patch fixes the code and also changes the %pyrex to %cython\n\nIssue created by migration from https://trac.sagemath.org/ticket/3966\n\n",
    "created_at": "2008-08-27T15:47:56Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "title": "The ode cython example gives errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3966",
    "user": "jason"
}
```
Assignee: jkantor

The gsl ode_solver Cython/Pyrex example gives errors because the jacobian isn't passed (and doesn't need to be!).  This patch fixes the code and also changes the %pyrex to %cython

Issue created by migration from https://trac.sagemath.org/ticket/3966





---

archive/issue_comments_028491.json:
```json
{
    "body": "Attachment [ode-cython.patch](tarball://root/attachments/some-uuid/ticket3966/ode-cython.patch) by jason created at 2008-08-27 16:12:58",
    "created_at": "2008-08-27T16:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3966#issuecomment-28491",
    "user": "jason"
}
```

Attachment [ode-cython.patch](tarball://root/attachments/some-uuid/ticket3966/ode-cython.patch) by jason created at 2008-08-27 16:12:58



---

archive/issue_comments_028492.json:
```json
{
    "body": "This looks good to me.  All doctests still pass, and the cython example in the docs now works, although it is still not automatically tested.",
    "created_at": "2008-08-28T02:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3966#issuecomment-28492",
    "user": "jwmerrill"
}
```

This looks good to me.  All doctests still pass, and the cython example in the docs now works, although it is still not automatically tested.



---

archive/issue_comments_028493.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-29T03:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3966#issuecomment-28493",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_comments_028494.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T03:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3966#issuecomment-28494",
    "user": "mabshoff"
}
```

Resolution: fixed
