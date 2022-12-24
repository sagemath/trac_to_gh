# Issue 6590: [with patch, needs review] Cython __new__ should be __cinit__

archive/issues_006590.json:
```json
{
    "body": "Assignee: tbd\n\nThis changed a while back, but as long as the old form is in the library we won't be able to really implement a (Python-style) `__new__` and also people will keep using it in new code by analogy. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6590\n\n",
    "created_at": "2009-07-22T14:21:15Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] Cython __new__ should be __cinit__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6590",
    "user": "robertwb"
}
```
Assignee: tbd

This changed a while back, but as long as the old form is in the library we won't be able to really implement a (Python-style) `__new__` and also people will keep using it in new code by analogy. 

Issue created by migration from https://trac.sagemath.org/ticket/6590





---

archive/issue_comments_053931.json:
```json
{
    "body": "Attachment [6590-cinit.patch](tarball://root/attachments/some-uuid/ticket6590/6590-cinit.patch) by jason created at 2009-07-25 05:59:11\n\nHow come the some of the new __cinit__ functions have different signatures from the corresponding __init__ functions?  I thought the signatures should be the same, or at least the __cinit__ should have a *args or **kwds to accept the arguments passed to __init__\n\n\nIn particular, I refer to sage/libs/ntl/ntl_mat_GF2.pyx, sage/libs/ntl/ntl_mat_ZZ.pyx,  sage/matrix/matrix_integer_2x2.pyx, etc.",
    "created_at": "2009-07-25T05:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6590#issuecomment-53931",
    "user": "jason"
}
```

Attachment [6590-cinit.patch](tarball://root/attachments/some-uuid/ticket6590/6590-cinit.patch) by jason created at 2009-07-25 05:59:11

How come the some of the new __cinit__ functions have different signatures from the corresponding __init__ functions?  I thought the signatures should be the same, or at least the __cinit__ should have a *args or **kwds to accept the arguments passed to __init__


In particular, I refer to sage/libs/ntl/ntl_mat_GF2.pyx, sage/libs/ntl/ntl_mat_ZZ.pyx,  sage/matrix/matrix_integer_2x2.pyx, etc.



---

archive/issue_comments_053932.json:
```json
{
    "body": "If no __init__ parameters are not needed by __cinit__ they can simply be omitted. This saves on argument-parsing code, especially as **kwds needs to construct an empty dictionary each time. Also note that __cinit__ is called on PY_NEW, so the savings here is really nice. (Essentially, `__cinit__(self)` is implicitly `__cinit__(self, *args, **kwds)` where *args and **kwds are not parsed because they're not needed.",
    "created_at": "2009-07-25T10:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6590#issuecomment-53932",
    "user": "robertwb"
}
```

If no __init__ parameters are not needed by __cinit__ they can simply be omitted. This saves on argument-parsing code, especially as **kwds needs to construct an empty dictionary each time. Also note that __cinit__ is called on PY_NEW, so the savings here is really nice. (Essentially, `__cinit__(self)` is implicitly `__cinit__(self, *args, **kwds)` where *args and **kwds are not parsed because they're not needed.



---

archive/issue_comments_053933.json:
```json
{
    "body": "Attachment [6590-cinit_rebased.patch](tarball://root/attachments/some-uuid/ticket6590/6590-cinit_rebased.patch) by AlexGhitza created at 2009-08-17 14:06:44\n\nrebased against sage-4.1.1, apply instead of previous patch",
    "created_at": "2009-08-17T14:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6590#issuecomment-53933",
    "user": "AlexGhitza"
}
```

Attachment [6590-cinit_rebased.patch](tarball://root/attachments/some-uuid/ticket6590/6590-cinit_rebased.patch) by AlexGhitza created at 2009-08-17 14:06:44

rebased against sage-4.1.1, apply instead of previous patch



---

archive/issue_comments_053934.json:
```json
{
    "body": "Positive review.  I had to rebase it against sage-4.1.1 since it didn't apply cleanly.",
    "created_at": "2009-08-17T14:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6590#issuecomment-53934",
    "user": "AlexGhitza"
}
```

Positive review.  I had to rebase it against sage-4.1.1 since it didn't apply cleanly.



---

archive/issue_comments_053935.json:
```json
{
    "body": "Merged `6590-cinit_rebased.patch`.",
    "created_at": "2009-08-24T13:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6590#issuecomment-53935",
    "user": "mvngu"
}
```

Merged `6590-cinit_rebased.patch`.



---

archive/issue_comments_053936.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-24T13:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6590#issuecomment-53936",
    "user": "mvngu"
}
```

Resolution: fixed
