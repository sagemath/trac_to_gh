# Issue 3234: [with patch; needs review] cygwin -- make numpy work with cygwin

archive/issues_003234.json:
```json
{
    "body": "Assignee: mabshoff\n\nPatch here:\n\nhttp://sage.math.washington.edu/home/was/cygwin/numpy-20080104-1.0.4.p3.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/3234\n\n",
    "created_at": "2008-05-17T00:39:17Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch; needs review] cygwin -- make numpy work with cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3234",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Patch here:

http://sage.math.washington.edu/home/was/cygwin/numpy-20080104-1.0.4.p3.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3234





---

archive/issue_comments_022359.json:
```json
{
    "body": "Spkg looks good to me. I think that the core issue is with ATLAS's dynamic libraries being miscompiled on Cygwin, but we can explore that down the road. Having a working, but slightly slower,  numpy for now is better than no numpy at all on Cygwin.\n\nI also fixed some small formatting issue in SPKG.txt. In total: positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-18T13:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3234#issuecomment-22359",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg looks good to me. I think that the core issue is with ATLAS's dynamic libraries being miscompiled on Cygwin, but we can explore that down the road. Having a working, but slightly slower,  numpy for now is better than no numpy at all on Cygwin.

I also fixed some small formatting issue in SPKG.txt. In total: positive review.

Cheers,

Michael



---

archive/issue_comments_022360.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-18T13:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3234#issuecomment-22360",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_events_007274.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-18T13:29:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3234",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3234#event-7274"
}
```



---

archive/issue_comments_022361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-18T13:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3234#issuecomment-22361",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
