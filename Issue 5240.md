# Issue 5240: Updayte FLINT to 1.1.1 (latest upstream)

Issue created by migration from https://trac.sagemath.org/ticket/5240

Original creator: mabshoff

Original creation time: 2009-02-12 01:00:34

Assignee: tbd

CC:  burcin

From the flint-devel mailing list:

```
I've just release FLINT 1.1.1. This is a service release to fix some
SERIOUS issues in FLINT 1.1.0. I strongly recommend upgrading!

The issues fixed were as follows:

* fmpz_poly_gcd had a serious bug in it (which was actually in the
function fmpz_poly_gcd_heuristic) which caused it to return the
****WRONG ANSWER**** in certain cases, specifically when aliasing one
of the inputs with the output and where the heuristic gcd was not
sufficient to compute the gcd. In this case the heuristic gcd would
corrupt the output (which is aliased with an input) and pass the
corrupted inputs to another gcd algorithm, which would then get things
wrong. This occurs rarely, as the heuristic gcd cannot compute the gcd
in rare cases. I was unable to get it to return a wrong answer except
in the case where the inputs both had a Gaussian content whose gcd was
non-trivial. However, it may theoretically occur in other cases.

* fmpz_poly_gcd_subresultant needed a special case to deal with length
1 polynomials. Actually this probably did not cause a bug, but was
fixed anyway as a precaution (and for performance reasons).

* _fmpz_poly_scalar_mul_fmpz could cause a segmentation fault. This
was due to the fact that GMP, when multiplying integers of n1 and n2
limbs, automatically takes n1 + n2 limbs to write the result, even if
they are not all needed. I changed the interface of the precached FFT
multiplication some time ago to use this same semantics, but did not
adjust the scalar multiplication function accordingly.

* test__fmpz_poly_scalar_div_fmpz did not allocate sufficient space in
the output and so could segfault in very rare cases.

* test_fmpz_poly_scalar_div_fmpz did not allocate sufficient space in
the output and so could segfault in very rare cases.

* test_fmpz_poly_scalar_div_mpz did not allocate sufficient space in
the output and so could segfault in very rare cases.

Bill.
```

Sage is not affected by all of the bugs, but at least some of the crash bugs do affect Sage.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-12 01:00:52

Changing assignee from tbd to mabshoff.


---

Comment by mabshoff created at 2009-02-12 01:00:52

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-16 05:17:01

We are still shipping FLINT 1.0.21 in Sage 3.3, so let's bump the update post 3.3 since it is rather late to do this.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 05:17:30

Burcin: Have you done any work to update to FLINT 1.1 in Sage yet?

Cheers,

Michael


---

Comment by burcin created at 2009-02-22 11:13:20

Nothing beyond trivially replacing the source directory in the package, and that was only for 1.1.0. Since FLINT will link to zn_poly, I assume the package needs further changes.

If you put up a package, I can quickly check if any changes are required in the library for the update. Unfortunately, I don't think I'll have time to prepare a package myself.

Cheers,

Burcin


---

Comment by was created at 2009-03-01 04:56:13

I created an spkg:

http://sage.math.washington.edu/home/wstein/patches/flint-1.1.1.spkg


---

Comment by burcin created at 2009-03-01 15:28:26

With the package from comment:6, I get:


```
...
Finished extraction
****************************************************
Host system
uname -a:
Linux karr 2.6.28-tuxonice #1 SMP PREEMPT Tue Jan 13 08:45:33 CET 2009 x86_64 Intel(R) Core(TM)2 Duo CPU T9300 @ 2.50GHz GenuineIntel GNU/Linux
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: x86_64-pc-linux-gnu
Configured with: /var/portage/tmp/sys-devel-gcc-4.1.2/work/gcc-4.1.2/configure --prefix=/usr --bindir=/usr/x86_64-pc-linux-gnu/gcc-bin/4.1.2 --includedir=/usr/lib/gcc/x86_64-pc-linux-gnu/4.1.2/include --datadir=/usr/share/gcc-data/x86_64-pc-linux-gnu/4.1.2 --mandir=/usr/share/gcc-data/x86_64-pc-linux-gnu/4.1.2/man --infodir=/usr/share/gcc-data/x86_64-pc-linux-gnu/4.1.2/info --with-gxx-include-dir=/usr/lib/gcc/x86_64-pc-linux-gnu/4.1.2/include/g++-v4 --host=x86_64-pc-linux-gnu --build=x86_64-pc-linux-gnu --disable-altivec --enable-nls --without-included-gettext --with-system-zlib --disable-checking --disable-werror --enable-secureplt --enable-multilib --enable-libmudflap --disable-libssp --disable-libgcj --enable-languages=c,c++,treelang,fortran --enable-shared --enable-threads=posix --enable-__cxa_atexit --enable-clocale=gnu
Thread model: posix
gcc version 4.1.2 (Gentoo 4.1.2 p1.3)
****************************************************
Found gcc 4 or later
Deleting old FLINT
gcc -std=c99 -I/home/burcin/sage/sage-3.3.alpha5/local/include/ -I/home/burcin/sage/sage-3.3.alpha5/local/include -I -fPIC -funroll-loops  -O3 -c mpn_extras.c -o mpn_extras.o
...
gcc -std=c99 -I/home/burcin/sage/sage-3.3.alpha5/local/include/ -I/home/burcin/sage/sage-3.3.alpha5/local/include -I -fPIC -funroll-loops  -O3 -c mpz_mat.c -o mpz_mat.o
gcc -std=c99 -fPIC -shared -o libflint.so mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o zmod_poly.o NTL-interface.o theta.o zmod_mat.o mpz_mat.o  -L/home/burcin/sage/sage-3.3.alpha5/local/lib/ -L  -lgmp -lpthread -lntl -lm -lstdc++ 
/usr/lib/gcc/x86_64-pc-linux-gnu/4.1.2/../../../../x86_64-pc-linux-gnu/bin/ld: mpn_extras.o: relocation R_X86_64_32S against `FFT_SQR_TWK' can not be used when making a shared object; recompile with -fPIC
mpn_extras.o: could not read symbols: Bad value
collect2: ld returned 1 exit status
make: *** [libflint.so] Error 1
Error building flint shared library.

real    0m26.358s
user    0m21.673s
sys     0m0.924s
sage: An error occurred while installing flint-1.1.1
Please email sage-devel http://groups.google.com/group/sage-devel
...
```


I have no idea what the error about the shared library and -fPIC means. Looking at the gcc flags in the previous lines, -fPIC is already there.

BTW, deleting the library files before the build is not a good idea. In this case, the package corrupted my Sage install.


---

Comment by was created at 2009-03-01 16:32:02

I've posted:

http://sage.math.washington.edu/home/wstein/patches/flint-1.1.2.spkg

It does not address Burcin's comment, but updates the flint version.   This new version works fine on OS X but does *not* work on Linux. 

Regarding "deleting old FLINT", I didn't write that.  And I strongly agree it is a very annoying thing to do!  One should only do that if the build succeeds.


---

Comment by mabshoff created at 2009-03-01 16:37:39

I guess we ought to upgrade to 1.1.2 :)

```
I have issued a bug release for FLINT. This tries to fix some dramatic
slowdowns that occur in fmpz_poly_divrem and fmpz_poly_pseudo_divrem,
noted by William Stein.

Essentially the issue only showed up when calling these functions
repeatedly with some of the same polynomials as parameters (perhaps
permuted). This is common in euclidean gcd-like algorithms (e.g.
polynomial signature computation using Sturm sequences).

Along the way, I noted a handful of potentially unsafe lines of code
and I fixed those (unfortunately the unmanaged _fmpz_poly_left_shift
function doesn't like length 0 polynomials with zero limbs allocated
for coefficients), and this can't be fixed without radically altering
lots of FLINT 1.1.x. The managed version of this function is safe.
However some of the division code uses the unmanaged version and in a
couple of places where there may also be no limbs allocated. These
could have caused segfaults, though I expect their chance of doing so
was pretty low, though it is probably possible to construct
polynomials which could have caused the issue.

Bill.
```


Cheers,

Michael


---

Comment by was created at 2009-03-01 18:31:21

Hi,

The spkg here now works for me on sage.math (at least it builds fine).  Bill helped me fix an issue with missing -fPIC.

http://sage.math.washington.edu/home/wstein/patches/flint-1.1.2.spkg

I fixed the build issues.  

I ran the full sage test suite and all tests pass on 3.4.alpha0...

However, probably related, 190GB of RAM were being used.  So there may be a massive memory leak... somehow.


---

Comment by burcin created at 2009-03-15 11:58:46

There is a package for the latest FLINT version here:

http://sage.math.washington.edu/home/burcin/flint/flint-1.2.1.spkg

It builds fine on my laptop (Gentoo, gcc 4.1.2, Core2Duo T9300) and sage.math. All sage and FLINT tests pass.

Here are the list of changes (from SPKG.txt):

 * Upgraded to newest stable version
 * delay deleting library in local/lib until build is complete
 * added zmod_mat-test and NTL-interface-test to spkg-check
 * spkg-check now exits on error
 * enabled tests

With this version, I don't see any problems with memory usage during tests.


---

Comment by burcin created at 2009-03-15 11:58:46

Changing component from algebra to packages.


---

Comment by burcin created at 2009-03-31 09:54:06

New version of the package with FLINT 1.2.2 is here:

http://sage.math.washington.edu/home/burcin/flint/flint-1.2.2.spkg


---

Comment by mabshoff created at 2009-03-31 09:58:37

Incidentally Bill asked me about this update, so we should try to get this into 3.4.1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 20:35:29

FLINT 1.2.3 is out which fixes a bug Burcin pointed out[here](http://sourceforge.net/mailarchive/forum.php?thread_name=20090331192030.7634e082%40karr&forum_name=flint-devel). I will update the spkg shortly unless someone beats me to it.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-03 02:18:22

I update to FLINT 1.2.3, but there is some issue with `__thread` on OSX:

```
gcc -std=c99 -I/Users/mabshoff/sage-3.3.rc3/local/include/ -I/Users/mabshoff/sage-
3.3.rc3/local/include  -fPIC -funroll-loops   -O3 -c memory-manager.c -o memory-
manager.o
memory-manager.c:165: error: thread-local storage not supported for this target
memory-manager.c:166: error: thread-local storage not supported for this target
memory-manager.c:167: error: thread-local storage not supported for this target
memory-manager.c:168: error: thread-local storage not supported for this target
memory-manager.c:169: error: thread-local storage not supported for this target
memory-manager.c: In function ‘flint_stack_alloc’:
memory-manager.c:175: error: thread-local storage not supported for this target
memory-manager.c:176: error: thread-local storage not supported for this target
memory-manager.c:177: error: thread-local storage not supported for this target
memory-manager.c:178: error: thread-local storage not supported for this target
memory-manager.c:179: error: thread-local storage not supported for this target
memory-manager.c:180: error: thread-local storage not supported for this target
memory-manager.c: At top level:
memory-manager.c:329: error: thread-local storage not supported for this target
memory-manager.c:330: error: thread-local storage not supported for this target
make: *** [memory-manager.o] Error 1
Failed to build FLINT dylib.
```


Bill recommended removing `__thread` for now in Sage since we are not using any threading. There is a workaround for OSX - see http://lists.apple.com/archives/xcode-users/2006/Jun/msg00551.html

```
__thread is not supported. The specification is somewhat ELF- specific, which makes it a bit of a challenge.

Thread-local storage is supported, however. Take a look at the man page for pthread_getspecific, for example.
```


The latest spkg is at

  http://sage.math.washington.edu/home/mabshoff/SPKG/flint-1.2.3.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-03 02:57:58

There is another issue on Solaris 10:

```
gcc -std=c99 -I/home/mabshoff/build-3.3/sage-3.3-fulvia/local/include/ 
-I/home/mabshoff/build-3.3/sage-3.3-fulvia/local/include  -fPIC -funroll-loops   
-O3 -c mpn_extras-test.c -o mpn_extras-test.o
In file included from /usr/include/sys/time.h:99,
                 from profiler.h:30,
                 from test-support.h:36,
                 from mpn_extras-test.c:35:
/usr/include/sys/types.h:536: error: duplicate ‘unsigned’
make: *** [mpn_extras-test.o] Error 1
Error building the test suite for FLINT
```


The fix here is to undef ulong in profile.h right before including time.h and the other two headers.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-04 04:18:24

FLINT 1.2.4 is out which should fix the above problems :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-04 05:10:55

The latest spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc0/flint-1.2.4.spkg

It builds and passes its test suite fine on Linux, OSX and Solaris.

Since this is merely an updated version of Burcin's spkg I am giving this a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-04 05:12:16

Merged in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-04 05:12:16

Resolution: fixed


---

Comment by mabshoff created at 2009-04-04 06:30:36

Hmm, the following failure is cause by the new FLINT:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1487:
    sage: B = A.change_ring(Integers(p**prec)); B               # long time
Expected:
    [74311982 57996908]
    [95877067 25828133]
Got:
    [54572546 87269244]
    [10839343 79974813]
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1490:
    sage: B.det()                                               # long time
Expected:
    10007
Got:
    29700776
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1492:
    sage: B.trace()                                             # long time
Expected:
    66
Got:
    34407310
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc0/devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1562:
    sage: B.det()                                               # long time
Expected:
    11 + 484*t^2 + 451*t^3 + O(t^4)
Got:
    245 + 240*t + 724*t^2 + 808*t^3 + O(t^4)
**********************************************************************
```

