# Issue 3259: [with patch; needs review] shared library versioning for flint

archive/issues_003259.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  f.r.bissey@massey.ac.nz\n\nI've attached a patch which should add shared library versioning to libflint.so.\n\nIt includes the relevant patch for the Debian package and spkg-install, and also the relevant change s to the Debian packaging.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3259\n\n",
    "created_at": "2008-05-19T22:26:53Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch; needs review] shared library versioning for flint",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3259",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

CC:  f.r.bissey@massey.ac.nz

I've attached a patch which should add shared library versioning to libflint.so.

It includes the relevant patch for the Debian package and spkg-install, and also the relevant change s to the Debian packaging.

Issue created by migration from https://trac.sagemath.org/ticket/3259





---

archive/issue_comments_022499.json:
```json
{
    "body": "Attachment [flint-soname.patch](tarball://root/attachments/some-uuid/ticket3259/flint-soname.patch) by @timabbott created at 2008-05-19 22:30:17\n\nI forgot to note this, but because flint doesn't have a static library, we only need to build it with -fPIC, which is accomplished by setting MAKECMDGOALS=library",
    "created_at": "2008-05-19T22:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3259#issuecomment-22499",
    "user": "https://github.com/timabbott"
}
```

Attachment [flint-soname.patch](tarball://root/attachments/some-uuid/ticket3259/flint-soname.patch) by @timabbott created at 2008-05-19 22:30:17

I forgot to note this, but because flint doesn't have a static library, we only need to build it with -fPIC, which is accomplished by setting MAKECMDGOALS=library



---

archive/issue_comments_022500.json:
```json
{
    "body": "I had forgotten about flint. Easy to do as my gentoo patch\nis a one liner sed command to add a soname. \n\nThe patch to the makefile looks good to me, I won't comment \non the debian package rules. The makefile already use -fpic,\ndo you have to overrule that in debian?",
    "created_at": "2008-05-19T22:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3259#issuecomment-22500",
    "user": "https://github.com/kiwifb"
}
```

I had forgotten about flint. Easy to do as my gentoo patch
is a one liner sed command to add a soname. 

The patch to the makefile looks good to me, I won't comment 
on the debian package rules. The makefile already use -fpic,
do you have to overrule that in debian?



---

archive/issue_comments_022501.json:
```json
{
    "body": "Patch looks good to me. The only issue along with #3300, i.e. that due to the copy operation we do not end up with a dynamic library and a link, but two identical copies. I fixed that in spkg-install. Positive review. The patches have been merged into \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/flint-1.06.p3.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T08:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3259#issuecomment-22501",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. The only issue along with #3300, i.e. that due to the copy operation we do not end up with a dynamic library and a link, but two identical copies. I fixed that in spkg-install. Positive review. The patches have been merged into 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/flint-1.06.p3.spkg

Cheers,

Michael



---

archive/issue_comments_022502.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-28T08:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3259#issuecomment-22502",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022503.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-28T08:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3259#issuecomment-22503",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.alpha0
