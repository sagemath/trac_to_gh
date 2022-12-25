# Issue 8285: Update R's spkg-install to work on Solaris

archive/issues_008285.json:
```json
{
    "body": "Assignee: drkirkby\n\n## Build environment\n* Sage 4.3.3.alpha0, which includes R 2.10.1\n* Sun Blade 1000 with two 900 MHz UltraSPARC III+ CPUs, 2 GB RAM. (This is the same sort of processor as 't2', but is a much older machine, though still quicker than t2 for building Sage!)\n* Solaris 10 03/2005 (The first release of Solaris 10). \n* gcc 4.4.3 (The latest as I write). \n\n## The problem\nSomeone updated R in Sage, without testing on Solaris. The update caused several problems on Solaris - the most obvious one being R now needs iconv, which Sage does not currently include. \n\nHowever, despite a new standard package for iconv #8191, R would still not build on Solaris, but failed with:\n  {{{\nUndefined                       first referenced\n symbol                             in file\nuiter_setUTF8                       libR.a(util.o)\nucol_strcollIter                    libR.a(util.o)\nld: fatal: Symbol referencing errors. No output written to R.bin\ncollect2: ld returned 1 exit status \n  }}}\n\n## The Solution\nSeveral changes were made to R's spkg-install file, to fix not only the fact R would not build at all, but also some other enhancements. The updated package can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/Solaris-fixes/r-2.10.1.p0/\n\n* Adds the undocumented option \n  {{{\n  --without-ICU\n  }}}\n  as that allows R to build without the ICU library from http://site.icu-project.org/ The option was suggested to me in a private email after a post to r-help <at> r-project.org. The build now shows: \n  {{{\nMaking Sage/Python scripts relocatable...\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nMaking script relocatable\nFinished installing rpy2-2.0.8.spkg\nFinished installing rpy2-2.0.8.spkg\n\nreal    25m49.233s\nuser    22m33.551s\nsys     3m1.363s\nSuccessfully installed r-2.10.1.p0\n }}}\n* Ensures SAGE64 will attempt a 64-bit build on any platform, not just OS X. (I've not actually built R 64-bit.) \n* Removed all references to the option \n  {{{\n--with-iconv=no \n   }}} \n  as R **must** have iconv now - it is no longer optional. #8191 is an iconv library. \n* Better detection for X support on Solaris. (The previous test would always indicate R could not be built with X support, despite the fact it could be). R's configure script should work this out itself, but some comments in spkg-install suggest this was not working right on a OSX Intel 10.5.1. **The changes I made will only impact Solaris**. \n* Added some hopefully helpful comments in spkg-install, as I believe there are still multiple issues in that file - see  #8274\n\n\n## How to test\nThis should have no impact on any platform other than Solaris, though of course it is useful to test on multiple platforms to be 100% sure.\n\nTo test on Solaris 10, one needs access to a SPARC box. Some notes about how to test on 't2' are given at \n\nhttp://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2\n\nFirst one needs to add a new standard package for iconv - #8191. \n\n* Get the spkg from http://boxen.math.washington.edu/home/kirkby/new-packages/iconv/iconv-1.13.1.spkg and place it in $SAGE_ROOT/spkg/standard\n* Copy http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8191/deps to $SAGE_ROOT/spkg/standard/deps\n* Copy http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8191/install to $SAGE_ROOT/spkg/install (This must be made executable - it will probably lose the execute permission when downloading)\n\nOnce that is all down, typing 'make' should allow R to build, and you should get: \n   {{{\nSuccessfully installed r-2.10.1.p0\n   }}}\n\n\n \n\nIssue created by migration from https://trac.sagemath.org/ticket/8285\n\n",
    "created_at": "2010-02-16T20:49:13Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Update R's spkg-install to work on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8285",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

## Build environment
* Sage 4.3.3.alpha0, which includes R 2.10.1
* Sun Blade 1000 with two 900 MHz UltraSPARC III+ CPUs, 2 GB RAM. (This is the same sort of processor as 't2', but is a much older machine, though still quicker than t2 for building Sage!)
* Solaris 10 03/2005 (The first release of Solaris 10). 
* gcc 4.4.3 (The latest as I write). 

## The problem
Someone updated R in Sage, without testing on Solaris. The update caused several problems on Solaris - the most obvious one being R now needs iconv, which Sage does not currently include. 

However, despite a new standard package for iconv #8191, R would still not build on Solaris, but failed with:
  {{{
Undefined                       first referenced
 symbol                             in file
uiter_setUTF8                       libR.a(util.o)
ucol_strcollIter                    libR.a(util.o)
ld: fatal: Symbol referencing errors. No output written to R.bin
collect2: ld returned 1 exit status 
  }}}

## The Solution
Several changes were made to R's spkg-install file, to fix not only the fact R would not build at all, but also some other enhancements. The updated package can be found at 

http://boxen.math.washington.edu/home/kirkby/Solaris-fixes/r-2.10.1.p0/

* Adds the undocumented option 
  {{{
  --without-ICU
  }}}
  as that allows R to build without the ICU library from http://site.icu-project.org/ The option was suggested to me in a private email after a post to r-help <at> r-project.org. The build now shows: 
  {{{
Making Sage/Python scripts relocatable...
Making Sage/Python scripts relocatable...
Making script relocatable
Making script relocatable
Finished installing rpy2-2.0.8.spkg
Finished installing rpy2-2.0.8.spkg

real    25m49.233s
user    22m33.551s
sys     3m1.363s
Successfully installed r-2.10.1.p0
 }}}
* Ensures SAGE64 will attempt a 64-bit build on any platform, not just OS X. (I've not actually built R 64-bit.) 
* Removed all references to the option 
  {{{
--with-iconv=no 
   }}} 
  as R **must** have iconv now - it is no longer optional. #8191 is an iconv library. 
* Better detection for X support on Solaris. (The previous test would always indicate R could not be built with X support, despite the fact it could be). R's configure script should work this out itself, but some comments in spkg-install suggest this was not working right on a OSX Intel 10.5.1. **The changes I made will only impact Solaris**. 
* Added some hopefully helpful comments in spkg-install, as I believe there are still multiple issues in that file - see  #8274


## How to test
This should have no impact on any platform other than Solaris, though of course it is useful to test on multiple platforms to be 100% sure.

To test on Solaris 10, one needs access to a SPARC box. Some notes about how to test on 't2' are given at 

http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

First one needs to add a new standard package for iconv - #8191. 

* Get the spkg from http://boxen.math.washington.edu/home/kirkby/new-packages/iconv/iconv-1.13.1.spkg and place it in $SAGE_ROOT/spkg/standard
* Copy http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8191/deps to $SAGE_ROOT/spkg/standard/deps
* Copy http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8191/install to $SAGE_ROOT/spkg/install (This must be made executable - it will probably lose the execute permission when downloading)

Once that is all down, typing 'make' should allow R to build, and you should get: 
   {{{
Successfully installed r-2.10.1.p0
   }}}


 

Issue created by migration from https://trac.sagemath.org/ticket/8285





---

archive/issue_comments_073243.json:
```json
{
    "body": "Attachment [Solaris-fixes-for-R.patch](tarball://root/attachments/some-uuid/ticket8285/Solaris-fixes-for-R.patch) by drkirkby created at 2010-02-17 00:24:23\n\nMercurial patch",
    "created_at": "2010-02-17T00:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8285#issuecomment-73243",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [Solaris-fixes-for-R.patch](tarball://root/attachments/some-uuid/ticket8285/Solaris-fixes-for-R.patch) by drkirkby created at 2010-02-17 00:24:23

Mercurial patch



---

archive/issue_comments_073244.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-17T00:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8285#issuecomment-73244",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073245.json:
```json
{
    "body": "Once this ticket is closed, so can #8272, as this addresses that issue.",
    "created_at": "2010-02-17T00:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8285#issuecomment-73245",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Once this ticket is closed, so can #8272, as this addresses that issue.



---

archive/issue_comments_073246.json:
```json
{
    "body": "The updated R spkg builds on sage.math, bsd.math, rosemary.math, t2.math, Skynet machines (cleo and iras). However, it doesn't build on Cygwin (winxp1 on boxen.math). As of Sage 4.3.3.alpha1, the build on Cygwin fails during the compilation process of gd, which normally gets built before R. Also, I would note that #8191 is a prerequisite for this updated R spkg.",
    "created_at": "2010-02-21T21:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8285#issuecomment-73246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The updated R spkg builds on sage.math, bsd.math, rosemary.math, t2.math, Skynet machines (cleo and iras). However, it doesn't build on Cygwin (winxp1 on boxen.math). As of Sage 4.3.3.alpha1, the build on Cygwin fails during the compilation process of gd, which normally gets built before R. Also, I would note that #8191 is a prerequisite for this updated R spkg.



---

archive/issue_comments_073247.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-21T21:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8285#issuecomment-73247",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073248.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-03-01T16:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8285#issuecomment-73248",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_073249.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T23:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8285#issuecomment-73249",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_073250.json:
```json
{
    "body": "Merged [r-2.10.1.p0.spkg](http://boxen.math.washington.edu/home/kirkby/Solaris-fixes/r-2.10.1.p0/r-2.10.1.p0.spkg) in the standard spkg repository.",
    "created_at": "2010-03-02T23:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8285#issuecomment-73250",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [r-2.10.1.p0.spkg](http://boxen.math.washington.edu/home/kirkby/Solaris-fixes/r-2.10.1.p0/r-2.10.1.p0.spkg) in the standard spkg repository.
