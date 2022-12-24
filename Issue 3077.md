# Issue 3077: pbuild does not return properly on failure

archive/issues_003077.json:
```json
{
    "body": "Assignee: gfurnish\n\nKeywords: pbuild\n\npbuild does not return an exceptional value to the operating system on failure.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3077\n\n",
    "created_at": "2008-05-02T10:06:58Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "pbuild does not return properly on failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3077",
    "user": "gfurnish"
}
```
Assignee: gfurnish

Keywords: pbuild

pbuild does not return an exceptional value to the operating system on failure.


Issue created by migration from https://trac.sagemath.org/ticket/3077





---

archive/issue_comments_021229.json:
```json
{
    "body": "Attachment [trac_3077.patch](tarball://root/attachments/some-uuid/ticket3077/trac_3077.patch) by gfurnish created at 2008-05-02 10:10:21",
    "created_at": "2008-05-02T10:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3077#issuecomment-21229",
    "user": "gfurnish"
}
```

Attachment [trac_3077.patch](tarball://root/attachments/some-uuid/ticket3077/trac_3077.patch) by gfurnish created at 2008-05-02 10:10:21



---

archive/issue_comments_021230.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-02T10:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3077#issuecomment-21230",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021231.json:
```json
{
    "body": "The easy test case for this is to create a cython failure and try to sage -br.  Prepatch it runs sage and postpatch it does not.",
    "created_at": "2008-05-02T10:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3077#issuecomment-21231",
    "user": "gfurnish"
}
```

The easy test case for this is to create a cython failure and try to sage -br.  Prepatch it runs sage and postpatch it does not.



---

archive/issue_comments_021232.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T12:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3077#issuecomment-21232",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021233.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T12:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3077#issuecomment-21233",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.rc0
