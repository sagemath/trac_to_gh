# Issue 6595: 'modified sage library code' fails at c_lib if /opt/SUNWspro/bin/CC can be found. (SCons issue)

Issue created by migration from https://trac.sagemath.org/ticket/6595

Original creator: drkirkby

Original creation time: 2009-07-23 07:27:40

Assignee: tbd

CC:  was david.kirkby@onetel.net

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





---

Comment by drkirkby created at 2009-10-19 08:50:31

It was suggested on sage-devel that removing the SCons build process and using a makefile might be better. Is this agreed by William? If so, I'll so it. SCons seems to cause countless problems in Sage.


---

Comment by drkirkby created at 2009-12-16 19:54:20

Changing priority from major to blocker.


---

Comment by drkirkby created at 2009-12-16 19:54:20

I'm changing this to a blocker for 4.3.1, as William is keen that Sage builds on Solaris asap, and this is the one remaining issue which prevents a clean build. It's also code written by Sage developers. 

I've looked at this and can't sort it out. Perhaps a fresh pair of eyes can. 

Dave


---

Comment by was created at 2009-12-17 01:07:41

Hi Dave,

Thanks.  Could you tell me *exactly* how -- using hardware I have access to (either on skynet, on t2, etc.) -- I can replicate the above?   Then maybe I'll fix it!

William


---

Comment by drkirkby created at 2009-12-17 01:49:30

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


note, if you try to run the Sun C or C++ compilers, you will find they do *not* work, since they are not in your path. 


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

Comment by drkirkby created at 2009-12-17 02:27:14

A few notes. 

 * Essentially this boils down to one thing - the library code should be made to honor the settings of CC and CXX, and not pick compilers at random. Since I'd not specifically set CC or CXX, then the Sage build environment will set them to gcc and g++. (I do not know for certain if this code honors the setting of CC or not, but it certainly does not honor CXX). 

 * By default, when Sun Studio is installed, it will create links so cc and CC are in /usr/bin, and so always in your path. So hacking SCons to remove /opt/SUNWspro/bin will not work for most installations of Sun Studio. In any case, that is not the way to right solve the problem. 

 * There are numerous packages in Sage which do not honor the values of CC and CXX, but just use gcc and g++. That is annoying, but not a fatal flaw, as they build as long as the first gcc and g++ in your path are suitable. This is more serious. 

 * There is a mixture of Sun (-KPIC) and GNU (-fPIC) compiler flags, but that should not be a fatal error, as unknown flags are ignored. 

 * I get the same problem on any SPARC I've tried this on, irrespective of the version of Sun Studio - other versions are installed in other paths. 


Dave


---

Comment by was created at 2009-12-19 07:20:37

Thank you!


---

Comment by was created at 2009-12-23 01:22:28

Wow.  I fixed the first bug that the Sun compiler finds (which doesn't matter), and it next found two more similar issues -- which in fact *are* both major bugs.   See attached patch.


---

Attachment

This one patch (sagelib_6595.patch) makes it so at least c_lib builds fine using CC... by fixing at least two potentially *major* bugs in c_lib.  Here's to porting/portability/multiple compilers/not ignoring warnings, etc!  And to Kirkby's persistence.


---

Comment by was created at 2009-12-23 01:24:50

Changing status from new to needs_review.


---

Comment by drkirkby created at 2009-12-23 02:13:49

Great you have found those problems. The Sun compiler is quite fussy, which annoys some, but does show up bugs that other compilers ignore. 

However, building the Sage library with 'CC' will *not* produce a workable Sage, as the Sun and GNU C++ compilers use different name mangling. We must get this to build with g++. Hence hte library it must be made to respect CC and CXX. 

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
}}} 

That's portable across all platforms now, and will be into the future.

-----------

Or the toolchain you pass to the Environment when you set it up:
{{{
     if os.environ['CC'].contains('gcc'):
         toolchain = ['gcc', 'g++', 'gnulink']
     else:
         toolchain = ['suncc', 'sunc++', 'sunlink']
     env = Environment(tools = [toolchain, 'other', 'tools'])
}}}
--------


---

Comment by was created at 2009-12-23 02:32:16

Hi, 

Of course building with sun's CC didn't work.  So while you posted the above, I randomly happened to track down exactly the same email and implement it.  I use os.environ['CC'].endswith('gcc') instead of contains, because the path could be something weird like /home/fredgcc/bar/compilers/net/CC.   I'll be posted a part 2 patch in a moment, which I hope you'll referee.


---

Comment by drkirkby created at 2009-12-23 15:58:40

Changing status from needs_review to positive_review.


---

Attachment

My 'sage -upgrade' seems to have hit a problem, as this library is built twice. The first time it builds fine, with no warnings g++. 

The second time it has the same issues as before - same warning, from the Sun compiler 'CC'. I can only assume something is a bit messed up here. It's clearly patched ok, but I must have left-over code being built. 

Note however, there is no -Wall option, so we wont catch many warnings from gcc/g++. It might be worth adding that at some point in the future, given you have noticed two serious bugs in what is a relatively small amount of code. But I don't know how to enable the warnings with SCons. 

I looked at your changes to the C and C++ code, and they look fine. I don't fully understand what that code is supposed to do, but clearly computing an answer, then not bothering to return it was rather obviously a mistake, which should have been caught with a compiler warning. 

Luckily the Sun compiler was not so forgiving as g++, so allowed those errors to be found. 

Dave


---

Comment by was created at 2009-12-24 07:12:59

Resolution: fixed


---

Comment by was created at 2009-12-24 07:12:59

merged into 4.3.rc2.


---

Comment by was created at 2009-12-24 17:36:50

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

Comment by was created at 2009-12-24 17:36:50

Changing status from closed to needs_work.


---

Comment by was created at 2009-12-24 17:42:27

> This patch breaks building Sage on OS X.

It breaks on OS X <= 10.5, not on 10.6.   Also, the problem is only the part2 patch.  The first patch with the genuine bug fixes is fine.


---

Comment by drkirkby created at 2009-12-24 18:02:05

That's very annoying, but one of those things I guess. Perhaps this bit of code needs to be Solaris-specific. Back to the drawing board.


---

Comment by was created at 2009-12-24 20:42:45

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

Comment by drkirkby created at 2009-12-24 22:23:40

Does that mean it gets to 4.3 then, or do we still have to wait for 4.3.1? 

I'm happy to give your fix a positive review if you want to change it from 'needs work' to 'needs review'. That fix can only affect Solaris. 


Dave


---

Comment by drkirkby created at 2009-12-26 16:20:55

I've created a revised version of William's patch, which will force gcc and g++ on AIX, HP-UX, IRIX, Solaris and Tru64 if the environment variable CXX ends in g++. (I chose CXX rather than CC, as testing for a compiler ending in 'cc' would match gcc as well as 'cc'. Although no such test is actually performed, potentially one might want to check on compilers ending in 'cc'). 

The patch should also handle the cases of where the Sun Studio compiler is used on Linux or Solaris. 

I'll post it once it has been better tested. 

It might be useful to force a compile of c_lib with the Sun C compiler, and see if it finds any defects like the Sun C++ compiler did. The revised patch will allow that. 

Dave


---

Comment by drkirkby created at 2009-12-31 02:56:07

Attaching patch, which should resolve all issues and hopefully not break anywhere. The issue with OS X is apparently one of whether the SHELL is defined or not.


---

Attachment

Revised version of SConstruct for c_lib


---

Comment by drkirkby created at 2009-12-31 02:59:21

Changing status from needs_work to needs_review.


---

Comment by was created at 2009-12-31 19:53:59

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 21:56:45

Merged 6595-SConstruct.patch
