# Issue 1701: attempt to clean up currRing if deallocated

archive/issues_001701.json:
```json
{
    "body": "Assignee: malb\n\nThis patch used to be attached to #1541 but logically doesn't belong there.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1701\n\n",
    "created_at": "2008-01-06T13:23:05Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "attempt to clean up currRing if deallocated",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1701",
    "user": "malb"
}
```
Assignee: malb

This patch used to be attached to #1541 but logically doesn't belong there.

Issue created by migration from https://trac.sagemath.org/ticket/1701





---

archive/issue_comments_010779.json:
```json
{
    "body": "Attachment [currRing.patch](tarball://root/attachments/some-uuid/ticket1701/currRing.patch) by mabshoff created at 2008-01-06 16:10:52\n\nI am under the impression that this patch already got merged, but I will investigate.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-06T16:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1701#issuecomment-10779",
    "user": "mabshoff"
}
```

Attachment [currRing.patch](tarball://root/attachments/some-uuid/ticket1701/currRing.patch) by mabshoff created at 2008-01-06 16:10:52

I am under the impression that this patch already got merged, but I will investigate.

Cheers,

Michael



---

archive/issue_comments_010780.json:
```json
{
    "body": "I just checked, it is not merged yet:\n\nmulti_polynomial_libsingular.pyx in Sage 2.9.2:\n\n\n```\n    def __dealloc__(self):\n        \"\"\"\n        \"\"\"\n        cdef ring *oldRing = NULL\n        if currRing != self._ring:\n            oldRing = currRing\n            rChangeCurrRing(self._ring)\n        rDelete(self._ring)\n        if oldRing != NULL:\n            rChangeCurrRing(oldRing)\n```\n",
    "created_at": "2008-01-06T16:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1701#issuecomment-10780",
    "user": "malb"
}
```

I just checked, it is not merged yet:

multi_polynomial_libsingular.pyx in Sage 2.9.2:


```
    def __dealloc__(self):
        """
        """
        cdef ring *oldRing = NULL
        if currRing != self._ring:
            oldRing = currRing
            rChangeCurrRing(self._ring)
        rDelete(self._ring)
        if oldRing != NULL:
            rChangeCurrRing(oldRing)
```




---

archive/issue_comments_010781.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-07T17:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1701#issuecomment-10781",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010782.json:
```json
{
    "body": "Looks good to me, Merged in Sage 2.10.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-07T17:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1701#issuecomment-10782",
    "user": "mabshoff"
}
```

Looks good to me, Merged in Sage 2.10.alpha0.

Cheers,

Michael
