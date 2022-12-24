# Issue 5293: tab-completion menu creates two copies of the choice made

archive/issues_005293.json:
```json
{
    "body": "Assignee: tbd\n\nIn sage-3.3.rc0 (presumable from some patch in an alpha release) tab-completion is somewhat broken in the notebook.  If you tab-complete and there is more than one possible completion, if you choose from the drop-down menu and press enter you get the entire command repeated, for example:\n\nQQ. [press tab, get menu, choose absolute_degree and press enter]\nQQ.absolute_degreeQQ.absolute_degree\n\nThis is currently effecting sagenb's rc0, and has been confirmed on several other installs.\n\nI am not sure where to begin to track this down, or what patch caused it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5293\n\n",
    "created_at": "2009-02-17T12:57:36Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "tab-completion menu creates two copies of the choice made",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5293",
    "user": "mhampton"
}
```
Assignee: tbd

In sage-3.3.rc0 (presumable from some patch in an alpha release) tab-completion is somewhat broken in the notebook.  If you tab-complete and there is more than one possible completion, if you choose from the drop-down menu and press enter you get the entire command repeated, for example:

QQ. [press tab, get menu, choose absolute_degree and press enter]
QQ.absolute_degreeQQ.absolute_degree

This is currently effecting sagenb's rc0, and has been confirmed on several other installs.

I am not sure where to begin to track this down, or what patch caused it.

Issue created by migration from https://trac.sagemath.org/ticket/5293





---

archive/issue_comments_040679.json:
```json
{
    "body": "Changing assignee from tbd to boothby.",
    "created_at": "2009-02-17T12:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40679",
    "user": "mhampton"
}
```

Changing assignee from tbd to boothby.



---

archive/issue_comments_040680.json:
```json
{
    "body": "Changing keywords from \"\" to \"tab completion\".",
    "created_at": "2009-02-17T12:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40680",
    "user": "mhampton"
}
```

Changing keywords from "" to "tab completion".



---

archive/issue_comments_040681.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2009-02-17T12:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40681",
    "user": "mhampton"
}
```

Changing component from algebra to notebook.



---

archive/issue_comments_040682.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-02-17T20:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40682",
    "user": "mhampton"
}
```

Changing priority from major to critical.



---

archive/issue_comments_040683.json:
```json
{
    "body": "This seems to be caused by #4440. I am working on a patch now.",
    "created_at": "2009-02-17T22:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40683",
    "user": "mhampton"
}
```

This seems to be caused by #4440. I am working on a patch now.



---

archive/issue_comments_040684.json:
```json
{
    "body": "I am just confirming that this is caused by #4440.  I found this with the (very cool) hg bisect command and then hand-tested before/after the patch was committed.",
    "created_at": "2009-02-17T23:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40684",
    "user": "@jasongrout"
}
```

I am just confirming that this is caused by #4440.  I found this with the (very cool) hg bisect command and then hand-tested before/after the patch was committed.



---

archive/issue_comments_040685.json:
```json
{
    "body": "Fixed by reverting #4440 for now.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T23:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40685",
    "user": "mabshoff"
}
```

Fixed by reverting #4440 for now.

Cheers,

Michael



---

archive/issue_comments_040686.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-17T23:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40686",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040687.json:
```json
{
    "body": "Attachment [5293.patch](tarball://root/attachments/some-uuid/ticket5293/5293.patch) by boothby created at 2009-02-19 20:39:45",
    "created_at": "2009-02-19T20:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40687",
    "user": "boothby"
}
```

Attachment [5293.patch](tarball://root/attachments/some-uuid/ticket5293/5293.patch) by boothby created at 2009-02-19 20:39:45



---

archive/issue_comments_040688.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-02-19T20:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40688",
    "user": "boothby"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_040689.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-02-19T20:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40689",
    "user": "boothby"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_040690.json:
```json
{
    "body": "patch depends on #4440",
    "created_at": "2009-02-19T20:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40690",
    "user": "boothby"
}
```

patch depends on #4440



---

archive/issue_comments_040691.json:
```json
{
    "body": "This appears to fix the side-effects from #4440.  Patch applies to rc0, which still had #4440 applied.",
    "created_at": "2009-02-19T21:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40691",
    "user": "mhampton"
}
```

This appears to fix the side-effects from #4440.  Patch applies to rc0, which still had #4440 applied.



---

archive/issue_comments_040692.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T07:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40692",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_comments_040693.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T07:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40693",
    "user": "mabshoff"
}
```

Resolution: fixed
