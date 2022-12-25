# Issue 2207: fcp for matrices over SR

archive/issues_002207.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2207\n\n",
    "created_at": "2008-02-18T21:25:50Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "fcp for matrices over SR",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2207",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/2207





---

archive/issue_comments_014535.json:
```json
{
    "body": "tidbits from mhansen's patch at 2028.",
    "created_at": "2008-02-18T21:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14535",
    "user": "https://github.com/jasongrout"
}
```

tidbits from mhansen's patch at 2028.



---

archive/issue_comments_014536.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-02-18T21:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14536",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_014537.json:
```json
{
    "body": "Attachment [trac-2028-part1.patch](tarball://root/attachments/some-uuid/ticket2207/trac-2028-part1.patch) by @jasongrout created at 2008-02-18 21:26:29",
    "created_at": "2008-02-18T21:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14537",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-2028-part1.patch](tarball://root/attachments/some-uuid/ticket2207/trac-2028-part1.patch) by @jasongrout created at 2008-02-18 21:26:29



---

archive/issue_comments_014538.json:
```json
{
    "body": "Apply.",
    "created_at": "2008-02-19T00:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14538",
    "user": "https://github.com/ncalexan"
}
```

Apply.



---

archive/issue_comments_014539.json:
```json
{
    "body": "Please rebase:\n\n```\nsage$ patch -p1 --dry-run < trac-2028-part1.patch\npatching file sage/matrix/matrix_symbolic_dense.pyx\nHunk #1 FAILED at 365.\n1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix_symbolic_dense.pyx.rej\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-19T15:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14539",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_events_002375.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2008-03-05T00:38:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2207#event-2375"
}
```



---

archive/issue_comments_014540.json:
```json
{
    "body": "This code made it in in #2053.",
    "created_at": "2008-03-05T00:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14540",
    "user": "https://github.com/mwhansen"
}
```

This code made it in in #2053.



---

archive/issue_comments_014541.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T00:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14541",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_014542.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-03-05T01:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14542",
    "user": "https://github.com/mwhansen"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_014543.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-05T01:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14543",
    "user": "https://github.com/mwhansen"
}
```

Changing status from closed to reopened.



---

archive/issue_events_002376.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2008-03-05T01:09:01Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2207#event-2376"
}
```



---

archive/issue_comments_014544.json:
```json
{
    "body": "Attachment [2207.patch](tarball://root/attachments/some-uuid/ticket2207/2207.patch) by @mwhansen created at 2008-03-05 01:09:01\n\nNew patch against 2.10.3.rc1 attached which adds missing doctests",
    "created_at": "2008-03-05T01:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14544",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2207.patch](tarball://root/attachments/some-uuid/ticket2207/2207.patch) by @mwhansen created at 2008-03-05 01:09:01

New patch against 2.10.3.rc1 attached which adds missing doctests



---

archive/issue_events_002377.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-05T05:35:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2207#event-2377"
}
```



---

archive/issue_comments_014545.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc2 - due to some hg stupidity parts of this patch made it in rc0. Mike Hansen's latest patch adds the missing docstring and doctest.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-05T05:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14545",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc2 - due to some hg stupidity parts of this patch made it in rc0. Mike Hansen's latest patch adds the missing docstring and doctest.

Cheers,

Michael



---

archive/issue_comments_014546.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T05:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14546",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014547.json:
```json
{
    "body": "When I tested 2.10.3.rc2 I got this:\n\n\n```\nsage -t  devel/sage-main/sage/matrix/matrix_symbolic_dense.pyxemacs devel/sage-main/sage/matrix/matrix_symbolic_dense.pyx**********************************************************************\nFile \"matrix_symbolic_dense.pyx\", line 871:\n    sage: list(a.fcp())\nExpected:\n    [(x^2 - 65*x - 250, 1), (x, 3)]\nGot:\n    [(x, 3), (x^2 - 65*x - 250, 1)]\n**********************************************************************\n```\n\n\nand I suggest changing line 871 from\n\n```\n            sage: list(a.fcp())\n```\n\nto\n\n```\n            sage: sorted(list(a.fcp()))\n```\n",
    "created_at": "2008-03-05T22:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2207",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2207#issuecomment-14547",
    "user": "https://github.com/JohnCremona"
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

