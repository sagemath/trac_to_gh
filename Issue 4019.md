# Issue 4019: [with patch, needs review] numerator and denominator for QQ[x]

archive/issues_004019.json:
```json
{
    "body": "Assignee: tbd\n\nQQ[x] should have a numerator and denominator method. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4019\n\n",
    "created_at": "2008-08-31T09:01:46Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] numerator and denominator for QQ[x]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4019",
    "user": "robertwb"
}
```
Assignee: tbd

QQ[x] should have a numerator and denominator method. 

Issue created by migration from https://trac.sagemath.org/ticket/4019





---

archive/issue_comments_028985.json:
```json
{
    "body": "Attachment [4019-QQx-numer.patch](tarball://root/attachments/some-uuid/ticket4019/4019-QQx-numer.patch) by robertwb created at 2008-08-31 09:06:25",
    "created_at": "2008-08-31T09:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28985",
    "user": "robertwb"
}
```

Attachment [4019-QQx-numer.patch](tarball://root/attachments/some-uuid/ticket4019/4019-QQx-numer.patch) by robertwb created at 2008-08-31 09:06:25



---

archive/issue_comments_028986.json:
```json
{
    "body": "The code looks fine.  However, I'm getting a doctest failure in finite_field_ntl_gf2e.pyx:\n\n\n```\nFile \"/opt/sage/tmp/finite_field_ntl_gf2e.py\", line 1018:\n    sage: e == f\nExpected:\n    True\nGot:\n    False\n```\n\n\nI can't tell where this is coming from.",
    "created_at": "2008-08-31T12:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28986",
    "user": "AlexGhitza"
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

archive/issue_comments_028987.json:
```json
{
    "body": "I am changing the subject to \"needs work\" so that the various report will pick up this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T01:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28987",
    "user": "mabshoff"
}
```

I am changing the subject to "needs work" so that the various report will pick up this ticket.

Cheers,

Michael



---

archive/issue_comments_028988.json:
```json
{
    "body": "I have been unable to reproduce this error, are you sure it's from this patch?",
    "created_at": "2008-09-01T21:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28988",
    "user": "robertwb"
}
```

I have been unable to reproduce this error, are you sure it's from this patch?



---

archive/issue_comments_028989.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> I have been unable to reproduce this error, are you sure it's from this patch? \n\nRobert, Alex,\n\napplying this patch only to my merge tree does not result in any doctest failure, so I am giving this a positive review. Hopefully this will not bit us in the ass down the road ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T21:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28989",
    "user": "mabshoff"
}
```

Replying to [comment:4 robertwb]:
> I have been unable to reproduce this error, are you sure it's from this patch? 

Robert, Alex,

applying this patch only to my merge tree does not result in any doctest failure, so I am giving this a positive review. Hopefully this will not bit us in the ass down the road ;)

Cheers,

Michael



---

archive/issue_comments_028990.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T21:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28990",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028991.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha4",
    "created_at": "2008-09-01T21:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4019",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4019#issuecomment-28991",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha4
