# Issue 2727: [with patch; needs review] uninitialized cdef in multi_polynomial_libsingular.pyx

archive/issues_002727.json:
```json
{
    "body": "Assignee: @timabbott\n\nThe mysterious libsingular.dll errors in the Debian SAGE port were caused by an uninitialized variable masking the real error.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2727\n\n",
    "created_at": "2008-03-29T22:32:55Z",
    "labels": [
        "component: debian-package",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch; needs review] uninitialized cdef in multi_polynomial_libsingular.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2727",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

The mysterious libsingular.dll errors in the Debian SAGE port were caused by an uninitialized variable masking the real error.

Issue created by migration from https://trac.sagemath.org/ticket/2727





---

archive/issue_comments_018747.json:
```json
{
    "body": "Attachment [sage-singular-lib.patch](tarball://root/attachments/some-uuid/ticket2727/sage-singular-lib.patch) by mabshoff created at 2008-03-29 23:06:03\n\nPatch looks good to me. Positive review.",
    "created_at": "2008-03-29T23:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2727#issuecomment-18747",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-singular-lib.patch](tarball://root/attachments/some-uuid/ticket2727/sage-singular-lib.patch) by mabshoff created at 2008-03-29 23:06:03

Patch looks good to me. Positive review.



---

archive/issue_comments_018748.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T23:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2727#issuecomment-18748",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018749.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T23:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2727#issuecomment-18749",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_events_002915.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-29T23:06:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2727",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2727#event-2915"
}
```
