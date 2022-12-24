# Issue 5351: Sage 3.3 broke the update of  easy-install.pth

archive/issues_005351.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen unpacking a Sage 3.3 binary the update of easy-install.pth is broken:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nThe SAGE install tree may have moved.\nRegenerating Python.pyo and .pyc files that hardcode the install PATH (please wait at\nmost a few minutes)...\nDo not interrupt this.\nWarning: something went wrong updating the easy-install.pth file.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5351\n\n",
    "created_at": "2009-02-23T19:06:18Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "title": "Sage 3.3 broke the update of  easy-install.pth",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5351",
    "user": "mabshoff"
}
```
Assignee: mabshoff

When unpacking a Sage 3.3 binary the update of easy-install.pth is broken:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
The SAGE install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH (please wait at
most a few minutes)...
Do not interrupt this.
Warning: something went wrong updating the easy-install.pth file.
```


Issue created by migration from https://trac.sagemath.org/ticket/5351





---

archive/issue_comments_041222.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-01T05:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5351#issuecomment-41222",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041223.json:
```json
{
    "body": "Attachment [trac_5351.patch](tarball://root/attachments/some-uuid/ticket5351/trac_5351.patch) by mabshoff created at 2009-03-01 05:52:45",
    "created_at": "2009-03-01T05:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5351#issuecomment-41223",
    "user": "mabshoff"
}
```

Attachment [trac_5351.patch](tarball://root/attachments/some-uuid/ticket5351/trac_5351.patch) by mabshoff created at 2009-03-01 05:52:45



---

archive/issue_comments_041224.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-03-02T05:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5351#issuecomment-41224",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_041225.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-02T05:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5351#issuecomment-41225",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041226.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T05:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5351#issuecomment-41226",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael
