# Issue 4472: Sage 3.2.a3: more numerical noise in sage/calculus/wester.py

archive/issues_004472.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  devel/sage/sage/calculus/wester.py                   \n********************************************************************** \nFile \"/Users/tmp/sage-3.2.alpha3/tmp/wester.py\", line 261: \n     : [float(f(i/10)) for i in range(1,5)] \nExpected: \n     <BLANKLINE> \n     [-0.00033670040754082975, \n      -0.0027778004096620235, \n      -0.00989099409140..., \n      -0.025411145508414...] \nGot: \n     [-0.00033670040754081587, -0.0027778004096621622,   \n-0.0098909940914039818, -0.025411145508414779] \n********************************************************************** \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4472\n\n",
    "created_at": "2008-11-09T00:21:19Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.2.a3: more numerical noise in sage/calculus/wester.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4472",
    "user": "mabshoff"
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

archive/issue_comments_033034.json:
```json
{
    "body": "patch against Sage 3.2.rc1",
    "created_at": "2008-11-16T08:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4472#issuecomment-33034",
    "user": "GeorgSWeber"
}
```

patch against Sage 3.2.rc1



---

archive/issue_comments_033035.json:
```json
{
    "body": "Attachment [4472-wester.patch](tarball://root/attachments/some-uuid/ticket4472/4472-wester.patch) by GeorgSWeber created at 2008-11-16 08:21:57",
    "created_at": "2008-11-16T08:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4472#issuecomment-33035",
    "user": "GeorgSWeber"
}
```

Attachment [4472-wester.patch](tarball://root/attachments/some-uuid/ticket4472/4472-wester.patch) by GeorgSWeber created at 2008-11-16 08:21:57



---

archive/issue_comments_033036.json:
```json
{
    "body": "Looks good to me. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-16T08:56:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4472#issuecomment-33036",
    "user": "mabshoff"
}
```

Looks good to me. 

Cheers,

Michael



---

archive/issue_comments_033037.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-18T18:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4472#issuecomment-33037",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_033038.json:
```json
{
    "body": "Merged in Sage 3.2.rc2",
    "created_at": "2008-11-18T18:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4472",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4472#issuecomment-33038",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc2
