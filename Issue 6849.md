# Issue 6849: port Sage to OS X 10.6

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-08-31 01:29:56

Assignee: tbd

CC:  craigcitro drkirkby

Attach to this ticket some of the fixes for getting Sage to build on OS X 10.6 (the new release of OS X).

Note that a Sage build on OS X 10.5 does seem to work fine on 10.6, but Sage does not "just build" on 10.6


---

Comment by was created at 2009-08-31 04:13:17

After readline, the next problem is that R fails to build (at least in 64-bit mode):

```
darwin8/4.2.3/x86_64 -L/Users/wstein/build/sage-4.1.1/local/lib/gcc/i686-apple-darwin8/4.2.3 -L/Users/wstein/build/sage-4.1.1/local/lib/gcc -L/usr/local/lib -lgfortran -lgcc_s.10.4  ../extra/zlib/libz.a ../extr
a/bzip2/libbz2.a ../extra/pcre/libpcre.a  ../extra/intl/libintl.a -liconv  -Wl,-framework -Wl,CoreFoundat
ion -lreadline  -lm
ld: symbol dyld_stub_binding_helper not defined (usually in crt1.o/dylib1.o/bundle1.o)
collect2: ld returned 1 exit status
make[5]: *** [libR.dylib] Error 1make[4]: *** [R] Error 2
make[3]: *** [R] Error 1
make[2]: *** [R] Error 1
Error building R.

real    2m52.365s
user    2m45.681s
sys     0m56.183ssage: An error occurred while installing r-2.6.1.p23
```



---

Comment by was created at 2009-08-31 04:53:25

Next failure is the Boehm GC:

```
 gcc -DPACKAGE_NAME=\"gc\" -DPACKAGE_TARNAME=\"gc\" -DPACKAGE_VERSION=\"7.1\" "-DPACKAGE_STRING=\"gc 7.1\"" -DPACKAGE_BUGREPORT=\"Hans.Boehm`@`hp.com\" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 -DPACKAGE=\"gc\" -DVERSION=\"7.1\" -DGC_DARWIN_THREADS=1 -DTHREAD_LOCAL_ALLOC=1 -DHAS_X86_THREAD_STATE32___EAX=1 -DSTDC_HEA
DERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DH
AVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PER
MISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DL
ARGE_CONFIG=1 -I./include -fexceptions -I libatomic_ops/src -O2 -g -fPIC -m64 -MT atomic_ops.lo -MD -MP -
MF .deps/atomic_ops.Tpo -c atomic_ops.c  -fno-common -DPIC -o .libs/atomic_ops.o
In file included from mach_dep.c:163:
/usr/include/ucontext.h:42:2: error: #error ucontext routines are deprecated, and require _XOPEN_SOURCE t
o be defined
make[3]: *** [mach_dep.lo] Error 1
make[3]: *** Waiting for unfinished jobs....
 gcc -DPACKAGE_NAME=\"gc\" -DPACKAGE_TARNAME=\"gc\" -DPACKAGE_VERSION=\"7.1\" "-DPACKAGE_STRING=\"gc 7.1\
"" -DPACKAGE_BUGREPORT=\"Hans.Boehm`@`hp.com\" -DGC_VERSION_MAJOR=7 -DGC_VERSION_MINOR=1 -DPACKAGE=\"gc\" -
DVERSION=\"7.1\" -DGC_DARWIN_THREADS=1 -DTHREAD_LOCAL_ALLOC=1 -DHAS_X86_THREAD_STATE32___EAX=1 -DSTDC_HEA
DERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DH
AVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DLFCN_H=1 -DNO_EXECUTE_PER
MISSION=1 -DALL_INTERIOR_POINTERS=1 -DGC_GCJ_SUPPORT=1 -DJAVA_FINALIZATION=1 -DATOMIC_UNCOLLECTABLE=1 -DL
ARGE_CONFIG=1 -I./include -fexceptions -I libatomic_ops/src -O2 -g -fPIC -m64 -MT atomic_ops.lo -MD -MP -
MF .deps/atomic_ops.Tpo -c atomic_ops.c -o atomic_ops.o >/dev/null 2>&1
make[2]: *** [all-recursive] Error 1
Error building BoehmGC.

real    0m36.506s
user    0m24.002s
sys     0m20.925s
sage: An error occurred while installing boehm_gc-7.1.p1
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
```



---

Comment by drkirkby created at 2009-08-31 05:21:51

I checked your readline-6.0.spkg on Solaris 10 update 7. It builds fine with both Sun and GNU compilers. But the spkg still suffers from the issue of greping on the Suse file. I've created a new spkg 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/readline-6.0/readline-6.0.spkg

which addresses this, but also does some other things that are not necessarily necessary for readline, but which can be helpful in general, to make a more robust spkg. 

 * Upgrade to 6.0 (latest upstream) - see trac #6849
 * Remove numerous ugly build hacks needed only on OS X for older readline.
 * Track #6844 Made a test for /etc/SuSE-release, as the previous spkg-install
   greped on it, which generates a warning if the file does not
   exist, which it will not on most peoples systems.
 * Added '-m64' to CFLAGS, CXXFLAGS, FFLAGS and F77FLAGS
   if SAGE64 is set to 'yes'. I'm aware it is not necessary to do
   all of these in readline, but its better to stick to something that
   works on all packages.
 * Removes -m64 as a linker flag - no such linker flag exists.
 * Checks CC and CXX are not a mix of GNU and non-GNU compilers.
 * Added -Wall on gcc to show all warnings.
 * Adds -g by default, but it can be removed by setting
   SAGE_DEBUG to something other than 'yes'

You might notice that gcc gives a lot of compiler warnings now I've added -Wall. It's a wonder the package works at all. 

Dave


---

Comment by drkirkby created at 2009-09-16 08:43:24

I've made another improved version of the readline package - see 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/readline-6.0-2nd-try/readline-6.0.spkg

I've made the upgrade of readline a new ticket (Update readline to version 6.0 #6945). 

Dave


---

Comment by was created at 2009-09-20 22:22:08

I've made


---

Comment by jhpalmieri created at 2009-09-26 04:30:14

It seems that the patch from #6883 is needed here to avoid a doctest failure in `sage/interfaces/maxima.py`.  (This is for 10.6 and also 64-bit 10.5.  With 32-bit 10.5, this file passes doctests with or without the patch.)

On 10.6, after building using the spkgs mentioned in the ticket, I have the following other doctest failures:

```
sage -t -long "devel/sage/sage/ext/fast_eval.pyx"           
**********************************************************************
File "/Applications/sage_builds/sage-4.1.2.alpha2-64bit/devel/sage/sage/ext/fast_eval.pyx", line 1080:
    sage: f(0.5)
Expected:
    0.5235987755982989...
Got:
    0.52359877559829882
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_32
***Test Failed*** 1 failures.
For whitespace errors, see the file /Applications/sage_builds/sage-4.1.2.alpha2-64bit/tmp/.doctest_fast_eval.py

sage -t -long "devel/sage/sage/functions/other.py"                
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.

sage -t -long "devel/sage/sage/plot/text.py"                
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.

sage -t -long "devel/sage/sage/rings/polynomial/pbori.pyx"  
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.

sage -t -long "devel/sage/sage/symbolic/constants.py"       
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.

sage -t -long "devel/sage/sage/symbolic/expression.pyx"     
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.

sage -t -long "devel/sage/sage/symbolic/function.pyx"       
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
```

For instance, functions/other.py crashes Sage here:

```
sage: f = factorial(x + factorial(x))
/Applications/sage_builds/sage-4.1.2.alpha2/local/bin/sage-sage: line 199:   5554 Abort trap        sage-ipython "$`@`" -i
```

`sage/symbolic/expression.pyx` crashes on the line `float(SR(RIF(Integer(2))))` with a similar message.  (I'm typing these on one computer while testing on another -- I'm not cut-and-pasting, so apologies for any typos.)

Setting SAGE64 to "yes" resulting in a build with the same doctest failures.  I don't know if setting SAGE64 to "yes" has any actual effect, but it does have cosmetic effects: first, when building a package like readline, without SAGE64, I get the message "Building a 32-bit version of Readline", but the resulting library is 64-bit.  Also, when SAGE64 is set, then compiler flags (for example when building bzip2) include "-m64".  I don't know if these are just cosmetic, or if they have a more serious effect.

On 10.5, using these spkgs, I get some failures with the 32-bit build, but these are known: see [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/954ecbadeb7676a8?tvc=2).

On 10.5, 64-bit build, all tests pass!


---

Attachment

doctest log for bsd.math OS X 10.6


---

Comment by mvngu created at 2009-09-26 23:33:10

doctest log for cicero on SkyNet 32-bit Fedora 9


---

Attachment

Here is John Palmieri's report from [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/e47addca35db2f5f/55d70e14b5c25a0e):

```
> * #6969 boehm_gc-7.1.p2.spkg
> * #6971 ecl-9.8.4-20090913cvs.p1.spkg
> * #7006 mpir-1.2.p6.spkg
> * #6919 flint-1.5.0.p0.spkg
> * #6990 python-2.6.2.p2.spkg
> * #6951 singular-3-1-0-4-20090818.p0.spkg
> * #6758 libgcrypt-1.4.3.p2.spkg
> * #6681 cliquer-1.2.p0.spkg

In an attempt to save time, I attempted to build using all of these at
once (instead of doing one at a time), along with the new fortran spkg
(#6981) and the new r spkg (#6972).  On OS X 10.5, both 32-bit and 64-
bit, building was successful.  After applying the appropriate patches
-- the ones from 6883, 6919, 6972 -- 64-bit: all tests passed.  After
applying these patches to the 32-bit build, same failures as Minh
reported in another thread ("Sage 4.1.2.alpha2 doctest failures on OS
X 10.5.8").

In other words, the packages seem to all look good.  I have not
examined each one to see if the spkg-install files make sense, for
instance, but from the point of view of building and (apparently)
functioning on OS X 10.5, they work.

I don't have the energy to comment on each ticket individually, so
take this as my portion of a positive review for each ticket: on Mac
OS X 10.5, they build properly and seem to work.
```


Here is my report. I compiled Sage 4.1.2.alpha2 from scratch with the following packages:

 * #6972 --- r-2.9.2.spkg
 * #6981 --- fortran-20071120.p8.spkg
 * #6974 --- libgpg_error-1.6.p2.spkg, gnutls-2.2.1.p3.spkg, python_gnutls-1.1.4.p6.spkg, libgcrypt-1.4.3.p2.spkg, opencdk-0.6.6.p1.spkg
 * #6976 --- numpy-1.3.0.p2.spkg
 * #6982 --- atlas-3.8.3.p8.spkg, linbox-1.1.6.p1.spkg
 * #6969 --- boehm_gc-7.1.p2.spkg
 * #6971 --- ecl-9.8.4-20090913cvs.p1.spkg
 * #7006 --- mpir-1.2.p6.spkg
 * #6919 --- flint-1.5.0.p0.spkg
 * #6990 --- python-2.6.2.p2.spkg
 * #6951 --- singular-3-1-0-4-20090818.p0.spkg

The building machines are:

 * bsd.math: x86 Mac OS X 10.6 --- compile: yes; doctest pass: no. Full log is attached.
 * sage.math: x86_64 Ubuntu 8.04.3 LTS --- compile: yes; doctest pass: yes
 * rosemary.math: x86_64 RHEL 5.4 --- compile: yes; doctest pass: yes
 * cicero on SkyNet: x86 Fedora 9 --- compile: yes; doctest pass: no. The failed tests are:
 {{{
sage -t -long "devel/sage/sage/misc/randstate.pyx"
sage -t -long "devel/sage/sage/rings/polynomial/pbori.pyx"
sage -t -long "devel/sage/sage/interfaces/gp.py"
sage -t -long "devel/sage/sage/interfaces/expect.py"
sage -t -long "devel/sage/sage/interfaces/sage0.py"
sage -t -long "devel/sage/sage/crypto/boolean_function.pyx"
sage -t -long "devel/sage/sage/server/simple/twist.py"
 }}}
 which have been reported before to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ff85e2965dc9e59b).
 * eno on SkyNet: x86_64 Fedora 9 --- compile: yes; doctest pass: yes
 * lena on SkyNet: x86_64 RHEL 5.3 --- compile: yes; doctest pass: yes
 * menas on SkyNet: x86_64 openSUSE 11.1 --- compile: yes; doctest: yes

Positive review from me. Any doctest failures are to be fixed in upcoming rc release(s). At the moment, there are so many packages with porting work to Cygwin and OS X 10.6. I'm happy that those packages build OK on Cygwin and OS X 10.6.


---

Comment by was created at 2009-10-02 17:42:57

Changing priority from major to blocker.


---

Comment by was created at 2009-10-14 16:10:33

I'm closing this metaticket.  There is one remaining issue, but that is now at #6849.


---

Comment by was created at 2009-10-14 16:10:33

Resolution: fixed


---

Comment by jason created at 2009-10-14 21:17:17

Replying to [comment:21 was]:
> I'm closing this metaticket.  There is one remaining issue, but that is now at #6849.

This *is* #6849.  Surely you meant another ticket?
