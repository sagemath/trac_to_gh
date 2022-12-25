# Issue 2569: Add XOR to preparser

archive/issues_002569.json:
```json
{
    "body": "Assignee: cwitty\n\nSince the preparser replaces \"^\" with \"**\",\nthere should be a way to access the python-buildin-XOR again.\n\nThe discussion is here: [http://groups.google.com/group/sage-devel/browse_thread/thread/a7aaccd2081098bc/de225692ee38f0a5](http://groups.google.com/group/sage-devel/browse_thread/thread/a7aaccd2081098bc/de225692ee38f0a5)\n\nThe conclusion is:\n\n```\nUnless somebody thinks of something better, I like ^^ as well.\n\nWilliam\n```\n\n\n\n\nSo the preparser should replace \"^^\" with \"^\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/2569\n\n",
    "created_at": "2008-03-17T09:35:50Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Add XOR to preparser",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2569",
    "user": "https://github.com/m-r-k"
}
```
Assignee: cwitty

Since the preparser replaces "^" with "**",
there should be a way to access the python-buildin-XOR again.

The discussion is here: [http://groups.google.com/group/sage-devel/browse_thread/thread/a7aaccd2081098bc/de225692ee38f0a5](http://groups.google.com/group/sage-devel/browse_thread/thread/a7aaccd2081098bc/de225692ee38f0a5)

The conclusion is:

```
Unless somebody thinks of something better, I like ^^ as well.

William
```




So the preparser should replace "^^" with "^".

Issue created by migration from https://trac.sagemath.org/ticket/2569





---

archive/issue_comments_017518.json:
```json
{
    "body": "Attachment [trac2569-preparse-xor.patch](tarball://root/attachments/some-uuid/ticket2569/trac2569-preparse-xor.patch) by cwitty created at 2008-08-23 18:48:48",
    "created_at": "2008-08-23T18:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2569#issuecomment-17518",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac2569-preparse-xor.patch](tarball://root/attachments/some-uuid/ticket2569/trac2569-preparse-xor.patch) by cwitty created at 2008-08-23 18:48:48



---

archive/issue_comments_017519.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-08-24T23:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2569#issuecomment-17519",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_017520.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T01:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2569#issuecomment-17520",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017521.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.2.alpha1",
    "created_at": "2008-08-25T01:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2569#issuecomment-17521",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.1.2.alpha1



---

archive/issue_comments_017522.json:
```json
{
    "body": "Oops, merged the one and only patch attached to this ticket. Damn copy & paste ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T01:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2569#issuecomment-17522",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, merged the one and only patch attached to this ticket. Damn copy & paste ;)

Cheers,

Michael
