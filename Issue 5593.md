# Issue 5593: [with patch; needs review or throwing away] CremonaDB.conductor_range does not give a Python style range

archive/issues_005593.json:
```json
{
    "body": "Assignee: @nbruin\n\nCremonaDB().conductor_range() gives an inclusive upper bound, so that\nsrange(*CremonaDB().conductor_range()) may miss a conductor.\n\nFix attached\n\nIssue created by migration from https://trac.sagemath.org/ticket/5593\n\n",
    "created_at": "2009-03-23T19:02:14Z",
    "labels": [
        "component: modular forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch; needs review or throwing away] CremonaDB.conductor_range does not give a Python style range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5593",
    "user": "https://github.com/nbruin"
}
```
Assignee: @nbruin

CremonaDB().conductor_range() gives an inclusive upper bound, so that
srange(*CremonaDB().conductor_range()) may miss a conductor.

Fix attached

Issue created by migration from https://trac.sagemath.org/ticket/5593





---

archive/issue_comments_043481.json:
```json
{
    "body": "Patch",
    "created_at": "2009-03-23T19:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5593#issuecomment-43481",
    "user": "https://github.com/nbruin"
}
```

Patch



---

archive/issue_comments_043482.json:
```json
{
    "body": "Attachment [11804.patch](tarball://root/attachments/some-uuid/ticket5593/11804.patch) by @robertwb created at 2009-03-23 19:30:55\n\nYes, this looks like the right thing to do.",
    "created_at": "2009-03-23T19:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5593#issuecomment-43482",
    "user": "https://github.com/robertwb"
}
```

Attachment [11804.patch](tarball://root/attachments/some-uuid/ticket5593/11804.patch) by @robertwb created at 2009-03-23 19:30:55

Yes, this looks like the right thing to do.



---

archive/issue_comments_043483.json:
```json
{
    "body": "Looks good to me too.",
    "created_at": "2009-03-23T20:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5593#issuecomment-43483",
    "user": "https://github.com/JohnCremona"
}
```

Looks good to me too.



---

archive/issue_events_013180.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-23T21:17:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5593#event-13180"
}
```



---

archive/issue_comments_043484.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T21:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5593#issuecomment-43484",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_043485.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T21:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5593#issuecomment-43485",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
