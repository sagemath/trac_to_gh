# Issue 2867: [witch patch, needs review] allow load_files parameter in __call__

archive/issues_002867.json:
```json
{
    "body": "Assignee: yi\n\nThis patch allows you to do dsage('f = Foo()', load_files = ['foo.py']) which loads foo.py before executing the job. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2867\n\n",
    "created_at": "2008-04-09T23:09:00Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[witch patch, needs review] allow load_files parameter in __call__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2867",
    "user": "yi"
}
```
Assignee: yi

This patch allows you to do dsage('f = Foo()', load_files = ['foo.py']) which loads foo.py before executing the job. 

Issue created by migration from https://trac.sagemath.org/ticket/2867





---

archive/issue_comments_019675.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nFor the record: Please post proper mercurial patches in the future. I.e. use export instead of diff. I cannot tell the difference with patch preview and by the time I import the patch it is too late.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-10T01:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2867#issuecomment-19675",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.

For the record: Please post proper mercurial patches in the future. I.e. use export instead of diff. I cannot tell the difference with patch preview and by the time I import the patch it is too late.

Cheers,

Michael



---

archive/issue_comments_019676.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-10T01:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2867#issuecomment-19676",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019677.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-10T01:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2867#issuecomment-19677",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_comments_019678.json:
```json
{
    "body": "Attachment [load_files.2.patch](tarball://root/attachments/some-uuid/ticket2867/load_files.2.patch) by yi created at 2008-04-10 03:41:12",
    "created_at": "2008-04-10T03:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2867#issuecomment-19678",
    "user": "yi"
}
```

Attachment [load_files.2.patch](tarball://root/attachments/some-uuid/ticket2867/load_files.2.patch) by yi created at 2008-04-10 03:41:12



---

archive/issue_comments_019679.json:
```json
{
    "body": "Oh, the irony that I didn't catch this doctest failure: Merged load_files.2.patch in Sage 3.0.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-10T03:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2867#issuecomment-19679",
    "user": "mabshoff"
}
```

Oh, the irony that I didn't catch this doctest failure: Merged load_files.2.patch in Sage 3.0.alpha4.

Cheers,

Michael
