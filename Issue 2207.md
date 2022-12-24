# Issue 2207: fcp for matrices over SR

archive/issues_002207.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2207\n\n",
    "created_at": "2008-02-18T21:25:50Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "fcp for matrices over SR",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2207",
    "user": "@jasongrout"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/2207





---

archive/issue_comments_014566.json:
```json
{
    "body": "tidbits from mhansen's patch at 2028.",
    "created_at": "2008-02-18T21:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14566",
    "user": "@jasongrout"
}
```

tidbits from mhansen's patch at 2028.



---

archive/issue_comments_014567.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-02-18T21:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14567",
    "user": "@jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_014568.json:
```json
{
    "body": "Attachment [trac-2028-part1.patch](tarball://root/attachments/some-uuid/ticket2207/trac-2028-part1.patch) by @jasongrout created at 2008-02-18 21:26:29",
    "created_at": "2008-02-18T21:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14568",
    "user": "@jasongrout"
}
```

Attachment [trac-2028-part1.patch](tarball://root/attachments/some-uuid/ticket2207/trac-2028-part1.patch) by @jasongrout created at 2008-02-18 21:26:29



---

archive/issue_comments_014569.json:
```json
{
    "body": "Apply.",
    "created_at": "2008-02-19T00:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14569",
    "user": "@ncalexan"
}
```

Apply.



---

archive/issue_comments_014570.json:
```json
{
    "body": "Please rebase:\n\n```\nsage$ patch -p1 --dry-run < trac-2028-part1.patch\npatching file sage/matrix/matrix_symbolic_dense.pyx\nHunk #1 FAILED at 365.\n1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_symbolic_dense.pyx.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-19T15:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14570",
    "user": "mabshoff"
}
```

Please rebase:

```
sage$ patch -p1 --dry-run < trac-2028-part1.patch
patching file sage/matrix/matrix_symbolic_dense.pyx
Hunk #1 FAILED at 365.
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_symbolic_dense.pyx.rej
```


Cheers,

Michael



---

archive/issue_comments_014571.json:
```json
{
    "body": "This code made it in in #2053.",
    "created_at": "2008-03-05T00:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14571",
    "user": "@mwhansen"
}
```

This code made it in in #2053.



---

archive/issue_comments_014572.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T00:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14572",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_014573.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-03-05T01:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14573",
    "user": "@mwhansen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_014574.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-05T01:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14574",
    "user": "@mwhansen"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_014575.json:
```json
{
    "body": "Attachment [2207.patch](tarball://root/attachments/some-uuid/ticket2207/2207.patch) by @mwhansen created at 2008-03-05 01:09:01\n\nNew patch against 2.10.3.rc1 attached which adds missing doctests",
    "created_at": "2008-03-05T01:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14575",
    "user": "@mwhansen"
}
```

Attachment [2207.patch](tarball://root/attachments/some-uuid/ticket2207/2207.patch) by @mwhansen created at 2008-03-05 01:09:01

New patch against 2.10.3.rc1 attached which adds missing doctests



---

archive/issue_comments_014576.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc2 - due to some hg stupidity parts of this patch made it in rc0. Mike Hansen's latest patch adds the missing docstring and doctest.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-05T05:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14576",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc2 - due to some hg stupidity parts of this patch made it in rc0. Mike Hansen's latest patch adds the missing docstring and doctest.

Cheers,

Michael



---

archive/issue_comments_014577.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T05:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14577",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014578.json:
```json
{
    "body": "When I tested 2.10.3.rc2 I got this:\n\n\n```\nsage -t  devel/sage-main/sage/matrix/matrix_symbolic_dense.pyxemacs devel/sage-main/sage/matrix/matrix_symbolic_dense.pyx**********************************************************************\nFile \"matrix_symbolic_dense.pyx\", line 871:\n    sage: list(a.fcp())\nExpected:\n    [(x^2 - 65*x - 250, 1), (x, 3)]\nGot:\n    [(x, 3), (x^2 - 65*x - 250, 1)]\n**********************************************************************\n```\n\n\nand I suggest changing line 871 from\n\n```\n            sage: list(a.fcp())\n```\n\nto\n\n```\n            sage: sorted(list(a.fcp()))\n```\n",
    "created_at": "2008-03-05T22:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14578",
    "user": "@JohnCremona"
}
```

When I tested 2.10.3.rc2 I got this:


```
sage -t  devel/sage-main/sage/matrix/matrix_symbolic_dense.pyxemacs devel/sage-main/sage/matrix/matrix_symbolic_dense.pyx**********************************************************************
File "matrix_symbolic_dense.pyx", line 871:
    sage: list(a.fcp())
Expected:
    [(x^2 - 65*x - 250, 1), (x, 3)]
Got:
    [(x, 3), (x^2 - 65*x - 250, 1)]
**********************************************************************
```


and I suggest changing line 871 from

```
            sage: list(a.fcp())
```

to

```
            sage: sorted(list(a.fcp()))
```

