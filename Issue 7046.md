# Issue 7046: Singular fails to build on OS X 10.6 with case sensitive file system

archive/issues_007046.json:
```json
{
    "body": "Assignee: tbd\n\nThere is a typo in spkg-install so that a patched file doesn't get copied and building fails.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7046\n\n",
    "created_at": "2009-09-28T08:34:12Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Singular fails to build on OS X 10.6 with case sensitive file system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7046",
    "user": "https://github.com/gvol"
}
```
Assignee: tbd

There is a typo in spkg-install so that a patched file doesn't get copied and building fails.

Issue created by migration from https://trac.sagemath.org/ticket/7046





---

archive/issue_comments_058220.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-09-28T08:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58220",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_058221.json:
```json
{
    "body": "Should be patched against the `spkg-install` of the Singular spkg.",
    "created_at": "2009-09-28T08:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58221",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Should be patched against the `spkg-install` of the Singular spkg.



---

archive/issue_comments_058222.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2009-09-28T08:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58222",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_058223.json:
```json
{
    "body": "Changing component from build to packages.",
    "created_at": "2009-09-28T08:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58223",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from build to packages.



---

archive/issue_comments_058224.json:
```json
{
    "body": "based on Sage 4.1.2.alpha4",
    "created_at": "2009-09-28T08:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58224",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.1.2.alpha4



---

archive/issue_comments_058225.json:
```json
{
    "body": "Attachment [trac_7046-singular_build.patch](tarball://root/attachments/some-uuid/ticket7046/trac_7046-singular_build.patch) by mvngu created at 2009-09-28 08:57:07\n\nUpdated Singular package at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/singular-3-1-0-4-20090818.p1.spkg",
    "created_at": "2009-09-28T08:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58225",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7046-singular_build.patch](tarball://root/attachments/some-uuid/ticket7046/trac_7046-singular_build.patch) by mvngu created at 2009-09-28 08:57:07

Updated Singular package at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/singular-3-1-0-4-20090818.p1.spkg



---

archive/issue_comments_058226.json:
```json
{
    "body": "Attachment [doctest-4.1.2.alpha4-bsd.math-7046.log.bz2](tarball://root/attachments/some-uuid/ticket7046/doctest-4.1.2.alpha4-bsd.math-7046.log.bz2) by mvngu created at 2009-09-30 04:13:56\n\ndoctest log for bsd.math with Sage 4.1.2.alpha4 and updated Singular spkg",
    "created_at": "2009-09-30T04:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58226",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [doctest-4.1.2.alpha4-bsd.math-7046.log.bz2](tarball://root/attachments/some-uuid/ticket7046/doctest-4.1.2.alpha4-bsd.math-7046.log.bz2) by mvngu created at 2009-09-30 04:13:56

doctest log for bsd.math with Sage 4.1.2.alpha4 and updated Singular spkg



---

archive/issue_comments_058227.json:
```json
{
    "body": "doctest log for cicero with Sage 4.1.2.alpha4 and updated Singular spkg",
    "created_at": "2009-09-30T04:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58227",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

doctest log for cicero with Sage 4.1.2.alpha4 and updated Singular spkg



---

archive/issue_comments_058228.json:
```json
{
    "body": "Attachment [doctest-4.1.2.alpha4-cicero-7046.log.bz2](tarball://root/attachments/some-uuid/ticket7046/doctest-4.1.2.alpha4-cicero-7046.log.bz2) by mvngu created at 2009-09-30 12:00:21\n\ninstall log for t2.math with Sage 4.1.2.alpha4 and updated Singular spkg",
    "created_at": "2009-09-30T12:00:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58228",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [doctest-4.1.2.alpha4-cicero-7046.log.bz2](tarball://root/attachments/some-uuid/ticket7046/doctest-4.1.2.alpha4-cicero-7046.log.bz2) by mvngu created at 2009-09-30 12:00:21

install log for t2.math with Sage 4.1.2.alpha4 and updated Singular spkg



---

archive/issue_comments_058229.json:
```json
{
    "body": "Attachment [install-4.1.2.alpha4-t2.math-7046.log.bz2](tarball://root/attachments/some-uuid/ticket7046/install-4.1.2.alpha4-t2.math-7046.log.bz2) by mvngu created at 2009-09-30 12:02:01\n\nReport of my testing on various platforms with the updated Singular package and the cliquer spkg at #6681:\n\n* sage.math: 64-bit Ubuntu 8.04.3 LTS --- compile OK; all doctests pass.\n* bsd.math: 64-bit Mac OS X 10.6 --- compile OK; many doctest failures, all of which have been reported to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/cdcf10c5c730f5b5). The full doctest log is attached.\n* rosemary.math: 64-bit RHEL 5.4 --- compile OK; all doctests pass.\n* cicero on SkyNet: 32-bit Fedora 9 --- compile OK; some doctest failures, all of which have been reported to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/6abc4e530a6cd626). The full doctest log is attached.\n* eno on SkyNet: 64-bit Fedora 9 --- compile OK; all doctests pass.\n* lena on SkyNet: 64-bit RHEL 5.3 --- compile OK; all doctests pass.\n* menas on SkyNet: 64-bit openSUSE 11.1 --- compile OK; all doctests pass.\n* t2.math: SPARC Solaris with GCC 4.4.1 --- compilation abort when trying to install sage-4.1.2.alpha4.spkg; got past installing Singular, though. The full install log is attached.",
    "created_at": "2009-09-30T12:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58229",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [install-4.1.2.alpha4-t2.math-7046.log.bz2](tarball://root/attachments/some-uuid/ticket7046/install-4.1.2.alpha4-t2.math-7046.log.bz2) by mvngu created at 2009-09-30 12:02:01

Report of my testing on various platforms with the updated Singular package and the cliquer spkg at #6681:

* sage.math: 64-bit Ubuntu 8.04.3 LTS --- compile OK; all doctests pass.
* bsd.math: 64-bit Mac OS X 10.6 --- compile OK; many doctest failures, all of which have been reported to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/cdcf10c5c730f5b5). The full doctest log is attached.
* rosemary.math: 64-bit RHEL 5.4 --- compile OK; all doctests pass.
* cicero on SkyNet: 32-bit Fedora 9 --- compile OK; some doctest failures, all of which have been reported to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/6abc4e530a6cd626). The full doctest log is attached.
* eno on SkyNet: 64-bit Fedora 9 --- compile OK; all doctests pass.
* lena on SkyNet: 64-bit RHEL 5.3 --- compile OK; all doctests pass.
* menas on SkyNet: 64-bit openSUSE 11.1 --- compile OK; all doctests pass.
* t2.math: SPARC Solaris with GCC 4.4.1 --- compilation abort when trying to install sage-4.1.2.alpha4.spkg; got past installing Singular, though. The full install log is attached.



---

archive/issue_comments_058230.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-30T12:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58230",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_058231.json:
```json
{
    "body": "Merged `singular-3-1-0-4-20090818.p1.spkg` in the standard packages repository.",
    "created_at": "2009-09-30T12:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7046#issuecomment-58231",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `singular-3-1-0-4-20090818.p1.spkg` in the standard packages repository.
