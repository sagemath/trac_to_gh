# Issue 3710: Segfault in Tachyon on some latest GCC versions

archive/issues_003710.json:
```json
{
    "body": "Assignee: @williamstein\n\nSegfault confirmed on 32 bit linux with GCC 4.3.1 and GCC 4.2.4, versions prior to GCC 4.2.3 including should work, status of version 4.3.0 is still not known, also status of 64 bit builds is not known. This bug is bug in gcc or bug in Tachyon that showed up after some changes to GCC somewhere in between 2008-02-01 and 2008-05-19. Status of 64 bit version is unknown because I have no access to hardware with those compile versions.\n\nWhen 32 bit threaded version of Tachyon is built using \"make linux-thr\" and used to render attached scene, it segfaults around 59%. Non threaded version works (one built with \"make linux\"), threaded version works when -fno-crossjumping -fno-reorder-blocks compilation flags are added.\n\nStill working to get smaller test case and informations on gcc 4.3.0, there will hopefully be patch/spkg soon.\n\nThis ticket is follow-up of report from \"Sage 3.0.6.alpha0 released\" sage-devel thread.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3710\n\n",
    "created_at": "2008-07-23T00:18:44Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Segfault in Tachyon on some latest GCC versions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3710",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```
Assignee: @williamstein

Segfault confirmed on 32 bit linux with GCC 4.3.1 and GCC 4.2.4, versions prior to GCC 4.2.3 including should work, status of version 4.3.0 is still not known, also status of 64 bit builds is not known. This bug is bug in gcc or bug in Tachyon that showed up after some changes to GCC somewhere in between 2008-02-01 and 2008-05-19. Status of 64 bit version is unknown because I have no access to hardware with those compile versions.

When 32 bit threaded version of Tachyon is built using "make linux-thr" and used to render attached scene, it segfaults around 59%. Non threaded version works (one built with "make linux"), threaded version works when -fno-crossjumping -fno-reorder-blocks compilation flags are added.

Still working to get smaller test case and informations on gcc 4.3.0, there will hopefully be patch/spkg soon.

This ticket is follow-up of report from "Sage 3.0.6.alpha0 released" sage-devel thread.


Issue created by migration from https://trac.sagemath.org/ticket/3710





---

archive/issue_comments_026275.json:
```json
{
    "body": "testcase made from simplified doctest example that was found to segfault",
    "created_at": "2008-07-23T00:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26275",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

testcase made from simplified doctest example that was found to segfault



---

archive/issue_comments_026276.json:
```json
{
    "body": "Changing assignee from @williamstein to aginiewicz.",
    "created_at": "2008-07-23T00:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26276",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Changing assignee from @williamstein to aginiewicz.



---

archive/issue_comments_026277.json:
```json
{
    "body": "Attachment [test.dat](tarball://root/attachments/some-uuid/ticket3710/test.dat) by aginiewicz created at 2008-07-23 00:20:15",
    "created_at": "2008-07-23T00:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26277",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Attachment [test.dat](tarball://root/attachments/some-uuid/ticket3710/test.dat) by aginiewicz created at 2008-07-23 00:20:15



---

archive/issue_comments_026278.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-23T00:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26278",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026279.json:
```json
{
    "body": "There's what I did to fix it: I added gcc version check and set GCCFIX variable to flags needed to fix the issue for gcc 4.2.4 and all 4.3.* (I wasn't able to test 4.3.0), also added simple patch that adds it to src/unix/Make-arch... I put it into patches directory and spkg-install, basing how it's done with some other packages\n\nI hope all is ok because that's my only second fix but first tracked from start and with own ticket... if anything would look better other way I'd be happy to know",
    "created_at": "2008-08-02T02:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26279",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

There's what I did to fix it: I added gcc version check and set GCCFIX variable to flags needed to fix the issue for gcc 4.2.4 and all 4.3.* (I wasn't able to test 4.3.0), also added simple patch that adds it to src/unix/Make-arch... I put it into patches directory and spkg-install, basing how it's done with some other packages

I hope all is ok because that's my only second fix but first tracked from start and with own ticket... if anything would look better other way I'd be happy to know



---

archive/issue_comments_026280.json:
```json
{
    "body": "btw, as this is segfault fix only I guess it could go to 3.1 so I reassign it to 3.1 as I don't know if before release tickets ready to review from next milestone are searched for... are there reasons for it to not make in for 3.1?\n\ncheers,\nAndrzej.",
    "created_at": "2008-08-03T00:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26280",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

btw, as this is segfault fix only I guess it could go to 3.1 so I reassign it to 3.1 as I don't know if before release tickets ready to review from next milestone are searched for... are there reasons for it to not make in for 3.1?

cheers,
Andrzej.



---

archive/issue_comments_026281.json:
```json
{
    "body": "Changed spkg along with information from #3882 - there are both patch (to generate new file if new version of Tachyon will come out) and patched file that is copied over.",
    "created_at": "2008-08-17T20:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26281",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Changed spkg along with information from #3882 - there are both patch (to generate new file if new version of Tachyon will come out) and patched file that is copied over.



---

archive/issue_comments_026282.json:
```json
{
    "body": "Hi Andrzej,\n\na couple remarks:\n\n* You deleted the hg history of the spkg - that is not good :)\n* Instead of the construct using \"gcc -v ...\" it is much easier to use \"gcc -dumpversion\". I did that in the updated spkg.\n* Please do not attach spkgs to tickets. Put them up somewhere and post a link.\n\nI am giving the spkg with the changes I made a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T21:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26282",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Andrzej,

a couple remarks:

* You deleted the hg history of the spkg - that is not good :)
* Instead of the construct using "gcc -v ..." it is much easier to use "gcc -dumpversion". I did that in the updated spkg.
* Please do not attach spkgs to tickets. Put them up somewhere and post a link.

I am giving the spkg with the changes I made a positive review.

Cheers,

Michael



---

archive/issue_comments_026283.json:
```json
{
    "body": "For the record: the updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha0/tachyon-0.98beta.p6.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T21:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26283",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: the updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha0/tachyon-0.98beta.p6.spkg

Cheers,

Michael



---

archive/issue_comments_026284.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0",
    "created_at": "2008-08-22T21:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26284",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha0



---

archive/issue_comments_026285.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-22T21:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26285",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003930.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-22T21:42:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3710#event-3930"
}
```



---

archive/issue_comments_026286.json:
```json
{
    "body": "will know next time, thanks for pointing all this out!",
    "created_at": "2008-08-23T03:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3710#issuecomment-26286",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

will know next time, thanks for pointing all this out!
