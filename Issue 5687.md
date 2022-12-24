# Issue 5687: [with patch; needs review] notebook -- only save snapshot when worksheet.txt has changed.

archive/issues_005687.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5687\n\n",
    "created_at": "2009-04-05T05:38:54Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch; needs review] notebook -- only save snapshot when worksheet.txt has changed.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5687",
    "user": "was"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/5687





---

archive/issue_comments_044478.json:
```json
{
    "body": "Attachment [trac_5687.patch](tarball://root/attachments/some-uuid/ticket5687/trac_5687.patch) by TimothyClemans created at 2009-04-05 06:38:18",
    "created_at": "2009-04-05T06:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5687#issuecomment-44478",
    "user": "TimothyClemans"
}
```

Attachment [trac_5687.patch](tarball://root/attachments/some-uuid/ticket5687/trac_5687.patch) by TimothyClemans created at 2009-04-05 06:38:18



---

archive/issue_comments_044479.json:
```json
{
    "body": "I can't create a new worksheet\n\nError:\n\n```\n\t    if open('%s/worksheet.txt'%self.__dir).read() == E:\n\texceptions.IOError: [Errno 2] No such file or directory: 'sage_notebook/worksheets/admin/44/worksheet.txt'\n```\n",
    "created_at": "2009-04-05T06:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5687#issuecomment-44479",
    "user": "TimothyClemans"
}
```

I can't create a new worksheet

Error:

```
	    if open('%s/worksheet.txt'%self.__dir).read() == E:
	exceptions.IOError: [Errno 2] No such file or directory: 'sage_notebook/worksheets/admin/44/worksheet.txt'
```




---

archive/issue_comments_044480.json:
```json
{
    "body": "Attachment [trac_5687-part2.patch](tarball://root/attachments/some-uuid/ticket5687/trac_5687-part2.patch) by TimothyClemans created at 2009-04-05 07:23:16\n\nPositive review: Tested both manual save and autosave",
    "created_at": "2009-04-05T07:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5687#issuecomment-44480",
    "user": "TimothyClemans"
}
```

Attachment [trac_5687-part2.patch](tarball://root/attachments/some-uuid/ticket5687/trac_5687-part2.patch) by TimothyClemans created at 2009-04-05 07:23:16

Positive review: Tested both manual save and autosave



---

archive/issue_comments_044481.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-05T22:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5687#issuecomment-44481",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044482.json:
```json
{
    "body": "Merged both patches in Sage 3.4.1.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T22:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5687#issuecomment-44482",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.1.rc1.

Cheers,

Michael
