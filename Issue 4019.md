# Issue 4019: [with patch, needs review] numerator and denominator for QQ[x]

archive/issues_004019.json:
```json
{
    "body": "Assignee: tbd\n\nQQ[x] should have a numerator and denominator method. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4019\n\n",
    "created_at": "2008-08-31T09:01:46Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] numerator and denominator for QQ[x]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4019",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd

QQ[x] should have a numerator and denominator method. 

Issue created by migration from https://trac.sagemath.org/ticket/4019





---

archive/issue_comments_028927.json:
```json
{
    "body": "Attachment [4019-QQx-numer.patch](tarball://root/attachments/some-uuid/ticket4019/4019-QQx-numer.patch) by @robertwb created at 2008-08-31 09:06:25",
    "created_at": "2008-08-31T09:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28927",
    "user": "https://github.com/robertwb"
}
```

Attachment [4019-QQx-numer.patch](tarball://root/attachments/some-uuid/ticket4019/4019-QQx-numer.patch) by @robertwb created at 2008-08-31 09:06:25



---

archive/issue_comments_028928.json:
```json
{
    "body": "The code looks fine.  However, I'm getting a doctest failure in finite_field_ntl_gf2e.pyx:\n\n\n```\nFile \"/opt/sage/tmp/finite_field_ntl_gf2e.py\", line 1018:\n    sage: e == f\nExpected:\n    True\nGot:\n    False\n```\n\n\nI can't tell where this is coming from.",
    "created_at": "2008-08-31T12:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28928",
    "user": "https://github.com/aghitza"
}
```

The code looks fine.  However, I'm getting a doctest failure in finite_field_ntl_gf2e.pyx:


```
File "/opt/sage/tmp/finite_field_ntl_gf2e.py", line 1018:
    sage: e == f
Expected:
    True
Got:
    False
```


I can't tell where this is coming from.



---

archive/issue_comments_028929.json:
```json
{
    "body": "I am changing the subject to \"needs work\" so that the various report will pick up this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T01:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28929",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am changing the subject to "needs work" so that the various report will pick up this ticket.

Cheers,

Michael



---

archive/issue_comments_028930.json:
```json
{
    "body": "I have been unable to reproduce this error, are you sure it's from this patch?",
    "created_at": "2008-09-01T21:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28930",
    "user": "https://github.com/robertwb"
}
```

I have been unable to reproduce this error, are you sure it's from this patch?



---

archive/issue_comments_028931.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> I have been unable to reproduce this error, are you sure it's from this patch? \n\nRobert, Alex,\n\napplying this patch only to my merge tree does not result in any doctest failure, so I am giving this a positive review. Hopefully this will not bit us in the ass down the road ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T21:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28931",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 robertwb]:
> I have been unable to reproduce this error, are you sure it's from this patch? 

Robert, Alex,

applying this patch only to my merge tree does not result in any doctest failure, so I am giving this a positive review. Hopefully this will not bit us in the ass down the road ;)

Cheers,

Michael



---

archive/issue_comments_028932.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T21:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28932",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009193.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-01T21:49:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4019#event-9193"
}
```



---

archive/issue_comments_028933.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T21:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28933",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha4
