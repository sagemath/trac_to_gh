# Issue 885: 2.8.7-alpha0: doctest failure in rings/morphism.pyx (loads/dumps)

archive/issues_000885.json:
```json
{
    "body": "Assignee: failure\n\nOn sage.math:\n\n```\nFile \"morphism.pyx\", line 312:\n    sage: c == loads(dumps(c))\nExpected:\n    True\nGot:\n    False\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/885\n\n",
    "created_at": "2007-10-13T20:23:36Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "2.8.7-alpha0: doctest failure in rings/morphism.pyx (loads/dumps)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/885",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: failure

On sage.math:

```
File "morphism.pyx", line 312:
    sage: c == loads(dumps(c))
Expected:
    True
Got:
    False
```


Issue created by migration from https://trac.sagemath.org/ticket/885





---

archive/issue_comments_005453.json:
```json
{
    "body": "Attachment [6931.patch](tarball://root/attachments/some-uuid/ticket885/6931.patch) by cwitty created at 2007-10-13 22:35:26\n\nChanged class RingHomomorphism_im_gens to use _cmp_c_impl (this is necessary to make Python subclasses compare correctly).",
    "created_at": "2007-10-13T22:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/885#issuecomment-5453",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [6931.patch](tarball://root/attachments/some-uuid/ticket885/6931.patch) by cwitty created at 2007-10-13 22:35:26

Changed class RingHomomorphism_im_gens to use _cmp_c_impl (this is necessary to make Python subclasses compare correctly).



---

archive/issue_events_000999.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-14T22:56:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/885",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/885#event-999"
}
```



---

archive/issue_comments_005454.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T22:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/885#issuecomment-5454",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
