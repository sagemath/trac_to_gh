# Issue 1257: [with patch] multi_polynomial_libsingular.pyx "random" segfault

archive/issues_001257.json:
```json
{
    "body": "Assignee: @williamstein\n\n`MPolynomialRing_libsingular.__dealloc__` changes the global Singular \"current ring\" to its wrapped ring, and then deletes the ring.  Since `__dealloc__` can get called at essentially random times (it can be called by the Python garbage collector, which can be called on any Python memory allocation), this means that at any time the Singular \"current ring\" may be changed to an invalid, deleted ring.\n\nMy patch changes the \"current ring\" back to its old value, after deleting the wrapped ring.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1257\n\n",
    "created_at": "2007-11-25T03:46:59Z",
    "labels": [
        "component: algebraic geometry",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.14",
    "title": "[with patch] multi_polynomial_libsingular.pyx \"random\" segfault",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1257",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

`MPolynomialRing_libsingular.__dealloc__` changes the global Singular "current ring" to its wrapped ring, and then deletes the ring.  Since `__dealloc__` can get called at essentially random times (it can be called by the Python garbage collector, which can be called on any Python memory allocation), this means that at any time the Singular "current ring" may be changed to an invalid, deleted ring.

My patch changes the "current ring" back to its old value, after deleting the wrapped ring.

Issue created by migration from https://trac.sagemath.org/ticket/1257





---

archive/issue_comments_007838.json:
```json
{
    "body": "Attachment [1257.patch](tarball://root/attachments/some-uuid/ticket1257/1257.patch) by cwitty created at 2007-11-25 03:48:44",
    "created_at": "2007-11-25T03:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1257#issuecomment-7838",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [1257.patch](tarball://root/attachments/some-uuid/ticket1257/1257.patch) by cwitty created at 2007-11-25 03:48:44



---

archive/issue_comments_007839.json:
```json
{
    "body": "Looks very good to me.",
    "created_at": "2007-11-25T05:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1257#issuecomment-7839",
    "user": "https://github.com/williamstein"
}
```

Looks very good to me.



---

archive/issue_events_003314.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-11-25T05:37:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1257",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1257#event-3314"
}
```



---

archive/issue_comments_007840.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-25T05:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1257",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1257#issuecomment-7840",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
