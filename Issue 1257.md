# Issue 1257: [with patch] multi_polynomial_libsingular.pyx "random" segfault

archive/issues_001257.json:
```json
{
    "body": "Assignee: was\n\n`MPolynomialRing_libsingular.__dealloc__` changes the global Singular \"current ring\" to its wrapped ring, and then deletes the ring.  Since `__dealloc__` can get called at essentially random times (it can be called by the Python garbage collector, which can be called on any Python memory allocation), this means that at any time the Singular \"current ring\" may be changed to an invalid, deleted ring.\n\nMy patch changes the \"current ring\" back to its old value, after deleting the wrapped ring.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1257\n\n",
    "created_at": "2007-11-25T03:46:59Z",
    "labels": [
        "algebraic geometry",
        "critical",
        "bug"
    ],
    "title": "[with patch] multi_polynomial_libsingular.pyx \"random\" segfault",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1257",
    "user": "cwitty"
}
```
Assignee: was

`MPolynomialRing_libsingular.__dealloc__` changes the global Singular "current ring" to its wrapped ring, and then deletes the ring.  Since `__dealloc__` can get called at essentially random times (it can be called by the Python garbage collector, which can be called on any Python memory allocation), this means that at any time the Singular "current ring" may be changed to an invalid, deleted ring.

My patch changes the "current ring" back to its old value, after deleting the wrapped ring.

Issue created by migration from https://trac.sagemath.org/ticket/1257





---

archive/issue_comments_007861.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-25T03:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1257#issuecomment-7861",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_007862.json:
```json
{
    "body": "Looks very good to me.",
    "created_at": "2007-11-25T05:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1257#issuecomment-7862",
    "user": "was"
}
```

Looks very good to me.



---

archive/issue_comments_007863.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-25T05:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1257#issuecomment-7863",
    "user": "was"
}
```

Resolution: fixed
