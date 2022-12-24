# Issue 4771: notebook -- get rid of these debug log messages I put in: "Dumping ..."

archive/issues_004771.json:
```json
{
    "body": "Assignee: boothby\n\nThe messages:\n\n```\n2008-12-12 10:56:37-0800 [HTTPChannel,53,24.143.70.101] Dumping admin history to 'sage_notebook/worksheets/admin/history.sobj'\n```\n\nthat the notebook prints out for no good reason should be deleted by commenting out the line in the notebook server code that prints them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4771\n\n",
    "created_at": "2008-12-12T19:04:12Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "notebook -- get rid of these debug log messages I put in: \"Dumping ...\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4771",
    "user": "was"
}
```
Assignee: boothby

The messages:

```
2008-12-12 10:56:37-0800 [HTTPChannel,53,24.143.70.101] Dumping admin history to 'sage_notebook/worksheets/admin/history.sobj'
```

that the notebook prints out for no good reason should be deleted by commenting out the line in the notebook server code that prints them.

Issue created by migration from https://trac.sagemath.org/ticket/4771





---

archive/issue_comments_036140.json:
```json
{
    "body": "Attachment [sage-4771.patch](tarball://root/attachments/some-uuid/ticket4771/sage-4771.patch) by TimothyClemans created at 2008-12-12 19:29:20",
    "created_at": "2008-12-12T19:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4771#issuecomment-36140",
    "user": "TimothyClemans"
}
```

Attachment [sage-4771.patch](tarball://root/attachments/some-uuid/ticket4771/sage-4771.patch) by TimothyClemans created at 2008-12-12 19:29:20



---

archive/issue_comments_036141.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T06:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4771#issuecomment-36141",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_036142.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-13T09:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4771#issuecomment-36142",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036143.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-13T09:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4771#issuecomment-36143",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha2
