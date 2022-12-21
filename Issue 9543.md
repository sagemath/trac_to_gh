# Issue 9543: Enable cephes on FreeBSD

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2010-07-18 19:57:13

Assignee: pjeremy

CC:  mhansen jpflori

FreeBSD does not currently have a full C99 libm and therefore also needs cephes.  The attached patch enables cephes on FreeBSD, removes a reference to a non-existent test package and enables error checking.  The latter two components are needed on Cygwin as well as FreeBSD.


---

Comment by mhansen created at 2010-10-12 01:03:08

I made an spkg at http://sage.math.washington.edu/home/mhansen/cephes-2.8.p0.spkg , but I get the following build error on Cygwin:


```

 /usr/lib/gcc/i686-pc-cygwin/4.3.4/collect2.exe -tsaware --wrap _Znwj --wrap _Znaj --wrap _ZdlPv --wrap _ZdaPv --wrap _ZnwjRKSt9nothrow_t --wrap _ZnajRKSt9nothrow_t --wrap _ZdlPvRKSt9nothrow_t --wrap _ZdaPvRKSt9nothrow_t -Bdynamic --dll-search-prefix=cyg -u ___register_frame_info -u ___deregister_frame_info -o mtst.exe /usr/lib/gcc/i686-pc-cygwin/4.3.4/../../../crt0.o /usr/lib/gcc/i686-pc-cygwin/4.3.4/crtbegin.o -L/home/mhansen/sage-4.5.3.alpha2/local/lib -L/home/mhansen/sage-4.5.3.alpha2/local/lib -L/usr/lib/gcc/i686-pc-cygwin/4.3.4 -L/usr/lib/gcc/i686-pc-cygwin/4.3.4 -L/usr/lib/gcc/i686-pc-cygwin/4.3.4/../../.. mtst.o cmplx.o clog.o cgamma.o stubs.o -lm -lgcc_s -lgcc -lgcc_eh -lcygwin -luser32 -lkernel32 -ladvapi32 -lshell32 -lgcc_s -lgcc -lgcc_eh /usr/lib/gcc/i686-pc-cygwin/4.3.4/crtend.o
gcc  -I. -g -O2 -Wall   -c -o cvect.o cvect.c
cvect.c: In function ‘main’:
cvect.c:130: warning: implicit declaration of function ‘memcmp’
cvect.c:223: warning: implicit declaration of function ‘exit’
cvect.c:223: warning: incompatible implicit declaration of built-in function ‘exit’
gcc -o cvect cvect.o clog.o cmplx.o stubs.o -lm
gcc  -I. -g -O2 -Wall -c dccalc.c
gcc -o dccalc dccalc.o libmc.a stubs.o -lm
gcc  -I. -g -O2 -Wall   -c -o mtstf.o mtstf.c
gcc -o mtstf mtstf.o cmplxf.o clogf.o cgammaf.o stubs.o -lm
make: *** No rule to make target `whitebxf.c', needed by `whitebxf.o'.  Stop.
```



---

Comment by pjeremy created at 2010-10-13 21:32:04

The patches I added do not affect the build on Cygwin and I get exactly the same failure when building cephes-2.8.spkg (without any of my patches) on Cygwin.  As I noted in my initial description, some of the cephes self-tests have been removed - whitebxf.c being one such.


---

Comment by jdemeyer created at 2012-01-24 14:24:31

Note that patches should now be applied by using `patch` instead of `cp`.

Also, it would be really nice to make it more uniform: when possible, use the same patches both for Cygwin and for FreeBSD.


---

Comment by kcrisman created at 2012-01-24 14:32:21

Replying to [comment:4 jdemeyer]:
> Note that patches should now be applied by using `patch` instead of `cp`.
> 
> Also, it would be really nice to make it more uniform: when possible, use the same patches both for Cygwin and for FreeBSD.
Of course, though with Cygwin development halted for a bit that may not be as crucial.


---

Comment by kcrisman created at 2012-01-31 01:58:57

With respect to this patch right now, according to Stephen Montgomery-Smith, "It caused build errors in other sub-packages."  However, it does seem that cephes is needed for ccosh and who knows what else.


---

Comment by kcrisman created at 2012-01-31 01:59:12

See [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/2feec7c5511c4ae5/857a00a9aa271f17).


---

Comment by stephen created at 2012-04-14 03:30:57

I could not get pjeremy's patch to work for FreeBSD.  After some searching, I found out that the problem is that his patch attempts to link the cephes functions with /lib/libm.so.  This is something that is not meant to work for dynamic libraries.  Once a dynamic library has been created, apparently there is no mechanism for merging it with other dynamic libraries.

My solution was to slightly modify pjeremy's patch so that it creates a library libm_complex.so.  The following patch should be applied to pjeremy's patch:


```
--- cephes-2.8	2012-04-14 01:39:13.000000000 +0000
+++ cephes-2.8	2012-04-14 01:38:51.000000000 +0000
`@``@` -1273,11 +1273,11 `@``@`
 +# Intermediate (ar) libraries
 +LIBS=c9x-complex/libmc.a double/libmd.a ldouble/libml.a single/libmf.a
 +
-+all: libm.so
++all: libm_complex.so
 +
-+install: libm.so complex.h math.h
++install: libm_complex.so complex.h math.h
 +	${INSTALL} -C -m 644 complex.h math.h "${SAGE_LOCAL}/include"
-+	${INSTALL} -C -m 755 libm.so "${SAGE_LOCAL}/lib"
++	${INSTALL} -C -m 755 libm_complex.so "${SAGE_LOCAL}/lib"
 +
 +check:
 +	cd c9x-complex && ${MAKE} "CC=${CC}" check
`@``@` -1291,7 +1291,7 `@``@`
 +#	TBD
 +
 +clean:
-+	rm -f libm.so syms.c99 syms.libm syms.wanted
++	rm -f libm_complex.so syms.c99 syms.libm syms.wanted
 +	cd c9x-complex && ${MAKE} clean
 +	cd double && ${MAKE} clean
 +	cd ldouble && ${MAKE} clean
`@``@` -1300,8 +1300,8 `@``@`
 +# FreeBSD includes some but not all of the C99 maths functions.  Build
 +# a "new" libm.so that uses cephes functions to replace the missing ones
 +# (listed in syms.wanted) and then fallback to the base libm.so
-+libm.so: ${LIBS} syms.wanted
-+	${LD} -shared -o $`@` $$(sed 's/^/-u /' syms.wanted) -L/usr/lib -lc -lm \
++libm_complex.so: ${LIBS} syms.wanted
++	${LD} -shared -o $`@` $$(sed 's/^/-u /' syms.wanted) -L/usr/lib \
 +	   ${LIBS} -lgcc
 +
 +# List of symbols defined in the FreeBSD base libc.so and libm.so
```


Then I put a script in $SAGE_ROOT/local/bin called "cc" which is a wrapper around the cc I really want to use:

{{{#!/usr/local/bin/bash

# Intersperse a "-lm_complex" before "-lm".

n=0
for i in "$`@`"; do
  if [ "x$i" = "x-lm" ]; then
    arg[$n]="-lm_complex"
    n=$((n+1))
    arg[$n]="-lm"
  else
    arg[$n]="$i"
  fi
  n=$((n+1))
done

# Some configure scripts invoke the compiler with the argument "-v", and if
# LDFLAGS are added to the arguments, this results in an error which
# ultimately stops the relevant package being built.

# Otherwise LDFLAGS needs to be added so that the linker knows where to find
# the dynamic libraries.

if [ $n = 1 -a "x${arg[0]}" = "x-v" ]; then
  exec /usr/local/bin/gcc46 "${arg[`@`]}"
else
  exec /usr/local/bin/gcc46 -Wl,-rpath=$SAGE_ROOT/local/lib  -Wl,-rpath=/usr/local/lib/gcc46 "${arg[`@`]}"
fi
```



---

Comment by jdemeyer created at 2012-04-14 09:03:33

Replying to [comment:8 stephen]:
> I could not get pjeremy's patch to work for FreeBSD.  After some searching, I found out that the problem is that his patch attempts to link the cephes functions with /lib/libm.so.  This is something that is not meant to work for dynamic libraries.
Are you sure about this?  Couldn't you link Cephes's `libm` against the system `-lm` (maybe you would have to rename the latter).

I'm willing to experiment with this if somebody could give me access to a FreeBSD box.


---

Comment by stephen created at 2012-04-14 12:34:54

Replying to [comment:9 jdemeyer]:
> Replying to [comment:8 stephen]:
> > I could not get pjeremy's patch to work for FreeBSD.  After some searching, I found out that the problem is that his patch attempts to link the cephes functions with /lib/libm.so.  This is something that is not meant to work for dynamic libraries.
> Are you sure about this?  Couldn't you link Cephes's `libm` against the system `-lm` (maybe you would have to rename the latter).
> 
> I'm willing to experiment with this if somebody could give me access to a FreeBSD box.

No I am not sure about this.  I received a private email from pjeremy, and did some more investigating.  I discovered his patch doesn't work when I use the *gcc46 compiler*, which comes with the FreeBSD ports system, and is automatically invoked when you use fortran.

Let me think some more about this.


---

Comment by stephen created at 2012-04-14 17:12:46

Replying to [comment:10 stephen]:

> No I am not sure about this.  I received a private email from pjeremy, and did some more investigating.  I discovered his patch doesn't work when I use the *gcc46 compiler*, which comes with the FreeBSD ports system, and is automatically invoked when you use fortran.
> 
> Let me think some more about this.

It looks like I found the problem.  I was building under a chroot'ed environment.  I have discovered that after I perform the 

```
chroot /usr/jail
```

I need to do

```
sh /etc/rc.d/ldconfig start
```

It looks like I only need to do this one time.

Thanks for sticking with me on this guys.  It looks like pjeremy's patch works, as is, with no changes.


---

Comment by kcrisman created at 2012-06-20 19:19:49

Great, we just have to make a new spkg for this.  Probably we should change to patches instead of entire files copied over, though these are all new files so it's not as big of an issue.


---

Comment by kcrisman created at 2012-12-18 16:54:06

On #13806 [this message](http://freebsd.1045724.n5.nabble.com/Use-of-C99-extra-long-double-math-functions-after-r236148-td5712748.html) came up.  Relevant?  Sorry that we still haven't made an spkg for this...


---

Comment by jpflori created at 2012-12-19 10:56:57

Spkg cleanup and only targetting FreeBSD at
http://boxen.math.washington.edu/home/jpflori/cephes-2.8.p0.spkg


---

Comment by kcrisman created at 2013-01-04 15:32:59

Trivial error

```
if [ "$UNAME" != "FreeBSD" ]; then 
    echo "We only install the cephes library on Cygwin and FreeBSD." 
    exit 0 
fi
```

Anyway, I'm trying this on Cygwin now.


---

Comment by stephen created at 2013-01-04 16:52:35

Regarding testing the cephes library - I don't think it is fair to
expect them to give super accurate answers.  I believe that the linux
library functions will fail in the same way.  Same with OpenBSD.

I have been working with the FreeBSD people to get the C99 math
functions into FreeBSD.  They are remarkably fussy.  I have been working
on the complex arc-trig functions casin(h), cacos(h), catan(h), and I
have written some extremely well tested and verified code which is
listed here: http://www.math.missouri.edu/~stephen/software/#catrig

Nevertheless they still won't commit my programs until I have made some
style corrections, and I don't have time right now to do this.

The only other package I know of that implements these functions well
are the boost libraries.  And even those were buggy (my bug fixes were
recently accepted by them).

Another person is working on clog.  The real part of clog(z) is
particularly hard to implement in the case that |z| is close to one.

The linux and OpenBSD libraries totally disregard the issues that give
rise to the huge errors.

And for casinh and cacosh, even the mpc libraries are badly written in
that their only saving grace is that they keep increasing the number of
internal digits until they are sure that their answer is correct.  (If
you wanted something like 200 bits of accuracy for cacosh, some inputs
can take minutes to compute.)

Anyway, all this is to say that you shouldn't hold the cephes libraries
up to any kind of high standard.  Treat them as work arounds so that
ccosh and such like will actually be compiled into sage on FreeBSD,
rather that the answers should be particularly accurate.


---

Comment by kcrisman created at 2013-01-04 17:09:59

Replying to [comment:17 stephen]:
> Regarding testing the cephes library - I don't think it is fair to
> expect them to give super accurate answers.  I believe that the linux
> library functions will fail in the same way.  Same with OpenBSD.
I'm not sure anyone was suggesting doing this, just to at least _provide_ such functions on Cygwin.
> Anyway, all this is to say that you shouldn't hold the cephes libraries
> up to any kind of high standard.  Treat them as work arounds so that
> ccosh and such like will actually be compiled into sage on FreeBSD,
> rather that the answers should be particularly accurate.
Hopefully that is all we are asking for!  I'm going to change the description to point out that we really just want this.

----

So... would you mind checking (at your convenience) whether this spkg indeed does the same thing as the patches from before and at [your port](http://www.freebsd.org/cgi/cvsweb.cgi/ports/math/sage/files/spkg-patch-cephes_-_big-patch)?  Then if it works on Cygwin (i.e., if Cygwin doesn't need it) we can merge this and simplify things slightly.


---

Comment by kcrisman created at 2013-01-04 17:09:59

Changing status from new to needs_review.


---

Comment by stephen created at 2013-01-04 20:43:11

This new spkg failed to build rather early in the process:



```
Found package cephes-2.8.p0 in spkg/standard/cephes-2.8.p0.spkg
cephes-2.8.p0
====================================================
Extracting package /usr/home/stephen/sage-devel/work/sage-5.6.beta2/spkg/standard/cephes-2.8.p0.spkg
-rw-r--r--  1 stephen  staff  2514467 Jan  4 20:36 /usr/home/stephen/sage-devel/work/sage-5.6.beta2/spkg/standard/cephes-2.8.p0.spkg
Finished extraction
****************************************************
Host system:
FreeBSD wilberforce 8.3-STABLE FreeBSD 8.3-STABLE #0: Wed Jan  2 15:53:46 CST 2013     root`@`wilberforce:/usr/obj/usr/src/sys/GENERIC  amd64
****************************************************
C compiler: gcc
C compiler version:
Using built-in specs.
COLLECT_GCC=/usr/local/bin/gcc46
COLLECT_LTO_WRAPPER=/usr/local/libexec/gcc46/gcc/x86_64-portbld-freebsd8.3/4.6.3/lto-wrapper
Target: x86_64-portbld-freebsd8.3
Configured with: ./../gcc-4.6.3/configure --disable-bootstrap --disable-nls --libdir=/usr/local/lib/gcc46 --libexecdir=/usr/local/libexec/gcc46 --program-suffix=46 --with-as=/usr/local/bin/as --with-gmp=/usr/local --with-gxx-include-dir=/usr/local/lib/gcc46/include/c++/ --with-ld=/usr/local/bin/ld --with-libiconv-prefix=/usr/local --with-pkgversion='FreeBSD Ports Collection' --with-system-zlib --enable-languages=c,c++,objc,fortran,java --prefix=/usr/local --mandir=/usr/local/man --infodir=/usr/local/info/gcc46 --build=x86_64-portbld-freebsd8.3
Thread model: posix
gcc version 4.6.3 (FreeBSD Ports Collection)
****************************************************
Applying patches (if any)...
patching file c9x-complex/cgamma.c
patching file c9x-complex/cgammaf.c
patching file c9x-complex/cgammal.c
patching file c9x-complex/makefile
patching file double/makefile
patching file ldouble/gammal.c
patching file ldouble/makefile
patching file Makefile
./spkg-install: line 21: check_error: command not found
Building Cephes...
make[3]: Entering directory `/usr/home/stephen/sage-devel/work/sage-5.6.beta2/spkg/build/cephes-2.8.p0/src'
make[3]: *** No rule to make target `../patches/complex_bsd.h', needed by `c9x-complex/complex.h'.  Stop.
make[3]: Leaving directory `/usr/home/stephen/sage-devel/work/sage-5.6.beta2/spkg/build/cephes-2.8.p0/src'
Error - Failed to build Cephes ... exiting

real    0m0.025s
user    0m0.002s
sys     0m0.013s
************************************************************************
Error installing package cephes-2.8.p0
************************************************************************
```



---

Comment by kcrisman created at 2013-01-04 20:52:50

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2013-01-04 20:52:50


```
./spkg-install: line 21: check_error: command not found
```

JP, I think you might have used that command from a different spkg we've been working on.  So that's two things... and then the third is that the `complex_bsd.h` is completely missing from pjeremy's patch to yours.
----
Still waiting on Cygwin, probably will hear back Monday since I'm using `SAGE_CHECK`.


---

Comment by kcrisman created at 2013-01-07 14:46:25

Cygwin is fine, unsurprisingly, though of course the message is a little funny

```
...
gcc version 4.5.3 (GCC)
We only install the cephes library on Cygwin and FreeBSD.

real ...
user ...
sys ...
Successfully installed cephes-2.8.p0
...
```



---

Comment by jpflori created at 2013-01-07 15:12:31

I've upped a new spkg which:
* fixes the exit message,
* fixes the use of check_error,
* does not add math_bsd or complex_bsd as pjeremy's patch did not lead to their creation or installation, the bsd.patch and spkg-install I've produced should replicate the behavior of what you get with pjeremy's patch.


---

Comment by jpflori created at 2013-01-07 15:12:31

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2013-01-07 15:12:31

Changing keywords from "" to "cephes spkg cygwin freebsd".


---

Comment by kcrisman created at 2013-01-07 15:19:58

This is fine from my point of view.  If Stephen can check whether it performs as promised then we'll be set.


---

Comment by jpflori created at 2013-01-07 15:23:34

Replying to [comment:23 kcrisman]:
> This is fine from my point of view.  If Stephen can check whether it performs as promised then we'll be set.
Agreed!

Quite strangely, I don't have access to a FreeBSD box :) (although I vaguely remember trying to setup one once)


---

Comment by stephen created at 2013-01-07 20:28:13

It still fails with the "complex_bsd.h" no rule message.

I looked at Jeremy's patch, and it seemed to me that it did create math_bsd.h and complex_bsd.h.  For example, it has lines like this:


```
--- cephes-2.8/patches/complex_bsd.h.orig       2010-07-26 08:25:54.654310990 +1000
+++ cephes-2.8/patches/complex_bsd.h    2010-07-26 08:25:54.658310309 +1000
```


This is a diff against a non-existent file, using the "-N" option to diff.  The patch program creates a new file.

Makefile then copies this from cephes-2.8/patches to where-ever it is needed.  I would probably change the patch so that it is created directly in the directory where it is needed.


---

Comment by stephen created at 2013-01-07 20:29:56

Oh, and the reason it worked so well with cygwin is because it didn't do anything.


---

Comment by kcrisman created at 2013-01-07 21:12:11

> Oh, and the reason it worked so well with cygwin is because it didn't do anything.
Yes, understood.


---

Comment by jpflori created at 2013-01-07 22:13:21

Ok, I had a closer look at jeremy's patch and indeed the *_bsd.h file are needed and copied by the new makefile.

I did not create them at first because the bunch of bash functions called on cygwin explicitely copied them whereas on bsd we just have make / make install calls which got me confused.

I'll fix that tomorrow.


---

Attachment

Spkg diff, for review only.


---

Comment by jpflori created at 2013-01-08 14:19:05

Everything is hopefully fine now.

I've slightly modified Jeremy's approach to create (or rather modify as far as complex.h is concerned) the various headers while patching the src dir, rather than overwriting them with Makefile rules.


---

Comment by stephen created at 2013-01-08 23:13:47

The latest version built and worked just fine.


---

Comment by kcrisman created at 2013-01-09 06:22:59

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-01-09 06:22:59

And the spkg-install looks good to me.  Assuming that you formed it correctly, this should be good to go in!


---

Comment by jdemeyer created at 2013-01-09 09:04:47

Sorry to be annoying but could you please document _why_ we need cephes on FreeBSD? Preferably something should be mentioned in `SPKG.txt`. In the ticket description I only see
> FreeBSD does not currently have a full C99 libm and therefore also needs cephes
which is very vague.


---

Comment by stephen created at 2013-01-09 13:14:26

FreeBSD's math library does not have all the mathematics functions described in Sections 7.3 and 7.12 of the C99 standard:

```
http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1124.pdf
```

Specifically many of the complex and long double functions are missing in FreeBSD.

Cephes provides those functions that are missing from FreeBSD.  The Makefiles have been modified so that it only adds those functions missing from the version of FreeBSD in which compilation is taking place.


---

Comment by jpflori created at 2013-01-09 15:26:33

New spkg with SPKG.txt including a note with what stephen posted.
As the change is minimal I'm leaving this as positive review.


---

Comment by jpflori created at 2013-01-09 15:26:55

Spkg diff, for review only.


---

Comment by jdemeyer created at 2013-01-12 08:52:00

Resolution: fixed


---

Attachment
