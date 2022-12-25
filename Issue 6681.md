# Issue 6681: cliquer doesn't work in 64-bit OS X

archive/issues_006681.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @nathanncohen\n\nIf I try a [64-bit build](http://wiki.sagemath.org/osx64) of Sage (4.1.1.rc1) on an Intel Mac running OS X 10.5, cliquer seems to install fine: I get a message saying,\n\"Successfully installed cliquer-1.2\".  However, starting Sage gives me an `ImportError`:\n\n```\nImportError: dlopen(/Applications/sage_builds/sage-4.1.1.rc1/local/lib/\npython2.6/site-packages/sage/graphs/cliquer.so, 2): Symbol not found:\n_graph_new\n  Referenced from: /Applications/sage_builds/sage-4.1.1.rc1/local/lib/\npython2.6/site-packages/sage/graphs/cliquer.so\n  Expected in: dynamic lookup\n\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6681\n\n",
    "created_at": "2009-08-06T19:13:39Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "cliquer doesn't work in 64-bit OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6681",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @rlmill

CC:  @nathanncohen

If I try a [64-bit build](http://wiki.sagemath.org/osx64) of Sage (4.1.1.rc1) on an Intel Mac running OS X 10.5, cliquer seems to install fine: I get a message saying,
"Successfully installed cliquer-1.2".  However, starting Sage gives me an `ImportError`:

```
ImportError: dlopen(/Applications/sage_builds/sage-4.1.1.rc1/local/lib/
python2.6/site-packages/sage/graphs/cliquer.so, 2): Symbol not found:
_graph_new
  Referenced from: /Applications/sage_builds/sage-4.1.1.rc1/local/lib/
python2.6/site-packages/sage/graphs/cliquer.so
  Expected in: dynamic lookup

Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed. 
```


Issue created by migration from https://trac.sagemath.org/ticket/6681





---

archive/issue_comments_054815.json:
```json
{
    "body": "My failed attempt at this: change the beginning of SConstruct from\n\n```\nenv = Environment()  # Create an environment\n```\n\nto\n\n```\nimport os\n\n# Create an environment\nif os.getenv(\"SAGE64\") == \"yes\":\n   env = Environment(CFLAGS = '-O3 -fomit-frame-pointer -funroll-loops -g -m64',\n      LINKFLAGS='-m64')\nelse:\n   env = Environment()\n```\n\nThis uses '-m64' for the compilation process when SAGE64 is set to yes (and it should probably also check for OSX):\n\n```\nscons: Reading SConscript files ...\nscons: done reading SConscript files.\nscons: Building targets ...\ngcc -o src/cl.os -c -O3 -fomit-frame-pointer -funroll-loops -g -m64 -fPIC src/cl.c\ngcc -o src/cliquer.os -c -O3 -fomit-frame-pointer -funroll-loops -g -m64 -fPIC src/cliquer.c\ngcc -o src/graph.os -c -O3 -fomit-frame-pointer -funroll-loops -g -m64 -fPIC src/graph.c\ngcc -o src/reorder.os -c -O3 -fomit-frame-pointer -funroll-loops -g -m64 -fPIC src/reorder.c\ngcc -o libcliquer.dylib -m64 -dynamiclib src/cl.os src/cliquer.os src/graph.os src/reorder.os\nInstall file: \"libcliquer.dylib\" as \"Build/libcliquer.dylib\"\nscons: done building targets.\n```\n\nBut I still get the same error message when starting Sage.  I know basically nothing about compiling programs, though, so I was just taking a shot in the dark anyway.\n\n(By the way, I got the flags \"-fomit-frame-pointer -funroll-loops\" from the cliquer Makefile; removing them doesn't help.)",
    "created_at": "2009-08-21T05:23:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54815",
    "user": "https://github.com/jhpalmieri"
}
```

My failed attempt at this: change the beginning of SConstruct from

```
env = Environment()  # Create an environment
```

to

```
import os

# Create an environment
if os.getenv("SAGE64") == "yes":
   env = Environment(CFLAGS = '-O3 -fomit-frame-pointer -funroll-loops -g -m64',
      LINKFLAGS='-m64')
else:
   env = Environment()
```

This uses '-m64' for the compilation process when SAGE64 is set to yes (and it should probably also check for OSX):

```
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
gcc -o src/cl.os -c -O3 -fomit-frame-pointer -funroll-loops -g -m64 -fPIC src/cl.c
gcc -o src/cliquer.os -c -O3 -fomit-frame-pointer -funroll-loops -g -m64 -fPIC src/cliquer.c
gcc -o src/graph.os -c -O3 -fomit-frame-pointer -funroll-loops -g -m64 -fPIC src/graph.c
gcc -o src/reorder.os -c -O3 -fomit-frame-pointer -funroll-loops -g -m64 -fPIC src/reorder.c
gcc -o libcliquer.dylib -m64 -dynamiclib src/cl.os src/cliquer.os src/graph.os src/reorder.os
Install file: "libcliquer.dylib" as "Build/libcliquer.dylib"
scons: done building targets.
```

But I still get the same error message when starting Sage.  I know basically nothing about compiling programs, though, so I was just taking a shot in the dark anyway.

(By the way, I got the flags "-fomit-frame-pointer -funroll-loops" from the cliquer Makefile; removing them doesn't help.)



---

archive/issue_comments_054816.json:
```json
{
    "body": "An updated package is up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg\n\nUnlike the previous package cliquer-1.2.spkg, the updated package cliquer-1.2.p0.spkg doesn't use SCons. Based upon the Makefile of cliquer 1.2, I added some custom compilation and linking flags to that Makefile. The custom Makefile is located in the patch/ directory. When installing cliquer-1.2.p0.spkg, the Makefile of cliquer found in src/ is replaced with this custom Makefile. I have tested cliquer-1.2.p0.spkg under the following platforms:\n\n* bsd.math --- Mac OS X 10.5.8 in 32-bit mode, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK; all tests passed even with the option \"-long\".\n\n* bsd.math --- Mac OS X 10.5.8 in 64-bit mode, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. ECL didn't build at all in 64-bit mode. When ECL failed to build, I manually installed cliquer using\n\n```\n./sage -f spkg/standard/cliquer-1.2.p0.spkg\n```\n\n Compilation went OK. I didn't run the test suite since ECL failing to build meant that I would get heaps of doctest failures.\n\n* sage.math --- x86_64 Ubuntu 8.04.3 LTS, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK. All tests passed even with the option \"-long\".\n\n* t2.math --- SPARC Solaris 5.10 with GCC 4.4.1 and Sun linker. Sage 4.1.1 failed to build on t2.math. Using this (failed) build, I installed cliquer-1.2.p0.spkg using\n\n```\n./sage -f /patch/to/cliquer-1.2.p0.spkg\n```\n\n Compilation went OK.\n\n* cicero on SkyNet --- x86 Fedora 9 with GCC 4.4.1, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK. The following tests failed:\n\n```\nsage -t -long \"devel/sage/sage/misc/randstate.pyx\"\nsage -t -long \"devel/sage/sage/interfaces/expect.py\"\nsage -t -long \"devel/sage/sage/interfaces/sage0.py\"\nsage -t -long \"devel/sage/sage/server/simple/twist.py\"\n```\n\n all of which had nothing to do with cliquer.\n\n* eno on SkyNet --- x86_64 Fedora 9 with GCC 4.4.1, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK. All tests passed even with the option \"-long\".\n\n* lena on SkyNet --- x86_64 RHEL 5.3 with GCC 4.4.1, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK. All tests passed even with the option \"-long\".\n\n* menas on SkyNet --- x86_64 openSUSE 11.1 with GCC 4.4.1, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK; previously, Sage 4.1.1 failed to build on menas due to 64-bit bit issue in cliquer. All tests passed even with the option \"-long\".",
    "created_at": "2009-09-13T09:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54816",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

An updated package is up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg

Unlike the previous package cliquer-1.2.spkg, the updated package cliquer-1.2.p0.spkg doesn't use SCons. Based upon the Makefile of cliquer 1.2, I added some custom compilation and linking flags to that Makefile. The custom Makefile is located in the patch/ directory. When installing cliquer-1.2.p0.spkg, the Makefile of cliquer found in src/ is replaced with this custom Makefile. I have tested cliquer-1.2.p0.spkg under the following platforms:

* bsd.math --- Mac OS X 10.5.8 in 32-bit mode, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK; all tests passed even with the option "-long".

* bsd.math --- Mac OS X 10.5.8 in 64-bit mode, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. ECL didn't build at all in 64-bit mode. When ECL failed to build, I manually installed cliquer using

```
./sage -f spkg/standard/cliquer-1.2.p0.spkg
```

 Compilation went OK. I didn't run the test suite since ECL failing to build meant that I would get heaps of doctest failures.

* sage.math --- x86_64 Ubuntu 8.04.3 LTS, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK. All tests passed even with the option "-long".

* t2.math --- SPARC Solaris 5.10 with GCC 4.4.1 and Sun linker. Sage 4.1.1 failed to build on t2.math. Using this (failed) build, I installed cliquer-1.2.p0.spkg using

```
./sage -f /patch/to/cliquer-1.2.p0.spkg
```

 Compilation went OK.

* cicero on SkyNet --- x86 Fedora 9 with GCC 4.4.1, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK. The following tests failed:

```
sage -t -long "devel/sage/sage/misc/randstate.pyx"
sage -t -long "devel/sage/sage/interfaces/expect.py"
sage -t -long "devel/sage/sage/interfaces/sage0.py"
sage -t -long "devel/sage/sage/server/simple/twist.py"
```

 all of which had nothing to do with cliquer.

* eno on SkyNet --- x86_64 Fedora 9 with GCC 4.4.1, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK. All tests passed even with the option "-long".

* lena on SkyNet --- x86_64 RHEL 5.3 with GCC 4.4.1, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK. All tests passed even with the option "-long".

* menas on SkyNet --- x86_64 openSUSE 11.1 with GCC 4.4.1, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK; previously, Sage 4.1.1 failed to build on menas due to 64-bit bit issue in cliquer. All tests passed even with the option "-long".



---

archive/issue_comments_054817.json:
```json
{
    "body": "If the updated cliquer package also builds on 64-bit Fedora 10, then #6746 should be closed as a duplicate of this ticket.",
    "created_at": "2009-09-13T09:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54817",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

If the updated cliquer package also builds on 64-bit Fedora 10, then #6746 should be closed as a duplicate of this ticket.



---

archive/issue_comments_054818.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n> An updated package is up at\n> \n> http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg\n> \n> Unlike the previous package cliquer-1.2.spkg, the updated package cliquer-1.2.p0.spkg doesn't use SCons. Based upon the Makefile of cliquer 1.2, I added some custom compilation and linking flags to that Makefile. The custom Makefile is located in the patch/ directory. When installing cliquer-1.2.p0.spkg, the Makefile of cliquer found in src/ is replaced with this custom Makefile. I have tested cliquer-1.2.p0.spkg under the following platforms:\n> \n>  * bsd.math --- Mac OS X 10.5.8 in 32-bit mode, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK; all tests passed even with the option \"-long\".\n\nWorks for me, too (although so far I've only had the patience to doctest the \"graphs\" directory).\n\n>  * bsd.math --- Mac OS X 10.5.8 in 64-bit mode, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. ECL didn't build at all in 64-bit mode. When ECL failed to build, I manually installed cliquer using\n> {{{\n> ./sage -f spkg/standard/cliquer-1.2.p0.spkg\n> }}}\n>  Compilation went OK. I didn't run the test suite since ECL failing to build meant that I would get heaps of doctest failures.\n\nSee my message [on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e4bf19abd63b598b?tvc=2) for how I got Sage 4.1.2.alpha1 to build and run (except for 1 doctest failure) on 64-bit Mac OS X.  Basically, I used [http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4.p0-5th-attempt/ecl-9.8.4.p0.spkg](http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4.p0-5th-attempt/ecl-9.8.4.p0.spkg); although this doesn't actually build in 64-bit mode, it's not clear how bad that is.  Sage runs this way, so it's better than nothing.  You could also test your cliquer spkg on 4.1.2.alpha0 or 4.1.1.\n\nWith this build, the new cliquer spkg doesn't work, unfortunately: it compiles, but when I start Sage, I get the same `ImportError` as reported in the ticket description:\n\n```\nImportError                               Traceback (most recent call last)\n\n[snip]\n\nImportError: dlopen(/Applications/sage_builds/sage-4.1.2.alpha1-64bit/local/lib/python2.6/site-packages/sage/graphs/cliquer.so, 2): Symbol not found: _graph_new\n  Referenced from: /Applications/sage_builds/sage-4.1.2.alpha1-64bit/local/lib/python2.6/site-packages/sage/graphs/cliquer.so\n  Expected in: dynamic lookup\n\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\nI wish I knew something about Makefiles, but I don't, so I don't know what to suggest.",
    "created_at": "2009-09-13T15:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54818",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:3 mvngu]:
> An updated package is up at
> 
> http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg
> 
> Unlike the previous package cliquer-1.2.spkg, the updated package cliquer-1.2.p0.spkg doesn't use SCons. Based upon the Makefile of cliquer 1.2, I added some custom compilation and linking flags to that Makefile. The custom Makefile is located in the patch/ directory. When installing cliquer-1.2.p0.spkg, the Makefile of cliquer found in src/ is replaced with this custom Makefile. I have tested cliquer-1.2.p0.spkg under the following platforms:
> 
>  * bsd.math --- Mac OS X 10.5.8 in 32-bit mode, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. Compilation went OK; all tests passed even with the option "-long".

Works for me, too (although so far I've only had the patience to doctest the "graphs" directory).

>  * bsd.math --- Mac OS X 10.5.8 in 64-bit mode, compiling Sage 4.1.2.alpha1 from scratch with cliquer-1.2.p0.spkg. ECL didn't build at all in 64-bit mode. When ECL failed to build, I manually installed cliquer using
> {{{
> ./sage -f spkg/standard/cliquer-1.2.p0.spkg
> }}}
>  Compilation went OK. I didn't run the test suite since ECL failing to build meant that I would get heaps of doctest failures.

See my message [on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e4bf19abd63b598b?tvc=2) for how I got Sage 4.1.2.alpha1 to build and run (except for 1 doctest failure) on 64-bit Mac OS X.  Basically, I used [http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4.p0-5th-attempt/ecl-9.8.4.p0.spkg](http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4.p0-5th-attempt/ecl-9.8.4.p0.spkg); although this doesn't actually build in 64-bit mode, it's not clear how bad that is.  Sage runs this way, so it's better than nothing.  You could also test your cliquer spkg on 4.1.2.alpha0 or 4.1.1.

With this build, the new cliquer spkg doesn't work, unfortunately: it compiles, but when I start Sage, I get the same `ImportError` as reported in the ticket description:

```
ImportError                               Traceback (most recent call last)

[snip]

ImportError: dlopen(/Applications/sage_builds/sage-4.1.2.alpha1-64bit/local/lib/python2.6/site-packages/sage/graphs/cliquer.so, 2): Symbol not found: _graph_new
  Referenced from: /Applications/sage_builds/sage-4.1.2.alpha1-64bit/local/lib/python2.6/site-packages/sage/graphs/cliquer.so
  Expected in: dynamic lookup

Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```

I wish I knew something about Makefiles, but I don't, so I don't know what to suggest.



---

archive/issue_comments_054819.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n>You could also test your cliquer spkg on 4.1.2.alpha0 or 4.1.1.\n\nCompile Sage 4.1.1 successfully from scratch with cliquer-1.2.p0.spkg on OS X 10.5.8 (bsd.math) in 64-bit mode. All tests passed even with the option \"-long\". Sage loads without problems.\n\n\n\n\nI'm doing more porting work with cliquer as suggested by David Kirkby at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/15c461b1355a8460) thread. So I'm marking this ticket as \"needs work\".",
    "created_at": "2009-09-13T15:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54819",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:5 jhpalmieri]:
>You could also test your cliquer spkg on 4.1.2.alpha0 or 4.1.1.

Compile Sage 4.1.1 successfully from scratch with cliquer-1.2.p0.spkg on OS X 10.5.8 (bsd.math) in 64-bit mode. All tests passed even with the option "-long". Sage loads without problems.




I'm doing more porting work with cliquer as suggested by David Kirkby at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/15c461b1355a8460) thread. So I'm marking this ticket as "needs work".



---

archive/issue_comments_054820.json:
```json
{
    "body": "\n```\n> Hence I would be tempted to make that as 'with spgk, needs work', since\n> it makes some pretty fundamental assumptions which will not be valid.\n>\n\nBut alas cliquer is already in Sage, and that ticket is titled:\n\n   \"cliquer doesn't work in 64-bit OS X\"\n\nIf the spkg fixes this problem and doesn't make things *worse* on\nSolaris, it absolutely  should get a positive review.  Note that the assuming \"CC=gcc\" was already in the original cliquer spkg.  It is not something added by that ticket. \n\nIf we were discussing including cliquer in the first place, I might\nhave a different opinion.\n\nI encourage you to open your own ticket which is entitled \"port cliquer so that it builds with the Sun Studio compiler\", then post a patch there that addresses the problem you see. \n```\n",
    "created_at": "2009-09-13T17:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54820",
    "user": "https://github.com/williamstein"
}
```


```
> Hence I would be tempted to make that as 'with spgk, needs work', since
> it makes some pretty fundamental assumptions which will not be valid.
>

But alas cliquer is already in Sage, and that ticket is titled:

   "cliquer doesn't work in 64-bit OS X"

If the spkg fixes this problem and doesn't make things *worse* on
Solaris, it absolutely  should get a positive review.  Note that the assuming "CC=gcc" was already in the original cliquer spkg.  It is not something added by that ticket. 

If we were discussing including cliquer in the first place, I might
have a different opinion.

I encourage you to open your own ticket which is entitled "port cliquer so that it builds with the Sun Studio compiler", then post a patch there that addresses the problem you see. 
```




---

archive/issue_comments_054821.json:
```json
{
    "body": "Some comments:\n\n* The spkg-install script has\n\n```\nmkdir \"$SAGE_LOCAL/include/cliquer/\"\ncp src/*.h \"$SAGE_LOCAL/include/cliquer/\"\n```\n\nat the top.  There are two problems with this:\n\n1. If the build fails, you've just possibly messed up $SAGE_LOCAL.  It's best if when building nothing is changed in SAGE_LOCAL unless the build succeeds.  So just move these lines down past the make line. \n\n2. After the first time cliquer is installed, any future time it is installed the line `mkdir \"$SAGE_LOCAL/include/cliquer/\"` will give an error (which is ignored since the error isn't checked):\n\n  {{{\n  bash-3.2$ mkdir \"$SAGE_LOCAL/include/cliquer/\"\n  mkdir: /Users/wstein/sage/build/64bit/sage/local/include/cliquer/: File exists\n  }}}\n\n* After the \"make\" command, no error checking is done.  If the make fails you might not even know!\n\n```\ncd src\nmake\ncp -f libcliquer.so \"$SAGE_LOCAL/lib/\"\n```\n\n\nYou just luck out if it happens that the make failing doesn't produce libcliquer.so since that cp line just happens to be the last line of the file.  You need to check the output code of the make like is done in every other spkg-install. \n\n* Regarding the line that Kirkby pointed out that \"CC=gcc\".   That's trivial to fix -- just delete it in Makefile!  Since CC gets sets before spkg-install is run, it isn't something your spkg has to worry about.",
    "created_at": "2009-09-13T18:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54821",
    "user": "https://github.com/williamstein"
}
```

Some comments:

* The spkg-install script has

```
mkdir "$SAGE_LOCAL/include/cliquer/"
cp src/*.h "$SAGE_LOCAL/include/cliquer/"
```

at the top.  There are two problems with this:

1. If the build fails, you've just possibly messed up $SAGE_LOCAL.  It's best if when building nothing is changed in SAGE_LOCAL unless the build succeeds.  So just move these lines down past the make line. 

2. After the first time cliquer is installed, any future time it is installed the line `mkdir "$SAGE_LOCAL/include/cliquer/"` will give an error (which is ignored since the error isn't checked):

  {{{
  bash-3.2$ mkdir "$SAGE_LOCAL/include/cliquer/"
  mkdir: /Users/wstein/sage/build/64bit/sage/local/include/cliquer/: File exists
  }}}

* After the "make" command, no error checking is done.  If the make fails you might not even know!

```
cd src
make
cp -f libcliquer.so "$SAGE_LOCAL/lib/"
```


You just luck out if it happens that the make failing doesn't produce libcliquer.so since that cp line just happens to be the last line of the file.  You need to check the output code of the make like is done in every other spkg-install. 

* Regarding the line that Kirkby pointed out that "CC=gcc".   That's trivial to fix -- just delete it in Makefile!  Since CC gets sets before spkg-install is run, it isn't something your spkg has to worry about.



---

archive/issue_comments_054822.json:
```json
{
    "body": "Replying to [comment:8 was]:\n>   1. If the build fails, you've just possibly messed up $SAGE_LOCAL.  It's best if when building nothing is changed in SAGE_LOCAL unless the build succeeds.  So just move these lines down past the make line. \nDone.\n\n\n\n\n\n>   2. After the first time cliquer is installed, any future time it is installed the line `mkdir \"$SAGE_LOCAL/include/cliquer/\"` will give an error (which is ignored since the error isn't checked):\n> \n>   {{{\n>   bash-3.2$ mkdir \"$SAGE_LOCAL/include/cliquer/\"\n>   mkdir: /Users/wstein/sage/build/64bit/sage/local/include/cliquer/: File exists\n>   }}}\nThe file `spkg-install` now checks for the existence of the directory `SAGE_LOCAL/include/cliquer/`. If that directory doesn't exist, it would be created.\n\n\n\n\n\n> You just luck out if it happens that the make failing doesn't produce libcliquer.so since that cp line just happens to be the last line of the file.  You need to check the output code of the make like is done in every other spkg-install. \nDone. The output code of `make` is now checked.\n\n\n\n\n\n> * Regarding the line that Kirkby pointed out that \"CC=gcc\".   That's trivial to fix -- just delete it in Makefile!  Since CC gets sets before spkg-install is run, it isn't something your spkg has to worry about. \nDone.\n\n\n\n\n\nAn updated package is up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg",
    "created_at": "2009-09-16T09:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54822",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:8 was]:
>   1. If the build fails, you've just possibly messed up $SAGE_LOCAL.  It's best if when building nothing is changed in SAGE_LOCAL unless the build succeeds.  So just move these lines down past the make line. 
Done.





>   2. After the first time cliquer is installed, any future time it is installed the line `mkdir "$SAGE_LOCAL/include/cliquer/"` will give an error (which is ignored since the error isn't checked):
> 
>   {{{
>   bash-3.2$ mkdir "$SAGE_LOCAL/include/cliquer/"
>   mkdir: /Users/wstein/sage/build/64bit/sage/local/include/cliquer/: File exists
>   }}}
The file `spkg-install` now checks for the existence of the directory `SAGE_LOCAL/include/cliquer/`. If that directory doesn't exist, it would be created.





> You just luck out if it happens that the make failing doesn't produce libcliquer.so since that cp line just happens to be the last line of the file.  You need to check the output code of the make like is done in every other spkg-install. 
Done. The output code of `make` is now checked.





> * Regarding the line that Kirkby pointed out that "CC=gcc".   That's trivial to fix -- just delete it in Makefile!  Since CC gets sets before spkg-install is run, it isn't something your spkg has to worry about. 
Done.





An updated package is up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg



---

archive/issue_comments_054823.json:
```json
{
    "body": "Changing component from graph theory to packages.",
    "created_at": "2009-09-16T09:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54823",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from graph theory to packages.



---

archive/issue_comments_054824.json:
```json
{
    "body": "Changing assignee from @rlmill to mabshoff.",
    "created_at": "2009-09-16T09:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54824",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing assignee from @rlmill to mabshoff.



---

archive/issue_comments_054825.json:
```json
{
    "body": "I believe there is a problem here. \n\n'set -e' was put at the top, so the script will exit immediately if there is an error. Therefore if 'make' fails for any reason, the script will exit, and the message \"Failed to compile cliquer... exiting\" will never appear. Hence there needs to be a 'set +e' immediately before the 'make' command. Then 'set -e' needs to be enabled again. Hence the end of the spkg-install should be like this:\n\n\n```\ncp -f patch/Makefile src/\n\ncd src\n#Do not exit script if there is an error, but instead print an informative error message\nset +e \nmake\nif [ $? -ne 0 ]; then\n    echo \"Failed to compile cliquer... exiting\"\n    exit 1\nfi\nset -e \nif [ ! -e \"$SAGE_LOCAL/include/cliquer\" ]; then\n    mkdir \"$SAGE_LOCAL/include/cliquer/\"\nfi\n\ncp -f *.h \"$SAGE_LOCAL/include/cliquer/\"\ncp -f libcliquer.so \"$SAGE_LOCAL/lib/\"\n```\n",
    "created_at": "2009-09-16T10:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54825",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I believe there is a problem here. 

'set -e' was put at the top, so the script will exit immediately if there is an error. Therefore if 'make' fails for any reason, the script will exit, and the message "Failed to compile cliquer... exiting" will never appear. Hence there needs to be a 'set +e' immediately before the 'make' command. Then 'set -e' needs to be enabled again. Hence the end of the spkg-install should be like this:


```
cp -f patch/Makefile src/

cd src
#Do not exit script if there is an error, but instead print an informative error message
set +e 
make
if [ $? -ne 0 ]; then
    echo "Failed to compile cliquer... exiting"
    exit 1
fi
set -e 
if [ ! -e "$SAGE_LOCAL/include/cliquer" ]; then
    mkdir "$SAGE_LOCAL/include/cliquer/"
fi

cp -f *.h "$SAGE_LOCAL/include/cliquer/"
cp -f libcliquer.so "$SAGE_LOCAL/lib/"
```




---

archive/issue_comments_054826.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n> Hence the end of the spkg-install should be like this:\nDone. Updated package is up at the same place:\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg",
    "created_at": "2009-09-16T13:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54826",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:11 drkirkby]:
> Hence the end of the spkg-install should be like this:
Done. Updated package is up at the same place:

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg



---

archive/issue_comments_054827.json:
```json
{
    "body": "That looks fine to me now\n\nDave",
    "created_at": "2009-09-16T16:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54827",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That looks fine to me now

Dave



---

archive/issue_comments_054828.json:
```json
{
    "body": "On 64-bit OS X, when I ran \"sage -f cliquer...\", I get doctest failures. (32-bit worked fine.)  I'm building from scratch now.  Until that's done, I'm changing this from \"positive review\" to \"needs review\"; if it passes tests, I'll restore the positive review.  If not, I'll of course report the failures and mark it as \"needs work\".\n\nI'm also building from scratch for 32-bit OS X, just to double-check that version.",
    "created_at": "2009-09-16T16:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54828",
    "user": "https://github.com/jhpalmieri"
}
```

On 64-bit OS X, when I ran "sage -f cliquer...", I get doctest failures. (32-bit worked fine.)  I'm building from scratch now.  Until that's done, I'm changing this from "positive review" to "needs review"; if it passes tests, I'll restore the positive review.  If not, I'll of course report the failures and mark it as "needs work".

I'm also building from scratch for 32-bit OS X, just to double-check that version.



---

archive/issue_comments_054829.json:
```json
{
    "body": "32-bit Mac OS X builds fine and all tests pass.\n\n64-bit Mac OS X builds fine and all tests pass.\n\nSince the summary of the ticket just mentions 64-bit OS X, is this good enough for a positive review, or do we need to doctest on other platforms?  drkirby, when you gave your positive review, what platforms had you doctested it on?",
    "created_at": "2009-09-17T02:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54829",
    "user": "https://github.com/jhpalmieri"
}
```

32-bit Mac OS X builds fine and all tests pass.

64-bit Mac OS X builds fine and all tests pass.

Since the summary of the ticket just mentions 64-bit OS X, is this good enough for a positive review, or do we need to doctest on other platforms?  drkirby, when you gave your positive review, what platforms had you doctested it on?



---

archive/issue_comments_054830.json:
```json
{
    "body": "One tiny problem I see on Ubuntu Jaunty amd64: the installation says it's building a 32-bit version, but I'm reasonably certain a 64-bit version gets built. Here's a couple of the gcc lines from installation:\n\n```\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/var/tmp/sage-4.1.2.alpha1/local/include   -c -o cliquer.o cliquer.c\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/var/tmp/sage-4.1.2.alpha1/local/include   -c -o graph.o graph.c\n```\n\nThose all look pretty simple. And...\n\n```\n$ ldd local/lib/libcliquer.so \n\tlinux-vdso.so.1 =>  (0x00007fff1d7ff000)\n\tlibc.so.6 => /lib/libc.so.6 (0x00007fa915236000)\n\t/lib64/ld-linux-x86-64.so.2 (0x0000003582800000)\n```\n\n\nI see that spkg-install is just looking for SAGE64, which I don't set on Ubuntu; the 64-bit build \"just happens\" AFAIK.\n\nAlso, it builds with debugging information present by default -- is that what we want?\n\nAlso, how do I run the tests? I set SAGE_CHECK=yes, but \"sage -f (url)\" didn't do any tests. When I went into the src/ directory and ran \"make test\", it couldn't find the \"testcases\" program -- I think it needs \"./testcases\". When I ran that myself, it passed all the tests.",
    "created_at": "2009-09-18T00:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54830",
    "user": "https://github.com/dandrake"
}
```

One tiny problem I see on Ubuntu Jaunty amd64: the installation says it's building a 32-bit version, but I'm reasonably certain a 64-bit version gets built. Here's a couple of the gcc lines from installation:

```
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/var/tmp/sage-4.1.2.alpha1/local/include   -c -o cliquer.o cliquer.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/var/tmp/sage-4.1.2.alpha1/local/include   -c -o graph.o graph.c
```

Those all look pretty simple. And...

```
$ ldd local/lib/libcliquer.so 
	linux-vdso.so.1 =>  (0x00007fff1d7ff000)
	libc.so.6 => /lib/libc.so.6 (0x00007fa915236000)
	/lib64/ld-linux-x86-64.so.2 (0x0000003582800000)
```


I see that spkg-install is just looking for SAGE64, which I don't set on Ubuntu; the 64-bit build "just happens" AFAIK.

Also, it builds with debugging information present by default -- is that what we want?

Also, how do I run the tests? I set SAGE_CHECK=yes, but "sage -f (url)" didn't do any tests. When I went into the src/ directory and ran "make test", it couldn't find the "testcases" program -- I think it needs "./testcases". When I ran that myself, it passed all the tests.



---

archive/issue_comments_054831.json:
```json
{
    "body": "Replying to [comment:16 ddrake]:\n> One tiny problem I see on Ubuntu Jaunty amd64: the installation says it's building a 32-bit version, but I'm reasonably certain a 64-bit version gets built.\nFixed. That \"building a 32-bit version\" message as output by spkg-install is misleading. I have commented it out.\n\n\n\n\n\n> Also, it builds with debugging information present by default -- is that what we want?\nYes. Better safe than sorry. Since David Kirkby has been doing porting work to Solaris a few months ago, we have been building with debugging information by default for all packages updated so far by David and I.\n\n\n\n\n\n> Also, how do I run the tests? I set SAGE_CHECK=yes, but \"sage -f (url)\" didn't do any tests. When I went into the src/ directory and ran \"make test\", it couldn't find the \"testcases\" program -- I think it needs \"./testcases\". When I ran that myself, it passed all the tests.\nFixed. I have modified `spkg-install` to allow you to compile and run `testcases` of cliquer. To do so, set the environment variable `SAGE_CHECK` to true before compiling; e.g.\n\n```\nexport SAGE_CHECK=yes\n```\n\nAn updated spkg is up at the same place:\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg",
    "created_at": "2009-09-18T01:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54831",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:16 ddrake]:
> One tiny problem I see on Ubuntu Jaunty amd64: the installation says it's building a 32-bit version, but I'm reasonably certain a 64-bit version gets built.
Fixed. That "building a 32-bit version" message as output by spkg-install is misleading. I have commented it out.





> Also, it builds with debugging information present by default -- is that what we want?
Yes. Better safe than sorry. Since David Kirkby has been doing porting work to Solaris a few months ago, we have been building with debugging information by default for all packages updated so far by David and I.





> Also, how do I run the tests? I set SAGE_CHECK=yes, but "sage -f (url)" didn't do any tests. When I went into the src/ directory and ran "make test", it couldn't find the "testcases" program -- I think it needs "./testcases". When I ran that myself, it passed all the tests.
Fixed. I have modified `spkg-install` to allow you to compile and run `testcases` of cliquer. To do so, set the environment variable `SAGE_CHECK` to true before compiling; e.g.

```
export SAGE_CHECK=yes
```

An updated spkg is up at the same place:

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg



---

archive/issue_comments_054832.json:
```json
{
    "body": "Replying to [comment:17 mvngu]:\n> An updated spkg is up at the same place:\n> \n> http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg\n\nAll my concerns are addressed, and it builds and passes tests on Ubuntu amd64. If drkirkby thinks this is good enough, I say it's fine.",
    "created_at": "2009-09-18T05:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54832",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:17 mvngu]:
> An updated spkg is up at the same place:
> 
> http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg

All my concerns are addressed, and it builds and passes tests on Ubuntu amd64. If drkirkby thinks this is good enough, I say it's fine.



---

archive/issue_comments_054833.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-09-21T02:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54833",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_054834.json:
```json
{
    "body": "This spkg builds as part of 4.1.2alpha2 and passes all tests on 64-bit Fedora 10.",
    "created_at": "2009-09-22T19:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54834",
    "user": "https://github.com/kedlaya"
}
```

This spkg builds as part of 4.1.2alpha2 and passes all tests on 64-bit Fedora 10.



---

archive/issue_comments_054835.json:
```json
{
    "body": "This builds and passes tests on OS X 10.6 (if installed along with the other SPKG's listed at #6849).",
    "created_at": "2009-09-27T16:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54835",
    "user": "https://github.com/jhpalmieri"
}
```

This builds and passes tests on OS X 10.6 (if installed along with the other SPKG's listed at #6849).



---

archive/issue_comments_054836.json:
```json
{
    "body": "What needs to be done for this to get a positive review?",
    "created_at": "2009-10-01T14:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54836",
    "user": "https://github.com/jhpalmieri"
}
```

What needs to be done for this to get a positive review?



---

archive/issue_comments_054837.json:
```json
{
    "body": "Replying to [comment:22 jhpalmieri]:\n> What needs to be done for this to get a positive review?\nCompile Sage with this cliquer package on Solaris (t2.math or any SPARC Solaris machine) using GCC.",
    "created_at": "2009-10-01T14:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54837",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:22 jhpalmieri]:
> What needs to be done for this to get a positive review?
Compile Sage with this cliquer package on Solaris (t2.math or any SPARC Solaris machine) using GCC.



---

archive/issue_comments_054838.json:
```json
{
    "body": "Does the old cliquer package work on Solaris?  If so, is it possible to combine the two to get something which works on both Solaris and 64-bit Mac OS X?",
    "created_at": "2009-10-01T15:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54838",
    "user": "https://github.com/jhpalmieri"
}
```

Does the old cliquer package work on Solaris?  If so, is it possible to combine the two to get something which works on both Solaris and 64-bit Mac OS X?



---

archive/issue_comments_054839.json:
```json
{
    "body": "Replying to [comment:24 jhpalmieri]:\n> Does the old cliquer package work on Solaris? \nNo. The current version of the cliquer spkg that's shipped with Sage uses SCons and so it can fail to build on some 64-bit platforms and t2.math.\n\n\n\n\n> If so, is it possible to combine the two to get something which works on both Solaris and 64-bit Mac OS X?\nThat's what the updated cliquer package is doing. It removes the need for using SCons to build cliquer and at the same time adds support for building cliquer on the platforms that are known to fail previously. I have built the updated cliquer spkg with Sage 4.1.2.rc0 on t2.math and 64-bit openSUSE 11.1 and it compiled OK. It's just that someone else besides the package author (me) should do the same thing on t2.math to make sure that cliquer builds as I so claim.",
    "created_at": "2009-10-01T15:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54839",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:24 jhpalmieri]:
> Does the old cliquer package work on Solaris? 
No. The current version of the cliquer spkg that's shipped with Sage uses SCons and so it can fail to build on some 64-bit platforms and t2.math.




> If so, is it possible to combine the two to get something which works on both Solaris and 64-bit Mac OS X?
That's what the updated cliquer package is doing. It removes the need for using SCons to build cliquer and at the same time adds support for building cliquer on the platforms that are known to fail previously. I have built the updated cliquer spkg with Sage 4.1.2.rc0 on t2.math and 64-bit openSUSE 11.1 and it compiled OK. It's just that someone else besides the package author (me) should do the same thing on t2.math to make sure that cliquer builds as I so claim.



---

archive/issue_comments_054840.json:
```json
{
    "body": "Replying to [comment:25 mvngu]:\n> It's just that someone else besides the package author (me) should do the same thing on t2.math to make sure that cliquer builds as I so claim.\n\nI'm doing this now.",
    "created_at": "2009-10-02T18:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54840",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:25 mvngu]:
> It's just that someone else besides the package author (me) should do the same thing on t2.math to make sure that cliquer builds as I so claim.

I'm doing this now.



---

archive/issue_comments_054841.json:
```json
{
    "body": "Hi,\n\nI've merged http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg into sage-4.1.2.rc1.spkg.\nMinh -- unless something changes you can close this ticket.  It certainly solves the problem \"cliquer doesn't work in 64-bit OS X\".",
    "created_at": "2009-10-04T02:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54841",
    "user": "https://github.com/williamstein"
}
```

Hi,

I've merged http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg into sage-4.1.2.rc1.spkg.
Minh -- unless something changes you can close this ticket.  It certainly solves the problem "cliquer doesn't work in 64-bit OS X".



---

archive/issue_comments_054842.json:
```json
{
    "body": "I can verify that the cliquer part of the install worked on t2.",
    "created_at": "2009-10-04T02:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54842",
    "user": "https://github.com/rlmill"
}
```

I can verify that the cliquer part of the install worked on t2.



---

archive/issue_comments_054843.json:
```json
{
    "body": "Does the new cliquer spkg not use scons anymore? If so, is deps updated to not depend on cliquer? Just curious.",
    "created_at": "2009-10-04T02:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54843",
    "user": "https://github.com/rlmill"
}
```

Does the new cliquer spkg not use scons anymore? If so, is deps updated to not depend on cliquer? Just curious.



---

archive/issue_comments_054844.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-05T03:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6681#issuecomment-54844",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_006916.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-05T03:01:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6681",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6681#event-6916"
}
```
