# Issue 4094: evaluate all causes massive browser hang

archive/issues_004094.json:
```json
{
    "body": "Assignee: tbd\n\n#4078 was done wrong.  Any reference to eval_bool should be removed.  Non-async calls *must never be used*.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4094\n\n",
    "created_at": "2008-09-09T20:52:27Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "evaluate all causes massive browser hang",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4094",
    "user": "boothby"
}
```
Assignee: tbd

#4078 was done wrong.  Any reference to eval_bool should be removed.  Non-async calls *must never be used*.

Issue created by migration from https://trac.sagemath.org/ticket/4094





---

archive/issue_comments_029533.json:
```json
{
    "body": "Changing assignee from tbd to boothby.",
    "created_at": "2008-09-09T20:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4094#issuecomment-29533",
    "user": "boothby"
}
```

Changing assignee from tbd to boothby.



---

archive/issue_comments_029534.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2008-09-09T20:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4094#issuecomment-29534",
    "user": "boothby"
}
```

Changing component from algebra to notebook.



---

archive/issue_comments_029535.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-09-09T21:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4094#issuecomment-29535",
    "user": "boothby"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_029536.json:
```json
{
    "body": "Attachment [4094-eval_all.patch](tarball://root/attachments/some-uuid/ticket4094/4094-eval_all.patch) by boothby created at 2008-09-09 23:01:00",
    "created_at": "2008-09-09T23:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4094#issuecomment-29536",
    "user": "boothby"
}
```

Attachment [4094-eval_all.patch](tarball://root/attachments/some-uuid/ticket4094/4094-eval_all.patch) by boothby created at 2008-09-09 23:01:00



---

archive/issue_comments_029537.json:
```json
{
    "body": "The attached does *NOT* depend on #4078.  In fact, it conflicts hugely.  If it is possible to reverse #4078, please do so.  Otherwise, I'll resolve the conflict tonight.",
    "created_at": "2008-09-09T23:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4094#issuecomment-29537",
    "user": "boothby"
}
```

The attached does *NOT* depend on #4078.  In fact, it conflicts hugely.  If it is possible to reverse #4078, please do so.  Otherwise, I'll resolve the conflict tonight.



---

archive/issue_comments_029538.json:
```json
{
    "body": "Attachment [trac_4094.patch](tarball://root/attachments/some-uuid/ticket4094/trac_4094.patch) by mhansen created at 2008-09-10 00:24:51",
    "created_at": "2008-09-10T00:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4094#issuecomment-29538",
    "user": "mhansen"
}
```

Attachment [trac_4094.patch](tarball://root/attachments/some-uuid/ticket4094/trac_4094.patch) by mhansen created at 2008-09-10 00:24:51



---

archive/issue_comments_029539.json:
```json
{
    "body": "This is a better fix.  Apply only trac_4094.patch which should apply fine against the current tree.",
    "created_at": "2008-09-10T00:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4094#issuecomment-29539",
    "user": "mhansen"
}
```

This is a better fix.  Apply only trac_4094.patch which should apply fine against the current tree.



---

archive/issue_comments_029540.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-10T01:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4094#issuecomment-29540",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029541.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc2",
    "created_at": "2008-09-10T01:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4094#issuecomment-29541",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc2
