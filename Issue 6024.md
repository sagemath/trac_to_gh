# Issue 6024: ecl->clisp switch

archive/issues_006024.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is required for gcc 4.4.0, Solaris and so on.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/6024\n\n",
    "created_at": "2009-05-12T06:11:52Z",
    "labels": [
        "component: porting",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "ecl->clisp switch",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6024",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

This is required for gcc 4.4.0, Solaris and so on.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/6024





---

archive/issue_comments_047884.json:
```json
{
    "body": "Attachment [trac_6024-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket6024/trac_6024-doctest-fix.patch) by mabshoff created at 2009-05-12 06:14:17",
    "created_at": "2009-05-12T06:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_6024-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket6024/trac_6024-doctest-fix.patch) by mabshoff created at 2009-05-12 06:14:17



---

archive/issue_comments_047885.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-12T06:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_014150.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-12T07:40:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6024#event-14150"
}
```



---

archive/issue_comments_047886.json:
```json
{
    "body": "The new Maxima is at \n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/maxima-5.16.3.p2.spkg\n\nNote that the ecl.spkg is still missing and will be next.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T14:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The new Maxima is at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/maxima-5.16.3.p2.spkg

Note that the ecl.spkg is still missing and will be next.

Cheers,

Michael



---

archive/issue_comments_047887.json:
```json
{
    "body": "The ecl.spkg skpg that now finally works is at \n\n   http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/ecl-9.4.1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T20:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47887",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The ecl.spkg skpg that now finally works is at 

   http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/ecl-9.4.1.spkg

Cheers,

Michael



---

archive/issue_comments_047888.json:
```json
{
    "body": "Positive review pending:\n\n1. Remove the msvc directory for now.\n\n2. Put \"unset MAKE\" at the top of spkg-install for now, since it definitely breaks if one doesn't do that.",
    "created_at": "2009-05-16T00:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47888",
    "user": "https://github.com/williamstein"
}
```

Positive review pending:

1. Remove the msvc directory for now.

2. Put "unset MAKE" at the top of spkg-install for now, since it definitely breaks if one doesn't do that.



---

archive/issue_comments_047889.json:
```json
{
    "body": "ok, full positive review.",
    "created_at": "2009-05-16T00:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47889",
    "user": "https://github.com/williamstein"
}
```

ok, full positive review.



---

archive/issue_comments_047890.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-16T00:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47890",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047891.json:
```json
{
    "body": "Merged both spkgs and the patch in Sage 4.0.alpha0. \n\nI also fixed deps and install accordingly.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-16T00:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47891",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both spkgs and the patch in Sage 4.0.alpha0. 

I also fixed deps and install accordingly.

Cheers,

Michael



---

archive/issue_events_014151.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-16T00:27:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6024#event-14151"
}
```
