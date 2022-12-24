# Issue 6024: ecl->clisp switch

archive/issues_006024.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is required for gcc 4.4.0, Solaris and so on.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/6024\n\n",
    "created_at": "2009-05-12T06:11:52Z",
    "labels": [
        "porting",
        "blocker",
        "bug"
    ],
    "title": "ecl->clisp switch",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6024",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This is required for gcc 4.4.0, Solaris and so on.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/6024





---

archive/issue_comments_047975.json:
```json
{
    "body": "Attachment [trac_6024-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket6024/trac_6024-doctest-fix.patch) by mabshoff created at 2009-05-12 06:14:17",
    "created_at": "2009-05-12T06:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47975",
    "user": "mabshoff"
}
```

Attachment [trac_6024-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket6024/trac_6024-doctest-fix.patch) by mabshoff created at 2009-05-12 06:14:17



---

archive/issue_comments_047976.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-12T06:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47976",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047977.json:
```json
{
    "body": "The new Maxima is at \n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/maxima-5.16.3.p2.spkg\n\nNote that the ecl.spkg is still missing and will be next.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T14:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47977",
    "user": "mabshoff"
}
```

The new Maxima is at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/maxima-5.16.3.p2.spkg

Note that the ecl.spkg is still missing and will be next.

Cheers,

Michael



---

archive/issue_comments_047978.json:
```json
{
    "body": "The ecl.spkg skpg that now finally works is at \n\n   http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/ecl-9.4.1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T20:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47978",
    "user": "mabshoff"
}
```

The ecl.spkg skpg that now finally works is at 

   http://sage.math.washington.edu/home/mabshoff/release-cycles-4.0/alpha0/ecl-9.4.1.spkg

Cheers,

Michael



---

archive/issue_comments_047979.json:
```json
{
    "body": "Positive review pending:\n\n1. Remove the msvc directory for now.\n\n2. Put \"unset MAKE\" at the top of spkg-install for now, since it definitely breaks if one doesn't do that.",
    "created_at": "2009-05-16T00:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47979",
    "user": "was"
}
```

Positive review pending:

1. Remove the msvc directory for now.

2. Put "unset MAKE" at the top of spkg-install for now, since it definitely breaks if one doesn't do that.



---

archive/issue_comments_047980.json:
```json
{
    "body": "ok, full positive review.",
    "created_at": "2009-05-16T00:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47980",
    "user": "was"
}
```

ok, full positive review.



---

archive/issue_comments_047981.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-16T00:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47981",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047982.json:
```json
{
    "body": "Merged both spkgs and the patch in Sage 4.0.alpha0. \n\nI also fixed deps and install accordingly.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-16T00:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6024",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6024#issuecomment-47982",
    "user": "mabshoff"
}
```

Merged both spkgs and the patch in Sage 4.0.alpha0. 

I also fixed deps and install accordingly.

Cheers,

Michael
