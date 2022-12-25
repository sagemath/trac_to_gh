# Issue 7851: libz igoresSAGE64 other than on OS X

archive/issues_007851.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies\n\nThe spkg-install of libz zlib-1.2.3.p5 has this:\n\n\n```\nif [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n   CFLAGS=\" -m64 $CFLAGS -fPIC -g -I\\\"$SAGE_LOCAL/include\\\"\"\n   cp ../patches/configure-OSX-64 configure\nelse\n   CFLAGS=\"$CFLAGS -fPIC -g -I\\\"$SAGE_LOCAL/include\\\"\"\nfi\nexport CFLAGS\n```\n\n\nso is almost doomed to a 64-bit build unless one sets CFLAGS externally. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7851\n\n",
    "created_at": "2010-01-05T19:04:56Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "libz igoresSAGE64 other than on OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7851",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies

The spkg-install of libz zlib-1.2.3.p5 has this:


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   CFLAGS=" -m64 $CFLAGS -fPIC -g -I\"$SAGE_LOCAL/include\""
   cp ../patches/configure-OSX-64 configure
else
   CFLAGS="$CFLAGS -fPIC -g -I\"$SAGE_LOCAL/include\""
fi
export CFLAGS
```


so is almost doomed to a 64-bit build unless one sets CFLAGS externally. 

Issue created by migration from https://trac.sagemath.org/ticket/7851





---

archive/issue_comments_067887.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T05:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67887",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067888.json:
```json
{
    "body": "Attachment [add-64-bit-support-to-zlib.patch](tarball://root/attachments/some-uuid/ticket7851/add-64-bit-support-to-zlib.patch) by drkirkby created at 2010-01-12 05:53:23\n\nWith the recent updates to sage-env, this will actually build in 64-bit mode, as that will set CFLAGS appropriately. But there were some other issues with this package, so the following have been addressed. \n\n* Move -I $SAGE_LOCAL/include to CPPFLAGS, not CFLAGS\n  There's no reason it should go there. \n* Removed most of the SAGE64 related stuff. The only bit \n  remaining is to apply a patch on OS X in 64-bit mode. \n* Removed -Wall and -g from CFLAGS - the new sage-eve \n  will add these automatically for gcc. Since they are \n  GNU specific flags, they would break with other compilers. \n* Substituted -fPIC for $FPIC_FLAG as -fPIC is a GNU specfic \n  option and sage-env defines FPIC_FLAG to be -fPIC for \n  gcc, but other things for Sun Studio and other compilers from\n  HP and IBM. \n\nAn updated spkg can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/zlib-1.2.3.p6/zlib-1.2.3.p6.spkg\n\nother relevant files in http://boxen.math.washington.edu/home/kirkby/portability/zlib-1.2.3.p6/\n\nDave",
    "created_at": "2010-01-12T05:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67888",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [add-64-bit-support-to-zlib.patch](tarball://root/attachments/some-uuid/ticket7851/add-64-bit-support-to-zlib.patch) by drkirkby created at 2010-01-12 05:53:23

With the recent updates to sage-env, this will actually build in 64-bit mode, as that will set CFLAGS appropriately. But there were some other issues with this package, so the following have been addressed. 

* Move -I $SAGE_LOCAL/include to CPPFLAGS, not CFLAGS
  There's no reason it should go there. 
* Removed most of the SAGE64 related stuff. The only bit 
  remaining is to apply a patch on OS X in 64-bit mode. 
* Removed -Wall and -g from CFLAGS - the new sage-eve 
  will add these automatically for gcc. Since they are 
  GNU specific flags, they would break with other compilers. 
* Substituted -fPIC for $FPIC_FLAG as -fPIC is a GNU specfic 
  option and sage-env defines FPIC_FLAG to be -fPIC for 
  gcc, but other things for Sun Studio and other compilers from
  HP and IBM. 

An updated spkg can be found at 

http://boxen.math.washington.edu/home/kirkby/portability/zlib-1.2.3.p6/zlib-1.2.3.p6.spkg

other relevant files in http://boxen.math.washington.edu/home/kirkby/portability/zlib-1.2.3.p6/

Dave



---

archive/issue_comments_067889.json:
```json
{
    "body": "I'm not 100% happy with this. I'm returning it to 'needs work.'",
    "created_at": "2010-01-12T17:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67889",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm not 100% happy with this. I'm returning it to 'needs work.'



---

archive/issue_comments_067890.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-12T17:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67890",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067891.json:
```json
{
    "body": "This problem is not as simple as I first thought. Using the zlib source code, without any CFLAGS, but with the --shared option, we get the message the shared library is built. \n\n\n```\ndrkirkby@swan:[~/sage-4.3.1.alpha1/spkg/standard/zlib-1.2.3.p5/src] $  ./configure --shared\nChecking for shared library support...\nBuilding shared library libz.so.1.2.3 with /usr/local/gcc-4.4.1-sun-linker/bin/gcc.\nChecking for unistd.h... Yes.\nChecking whether to use vs[n]printf() or s[n]printf()... using vs[n]printf()\nChecking for vsnprintf() in stdio.h... Yes.\nChecking for return value of vsnprintf()... Yes.\nChecking for errno.h... Yes.\nChecking for mmap support... Yes.\n```\n\n\nTrying to build in 64-bit mode, the shared library is not built. \n\n\n```\ndrkirkby@swan:[~/sage-4.3.1.alpha1/spkg/standard/zlib-1.2.3.p5/src] $ CFLAGS=-m64  ./configure --shared\nChecking for shared library support...\nNo shared library support; try without defining CC and CFLAGS\nBuilding static library libz.a version 1.2.3 with /usr/local/gcc-4.4.1-sun-linker/bin/gcc.\nChecking for unistd.h... Yes.\nChecking whether to use vs[n]printf() or s[n]printf()... using vs[n]printf()\nChecking for vsnprintf() in stdio.h... Yes.\nChecking for return value of vsnprintf()... Yes.\nChecking for errno.h... Yes.\nChecking for mmap support... Yes.\n```\n\n\nI've reported this issue to the email address zlib at gzip.org and are awaiting feedback.  I don't think it will be easy to progress on this until that point. \n\nDave",
    "created_at": "2010-01-28T12:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67891",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This problem is not as simple as I first thought. Using the zlib source code, without any CFLAGS, but with the --shared option, we get the message the shared library is built. 


```
drkirkby@swan:[~/sage-4.3.1.alpha1/spkg/standard/zlib-1.2.3.p5/src] $  ./configure --shared
Checking for shared library support...
Building shared library libz.so.1.2.3 with /usr/local/gcc-4.4.1-sun-linker/bin/gcc.
Checking for unistd.h... Yes.
Checking whether to use vs[n]printf() or s[n]printf()... using vs[n]printf()
Checking for vsnprintf() in stdio.h... Yes.
Checking for return value of vsnprintf()... Yes.
Checking for errno.h... Yes.
Checking for mmap support... Yes.
```


Trying to build in 64-bit mode, the shared library is not built. 


```
drkirkby@swan:[~/sage-4.3.1.alpha1/spkg/standard/zlib-1.2.3.p5/src] $ CFLAGS=-m64  ./configure --shared
Checking for shared library support...
No shared library support; try without defining CC and CFLAGS
Building static library libz.a version 1.2.3 with /usr/local/gcc-4.4.1-sun-linker/bin/gcc.
Checking for unistd.h... Yes.
Checking whether to use vs[n]printf() or s[n]printf()... using vs[n]printf()
Checking for vsnprintf() in stdio.h... Yes.
Checking for return value of vsnprintf()... Yes.
Checking for errno.h... Yes.
Checking for mmap support... Yes.
```


I've reported this issue to the email address zlib at gzip.org and are awaiting feedback.  I don't think it will be easy to progress on this until that point. 

Dave



---

archive/issue_comments_067892.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-01-28T12:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67892",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_067893.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-02-05T20:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67893",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_067894.json:
```json
{
    "body": "I found out the problem is in src/configure. This file is very old!\nHas entries for QNX os, remember those days.\n\nThis file needs a patch!!!\n\nJaap",
    "created_at": "2010-02-05T20:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67894",
    "user": "https://github.com/jaapspies"
}
```

I found out the problem is in src/configure. This file is very old!
Has entries for QNX os, remember those days.

This file needs a patch!!!

Jaap



---

archive/issue_comments_067895.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2020-08-24T18:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67895",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_067896.json:
```json
{
    "body": "this is obsolete.",
    "created_at": "2020-08-24T18:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67896",
    "user": "https://github.com/dimpase"
}
```

this is obsolete.



---

archive/issue_comments_067897.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-10T08:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7851",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7851#issuecomment-67897",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
