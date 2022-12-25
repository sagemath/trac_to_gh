# Issue 2566: [with patch, needs review] fix type of "size" in graph_isom and binary_code

archive/issues_002566.json:
```json
{
    "body": "Assignee: @rlmill\n\nBecause, after all, 14! > 2<sup>32</sup> and 21! > 2<sup>64</sup>.\n\nThis also makes the codewords in `binary_code.pyx` unsigned, because of those pesky signed integer shifting issues...\n\nIssue created by migration from https://trac.sagemath.org/ticket/2566\n\n",
    "created_at": "2008-03-17T06:39:38Z",
    "labels": [
        "component: coding theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, needs review] fix type of \"size\" in graph_isom and binary_code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2566",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

Because, after all, 14! > 2<sup>32</sup> and 21! > 2<sup>64</sup>.

This also makes the codewords in `binary_code.pyx` unsigned, because of those pesky signed integer shifting issues...

Issue created by migration from https://trac.sagemath.org/ticket/2566





---

archive/issue_comments_017456.json:
```json
{
    "body": "Attachment [2566-mp-size-binary_code.patch](tarball://root/attachments/some-uuid/ticket2566/2566-mp-size-binary_code.patch) by @rlmill created at 2008-03-19 23:42:35",
    "created_at": "2008-03-19T23:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2566#issuecomment-17456",
    "user": "https://github.com/rlmill"
}
```

Attachment [2566-mp-size-binary_code.patch](tarball://root/attachments/some-uuid/ticket2566/2566-mp-size-binary_code.patch) by @rlmill created at 2008-03-19 23:42:35



---

archive/issue_comments_017457.json:
```json
{
    "body": "Applies and passes tests.  Looks good to me.",
    "created_at": "2008-03-19T23:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2566#issuecomment-17457",
    "user": "https://github.com/mwhansen"
}
```

Applies and passes tests.  Looks good to me.



---

archive/issue_comments_017458.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T00:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2566#issuecomment-17458",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017459.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-20T00:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2566#issuecomment-17459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0
