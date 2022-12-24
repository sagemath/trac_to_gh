# Issue 771: GF(p^n) vector() NotImplemented for p^n > 2^16

archive/issues_000771.json:
```json
{
    "body": "Assignee: was\n\n\n```\nK.<a> = GF(2^15, 'a')\nV = K.vector_space()\nz = (a+1)^13\nV(z)\n\n(1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0)\n```\n\n\n2^16: Error!\n\n```\nK.<a> = GF(2^16, 'a')\nV = K.vector_space()\nz = (a+1)^13\nV(z)\n\n\n\nException (click to the left for traceback):\n...\nTypeError: can't initialize vector from nonzero non-list\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/771\n\n",
    "created_at": "2007-10-01T13:26:30Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "GF(p^n) vector() NotImplemented for p^n > 2^16",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/771",
    "user": "malb"
}
```
Assignee: was


```
K.<a> = GF(2^15, 'a')
V = K.vector_space()
z = (a+1)^13
V(z)

(1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0)
```


2^16: Error!

```
K.<a> = GF(2^16, 'a')
V = K.vector_space()
z = (a+1)^13
V(z)



Exception (click to the left for traceback):
...
TypeError: can't initialize vector from nonzero non-list
```


Issue created by migration from https://trac.sagemath.org/ticket/771





---

archive/issue_comments_004580.json:
```json
{
    "body": "Attachment [K_vector.patch](tarball://root/attachments/some-uuid/ticket771/K_vector.patch) by malb created at 2007-10-20 21:57:29",
    "created_at": "2007-10-20T21:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/771#issuecomment-4580",
    "user": "malb"
}
```

Attachment [K_vector.patch](tarball://root/attachments/some-uuid/ticket771/K_vector.patch) by malb created at 2007-10-20 21:57:29



---

archive/issue_comments_004581.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T22:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/771#issuecomment-4581",
    "user": "was"
}
```

Resolution: fixed
