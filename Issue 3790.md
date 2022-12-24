# Issue 3790: limit gets stuck without computing anything

archive/issues_003790.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n\n```\n I noticed that for some expressions limit() gets stuck and does not\nreturn to the sage prompt.  It does not seem to be computing anything\nsince the cpu usage is 0.\n For example in Sage 3.0.6 try:\nvars('Ax,Bx,By')\nt = -Ax*sin(sqrt(Ax^2)/2)/(sqrt(Ax^2)*sqrt(By^2 + Bx^2))\nt.limit(Ax=0,dir='above')\n\n It just sits there.  And you need to ctrl-c to get the prompt back.\nIf you set t = -Ax*sin(sqrt(Ax^2)/2)/(sqrt(Ax^2)*sqrt(By^2))\nThen do t.limit(Ax=0,dir='above'), you get a message asking if By is\nzero or nonzero.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3790\n\n",
    "created_at": "2008-08-07T22:07:41Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "limit gets stuck without computing anything",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3790",
    "user": "@mwhansen"
}
```
Assignee: @garyfurnish


```
 I noticed that for some expressions limit() gets stuck and does not
return to the sage prompt.  It does not seem to be computing anything
since the cpu usage is 0.
 For example in Sage 3.0.6 try:
vars('Ax,Bx,By')
t = -Ax*sin(sqrt(Ax^2)/2)/(sqrt(Ax^2)*sqrt(By^2 + Bx^2))
t.limit(Ax=0,dir='above')

 It just sits there.  And you need to ctrl-c to get the prompt back.
If you set t = -Ax*sin(sqrt(Ax^2)/2)/(sqrt(Ax^2)*sqrt(By^2))
Then do t.limit(Ax=0,dir='above'), you get a message asking if By is
zero or nonzero.

```


Issue created by migration from https://trac.sagemath.org/ticket/3790





---

archive/issue_comments_026950.json:
```json
{
    "body": "Attachment [trac_3790.patch](tarball://root/attachments/some-uuid/ticket3790/trac_3790.patch) by @mwhansen created at 2008-08-07 22:13:40",
    "created_at": "2008-08-07T22:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3790#issuecomment-26950",
    "user": "@mwhansen"
}
```

Attachment [trac_3790.patch](tarball://root/attachments/some-uuid/ticket3790/trac_3790.patch) by @mwhansen created at 2008-08-07 22:13:40



---

archive/issue_comments_026951.json:
```json
{
    "body": "Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-08T02:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3790#issuecomment-26951",
    "user": "mabshoff"
}
```

Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_026952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-08T23:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3790#issuecomment-26952",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026953.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-08T23:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3790#issuecomment-26953",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1
