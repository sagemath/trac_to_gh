# Issue 7025: givaro 3.2.13rc2 says GMP is not installed, even though MPIR is.

archive/issues_007025.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @dimpase\n\nMPIR is supposed to be a substitute for GMP. When using the Sun compiler with sage-4.1.2.alpha2, givaro-3.2.13rc2 seems to think GMP is not installed, even though the substitute mpir is installed. See below. \n\nIt works on Solaris if gcc is used, which is a bit odd. I checked to see if the mpir had created the header files and libraries, and see that local/include/gmp.h and local/lib/libgmp.* do in fact exist, so mpir really has been installed. \n\n\n\n```\ngivaro-3.2.13rc2/src/examples/Polynomial/pol_eval.C\ngivaro-3.2.13rc2/src/examples/Polynomial/pol_factor.C\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nCopying updated gmp++.h\nchecking for a BSD-compatible install... /usr/local/bin/ginstall -c\nchecking whether build environment is sane... yes\nchecking for a thread-safe mkdir -p... ./install-sh -c -d\n<SNIP>\nchecking for GMP >= 3.1.1... not found\n*******************************************************************************\n ERROR: GMP not found!\n\n GMP version 3.1.1 or greater is required for this library to compile. Please\n make sure GMP is installed and specify its location with the option\n --with-gmp=<prefix> when running configure.\n*******************************************************************************\nError configuring givaro\n\nreal    0m22.266s\nuser    0m7.925s\nsys     0m13.148s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7025\n\n",
    "created_at": "2009-09-27T11:11:06Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "givaro 3.2.13rc2 says GMP is not installed, even though MPIR is.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7025",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @dimpase

MPIR is supposed to be a substitute for GMP. When using the Sun compiler with sage-4.1.2.alpha2, givaro-3.2.13rc2 seems to think GMP is not installed, even though the substitute mpir is installed. See below. 

It works on Solaris if gcc is used, which is a bit odd. I checked to see if the mpir had created the header files and libraries, and see that local/include/gmp.h and local/lib/libgmp.* do in fact exist, so mpir really has been installed. 



```
givaro-3.2.13rc2/src/examples/Polynomial/pol_eval.C
givaro-3.2.13rc2/src/examples/Polynomial/pol_factor.C
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
Copying updated gmp++.h
checking for a BSD-compatible install... /usr/local/bin/ginstall -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... ./install-sh -c -d
<SNIP>
checking for GMP >= 3.1.1... not found
*******************************************************************************
 ERROR: GMP not found!

 GMP version 3.1.1 or greater is required for this library to compile. Please
 make sure GMP is installed and specify its location with the option
 --with-gmp=<prefix> when running configure.
*******************************************************************************
Error configuring givaro

real    0m22.266s
user    0m7.925s
sys     0m13.148s
```


Issue created by migration from https://trac.sagemath.org/ticket/7025





---

archive/issue_comments_058065.json:
```json
{
    "body": "Changing component from build to packages: standard.",
    "created_at": "2015-09-08T12:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7025#issuecomment-58065",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from build to packages: standard.



---

archive/issue_comments_058066.json:
```json
{
    "body": "Outdated spkg or build system ticket, should be closed",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7025#issuecomment-58066",
    "user": "https://github.com/mkoeppe"
}
```

Outdated spkg or build system ticket, should be closed



---

archive/issue_comments_058067.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7025#issuecomment-58067",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058068.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-22T07:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7025#issuecomment-58068",
    "user": "https://github.com/slel"
}
```

Resolution: invalid
