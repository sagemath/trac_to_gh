# Issue 3647: [with spkg, needs review] remove "- static-libgcc" from lcalc's CFLAGS

archive/issues_003647.json:
```json
{
    "body": "Assignee: mabshoff\n\nAt some point we added \"-static-libgcc\" to lcalc's CFLAGS. I am not so sure why we did it since the reasoning behind it is undocumented and I cannot imagine any reason why we should use it. This is causing trouble on some build platoforms, see\n\nhttps://groups.google.com/group/sage-support/browse_thread/thread/a0e26173803f11d4/92f2602b2c448b59#92f2602b2c448b59\n\nThe spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/lcalc-20080205.p2.spkg\n\nremoves that option.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3647\n\n",
    "created_at": "2008-07-12T13:44:20Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with spkg, needs review] remove \"- static-libgcc\" from lcalc's CFLAGS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3647",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

At some point we added "-static-libgcc" to lcalc's CFLAGS. I am not so sure why we did it since the reasoning behind it is undocumented and I cannot imagine any reason why we should use it. This is causing trouble on some build platoforms, see

https://groups.google.com/group/sage-support/browse_thread/thread/a0e26173803f11d4/92f2602b2c448b59#92f2602b2c448b59

The spkg at

http://sage.math.washington.edu/home/mabshoff/lcalc-20080205.p2.spkg

removes that option.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3647





---

archive/issue_comments_025742.json:
```json
{
    "body": "There is some interesting discussion why \"-static-libgcc\" seem to be a can of worms at\n\nhttp://www.trilithium.com/johan/2005/06/static-libstdc/\n\nCheers,\n\nMichael",
    "created_at": "2008-07-12T13:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3647#issuecomment-25742",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is some interesting discussion why "-static-libgcc" seem to be a can of worms at

http://www.trilithium.com/johan/2005/06/static-libstdc/

Cheers,

Michael



---

archive/issue_comments_025743.json:
```json
{
    "body": "+1",
    "created_at": "2008-07-16T04:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3647#issuecomment-25743",
    "user": "https://github.com/mwhansen"
}
```

+1



---

archive/issue_comments_025744.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-16T05:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3647#issuecomment-25744",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025745.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-16T05:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3647#issuecomment-25745",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.alpha0
