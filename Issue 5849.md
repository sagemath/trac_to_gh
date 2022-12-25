# Issue 5849: Update MPIR to 1.1.1

archive/issues_005849.json:
```json
{
    "body": "Assignee: mabshoff\n\nMPIR 1.1.1 is about to be released fixing a couple small issues that in rare circumstances can cause trouble, i.e. when a pathscale compiler is installed on x86-64. \n\nWhile we are at it: Make sure to select generic x86-64 code since right now we build code using lahf on sage.math that some early P4s did not have as mentioned on #5284. Use the SAGE_SIMD_FLAG flag to decide what to do.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5849\n\n",
    "created_at": "2009-04-22T03:56:58Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Update MPIR to 1.1.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5849",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

MPIR 1.1.1 is about to be released fixing a couple small issues that in rare circumstances can cause trouble, i.e. when a pathscale compiler is installed on x86-64. 

While we are at it: Make sure to select generic x86-64 code since right now we build code using lahf on sage.math that some early P4s did not have as mentioned on #5284. Use the SAGE_SIMD_FLAG flag to decide what to do.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5849





---

archive/issue_comments_046062.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-22T03:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5849#issuecomment-46062",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046063.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-04-24T12:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5849#issuecomment-46063",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing priority from major to critical.



---

archive/issue_comments_046064.json:
```json
{
    "body": "I would like to add that this is extremely important for me, since I cannot build sage-3.4.1 on my laptop, which is what I usually develop on.",
    "created_at": "2009-04-24T12:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5849#issuecomment-46064",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I would like to add that this is extremely important for me, since I cannot build sage-3.4.1 on my laptop, which is what I usually develop on.



---

archive/issue_comments_046065.json:
```json
{
    "body": "The spkg is at \n\n   http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/rc0/gmp-mpir-1.1.1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T07:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5849#issuecomment-46065",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg is at 

   http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/rc0/gmp-mpir-1.1.1.spkg

Cheers,

Michael



---

archive/issue_comments_046066.json:
```json
{
    "body": "Ok, bumping back to 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T09:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5849#issuecomment-46066",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, bumping back to 3.4.2.

Cheers,

Michael



---

archive/issue_comments_046067.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2009-04-30T09:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5849#issuecomment-46067",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_046068.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-01T00:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5849#issuecomment-46068",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_046069.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-01T00:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5849#issuecomment-46069",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
