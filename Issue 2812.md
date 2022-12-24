# Issue 2812: [with patch; needs review] notebook.py doctests

archive/issues_002812.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2812\n\n",
    "created_at": "2008-04-05T18:56:51Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] notebook.py doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2812",
    "user": "TimothyClemans"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/2812





---

archive/issue_comments_019300.json:
```json
{
    "body": "Attachment [2812_2.patch](tarball://root/attachments/some-uuid/ticket2812/2812_2.patch) by TimothyClemans created at 2008-04-05 19:20:17\n\ndo not apply 2812_1.patch this patch corrects the encoding error",
    "created_at": "2008-04-05T19:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2812#issuecomment-19300",
    "user": "TimothyClemans"
}
```

Attachment [2812_2.patch](tarball://root/attachments/some-uuid/ticket2812/2812_2.patch) by TimothyClemans created at 2008-04-05 19:20:17

do not apply 2812_1.patch this patch corrects the encoding error



---

archive/issue_comments_019301.json:
```json
{
    "body": "I just noticed that the doctests for users and user are the same. I'll fix that as soon as I get back.",
    "created_at": "2008-04-05T20:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2812#issuecomment-19301",
    "user": "TimothyClemans"
}
```

I just noticed that the doctests for users and user are the same. I'll fix that as soon as I get back.



---

archive/issue_comments_019302.json:
```json
{
    "body": "fixes users() and user() doctests are the same issue",
    "created_at": "2008-04-05T20:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2812#issuecomment-19302",
    "user": "TimothyClemans"
}
```

fixes users() and user() doctests are the same issue



---

archive/issue_comments_019303.json:
```json
{
    "body": "Attachment [2812_4.patch](tarball://root/attachments/some-uuid/ticket2812/2812_4.patch) by TimothyClemans created at 2008-04-05 21:02:54\n\nmade sure dictonaries were sorted and changed 'mat' to 'password' and 'mark' to 'newpassword' in create_default_users() doctests",
    "created_at": "2008-04-05T21:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2812#issuecomment-19303",
    "user": "TimothyClemans"
}
```

Attachment [2812_4.patch](tarball://root/attachments/some-uuid/ticket2812/2812_4.patch) by TimothyClemans created at 2008-04-05 21:02:54

made sure dictonaries were sorted and changed 'mat' to 'password' and 'mark' to 'newpassword' in create_default_users() doctests



---

archive/issue_comments_019304.json:
```json
{
    "body": "Attachment [2812.patch](tarball://root/attachments/some-uuid/ticket2812/2812.patch) by mhansen created at 2008-04-05 21:31:38\n\nLooks good to me.  I've combined all the need patches into 2812.patch so that is the only one that needs to be applied.",
    "created_at": "2008-04-05T21:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2812#issuecomment-19304",
    "user": "mhansen"
}
```

Attachment [2812.patch](tarball://root/attachments/some-uuid/ticket2812/2812.patch) by mhansen created at 2008-04-05 21:31:38

Looks good to me.  I've combined all the need patches into 2812.patch so that is the only one that needs to be applied.



---

archive/issue_comments_019305.json:
```json
{
    "body": "Merged 2812.patch in Sage 3.0.alpha2",
    "created_at": "2008-04-05T22:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2812#issuecomment-19305",
    "user": "mabshoff"
}
```

Merged 2812.patch in Sage 3.0.alpha2



---

archive/issue_comments_019306.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-05T22:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2812#issuecomment-19306",
    "user": "mabshoff"
}
```

Resolution: fixed
