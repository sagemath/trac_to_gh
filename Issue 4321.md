# Issue 4321: wrong Unix permissions

archive/issues_004321.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  polybori\n\nThe Unix permissions are too restrictive in sage-3.1.4, they don't allow installation on a\nmulti-user system:\n\n```\ndrwx------ 12 zimmerma cacao 4096 2008-10-17 10:13 /usr/local/sage-3.1.4/sage/local/include/boost\n-rw-------  1 zimmerma cacao 2664 2008-09-01 15:36 /usr/local/sage-3.1.4/sage/local/man/man1/ipbori.1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4321\n\n",
    "created_at": "2008-10-18T20:33:42Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "wrong Unix permissions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4321",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: mabshoff

CC:  polybori

The Unix permissions are too restrictive in sage-3.1.4, they don't allow installation on a
multi-user system:

```
drwx------ 12 zimmerma cacao 4096 2008-10-17 10:13 /usr/local/sage-3.1.4/sage/local/include/boost
-rw-------  1 zimmerma cacao 2664 2008-09-01 15:36 /usr/local/sage-3.1.4/sage/local/man/man1/ipbori.1
```


Issue created by migration from https://trac.sagemath.org/ticket/4321





---

archive/issue_comments_031587.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-30T05:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31587",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031588.json:
```json
{
    "body": "I will fix that in Sage 3.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T05:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31588",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will fix that in Sage 3.2.

Cheers,

Michael



---

archive/issue_comments_031589.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-29T10:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31589",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_031590.json:
```json
{
    "body": "Attachment [man_perms.patch](tarball://root/attachments/some-uuid/ticket4321/man_perms.patch) by PolyBoRi created at 2008-11-29 22:07:48\n\nFix man-page permissions for PolyBoRi's install target",
    "created_at": "2008-11-29T22:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31590",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Attachment [man_perms.patch](tarball://root/attachments/some-uuid/ticket4321/man_perms.patch) by PolyBoRi created at 2008-11-29 22:07:48

Fix man-page permissions for PolyBoRi's install target



---

archive/issue_comments_031591.json:
```json
{
    "body": "I believe for the man page the problem could be fixed upstream, see attached patch. \n\nBest regards,\n  Alexander",
    "created_at": "2008-11-29T22:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31591",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

I believe for the man page the problem could be fixed upstream, see attached patch. 

Best regards,
  Alexander



---

archive/issue_comments_031592.json:
```json
{
    "body": "Thanks Alexander, I will test the patch and report back. The issue with the boost permissions I will fix in the spkg itself.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T22:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31592",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Thanks Alexander, I will test the patch and report back. The issue with the boost permissions I will fix in the spkg itself.

Cheers,

Michael



---

archive/issue_comments_031593.json:
```json
{
    "body": "The spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/polybori-0.5rc.p6.spkg\n\nincorporates Alexander's fix as well as my fix to set boost permissions correctly. As a test do cp -r on $SAGE_LOCAL/include/boost as the non-owner of the files. To check for any other issues I am doing a complete cp of the Sage tree to see if anything else has permission issues.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T06:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31593",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/polybori-0.5rc.p6.spkg

incorporates Alexander's fix as well as my fix to set boost permissions correctly. As a test do cp -r on $SAGE_LOCAL/include/boost as the non-owner of the files. To check for any other issues I am doing a complete cp of the Sage tree to see if anything else has permission issues.

Cheers,

Michael



---

archive/issue_comments_031594.json:
```json
{
    "body": "Oops, wrong fix. New spkg coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T06:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31594",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, wrong fix. New spkg coming up.

Cheers,

Michael



---

archive/issue_comments_031595.json:
```json
{
    "body": "The spkg in the same place has been updated and finally fixes the issue for me.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T07:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31595",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg in the same place has been updated and finally fixes the issue for me.

Cheers,

Michael



---

archive/issue_comments_031596.json:
```json
{
    "body": "Everything looks good.",
    "created_at": "2008-12-01T08:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31596",
    "user": "https://github.com/craigcitro"
}
```

Everything looks good.



---

archive/issue_comments_031597.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1",
    "created_at": "2008-12-01T08:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31597",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.rc1



---

archive/issue_comments_031598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-01T08:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31598",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031599.json:
```json
{
    "body": "It seems to me Michael that you reviewed the patch, and I think putting it in the spkg is just sort of applying it.  So I think all that has to be done is somebody else to check that the spkg looks good. \n\nI have looked in the spkg and it looks good.  I also tried building it and it built fine.  After building, I looked at the permissions and they are now right.  so... another positive review in addition to Craig's. :-)",
    "created_at": "2008-12-01T08:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31599",
    "user": "https://github.com/williamstein"
}
```

It seems to me Michael that you reviewed the patch, and I think putting it in the spkg is just sort of applying it.  So I think all that has to be done is somebody else to check that the spkg looks good. 

I have looked in the spkg and it looks good.  I also tried building it and it built fine.  After building, I looked at the permissions and they are now right.  so... another positive review in addition to Craig's. :-)



---

archive/issue_comments_031600.json:
```json
{
    "body": "Replying to [comment:12 was]:\n> It seems to me Michael that you reviewed the patch, and I think putting it in the spkg is just sort of applying it.  So I think all that has to be done is somebody else to check that the spkg looks good. \n\nThere were two issues: one is the headers, the other one was the man page. Craig reviewed the header issue as well as Alexander's fix once I told him what it did.\n\n> I have looked in the spkg and it looks good.  I also tried building it and it built fine.  After building, I looked at the permissions and they are now right.  so... another positive review in addition to Craig's. :-)\n\nI did a cp of the whole Sage tree after fixing this and the Singular header permission issue and for now there are no more problems, so Paul can be assured that issue is gone for now. I will keep testing that no other permission issues return since Sage should never be released with such a permission problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T08:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4321#issuecomment-31600",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:12 was]:
> It seems to me Michael that you reviewed the patch, and I think putting it in the spkg is just sort of applying it.  So I think all that has to be done is somebody else to check that the spkg looks good. 

There were two issues: one is the headers, the other one was the man page. Craig reviewed the header issue as well as Alexander's fix once I told him what it did.

> I have looked in the spkg and it looks good.  I also tried building it and it built fine.  After building, I looked at the permissions and they are now right.  so... another positive review in addition to Craig's. :-)

I did a cp of the whole Sage tree after fixing this and the Singular header permission issue and for now there are no more problems, so Paul can be assured that issue is gone for now. I will keep testing that no other permission issues return since Sage should never be released with such a permission problem.

Cheers,

Michael
