# Issue 7440: optional valgrind-3.3.1 spkg doesn't build with newer GCC's

archive/issues_007440.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein david.kirkby@onetel.net\n\nI tried to build the valgrind_3.3.1 spkg on ubuntu-9.10 and it quickly fails with \n\n```\nconfigure: error: Valgrind requires glibc version 2.2 - 2.7\nerror configuring valgrind 3.3.1\n\nreal    0m10.843s\nuser    0m2.928s\nsys     0m6.640s\nsage: An error occurred while installing valgrind_3.3.1\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7440\n\n",
    "closed_at": "2010-08-28T12:10:25Z",
    "created_at": "2009-11-12T05:40:01Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "optional valgrind-3.3.1 spkg doesn't build with newer GCC's",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7440",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @williamstein david.kirkby@onetel.net

I tried to build the valgrind_3.3.1 spkg on ubuntu-9.10 and it quickly fails with 

```
configure: error: Valgrind requires glibc version 2.2 - 2.7
error configuring valgrind 3.3.1

real    0m10.843s
user    0m2.928s
sys     0m6.640s
sage: An error occurred while installing valgrind_3.3.1
```

Issue created by migration from https://trac.sagemath.org/ticket/7440





---

archive/issue_comments_062499.json:
```json
{
    "body": "I sent this email to sage-devel:\n\n```\nHello,\n\nThe valgrind-3.3.1 spkg no longer works with newer Linux installs.\nE.g., with Ubuntu-9.10 we get the error:\n\n    configure: error: Valgrind requires glibc version 2.2 - 2.7\n    error configuring valgrind 3.3.1\n\nSee: http://trac.sagemath.org/sage_trac/ticket/7440\n\nUnfortunately, Michael Abshoff is the official maintainer of this\nspkg.  Can somebody else please volunteer to be the Valgrind spkg\nmaintainer?  If nobody does, then I'll remove valgrind as an optional\nspkg (I'll put it in experimental), at least until I have more time\nand maintain it myself.\n\n -- William\n```",
    "created_at": "2009-11-12T05:44:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62499",
    "user": "https://github.com/williamstein"
}
```

I sent this email to sage-devel:

```
Hello,

The valgrind-3.3.1 spkg no longer works with newer Linux installs.
E.g., with Ubuntu-9.10 we get the error:

    configure: error: Valgrind requires glibc version 2.2 - 2.7
    error configuring valgrind 3.3.1

See: http://trac.sagemath.org/sage_trac/ticket/7440

Unfortunately, Michael Abshoff is the official maintainer of this
spkg.  Can somebody else please volunteer to be the Valgrind spkg
maintainer?  If nobody does, then I'll remove valgrind as an optional
spkg (I'll put it in experimental), at least until I have more time
and maintain it myself.

 -- William
```



---

archive/issue_comments_062500.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-21T04:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62500",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062501.json:
```json
{
    "body": "A new package with the latest version of valgrind is here: http://sage.math.washington.edu/home/timdumol/valgrind-3.5.0.p0.spkg.",
    "created_at": "2009-12-21T04:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62501",
    "user": "https://github.com/TimDumol"
}
```

A new package with the latest version of valgrind is here: http://sage.math.washington.edu/home/timdumol/valgrind-3.5.0.p0.spkg.



---

archive/issue_comments_062502.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-22T05:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62502",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062503.json:
```json
{
    "body": "I tried installing this on Mac OS X 10.6 and got an error during the \"configure\" process:\n\n```\nchecking build system type... i686-apple-darwin10.2.0\nchecking host system type... i686-apple-darwin10.2.0\nchecking for a supported CPU... ok (i686)\nchecking for a 64-bit only build... no\nchecking for a 32-bit only build... no\nchecking for a supported OS... ok (darwin10.2.0)\nchecking for the kernel version... unsupported (10.2.0)\nconfigure: error: Valgrind works on Darwin 9.x (Mac OS X 10.5)\nerror configuring valgrind 3.5.0\n```\nSeems to build correctly on sage.math, for what that's worth.\n\nOnce the OS X issue is worked out, other people should definitely look at this; I don't think I'm qualified to review it properly.",
    "created_at": "2009-12-22T05:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62503",
    "user": "https://github.com/jhpalmieri"
}
```

I tried installing this on Mac OS X 10.6 and got an error during the "configure" process:

```
checking build system type... i686-apple-darwin10.2.0
checking host system type... i686-apple-darwin10.2.0
checking for a supported CPU... ok (i686)
checking for a 64-bit only build... no
checking for a 32-bit only build... no
checking for a supported OS... ok (darwin10.2.0)
checking for the kernel version... unsupported (10.2.0)
configure: error: Valgrind works on Darwin 9.x (Mac OS X 10.5)
error configuring valgrind 3.5.0
```
Seems to build correctly on sage.math, for what that's worth.

Once the OS X issue is worked out, other people should definitely look at this; I don't think I'm qualified to review it properly.



---

archive/issue_comments_062504.json:
```json
{
    "body": "Despite the message \"Valgrind works on Darwin 9.x\", that Valgrind spkg has never built on OS X.  Valgrind was Linux only.   I recently heard that it was ported to OS X, but I'm not sure if that is really the case.   Mabshoff used to tell me that it would be ported any day now...",
    "created_at": "2009-12-22T17:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62504",
    "user": "https://github.com/williamstein"
}
```

Despite the message "Valgrind works on Darwin 9.x", that Valgrind spkg has never built on OS X.  Valgrind was Linux only.   I recently heard that it was ported to OS X, but I'm not sure if that is really the case.   Mabshoff used to tell me that it would be ported any day now...



---

archive/issue_comments_062505.json:
```json
{
    "body": "I believe OS X 10.6 is Darwin 10.x, which Valgrind indeed does not support. I have uploaded a new version of the package which checks for the release version here: http://sage.math.washington.edu/home/timdumol/valgrind-3.5.0.p0.spkg.",
    "created_at": "2009-12-23T03:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62505",
    "user": "https://github.com/TimDumol"
}
```

I believe OS X 10.6 is Darwin 10.x, which Valgrind indeed does not support. I have uploaded a new version of the package which checks for the release version here: http://sage.math.washington.edu/home/timdumol/valgrind-3.5.0.p0.spkg.



---

archive/issue_comments_062506.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-23T03:39:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62506",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062507.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-24T00:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62507",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062508.json:
```json
{
    "body": "This has a portability bug. 'uname' will will called with the '-p' option on any non-Linux system. But '-p' is not a POSIX option for uname. \n\nhttp://www.opengroup.org/onlinepubs/9699919799/utilities/uname.html\n\nso there is no reason any system should support the -p option. If you need to test the processor type, make sure the test is only done on platforms where you know the -p option is supported. HP-UX is one platform where this will fail, and I expect there are others too. \n\n```\n$ uname -a\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n$ uname -p\nuname: illegal option -- p\nusage: uname [-amnrsvil] [-S nodename]\n```\n\nDave",
    "created_at": "2009-12-24T00:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62508",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This has a portability bug. 'uname' will will called with the '-p' option on any non-Linux system. But '-p' is not a POSIX option for uname. 

http://www.opengroup.org/onlinepubs/9699919799/utilities/uname.html

so there is no reason any system should support the -p option. If you need to test the processor type, make sure the test is only done on platforms where you know the -p option is supported. HP-UX is one platform where this will fail, and I expect there are others too. 

```
$ uname -a
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
$ uname -p
uname: illegal option -- p
usage: uname [-amnrsvil] [-S nodename]
```

Dave



---

archive/issue_comments_062509.json:
```json
{
    "body": "FYI: Valgrind doesn't make any sense on any platforms that don't support 'uname -p'.  The only supported platforms for the latest Valgrind are:  X86/Linux, AMD64/Linux, PPC32/Linux, PPC64/Linux, and X86/Darwin (Mac OS X).  These all support uname -p.",
    "created_at": "2009-12-24T20:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62509",
    "user": "https://github.com/williamstein"
}
```

FYI: Valgrind doesn't make any sense on any platforms that don't support 'uname -p'.  The only supported platforms for the latest Valgrind are:  X86/Linux, AMD64/Linux, PPC32/Linux, PPC64/Linux, and X86/Darwin (Mac OS X).  These all support uname -p.



---

archive/issue_comments_062510.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-25T04:03:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62510",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062511.json:
```json
{
    "body": "Replying to [comment:7 drkirkby]:\n> This has a portability bug. 'uname' will will called with the '-p' option on any non-Linux system. But '-p' is not a POSIX option for uname. \n\n\nI do not believe this is a problem, since `uname -p` will only be called on Linux and Darwin platforms because of boolean logic shortcircuiting, e.g.:\n\n```\n[timdumol@tim-pc sage]$ if [ -z \"\" ] && [ -z \"`error`\" ]; then echo \"Success\"; fi\nbash: error: command not found\nSuccess\n[timdumol@tim-pc sage]$ if [ -n \"\" ] && [ -z \"`error`\" ]; then echo \"Success\"; fi\n```",
    "created_at": "2009-12-25T04:03:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62511",
    "user": "https://github.com/TimDumol"
}
```

Replying to [comment:7 drkirkby]:
> This has a portability bug. 'uname' will will called with the '-p' option on any non-Linux system. But '-p' is not a POSIX option for uname. 


I do not believe this is a problem, since `uname -p` will only be called on Linux and Darwin platforms because of boolean logic shortcircuiting, e.g.:

```
[timdumol@tim-pc sage]$ if [ -z "" ] && [ -z "`error`" ]; then echo "Success"; fi
bash: error: command not found
Success
[timdumol@tim-pc sage]$ if [ -n "" ] && [ -z "`error`" ]; then echo "Success"; fi
```



---

archive/issue_comments_062512.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-25T14:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62512",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062513.json:
```json
{
    "body": "First, merry Christmas to you both. \n\nWilliam asked me the other day to check what optional packages installed on Solaris. Valgind did not install, but did give a helpful error message, indicating why. That's much better than executing a command which will fail. So I believe the fact Valgind does not work on Solaris, AIX, HP-UX etc is a not an excuse for sloppy programming - there is enough of that in Sage anyway!\n\nWilliam's use of:\n\n```\nelif [ `uname` = \"SunOS\" -a \"`uname -p`\" != \"sparc\" ]; then\n```\n\nin an early version of 'prereq' did cause an issue on HP-UX, with the -p option creating problems - see #7156. \n\nTim's version is written slighlty different, using the preffered '&&' instead of '-a'. The use of '-a' is deprecated and discouraged by POSIX\n\nhttp://www.opengroup.org/onlinepubs/009695399/utilities/test.html\n\nso perhaps Tim's arugument is valid. On reflection, I agree with Tim. \n\nHowever, as my grandmother used to say, the proof of the pudding is in the eating, so I tested this on HP-UX, where sage-4.2.1 is installed. \n\n```\nvalgrind-3.5.0.p0/patches/sage.supp\nFinished extraction\n****************************************************\nHost system\nuname -a:\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: hppa1.1-hp-hpux11.11\nConfigured with: /tmp/gcc-4.3.3.tar.gz/gcc-4.3.3/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.3.3 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11\nThread model: posix\ngcc version 4.3.3 (GCC)\n****************************************************\nSorry, Valgrind only works on X86/Linux, AMD64/Linux,\nPPC32/Linux, PPC64/Linux and X86/Darwin 9.x\n(Mac OS X 10.5.x)\n\nreal    0m0.020s\nuser    0m0.020s\nsys     0m0.010s\nsage: An error occurred while installing valgrind-3.5.0.p0\n```\n\nSo I would have to agree, the spkg-install **does** work properly, even on HP-UX. The error message is helpful too. The spkg-install does not fail as I initially expected it would, so I'm changing this to positive review. \n\nDave",
    "created_at": "2009-12-25T14:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62513",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

First, merry Christmas to you both. 

William asked me the other day to check what optional packages installed on Solaris. Valgind did not install, but did give a helpful error message, indicating why. That's much better than executing a command which will fail. So I believe the fact Valgind does not work on Solaris, AIX, HP-UX etc is a not an excuse for sloppy programming - there is enough of that in Sage anyway!

William's use of:

```
elif [ `uname` = "SunOS" -a "`uname -p`" != "sparc" ]; then
```

in an early version of 'prereq' did cause an issue on HP-UX, with the -p option creating problems - see #7156. 

Tim's version is written slighlty different, using the preffered '&&' instead of '-a'. The use of '-a' is deprecated and discouraged by POSIX

http://www.opengroup.org/onlinepubs/009695399/utilities/test.html

so perhaps Tim's arugument is valid. On reflection, I agree with Tim. 

However, as my grandmother used to say, the proof of the pudding is in the eating, so I tested this on HP-UX, where sage-4.2.1 is installed. 

```
valgrind-3.5.0.p0/patches/sage.supp
Finished extraction
****************************************************
Host system
uname -a:
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.3.3.tar.gz/gcc-4.3.3/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.3.3 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.3.3 (GCC)
****************************************************
Sorry, Valgrind only works on X86/Linux, AMD64/Linux,
PPC32/Linux, PPC64/Linux and X86/Darwin 9.x
(Mac OS X 10.5.x)

real    0m0.020s
user    0m0.020s
sys     0m0.010s
sage: An error occurred while installing valgrind-3.5.0.p0
```

So I would have to agree, the spkg-install **does** work properly, even on HP-UX. The error message is helpful too. The spkg-install does not fail as I initially expected it would, so I'm changing this to positive review. 

Dave



---

archive/issue_comments_062514.json:
```json
{
    "body": "BTW, I just noticed that Michael Abshoff is the noted as the package maintainer in SPKG.txt. #7738 says he should be removed from all packages, and specificially lists Valgrind. Hence I believe this would be a good oppotunity to remove Michael's name. Does time want to take on the role? \n\nAs such, I'm swapping this back to 'needs work'. It would seem silly to update a package, without addressing this minor issue. Otherwise, I'm happy with this, so will change it back to positive when its done. \n\nDave",
    "created_at": "2009-12-25T15:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62514",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

BTW, I just noticed that Michael Abshoff is the noted as the package maintainer in SPKG.txt. #7738 says he should be removed from all packages, and specificially lists Valgrind. Hence I believe this would be a good oppotunity to remove Michael's name. Does time want to take on the role? 

As such, I'm swapping this back to 'needs work'. It would seem silly to update a package, without addressing this minor issue. Otherwise, I'm happy with this, so will change it back to positive when its done. 

Dave



---

archive/issue_comments_062515.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-25T15:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62515",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_062516.json:
```json
{
    "body": "That was supposed to be 'does **Tim** want to take on the role?', not 'time' as I said.",
    "created_at": "2009-12-25T15:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62516",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That was supposed to be 'does **Tim** want to take on the role?', not 'time' as I said.



---

archive/issue_comments_062517.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-28T18:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62517",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062518.json:
```json
{
    "body": "Replying to [comment:13 drkirkby]:\n> BTW, I just noticed that Michael Abshoff is the noted as the package maintainer in SPKG.txt. #7738 says he should be removed from all packages, and specificially lists Valgrind. Hence I believe this would be a good oppotunity to remove Michael's name. Does time want to take on the role? \n> \n> As such, I'm swapping this back to 'needs work'. It would seem silly to update a package, without addressing this minor issue. Otherwise, I'm happy with this, so will change it back to positive when its done. \n> \n> Dave \n\n\nSure, I'll be glad to. New version of spkg up at http://sage.math.washington.edu/home/timdumol/valgrind-3.5.0.p0.spkg",
    "created_at": "2009-12-28T18:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62518",
    "user": "https://github.com/TimDumol"
}
```

Replying to [comment:13 drkirkby]:
> BTW, I just noticed that Michael Abshoff is the noted as the package maintainer in SPKG.txt. #7738 says he should be removed from all packages, and specificially lists Valgrind. Hence I believe this would be a good oppotunity to remove Michael's name. Does time want to take on the role? 
> 
> As such, I'm swapping this back to 'needs work'. It would seem silly to update a package, without addressing this minor issue. Otherwise, I'm happy with this, so will change it back to positive when its done. 
> 
> Dave 


Sure, I'll be glad to. New version of spkg up at http://sage.math.washington.edu/home/timdumol/valgrind-3.5.0.p0.spkg



---

archive/issue_comments_062519.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-28T19:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62519",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062520.json:
```json
{
    "body": "Due to the problems with Sage (disk related I believe), I unable to download this. But since the only issue was changing someone name in a text file, I'm sure there will be no problem, so I'm changing it to positive review.",
    "created_at": "2009-12-28T19:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62520",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Due to the problems with Sage (disk related I believe), I unable to download this. But since the only issue was changing someone name in a text file, I'm sure there will be no problem, so I'm changing it to positive review.



---

archive/issue_events_017640.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-19T01:34:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7440#event-17640"
}
```



---

archive/issue_comments_062521.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T01:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62521",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_062522.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-08-28T12:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62522",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_017641.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/maldun",
    "created_at": "2010-08-28T12:03:25Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7440#event-17641"
}
```



---

archive/issue_comments_062523.json:
```json
{
    "body": "Now this package has a problem with the new glibc version as well.\n\nI get: \n\n```\nchecking for a supported CPU/OS combination... ok (amd64-linux)\nchecking for use as an inner Valgrind... no\nchecking for egrep... grep -E\nchecking the GLIBC_VERSION version... unsupported version\nconfigure: error: Valgrind requires glibc version 2.2 - 2.10\nerror configuring valgrind 3.5.0\n```\n\nI use Ubuntu 10.04, and the glibc version is 2.11 ....\nValgrind 3.6.0 is already out",
    "created_at": "2010-08-28T12:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62523",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Now this package has a problem with the new glibc version as well.

I get: 

```
checking for a supported CPU/OS combination... ok (amd64-linux)
checking for use as an inner Valgrind... no
checking for egrep... grep -E
checking the GLIBC_VERSION version... unsupported version
configure: error: Valgrind requires glibc version 2.2 - 2.10
error configuring valgrind 3.5.0
```

I use Ubuntu 10.04, and the glibc version is 2.11 ....
Valgrind 3.6.0 is already out



---

archive/issue_events_017642.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/maldun",
    "created_at": "2010-08-28T12:10:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7440#event-17642"
}
```



---

archive/issue_comments_062524.json:
```json
{
    "body": "Sorry I oversaw ticket #7766: http://trac.sagemath.org/sage_trac/ticket/7766",
    "created_at": "2010-08-28T12:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62524",
    "user": "https://trac.sagemath.org/admin/accounts/users/maldun"
}
```

Sorry I oversaw ticket #7766: http://trac.sagemath.org/sage_trac/ticket/7766



---

archive/issue_comments_062525.json:
```json
{
    "body": "Replying to [comment:18 maldun]:\n> Now this package has a problem with the new glibc version as well.\n\n\nAs a general rule, don't reopen a ticket once it is closed. Open a new ticket instead.",
    "created_at": "2010-08-28T18:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7440",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7440#issuecomment-62525",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:18 maldun]:
> Now this package has a problem with the new glibc version as well.


As a general rule, don't reopen a ticket once it is closed. Open a new ticket instead.
