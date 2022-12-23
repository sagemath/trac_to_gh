# Issue 3230: [with patch; needs review] cygwin -- new givaro spkg that works around stupidity in cygwin

archive/issues_003230.json:
```json
{
    "body": "Assignee: mabshoff\n\nCygwin forgot this line in math.h: \n\n```\nextern double logb _PARAMS((double));\n```\n\n\nI put that line in the relevant file (see spkg-install) and now the build works fine. \n\nThe new spkg is here:\n\nhttp://sage.math.washington.edu/home/was/cygwin/givaro-3.2.10.rc3.p2.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/3230\n\n",
    "created_at": "2008-05-16T22:29:05Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] cygwin -- new givaro spkg that works around stupidity in cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3230",
    "user": "was"
}
```
Assignee: mabshoff

Cygwin forgot this line in math.h: 

```
extern double logb _PARAMS((double));
```


I put that line in the relevant file (see spkg-install) and now the build works fine. 

The new spkg is here:

http://sage.math.washington.edu/home/was/cygwin/givaro-3.2.10.rc3.p2.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3230





---

archive/issue_comments_022342.json:
```json
{
    "body": "Spkg looks good to me. I added a diff of givtablelimits.h to the patches directory. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-18T17:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3230#issuecomment-22342",
    "user": "mabshoff"
}
```

Spkg looks good to me. I added a diff of givtablelimits.h to the patches directory. Positive review.

Cheers,

Michael



---

archive/issue_comments_022343.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-18T17:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3230#issuecomment-22343",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022344.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-18T17:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3230#issuecomment-22344",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha1
