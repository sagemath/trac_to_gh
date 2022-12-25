# Issue 6595: 'modified sage library code' fails at c_lib if /opt/SUNWspro/bin/CC can be found. (SCons issue)

archive/issues_006595.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein david.kirkby@onetel.net\n\nKeywords: scons SUNWspro SunStudio\n\nThis failure was first observed in Sage 4.1.1.alpha0.\n\nIf the Sun Studio compiler suite is installed, the C++ compiler will be at /opt/SUNWspro/bin/CC. This causes the failure below. note in particular the line, which shows the Sun C++ compiler being used. But only a line or two before, the GNU C compiler was used. Mixing object files between the two compilers is unlikely to work. \n\nIt might be worth taking note of the error though. The Sun compiler is a lot more fussy than g++, so probably picks up bad code that g++ will accept. \n\n\n```\n/opt/SUNWspro/bin/CC -o src/so_ZZ_pylong.o -c -KPIC -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/ZZ_pylong.cpp\nCC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise\n\"src/ZZ_pylong.cpp\", line 47: Error: \"ZZ_set_pylong(NTL::ZZ&, _object*)\" is expected to return a value.\n1 Error(s) detected.\n\n```\n\nHere's the fuller output. I believe this is a SCons issue again. SCons on Solaris looks for /opt/SUNWspro/bin/CC and will use that sometimes. PolyBoRi did suffer this problem, but Alexander Dreyer has sorted that out.\n\n\n```\nDeleting the scons target.\nRemoved src/so_convert.o\nRemoved src/so_interrupt.o\nRemoved src/so_mpn_pylong.o\nRemoved src/so_mpz_pylong.o\nRemoved src/so_mpz_longlong.o\nRemoved src/so_stdsage.o\nRemoved src/so_gmp_globals.o\nscons: Reading SConscript files ...\nscons: done reading SConscript files.\nscons: Cleaning targets ...\nscons: done cleaning targets.\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\ngcc -o src/so_convert.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/convert.c\ngcc -o src/so_interrupt.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/interrupt.c\ngcc -o src/so_mpn_pylong.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/mpn_pylong.c\ngcc -o src/so_mpz_pylong.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/mpz_pylong.c\ngcc -o src/so_mpz_longlong.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/mpz_longlong.c\ngcc -o src/so_stdsage.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/stdsage.c\ngcc -o src/so_gmp_globals.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/gmp_globals.c\n/opt/SUNWspro/bin/CC -o src/so_ZZ_pylong.o -c -KPIC -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/ZZ_pylong.cpp\nCC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise\n\"src/ZZ_pylong.cpp\", line 47: Error: \"ZZ_set_pylong(NTL::ZZ&, _object*)\" is expected to return a value.\n1 Error(s) detected.\nscons: *** [src/so_ZZ_pylong.o] Error 1\nERROR: There was an error building c_lib.\n\n\nreal    0m39.279s\nuser    0m33.652s\nsys     0m4.841s\nError building new version of SAGE.\nYou might try typing 'sage -ba' or write to sage-support with as much information as possible.\n\nreal    2m21.275s\nuser    2m2.010s\nsys     0m16.789s\nsage: An error occurred while installing sage-4.1.1.alpha0\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6595\n\n",
    "created_at": "2009-07-23T07:27:40Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "'modified sage library code' fails at c_lib if /opt/SUNWspro/bin/CC can be found. (SCons issue)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6595",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @williamstein david.kirkby@onetel.net

Keywords: scons SUNWspro SunStudio

This failure was first observed in Sage 4.1.1.alpha0.

If the Sun Studio compiler suite is installed, the C++ compiler will be at /opt/SUNWspro/bin/CC. This causes the failure below. note in particular the line, which shows the Sun C++ compiler being used. But only a line or two before, the GNU C compiler was used. Mixing object files between the two compilers is unlikely to work. 

It might be worth taking note of the error though. The Sun compiler is a lot more fussy than g++, so probably picks up bad code that g++ will accept. 


```
/opt/SUNWspro/bin/CC -o src/so_ZZ_pylong.o -c -KPIC -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/ZZ_pylong.cpp
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
"src/ZZ_pylong.cpp", line 47: Error: "ZZ_set_pylong(NTL::ZZ&, _object*)" is expected to return a value.
1 Error(s) detected.

```

Here's the fuller output. I believe this is a SCons issue again. SCons on Solaris looks for /opt/SUNWspro/bin/CC and will use that sometimes. PolyBoRi did suffer this problem, but Alexander Dreyer has sorted that out.


```
Deleting the scons target.
Removed src/so_convert.o
Removed src/so_interrupt.o
Removed src/so_mpn_pylong.o
Removed src/so_mpz_pylong.o
Removed src/so_mpz_longlong.o
Removed src/so_stdsage.o
Removed src/so_gmp_globals.o
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Cleaning targets ...
scons: done cleaning targets.

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
gcc -o src/so_convert.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/convert.c
gcc -o src/so_interrupt.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/interrupt.c
gcc -o src/so_mpn_pylong.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/mpn_pylong.c
gcc -o src/so_mpz_pylong.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/mpz_pylong.c
gcc -o src/so_mpz_longlong.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/mpz_longlong.c
gcc -o src/so_stdsage.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/stdsage.c
gcc -o src/so_gmp_globals.o -c -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/gmp_globals.c
/opt/SUNWspro/bin/CC -o src/so_ZZ_pylong.o -c -KPIC -fPIC -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/python2.6 -I/rootpool2/local/kirkby/sage-4.1.1.alpha0/local/include/NTL -Iinclude src/ZZ_pylong.cpp
CC: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
"src/ZZ_pylong.cpp", line 47: Error: "ZZ_set_pylong(NTL::ZZ&, _object*)" is expected to return a value.
1 Error(s) detected.
scons: *** [src/so_ZZ_pylong.o] Error 1
ERROR: There was an error building c_lib.


real    0m39.279s
user    0m33.652s
sys     0m4.841s
Error building new version of SAGE.
You might try typing 'sage -ba' or write to sage-support with as much information as possible.

real    2m21.275s
user    2m2.010s
sys     0m16.789s
sage: An error occurred while installing sage-4.1.1.alpha0
```




Issue created by migration from https://trac.sagemath.org/ticket/6595





---

archive/issue_comments_053865.json:
```json
{
    "body": "It was suggested on sage-devel that removing the SCons build process and using a makefile might be better. Is this agreed by William? If so, I'll so it. SCons seems to cause countless problems in Sage.",
    "created_at": "2009-10-19T08:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53865",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It was suggested on sage-devel that removing the SCons build process and using a makefile might be better. Is this agreed by William? If so, I'll so it. SCons seems to cause countless problems in Sage.



---

archive/issue_comments_053866.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-12-16T19:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53866",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_053867.json:
```json
{
    "body": "I'm changing this to a blocker for 4.3.1, as William is keen that Sage builds on Solaris asap, and this is the one remaining issue which prevents a clean build. It's also code written by Sage developers. \n\nI've looked at this and can't sort it out. Perhaps a fresh pair of eyes can. \n\nDave",
    "created_at": "2009-12-16T19:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53867",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm changing this to a blocker for 4.3.1, as William is keen that Sage builds on Solaris asap, and this is the one remaining issue which prevents a clean build. It's also code written by Sage developers. 

I've looked at this and can't sort it out. Perhaps a fresh pair of eyes can. 

Dave



---

archive/issue_comments_053868.json:
```json
{
    "body": "Hi Dave,\n\nThanks.  Could you tell me *exactly* how -- using hardware I have access to (either on skynet, on t2, etc.) -- I can replicate the above?   Then maybe I'll fix it!\n\nWilliam",
    "created_at": "2009-12-17T01:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53868",
    "user": "https://github.com/williamstein"
}
```

Hi Dave,

Thanks.  Could you tell me *exactly* how -- using hardware I have access to (either on skynet, on t2, etc.) -- I can replicate the above?   Then maybe I'll fix it!

William



---

archive/issue_comments_053869.json:
```json
{
    "body": "Hi William, \n\nUsing 't2' set the following environment up before starting to build sage. \n\n\n```\nkirkby@t2:[~] $ echo $SAGE_FORTRAN_LIB\n/usr/local/gcc-4.4.1-sun-linker/lib/libgfortran.so\nkirkby@t2:[~] $ echo $SAGE_FORTRAN\n/usr/local/gcc-4.4.1-sun-linker/bin/gfortran\nkirkby@t2:[~] $ echo $LD_LIBRARY_PATH\n/usr/local/gcc-4.4.1-sun-linker/lib:/usr/local/lib\nkirkby@t2:[~] $ echo $PATH\n/usr/local/gcc-4.4.1-sun-linker/bin:/usr/local/bin2:/usr/bin:/usr/ccs/bin:/usr/local/bin:/usr/sfw/bin:/bin:/usr/sbin\n```\n\n\nnote, if you try to run the Sun C or C++ compilers, you will find they do **not** work, since they are not in your path. \n\n\n```\nkirkby@t2:[~] $ cc\n-bash: cc: command not found\nkirkby@t2:[~] $ CC\n-bash: CC: command not found\n```\n\n\nThat is intensional, since for now at least, Sage will only build with gcc, so the Sun compilers are not in the path. \n\nType 'make' and you will find it fails at the point indicated, as the Sun C++ compiler (/opt/SUNWspro/bin/CC) will be used to try to compile the C++ files. This is despite your path does not include /opt/SUNWspro/bin/. The path /opt/SUNWspro/bin/ is hard-coded into SCons - it looks for the Sun tools there. Why the hell it uses the GNU C compiler, but the Sun C++ compiler is beyond me. \n\nI'm just about to go to bed, but will hang around for 20 minutes or so, therefore if you have any questions, get them to me asap. \n\nDave",
    "created_at": "2009-12-17T01:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53869",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Hi William, 

Using 't2' set the following environment up before starting to build sage. 


```
kirkby@t2:[~] $ echo $SAGE_FORTRAN_LIB
/usr/local/gcc-4.4.1-sun-linker/lib/libgfortran.so
kirkby@t2:[~] $ echo $SAGE_FORTRAN
/usr/local/gcc-4.4.1-sun-linker/bin/gfortran
kirkby@t2:[~] $ echo $LD_LIBRARY_PATH
/usr/local/gcc-4.4.1-sun-linker/lib:/usr/local/lib
kirkby@t2:[~] $ echo $PATH
/usr/local/gcc-4.4.1-sun-linker/bin:/usr/local/bin2:/usr/bin:/usr/ccs/bin:/usr/local/bin:/usr/sfw/bin:/bin:/usr/sbin
```


note, if you try to run the Sun C or C++ compilers, you will find they do **not** work, since they are not in your path. 


```
kirkby@t2:[~] $ cc
-bash: cc: command not found
kirkby@t2:[~] $ CC
-bash: CC: command not found
```


That is intensional, since for now at least, Sage will only build with gcc, so the Sun compilers are not in the path. 

Type 'make' and you will find it fails at the point indicated, as the Sun C++ compiler (/opt/SUNWspro/bin/CC) will be used to try to compile the C++ files. This is despite your path does not include /opt/SUNWspro/bin/. The path /opt/SUNWspro/bin/ is hard-coded into SCons - it looks for the Sun tools there. Why the hell it uses the GNU C compiler, but the Sun C++ compiler is beyond me. 

I'm just about to go to bed, but will hang around for 20 minutes or so, therefore if you have any questions, get them to me asap. 

Dave



---

archive/issue_comments_053870.json:
```json
{
    "body": "A few notes. \n\n* Essentially this boils down to one thing - the library code should be made to honor the settings of CC and CXX, and not pick compilers at random. Since I'd not specifically set CC or CXX, then the Sage build environment will set them to gcc and g++. (I do not know for certain if this code honors the setting of CC or not, but it certainly does not honor CXX). \n\n* By default, when Sun Studio is installed, it will create links so cc and CC are in /usr/bin, and so always in your path. So hacking SCons to remove /opt/SUNWspro/bin will not work for most installations of Sun Studio. In any case, that is not the way to right solve the problem. \n\n* There are numerous packages in Sage which do not honor the values of CC and CXX, but just use gcc and g++. That is annoying, but not a fatal flaw, as they build as long as the first gcc and g++ in your path are suitable. This is more serious. \n\n* There is a mixture of Sun (-KPIC) and GNU (-fPIC) compiler flags, but that should not be a fatal error, as unknown flags are ignored. \n\n* I get the same problem on any SPARC I've tried this on, irrespective of the version of Sun Studio - other versions are installed in other paths. \n\n\nDave",
    "created_at": "2009-12-17T02:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53870",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

A few notes. 

* Essentially this boils down to one thing - the library code should be made to honor the settings of CC and CXX, and not pick compilers at random. Since I'd not specifically set CC or CXX, then the Sage build environment will set them to gcc and g++. (I do not know for certain if this code honors the setting of CC or not, but it certainly does not honor CXX). 

* By default, when Sun Studio is installed, it will create links so cc and CC are in /usr/bin, and so always in your path. So hacking SCons to remove /opt/SUNWspro/bin will not work for most installations of Sun Studio. In any case, that is not the way to right solve the problem. 

* There are numerous packages in Sage which do not honor the values of CC and CXX, but just use gcc and g++. That is annoying, but not a fatal flaw, as they build as long as the first gcc and g++ in your path are suitable. This is more serious. 

* There is a mixture of Sun (-KPIC) and GNU (-fPIC) compiler flags, but that should not be a fatal error, as unknown flags are ignored. 

* I get the same problem on any SPARC I've tried this on, irrespective of the version of Sun Studio - other versions are installed in other paths. 


Dave



---

archive/issue_comments_053871.json:
```json
{
    "body": "Thank you!",
    "created_at": "2009-12-19T07:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53871",
    "user": "https://github.com/williamstein"
}
```

Thank you!



---

archive/issue_comments_053872.json:
```json
{
    "body": "Wow.  I fixed the first bug that the Sun compiler finds (which doesn't matter), and it next found two more similar issues -- which in fact *are* both major bugs.   See attached patch.",
    "created_at": "2009-12-23T01:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53872",
    "user": "https://github.com/williamstein"
}
```

Wow.  I fixed the first bug that the Sun compiler finds (which doesn't matter), and it next found two more similar issues -- which in fact *are* both major bugs.   See attached patch.



---

archive/issue_comments_053873.json:
```json
{
    "body": "Attachment [sagelib_6595.patch](tarball://root/attachments/some-uuid/ticket6595/sagelib_6595.patch) by @williamstein created at 2009-12-23 01:24:50\n\nThis one patch (sagelib_6595.patch) makes it so at least c_lib builds fine using CC... by fixing at least two potentially *major* bugs in c_lib.  Here's to porting/portability/multiple compilers/not ignoring warnings, etc!  And to Kirkby's persistence.",
    "created_at": "2009-12-23T01:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53873",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagelib_6595.patch](tarball://root/attachments/some-uuid/ticket6595/sagelib_6595.patch) by @williamstein created at 2009-12-23 01:24:50

This one patch (sagelib_6595.patch) makes it so at least c_lib builds fine using CC... by fixing at least two potentially *major* bugs in c_lib.  Here's to porting/portability/multiple compilers/not ignoring warnings, etc!  And to Kirkby's persistence.



---

archive/issue_comments_053874.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-23T01:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53874",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053875.json:
```json
{
    "body": "Great you have found those problems. The Sun compiler is quite fussy, which annoys some, but does show up bugs that other compilers ignore. \n\nHowever, building the Sage library with 'CC' will **not** produce a workable Sage, as the Sun and GNU C++ compilers use different name mangling. We must get this to build with g++. Hence hte library it must be made to respect CC and CXX. \n\nI've had some feedback from the SCons mailing list. It's 2:02 AM here, so I'm not going to implement any of these now, but hopefully later I'll look at resolving the issues. It would appear that SCons ignores CC and CXX, but there are things we can do. Some code snippets posted by two or three different people include the following. \n\n-----\nHi David,\n\nI believe your problem is the line:\n\n```\nenv = Environment(ENV = os.environ)\n```\n\nwhich imports wholesale everything from the shell environment. Try\nremoving this and your cxx=g++ override should work.\n-------------\nYour best technique is just to specify the GNU toolchain when setting  \nup the Environment: \n\n```\ntools=['gcc','g++','gnulink',WhateverElseYouNeed). \n```\n \n\nThat's portable across all platforms now, and will be into the future.\n\n-----------\n\nOr the toolchain you pass to the Environment when you set it up:\n\n```\n     if os.environ['CC'].contains('gcc'):\n         toolchain = ['gcc', 'g++', 'gnulink']\n     else:\n         toolchain = ['suncc', 'sunc++', 'sunlink']\n     env = Environment(tools = [toolchain, 'other', 'tools'])\n```\n\n--------",
    "created_at": "2009-12-23T02:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53875",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Great you have found those problems. The Sun compiler is quite fussy, which annoys some, but does show up bugs that other compilers ignore. 

However, building the Sage library with 'CC' will **not** produce a workable Sage, as the Sun and GNU C++ compilers use different name mangling. We must get this to build with g++. Hence hte library it must be made to respect CC and CXX. 

I've had some feedback from the SCons mailing list. It's 2:02 AM here, so I'm not going to implement any of these now, but hopefully later I'll look at resolving the issues. It would appear that SCons ignores CC and CXX, but there are things we can do. Some code snippets posted by two or three different people include the following. 

-----
Hi David,

I believe your problem is the line:

```
env = Environment(ENV = os.environ)
```

which imports wholesale everything from the shell environment. Try
removing this and your cxx=g++ override should work.
-------------
Your best technique is just to specify the GNU toolchain when setting  
up the Environment: 

```
tools=['gcc','g++','gnulink',WhateverElseYouNeed). 
```
 

That's portable across all platforms now, and will be into the future.

-----------

Or the toolchain you pass to the Environment when you set it up:

```
     if os.environ['CC'].contains('gcc'):
         toolchain = ['gcc', 'g++', 'gnulink']
     else:
         toolchain = ['suncc', 'sunc++', 'sunlink']
     env = Environment(tools = [toolchain, 'other', 'tools'])
```

--------



---

archive/issue_comments_053876.json:
```json
{
    "body": "Hi, \n\nOf course building with sun's CC didn't work.  So while you posted the above, I randomly happened to track down exactly the same email and implement it.  I use os.environ['CC'].endswith('gcc') instead of contains, because the path could be something weird like /home/fredgcc/bar/compilers/net/CC.   I'll be posted a part 2 patch in a moment, which I hope you'll referee.",
    "created_at": "2009-12-23T02:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53876",
    "user": "https://github.com/williamstein"
}
```

Hi, 

Of course building with sun's CC didn't work.  So while you posted the above, I randomly happened to track down exactly the same email and implement it.  I use os.environ['CC'].endswith('gcc') instead of contains, because the path could be something weird like /home/fredgcc/bar/compilers/net/CC.   I'll be posted a part 2 patch in a moment, which I hope you'll referee.



---

archive/issue_comments_053877.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-23T15:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53877",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053878.json:
```json
{
    "body": "Attachment [sagelib_6595-part2.patch](tarball://root/attachments/some-uuid/ticket6595/sagelib_6595-part2.patch) by drkirkby created at 2009-12-23 15:58:40\n\nMy 'sage -upgrade' seems to have hit a problem, as this library is built twice. The first time it builds fine, with no warnings g++. \n\nThe second time it has the same issues as before - same warning, from the Sun compiler 'CC'. I can only assume something is a bit messed up here. It's clearly patched ok, but I must have left-over code being built. \n\nNote however, there is no -Wall option, so we wont catch many warnings from gcc/g++. It might be worth adding that at some point in the future, given you have noticed two serious bugs in what is a relatively small amount of code. But I don't know how to enable the warnings with SCons. \n\nI looked at your changes to the C and C++ code, and they look fine. I don't fully understand what that code is supposed to do, but clearly computing an answer, then not bothering to return it was rather obviously a mistake, which should have been caught with a compiler warning. \n\nLuckily the Sun compiler was not so forgiving as g++, so allowed those errors to be found. \n\nDave",
    "created_at": "2009-12-23T15:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53878",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [sagelib_6595-part2.patch](tarball://root/attachments/some-uuid/ticket6595/sagelib_6595-part2.patch) by drkirkby created at 2009-12-23 15:58:40

My 'sage -upgrade' seems to have hit a problem, as this library is built twice. The first time it builds fine, with no warnings g++. 

The second time it has the same issues as before - same warning, from the Sun compiler 'CC'. I can only assume something is a bit messed up here. It's clearly patched ok, but I must have left-over code being built. 

Note however, there is no -Wall option, so we wont catch many warnings from gcc/g++. It might be worth adding that at some point in the future, given you have noticed two serious bugs in what is a relatively small amount of code. But I don't know how to enable the warnings with SCons. 

I looked at your changes to the C and C++ code, and they look fine. I don't fully understand what that code is supposed to do, but clearly computing an answer, then not bothering to return it was rather obviously a mistake, which should have been caught with a compiler warning. 

Luckily the Sun compiler was not so forgiving as g++, so allowed those errors to be found. 

Dave



---

archive/issue_events_006832.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-24T07:12:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6595#event-6832"
}
```



---

archive/issue_comments_053879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-24T07:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53879",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_053880.json:
```json
{
    "body": "merged into 4.3.rc2.",
    "created_at": "2009-12-24T07:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53880",
    "user": "https://github.com/williamstein"
}
```

merged into 4.3.rc2.



---

archive/issue_comments_053881.json:
```json
{
    "body": "This patch breaks building Sage on OS X.  I'm re-opening it.  This will have to go in 4.3.1 when fixed.\n\n```\nrunning build_py\nrunning build_ext\nbuilding 'sage.algebras.quatalg.quaternion_algebra_element' extension\ng++ -L/Users/wstein/build/sage-4.3.rc2/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.3-i386-2.6/sage/algebras/quatalg/quaternion_algebra_element.o -L/Users/wstein/build/sage-4.3.rc2/local//lib -lcsage -lcsage -lflint -lgmp -lgmpxx -lm -lstdc++ -lntl -lstdc++ -lntl -o build/lib.macosx-10.3-i386-2.6/sage/algebras/quatalg/quaternion_algebra_element.so\nld: in /Users/wstein/build/sage-4.3.rc2/local/lib/libcsage.dylib, can't link with a main executable\ncollect2: ld returned 1 exit status\nerror: command 'g++' failed with exit status 1\nsage: There was an error installing modified sage library code.\n\n\nreal    0m2.029s\n```\n",
    "created_at": "2009-12-24T17:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53881",
    "user": "https://github.com/williamstein"
}
```

This patch breaks building Sage on OS X.  I'm re-opening it.  This will have to go in 4.3.1 when fixed.

```
running build_py
running build_ext
building 'sage.algebras.quatalg.quaternion_algebra_element' extension
g++ -L/Users/wstein/build/sage-4.3.rc2/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.3-i386-2.6/sage/algebras/quatalg/quaternion_algebra_element.o -L/Users/wstein/build/sage-4.3.rc2/local//lib -lcsage -lcsage -lflint -lgmp -lgmpxx -lm -lstdc++ -lntl -lstdc++ -lntl -o build/lib.macosx-10.3-i386-2.6/sage/algebras/quatalg/quaternion_algebra_element.so
ld: in /Users/wstein/build/sage-4.3.rc2/local/lib/libcsage.dylib, can't link with a main executable
collect2: ld returned 1 exit status
error: command 'g++' failed with exit status 1
sage: There was an error installing modified sage library code.


real    0m2.029s
```




---

archive/issue_comments_053882.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2009-12-24T17:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53882",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_006833.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-24T17:36:50Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6595#event-6833"
}
```



---

archive/issue_comments_053883.json:
```json
{
    "body": "> This patch breaks building Sage on OS X.\n\nIt breaks on OS X <= 10.5, not on 10.6.   Also, the problem is only the part2 patch.  The first patch with the genuine bug fixes is fine.",
    "created_at": "2009-12-24T17:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53883",
    "user": "https://github.com/williamstein"
}
```

> This patch breaks building Sage on OS X.

It breaks on OS X <= 10.5, not on 10.6.   Also, the problem is only the part2 patch.  The first patch with the genuine bug fixes is fine.



---

archive/issue_comments_053884.json:
```json
{
    "body": "That's very annoying, but one of those things I guess. Perhaps this bit of code needs to be Solaris-specific. Back to the drawing board.",
    "created_at": "2009-12-24T18:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53884",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That's very annoying, but one of those things I guess. Perhaps this bit of code needs to be Solaris-specific. Back to the drawing board.



---

archive/issue_comments_053885.json:
```json
{
    "body": "> That's very annoying, but one of those things I guess.\n> Perhaps this bit of code needs to be Solaris-specific. \n\nThat's an excellent idea and would be easy to do.  Basically we just change\n\n```\nif os.environ['CC'].endswith('gcc'): \n```\n\nto\n\n```\nif os.uname()[0] == 'SunOS' and os.environ['CC'].endswith('gcc'): \n```\n\nand we're good to go.",
    "created_at": "2009-12-24T20:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53885",
    "user": "https://github.com/williamstein"
}
```

> That's very annoying, but one of those things I guess.
> Perhaps this bit of code needs to be Solaris-specific. 

That's an excellent idea and would be easy to do.  Basically we just change

```
if os.environ['CC'].endswith('gcc'): 
```

to

```
if os.uname()[0] == 'SunOS' and os.environ['CC'].endswith('gcc'): 
```

and we're good to go.



---

archive/issue_comments_053886.json:
```json
{
    "body": "Does that mean it gets to 4.3 then, or do we still have to wait for 4.3.1? \n\nI'm happy to give your fix a positive review if you want to change it from 'needs work' to 'needs review'. That fix can only affect Solaris. \n\n\nDave",
    "created_at": "2009-12-24T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53886",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Does that mean it gets to 4.3 then, or do we still have to wait for 4.3.1? 

I'm happy to give your fix a positive review if you want to change it from 'needs work' to 'needs review'. That fix can only affect Solaris. 


Dave



---

archive/issue_comments_053887.json:
```json
{
    "body": "I've created a revised version of William's patch, which will force gcc and g++ on AIX, HP-UX, IRIX, Solaris and Tru64 if the environment variable CXX ends in g++. (I chose CXX rather than CC, as testing for a compiler ending in 'cc' would match gcc as well as 'cc'. Although no such test is actually performed, potentially one might want to check on compilers ending in 'cc'). \n\nThe patch should also handle the cases of where the Sun Studio compiler is used on Linux or Solaris. \n\nI'll post it once it has been better tested. \n\nIt might be useful to force a compile of c_lib with the Sun C compiler, and see if it finds any defects like the Sun C++ compiler did. The revised patch will allow that. \n\nDave",
    "created_at": "2009-12-26T16:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53887",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've created a revised version of William's patch, which will force gcc and g++ on AIX, HP-UX, IRIX, Solaris and Tru64 if the environment variable CXX ends in g++. (I chose CXX rather than CC, as testing for a compiler ending in 'cc' would match gcc as well as 'cc'. Although no such test is actually performed, potentially one might want to check on compilers ending in 'cc'). 

The patch should also handle the cases of where the Sun Studio compiler is used on Linux or Solaris. 

I'll post it once it has been better tested. 

It might be useful to force a compile of c_lib with the Sun C compiler, and see if it finds any defects like the Sun C++ compiler did. The revised patch will allow that. 

Dave



---

archive/issue_comments_053888.json:
```json
{
    "body": "Attaching patch, which should resolve all issues and hopefully not break anywhere. The issue with OS X is apparently one of whether the SHELL is defined or not.",
    "created_at": "2009-12-31T02:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53888",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attaching patch, which should resolve all issues and hopefully not break anywhere. The issue with OS X is apparently one of whether the SHELL is defined or not.



---

archive/issue_comments_053889.json:
```json
{
    "body": "Attachment [6595-SConstruct.patch](tarball://root/attachments/some-uuid/ticket6595/6595-SConstruct.patch) by drkirkby created at 2009-12-31 02:58:16\n\nRevised version of SConstruct for c_lib",
    "created_at": "2009-12-31T02:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53889",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [6595-SConstruct.patch](tarball://root/attachments/some-uuid/ticket6595/6595-SConstruct.patch) by drkirkby created at 2009-12-31 02:58:16

Revised version of SConstruct for c_lib



---

archive/issue_comments_053890.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-31T02:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53890",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053891.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-31T19:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53891",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006834.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-03T21:56:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6595#event-6834"
}
```



---

archive/issue_comments_053892.json:
```json
{
    "body": "Merged 6595-SConstruct.patch",
    "created_at": "2010-01-03T21:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6595#issuecomment-53892",
    "user": "https://github.com/mwhansen"
}
```

Merged 6595-SConstruct.patch
