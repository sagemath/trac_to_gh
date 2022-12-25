# Issue 9308: Add an spkg-check file for GnuTLS

archive/issues_009308.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nexttime @jhpalmieri @peterjeremy\n\nGnuTLS is one of the many standard packages in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to \"yes\", no self-tests of the package will be run. This is silly, as GnuTLS has a test suite.\n\nAfter adding the required file, the test suite is run and at least on my OpenSolaris laptop, passes all tests. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9308\n\n",
    "created_at": "2010-06-22T13:28:23Z",
    "labels": [
        "component: spkg-check",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add an spkg-check file for GnuTLS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9308",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @nexttime @jhpalmieri @peterjeremy

GnuTLS is one of the many standard packages in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to "yes", no self-tests of the package will be run. This is silly, as GnuTLS has a test suite.

After adding the required file, the test suite is run and at least on my OpenSolaris laptop, passes all tests. 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9308





---

archive/issue_comments_087516.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-22T14:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9308#issuecomment-87516",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087517.json:
```json
{
    "body": "After this is added, we can see the results - in this case all 15 tests pass, on a Sony laptop running OpenSolaris 06/2009. \n\n\n```\nPASS: resume\n===================\nAll 15 tests passed\n===================\nmake[3]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/tests'\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/tests'\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/tests'\nMaking check in po\nmake[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/po'\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/po'\nmake[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src'\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src'\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing gnutls-2.2.1.p6.spkg\n```\n\n\nThe revised package may be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/gnutls-2.2.1.p6.spkg",
    "created_at": "2010-06-22T14:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9308#issuecomment-87517",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

After this is added, we can see the results - in this case all 15 tests pass, on a Sony laptop running OpenSolaris 06/2009. 


```
PASS: resume
===================
All 15 tests passed
===================
make[3]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/tests'
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/tests'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/tests'
Making check in po
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/po'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src/po'
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6/src'
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/gnutls-2.2.1.p6
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing gnutls-2.2.1.p6.spkg
```


The revised package may be found at 

http://boxen.math.washington.edu/home/kirkby/patches/gnutls-2.2.1.p6.spkg



---

archive/issue_comments_087518.json:
```json
{
    "body": "Mercurial patch to add an spkg-check to enable self-tests",
    "created_at": "2010-06-22T14:01:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9308#issuecomment-87518",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Mercurial patch to add an spkg-check to enable self-tests



---

archive/issue_comments_087519.json:
```json
{
    "body": "Attachment [9308.patch](tarball://root/attachments/some-uuid/ticket9308/9308.patch) by drkirkby created at 2010-07-16 15:11:17\n\nAgain, cc'ing a few people who seem keen to improve the quality of Sage. \n\nDave",
    "created_at": "2010-07-16T15:11:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9308#issuecomment-87519",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9308.patch](tarball://root/attachments/some-uuid/ticket9308/9308.patch) by drkirkby created at 2010-07-16 15:11:17

Again, cc'ing a few people who seem keen to improve the quality of Sage. 

Dave



---

archive/issue_comments_087520.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-10-05T09:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9308#issuecomment-87520",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_087521.json:
```json
{
    "body": "Invalid since GNUTLS is no longer part of Sage.",
    "created_at": "2012-10-05T09:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9308",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9308#issuecomment-87521",
    "user": "https://github.com/jdemeyer"
}
```

Invalid since GNUTLS is no longer part of Sage.
