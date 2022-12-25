# Issue 8039: [with spkg, needs review] ATLAS libs fail to build on Open Solaris 64 bit due to wrong LDFLAG -melf_x86_64

archive/issues_008039.json:
```json
{
    "body": "Assignee: drkirkby\n\nKeywords: building\n\nin src/CONFIG/src/SpewMakeInc.c LDFLAGS are set for inclusion in Make.inc. This file is included in all Makefiles.\n\nAs a workaround I changed -melf_x86_64 in -64 in Make.inc in the directory where the libraries are built.\n\nThis is SunOS with SAGE64=\"yes\" only.\n\nAn spkg can be found here:\n[http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p11.spkg](http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p11.spkg)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8039\n\n",
    "created_at": "2010-01-22T13:11:49Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "[with spkg, needs review] ATLAS libs fail to build on Open Solaris 64 bit due to wrong LDFLAG -melf_x86_64",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8039",
    "user": "https://github.com/jaapspies"
}
```
Assignee: drkirkby

Keywords: building

in src/CONFIG/src/SpewMakeInc.c LDFLAGS are set for inclusion in Make.inc. This file is included in all Makefiles.

As a workaround I changed -melf_x86_64 in -64 in Make.inc in the directory where the libraries are built.

This is SunOS with SAGE64="yes" only.

An spkg can be found here:
[http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p11.spkg](http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p11.spkg)

Issue created by migration from https://trac.sagemath.org/ticket/8039





---

archive/issue_comments_070121.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-22T15:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70121",
    "user": "https://github.com/jaapspies"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070122.json:
```json
{
    "body": "What has been changed? I can't find the changed file? You should not change the ATLAS source code, but create a patch, which gets applied with spkg-install.",
    "created_at": "2010-01-26T12:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70122",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

What has been changed? I can't find the changed file? You should not change the ATLAS source code, but create a patch, which gets applied with spkg-install.



---

archive/issue_comments_070123.json:
```json
{
    "body": "PS, you should also report this failure upstream.",
    "created_at": "2010-01-26T12:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70123",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

PS, you should also report this failure upstream.



---

archive/issue_comments_070124.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n> What has been changed? I can't find the changed file? You should not change the ATLAS source code, but create a patch, which gets applied with spkg-install. \n> \n\n\nSee the patch.\n\nJaap",
    "created_at": "2010-01-26T18:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70124",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:2 drkirkby]:
> What has been changed? I can't find the changed file? You should not change the ATLAS source code, but create a patch, which gets applied with spkg-install. 
> 


See the patch.

Jaap



---

archive/issue_comments_070125.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-27T02:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70125",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070126.json:
```json
{
    "body": "This will not work for me, as I believe there is a syntax error in your script.  This might be an example of things that work on one shell do not on another.\n\n```\nATLAS-build/lib/Makefile will be changed.\n'-shared' will be changed to '-G'\n'-soname' will be changed to '-h'\n'--whole-archive' will be changed to '-zallextract'\n'--no-whole-archive' will be changed to '-zdefaultextract'\nA copy of the original Makefile will be copied to Makefile.orig\n./spkg-install-script: line 94: [: yes: unary operator expected\nmake[2]: Entering directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build/lib'\nrm -f libatlas.so liblapack.so\n```\n\nThis is line 94 of the script, which is causing the problem. \n\n```\n  if [ $SAGE64 =\"yes\" ]; then \n```\n\nI believe there should be a space after the '=' sign. \n\nI'd make a couple of other points tests in general, I've gleaned from studying the shell more, and from things from comp.unix.shell. \n\n* It is better to test for \"x$SAGE64\" = xyes, as some shells have problems if SAGE64 is not defined. Adding an 'x' or anything else you fancy, will avoid that possibility, though 'x' is commonly used, so I would stick to a lower case x. That problem is not true of modern versions of bash, but its a good habit to get into, as then your scripts will work on any shell. \n* It is desirable to quote \"x$SAGE64\" as potentially SAGE64 might be set to something with spaces in it. I know in this case, there unlikely to be spaces, but you don't know if someone has set it correctly or not. \n\nHence the following is the safest test sort of test, and does not contain any unnecessary quotes. Quoting xNO will not hurt, but it is unnecessary as you know xNO will have no spaces, but you don't know that about FOOBAR.\n\n``` \n             if [ \"x$FOOBAR\" = xNO ]; then\n```\n\nI leave you to convert it to what is needed here. Otherwise I become an author and can't review it!\n\nI would also \n* Report this upstream, and add to the trac ticket the URL of the ticket. Currently it is set to N/A which is clearly not true. \n* Stick a note in the spkg-install saying why the change is made. i.e. the original flag is not valid. -64 is needed to build 64-bit, or something like that. \n* I would echo a quick statement like I did before when changing flags, like I did before. \n\n``` \n'-shared' will be changed to '-G'\n```\n\n* You are using a temporary variable of 'makefile' while editing 'Make.inc' I think that is unwise, and I know I was guilty of it above, but 'makefile' has some significance, and you could overwrite such a file if it existed. \n\nBetter would be \n\n```\nsed 's/-melf_x86_64/-64/g' Make.inc > Make.inc.tmp\n```\n\nor perhaps uses Make.inc.$$, which will create a file with the PID appended. \n\nAlso, the description is inaccurate, as it says \"As a workaround I changed -melf_x86_64 in -64 in Make.inc\". I think you mean you changed it *'too* -64. \n\nSo with \n\n* The syntax error removed\n* Description updated. \n* Some other minor changes you might want to consider\n* Reported upstream, the URL posted. \n* Change to \"reported upstream\" from N/A \n* Revised patch attached. \n\nthen I think this should be ok. But now, there is a syntax error so it will not build at all for me. \n\nDave",
    "created_at": "2010-01-27T02:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70126",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This will not work for me, as I believe there is a syntax error in your script.  This might be an example of things that work on one shell do not on another.

```
ATLAS-build/lib/Makefile will be changed.
'-shared' will be changed to '-G'
'-soname' will be changed to '-h'
'--whole-archive' will be changed to '-zallextract'
'--no-whole-archive' will be changed to '-zdefaultextract'
A copy of the original Makefile will be copied to Makefile.orig
./spkg-install-script: line 94: [: yes: unary operator expected
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build/lib'
rm -f libatlas.so liblapack.so
```

This is line 94 of the script, which is causing the problem. 

```
  if [ $SAGE64 ="yes" ]; then 
```

I believe there should be a space after the '=' sign. 

I'd make a couple of other points tests in general, I've gleaned from studying the shell more, and from things from comp.unix.shell. 

* It is better to test for "x$SAGE64" = xyes, as some shells have problems if SAGE64 is not defined. Adding an 'x' or anything else you fancy, will avoid that possibility, though 'x' is commonly used, so I would stick to a lower case x. That problem is not true of modern versions of bash, but its a good habit to get into, as then your scripts will work on any shell. 
* It is desirable to quote "x$SAGE64" as potentially SAGE64 might be set to something with spaces in it. I know in this case, there unlikely to be spaces, but you don't know if someone has set it correctly or not. 

Hence the following is the safest test sort of test, and does not contain any unnecessary quotes. Quoting xNO will not hurt, but it is unnecessary as you know xNO will have no spaces, but you don't know that about FOOBAR.

``` 
             if [ "x$FOOBAR" = xNO ]; then
```

I leave you to convert it to what is needed here. Otherwise I become an author and can't review it!

I would also 
* Report this upstream, and add to the trac ticket the URL of the ticket. Currently it is set to N/A which is clearly not true. 
* Stick a note in the spkg-install saying why the change is made. i.e. the original flag is not valid. -64 is needed to build 64-bit, or something like that. 
* I would echo a quick statement like I did before when changing flags, like I did before. 

``` 
'-shared' will be changed to '-G'
```

* You are using a temporary variable of 'makefile' while editing 'Make.inc' I think that is unwise, and I know I was guilty of it above, but 'makefile' has some significance, and you could overwrite such a file if it existed. 

Better would be 

```
sed 's/-melf_x86_64/-64/g' Make.inc > Make.inc.tmp
```

or perhaps uses Make.inc.$$, which will create a file with the PID appended. 

Also, the description is inaccurate, as it says "As a workaround I changed -melf_x86_64 in -64 in Make.inc". I think you mean you changed it *'too* -64. 

So with 

* The syntax error removed
* Description updated. 
* Some other minor changes you might want to consider
* Reported upstream, the URL posted. 
* Change to "reported upstream" from N/A 
* Revised patch attached. 

then I think this should be ok. But now, there is a syntax error so it will not build at all for me. 

Dave



---

archive/issue_comments_070127.json:
```json
{
    "body": "Attachment [atlas-3.8.3.p11.patch](tarball://root/attachments/some-uuid/ticket8039/atlas-3.8.3.p11.patch) by @jaapspies created at 2010-01-27 15:02:55\n\nMostly done as you wrote above.\n\nReported upstream:\n[https://sourceforge.net/tracker/?func=detail&aid=2941029&group_id=23725&atid=379483](https://sourceforge.net/tracker/?func=detail&aid=2941029&group_id=23725&atid=379483)\n\nJaap",
    "created_at": "2010-01-27T15:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70127",
    "user": "https://github.com/jaapspies"
}
```

Attachment [atlas-3.8.3.p11.patch](tarball://root/attachments/some-uuid/ticket8039/atlas-3.8.3.p11.patch) by @jaapspies created at 2010-01-27 15:02:55

Mostly done as you wrote above.

Reported upstream:
[https://sourceforge.net/tracker/?func=detail&aid=2941029&group_id=23725&atid=379483](https://sourceforge.net/tracker/?func=detail&aid=2941029&group_id=23725&atid=379483)

Jaap



---

archive/issue_comments_070128.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-27T15:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70128",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070129.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-28T14:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70129",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070130.json:
```json
{
    "body": "I'm a bit worried about this one:\n\n```\nPlatform detected to be 32 bits\n```\n\nDave",
    "created_at": "2010-01-28T14:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70130",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm a bit worried about this one:

```
Platform detected to be 32 bits
```

Dave



---

archive/issue_comments_070131.json:
```json
{
    "body": "It also fails on my machine\n\n```\nmake[1]: *** [atlas_run] Error 7\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'\nmake: *** [IRun_comp] Error 2\nAssertion failed: !system(ln), file /export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build/../src//CONFIG/src/config.c, line 125\n\nOS configured as SunOS (2)\n\nAssembly configured as GAS_x8632 (1)\n\nVector ISA Extension configured as  SSE3 (2,28)\n\nArchitecture configured as  Corei7 (16)\n\nClock rate configured as 3325Mhz\nCannot detect CPU throttling.\n/bin/sh: line 1: 22300: Abort(coredump)\nxconfig exited with 6\nmake -f Make.top build\nmake[1]: Entering directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'\nmake[1]: Make.top: No such file or directory\nmake[1]: *** No rule to make target `Make.top'.  Stop.\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'\nmake: *** [build] Error 2\nFailed to build ATLAS.\nFailed to build ATLAS.\n\nreal\t0m3.065s\nuser\t0m1.150s\nsys\t0m1.074s\nsage: An error occurred while installing atlas-3.8.3.p11\n```",
    "created_at": "2010-01-28T14:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70131",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It also fails on my machine

```
make[1]: *** [atlas_run] Error 7
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'
make: *** [IRun_comp] Error 2
Assertion failed: !system(ln), file /export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build/../src//CONFIG/src/config.c, line 125

OS configured as SunOS (2)

Assembly configured as GAS_x8632 (1)

Vector ISA Extension configured as  SSE3 (2,28)

Architecture configured as  Corei7 (16)

Clock rate configured as 3325Mhz
Cannot detect CPU throttling.
/bin/sh: line 1: 22300: Abort(coredump)
xconfig exited with 6
make -f Make.top build
make[1]: Entering directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'
make[1]: Make.top: No such file or directory
make[1]: *** No rule to make target `Make.top'.  Stop.
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'
make: *** [build] Error 2
Failed to build ATLAS.
Failed to build ATLAS.

real	0m3.065s
user	0m1.150s
sys	0m1.074s
sage: An error occurred while installing atlas-3.8.3.p11
```



---

archive/issue_comments_070132.json:
```json
{
    "body": "This is on your machine too:\n\n\n```\nchmod: cannot access `/export/home/jaap/sage_port/sage-4.3.1/local/lib/libptf77blas.a': No such file or directory\nmake[1]: [install_lib] Error 1 (ignored)\nmake[1]: Leaving directory `/export/home/jaap/sage_port/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'\nDeleting liblapack.so on Solaris due to bug in numpy/scipy\n\nreal    8m49.450s\nuser    7m35.780s\nsys     1m0.353s\nSuccessfully installed atlas-3.8.3.p11\n\n```\n\n\nWhat's wrong?\n\nJaap",
    "created_at": "2010-01-28T14:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70132",
    "user": "https://github.com/jaapspies"
}
```

This is on your machine too:


```
chmod: cannot access `/export/home/jaap/sage_port/sage-4.3.1/local/lib/libptf77blas.a': No such file or directory
make[1]: [install_lib] Error 1 (ignored)
make[1]: Leaving directory `/export/home/jaap/sage_port/sage-4.3.1/spkg/build/atlas-3.8.3.p11/ATLAS-build'
Deleting liblapack.so on Solaris due to bug in numpy/scipy

real    8m49.450s
user    7m35.780s
sys     1m0.353s
Successfully installed atlas-3.8.3.p11

```


What's wrong?

Jaap



---

archive/issue_comments_070133.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-05T14:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70133",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070134.json:
```json
{
    "body": "Dave, Did you try again? Still no reaction from upstream.\n\nJaap",
    "created_at": "2010-02-05T14:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70134",
    "user": "https://github.com/jaapspies"
}
```

Dave, Did you try again? Still no reaction from upstream.

Jaap



---

archive/issue_comments_070135.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-05T17:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70135",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070136.json:
```json
{
    "body": "Given\n* I found -m64 fixed the problem on the command line, and \n* you have proven it works on my machine\n\nI am going to give this is a positive review.",
    "created_at": "2010-02-05T17:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70136",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Given
* I found -m64 fixed the problem on the command line, and 
* you have proven it works on my machine

I am going to give this is a positive review.



---

archive/issue_comments_070137.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-10T17:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70137",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_070138.json:
```json
{
    "body": "Sage 4.3.2 includes `atlas-3.8.3.p11.spkg`.  Should the package here be `p12`?",
    "created_at": "2010-02-10T17:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70138",
    "user": "https://github.com/qed777"
}
```

Sage 4.3.2 includes `atlas-3.8.3.p11.spkg`.  Should the package here be `p12`?



---

archive/issue_comments_070139.json:
```json
{
    "body": "Replying to [comment:12 mpatel]:\n> Sage 4.3.2 includes `atlas-3.8.3.p11.spkg`.  Should the package here be `p12`?\n\n\n\nMaybe now, but not on the moment I wrote the patch!\n\nThere is a real danger that tickets with positive review are not merged for a long time and bitrot.\n\nJaap",
    "created_at": "2010-02-10T19:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70139",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:12 mpatel]:
> Sage 4.3.2 includes `atlas-3.8.3.p11.spkg`.  Should the package here be `p12`?



Maybe now, but not on the moment I wrote the patch!

There is a real danger that tickets with positive review are not merged for a long time and bitrot.

Jaap



---

archive/issue_comments_070140.json:
```json
{
    "body": "I think I've merged all the other Solaris-related tickets at\u00a0{32}\u00a0into a candidate 4.3.3.alpha0.",
    "created_at": "2010-02-10T19:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70140",
    "user": "https://github.com/qed777"
}
```

I think I've merged all the other Solaris-related tickets at {32} into a candidate 4.3.3.alpha0.



---

archive/issue_comments_070141.json:
```json
{
    "body": "Replying to [comment:14 mpatel]:\n> I think I've merged all the other Solaris-related tickets at\u00a0{32}\u00a0into a candidate 4.3.3.alpha0.\n\n\nLook at 'porting' to see some more!\n\nJaap",
    "created_at": "2010-02-10T20:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70141",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:14 mpatel]:
> I think I've merged all the other Solaris-related tickets at {32} into a candidate 4.3.3.alpha0.


Look at 'porting' to see some more!

Jaap



---

archive/issue_comments_070142.json:
```json
{
    "body": "Yes, I've already those.",
    "created_at": "2010-02-10T22:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70142",
    "user": "https://github.com/qed777"
}
```

Yes, I've already those.



---

archive/issue_comments_070143.json:
```json
{
    "body": "Attachment [atlas-3.8.3.p12.patch](tarball://root/attachments/some-uuid/ticket8039/atlas-3.8.3.p12.patch) by @jaapspies created at 2010-02-22 21:39:10\n\nUpdated patch",
    "created_at": "2010-02-22T21:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70143",
    "user": "https://github.com/jaapspies"
}
```

Attachment [atlas-3.8.3.p12.patch](tarball://root/attachments/some-uuid/ticket8039/atlas-3.8.3.p12.patch) by @jaapspies created at 2010-02-22 21:39:10

Updated patch



---

archive/issue_comments_070144.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-22T21:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70144",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070145.json:
```json
{
    "body": "Rebased and increased patch level. New spkg:\n\n[http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p12.spkg](http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p12.spkg)\n\n\n```\nmake[1]: Leaving directory `/export/home/jaap/sage_port/sage-4.3.2.alpha1/spkg/build/atlas-3.8.3.p12/ATLAS-build'\nDeleting liblapack.so on Solaris due to bug in numpy/scipy\n\nreal    9m5.693s\nuser    7m45.589s\nsys     1m3.860s\nSuccessfully installed atlas-3.8.3.p12\nYou can safely delete the temporary build directory\n/export/home/jaap/sage_port/sage-4.3.2.alpha1/spkg/build/atlas-3.8.3.p12\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing atlas-3.8.3.p12.spkg\n-bash-3.2$ file local/lib/libatlas.*\nlocal/lib/libatlas.a:   current ar archive, not a dynamic executable or shared object\nlocal/lib/libatlas.so:  ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available\n\n```\n\nJaap",
    "created_at": "2010-02-22T21:45:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70145",
    "user": "https://github.com/jaapspies"
}
```

Rebased and increased patch level. New spkg:

[http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p12.spkg](http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p12.spkg)


```
make[1]: Leaving directory `/export/home/jaap/sage_port/sage-4.3.2.alpha1/spkg/build/atlas-3.8.3.p12/ATLAS-build'
Deleting liblapack.so on Solaris due to bug in numpy/scipy

real    9m5.693s
user    7m45.589s
sys     1m3.860s
Successfully installed atlas-3.8.3.p12
You can safely delete the temporary build directory
/export/home/jaap/sage_port/sage-4.3.2.alpha1/spkg/build/atlas-3.8.3.p12
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing atlas-3.8.3.p12.spkg
-bash-3.2$ file local/lib/libatlas.*
local/lib/libatlas.a:   current ar archive, not a dynamic executable or shared object
local/lib/libatlas.so:  ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped, no debugging information available

```

Jaap



---

archive/issue_comments_070146.json:
```json
{
    "body": "That looks good. It would be nice to find out exactly what -melf_x86_64 is supposed to do, but on a practical level, this allows ATLAS to build on OpenSolaris. Some more changees may be needed once Sage builds and we can run the doctests. But at least this builds, only effects Solaris and allows progress to be made.",
    "created_at": "2010-02-22T22:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70146",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That looks good. It would be nice to find out exactly what -melf_x86_64 is supposed to do, but on a practical level, this allows ATLAS to build on OpenSolaris. Some more changees may be needed once Sage builds and we can run the doctests. But at least this builds, only effects Solaris and allows progress to be made.



---

archive/issue_comments_070147.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-22T22:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70147",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019258.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-02T23:08:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8039#event-19258"
}
```



---

archive/issue_comments_070148.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T23:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70148",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_070149.json:
```json
{
    "body": "Merged [atlas-3.8.3.p12.spkg](http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p12.spkg) in the standard spkg repository.",
    "created_at": "2010-03-02T23:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8039",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8039#issuecomment-70149",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [atlas-3.8.3.p12.spkg](http://boxen.math.washington.edu/home/jsp/ports/atlas-3.8.3.p12.spkg) in the standard spkg repository.
