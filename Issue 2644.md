# Issue 2644: doctest failures in matrix_real_double_dense

archive/issues_002644.json:
```json
{
    "body": "Assignee: was\n\nOn 2.11alpha0, the doctest for `__invert__` randomly fails\n\nIssue created by migration from https://trac.sagemath.org/ticket/2644\n\n",
    "created_at": "2008-03-22T14:39:47Z",
    "labels": [
        "linear algebra",
        "blocker",
        "bug"
    ],
    "title": "doctest failures in matrix_real_double_dense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2644",
    "user": "dfdeshom"
}
```
Assignee: was

On 2.11alpha0, the doctest for `__invert__` randomly fails

Issue created by migration from https://trac.sagemath.org/ticket/2644





---

archive/issue_comments_018176.json:
```json
{
    "body": "Attachment [2644.patch](tarball://root/attachments/some-uuid/ticket2644/2644.patch) by dfdeshom created at 2008-03-22 15:36:24\n\npatch against 2.11alpha",
    "created_at": "2008-03-22T15:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18176",
    "user": "dfdeshom"
}
```

Attachment [2644.patch](tarball://root/attachments/some-uuid/ticket2644/2644.patch) by dfdeshom created at 2008-03-22 15:36:24

patch against 2.11alpha



---

archive/issue_comments_018177.json:
```json
{
    "body": "Here is a patch against 2.11alpha0",
    "created_at": "2008-03-22T15:37:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18177",
    "user": "dfdeshom"
}
```

Here is a patch against 2.11alpha0



---

archive/issue_comments_018178.json:
```json
{
    "body": "Changing assignee from was to dfdeshom.",
    "created_at": "2008-03-22T15:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18178",
    "user": "dfdeshom"
}
```

Changing assignee from was to dfdeshom.



---

archive/issue_comments_018179.json:
```json
{
    "body": "Looks good and tests fine.",
    "created_at": "2008-03-22T15:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18179",
    "user": "AlexGhitza"
}
```

Looks good and tests fine.



---

archive/issue_comments_018180.json:
```json
{
    "body": "Yep, I think this is the right way to fix this. It is clear from the context that the inversion of the matrix should fail and am somewhat surprised that the numerical noise is large enough that the determinant of a rank deficient matrix like A in this example is not even close to zero.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T19:13:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18180",
    "user": "mabshoff"
}
```

Yep, I think this is the right way to fix this. It is clear from the context that the inversion of the matrix should fail and am somewhat surprised that the numerical noise is large enough that the determinant of a rank deficient matrix like A in this example is not even close to zero.

Cheers,

Michael



---

archive/issue_comments_018181.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-22T19:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18181",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_comments_018182.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T19:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2644#issuecomment-18182",
    "user": "mabshoff"
}
```

Resolution: fixed
