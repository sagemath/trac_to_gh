# Issue 2123: bug in modular symbols setting sign on subspace

archive/issues_002123.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThis is wrong:\n\n\n```\nsage: A = ModularSymbols(1,80,0,base_ring=GF(37))\n\nsage: A.plus_submodule().cuspidal_submodule().sign()\n 0\n\n```\n\n\nI'll fix it at some point soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2123\n\n",
    "created_at": "2008-02-09T03:59:11Z",
    "labels": [
        "modular forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "bug in modular symbols setting sign on subspace",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2123",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

This is wrong:


```
sage: A = ModularSymbols(1,80,0,base_ring=GF(37))

sage: A.plus_submodule().cuspidal_submodule().sign()
 0

```


I'll fix it at some point soon.

Issue created by migration from https://trac.sagemath.org/ticket/2123





---

archive/issue_comments_013929.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-12T07:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2123#issuecomment-13929",
    "user": "@craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013930.json:
```json
{
    "body": "... and it's fixed.",
    "created_at": "2008-02-12T07:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2123#issuecomment-13930",
    "user": "@craigcitro"
}
```

... and it's fixed.



---

archive/issue_comments_013931.json:
```json
{
    "body": "Attachment [trac-2123.patch](tarball://root/attachments/some-uuid/ticket2123/trac-2123.patch) by @craigcitro created at 2008-02-12 07:26:44",
    "created_at": "2008-02-12T07:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2123#issuecomment-13931",
    "user": "@craigcitro"
}
```

Attachment [trac-2123.patch](tarball://root/attachments/some-uuid/ticket2123/trac-2123.patch) by @craigcitro created at 2008-02-12 07:26:44



---

archive/issue_comments_013932.json:
```json
{
    "body": "looks good!",
    "created_at": "2008-02-12T07:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2123#issuecomment-13932",
    "user": "@williamstein"
}
```

looks good!



---

archive/issue_comments_013933.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-13T07:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2123#issuecomment-13933",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013934.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-13T07:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2123#issuecomment-13934",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
