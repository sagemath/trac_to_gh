# Issue 7073: scipy_sandbox 20071020.p4 has a GNUism, sending GNU flags to the Sun compiler.

archive/issues_007073.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: GNUism fortran\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha4\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used #7021 \n\n\n```\nscipy_sandbox-20071020.p4/patches/setup.py.arpack\nscipy_sandbox-20071020.p4/patches/setup.py~\nscipy_sandbox-20071020.p4/patches/setup.py.spline\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nf95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise\nf95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise\nUsage: f95 [ options ] files.  Use 'f95 -flags' for details\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7073\n\n",
    "created_at": "2009-09-29T13:44:33Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "scipy_sandbox 20071020.p4 has a GNUism, sending GNU flags to the Sun compiler.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7073",
    "user": "drkirkby"
}
```
Assignee: tbd

Keywords: GNUism fortran

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha4
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used #7021 


```
scipy_sandbox-20071020.p4/patches/setup.py.arpack
scipy_sandbox-20071020.p4/patches/setup.py~
scipy_sandbox-20071020.p4/patches/setup.py.spline
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details
```



Issue created by migration from https://trac.sagemath.org/ticket/7073





---

archive/issue_comments_058501.json:
```json
{
    "body": "scipy_sandbox is no longer a package.",
    "created_at": "2015-09-08T12:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7073#issuecomment-58501",
    "user": "jdemeyer"
}
```

scipy_sandbox is no longer a package.



---

archive/issue_comments_058502.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-09-08T12:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7073#issuecomment-58502",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058503.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-08T12:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7073#issuecomment-58503",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058504.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-09-12T13:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7073#issuecomment-58504",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_058505.json:
```json
{
    "body": "Maybe I am being pedantic, but should this not be wontfix?",
    "created_at": "2015-09-12T15:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7073#issuecomment-58505",
    "user": "drkirkby"
}
```

Maybe I am being pedantic, but should this not be wontfix?



---

archive/issue_comments_058506.json:
```json
{
    "body": "More likely invalid, but it doesn't really matter.",
    "created_at": "2015-09-12T22:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7073#issuecomment-58506",
    "user": "jdemeyer"
}
```

More likely invalid, but it doesn't really matter.
