# Issue 806: matrix_integer_dense.elementary_divisors return a mutable object

archive/issues_000806.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following code causes incorrect output:\n\n```\nsage: M=random_matrix(ZZ,3,2)\n\nsage: M.elementary_divisors()\n [1, 1, 0]\n\nsage: edivs=M.elementary_divisors()\n\nsage: edivs.pop()\n 0\n\nsage: edivs\n [1, 1]\n\nsage: M.elementary_divisors()\n [1, 1]\n```\n\nThe problem seems to be elementary_divisors() caches the result, but returns a mutable object.\n\nIssue created by migration from https://trac.sagemath.org/ticket/806\n\n",
    "created_at": "2007-10-03T14:52:20Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "matrix_integer_dense.elementary_divisors return a mutable object",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/806",
    "user": "https://github.com/syazdani77"
}
```
Assignee: @williamstein

The following code causes incorrect output:

```
sage: M=random_matrix(ZZ,3,2)

sage: M.elementary_divisors()
 [1, 1, 0]

sage: edivs=M.elementary_divisors()

sage: edivs.pop()
 0

sage: edivs
 [1, 1]

sage: M.elementary_divisors()
 [1, 1]
```

The problem seems to be elementary_divisors() caches the result, but returns a mutable object.

Issue created by migration from https://trac.sagemath.org/ticket/806





---

archive/issue_comments_004854.json:
```json
{
    "body": "Patch attached.\n\n\n```\nsage: M=random_matrix(ZZ,3,2)\nsage: \nsage: M.elementary_divisors()\n[1, 1, 0]\nsage: edivs = M.elementary_divisors()\nsage: edivs.pop()\n0\nsage: edivs\n[1, 1]\nsage: M.elementary_divisors()\n[1, 1, 0]\n```\n",
    "created_at": "2007-10-04T11:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/806#issuecomment-4854",
    "user": "https://github.com/mwhansen"
}
```

Patch attached.


```
sage: M=random_matrix(ZZ,3,2)
sage: 
sage: M.elementary_divisors()
[1, 1, 0]
sage: edivs = M.elementary_divisors()
sage: edivs.pop()
0
sage: edivs
[1, 1]
sage: M.elementary_divisors()
[1, 1, 0]
```




---

archive/issue_comments_004855.json:
```json
{
    "body": "Attachment [806.patch](tarball://root/attachments/some-uuid/ticket806/806.patch) by @mwhansen created at 2007-10-04 11:50:20",
    "created_at": "2007-10-04T11:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/806#issuecomment-4855",
    "user": "https://github.com/mwhansen"
}
```

Attachment [806.patch](tarball://root/attachments/some-uuid/ticket806/806.patch) by @mwhansen created at 2007-10-04 11:50:20



---

archive/issue_comments_004856.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T18:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/806#issuecomment-4856",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
