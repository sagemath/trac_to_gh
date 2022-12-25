# Issue 2806: [with patch, positive review] Sage 3.0.a2: numerical noise in sage/misc/prandom.py doctest

archive/issues_002806.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @JohnCremona\n\nJohn Cremona reported:\n\n```\nsage -t  devel/sage/sage/misc/prandom.py\n**********************************************************************\nFile \"/home/jec/sage-3.0.alpha1/tmp/prandom.py\", line 285:\n    sage: [vonmisesvariate(1.0r, 3.0r) for i in range(1, 5)]\nExpected:\n    [0.89832863935542584, 0.67180300070412846, 2.0308777524813397,\n1.7143252537251459]\nGot:\n    [0.89832863935542584, 0.67180300070412846, 2.0308777524813397,\n1.7143252537251454]\n**********************************************************************\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2806\n\n",
    "closed_at": "2008-04-05T16:19:01Z",
    "created_at": "2008-04-05T14:28:33Z",
    "labels": [
        "component: numerical",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, positive review] Sage 3.0.a2: numerical noise in sage/misc/prandom.py doctest",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2806",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @JohnCremona

John Cremona reported:

```
sage -t  devel/sage/sage/misc/prandom.py
**********************************************************************
File "/home/jec/sage-3.0.alpha1/tmp/prandom.py", line 285:
    sage: [vonmisesvariate(1.0r, 3.0r) for i in range(1, 5)]
Expected:
    [0.89832863935542584, 0.67180300070412846, 2.0308777524813397,
1.7143252537251459]
Got:
    [0.89832863935542584, 0.67180300070412846, 2.0308777524813397,
1.7143252537251454]
**********************************************************************
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2806





---

archive/issue_comments_019222.json:
```json
{
    "body": "Attachment [trac_2806.patch](tarball://root/attachments/some-uuid/ticket2806/trac_2806.patch) by mabshoff created at 2008-04-05 15:20:38",
    "created_at": "2008-04-05T15:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2806#issuecomment-19222",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2806.patch](tarball://root/attachments/some-uuid/ticket2806/trac_2806.patch) by mabshoff created at 2008-04-05 15:20:38



---

archive/issue_comments_019223.json:
```json
{
    "body": "John,\n\ncan you test if this trivial patch fixes the issue for you? The problem is that vonmisesvariate() uses standard libm math functions and hence has some precision issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-05T15:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2806#issuecomment-19223",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John,

can you test if this trivial patch fixes the issue for you? The problem is that vonmisesvariate() uses standard libm math functions and hence has some precision issues.

Cheers,

Michael



---

archive/issue_comments_019224.json:
```json
{
    "body": "Changing assignee from jkantor to mabshoff.",
    "created_at": "2008-04-05T15:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2806#issuecomment-19224",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from jkantor to mabshoff.



---

archive/issue_comments_019225.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-05T15:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2806#issuecomment-19225",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019226.json:
```json
{
    "body": "Yes, that works for me.",
    "created_at": "2008-04-05T15:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2806#issuecomment-19226",
    "user": "https://github.com/JohnCremona"
}
```

Yes, that works for me.



---

archive/issue_comments_019227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-05T16:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2806#issuecomment-19227",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006464.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-05T16:19:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2806",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2806#event-6464"
}
```



---

archive/issue_comments_019228.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-05T16:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2806#issuecomment-19228",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2
