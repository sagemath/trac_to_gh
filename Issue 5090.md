# Issue 5090: upgrade numpy to 1.2.1

archive/issues_005090.json:
```json
{
    "body": "Assignee: @williamstein\n\nAn spkg is at http://sage.math.washington.edu/home/jason/numpy-1.2.1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/5090\n\n",
    "created_at": "2009-01-24T16:35:47Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "upgrade numpy to 1.2.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5090",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

An spkg is at http://sage.math.washington.edu/home/jason/numpy-1.2.1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/5090





---

archive/issue_comments_038780.json:
```json
{
    "body": "Jason,\n\nthis sounds like it is ready to be reviewed. Am I correct?\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T18:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38780",
    "user": "mabshoff"
}
```

Jason,

this sounds like it is ready to be reviewed. Am I correct?

Cheers,

Michael



---

archive/issue_comments_038781.json:
```json
{
    "body": "Changing component from linear algebra to packages.",
    "created_at": "2009-01-24T18:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38781",
    "user": "mabshoff"
}
```

Changing component from linear algebra to packages.



---

archive/issue_comments_038782.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2009-01-24T18:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38782",
    "user": "mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_038783.json:
```json
{
    "body": "And this is a package, so move it from linear algebra.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T18:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38783",
    "user": "mabshoff"
}
```

And this is a package, so move it from linear algebra.

Cheers,

Michael



---

archive/issue_comments_038784.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T18:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38784",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038785.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T18:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38785",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2

Cheers,

Michael



---

archive/issue_comments_038786.json:
```json
{
    "body": "Oops, I will review this later.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T18:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38786",
    "user": "mabshoff"
}
```

Oops, I will review this later.

Cheers,

Michael



---

archive/issue_comments_038787.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-01-24T18:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38787",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_038788.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-01-24T18:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38788",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_038789.json:
```json
{
    "body": "Michael, yes you are correct on all accounts.",
    "created_at": "2009-01-24T21:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38789",
    "user": "@jasongrout"
}
```

Michael, yes you are correct on all accounts.



---

archive/issue_comments_038790.json:
```json
{
    "body": "Actually, I just remembered that I removed the patch which silenced deprecation warnings.  This was because I was hoping this spkg would be merged with the new scipy 0.7, and the deprecated calls would be fixed.  So we should hold off on this upgrade for now.",
    "created_at": "2009-01-25T02:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38790",
    "user": "@jasongrout"
}
```

Actually, I just remembered that I removed the patch which silenced deprecation warnings.  This was because I was hoping this spkg would be merged with the new scipy 0.7, and the deprecated calls would be fixed.  So we should hold off on this upgrade for now.



---

archive/issue_comments_038791.json:
```json
{
    "body": "This has been superseded by #6140, which has been merged in `4.0.2.alpha0`. I'm closing as `wontfix`, though maybe `duplicate` is just as good.",
    "created_at": "2009-06-12T06:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38791",
    "user": "@craigcitro"
}
```

This has been superseded by #6140, which has been merged in `4.0.2.alpha0`. I'm closing as `wontfix`, though maybe `duplicate` is just as good.



---

archive/issue_comments_038792.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-06-12T06:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5090",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5090#issuecomment-38792",
    "user": "@craigcitro"
}
```

Resolution: wontfix
