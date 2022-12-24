# Issue 2309: [with patch, needs review] #2267 introduced spurious linebreak commands '\\'

archive/issues_002309.json:
```json
{
    "body": "Assignee: tba\n\nmabshoff changed `\\&` to `\\\\&`; the correct fix is to change to `&`.  I rebuilt the manual, and verified that it does rebuild and that the spurious linebreaks are gone (although the formatting in the second relevant section is still pretty bad).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2309\n\n",
    "created_at": "2008-02-26T03:45:18Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] #2267 introduced spurious linebreak commands '\\\\'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2309",
    "user": "cwitty"
}
```
Assignee: tba

mabshoff changed `\&` to `\\&`; the correct fix is to change to `&`.  I rebuilt the manual, and verified that it does rebuild and that the spurious linebreaks are gone (although the formatting in the second relevant section is still pretty bad).


Issue created by migration from https://trac.sagemath.org/ticket/2309





---

archive/issue_comments_015367.json:
```json
{
    "body": "Attachment [trac2267-no-linebreaks.patch](tarball://root/attachments/some-uuid/ticket2309/trac2267-no-linebreaks.patch) by mabshoff created at 2008-02-26 04:04:23\n\nNice catch by cwitty. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-26T04:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2309#issuecomment-15367",
    "user": "mabshoff"
}
```

Attachment [trac2267-no-linebreaks.patch](tarball://root/attachments/some-uuid/ticket2309/trac2267-no-linebreaks.patch) by mabshoff created at 2008-02-26 04:04:23

Nice catch by cwitty. Positive review.

Cheers,

Michael



---

archive/issue_comments_015368.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-26T04:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2309#issuecomment-15368",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015369.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-26T04:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2309#issuecomment-15369",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.alpha0



---

archive/issue_comments_015370.json:
```json
{
    "body": "Changing assignee from tba to mabshoff.",
    "created_at": "2008-02-26T04:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2309#issuecomment-15370",
    "user": "mabshoff"
}
```

Changing assignee from tba to mabshoff.



---

archive/issue_comments_015371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-26T04:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2309#issuecomment-15371",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015372.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-26T04:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2309#issuecomment-15372",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.alpha0
