# Issue 4472: Sage 3.2.a3: more numerical noise in sage/calculus/wester.py

archive/issues_004472.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  devel/sage/sage/calculus/wester.py                   \n********************************************************************** \nFile \"/Users/tmp/sage-3.2.alpha3/tmp/wester.py\", line 261: \n     : [float(f(i/10)) for i in range(1,5)] \nExpected: \n     <BLANKLINE> \n     [-0.00033670040754082975, \n      -0.0027778004096620235, \n      -0.00989099409140..., \n      -0.025411145508414...] \nGot: \n     [-0.00033670040754081587, -0.0027778004096621622,   \n-0.0098909940914039818, -0.025411145508414779] \n********************************************************************** \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4472\n\n",
    "created_at": "2008-11-09T00:21:19Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.2.a3: more numerical noise in sage/calculus/wester.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4472",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
sage -t  devel/sage/sage/calculus/wester.py                   
********************************************************************** 
File "/Users/tmp/sage-3.2.alpha3/tmp/wester.py", line 261: 
     : [float(f(i/10)) for i in range(1,5)] 
Expected: 
     <BLANKLINE> 
     [-0.00033670040754082975, 
      -0.0027778004096620235, 
      -0.00989099409140..., 
      -0.025411145508414...] 
Got: 
     [-0.00033670040754081587, -0.0027778004096621622,   
-0.0098909940914039818, -0.025411145508414779] 
********************************************************************** 
```


Issue created by migration from https://trac.sagemath.org/ticket/4472





---

archive/issue_comments_032969.json:
```json
{
    "body": "patch against Sage 3.2.rc1",
    "created_at": "2008-11-16T08:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4472#issuecomment-32969",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

patch against Sage 3.2.rc1



---

archive/issue_comments_032970.json:
```json
{
    "body": "Attachment [4472-wester.patch](tarball://root/attachments/some-uuid/ticket4472/4472-wester.patch) by GeorgSWeber created at 2008-11-16 08:21:57",
    "created_at": "2008-11-16T08:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4472#issuecomment-32970",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [4472-wester.patch](tarball://root/attachments/some-uuid/ticket4472/4472-wester.patch) by GeorgSWeber created at 2008-11-16 08:21:57



---

archive/issue_comments_032971.json:
```json
{
    "body": "Looks good to me. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-16T08:56:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4472#issuecomment-32971",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me. 

Cheers,

Michael



---

archive/issue_comments_032972.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-18T18:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4472#issuecomment-32972",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032973.json:
```json
{
    "body": "Merged in Sage 3.2.rc2",
    "created_at": "2008-11-18T18:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4472#issuecomment-32973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.rc2



---

archive/issue_events_010104.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-18T18:14:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4472#event-10104"
}
```
