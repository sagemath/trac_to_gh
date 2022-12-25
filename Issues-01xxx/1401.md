# Issue 1401: [with patch, positive review that is a patch itself] deprecate A[n] for n a matrix (easy to implement usability improvement)

archive/issues_001401.json:
```json
{
    "body": "Assignee: @mwhansen\n\nSage currently works this way:\n\n```\nsage: a = matrix(ZZ, 2, [1..4])\nsage: a[1]\n(3, 4)\nsage: a.row(1)\n(3, 4)\nsage: a[1][0] = 5\nsage: a\n[1 2]\n[3 4]\n```\n\nInstead Sage should do this:\n\n```\nsage: a = matrix(ZZ, 2, [1..4])\nsage: a[1]\nboom!\nsage: a.row(1)\n(3, 4)\nsage: a[1][0] = 5\nboom!\n```\n\nWhere boom explains that one should use a.row(...) to get a row, or a[i,j] to get/set the ij entry.\n\nThis confuses the heck out of TONS of people!!!  (Not me, but others.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1401\n\n",
    "closed_at": "2007-12-15T13:32:06Z",
    "created_at": "2007-12-04T23:57:36Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch, positive review that is a patch itself] deprecate A[n] for n a matrix (easy to implement usability improvement)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1401",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mwhansen

Sage currently works this way:

```
sage: a = matrix(ZZ, 2, [1..4])
sage: a[1]
(3, 4)
sage: a.row(1)
(3, 4)
sage: a[1][0] = 5
sage: a
[1 2]
[3 4]
```

Instead Sage should do this:

```
sage: a = matrix(ZZ, 2, [1..4])
sage: a[1]
boom!
sage: a.row(1)
(3, 4)
sage: a[1][0] = 5
boom!
```

Where boom explains that one should use a.row(...) to get a row, or a[i,j] to get/set the ij entry.

This confuses the heck out of TONS of people!!!  (Not me, but others.)

Issue created by migration from https://trac.sagemath.org/ticket/1401





---

archive/issue_comments_009010.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T21:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9010",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009011.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-12-06T21:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9011",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_009012.json:
```json
{
    "body": "Attachment [1401.patch](tarball://root/attachments/some-uuid/ticket1401/1401.patch) by @mwhansen created at 2007-12-06 23:15:40",
    "created_at": "2007-12-06T23:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9012",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1401.patch](tarball://root/attachments/some-uuid/ticket1401/1401.patch) by @mwhansen created at 2007-12-06 23:15:40



---

archive/issue_comments_009013.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2007-12-06T23:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9013",
    "user": "https://github.com/mwhansen"
}
```

Patch attached.



---

archive/issue_comments_009014.json:
```json
{
    "body": "I just realized that a much better solution is to finish implementing immutable vectors and make the return of A[n] be an immutable row.  It accomplishes the same thing and is more usable.  So I did this.\n\nThat said, the above patch is fine -- using .row(...) all over in code is fine and faster.",
    "created_at": "2007-12-15T12:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9014",
    "user": "https://github.com/williamstein"
}
```

I just realized that a much better solution is to finish implementing immutable vectors and make the return of A[n] be an immutable row.  It accomplishes the same thing and is more usable.  So I did this.

That said, the above patch is fine -- using .row(...) all over in code is fine and faster.



---

archive/issue_comments_009015.json:
```json
{
    "body": "Attachment [trac-1401-part2.patch](tarball://root/attachments/some-uuid/ticket1401/trac-1401-part2.patch) by @williamstein created at 2007-12-15 12:57:27",
    "created_at": "2007-12-15T12:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9015",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1401-part2.patch](tarball://root/attachments/some-uuid/ticket1401/trac-1401-part2.patch) by @williamstein created at 2007-12-15 12:57:27



---

archive/issue_comments_009016.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T13:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_events_003617.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T13:32:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1401#event-3617"
}
```



---

archive/issue_comments_009017.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T13:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9017",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
