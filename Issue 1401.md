# Issue 1401: deprecate A[n] for n a matrix (easy to implement usability improvement)

archive/issues_001401.json:
```json
{
    "body": "Assignee: @williamstein\n\nSage currently works this way:\n\n```\nsage: a = matrix(ZZ, 2, [1..4])\nsage: a[1]\n(3, 4)\nsage: a.row(1)\n(3, 4)\nsage: a[1][0] = 5\nsage: a\n[1 2]\n[3 4]\n```\n\n\nInstead Sage should do this:\n\n\n```\nsage: a = matrix(ZZ, 2, [1..4])\nsage: a[1]\nboom!\nsage: a.row(1)\n(3, 4)\nsage: a[1][0] = 5\nboom!\n```\n\n\nWhere boom explains that one should use a.row(...) to get a row, or a[i,j] to get/set the ij entry.\n\nThis confuses the heck out of TONS of people!!!  (Not me, but others.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/1401\n\n",
    "created_at": "2007-12-04T23:57:36Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "deprecate A[n] for n a matrix (easy to implement usability improvement)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1401",
    "user": "@williamstein"
}
```
Assignee: @williamstein

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

archive/issue_comments_009034.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T21:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9034",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009035.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-12-06T21:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9035",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_009036.json:
```json
{
    "body": "Attachment [1401.patch](tarball://root/attachments/some-uuid/ticket1401/1401.patch) by @mwhansen created at 2007-12-06 23:15:40",
    "created_at": "2007-12-06T23:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9036",
    "user": "@mwhansen"
}
```

Attachment [1401.patch](tarball://root/attachments/some-uuid/ticket1401/1401.patch) by @mwhansen created at 2007-12-06 23:15:40



---

archive/issue_comments_009037.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2007-12-06T23:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9037",
    "user": "@mwhansen"
}
```

Patch attached.



---

archive/issue_comments_009038.json:
```json
{
    "body": "I just realized that a much better solution is to finish implementing immutable vectors and make the return of A[n] be an immutable row.  It accomplishes the same thing and is more usable.  So I did this.\n\nThat said, the above patch is fine -- using .row(...) all over in code is fine and faster.",
    "created_at": "2007-12-15T12:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9038",
    "user": "@williamstein"
}
```

I just realized that a much better solution is to finish implementing immutable vectors and make the return of A[n] be an immutable row.  It accomplishes the same thing and is more usable.  So I did this.

That said, the above patch is fine -- using .row(...) all over in code is fine and faster.



---

archive/issue_comments_009039.json:
```json
{
    "body": "Attachment [trac-1401-part2.patch](tarball://root/attachments/some-uuid/ticket1401/trac-1401-part2.patch) by @williamstein created at 2007-12-15 12:57:27",
    "created_at": "2007-12-15T12:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9039",
    "user": "@williamstein"
}
```

Attachment [trac-1401-part2.patch](tarball://root/attachments/some-uuid/ticket1401/trac-1401-part2.patch) by @williamstein created at 2007-12-15 12:57:27



---

archive/issue_comments_009040.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T13:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9040",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009041.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T13:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1401#issuecomment-9041",
    "user": "mabshoff"
}
```

Resolution: fixed
