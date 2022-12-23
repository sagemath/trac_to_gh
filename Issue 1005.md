# Issue 1005: Make Sage compile in 32 bit mode on OSX 10.5

Issue created by migration from https://trac.sagemath.org/ticket/1005

Original creator: mabshoff

Original creation time: 2007-10-26 20:43:43

Assignee: mabshoff

Keywords: Leopard




---

Comment by mabshoff created at 2007-10-26 20:44:55

Changing status from new to assigned.


---

Comment by cwitty created at 2007-10-27 03:55:40

When this is fixed, inst/inst.tex should be updated; I just changed that file to say that OS X 10.5 is not yet supported.


---

Comment by was created at 2007-10-29 01:55:39

Some hacks / workarounds:


```
Crazy hacks to get things to build.  Will figure out right fixes once everything
works, etc.

These come from rpw, me, Mabshoff .

1) FLINT (william stein):
Problem -- Multiple symbols... --
Solution:
   comment out this one line 423 of local/include/gmp.h
/* #define __GMP_EXTERN_INLINE      extern __inline__ */

2) PYTHON (rpw):
Python fails to build:
Solution:
I did
   export CFLAGS="-D__DARWIN_UNIX03"
then in src/ manually did this line again after it failed:
gcc -fno-strict-aliasing -Wno-long-double -no-cpp-precomp -mno-fused-madd -DNDEBUG -g -O3 -Wall -Wstrict-prototypes  -I. -I./Include   -DPy_BUILD_CORE  -c ./Modules/posixmodule.c -o Modules/posixmodule.o

Note that putting the above CFLAGS lines in spkg-install at the top or in the ./configure
line did *not* work for some reason.

3) GIVARO (rpw and mabshoff):
Problem: Fails to build.
Solution: Add #include "sys/types.h" to the top of
src/src/kernel/zpz/givzpz32std.inl
src/src/kernel/zpz/givzpz32uns.inl

```



---

Comment by was created at 2007-10-29 02:57:10


```
4) Building clisp fails with 

  UNIX error 45: Operation not supported

SOLUTION: 

   cd spkg/build/clisp-*
   cd src/src
   make
   make install

It works.  The problem is that building tee'ing breaks on 10.5. See
http://osdir.com/ml/apple.fink.tracker/2004-12/msg00149.html
```



---

Comment by was created at 2007-10-29 03:00:10


```
5) MAXIMA:

Solution: Exactly the same as for clisp.  This works.
```



---

Comment by was created at 2007-10-29 03:14:24

Other broken packages:

```
lcalc -- fails
flintqs -- fails
scipy -- fails (looks easy to fix)
```


Everything else builds and Sage starts up.


---

Comment by was created at 2007-10-29 05:44:31

6) LCALC:

The fix for lcalc is to change the line

```
cp lcalc* "$SAGE_LOCAL"/bin
```

in spkg-install to 

```
cp lcalc "$SAGE_LOCAL"/bin
```


The former was needed when we supported windows (e.g., lcalc.exe), and
was sort of hack-ish.  The latter works around that there is some 
small problem with strip on os x, which isn't an issue. 

 -- William


---

Comment by was created at 2007-10-29 05:55:39

7) FLINTQS:

The fix for flintqs is the same as for givaro, basically.
To the file

```
    src/lanczos.c
```

add the following as the first line:

```
#include "sys/types.h"
```

Then it builds fine.


---

Comment by was created at 2007-10-29 07:10:45

8) SCIPY

The final build problem was with Scipy.  There is a problem with g95 not working correctly to build some of scipy on 10.5.  Fortunately, using gfortran instead *does* work.  So I installed a system-wide gfortran in /usr/local/bin/, then did

```
   export SAGE_FORTRAN=`which gfortran`
   cd SAGE_ROOT
   rm spkg/installed/fortran*
   sage -f fortran-20070912
   make
```

and the rest of the build completed fine.


---

Comment by mabshoff created at 2007-10-29 07:47:33

Replying to [ticket:1005 mabshoff]:
> NOTES:  The remarks below are enough to get Sage to 100% build on OSX 10.5.
> 
> 
> 
> Doctesting the tutorial results in a bunch of error messages like this:
> {{{
> python(15525) malloc: *** error for object 0xa023c6d8: Non-aligned pointer being freed
> *** set a breakpoint in malloc_error_break to debug
> }}}

Check out https://lists.ubuntu.com/archives/storm/2007-July/000035.html for some pointers how this might be resolved.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-29 08:18:10

There are two potential patches to try out to fix the non-aligned pointer issue:

http://groups.google.com/group/sage-devel/attach/64e42ec65e8a9fa2/no-collect-integer.patch?part=2

http://groups.google.com/group/sage-devel/attach/3cd7a66aa5c1a355/__Pyx_ImportModule-decref-fix.patch?part=2

Both are from Robert Bradshaw, they should get rolled into 2.8.11, so I will open a ticket for them once I get some feedback from Robert.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-29 08:57:17

Pointers toward a potential solution for the flint problem with gmp at link time can be found at 

http://lists.apple.com/archives/darwin-dev/2006/Oct/msg00015.html

Cheers,

Michael


---

Comment by was created at 2007-10-29 17:38:33

NOTE: A binary built on 10.5 will *not* work on 10.4.


---

Comment by was created at 2007-10-29 21:20:26

I've posted a pre-built version of Sage that was built on Leopard here:

http://sagemath.org/SAGEbin/apple_osx/intel/leopard/

This might be the optimal version of Sage to use on OSX 10.5.  It 
probably won't 100% work without gfortran installed though.


---

Comment by was created at 2007-10-31 21:04:07

I just tried making some matplotlib plots using athe sage I built on 10.5.  I get lots of *serious* problems.  Nothing works.  This may be very difficult to resolve; I don't know.   This happens both in the notebook and from the command line.


```
sage: P = point( (0,0) )
sage: show( P )
python(5144) malloc: *** error for object 0xa023c6d8: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
python(5144) malloc: *** error for object 0xa023c6d8: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
python(5144) malloc: *** error for object 0xa023c6d8: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
python(5144) malloc: *** error for object 0xa023c6d8: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
python(5144) malloc: *** error for object 0xa023c6d8: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
python(5144) malloc: *** error for object 0xa023c6d8: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
python(5144) malloc: *** error for object 0xa023c6d8: Non-aligned pointer being freed
*** set a breakpoint in malloc_error_break to debug
```


NOTE: Using sage-2.8.9 that I built on OS X 10.4 the above problem does not occur.


---

Comment by was created at 2007-11-01 06:21:55

*READLINE in GP doesn't work*

Yet another problem:


```
sage: !gp
                       GP/PARI CALCULATOR Version 2.3.2 (released)
               i386 running darwin (ix86/GMP-4.2.1 kernel) 32-bit version
                compiled: Oct 31 2007, gcc-4.0.1 (Apple Inc. build 5465)
                   (readline not compiled in, extended help available)
                             ^^^^^^^^^^^^^^^
```



---

Comment by was created at 2007-11-01 06:22:16

Changing component from distribution to memleak.


---

Comment by was created at 2007-11-01 06:22:33

Changing component from memleak to porting.


---

Comment by was created at 2007-11-01 07:23:32

Replying to [comment:15 was]:
> I just tried making some matplotlib plots using athe sage I built on 10.5.  
> I get lots of *serious* problems.  

I think this was a result of something involving #1044; I've tested
again and I can't replicate this problem at all.  So never mind -- matplotlib is fine :-).


---

Comment by was created at 2007-11-01 16:51:56

From rpw:

```
Ralf-Philipp Weinmann 	
to Jean-Guillaume., sage-devel
	
show details
	 7:21 am (2 hours ago) 
Dear Dr. Dumas,

I've encountered a build problem in Givaro 3.2.6 on MacOS X 10.5. The
uint type used in src/kernel/zpz/givzpz32std.inl for example is not
available unless sys/types.h is included. The following patch fixes
the problem for me:

--- src/kernel/system/givbasictype.h.ORIG       2007-11-01
15:17:57.000000000 +0100
+++ src/kernel/system/givbasictype.h    2007-11-01 15:18:33.000000000 +0100
@@ -11,6 +11,9 @@
 #include "givaro/givconfig.h"

 #include <stdlib.h> // for size_t
+#ifdef MACOSX
+#  include <sys/types.h> // needed on MacOS X 10.5 for uint type
+#endif

 // -- Neutral type: definition of zero and one
 class Neutral {
```



---

Comment by mabshoff created at 2007-11-01 23:54:40

The givaro issue has been fixed in givaro-3.2.6.p2 for 2.8.11.rc1

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-02 00:43:59

The lcalc issue has been fixed in lcalc-20070107.p0.spkg

Cheers,

Michael


---

Comment by was created at 2007-11-02 00:46:55

I've posted a patched python spkg here:

http://sage.math.washington.edu/tmp/python-2.5.1.p8.spkg


---

Comment by was created at 2007-11-02 03:23:17

I'm posting spkgs here:

http://sage.math.washington.edu/tmp/leopard/


---

Comment by mabshoff created at 2007-11-03 12:13:45

All the above spkgs have been merged in 2.8.11. The only open issue now is that g95 miscompiles scipy and we need to figure out what to do about this. A binary of gfortran 4.2.2 is 19mb compressed, so that is not the solution.

Cheers,

Michael


---

Comment by was created at 2007-11-20 05:11:57


```
Hi,

I just did a test and using the new version of g95 here:
    http://ftp.g95.org/g95-x86-osx.tgz
works fine for building Sage on Leopard OS X 10.5 intel.  
So, we can just update that and stop worrying about require
gfortran on that platform.  Very nice. 

 -- Wiliam

```



---

Comment by mabshoff created at 2007-11-20 11:34:26

Resolution: fixed


---

Comment by mabshoff created at 2007-11-20 11:34:26

The new fortran.spkg at 

http://sage.math.washington.edu/home/mabshoff/fortran-20071120.spkg

fixes the last known issue.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-20 11:36:21

2.8.13.rc0 builds "out of the box" on bsd.

Cheers,

Michael
