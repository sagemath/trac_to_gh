# Issue 2727: [with patch; needs review] uninitialized cdef in multi_polynomial_libsingular.pyx

archive/issues_002727.json:
```json
{
    "body": "Assignee: tabbott\n\nThe mysterious libsingular.dll errors in the Debian SAGE port were caused by an uninitialized variable masking the real error.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2727\n\n",
    "created_at": "2008-03-29T22:32:55Z",
    "labels": [
        "debian-package",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] uninitialized cdef in multi_polynomial_libsingular.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2727",
    "user": "tabbott"
}
```
Assignee: tabbott

The mysterious libsingular.dll errors in the Debian SAGE port were caused by an uninitialized variable masking the real error.

Issue created by migration from https://trac.sagemath.org/ticket/2727





---

archive/issue_comments_018786.json:
```json
{
    "body": "Attachment\n\nPatch looks good to me. Positive review.",
    "created_at": "2008-03-29T23:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2727#issuecomment-18786",
    "user": "mabshoff"
}
```

Attachment

Patch looks good to me. Positive review.



---

archive/issue_comments_018787.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T23:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2727#issuecomment-18787",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018788.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T23:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2727#issuecomment-18788",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0
