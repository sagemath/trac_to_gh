# Issue 6681: cliquer doesn't work in 64-bit OS X

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-08-06 19:13:39

Assignee: rlm

CC:  ncohen

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



---

Comment by jhpalmieri created at 2009-08-21 05:23:10

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

Comment by mvngu created at 2009-09-13 09:37:47

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

Comment by mvngu created at 2009-09-13 09:43:17

If the updated cliquer package also builds on 64-bit Fedora 10, then #6746 should be closed as a duplicate of this ticket.


---

Comment by jhpalmieri created at 2009-09-13 15:46:09

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

Comment by mvngu created at 2009-09-13 15:58:45

Replying to [comment:5 jhpalmieri]:
>You could also test your cliquer spkg on 4.1.2.alpha0 or 4.1.1.

Compile Sage 4.1.1 successfully from scratch with cliquer-1.2.p0.spkg on OS X 10.5.8 (bsd.math) in 64-bit mode. All tests passed even with the option "-long". Sage loads without problems.




I'm doing more porting work with cliquer as suggested by David Kirkby at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/15c461b1355a8460) thread. So I'm marking this ticket as "needs work".


---

Comment by was created at 2009-09-13 17:56:18


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

Comment by was created at 2009-09-13 18:17:28

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

Comment by mvngu created at 2009-09-16 09:29:24

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

Comment by mvngu created at 2009-09-16 09:29:24

Changing component from graph theory to packages.


---

Comment by mvngu created at 2009-09-16 09:29:24

Changing assignee from rlm to mabshoff.


---

Comment by drkirkby created at 2009-09-16 10:55:39

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

Comment by mvngu created at 2009-09-16 13:11:11

Replying to [comment:11 drkirkby]:
> Hence the end of the spkg-install should be like this:
Done. Updated package is up at the same place:

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg


---

Comment by drkirkby created at 2009-09-16 16:09:46

That looks fine to me now

Dave


---

Comment by jhpalmieri created at 2009-09-16 16:51:23

On 64-bit OS X, when I ran "sage -f cliquer...", I get doctest failures. (32-bit worked fine.)  I'm building from scratch now.  Until that's done, I'm changing this from "positive review" to "needs review"; if it passes tests, I'll restore the positive review.  If not, I'll of course report the failures and mark it as "needs work".

I'm also building from scratch for 32-bit OS X, just to double-check that version.


---

Comment by jhpalmieri created at 2009-09-17 02:42:53

32-bit Mac OS X builds fine and all tests pass.

64-bit Mac OS X builds fine and all tests pass.

Since the summary of the ticket just mentions 64-bit OS X, is this good enough for a positive review, or do we need to doctest on other platforms?  drkirby, when you gave your positive review, what platforms had you doctested it on?


---

Comment by ddrake created at 2009-09-18 00:11:04

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

Comment by mvngu created at 2009-09-18 01:02:28

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

Comment by ddrake created at 2009-09-18 05:27:33

Replying to [comment:17 mvngu]:
> An updated spkg is up at the same place:
> 
> http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg

All my concerns are addressed, and it builds and passes tests on Ubuntu amd64. If drkirkby thinks this is good enough, I say it's fine.


---

Comment by was created at 2009-09-21 02:18:37

Changing priority from major to blocker.


---

Comment by kedlaya created at 2009-09-22 19:06:03

This spkg builds as part of 4.1.2alpha2 and passes all tests on 64-bit Fedora 10.


---

Comment by jhpalmieri created at 2009-09-27 16:04:45

This builds and passes tests on OS X 10.6 (if installed along with the other SPKG's listed at #6849).


---

Comment by jhpalmieri created at 2009-10-01 14:58:05

What needs to be done for this to get a positive review?


---

Comment by mvngu created at 2009-10-01 14:59:49

Replying to [comment:22 jhpalmieri]:
> What needs to be done for this to get a positive review?
Compile Sage with this cliquer package on Solaris (t2.math or any SPARC Solaris machine) using GCC.


---

Comment by jhpalmieri created at 2009-10-01 15:11:05

Does the old cliquer package work on Solaris?  If so, is it possible to combine the two to get something which works on both Solaris and 64-bit Mac OS X?


---

Comment by mvngu created at 2009-10-01 15:25:49

Replying to [comment:24 jhpalmieri]:
> Does the old cliquer package work on Solaris? 
No. The current version of the cliquer spkg that's shipped with Sage uses SCons and so it can fail to build on some 64-bit platforms and t2.math.




> If so, is it possible to combine the two to get something which works on both Solaris and 64-bit Mac OS X?
That's what the updated cliquer package is doing. It removes the need for using SCons to build cliquer and at the same time adds support for building cliquer on the platforms that are known to fail previously. I have built the updated cliquer spkg with Sage 4.1.2.rc0 on t2.math and 64-bit openSUSE 11.1 and it compiled OK. It's just that someone else besides the package author (me) should do the same thing on t2.math to make sure that cliquer builds as I so claim.


---

Comment by rlm created at 2009-10-02 18:05:19

Replying to [comment:25 mvngu]:
> It's just that someone else besides the package author (me) should do the same thing on t2.math to make sure that cliquer builds as I so claim.

I'm doing this now.


---

Comment by was created at 2009-10-04 02:05:05

Hi,

I've merged http://sage.math.washington.edu/home/mvngu/release/spkg/standard/cliquer-1.2.p0.spkg into sage-4.1.2.rc1.spkg.
Minh -- unless something changes you can close this ticket.  It certainly solves the problem "cliquer doesn't work in 64-bit OS X".


---

Comment by rlm created at 2009-10-04 02:38:51

I can verify that the cliquer part of the install worked on t2.


---

Comment by rlm created at 2009-10-04 02:42:13

Does the new cliquer spkg not use scons anymore? If so, is deps updated to not depend on cliquer? Just curious.


---

Comment by was created at 2009-10-05 03:01:34

Resolution: fixed
