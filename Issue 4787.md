# Issue 4787: Race condition in sage-doctest folder creation

archive/issues_004787.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nThere is a race condition in sage-doctest during folder creation at line 586, which is in a function called at line 441.  This can cause doctesting a file to fail with file not found errors.  This is different then the other file not found error that was in ptest.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/4787\n\n",
    "created_at": "2008-12-14T00:58:37Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Race condition in sage-doctest folder creation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4787",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

There is a race condition in sage-doctest during folder creation at line 586, which is in a function called at line 441.  This can cause doctesting a file to fail with file not found errors.  This is different then the other file not found error that was in ptest.  

Issue created by migration from https://trac.sagemath.org/ticket/4787





---

archive/issue_comments_036222.json:
```json
{
    "body": "Attachment [trac_4787_bin.patch](tarball://root/attachments/some-uuid/ticket4787/trac_4787_bin.patch) by @garyfurnish created at 2008-12-14 01:48:32",
    "created_at": "2008-12-14T01:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4787#issuecomment-36222",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_4787_bin.patch](tarball://root/attachments/some-uuid/ticket4787/trac_4787_bin.patch) by @garyfurnish created at 2008-12-14 01:48:32



---

archive/issue_comments_036223.json:
```json
{
    "body": "Changing keywords from \"\" to \"mabshoff\".",
    "created_at": "2008-12-14T01:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4787#issuecomment-36223",
    "user": "https://github.com/garyfurnish"
}
```

Changing keywords from "" to "mabshoff".



---

archive/issue_comments_036224.json:
```json
{
    "body": "The line numbers in the description above should be switched -- basically in a rare case another sage-doctest can create the directories before this one creates them, but after it has decided they don't already exist.  This tells it to ignore errors on making the directories -- they will still get caught later.",
    "created_at": "2008-12-14T01:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4787#issuecomment-36224",
    "user": "https://github.com/garyfurnish"
}
```

The line numbers in the description above should be switched -- basically in a rare case another sage-doctest can create the directories before this one creates them, but after it has decided they don't already exist.  This tells it to ignore errors on making the directories -- they will still get caught later.



---

archive/issue_comments_036225.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-14T01:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4787#issuecomment-36225",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036226.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-14T04:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4787#issuecomment-36226",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_036227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-14T05:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4787#issuecomment-36227",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005031.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-14T05:43:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4787",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4787#event-5031"
}
```



---

archive/issue_comments_036228.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc0",
    "created_at": "2008-12-14T05:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4787#issuecomment-36228",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.rc0
