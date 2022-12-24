# Issue 2848: numerical noise in sage/misc/prandom.py on MacIntel OSX 10.5/

archive/issues_002848.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  justin\n\nJustin Walker reported:\n\n```\n     sage -t  devel/sage/sage/misc/prandom.py\n     File \"/Users/tmp/sage-3.0.alpha2/tmp/prandom.py\", line 241:\n         sage: [gauss(0, 100) for i in range(3)]\n     Expected:\n         [24.916051749154448, -62.992720615792727, -8.1993122536718097]\n     Got:\n         [24.916051749154448, -62.992720615792727, -8.1993122536718115] \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2848\n\n",
    "created_at": "2008-04-07T19:49:36Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "numerical noise in sage/misc/prandom.py on MacIntel OSX 10.5/",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2848",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  justin

Justin Walker reported:

```
     sage -t  devel/sage/sage/misc/prandom.py
     File "/Users/tmp/sage-3.0.alpha2/tmp/prandom.py", line 241:
         sage: [gauss(0, 100) for i in range(3)]
     Expected:
         [24.916051749154448, -62.992720615792727, -8.1993122536718097]
     Got:
         [24.916051749154448, -62.992720615792727, -8.1993122536718115] 
```


Issue created by migration from https://trac.sagemath.org/ticket/2848





---

archive/issue_comments_019545.json:
```json
{
    "body": "Attachment [trac_2848.patch](tarball://root/attachments/some-uuid/ticket2848/trac_2848.patch) by mabshoff created at 2008-04-07 20:02:24",
    "created_at": "2008-04-07T20:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2848#issuecomment-19545",
    "user": "mabshoff"
}
```

Attachment [trac_2848.patch](tarball://root/attachments/some-uuid/ticket2848/trac_2848.patch) by mabshoff created at 2008-04-07 20:02:24



---

archive/issue_comments_019546.json:
```json
{
    "body": "Justin, \n\ncan you check if this patch fixes it for you. Provided it does fix the issue feel free to give it a positive review ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T20:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2848#issuecomment-19546",
    "user": "mabshoff"
}
```

Justin, 

can you check if this patch fixes it for you. Provided it does fix the issue feel free to give it a positive review ;)

Cheers,

Michael



---

archive/issue_comments_019547.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-07T22:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2848#issuecomment-19547",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_019548.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-07T22:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2848#issuecomment-19548",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha3



---

archive/issue_comments_019549.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T22:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2848#issuecomment-19549",
    "user": "mabshoff"
}
```

Resolution: fixed
