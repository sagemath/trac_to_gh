# Issue 3234: [with patch; needs review] cygwin -- make numpy work with cygwin

archive/issues_003234.json:
```json
{
    "body": "Assignee: mabshoff\n\nPatch here:\n\nhttp://sage.math.washington.edu/home/was/cygwin/numpy-20080104-1.0.4.p3.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/3234\n\n",
    "created_at": "2008-05-17T00:39:17Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch; needs review] cygwin -- make numpy work with cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3234",
    "user": "@williamstein"
}
```
Assignee: mabshoff

Patch here:

http://sage.math.washington.edu/home/was/cygwin/numpy-20080104-1.0.4.p3.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3234





---

archive/issue_comments_022406.json:
```json
{
    "body": "Spkg looks good to me. I think that the core issue is with ATLAS's dynamic libraries being miscompiled on Cygwin, but we can explore that down the road. Having a working, but slightly slower,  numpy for now is better than no numpy at all on Cygwin.\n\nI also fixed some small formatting issue in SPKG.txt. In total: positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-18T13:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3234#issuecomment-22406",
    "user": "mabshoff"
}
```

Spkg looks good to me. I think that the core issue is with ATLAS's dynamic libraries being miscompiled on Cygwin, but we can explore that down the road. Having a working, but slightly slower,  numpy for now is better than no numpy at all on Cygwin.

I also fixed some small formatting issue in SPKG.txt. In total: positive review.

Cheers,

Michael



---

archive/issue_comments_022407.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-18T13:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3234#issuecomment-22407",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_comments_022408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-18T13:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3234",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3234#issuecomment-22408",
    "user": "mabshoff"
}
```

Resolution: fixed
