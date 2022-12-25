# Issue 9665: Make lcalc accessible as a library on OS X

archive/issues_009665.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @kiwifb drkirkby georgsweber @rishikesha @robertwb @williamstein ylchapuy mrubinst@math.uwaterloo.ca @kcrisman\n\nReported by Georg Weber on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a/a19253d8c2f48d2f#a19253d8c2f48d2f):\n\n```\n...\nbuilding 'sage.libs.lcalc.lcalc_Lfunction' extension\n...\ng++ -L/Users/Shared/sage/sage-4.5.2.rc0/local/lib -bundle -undefined\ndynamic_lookup build/temp.macosx-10.4-i386-2.6/sage/libs/lcalc/\nlcalc_Lfunction.o -L/Users/Shared/sage/sage-4.5.2.rc0/local//lib -\nlcsage -lm -lntl -lmpfr -lgmp -lgmpxx -lLfunction -lstdc++ -lstdc++ -\nlntl -o build/lib.macosx-10.4-i386-2.6/sage/libs/lcalc/\nlcalc_Lfunction.so\ngcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-\nprototypes -I/Users/Shared/sage/sage-4.5.2.rc0/local//include -I/Users/\nShared/sage/sage-4.5.2.rc0/local//include/csage -I/Users/Shared/sage/\nsage-4.5.2.rc0/devel//sage/sage/ext -I/Users/Shared/sage/\nsage-4.5.2.rc0/local/include/python2.6 -c sage/libs/pari/gen.c -o\nbuild/temp.macosx-10.4-i386-2.6/sage/libs/pari/gen.o -w\n/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: can't locate file for: -\nlLfunction\ncollect2: ld returned 1 exit status\nerror: command 'g++' failed with exit status 1\nsage: There was an error installing modified sage library code.\n...\n\nIt seems that in the Sage library code, the usage of some \"Lfunction\"\nlibrary from the lcalc package was newly introduced. On my Mac, both\nthe (half-built) Sage-4.5.2 and the older (fuly working) Sage-4.5.1\nhave under local/lib/ some library \"libLfunction.so\". But on a Mac\nunder OS X (OS X 10.4 at least), this would need to be\n\"libLfunction.dylib\" to be usable ... \n```\n\n\n[Georg continues](http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a/99b55c2958a197cb#99b55c2958a197cb):\n\n```\nfor the \"Lfunction\" issue, the relevant tickets are #5396 resp. #4793.\nIt seems to be as I thought --- the lcalc spkg (#4793) never built a\ncorrect dynamic (\".dylib\") library on OS X. But this was not relevant\nor did break anything, until the interface between Sage and lcalc was\nchanged from using pexpect to using this library directly (#5396,\nintroduced in Sage-4.5.2.alpha1). \n```\n\n\nRelated: #4793, #5396.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9665\n\n",
    "created_at": "2010-08-01T21:18:40Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Make lcalc accessible as a library on OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9665",
    "user": "https://github.com/qed777"
}
```
Assignee: tbd

CC:  @kiwifb drkirkby georgsweber @rishikesha @robertwb @williamstein ylchapuy mrubinst@math.uwaterloo.ca @kcrisman

Reported by Georg Weber on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a/a19253d8c2f48d2f#a19253d8c2f48d2f):

```
...
building 'sage.libs.lcalc.lcalc_Lfunction' extension
...
g++ -L/Users/Shared/sage/sage-4.5.2.rc0/local/lib -bundle -undefined
dynamic_lookup build/temp.macosx-10.4-i386-2.6/sage/libs/lcalc/
lcalc_Lfunction.o -L/Users/Shared/sage/sage-4.5.2.rc0/local//lib -
lcsage -lm -lntl -lmpfr -lgmp -lgmpxx -lLfunction -lstdc++ -lstdc++ -
lntl -o build/lib.macosx-10.4-i386-2.6/sage/libs/lcalc/
lcalc_Lfunction.so
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-
prototypes -I/Users/Shared/sage/sage-4.5.2.rc0/local//include -I/Users/
Shared/sage/sage-4.5.2.rc0/local//include/csage -I/Users/Shared/sage/
sage-4.5.2.rc0/devel//sage/sage/ext -I/Users/Shared/sage/
sage-4.5.2.rc0/local/include/python2.6 -c sage/libs/pari/gen.c -o
build/temp.macosx-10.4-i386-2.6/sage/libs/pari/gen.o -w
/usr/libexec/gcc/i686-apple-darwin8/4.0.1/ld: can't locate file for: -
lLfunction
collect2: ld returned 1 exit status
error: command 'g++' failed with exit status 1
sage: There was an error installing modified sage library code.
...

It seems that in the Sage library code, the usage of some "Lfunction"
library from the lcalc package was newly introduced. On my Mac, both
the (half-built) Sage-4.5.2 and the older (fuly working) Sage-4.5.1
have under local/lib/ some library "libLfunction.so". But on a Mac
under OS X (OS X 10.4 at least), this would need to be
"libLfunction.dylib" to be usable ... 
```


[Georg continues](http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a/99b55c2958a197cb#99b55c2958a197cb):

```
for the "Lfunction" issue, the relevant tickets are #5396 resp. #4793.
It seems to be as I thought --- the lcalc spkg (#4793) never built a
correct dynamic (".dylib") library on OS X. But this was not relevant
or did break anything, until the interface between Sage and lcalc was
changed from using pexpect to using this library directly (#5396,
introduced in Sage-4.5.2.alpha1). 
```


Related: #4793, #5396.

Issue created by migration from https://trac.sagemath.org/ticket/9665





---

archive/issue_comments_093670.json:
```json
{
    "body": "Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math.  In particular,\n\n```sh\n$ uname -a\nDarwin bsd.local 10.4.0 Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386 i386\n$ pwd\n/Users/mpatel/apps/sage-4.5.2.rc0\n$ find . | grep libLfunction\n./local/lib/libLfunction.so\n$ touch devel/sage-main/sage/libs/lcalc/lcalc_Lfunction.pyx\n$ ./sage -b\n...\ngcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/mpatel/apps/sage-4.5.2.rc0/local/include/lcalc/ -I/Users/mpatel/apps/sage-4.5.2.rc0/local//include -I/Users/mpatel/apps/sage-4.5.2.rc0/local//include/csage -I/Users/mpatel/apps/sage-4.5.2.rc0/devel//sage/sage/ext -I/Users/mpatel/apps/sage-4.5.2.rc0/local/include/python2.6 -c sage/libs/lcalc/lcalc_Lfunction.cpp -o build/temp.macosx-10.6-i386-2.6/sage/libs/lcalc/lcalc_Lfunction.o -O3 -ffast-math -w\n...\ng++ -L/Users/mpatel/apps/sage-4.5.2.rc0/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.6-i386-2.6/sage/libs/lcalc/lcalc_Lfunction.o -L/Users/mpatel/apps/sage-4.5.2.rc0/local//lib -lcsage -lm -lntl -lmpfr -lgmp -lgmpxx -lLfunction -lstdc++ -lstdc++ -lntl -o build/lib.macosx-10.6-i386-2.6/sage/libs/lcalc/lcalc_Lfunction.so\n...\n```\n\nfinishes with several warnings but no errors.  Does bsd.math not require a .dylib library?\n\nDisclaimer:  I'm not familiar with OS X.",
    "created_at": "2010-08-01T21:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93670",
    "user": "https://github.com/qed777"
}
```

Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math.  In particular,

```sh
$ uname -a
Darwin bsd.local 10.4.0 Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386 i386
$ pwd
/Users/mpatel/apps/sage-4.5.2.rc0
$ find . | grep libLfunction
./local/lib/libLfunction.so
$ touch devel/sage-main/sage/libs/lcalc/lcalc_Lfunction.pyx
$ ./sage -b
...
gcc -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/mpatel/apps/sage-4.5.2.rc0/local/include/lcalc/ -I/Users/mpatel/apps/sage-4.5.2.rc0/local//include -I/Users/mpatel/apps/sage-4.5.2.rc0/local//include/csage -I/Users/mpatel/apps/sage-4.5.2.rc0/devel//sage/sage/ext -I/Users/mpatel/apps/sage-4.5.2.rc0/local/include/python2.6 -c sage/libs/lcalc/lcalc_Lfunction.cpp -o build/temp.macosx-10.6-i386-2.6/sage/libs/lcalc/lcalc_Lfunction.o -O3 -ffast-math -w
...
g++ -L/Users/mpatel/apps/sage-4.5.2.rc0/local/lib -bundle -undefined dynamic_lookup build/temp.macosx-10.6-i386-2.6/sage/libs/lcalc/lcalc_Lfunction.o -L/Users/mpatel/apps/sage-4.5.2.rc0/local//lib -lcsage -lm -lntl -lmpfr -lgmp -lgmpxx -lLfunction -lstdc++ -lstdc++ -lntl -o build/lib.macosx-10.6-i386-2.6/sage/libs/lcalc/lcalc_Lfunction.so
...
```

finishes with several warnings but no errors.  Does bsd.math not require a .dylib library?

Disclaimer:  I'm not familiar with OS X.



---

archive/issue_comments_093671.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math. Does bsd.math not require a .dylib library?\n> \n> Disclaimer:  I'm not familiar with OS X.\n\nThe \"bsd.math\" Mac runs with OS X 10.6 using Apples version of GCC 4.2, and obviously this one knows how to handle \".so\" dynamic libraries in addition to \".dylib\" ones. I suspected so earlier, but since I work almost exclusively with OS X 10.4 (and thus Apples version of GCC 4.0.1), I couldn't tell, or know, for sure. So OS X 10.6 is \"out of the game\" for the time being.\n\nBut how about OS X 10.5 (I think it also still uses GCC 4.0.1)?\nAny results on this platform anybody?",
    "created_at": "2010-08-02T11:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93671",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Replying to [comment:1 mpatel]:
> Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math. Does bsd.math not require a .dylib library?
> 
> Disclaimer:  I'm not familiar with OS X.

The "bsd.math" Mac runs with OS X 10.6 using Apples version of GCC 4.2, and obviously this one knows how to handle ".so" dynamic libraries in addition to ".dylib" ones. I suspected so earlier, but since I work almost exclusively with OS X 10.4 (and thus Apples version of GCC 4.0.1), I couldn't tell, or know, for sure. So OS X 10.6 is "out of the game" for the time being.

But how about OS X 10.5 (I think it also still uses GCC 4.0.1)?
Any results on this platform anybody?



---

archive/issue_comments_093672.json:
```json
{
    "body": "Last time I built on 10.5, it worked fine. I do not have access to 10.4 intel machine. I am building it again, but I do not think anything should change since last time.\n\nReplying to [comment:3 GeorgSWeber]:\n> Replying to [comment:1 mpatel]:\n> > Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math. Does bsd.math not require a .dylib library?\n> > \n> > Disclaimer:  I'm not familiar with OS X.\n> \n> The \"bsd.math\" Mac runs with OS X 10.6 using Apples version of GCC 4.2, and obviously this one knows how to handle \".so\" dynamic libraries in addition to \".dylib\" ones. I suspected so earlier, but since I work almost exclusively with OS X 10.4 (and thus Apples version of GCC 4.0.1), I couldn't tell, or know, for sure. So OS X 10.6 is \"out of the game\" for the time being.\n> \n> But how about OS X 10.5 (I think it also still uses GCC 4.0.1)?\n> Any results on this platform anybody?",
    "created_at": "2010-08-02T15:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93672",
    "user": "https://github.com/rishikesha"
}
```

Last time I built on 10.5, it worked fine. I do not have access to 10.4 intel machine. I am building it again, but I do not think anything should change since last time.

Replying to [comment:3 GeorgSWeber]:
> Replying to [comment:1 mpatel]:
> > Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math. Does bsd.math not require a .dylib library?
> > 
> > Disclaimer:  I'm not familiar with OS X.
> 
> The "bsd.math" Mac runs with OS X 10.6 using Apples version of GCC 4.2, and obviously this one knows how to handle ".so" dynamic libraries in addition to ".dylib" ones. I suspected so earlier, but since I work almost exclusively with OS X 10.4 (and thus Apples version of GCC 4.0.1), I couldn't tell, or know, for sure. So OS X 10.6 is "out of the game" for the time being.
> 
> But how about OS X 10.5 (I think it also still uses GCC 4.0.1)?
> Any results on this platform anybody?



---

archive/issue_comments_093673.json:
```json
{
    "body": "It works fine on 10.5 on intel mac. I could not replicate the problem. I am also building on a ppc machine. This should take a long time.",
    "created_at": "2010-08-02T16:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93673",
    "user": "https://github.com/rishikesha"
}
```

It works fine on 10.5 on intel mac. I could not replicate the problem. I am also building on a ppc machine. This should take a long time.



---

archive/issue_comments_093674.json:
```json
{
    "body": "It sounds from gsw that the issue is Tiger, not PPC versus Intel (he has Intel for Tiger).  Does anyone know of an spkg that builds .so files versus .dylib files for these situations? Then one could copy that naively and a non-expert (say, me) with access to Tiger could try it out.\n\nOtherwise, [this](http://osdir.com/ml/bug-libtool-gnu/2010-02/msg00003.html) link seems relevant, though I can't gauge its usefulness for sure.",
    "created_at": "2010-08-02T16:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93674",
    "user": "https://github.com/kcrisman"
}
```

It sounds from gsw that the issue is Tiger, not PPC versus Intel (he has Intel for Tiger).  Does anyone know of an spkg that builds .so files versus .dylib files for these situations? Then one could copy that naively and a non-expert (say, me) with access to Tiger could try it out.

Otherwise, [this](http://osdir.com/ml/bug-libtool-gnu/2010-02/msg00003.html) link seems relevant, though I can't gauge its usefulness for sure.



---

archive/issue_comments_093675.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-02T19:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93675",
    "user": "https://github.com/rishikesha"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093676.json:
```json
{
    "body": "New spkg should work. It is only needed to compile on 10.4. If you are using a compiled version from 10.5 to run on 10.4 then this spkg update is not needed. \n\nhttp://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p1.spkg",
    "created_at": "2010-08-02T19:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93676",
    "user": "https://github.com/rishikesha"
}
```

New spkg should work. It is only needed to compile on 10.4. If you are using a compiled version from 10.5 to run on 10.4 then this spkg update is not needed. 

http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p1.spkg



---

archive/issue_comments_093677.json:
```json
{
    "body": "In the meantime, I had a look on the \"p0\" spkg build system (makefile and such). All seems fine, except that \".so\" is hardcoded as suffix. Usually, one has something like $(SO_SUFFIX), and this defaults to so on Linux, dylib on Mac OS X, and dll under Windows. No surprise that in the spkg-install, it is said that this lcalc spkg does not work under Cygwin ...\n\nBut otherwise, OS X is taken care for in the build system, e.g. using \"dynamiclib\" as an option instead of \"shared\". So I duplicated under /local/lib/ the file \"libLfunction.so\" to another file \"libLfunction.dylib\" and, oh wonder, everything works fine. Sage builds, and the doctest for \"devel/sage/sage/libs/lcalc/lcalc_Lfunction.pyx\" passes.\n\nNow I just downloaded the \"p1\" lcalc spkg and check it out. Thanks for the quick work!",
    "created_at": "2010-08-02T19:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93677",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

In the meantime, I had a look on the "p0" spkg build system (makefile and such). All seems fine, except that ".so" is hardcoded as suffix. Usually, one has something like $(SO_SUFFIX), and this defaults to so on Linux, dylib on Mac OS X, and dll under Windows. No surprise that in the spkg-install, it is said that this lcalc spkg does not work under Cygwin ...

But otherwise, OS X is taken care for in the build system, e.g. using "dynamiclib" as an option instead of "shared". So I duplicated under /local/lib/ the file "libLfunction.so" to another file "libLfunction.dylib" and, oh wonder, everything works fine. Sage builds, and the doctest for "devel/sage/sage/libs/lcalc/lcalc_Lfunction.pyx" passes.

Now I just downloaded the "p1" lcalc spkg and check it out. Thanks for the quick work!



---

archive/issue_comments_093678.json:
```json
{
    "body": "Replying to [comment:9 GeorgSWeber]:\n> In the meantime, I had a look on the \"p0\" spkg build system (makefile and such). All seems fine, except that \".so\" is hardcoded as suffix. Usually, one has something like $(SO_SUFFIX), and this defaults to so on Linux, dylib on Mac OS X, and dll under Windows. No surprise that in the spkg-install, it is said that this lcalc spkg does not work under Cygwin ...\n> \n\nDoes that mean the 'correct' fix is to do this instead, since we eventually want to get Cygwin or whatever to work?  Presumably drkirkby has a comment about this as well :)",
    "created_at": "2010-08-02T19:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93678",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:9 GeorgSWeber]:
> In the meantime, I had a look on the "p0" spkg build system (makefile and such). All seems fine, except that ".so" is hardcoded as suffix. Usually, one has something like $(SO_SUFFIX), and this defaults to so on Linux, dylib on Mac OS X, and dll under Windows. No surprise that in the spkg-install, it is said that this lcalc spkg does not work under Cygwin ...
> 

Does that mean the 'correct' fix is to do this instead, since we eventually want to get Cygwin or whatever to work?  Presumably drkirkby has a comment about this as well :)



---

archive/issue_comments_093679.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> Replying to [comment:9 GeorgSWeber]:\n> > In the meantime, I had a look on the \"p0\" spkg build system (makefile and such). All seems fine, except that \".so\" is hardcoded as suffix. Usually, one has something like $(SO_SUFFIX), and this defaults to so on Linux, dylib on Mac OS X, and dll under Windows. No surprise that in the spkg-install, it is said that this lcalc spkg does not work under Cygwin ...\n> > \n> \n> Does that mean the 'correct' fix is to do this instead, since we eventually want to get Cygwin or whatever to work?  Presumably drkirkby has a comment about this as well :)\n\n*This* ticket is about OS X 10.4, and although the difference between p0 and p1 is a quick and dirty hack --- it's exactly the one I myself had in mind ...\n\nLet's open up a new ticket for the Cygwin issues (resp. there probably is already one), and close this one. Because I'm giving it a positive review (I just tested it OK).",
    "created_at": "2010-08-02T20:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93679",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Replying to [comment:10 kcrisman]:
> Replying to [comment:9 GeorgSWeber]:
> > In the meantime, I had a look on the "p0" spkg build system (makefile and such). All seems fine, except that ".so" is hardcoded as suffix. Usually, one has something like $(SO_SUFFIX), and this defaults to so on Linux, dylib on Mac OS X, and dll under Windows. No surprise that in the spkg-install, it is said that this lcalc spkg does not work under Cygwin ...
> > 
> 
> Does that mean the 'correct' fix is to do this instead, since we eventually want to get Cygwin or whatever to work?  Presumably drkirkby has a comment about this as well :)

*This* ticket is about OS X 10.4, and although the difference between p0 and p1 is a quick and dirty hack --- it's exactly the one I myself had in mind ...

Let's open up a new ticket for the Cygwin issues (resp. there probably is already one), and close this one. Because I'm giving it a positive review (I just tested it OK).



---

archive/issue_comments_093680.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-02T20:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93680",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093681.json:
```json
{
    "body": "Replying to [comment:3 GeorgSWeber]:\n> Replying to [comment:1 mpatel]:\n> > Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math. Does bsd.math not require a .dylib library?\n> > \n> > Disclaimer:  I'm not familiar with OS X.\n> \n> The \"bsd.math\" Mac runs with OS X 10.6 using Apples version of GCC 4.2, and obviously this one knows how to handle \".so\" dynamic libraries in addition to \".dylib\" ones.\n\nThanks to Georg and [Karl-Dieter](http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a/570c8fc35ac1014d#570c8fc35ac1014d) for their clarifications!",
    "created_at": "2010-08-02T23:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93681",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:3 GeorgSWeber]:
> Replying to [comment:1 mpatel]:
> > Sage 4.5.2.rc0 happens to build successfully and pass the long doctests on bsd.math. Does bsd.math not require a .dylib library?
> > 
> > Disclaimer:  I'm not familiar with OS X.
> 
> The "bsd.math" Mac runs with OS X 10.6 using Apples version of GCC 4.2, and obviously this one knows how to handle ".so" dynamic libraries in addition to ".dylib" ones.

Thanks to Georg and [Karl-Dieter](http://groups.google.com/group/sage-release/browse_thread/thread/fa2facb36603675a/570c8fc35ac1014d#570c8fc35ac1014d) for their clarifications!



---

archive/issue_comments_093682.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-04T02:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93682",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_093683.json:
```json
{
    "body": "Just to confirm, this worked fine on my PPC OS X 10.4 Mac as well, so it works on Intel and PPC (as it should, having read the hack).  Huzzah!",
    "created_at": "2010-08-04T03:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93683",
    "user": "https://github.com/kcrisman"
}
```

Just to confirm, this worked fine on my PPC OS X 10.4 Mac as well, so it works on Intel and PPC (as it should, having read the hack).  Huzzah!



---

archive/issue_comments_093684.json:
```json
{
    "body": ">Hi Dave,\n>\n>the makefile needed some sanity put back into it, especially linker wise. so that was a job that >was needed. I guess my main concern here is:\n>\n>*lcalc depends on mpfr when it shouldn't.\n\nlcalc as included does not need mpfr. Mike has experimental code which uses mpfr.\n\n>\n>The rest is just my ramblings about there being an unused variable in spkg-install - which may >lead people to think it is.\n\nFeel free to clean and put up an spkg for review.\n\n>\n>Francois",
    "created_at": "2010-08-06T19:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93684",
    "user": "https://github.com/rishikesha"
}
```

>Hi Dave,
>
>the makefile needed some sanity put back into it, especially linker wise. so that was a job that >was needed. I guess my main concern here is:
>
>*lcalc depends on mpfr when it shouldn't.

lcalc as included does not need mpfr. Mike has experimental code which uses mpfr.

>
>The rest is just my ramblings about there being an unused variable in spkg-install - which may >lead people to think it is.

Feel free to clean and put up an spkg for review.

>
>Francois



---

archive/issue_comments_093685.json:
```json
{
    "body": "Replying to [comment:16 rishi]:\n> >Hi Dave,\n> >\n> >the makefile needed some sanity put back into it, especially linker wise. so that was a job that >was needed. I guess my main concern here is:\n> >\n> >*lcalc depends on mpfr when it shouldn't.\n> \n> lcalc as included does not need mpfr. Mike has experimental code which uses mpfr.\n> \n> >\n> >The rest is just my ramblings about there being an unused variable in spkg-install - which may >lead people to think it is.\n> \n> Feel free to clean and put up an spkg for review.\n> \n\nThis should probably be on a different ticket, though.",
    "created_at": "2010-08-06T20:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93685",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:16 rishi]:
> >Hi Dave,
> >
> >the makefile needed some sanity put back into it, especially linker wise. so that was a job that >was needed. I guess my main concern here is:
> >
> >*lcalc depends on mpfr when it shouldn't.
> 
> lcalc as included does not need mpfr. Mike has experimental code which uses mpfr.
> 
> >
> >The rest is just my ramblings about there being an unused variable in spkg-install - which may >lead people to think it is.
> 
> Feel free to clean and put up an spkg for review.
> 

This should probably be on a different ticket, though.



---

archive/issue_comments_093686.json:
```json
{
    "body": "OK since I am redirected here.\nYes the lcalc spkg cleaning should happen in another ticket.\nBut does the lcalc wrapper in sage really need mpfr if lcalc\ndoesn't? From the new module_list.py:\n\n```\n    Extension('sage.libs.lcalc.lcalc_Lfunction',\n              sources = ['sage/libs/lcalc/lcalc_Lfunction.pyx'],\n              libraries = ['m', 'ntl', 'mpfr', 'gmp', 'gmpxx',\n                           'Lfunction', 'stdc++'],\n              include_dirs = [SAGE_ROOT + \"/local/include/lcalc/\"],\n              extra_compile_args=[\"-O3\", \"-ffast-math\"],\n              language = 'c++'),\n```\n\nAs a matter of fact I don't think it depends on gmp and gmpxx either.\nThose are added when you use mpfr.\nActually at the moment Lfunction.so is never ever linked against mpfr, gmp,\ngmpxx and pari. Only the lcalc executable is. The same could be said for ntl,\nwhich isn't a dependency of lcalc at all.\nSo unless the wrapper itself needs any of these I suggest they should go.\n\nFrancois",
    "created_at": "2010-08-06T22:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93686",
    "user": "https://github.com/kiwifb"
}
```

OK since I am redirected here.
Yes the lcalc spkg cleaning should happen in another ticket.
But does the lcalc wrapper in sage really need mpfr if lcalc
doesn't? From the new module_list.py:

```
    Extension('sage.libs.lcalc.lcalc_Lfunction',
              sources = ['sage/libs/lcalc/lcalc_Lfunction.pyx'],
              libraries = ['m', 'ntl', 'mpfr', 'gmp', 'gmpxx',
                           'Lfunction', 'stdc++'],
              include_dirs = [SAGE_ROOT + "/local/include/lcalc/"],
              extra_compile_args=["-O3", "-ffast-math"],
              language = 'c++'),
```

As a matter of fact I don't think it depends on gmp and gmpxx either.
Those are added when you use mpfr.
Actually at the moment Lfunction.so is never ever linked against mpfr, gmp,
gmpxx and pari. Only the lcalc executable is. The same could be said for ntl,
which isn't a dependency of lcalc at all.
So unless the wrapper itself needs any of these I suggest they should go.

Francois



---

archive/issue_comments_093687.json:
```json
{
    "body": "Yes it needs them. If you do not agree, try to remove and compile and see the error message, or better yet, see the code for the pyx file. It has been quite a long time since I wrote the wrapper. I never used NTL, but the wrapper does not compile without without those flags.",
    "created_at": "2010-08-06T22:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93687",
    "user": "https://github.com/rishikesha"
}
```

Yes it needs them. If you do not agree, try to remove and compile and see the error message, or better yet, see the code for the pyx file. It has been quite a long time since I wrote the wrapper. I never used NTL, but the wrapper does not compile without without those flags.



---

archive/issue_comments_093688.json:
```json
{
    "body": "In case anyone is already working on the lcalc spkg (`spkg-install` changes, dependencies, etc.) for a different ticket:  Ticket #9592 updates the lcalc package so that it's compatible with #9343's PARI upgrade.",
    "created_at": "2010-08-13T21:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9665#issuecomment-93688",
    "user": "https://github.com/qed777"
}
```

In case anyone is already working on the lcalc spkg (`spkg-install` changes, dependencies, etc.) for a different ticket:  Ticket #9592 updates the lcalc package so that it's compatible with #9343's PARI upgrade.
