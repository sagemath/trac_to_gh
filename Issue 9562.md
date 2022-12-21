# Issue 9562: Add M4RIE to Sage

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2010-07-21 10:41:53

Assignee: tbd

CC:  mvngu simonking

Keywords: m4ri

M4RIE is a library for linear algebra over small extension of GF(2). It is still in an early stage but already offers performance comparable to Magma for many inputs and is more than 1000 times faster than what we have in Sage right now.


---

Comment by malb created at 2010-07-21 10:43:56

The SPKG is here:

http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100730.spkg


---

Comment by malb created at 2010-07-21 10:45:48

The attached patch depends on #9475


---

Comment by malb created at 2010-07-21 10:50:03

The package compiles on t2. sage-check fails because libstdc++ cannot be found (I believe this is due to a problem in the old Sage I have on t2). I cannot apply my patch against this old version of Sage either.


---

Comment by mhansen created at 2010-07-21 12:24:02

This builds a static library only on Cygwin, but segfaults on both of the tests.


---

Comment by malb created at 2010-07-21 12:43:37

Mike, is there a Sage I can copy on winxp1?


---

Comment by malb created at 2010-07-21 13:20:58


```
sage -t  devel/sage/sage/modular/modsym/space.py # 1 doctests failed
sage -t  devel/sage/sage/misc/sagedoc.py # 3 doctests failed
sage -t  devel/sage/sage/crypto/mq/mpolynomialsystem.py # 19 doctests failed
sage -t  devel/sage/sage/crypto/mq/sr.py # 7 doctests failed
sage -t  devel/sage/sage/modular/modsym/modsym.py # 1 doctests failed
sage -t  devel/sage/sage/rings/polynomial/pbori.pyx # 2 doctests failed
sage -t  devel/sage/sage/crypto/block_cipher/miniaes.py # 72 doctests failed

```



---

Comment by drkirkby created at 2010-07-21 14:40:14

Replying to [comment:4 malb]:
> The package compiles on t2. sage-check fails because libstdc++ cannot be found (I believe this is due to a problem in the old Sage I have on t2). I cannot apply my patch against this old version of Sage either.

There's a Sage 4.5.1 package in /usr/local.


---

Comment by malb created at 2010-07-21 15:33:47

After unpacking that I get


```
     21 from numpy.lib import triu
---> 22 from numpy.linalg import lapack_lite
     23 from numpy.core.defmatrix import matrix_power
     24 

ImportError: ld.so.1: python: fatal: libgfortran.so.3: open failed: No such file or directory
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.

```

Any ideas?


---

Comment by malb created at 2010-07-21 20:49:41

Changing status from new to needs_work.


---

Comment by malb created at 2010-07-21 20:49:41

The updated patch fixes all doctest failures. 

PS: CCing Minh since I'm touching his code in a potentially non-trivial way/


---

Comment by drkirkby created at 2010-07-21 23:09:22

It's not passing the tests properly on 64-bit OpenSolaris, and I doubt anywhere where SAGE64 needs to be set to yes. The -m64 flag is not getting passed when running the tests, so whilst it builds a 64-bit library, it looks like it tries to create 32-bit objects and link to that 64-bit library. 

I have not investigated this in any detail, but they were my initial observations. I would try building on 't2' with SAGE64 set to yes. Not all of Sage will build 64-bit without some hacks, but it should be fairly easy to get enough of Sage built to build this library. 


```
Successfully installed libm4ri-20100730
Running the test suite.
Testing the M4RI library
make -j12  test_elimination test_multiplication
make[1]: Entering directory `/export/home/drkirkby/sage-4.5/spkg/build/libm4ri-20100730/m4rie'
make[1]: warning: -jN forced in submake: disabling jobserver mode.
g++ -DHAVE_CONFIG_H -I. -I./src   -I/export/home/drkirkby/sage-4.5/local/include -m64  -g -O2 -MT test_elimination.o -MD -MP -MF .deps/test_elimination.Tpo -c -o test_elimination.o `test -f 'tests/test_elimination.cc' || echo './'`tests/test_elimination.cc
g++ -DHAVE_CONFIG_H -I. -I./src   -I/export/home/drkirkby/sage-4.5/local/include -m64  -g -O2 -MT test_multiplication.o -MD -MP -MF .deps/test_multiplication.Tpo -c -o test_multiplication.o `test -f 'tests/test_multiplication.cc' || echo './'`tests/test_multiplication.cc
mv -f .deps/test_elimination.Tpo .deps/test_elimination.Po
/bin/sh ./libtool --tag=CXX   --mode=link g++  -g -O2 -lm4rie -lm4ri -lgivaro -lntl -lgmpxx -lgmp -lm -lstdc++  -o test_elimination test_elimination.o  
mv -f .deps/test_multiplication.Tpo .deps/test_multiplication.Po
/bin/sh ./libtool --tag=CXX   --mode=link g++  -g -O2 -lm4rie -lm4ri -lgivaro -lntl -lgmpxx -lgmp -lm -lstdc++  -o test_multiplication test_multiplication.o  
libtool: link: g++ -g -O2 -o .libs/test_elimination test_elimination.o  /export/home/drkirkby/sage-4.5/spkg/build/libm4ri-20100730/m4rie/.libs/libm4rie.so -L/export/home/drkirkby/sage-4.5/local/lib /export/home/drkirkby/sage-4.5/local/lib/libm4ri.so /export/home/drkirkby/sage-4.5/local/lib/libgivaro.so -L/export/home/drkirkby/sage-4.5/local//lib -lntl /export/home/drkirkby/sage-4.5/local/lib/libgmpxx.so /export/home/drkirkby/sage-4.5/local/lib/libgmp.so /usr/local/gcc-4.4.4-multilib/lib/amd64/libstdc++.so -lm -Wl,-R -Wl,/export/home/drkirkby/sage-4.5/local/lib -Wl,-R -Wl,/usr/local/gcc-4.4.4-multilib/lib/amd64
libtool: link: g++ -g -O2 -o .libs/test_multiplication test_multiplication.o  /export/home/drkirkby/sage-4.5/spkg/build/libm4ri-20100730/m4rie/.libs/libm4rie.so -L/export/home/drkirkby/sage-4.5/local/lib /export/home/drkirkby/sage-4.5/local/lib/libm4ri.so /export/home/drkirkby/sage-4.5/local/lib/libgivaro.so -L/export/home/drkirkby/sage-4.5/local//lib -lntl /export/home/drkirkby/sage-4.5/local/lib/libgmpxx.so /export/home/drkirkby/sage-4.5/local/lib/libgmp.so /usr/local/gcc-4.4.4-multilib/lib/amd64/libstdc++.so -lm -Wl,-R -Wl,/export/home/drkirkby/sage-4.5/local/lib -Wl,-R -Wl,/usr/local/gcc-4.4.4-multilib/lib/amd64
ldld::  fatal: filefatal :test_multiplication.o :file  wrong test_elimination.o: wrong ELF class:ELF ELFCLASS64
ld: fatal:  file processing errors.class No:  output ELFCLASS64written 
to .libs/test_multiplication
ld: fatal: file processing errors. No output written to .libs/test_elimination
collect2: ld returned 1 exit status
collect2: ld returned 1 exit status
make[1]: *** [test_multiplication] Error 1
make[1]: *** Waiting for unfinished jobs....
make[1]: *** [test_elimination] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.5/spkg/build/libm4ri-20100730/m4rie'
make: *** [check-am] Error 2
Error testing M4RI
*************************************
Error testing package ** libm4ri-20100730 **
*************************************
sage: An error occurred while testing libm4ri-20100730
```



---

Comment by malb created at 2010-07-21 23:39:13

I updated the SPKG linked above

 * Building shared libraries on Cygwin now
 * Fixed the crashes in spkg-check in Cygwin (this was actually a real bug)
 * Fixed flags for SAGE64


---

Comment by malb created at 2010-07-21 23:39:13

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-07-22 00:08:07

Everything works on my Cygwin install.


---

Comment by drkirkby created at 2010-07-22 00:33:55

It passed all self-tests on 64-bit OpenSolaris (x64) and 64-bit Solaris 10 (SPARC). Since neither platform has a stable version of Sage yet, running the doctests is pointless. 

A few questions:

 * Has there been an agreement to add this library? If so, can you provide a link to it. 
 * Why is it not in another package, rather than added to the libm4ri package? 
 * Do the self tests pass on Linux? 
 * Do the doctests pass on Linux? 
 * Do the self-tests pass on 32-bit SPARC?  (Note my point above about there being a 4.5.1 in /usr/local on t2)
 * Do the doc tests pass on 32-bit SPARC? 
 * Do the self-tests pass on OS X? 
 * Do the doctests pass on OS X?


---

Comment by malb created at 2010-07-22 01:16:42

Replying to [comment:14 drkirkby]:

> A few questions:
> * Has there been an agreement to add this library? If so, can you provide a link to it. 

No decision on [sage-devel] has happened yet. However, the Sage developers here at Sage Days 24 seem to be in favour of adding it.

> * Why is it not in another package, rather than added to the libm4ri package? 

It makes maintaining the thing easier for all sides: I'm the maintainer of both libraries for both upstream and the SPKGs. It isn't even decided yet whether the two libraries might get merged in the future. Finally, William asked me to not add a new SPKG but to add the M4RIe extension to the M4RI package.

> * Do the self tests pass on Linux? 

Yes.

> * Do the doctests pass on Linux? 

Yes.

> * Do the self-tests pass on 32-bit SPARC?  (Note my point above about there being a 4.5.1 in /usr/local on t2)

Note my point above about not being able to use it.

> * Do the doc tests pass on 32-bit SPARC? 

No clue.

> * Do the self-tests pass on OS X? 

Yes.

> * Do the doctests pass on OS X? 

Yes.


---

Comment by drkirkby created at 2010-07-22 07:00:29

Replying to [comment:15 malb]:
> Replying to [comment:14 drkirkby]:
> 
> > A few questions:
> > * Has there been an agreement to add this library? If so, can you provide a link to it. 
> 
> No decision on [sage-devel] has happened yet. However, the Sage developers here at Sage Days 24 seem to be in favour of adding it.

If the packages does get positive review, there should be a note to the release manager(s) not to merge it until there has been an agreement. Though in this case, it looks like getting a vote seems a formality. 
 
> > * Why is it not in another package, rather than added to the libm4ri package? 
> 
> It makes maintaining the thing easier for all sides: I'm the maintainer of both libraries for both upstream and the SPKGs. It isn't even decided yet whether the two libraries might get merged in the future. Finally, William asked me to not add a new SPKG but to add the M4RIe extension to the M4RI package.

One obvious disadvantage of that approach is that since one library relies on the other, the first could be built in parallel with some other packages. That could potentially slow parallel builds. 
 
> > * Do the self tests pass on Linux? 
> 
> Yes.
> 
> > * Do the doctests pass on Linux? 
> 
> Yes.
> 
> > * Do the self-tests pass on 32-bit SPARC?  (Note my point above about there being a 4.5.1 in /usr/local on t2)
> 
> Note my point above about not being able to use it.

Your point above says that's probably because you have an old version. 

But I said above, there is the latest version on there - (`/usr/local/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS.tar.gz` is a pre-built copy of the latest version of Sage on 't2').  If that does not work, let me know - I'd be very surprised if it does not. Otherwise, you could just build Sage from source. 

> > * Do the doc tests pass on 32-bit SPARC? 
> 
> No clue.

See point above. 

Dave


---

Comment by malb created at 2010-07-22 17:09:11

Dave, the testuite fails:


```
/bin/bash ./libtool --tag=CXX   --mode=link g++  -g -O2 -lm4rie -lm4ri -lgivaro -lntl -lgmpxx -lgmp -lm -lstdc++  -o test_elimination test_elimination.o  
libtool: link: warning: library `/home/malb/t2/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/libstdc++.la' was moved.
libtool: link: cannot find the library `/usr/local/gcc-4.4.3/lib/libstdc++.la' or unhandled argument `/usr/local/gcc-4.4.3/lib/libstdc++.la'
make[1]: *** [test_elimination] Error 1
make[1]: Leaving directory `/home/malb/t2/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/spkg/build/libm4ri-20100730/m4rie'

```

Any idea why it wouldn't find libstdc++ on t2?


---

Comment by malb created at 2010-07-22 17:38:02

Changing status from needs_review to needs_work.


---

Comment by malb created at 2010-07-22 21:50:03

These lines:


```
libtool: link: warning: library `/home/malb/t2/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/libstdc++.la' was moved.
libtool: link: cannot find the library `/usr/local/gcc-4.4.3/lib/libstdc++.la' or unhandled argument `/usr/local/gcc-4.4.3/lib/libstdc++.la'

```

make me think it's the Sage binary that is broken?  Why is there be a libstdc++ in the Sage tarball ?


---

Comment by drkirkby created at 2010-07-22 22:30:37

Replying to [comment:19 malb]:
> These lines:
> 
> {{{
> libtool: link: warning: library `/home/malb/t2/sage-4.5.1-Solaris_10_SPARC-sun4u-SunOS/local/lib/libstdc++.la' was moved.
> libtool: link: cannot find the library `/usr/local/gcc-4.4.3/lib/libstdc++.la' or unhandled argument `/usr/local/gcc-4.4.3/lib/libstdc++.la'
> 
> }}}
> make me think it's the Sage binary that is broken?  Why is there be a libstdc++ in the Sage tarball ?

The reason it is there is that the version of gcc shipped with Solaris is 3.4.3, so there are no recent gcc libraries. The compiler is not built with Fortran support, so there is no libgfortran at all. One needs recent run-time libraries, with fortran support, so I added them to the Sage binary. 

It may be that deleting (making a copy first) of those .la files will solve the problem. Otherwise, editing them to point at the location of the libraries in $SAGE_LOCAL/lib will almost certainly solve it. 

If that does not work, just build Sage from source. It does not take too long if you build packages in parallel. 

Dave


---

Comment by malb created at 2010-08-10 13:50:27

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-08-10 13:50:27


```
malb`@`t2:~/t2/sage-4.5.1$ ./sage -t devel/sage/sage/matrix/matrix_mod2_dense.pyx 

sage -t  "devel/sage/sage/matrix/matrix_mod2_dense.pyx"     

         [92.7 s]

 ----------------------------------------------------------------------

All tests passed!

Total time for all tests: 92.8 seconds

malb`@`t2:~/t2/sage-4.5.1$ ./sage -t devel/sage/sage/matrix/matrix_mod2e_dense.pyx 

sage -t  "devel/sage/sage/matrix/matrix_mod2e_dense.pyx"    

         [50.0 s]

----------------------------------------------------------------------

All tests passed!

Total time for all tests: 50.0 seconds


```

After finally building Sage t2 I can confirm that doctests pass there too


---

Comment by drkirkby created at 2010-08-10 14:46:03

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-08-10 14:46:03

It appears to be trying to use autoconf, but autoconf is not a perquisite for Sage. Are you sure the timestamps on all the files are right? 


```
checking for x86 cpuid 0x0 output... unknown
checking for the processor vendor... Unknown
checking the L1 cache size... 0 Bytes
checking the L2 cache size... 0 Bytes
checking whether make -j30 sets $(MAKE)... (cached) yes
configure: creating ./config.status
config.status: creating Makefile
config.status: creating src/config.h
config.status: executing depfiles commands
config.status: executing libtool commands
(CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/bash /rootpool2/local/kirkby/t2/64/s
age-4.5.3.alpha0/spkg/build/libm4ri-20100730/m4ri/missing --run autoheader)
aclocal.m4:16: warning: this file was generated for autoconf 2.65.
You have another version of autoconf.  It may work, but is not guaranteed to.
If you have problems, you may need to regenerate the build system entirely.
To do so, use the procedure documented by the package, typically `autoreconf'.
rm -f src/stamp-h1
touch src/config.h.in
cd . && /bin/bash ./config.status src/config.h
config.status: creating src/config.h
config.status: src/config.h is unchanged
```



---

Comment by malb created at 2010-08-10 15:17:33

I replaced the SPKG with a version where I touched both configure scripts again (I thought I did that before, but apparently I didn't). I tested it on t2 and it doesn't attempt to call autoconf.


---

Comment by malb created at 2010-08-14 19:29:29

Changing status from needs_info to needs_review.


---

Comment by malb created at 2010-08-18 18:27:30

Since there doesn't seem to be any movement on this ticket, I took the liberty to update the patch and to prepare a new SPKG:

http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100817.spkg

Just as before this ticket depends on #9717 which was merged in 4.5.3.alpha1.

I successfully built and doctested the SPKG + the patch on:

 * *sage.math*: 64-bit Linux, Intel CPU, pass
 * *redhawk*: 64-bit Linux, AMD CPU, pass
 * *bsd:* OS X, pass
 * *t2*: Solaris, pass (I failed to build R thus those doctests failed)

I also took a sage-4.5.3.alpha1.tar, replaced the M4RI SPKG and applied the patch. Then I built Sage from scratch on sage.math and ran make ptestlong. All doctests passed.

PS: This new SPKG runs some tests to detect the L1 and L2 cache sizes, thus it compiles a little bit longer than older SPKGs for M4RI. The gained performance is well worth the wait on e.g. modern Intel CPUs where it is better to detect how much memory is fast for random access than to rely on the actual L2 cache size.


---

Comment by mvngu created at 2010-10-18 09:11:55

Do you want to ignore `m4ri` and `m4rie`? Also the `dist/` directory can now be removed as per ticket #5903.


---

Comment by mvngu created at 2010-10-18 09:12:51

Replying to [comment:26 mvngu]:
> Do you want to ignore `m4ri` and `m4rie`?
What I mean is this:

```
[mvngu`@`sage libm4ri-20100817]$ hg st
? m4ri/.hgtags
? m4ri/AUTHORS
? m4ri/COPYING
? m4ri/ChangeLog
? m4ri/INSTALL
? m4ri/Makefile.am
? m4ri/Makefile.in
? m4ri/NEWS
? m4ri/README
? m4ri/aclocal.m4
? m4ri/config.guess
? m4ri/config.sub
? m4ri/configure
? m4ri/configure.ac
? m4ri/depcomp
? m4ri/install-sh
? m4ri/ltmain.sh
? m4ri/m4/ax_cache_size.m4
? m4ri/m4/ax_cache_size_tune.m4
? m4ri/m4/ax_check_compiler_flags.m4
? m4ri/m4/ax_cpu_vendor.m4
? m4ri/m4/ax_ext.m4
? m4ri/m4/ax_gcc_x86_cpuid.m4
? m4ri/m4/ax_openmp.m4
? m4ri/m4/libtool.m4
? m4ri/m4/ltoptions.m4
? m4ri/m4/ltsugar.m4
? m4ri/m4/ltversion.m4
? m4ri/m4/lt~obsolete.m4
? m4ri/m4ri
? m4ri/m4ri.sln
? m4ri/m4ri.vcproj
? m4ri/missing
? m4ri/testsuite/.directory
? m4ri/testsuite/Makefile
? m4ri/testsuite/bench_elimination.c
? m4ri/testsuite/bench_multiplication.c
? m4ri/testsuite/bench_pluq.c
? m4ri/testsuite/bench_trsm_lowerleft.c
? m4ri/testsuite/bench_trsm_lowerright.c
? m4ri/testsuite/bench_trsm_upperleft.c
? m4ri/testsuite/bench_trsm_upperright.c
? m4ri/testsuite/cpucycles-20060326/alpha.c
? m4ri/testsuite/cpucycles-20060326/alpha.h
? m4ri/testsuite/cpucycles-20060326/amd64cpuinfo.c
? m4ri/testsuite/cpucycles-20060326/amd64cpuinfo.h
? m4ri/testsuite/cpucycles-20060326/amd64tscfreq.c
? m4ri/testsuite/cpucycles-20060326/amd64tscfreq.h
? m4ri/testsuite/cpucycles-20060326/clockmonotonic.c
? m4ri/testsuite/cpucycles-20060326/clockmonotonic.h
? m4ri/testsuite/cpucycles-20060326/compile
? m4ri/testsuite/cpucycles-20060326/cpucycles.html
? m4ri/testsuite/cpucycles-20060326/do
? m4ri/testsuite/cpucycles-20060326/do.notes
? m4ri/testsuite/cpucycles-20060326/gettimeofday.c
? m4ri/testsuite/cpucycles-20060326/gettimeofday.h
? m4ri/testsuite/cpucycles-20060326/hppapstat.c
? m4ri/testsuite/cpucycles-20060326/hppapstat.h
? m4ri/testsuite/cpucycles-20060326/powerpcaix.c
? m4ri/testsuite/cpucycles-20060326/powerpcaix.h
? m4ri/testsuite/cpucycles-20060326/powerpclinux.c
? m4ri/testsuite/cpucycles-20060326/powerpclinux.h
? m4ri/testsuite/cpucycles-20060326/powerpcmacos.c
? m4ri/testsuite/cpucycles-20060326/powerpcmacos.h
? m4ri/testsuite/cpucycles-20060326/sparc32psrinfo.c
? m4ri/testsuite/cpucycles-20060326/sparc32psrinfo.h
? m4ri/testsuite/cpucycles-20060326/sparcpsrinfo.c
? m4ri/testsuite/cpucycles-20060326/sparcpsrinfo.h
? m4ri/testsuite/cpucycles-20060326/test.c
? m4ri/testsuite/cpucycles-20060326/x86cpuinfo.c
? m4ri/testsuite/cpucycles-20060326/x86cpuinfo.h
? m4ri/testsuite/cpucycles-20060326/x86tscfreq.c
? m4ri/testsuite/cpucycles-20060326/x86tscfreq.h
? m4ri/testsuite/test_elimination.c
? m4ri/testsuite/test_kernel.c
? m4ri/testsuite/test_multiplication.c
? m4ri/testsuite/test_pluq.c
? m4ri/testsuite/test_solve.c
? m4ri/testsuite/test_trsm.c
? m4ri/testsuite/walltime.h
? m4rie/.hgignore
? m4rie/.hgtags
? m4rie/AUTHORS
? m4rie/COPYING
? m4rie/ChangeLog
? m4rie/INSTALL
? m4rie/Makefile.am
? m4rie/Makefile.in
? m4rie/NEWS
? m4rie/README
? m4rie/aclocal.m4
? m4rie/bench/Makefile.am
? m4rie/bench/Makefile.in
? m4rie/bench/bench_elimination.cc
? m4rie/bench/bench_multiplication.cc
? m4rie/bench/cpucycles-20060326/alpha.c
? m4rie/bench/cpucycles-20060326/alpha.h
? m4rie/bench/cpucycles-20060326/amd64cpuinfo.c
? m4rie/bench/cpucycles-20060326/amd64cpuinfo.h
? m4rie/bench/cpucycles-20060326/amd64tscfreq.c
? m4rie/bench/cpucycles-20060326/amd64tscfreq.h
? m4rie/bench/cpucycles-20060326/clockmonotonic.c
? m4rie/bench/cpucycles-20060326/clockmonotonic.h
? m4rie/bench/cpucycles-20060326/compile
? m4rie/bench/cpucycles-20060326/cpucycles.html
? m4rie/bench/cpucycles-20060326/do
? m4rie/bench/cpucycles-20060326/do.notes
? m4rie/bench/cpucycles-20060326/gettimeofday.c
? m4rie/bench/cpucycles-20060326/gettimeofday.h
? m4rie/bench/cpucycles-20060326/hppapstat.c
? m4rie/bench/cpucycles-20060326/hppapstat.h
? m4rie/bench/cpucycles-20060326/powerpcaix.c
? m4rie/bench/cpucycles-20060326/powerpcaix.h
? m4rie/bench/cpucycles-20060326/powerpclinux.c
? m4rie/bench/cpucycles-20060326/powerpclinux.h
? m4rie/bench/cpucycles-20060326/powerpcmacos.c
? m4rie/bench/cpucycles-20060326/powerpcmacos.h
? m4rie/bench/cpucycles-20060326/sparc32psrinfo.c
? m4rie/bench/cpucycles-20060326/sparc32psrinfo.h
? m4rie/bench/cpucycles-20060326/sparcpsrinfo.c
? m4rie/bench/cpucycles-20060326/sparcpsrinfo.h
? m4rie/bench/cpucycles-20060326/test.c
? m4rie/bench/cpucycles-20060326/x86cpuinfo.c
? m4rie/bench/cpucycles-20060326/x86cpuinfo.h
? m4rie/bench/cpucycles-20060326/x86tscfreq.c
? m4rie/bench/cpucycles-20060326/x86tscfreq.h
? m4rie/bench/walltime.h
? m4rie/config.guess
? m4rie/config.sub
? m4rie/configure
? m4rie/configure.ac
? m4rie/depcomp
? m4rie/gf2e_cxx/finite_field_givaro.h
? m4rie/install-sh
? m4rie/ltmain.sh
? m4rie/m4/ax_cache_size.m4
? m4rie/m4/ax_cache_size_tune.m4
? m4rie/m4/ax_check_compiler_flags.m4
? m4rie/m4/ax_cpu_vendor.m4
? m4rie/m4/ax_ext.m4
? m4rie/m4/ax_gcc_x86_cpuid.m4
? m4rie/m4/ax_openmp.m4
? m4rie/m4/libtool.m4
? m4rie/m4/ltoptions.m4
? m4rie/m4/ltsugar.m4
? m4rie/m4/ltversion.m4
? m4rie/m4/lt~obsolete.m4
? m4rie/missing
? m4rie/tests/Makefile
? m4rie/tests/test_elimination.cc
? m4rie/tests/test_multiplication.cc
```



---

Comment by malb created at 2010-10-18 09:44:53

I've updated the SPKG accordingly at

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100817.p0.spkg


---

Comment by drkirkby created at 2010-11-07 11:04:56

Whatever checks are being used to determine the cache size is not working very well. First it reports the L1 cache size is 0, then it spends a couple of minutes on a 3.33 GHz Xeon, to determine the cache size (I thought it had hanged). It's also producing some NaN in the calculation of the cache size - is that not a bug?  

The CPU is an Intel Xeon W3580 and the operating system OpenSolaris. 


```
checking for gcc option to accept ISO C99... -std=gnu99
checking for x86 cpuid  output... b:756e6547:6c65746e:49656e69
checking for x86 cpuid 0x0 output... b:756e6547:6c65746e:49656e69
checking for the processor vendor... Intel
checking for x86 cpuid 0x00000001 output... 106a5:100800:9ce3bd:bfebfbff
checking whether mmx is supported... yes
checking whether sse is supported... yes
checking whether sse2 is supported... yes
checking whether sse3 is supported... yes
checking whether ssse3 is supported... yes
checking whether C compiler accepts -mmmx... yes
checking whether C compiler accepts -msse... yes
checking whether C compiler accepts -msse2... yes
checking whether C compiler accepts -msse3... yes
checking mm_malloc.h usability... yes
checking mm_malloc.h presence... yes
checking for mm_malloc.h... yes
checking for x86 cpuid 0x0 output... (cached) b:756e6547:6c65746e:49656e69
checking for the processor vendor... (cached) Intel
checking for x86 cpuid 0x80000000 output... 80000008:0:0:0
checking for x86 cpuid 0x80000005 output... 0:0:0:0
checking for x86 cpuid 0x80000006 output... 0:0:1006040:0
checking the L1 cache size... 0 Bytes
checking the L2 cache size... 262144 Bytes
checking for cache sizes... 
s:     4, rx:   0.03, x:   0.03, wt:   0.03, dx:    NaN
s:     8, rx:   0.06, x:   0.06, wt:   0.06, dx:   1.01
s:    16, rx:   0.12, x:   0.12, wt:   0.12, dx:   1.00
s:    32, rx:   0.24, x:   0.24, wt:   0.24, dx:   1.00
s:    64, rx:   0.53, x:   0.53, wt:   0.53, dx:   1.10
s:   128, rx:   0.32, x:   1.30, wt:   0.32, dx:   1.23
s:   256, rx:   0.37, x:   2.95, wt:   0.37, dx:   1.14
s:   512, rx:   0.42, x:   6.77, wt:   0.42, dx:   1.15

s:     4, rx:   0.03, x:   0.03, wt:   0.03, dx:    NaN
s:     8, rx:   0.06, x:   0.06, wt:   0.06, dx:   0.94
s:    16, rx:   0.12, x:   0.12, wt:   0.12, dx:   0.99
s:    32, rx:   0.24, x:   0.24, wt:   0.24, dx:   1.02
s:    64, rx:   0.53, x:   0.53, wt:   0.53, dx:   1.09
s:   128, rx:   0.32, x:   1.29, wt:   0.32, dx:   1.22
s:   256, rx:   0.37, x:   2.97, wt:   0.37, dx:   1.16
s:   512, rx:   0.43, x:   6.80, wt:   0.43, dx:   1.14

s:     4, rx:   0.03, x:   0.03, wt:   0.03, dx:    NaN
s:     8, rx:   0.06, x:   0.06, wt:   0.06, dx:   0.91
s:    16, rx:   0.12, x:   0.12, wt:   0.12, dx:   1.01
s:    32, rx:   0.24, x:   0.24, wt:   0.24, dx:   1.01
s:    64, rx:   0.52, x:   0.52, wt:   0.52, dx:   1.09
s:   128, rx:   0.32, x:   1.30, wt:   0.32, dx:   1.24
s:   256, rx:   0.37, x:   2.94, wt:   0.37, dx:   1.13
s:   512, rx:   0.41, x:   6.64, wt:   0.42, dx:   1.13

s:     4, rx:   0.03, x:   0.03, wt:   0.03, dx:    NaN
s:     8, rx:   0.06, x:   0.06, wt:   0.06, dx:   0.92
s:    16, rx:   0.12, x:   0.12, wt:   0.12, dx:   1.02
s:    32, rx:   0.24, x:   0.24, wt:   0.24, dx:   1.00
s:    64, rx:   0.53, x:   0.53, wt:   0.53, dx:   1.11
s:   128, rx:   0.33, x:   1.30, wt:   0.33, dx:   1.23
s:   256, rx:   0.37, x:   2.98, wt:   0.37, dx:   1.14
s:   512, rx:   0.41, x:   6.61, wt:   0.41, dx:   1.11

s:     4, rx:   0.03, x:   0.03, wt:   0.03, dx:    NaN
s:     8, rx:   0.06, x:   0.06, wt:   0.06, dx:   0.93
s:    16, rx:   0.12, x:   0.12, wt:   0.12, dx:   1.01
s:    32, rx:   0.24, x:   0.24, wt:   0.24, dx:   1.02
s:    64, rx:   0.53, x:   0.53, wt:   0.53, dx:   1.09
s:   128, rx:   0.32, x:   1.30, wt:   0.32, dx:   1.23
s:   256, rx:   0.37, x:   2.94, wt:   0.37, dx:   1.13
s:   512, rx:   0.42, x:   6.75, wt:   0.42, dx:   1.15

s:   512, rx:   0.42, x:   0.42, wt:   0.42, dx:    NaN
s:  1024, rx:   1.00, x:   1.00, wt:   1.00, dx:   1.18
s:  1536, rx:   0.39, x:   1.57, wt:   0.39, dx:   1.05
s:  2048, rx:   0.27, x:   2.19, wt:   0.27, dx:   1.04
s:  3072, rx:   0.21, x:   3.32, wt:   0.21, dx:   1.01
s:  4096, rx:   0.29, x:   4.60, wt:   0.29, dx:   1.04
s:  6144, rx:   0.28, x:   8.85, wt:   0.28, dx:   1.28
s:  8192, rx:   0.25, x:  15.96, wt:   0.25, dx:   1.35
s: 16384, rx:   0.43, x:  55.40, wt:   0.44, dx:   1.74
s: 32768, rx:   0.61, x: 156.25, wt:   0.62, dx:   1.41

s:   512, rx:   0.43, x:   0.43, wt:   0.43, dx:    NaN
s:  1024, rx:   0.99, x:   0.99, wt:   0.99, dx:   1.15
s:  1536, rx:   0.39, x:   1.56, wt:   0.39, dx:   1.05
s:  2048, rx:   0.27, x:   2.13, wt:   0.27, dx:   1.03
s:  3072, rx:   0.21, x:   3.32, wt:   0.21, dx:   1.04
s:  4096, rx:   0.28, x:   4.52, wt:   0.28, dx:   1.02
s:  6144, rx:   0.27, x:   8.76, wt:   0.28, dx:   1.29
s:  8192, rx:   0.25, x:  15.87, wt:   0.25, dx:   1.36
s: 16384, rx:   0.42, x:  54.27, wt:   0.43, dx:   1.71
s: 32768, rx:   0.61, x: 156.22, wt:   0.62, dx:   1.44

s:   512, rx:   0.42, x:   0.42, wt:   0.42, dx:    NaN
s:  1024, rx:   0.99, x:   0.99, wt:   0.99, dx:   1.17
s:  1536, rx:   0.39, x:   1.56, wt:   0.39, dx:   1.05
s:  2048, rx:   0.27, x:   2.14, wt:   0.27, dx:   1.03
s:  3072, rx:   0.21, x:   3.31, wt:   0.21, dx:   1.03
s:  4096, rx:   0.28, x:   4.53, wt:   0.29, dx:   1.03
s:  6144, rx:   0.27, x:   8.73, wt:   0.28, dx:   1.28
s:  8192, rx:   0.25, x:  16.01, wt:   0.25, dx:   1.38
s: 16384, rx:   0.42, x:  54.24, wt:   0.43, dx:   1.69
s: 32768, rx:   0.63, x: 162.00, wt:   0.65, dx:   1.49

s:   512, rx:   0.43, x:   0.43, wt:   0.43, dx:    NaN
s:  1024, rx:   1.01, x:   1.01, wt:   1.01, dx:   1.19
s:  1536, rx:   0.20, x:   1.58, wt:   0.20, dx:   1.04
s:  2048, rx:   0.28, x:   2.21, wt:   0.28, dx:   1.04
s:  3072, rx:   0.21, x:   3.39, wt:   0.21, dx:   1.02
s:  4096, rx:   0.29, x:   4.63, wt:   0.29, dx:   1.02
s:  6144, rx:   0.28, x:   8.84, wt:   0.28, dx:   1.27
s:  8192, rx:   0.25, x:  16.17, wt:   0.26, dx:   1.37
s: 16384, rx:   0.43, x:  55.01, wt:   0.44, dx:   1.70
s: 32768, rx:   0.61, x: 157.06, wt:   0.63, dx:   1.43

s:   512, rx:   0.43, x:   0.43, wt:   0.43, dx:    NaN
s:  1024, rx:   1.01, x:   1.01, wt:   1.01, dx:   1.17
s:  1536, rx:   0.20, x:   1.59, wt:   0.20, dx:   1.05
s:  2048, rx:   0.27, x:   2.19, wt:   0.27, dx:   1.03
s:  3072, rx:   0.21, x:   3.40, wt:   0.21, dx:   1.03
s:  4096, rx:   0.29, x:   4.63, wt:   0.29, dx:   1.02
s:  6144, rx:   0.28, x:   8.90, wt:   0.28, dx:   1.28
s:  8192, rx:   0.25, x:  16.12, wt:   0.26, dx:   1.36
s: 16384, rx:   0.43, x:  54.90, wt:   0.44, dx:   1.70
s: 32768, rx:   0.61, x: 157.41, wt:   0.63, dx:   1.43

65536:8388608
checking the L1 cache size... 65536 Bytes
checking the L2 cache size... 8388608 Bytes
```



---

Comment by malb created at 2010-11-07 13:57:27

Replying to [comment:29 drkirkby]:
> Whatever checks are being used to determine the cache size is not working very well.

I disagree, it works fine as far as I know but it is slow. For your machine I'd assume that 65536:8388608 indeed gives pretty good performance. If you want to check whether this hunch is correct let me know and I can tell you how to patch and test M4RI for various cache size configurations.

> First it reports the L1 cache size is 0,

That's probably because I don't know how to ask Solaris for the right information, however the tuning performed now is the better strategy anyway.

> then it spends a couple of minutes on a 3.33 GHz Xeon, to determine the cache size (I thought it had hanged). 

Tuning takes a while as described above. Some shells don't seem to print intermediate outputs, I don't know how to fix that. If you do, let me know. Also, I couldn't get reliable information if I lowered the time spent on tuning, if you have any ideas, let me know. 

> It's also producing some NaN in the calculation of the cache size - is that not a bug?  

No, the delta from the first element with respect to the previous element is not defined.


---

Comment by malb created at 2011-01-13 10:24:09

Minh, do you think you'll have some time to review this?


---

Comment by zimmerma created at 2011-03-30 12:01:34

the speedup provided by this patch is quite impressive. With vanilla Sage 4.6 on a 2.83Ghz Core 2:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: m=matrix(GF(2^8,'x'),1000,1000)
sage: m.randomize()
sage: time r=m*m
CPU times: user 76.33 s, sys: 0.10 s, total: 76.43 s
Wall time: 77.63 s
```

With this patch applied:

```
sage: m=matrix(GF(2^8,'x'),1000,1000)   
sage: m.randomize()
sage: time r=m*m
CPU times: user 0.27 s, sys: 0.00 s, total: 0.27 s
Wall time: 0.29 s
```

Paul Zimmermann


---

Comment by kcrisman created at 2011-06-30 14:03:59

On PPC OS X 10.4, this spkg installation hangs at

```
checking the L1 cache size... 32768 Bytes
checking the L2 cache size... 262144 Bytes
checking for cache sizes... 
```

I'm assuming this "cache size" checking isn't supposed to take 10 or more minutes.


---

Comment by malb created at 2011-06-30 14:17:33

Can you run spkg-install manually, i.e. unpack the spkg and run ./spkg-install in a SAGE shell? It will print intermediate information which might tell us whether it just takes long or whether it really hangs?


---

Comment by kcrisman created at 2011-06-30 14:34:42

So far it just seems to be *extremely* slow.  Well, this _is_ a machine with a 700MHz processor...

In lines like

```
s:   512, rx:  18.03, x:  18.03, wt:  18.03, dx:    NaN
s:  1024, rx:  73.30, x:  73.30, wt:  73.31, dx:   2.03
```

which column gives the timing, if any?


---

Comment by kcrisman created at 2011-06-30 18:05:43

Okay, it _did_ finally finish!  

```
checking for cache sizes... 
s:     4, rx:   0.20, x:   0.20, wt:   0.20, dx:    NaN
s:     8, rx:   0.38, x:   0.38, wt:   0.38, dx:   0.96
s:    16, rx:   0.39, x:   0.79, wt:   0.39, dx:   1.03
s:    32, rx:   0.46, x:   1.83, wt:   0.46, dx:   1.16
s:    64, rx:   0.49, x:   3.92, wt:   0.49, dx:   1.07
s:   128, rx:   0.57, x:   9.17, wt:   0.57, dx:   1.17
s:   256, rx:   0.63, x:  40.57, wt:   0.64, dx:   2.21
s:   512, rx:   1.17, x: 300.03, wt:   1.18, dx:   3.70

s:     4, rx:   0.19, x:   0.19, wt:   0.19, dx:    NaN
s:     8, rx:   0.38, x:   0.38, wt:   0.38, dx:   1.01
s:    16, rx:   0.42, x:   0.83, wt:   0.42, dx:   1.10
s:    32, rx:   0.44, x:   1.78, wt:   0.44, dx:   1.06
s:    64, rx:   0.50, x:   4.00, wt:   0.50, dx:   1.13
s:   128, rx:   0.46, x:  14.83, wt:   0.46, dx:   1.85
s:   256, rx:   0.99, x:  63.40, wt:   0.99, dx:   2.14
s:   512, rx:   1.21, x: 310.35, wt:   1.22, dx:   2.45

s:     4, rx:   0.17, x:   0.17, wt:   0.17, dx:    NaN
s:     8, rx:   0.39, x:   0.39, wt:   0.39, dx:   1.14
s:    16, rx:   0.43, x:   0.87, wt:   0.43, dx:   1.11
s:    32, rx:   0.43, x:   1.73, wt:   0.43, dx:   1.00
s:    64, rx:   0.47, x:   3.74, wt:   0.47, dx:   1.08
s:   128, rx:   0.60, x:   9.58, wt:   0.60, dx:   1.28
s:   256, rx:   0.56, x:  36.13, wt:   0.57, dx:   1.89
s:   512, rx:   1.25, x: 320.55, wt:   1.26, dx:   4.44

s:     4, rx:   0.21, x:   0.21, wt:   0.21, dx:    NaN
s:     8, rx:   0.39, x:   0.39, wt:   0.39, dx:   0.94
s:    16, rx:   0.43, x:   0.85, wt:   0.43, dx:   1.10
s:    32, rx:   0.44, x:   1.74, wt:   0.44, dx:   1.02
s:    64, rx:   0.48, x:   3.87, wt:   0.48, dx:   1.11
s:   128, rx:   0.59, x:   9.39, wt:   0.59, dx:   1.21
s:   256, rx:   0.63, x:  40.42, wt:   0.63, dx:   2.15
s:   512, rx:   1.16, x: 297.41, wt:   1.17, dx:   3.68

s:     4, rx:   0.19, x:   0.19, wt:   0.19, dx:    NaN
s:     8, rx:   0.39, x:   0.39, wt:   0.39, dx:   1.01
s:    16, rx:   0.41, x:   0.82, wt:   0.41, dx:   1.04
s:    32, rx:   0.42, x:   1.69, wt:   0.42, dx:   1.04
s:    64, rx:   0.48, x:   3.81, wt:   0.48, dx:   1.13
s:   128, rx:   0.59, x:   9.40, wt:   0.59, dx:   1.23
s:   256, rx:   0.73, x:  46.75, wt:   0.73, dx:   2.49
s:   512, rx:   1.20, x: 306.20, wt:   1.20, dx:   3.27

s:   512, rx:  20.54, x:  20.54, wt:  20.54, dx:    NaN
s:  1024, rx:  68.61, x:  68.61, wt:  68.63, dx:   1.67
s:  1536, rx:   0.24, x: 124.21, wt:   0.26, dx:   1.21
s:  2048, rx:   0.18, x: 182.39, wt:   0.20, dx:   1.10
s:  3072, rx:   0.30, x: 303.95, wt:   0.32, dx:   1.11
s:  4096, rx:   0.24, x: 487.92, wt:   0.28, dx:   1.20
s:  6144, rx:   0.19, x: 793.79, wt:   0.25, dx:   1.08
s:  8192, rx:   0.00, x:   0.38, wt:   0.08, dx:   0.00
s: 16384, rx:   0.00, x:   0.31, wt:   0.19, dx:   0.41
s: 32768, rx:   0.00, x:   0.37, wt:   0.32, dx:   0.59

s:   512, rx:  18.06, x:  18.06, wt:  18.07, dx:    NaN
s:  1024, rx:  68.43, x:  68.43, wt:  68.43, dx:   1.89
s:  1536, rx:   0.24, x: 125.17, wt:   0.26, dx:   1.22
s:  2048, rx:   0.17, x: 169.91, wt:   0.18, dx:   1.02
s:  3072, rx:   0.31, x: 318.15, wt:   0.34, dx:   1.25
s:  4096, rx:   0.22, x: 444.11, wt:   0.26, dx:   1.05
s:  6144, rx:   0.20, x: 803.39, wt:   0.26, dx:   1.21
s:  8192, rx:   0.00, x:   0.30, wt:   0.08, dx:   0.00
s: 16384, rx:   0.00, x:   0.38, wt:   0.15, dx:   0.62
s: 32768, rx:   0.00, x:   0.31, wt:   0.31, dx:   0.41

s:   512, rx:  17.85, x:  17.85, wt:  17.86, dx:    NaN
s:  1024, rx:  68.59, x:  68.59, wt:  68.60, dx:   1.92
s:  1536, rx:   0.26, x: 131.07, wt:   0.27, dx:   1.27
s:  2048, rx:   0.18, x: 182.17, wt:   0.20, dx:   1.04
s:  3072, rx:   0.32, x: 323.67, wt:   0.34, dx:   1.18
s:  4096, rx:   0.22, x: 444.65, wt:   0.26, dx:   1.03
s:  6144, rx:   0.19, x: 788.59, wt:   0.25, dx:   1.18
s:  8192, rx:   0.29, x: 1203.62, wt:   0.38, dx:   1.14
s: 16384, rx:   0.00, x:   0.35, wt:   0.16, dx:   0.00
s: 32768, rx:   0.00, x:   0.35, wt:   0.33, dx:   0.50

s:   512, rx:  17.39, x:  17.39, wt:  17.40, dx:    NaN
s:  1024, rx:  68.02, x:  68.02, wt:  68.03, dx:   1.96
s:  1536, rx:   0.24, x: 123.60, wt:   0.26, dx:   1.21
s:  2048, rx:   0.17, x: 178.99, wt:   0.19, dx:   1.09
s:  3072, rx:   0.29, x: 301.11, wt:   0.32, dx:   1.12
s:  4096, rx:   0.24, x: 501.66, wt:   0.28, dx:   1.25
s:  6144, rx:   0.19, x: 796.99, wt:   0.25, dx:   1.06
s:  8192, rx:   0.28, x: 1141.88, wt:   0.36, dx:   1.07
s: 16384, rx:   0.00, x:   0.36, wt:   0.15, dx:   0.00
s: 32768, rx:   0.00, x:   0.37, wt:   0.31, dx:   0.51

s:   512, rx:  19.65, x:  19.65, wt:  19.66, dx:    NaN
s:  1024, rx:  68.37, x:  68.37, wt:  68.38, dx:   1.74
s:  1536, rx:   0.23, x: 119.48, wt:   0.26, dx:   1.16
s:  2048, rx:   0.20, x: 202.14, wt:   0.22, dx:   1.27
s:  3072, rx:   0.29, x: 299.73, wt:   0.32, dx:   0.99
s:  4096, rx:   0.22, x: 441.61, wt:   0.26, dx:   1.11
s:  6144, rx:   0.19, x: 795.29, wt:   0.25, dx:   1.20
s:  8192, rx:   0.28, x: 1141.73, wt:   0.35, dx:   1.08
s: 16384, rx:   0.00, x:   0.35, wt:   0.16, dx:   0.00
s: 32768, rx:   0.00, x:   0.35, wt:   0.32, dx:   0.50

262144:524288
```



----

Doctest failure:

```
    sage: A.pivots() # indirect doctest
Expected:
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Got:
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
```


Series of failures, for all such doctests:

```
    AttributeError: 'sage.matrix.matrix_mod2e_dense.Matrix_mod2e_dense' object has no attribute '_multiply_classical'
```

Is something not inheriting properly?  This method seems to be defined in Sage, and similar doctests in the rest of the matrix/ folder pass (in fact, all other tests in crypto and matrix pass other than one unrelated one from something I did on this installation).


---

Comment by malb created at 2011-06-30 20:35:45

Replying to [comment:37 kcrisman]:
> Okay, it _did_ finally finish!  

Okay, good ... well, I'm still not sure what I should do about this. The easiest might be to disable cache tuning on PPC?

> ----
> 
> Doctest failure:
> {{{
>     sage: A.pivots() # indirect doctest
> Expected:
>      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
> Got:
>     (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
> }}}

I can reproduce this one.

> Series of failures, for all such doctests:
> {{{
>     AttributeError: 'sage.matrix.matrix_mod2e_dense.Matrix_mod2e_dense' object has no attribute '_multiply_classical'
> }}}
> Is something not inheriting properly?  This method seems to be defined in Sage, and similar doctests in the rest of the matrix/ folder pass (in fact, all other tests in crypto and matrix pass other than one unrelated one from something I did on this installation).

I cannot seem to reproduce these (in the matrix/ folder). Which file does give this?

PS: Thank you so much for taking an interest in this ticket!


---

Comment by kcrisman created at 2011-07-01 00:12:57

> Okay, good ... well, I'm still not sure what I should do about this. The easiest might be to disable cache tuning on PPC?

What I would say is to disable this on any machine that is probably old and slow - this is probably not a PPC thing per se.  That would be OS X 10.4, probably older versions of Ubuntu, ... I don't know how one would do this, though.

> > Series of failures, for all such doctests:
> > {{{
> >     AttributeError: 'sage.matrix.matrix_mod2e_dense.Matrix_mod2e_dense' object has no attribute '_multiply_classical'
> > }}}
> 
> I cannot seem to reproduce these (in the matrix/ folder). Which file does give this?
> 

This is the new file and class 'sage.matrix.matrix_mod2e_dense.Matrix_mod2e_dense' as indicated above.  Since the tests for `_multiply_classical` work in other files, something isn't working about the inheritance.  

This _could_ be related to my having installed numpy 1.6 before testing.  But that would seem strange, since neither this nor the other multiplication rely on this, they are .pyx files... and all the other ones work...

> PS: Thank you so much for taking an interest in this ticket!
I just have an interest in making sure older systems can still use Sage.  There is too much planned obsolescence in computers already.


---

Comment by malb created at 2011-07-01 15:12:32

Changing status from needs_review to needs_work.


---

Comment by malb created at 2011-07-01 15:12:32

Hi, can you give

   http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20110701.alpha.spkg

a try? It doesn't fix the doctest failures but compilation should be quicker and provide more feedback.


---

Comment by kcrisman created at 2011-07-01 16:35:22

Sorry, I won't have access to that machine for a while now.


---

Comment by kcrisman created at 2011-07-05 13:56:07

I'm a little confused.  The spkgs here and at #11574 are both libm4ri, and seem to be numbered backwards (the "earlier" one in the dependency is from 2011).


---

Comment by kcrisman created at 2011-07-05 14:50:32

Okay, I figured it out - sorry for the noise.  I agree that it is very annoying to have two things inside the same spkg.  There is, for instance, an open ticket to remove rpy2 from the r spkg.


---

Comment by kcrisman created at 2011-07-05 14:50:32

Remove assignee tbd.


---

Comment by malb created at 2011-07-05 15:12:45

Replying to [comment:44 kcrisman]:
> Okay, I figured it out - sorry for the noise.

NP, I should have explained things better.

> I agree that it is very annoying to have two things inside the same spkg.  
> There is, for instance, an open ticket to remove rpy2 from the r spkg.  

Well, it makes it easier to re-use tuning results. For example, I plan to run the cache tuning only once, i.e. for M4RI and M4RIE would re-use the results.


---

Comment by kcrisman created at 2011-07-05 15:17:07

Replying to [comment:45 malb]:
> Replying to [comment:44 kcrisman]:
> > I agree that it is very annoying to have two things inside the same spkg.  
> > There is, for instance, an open ticket to remove rpy2 from the r spkg.  
> 
> Well, it makes it easier to re-use tuning results. For example, I plan to run the cache tuning only once, i.e. for M4RI and M4RIE would re-use the results. 

That makes a lot of sense, especially since that takes a while even on speedy machines.

----
By the way, I tried #11574 but ran into trouble with an undefined symbol about `m4ri_swap_bits`, perhaps due to my having installed #9562 first.  I did apply the patch at #11574.  Anyway, I'm reverting to the vanilla Sage version, and then going back to #11574 (I already had done the PolyBoRi upgrade).


---

Comment by malb created at 2011-07-05 15:22:33

Hi, I updated the patch for #11574 21h ago, did you try it? It fixes the missing symbol stuff.


---

Comment by kcrisman created at 2011-07-05 15:34:12

Replying to [comment:47 malb]:
> Hi, I updated the patch for #11574 21h ago, did you try it? It fixes the missing symbol stuff.
Yes, for some reason I must have had things applied in the wrong order, though, so I am starting from scratch.


---

Comment by malb created at 2011-07-06 16:41:24

Changing status from needs_work to needs_review.


---

Comment by malb created at 2011-07-06 16:48:05

apply to root repository not to normal Sage repository


---

Attachment


---

Comment by fbissey created at 2011-07-06 18:54:48

Changing status from needs_review to needs_work.


---

Comment by fbissey created at 2011-07-06 18:54:48

Please no

```
depends = [SAGE_ROOT + "/local/include/m4rie/m4rie.h"],
```

in module_list.py I have just cleaned up (#11377) do

```
depends = [SAGE_INC + "m4rie/m4rie.h"],
```

instead.


---

Comment by malb created at 2011-07-07 09:30:02

Changing status from needs_work to needs_review.


---

Comment by malb created at 2011-07-07 09:30:02

Okay, fixed.


---

Comment by fbissey created at 2011-07-10 04:16:35

If I could just squeeze an extra request (not counting for review): could you tag a corresponding release of m4rie on bitbucket? That way I could make a gentoo ebuild from the bitbucket release rather than pulling the spkg. 

I also see that suddenly we have split libm4rie from libm4ri (which I am happy about) but without apparent warnings.


---

Comment by malb created at 2011-07-10 11:30:38

Yeah, sorry I was a bit lazy:

1) There will be an official 20110715 release of both M4RI and M4RIE. I put together the SPKGs to test whether they work with Sage. So perhaps I shouldn't have set "needs review"

2) Yes, I gave in to the demand to split them. I should have mentioned it.


---

Comment by malb created at 2011-07-10 11:30:38

Changing status from needs_review to needs_work.


---

Comment by fbissey created at 2011-07-10 19:44:16

I must say it only occurred to me yesterday while looking at tags on bitbucket that 20110715 is in the future.


---

Comment by malb created at 2011-07-11 14:22:59

Changing status from needs_work to needs_review.


---

Comment by malb created at 2011-07-11 14:22:59

It's now officially released.


---

Comment by SimonKing created at 2011-08-15 16:53:03

I get numerous errors when trying to install the spkg. The following is just a small selection of errors:

```
...
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:248: error: too many arguments to function 'mzed_make_table'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:249: warning: passing argument 2 of 'mzed_make_table' makes pointer from integer without a cast
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:145: note: expected 'struct mzed_t *' but argument is of type 'size_t'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:249: warning: passing argument 3 of 'mzed_make_table' makes pointer from integer without a cast
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:145: note: expected 'struct gf2e *' but argument is of type 'size_t'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:249: error: too many arguments to function 'mzed_make_table'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:251: error: 'mzed_t' has no member named 'nrows'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:251: warning: passing argument 2 of 'mzed_process_rows3' makes pointer from integer without a cast
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.h:172: note: expected 'struct mzed_t *' but argument is of type 'size_t'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:251: warning: passing argument 4 of 'mzed_process_rows3' makes pointer from integer without a cast
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.h:172: note: expected 'struct mzed_t *' but argument is of type 'size_t'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:251: error: too many arguments to function 'mzed_process_rows3'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:253: warning: passing argument 3 of 'mzed_process_rows3' makes pointer from integer without a cast
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.h:172: note: expected 'struct mzed_t *' but argument is of type 'size_t'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:253: warning: passing argument 4 of 'mzed_process_rows3' makes pointer from integer without a cast
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.h:172: note: expected 'struct mzed_t *' but argument is of type 'size_t'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:253: error: too many arguments to function 'mzed_process_rows3'
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:256: warning: passing argument 2 of 'mzed_make_table' makes pointer from integer without a cast
/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/travolta.c:145: note: expected 'struct mzed_t *' but argument is of type 'size_t'
make[1]: libtool: compile:  gcc -std=gnu99 -DHAVE_CONFIG_H -I. -I/mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie -I./src -I/mnt/local/king/SAGE/sage-4.7.1.rc1/local/include -I/mnt/local/king/SAGE/sage-4.7.1.rc1/local/include -g -fPIC -Wall -pedantic -O2 -MT finite_field.lo -MD -MP -MF .deps/finite_field.Tpo -c /mnt/local/king/SAGE/sage-4.7.1.rc1/spkg/build/libm4rie-20110715/m4rie/src/finite_field.c -o finite_field.o >/dev/null 2>&1
*** [gf2e_matrix.lo] Fehler 1
...
```


What may be the problem? Is it needed to apply the patches first (in contrast to what is said in the ticket description)?


---

Comment by SimonKing created at 2011-08-15 16:53:03

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-08-15 16:53:56

Ouch. Sorry. Right when hitting the "submit" button, I saw that the ticket has a dependency that I forgot to apply first.


---

Comment by SimonKing created at 2011-08-15 16:54:05

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-08-15 20:11:02

I got doctest failures in 4 files. But I have to admit that I applied your patch on top of various other patches, in particular #9138 (which is quite invasive). So, it could be that the problems are ultimately due to other patches.


---

Comment by malb created at 2011-08-15 20:27:56

I'll build 4.7.1.rc2 (on sage.math and locally) and test with that.


---

Comment by malb created at 2011-08-15 22:26:22

Simon, did you install #11261 as well and rebuild pbori.pyx? It's a dependency of the M4RI update and easy to overlook.


---

Comment by malb created at 2011-08-15 22:54:14

With everything applied + 4.7.1.rc2 I get


```
The following tests failed:

sage -t  -long -force_lib devel/sage/sage/tests/cmdline.py # 1 doctests failed
```


which is normal on sage.math.


---

Comment by SimonKing created at 2011-08-16 06:10:39

Replying to [comment:67 malb]:
> Simon, did you install #11261 as well and rebuild pbori.pyx? It's a dependency of the M4RI update and easy to overlook.

Me stupid! I only installed #11574, but not its dependency!


---

Comment by SimonKing created at 2011-08-16 10:44:41

The doc tests pass, but I think the documentation must be put into the reference manual.


---

Comment by SimonKing created at 2011-08-16 10:44:41

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-08-16 11:54:11

I found one benchmark that you should improve:


```
sage: MS = MatrixSpace(GF(64,'a'),5000,5000)
sage: K = MS.base_ring()
sage: c = K.random_element()
sage: %time A*c
CPU times: user 1.33 s, sys: 0.02 s, total: 1.35 s
Wall time: 1.35 s
5000 x 5000 dense matrix over Finite Field in a of size 2^6
sage: MS1 = MatrixSpace(GF(64,'a'),1,5000)
sage: B = MS1.random_element()
sage: %timeit B*c
625 loops, best of 3: 291 µs per loop
```


The reason is that "A*c" relies on a slow generic implementation.

I am sure that your library has a fast way to multiply a row respectively a matrix with a scalar. But you should overload `_lmul_` (please not `_rmul_`, according to the documentation), so that the user can benefit from it.


---

Comment by malb created at 2011-08-16 12:18:17

Replying to [comment:70 SimonKing]:
> The doc tests pass, but I think the documentation must be put into the reference manual.

I'm not sure that's desirable: most functions are cdefs and hence won't show up. Other functions begin with underscores (`_foo`) and hence won't show up. Thus, it looks pretty weird and as if very few actual functionality was implemented.


---

Comment by malb created at 2011-08-16 12:39:04

Changing status from needs_work to needs_review.


---

Comment by malb created at 2011-08-16 12:39:04

The updated patch includes `_lmul_` and includes this class in the reference manual. However, there isn't much content any way so it might be better not to include it?


---

Comment by SimonKing created at 2011-08-16 12:43:07

Replying to [comment:73 malb]:
> The updated patch includes `_lmul_` and includes this class in the reference manual. However, there isn't much content any way so it might be better not to include it?

Actually it seems you are right. ALL attributes of `sage.matrix.matrix_mod2_dense.Matrix_mod2_dense` either start with "_" or override a method that is documented in `sage.matrix.matrix_dense.Matrix_dense`.


---

Comment by SimonKing created at 2011-08-16 12:56:24

I am puzzled. I see that your new patch version contains _lmul_. When I downloaded it and read it in an editor, I find _lmul_. When I qdelete the old patch and qimport the new one, then _lmul_ is missing.

Do you have any explanation for what I did wrong?


---

Comment by malb created at 2011-08-16 13:00:05

`qpush` missing?


---

Comment by SimonKing created at 2011-08-16 14:15:11

Replying to [comment:76 malb]:
> `qpush` missing?

No. When I tried first, I simply did `qpush` after the qimport, and `sage -br`, but found that `_lmul_` was missing.

When one qimports a patch, then it is stored in the folder `.hg/patches`. When one qdeletes it, it is also removed from the folder.

And when I qimported your new patch, a file with the given patch name was created in `.hg/patches`, but that file did _not_ contain the string "lmul".

That never happened to me before today.


---

Comment by SimonKing created at 2011-08-16 14:19:24

I worked around the problem: I downloaded the new patch, saved it locally, and qimported it from the local file. I wonder, though, why the old patch version was not used when qimporting it with the http-address?


---

Comment by SimonKing created at 2011-08-16 14:20:52

Replying to [comment:78 SimonKing]:
> I wonder, though, why the old patch version was not used when qimporting it with the http-address?

One negation to many: "... why the old patch version was _used_ when qimporting it via http".


---

Comment by SimonKing created at 2011-08-16 14:34:10

The timings have clearly improved:

```
sage: MS = MatrixSpace(GF(64,'a'),5000,5000)
sage: K = MS.base_ring()
sage: c = K.random_element()
sage: A = MS.random_element()
sage: %time A*c
CPU times: user 0.68 s, sys: 0.02 s, total: 0.70 s
Wall time: 0.71 s
5000 x 5000 dense matrix over Finite Field in a of size 2^6
sage: MS1 = MatrixSpace(GF(64,'a'),1,5000)
sage: B = MS1.random_element()
sage: %timeit B*c
625 loops, best of 3: 88.3 µs per loop
```


That is good enough, I'd say.

Personally, I am still not happy, since scalar multiplication will very frequently occur in my application. My Meataxe fork does the first example in 39.4 ms and the second one in 20 µs. On the other hand, the time that I can gain by using M4RIE in echelon computation will probably be more than the time lost in scalar multiplication...


---

Comment by malb created at 2011-08-16 16:02:10

this is now https://bitbucket.org/malb/m4rie/issue/9/improve-scalar-multiplication-for-mzed_t


---

Comment by malb created at 2011-08-17 14:14:10

the updated patch avoids adding this class to the reference manual.


---

Comment by SimonKing created at 2011-08-17 16:58:27

With the old version of the M4RI and M4RIE patches, I got some doctest errors on mark (which is solaris):

```
        sage -t  -force_lib "devel/sage/sage/rings/polynomial/pbori.pyx"
        sage -t  -force_lib "devel/sage/sage/rings/polynomial/multi_polynomial_sequence.py"
        sage -t  -force_lib "devel/sage/sage/plot/plot.py" # Time out
        sage -t  -force_lib "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
        sage -t  -force_lib "devel/sage/sage/crypto/mq/sr.py"
        sage -t  -force_lib "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py" # Time out  
        sage -t  -force_lib "devel/sage/sage/schemes/elliptic_curves/heegner.py" # Time out
```


I need to investigate it further.


---

Comment by SimonKing created at 2011-08-17 17:01:40

Replying to [comment:83 SimonKing]:
> With the old version of the M4RI and M4RIE patches, I got some doctest errors on mark (which is solaris):

And that's since I am stupid!!! Again I forgot to install the dependencies!


---

Comment by SimonKing created at 2011-08-17 17:06:34

Replying to [comment:84 SimonKing]:
>  
> And that's since I am stupid!!! Again I forgot to install the dependencies!

Or perhaps not. The new polybori spkg from #11261 is installed, and so is the new M4RI spkg and the corresponding patches.

I have to leave office now. But it seems that either #11574 or this ticket are causing the problem.


---

Comment by malb created at 2011-08-17 17:13:39

Can you touch `sage/libs/polybori/decl.pxd`, run `sage -b` and try those again?


---

Comment by SimonKing created at 2011-08-17 18:29:37

Replying to [comment:86 malb]:
> Can you touch `sage/libs/polybori/decl.pxd`, run `sage -b` and try those again? 

I did, and get a segfault in `sage -t -force_lib "devel/sage/sage/rings/polynomial/pbori.pyx"`. That actually happens with #11574, so, I should report there.


---

Comment by SimonKing created at 2011-08-20 13:27:18

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-08-20 13:27:18

Finally, the tests on 32 bit solaris (mark on skynet) are finshed. They passed, modulo the usual timeouts. The long tests pass on my machine. If I understand the discussion above, it builds on 64 bit solaris and on Cygwin as well, and of course on linux and os x.

Moreover, it provides a very impressive speedup compared with old Sage matrices over GF(2<sup>e</sup>). If I am not mistaken, it is even faster than Magma.

So, it is almost a positive review.

But there remain a few things to do.

1. David Kirkby noted that we are adding a new standard spkg here. So, there should be a voting on sage-devel. So, that's "needs info".

2. I found some issues with the "randomize" methods. 

  i) The randomize method in sage/libs/ntl/ntl_mat_GF2E.pyx is not documented (thus, also has no tests), and it lacks the usual optional arguments `density` and `nonzero`.

  ii) The doc of Matrix_mod2e_dense.randomize gives no use cases for the optional arguments. Actually, the behaviour when passing the optional arguments is clearly not what we want:
  {{{
sage: MS = MatrixSpace(GF(64,'a'),100,100)
sage: A = MS.random_element(densitiy=0.3)
sage: A.density()
4913/5000
sage: B = MS.random_element(nonzero=True)
sage: B.density()
2469/2500
sage: C = MS.random_element(nonzero=True, density=1)
sage: C.density()
2461/2500
sage: D = MS.random_element(density=0)
sage: D.density()
983/1000
  }}}

3. The doc of many methods needs some polishing.

 * It would be nice to have a reference to research articles. I had never heard of Travolta tables before. Strassen-Winograd and Karatsuba may be better known, but still, a reference could help.

 * _matrix_times_matrix is not documented.

 * `__init__`, `__cinit__` do not specify their arguments.

 * `_lmul_`, `__neg__`, `__richcmp__`, `__invert__`, `__reduce__`, `set_unsafe` and `get_unsafe` do not state what they do, and the method names do not occur in the example (so, it should be marked as an indirect doctest). 

 * cdef'd methods such as rescale_row_c or add_multiple_of_row_c or swap_rows_c and so on may not be as easily visible by the user than Python methods. However, as a courtesy to developers who actually read the source file, the arguments of those methods should be specified.

 * "echelonize" should state what it does and what its optional arguments are. If I am not mistaken, it changes the matrix inplace, and that should be documented.

 * When I read "Classical cubic matrix multiplication.", I first understood that the matrix is cubic. But perhaps I'm a bit square here...
 
So, that's "needs work" for now.

Since there should be a vote on sage-devel anyway, we might also ask whether it should be included in the docs. I am still not sure: On the one hand, I think a reference manual should be thorough. On the other hand, all "new" methods that are no cdef'd methods and do not start with an underscore overwrite methods from super-classes that are documented elsewhere.


---

Comment by SimonKing created at 2011-08-20 15:40:41

For the record: I asked for a [vote on sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/bf75a0509d3ec978).


---

Comment by leif created at 2011-08-20 16:26:38

Replying to [comment:45 malb]:
> Replying to [comment:44 kcrisman]:
> > I agree that it is very annoying to have two things inside the same spkg.  
> > There is, for instance, an open ticket to remove rpy2 from the r spkg.  
> 
> Well, it makes it easier to re-use tuning results. For example, I plan to run the cache tuning only once, i.e. for M4RI and M4RIE would re-use the results.

Save them to some file in, say, `$SAGE_ROOT/local/share/m4ri/`?


---

Comment by leif created at 2011-08-20 16:51:38

P.S.: This would perhaps even allow specifying cache sizes manually, though the proper way would be something like

```sh
$ export M4RI_EXTRA_OPTS="--L1-cache-size=32 --L2-cache-size=1024" # passed to M4RI[E]'s 'configure'
$ sage -i m4rie
```

(And similar options for other cache parameters like the cache line sizes.)

Specifying these may at least _speed up_ the tuning (by omitting a lot of tries); don't know if you could skip tuning, given these, in whole.

Storing and using tuning parameters analoguous to GMP's `gmp-mparams.h` (including defaults for a couple of platforms / processors) wouldn't be bad either; then [optionally] bypassing self-tuning would really make sense.

[Disclaimer: Haven't looked at the spkg at all, so there might be better or other ways to achieve this.]


---

Comment by leif created at 2011-08-20 18:03:21

Replying to [comment:91 leif]:
> [Disclaimer: Haven't looked at the spkg at all, so there might be better or other ways to achieve this.]

Looks like you're currently not trying to query any of

```C
    _SC_LEVEL1_ICACHE_SIZE
    _SC_LEVEL1_ICACHE_ASSOC
    _SC_LEVEL1_ICACHE_LINESIZE
    _SC_LEVEL1_DCACHE_SIZE
    _SC_LEVEL1_DCACHE_ASSOC
    _SC_LEVEL1_DCACHE_LINESIZE
    _SC_LEVEL2_CACHE_SIZE
    _SC_LEVEL2_CACHE_ASSOC
    _SC_LEVEL2_CACHE_LINESIZE
    _SC_LEVEL3_CACHE_SIZE
    _SC_LEVEL3_CACHE_ASSOC
    _SC_LEVEL3_CACHE_LINESIZE
    _SC_LEVEL4_CACHE_SIZE
    _SC_LEVEL4_CACHE_ASSOC
    _SC_LEVEL4_CACHE_LINESIZE
```

(with `sysconf()`). At least some of these values aren't available on every platform, but if they are, you could perhaps use them.

AFAIK you'd have to set some feature test macro before including `unistd.h` on Solaris, although I doubt it supports any of the above.


---

Comment by malb created at 2011-08-20 18:05:45

* there's an optional parameter `--with-cachesize` for M4RI's configure which allows to specify L1 and L2.
 * However, this is not exported to Sage, i.e. M4RI_EXTRA_OPTS does not exist yet.
 * M4RIE does not re-tune any more but re-uses the data from M4RI.
 * In my experience (on i7s for example) tuning is much better than using the data reported by the CPU. That is, if one trusts L1 and L2 as reported by the CPU (which are correct) the code is much slower than tuning which essentially uses L3 instead of L2.


---

Comment by malb created at 2011-08-20 18:12:55

Replying to [comment:88 SimonKing]:
 
> 2. I found some issues with the "randomize" methods. 
> 
>   i) The randomize method in sage/libs/ntl/ntl_mat_GF2E.pyx is not documented (thus, also has no tests), and it lacks the usual optional arguments `density` and `nonzero`.

Okay, I'll take a look. Note that `ntl_mat_GF2E` does not have the same interface as normal matrices though. But it makes sense to make it consistent where possible.
 
>   ii) The doc of Matrix_mod2e_dense.randomize gives no use cases for the optional arguments. Actually, the behaviour when passing the optional arguments is clearly not what we want:

Okay, I'll take a look.

> 3. The doc of many methods needs some polishing.
> 
>  * It would be nice to have a reference to research articles. I had never heard of Travolta tables before. Strassen-Winograd and Karatsuba may be better known, but still, a reference could help.

There is no research article on Travolta tables yet since I made them up for M4RIE. But for the other ones I can add references.
 


>  * _matrix_times_matrix is not documented.

This is an internal method which is part of the standard matrix interface. I'd say it is hence understood what it does.
 
>  * `__init__`, `__cinit__` do not specify their arguments.

Okay.

>  * `_lmul_`, `__neg__`, `__richcmp__`, `__invert__`, `__reduce__`, `set_unsafe` and `get_unsafe` do not state what they do, and the method names do not occur in the example (so, it should be marked as an indirect doctest). 

These are special methods where either Python or our Matrix classes define what they do. I'd say it is hence understood what they do.

>  * cdef'd methods such as rescale_row_c or add_multiple_of_row_c or swap_rows_c and so on may not be as easily visible by the user than Python methods. However, as a courtesy to developers who actually read the source file, the arguments of those methods should be specified.

Okay.
 
>  * "echelonize" should state what it does and what its optional arguments are. If I am not mistaken, it changes the matrix inplace, and that should be documented.

Okay.
 
>  * When I read "Classical cubic matrix multiplication.", I first understood that the matrix is cubic. But perhaps I'm a bit square here...
>  
> So, that's "needs work" for now.
 
> Since there should be a vote on sage-devel anyway, we might also ask whether it should be included in the docs. I am still not sure: On the one hand, I think a reference manual should be thorough. On the other hand, all "new" methods that are no cdef'd methods and do not start with an underscore overwrite methods from super-classes that are documented elsewhere.

I'd much rather add a note to the reference manual which lists which library drives which base field?


---

Comment by leif created at 2011-08-20 18:32:46

The `dist/` (Debian) directory can and should be deleted (see #5903).


---

Comment by malb created at 2011-08-20 21:10:22

Agreed!


---

Comment by malb created at 2011-08-22 03:00:38

Changing status from needs_work to needs_review.


---

Comment by malb created at 2011-08-22 03:00:38

The updated patch + updated SPKG should address the comments above. Simon, as an added bonus the new SPKG also contains the faster scalar product.


---

Comment by malb created at 2011-08-22 05:25:35

doctests pass on sage.math btw.


---

Comment by SimonKing created at 2011-08-22 07:45:51

Changing status from needs_review to needs_info.


---

Comment by SimonKing created at 2011-08-22 07:45:51

I did `sage -f http://sage.math.washington.edu/home/malb/spkgs/libm4rie-20110821.spkg`, I removed the old version of `m4rie_for_sage.patch`, qimported the new one, checked that my computer was really downloading the new version, did qpush, and `sage -br`.

However, I get

```
sage: MS = MatrixSpace(GF(64,'a'),800,800)
sage: A = MS.random_element(densitiy=1)
sage: RR(A.density())
0.984492187500000
sage: A = MS.random_element(densitiy=0.001)
sage: RR(A.density())
0.984167187500000
```

I verified (by `A.randomize?`) that the new patch is applied.

Do you have any clue why that happened?


---

Comment by SimonKing created at 2011-08-22 07:48:56

Strange enough, the doc tests for matrix_mod2e_dense pass.

So, perhaps `MS.random_element(...)` is calling `randomize(...)` in a wrong way.


---

Comment by SimonKing created at 2011-08-22 07:52:22

Yes, it is passing the wrong arguments, due to a typo on my end: I wrote densitiy, not density). Sorry.


---

Comment by SimonKing created at 2011-08-22 07:52:22

Changing status from needs_info to needs_review.


---

Comment by SimonKing created at 2011-08-22 09:33:48

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-08-22 09:33:48

__Questions / To do__

* The hg repository of the spkg needs being updated. Even though the last log entry is of today (August 22), the status report is

```
$ hg status
? config.log
? m4rie/.hgignore
? m4rie/.hgtags
? m4rie/AUTHORS
? m4rie/COPYING
? m4rie/ChangeLog
? m4rie/INSTALL
? m4rie/Makefile.am
? m4rie/Makefile.in
? m4rie/NEWS
? m4rie/README
? m4rie/aclocal.m4
? m4rie/bench/Makefile.am
? m4rie/bench/Makefile.in
? m4rie/bench/bench_elimination.cc
? m4rie/bench/bench_multiplication.cc
? m4rie/bench/bench_smallops.cc
? m4rie/bench/benchmarking.cc
? m4rie/bench/benchmarking.h
? m4rie/bench/cpucycles-20060326/alpha.c
? m4rie/bench/cpucycles-20060326/alpha.h
? m4rie/bench/cpucycles-20060326/amd64cpuinfo.c
? m4rie/bench/cpucycles-20060326/amd64cpuinfo.h
? m4rie/bench/cpucycles-20060326/amd64tscfreq.c
? m4rie/bench/cpucycles-20060326/amd64tscfreq.h
? m4rie/bench/cpucycles-20060326/clockmonotonic.c
? m4rie/bench/cpucycles-20060326/clockmonotonic.h
? m4rie/bench/cpucycles-20060326/compile
? m4rie/bench/cpucycles-20060326/cpucycles.html
? m4rie/bench/cpucycles-20060326/do
? m4rie/bench/cpucycles-20060326/do.notes
? m4rie/bench/cpucycles-20060326/gettimeofday.c
? m4rie/bench/cpucycles-20060326/gettimeofday.h
? m4rie/bench/cpucycles-20060326/hppapstat.c
? m4rie/bench/cpucycles-20060326/hppapstat.h
? m4rie/bench/cpucycles-20060326/powerpcaix.c
? m4rie/bench/cpucycles-20060326/powerpcaix.h
? m4rie/bench/cpucycles-20060326/powerpclinux.c
? m4rie/bench/cpucycles-20060326/powerpclinux.h
? m4rie/bench/cpucycles-20060326/powerpcmacos.c
? m4rie/bench/cpucycles-20060326/powerpcmacos.h
? m4rie/bench/cpucycles-20060326/sparc32psrinfo.c
? m4rie/bench/cpucycles-20060326/sparc32psrinfo.h
? m4rie/bench/cpucycles-20060326/sparcpsrinfo.c
? m4rie/bench/cpucycles-20060326/sparcpsrinfo.h
? m4rie/bench/cpucycles-20060326/test.c
? m4rie/bench/cpucycles-20060326/x86cpuinfo.c
? m4rie/bench/cpucycles-20060326/x86cpuinfo.h
? m4rie/bench/cpucycles-20060326/x86tscfreq.c
? m4rie/bench/cpucycles-20060326/x86tscfreq.h
? m4rie/config.guess
? m4rie/config.sub
? m4rie/configure
? m4rie/configure.ac
? m4rie/depcomp
? m4rie/gf2e_cxx/finite_field_givaro.h
? m4rie/install-sh
? m4rie/ltmain.sh
? m4rie/m4/ax_check_compiler_flags.m4
? m4rie/m4/ax_openmp.m4
? m4rie/m4/libtool.m4
? m4rie/m4/ltoptions.m4
? m4rie/m4/ltsugar.m4
? m4rie/m4/ltversion.m4
? m4rie/m4/lt~obsolete.m4
? m4rie/missing
? m4rie/tests/test_elimination.cc
? m4rie/tests/test_multiplication.cc
? m4rie/tests/test_smallops.cc
? m4rie/tests/testing.h
```


* spkg-check does not seem to work. After opening the package and working in a sage shell, I get

```
$ ./spkg-check 
./spkg-check: Zeile 30: cd: build/m4ri: Datei oder Verzeichnis nicht gefunden
Testing the M4RI library
make: *** Keine Regel, um »check« zu erstellen.  Schluss.
Error testing M4RI
```


* Have you already implemented the ideas for storing the cache size information, so that installation of the package does not take so long? Or will that be in a future release?

* You said you'd much rather add a note to the reference manual which lists which library drives which base field. Did you do so? I can not find it in the patch.

__Done__

* The long doctests in doc/ and sage/ pass on my machine. The doctests in sage/matrix pass on 32 bit solaris.

* Randomize seems to work fine.

* Scalar multiplication has improved:

```

sage: MS = MatrixSpace(GF(64,'a'),5000,5000)
sage: K = MS.base_ring()
sage: c = K.random_element()
sage: A = MS.random_element()
sage: %time A*c
CPU times: user 0.05 s, sys: 0.01 s, total: 0.06 s
Wall time: 0.06 s
5000 x 5000 dense matrix over Finite Field in a of size 2^6
sage: MS1 = MatrixSpace(GF(64,'a'),1,5000)
sage: B = MS1.random_element()
sage: %timeit B*c
625 loops, best of 3: 51.5 µs per loop
```


* The docs are now almost fine from my point of view. We only have

```
$ sage -coverage sage/matrix/matrix_mod2e_dense.pyx
----------------------------------------------------------------------
sage/matrix/matrix_mod2e_dense.pyx
SCORE sage/matrix/matrix_mod2e_dense.pyx: 100% (27 of 27)

Possibly wrong (function name doesn't occur in doctests):
         * Matrix_mod2e_dense _multiply_travolta(Matrix_mod2e_dense self, Matrix_mod2e_dense right):
         * Matrix_mod2e_dense _multiply_karatsuba(Matrix_mod2e_dense self, Matrix_mod2e_dense right):
         * Matrix_mod2e_dense _multiply_strassen(Matrix_mod2e_dense self, Matrix_mod2e_dense right, cutoff=0):
         * ModuleElement _lmul_(self, RingElement right):

----------------------------------------------------------------------
```

and I suggest that I add a referee patch that simply adds a "indirect doctest" in the appropriate places.

__Conclusion__

I put it "needs work", but that's only since I'd like to create a referee patch. If you did not add the information on which library drives which base field yet, I can do so as well.

Please check in the changes to the hg repository, or "hg ignore" them. Please fix the self tests (or tell me why my attempt to call spkg-check did not work).


---

Comment by SimonKing created at 2011-08-22 09:37:27

Replying to [comment:103 SimonKing]:
> I put it "needs work", but that's only since I'd like to create a referee patch.

Sorry, I did a mistake when editing. I wrote that line before noticing the spkg-check and hg status issues. These need fixes as well.


---

Comment by leif created at 2011-08-22 09:58:32

Replying to [comment:103 SimonKing]:
> * spkg-check does not seem to work. After opening the package and working in a sage shell, I get

```
$ ./spkg-check 
./spkg-check: Zeile 30: cd: build/m4ri: Datei oder Verzeichnis nicht gefunden
Testing the M4RI library
make: *** Keine Regel, um »check« zu erstellen.  Schluss.
Error testing M4RI
```


I guess you'll first have to build, which also creates the directory and the Makefile there.

Did you try `env SAGE_CHECK=yes sage -f ...`?

If you've run `sage -i` also with `-s`, entering the build directory and doing `./spkg-check` should also work.


---

Comment by SimonKing created at 2011-08-22 13:00:16

Replying to [comment:105 leif]:
> I guess you'll first have to build, which also creates the directory and the Makefile there.
> 
> Did you try `env SAGE_CHECK=yes sage -f ...`?

I tried now, but it did not work.

> If you've run `sage -i` also with `-s`, entering the build directory and doing `./spkg-check` should also work.

Well, I learnt that `./spkg-check` should work if you have simply have opened the package and use a sage shell.


---

Comment by SimonKing created at 2011-08-22 13:20:28

Replying to [comment:106 SimonKing]:
> Well, I learnt that `./spkg-check` should work if you have simply have opened the package and use a sage shell.

And `export SAGE_CHECK="yes"` followed by `sage -f` should work as well. But it doesn't


---

Comment by malb created at 2011-08-22 17:45:41

Replying to [comment:103 SimonKing]:
> * The hg repository of the spkg needs being updated. Even though the last log entry is of today (August 22), the status report is

Agreed & fixed in the SPKG I'll update in a minute.
 
> * spkg-check does not seem to work. After opening the package and working in a sage shell, I get

Fixed.
 
> * Have you already implemented the ideas for storing the cache size information, so that installation of the package does not take so long? Or will that be in a future release?

I only implemented that M4RIE avoids detecting the cache size. It has nothing to do with cache size detection any more it just uses M4RI's results.

> * You said you'd much rather add a note to the reference manual which lists which library drives which base field. Did you do so? I can not find it in the patch.

We should open a new ticket for this?
 
> * The docs are now almost fine from my point of view. We only have
> and I suggest that I add a referee patch that simply adds a "indirect doctest" in the appropriate places.

I'll do that.


---

Comment by malb created at 2011-08-22 17:53:55

SPKG + patch updated.


---

Comment by malb created at 2011-08-22 17:53:55

Changing status from needs_work to needs_review.


---

Comment by was created at 2011-08-24 23:48:36

Changing keywords from "m4ri" to "m4ri, sd32".


---

Comment by SimonKing created at 2011-08-26 07:03:29

m4rie_for_sage.patch did not apply on top of my private patch chain. The conflict is with #4260. So, one should be made dependent on the other.

Martin, what seems to be more stable? This M4RIE patches? Or the Linbox patches?


---

Comment by SimonKing created at 2011-08-26 07:03:29

Changing status from needs_review to needs_info.


---

Comment by malb created at 2011-08-26 12:39:47

Changing status from needs_info to needs_review.


---

Comment by malb created at 2011-08-26 12:39:47

Replying to [comment:112 SimonKing]:
> m4rie_for_sage.patch did not apply on top of my private patch chain. 

Ouch, how unfortunate. I guess it's in `matrix_space.py`?

> The conflict is with #4260. So, one should be made dependent on the other.

I'm not so sure about this. They are fairly independent. I suggest each is reviewed independently and whichever gets in later is re-based accordingly.

> Martin, what seems to be more stable? This M4RIE patches? Or the Linbox patches?

I'd say M4RIE:
 * the M4RIE interface has been around for months and months
 * I'm willing to debug any issue that might come up because I'm quite invested in this ticket.
 * Many people have looked at M4RIE over the time.
 * The LinBox switch-over has not received a single review yet.
 * You reported some speed issues with the new LinBox interface
 * It is unclearly whether the new LinBox interface works/builds on anything besides 64-bit Linux.


---

Comment by SimonKing created at 2011-08-26 12:51:43

Replying to [comment:113 malb]:
> Replying to [comment:112 SimonKing]:
> > m4rie_for_sage.patch did not apply on top of my private patch chain. 
> 
> Ouch, how unfortunate. I guess it's in `matrix_space.py`?

Sure. It is when the `__matrix_class` is determined. And of course I have already modified the patches in my private patch chain, so that I can continue to work...

> I'm not so sure about this. They are fairly independent. I suggest each is reviewed independently and whichever gets in later is re-based accordingly.

Makes sense.


---

Comment by malb created at 2011-09-01 09:56:05

Changing status from needs_review to needs_work.


---

Comment by malb created at 2011-09-01 09:56:05

This clearly needs work since M4RIE does not add the appropriate -msse2 flag if M4RI was built with it.


---

Comment by SimonKing created at 2011-10-04 07:02:05

Is it still "needs work", or does your new patch fixes the -msse2 flag issue? The official work issues are `Fix some docs and fix "randomize()"`. Is that still relevant?


---

Comment by malb created at 2011-10-04 11:34:07

I've released a new version of M4RIE, 

   cf. https://bitbucket.org/malb/m4rie/wiki/M4RIE-20111004

which fixes bugs, deals with M4RI SSE2 flags correctly, implements asymptotically fast Gaussian elimination and triangular system solving, has a new Travolta table creation which is much much faster ...

The attached patch also takes care of any work issues I am aware of.

I've tested this code (patch + SPKG) on cicero, sage.math, bsd. I'm currently testing on iras.


---

Comment by malb created at 2011-10-04 11:34:07

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-10-04 11:41:26

Sorry, I will be unable to review for a few days. #11339 has destroyed most of my patch chain, and I will be busy with rebasing the majority of the patches that I've been working on in the last couple of weeks.


---

Comment by malb created at 2011-10-04 11:47:25

Yep, expected that much. Sorry, for being involved causing you this much trouble!


---

Comment by malb created at 2011-10-04 14:59:18

doctests also pass on iras, except for R doctests since I didn't bother to look up how to build R on iras.


---

Comment by SimonKing created at 2011-10-26 20:45:23

#4260 has been merged into sage-4.7.3.alpha0, but there is a conflict with the patch from here, namely in sage/matrix/matrix_space.py. I suggest that the patch will be rebased against #4260.


---

Comment by SimonKing created at 2011-10-26 20:45:23

Changing status from needs_review to needs_work.


---

Comment by malb created at 2011-10-27 17:52:48

rebased to 4.7.3.alpha0


---

Attachment

okay, rebased.


---

Comment by malb created at 2011-10-27 17:53:06

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-10-28 05:25:19

Replying to [comment:124 malb]:
> okay, rebased.

Thank you! The new patch applies cleanly.


---

Comment by SimonKing created at 2011-10-28 13:18:35

It seems to me that all previous complaints are addressed in the new spkg and patches.

In particular, if one has opened the spkg, starts a sage shell and does ./spkg-install, then ./spkg-check works, with all tests. passing.

hg status in the spkg is fine, and SPKG.txt looks fine as well (except a typo in the last line, should be "split from", not "split form" - but please leave that error, since the Gods don't like perfection among the mortals :)

Moreover, `sage -coverage sage/matrix/matrix_mod2e_dense.pyx` is OK.

All doc tests pass as well, and I think the original problems with t2 had been dealt with.

Thus, I hope all participants agree that it is a positive review!


---

Comment by SimonKing created at 2011-10-28 13:18:35

Changing status from needs_review to positive_review.


---

Comment by leif created at 2011-10-28 13:29:30

Replying to [comment:126 SimonKing]:
> Thus, I hope all participants agree that it is a positive review!

Sollte ich dein Urteil infrage stellen weil du uns für sterblich hältst?


---

Comment by jdemeyer created at 2011-11-15 08:55:13

Resolution: fixed


---

Comment by jdemeyer created at 2011-11-20 10:24:29

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-11-20 10:24:29

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2011-11-20 10:24:29

Reopened because of issues with #4260.


---

Comment by jdemeyer created at 2011-11-20 10:24:37

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2011-11-20 10:24:44

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-12-01 08:12:30

Resolution: fixed
