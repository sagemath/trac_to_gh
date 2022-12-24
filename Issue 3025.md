# Issue 3025: Sparse vector spaces don't cast on assignment.

archive/issues_003025.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: V = VectorSpace(GF(2),10, sparse=True)\nsage: w = V(0)\nsage: w[0] = 2\nsage: print w[0]\n2\nsage: print type(w[0])\n<type 'sage.rings.integer.Integer'>\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3025\n\n",
    "created_at": "2008-04-25T20:57:56Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "Sparse vector spaces don't cast on assignment.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3025",
    "user": "boothby"
}
```
Assignee: was


```
sage: V = VectorSpace(GF(2),10, sparse=True)
sage: w = V(0)
sage: w[0] = 2
sage: print w[0]
2
sage: print type(w[0])
<type 'sage.rings.integer.Integer'>
```



Issue created by migration from https://trac.sagemath.org/ticket/3025





---

archive/issue_comments_020801.json:
```json
{
    "body": "Attachment [9609.patch](tarball://root/attachments/some-uuid/ticket3025/9609.patch) by was created at 2008-04-25 21:18:57\n\nthis fixes the bug!",
    "created_at": "2008-04-25T21:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3025#issuecomment-20801",
    "user": "was"
}
```

Attachment [9609.patch](tarball://root/attachments/some-uuid/ticket3025/9609.patch) by was created at 2008-04-25 21:18:57

this fixes the bug!



---

archive/issue_comments_020802.json:
```json
{
    "body": "works for me",
    "created_at": "2008-04-25T21:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3025#issuecomment-20802",
    "user": "boothby"
}
```

works for me



---

archive/issue_comments_020803.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-25T23:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3025#issuecomment-20803",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.alpha0



---

archive/issue_comments_020804.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-25T23:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3025#issuecomment-20804",
    "user": "mabshoff"
}
```

Resolution: fixed
