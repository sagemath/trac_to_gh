# Issue 9358: zn_poly passes all tests on on Solaris 10 64-bit SPARC, but fails to install

Issue created by migration from https://trac.sagemath.org/ticket/9358

Original creator: drkirkby

Original creation time: 2010-06-28 16:47:26

Assignee: drkirkby

CC:  jhpalmieri jsp

znpoly passes about 40 self-tests, but fails to install properly. 


```
zn_array_mulmid_fft()... ok
zn_array_mul_fft_dft()... ok
zn_array_invert()... ok

All tests passed.
gcc -O3 -g -m64 -fPIC -L. -I/export/home/drkirkby/sage-4.5.alpha0/local/include 
-I./include -DNDEBUG -o src/tuning.o -c src/tuning.c
In file included from ./include/zn_poly.h:75,
                 from ./include/zn_poly_internal.h:41,
                 from src/tuning.c:28:
./include/wide_arith.h:297:2: warning: #warning No assembly implementation of wi
de multiplication available for this machine; using generic C code instead.
ar -r libzn_poly.a src/array.o src/invert.o src/ks_support.o src/mulmid.o src/mu
lmid_ks.o src/misc.o src/mpn_mulmid.o src/mul.o src/mul_fft.o src/mul_fft_dft.o 
src/mul_ks.o src/nuss.o src/pack.o src/pmf.o src/pmfvec_fft.o src/tuning.o src/z
n_mod.o
ar: creating libzn_poly.a
ranlib libzn_poly.a
gcc -shared -m64  -Wl,-soname,libzn_poly-`cat VERSION`.so -o libzn_poly-`cat VER
SION`.so src/array.o src/invert.o src/ks_support.o src/mulmid.o src/mulmid_ks.o 
src/misc.o src/mpn_mulmid.o src/mul.o src/mul_fft.o src/mul_fft_dft.o src/mul_ks
.o src/nuss.o src/pack.o src/pmf.o src/pmfvec_fft.o src/tuning.o src/zn_mod.o -L
/export/home/drkirkby/sage-4.5.alpha0/local/lib -lgmp -lm
ld: warning: option -o appears more than once, first setting taken
ld: fatal: file libzn_poly-0.9.so: unknown file type
ld: fatal: File processing errors. No output written to libzn_poly-0.9.so
collect2: ld returned 1 exit status
make: *** [libzn_poly.so] Error 1
Error building zn_poly shared library.

real	1m38.825s
user	1m34.368s
sys	0m3.849s
sage: An error occurred while installing zn_poly-0.9.p4
```


This looks like a problem in spkg-install, which is undoubtedly my fault. The script has in if/elif/else/fi which considers

 * A 64-bit build
 * A Solaris build with the Sun linker. 

It does *not* cover the possibility of a 64-bit build on Solaris with the Sun linker. 

This should be hopefully quite easy to fix.


---

Attachment

Log file of building on a Sun Blade 1000 SPARC (64-bit build)


---

Comment by jhpalmieri created at 2010-08-02 22:49:46

This also fails with a 64-bit build on fulvia (Solaris on x86), by the way.


---

Comment by drkirkby created at 2010-08-04 00:04:10

Replying to [comment:2 jhpalmieri]:
> This also fails with a 64-bit build on fulvia (Solaris on x86), by the way.

You do not surprise me. 

I have a patch, but I'm working on improving `spkg-install` and `spkg-check`. Currently `spkg-install` runs a quick test suite with `make check`. That does not seem such a bad idea, so I'm not changing that.  With SAGE_CHECK unset, this takes 46 seconds to build and run the quick test suite on my Sun Ultra 27 to build. 

However, `spkg-check` currently runs the same test suite for a second time, which is clearly pointless. I'm changing `spkg-check` to run run the more extensive test suite. That increases the time to 7 minutes and 37 seconds on my 3.33 GHz Sun Ultra 27. That will probably close to hour on the Sun T5240 't2.math.washington.edu', so if you run with SAGE_CHECK=yes, bear that in mind. 

Dave


---

Comment by drkirkby created at 2010-08-04 00:57:56

Whilst looking at the zn_poly package, I found what I think is a serious flaw in the dependencies for the package - see #9681. I'd appreciate a second pair of eyes on that one. 

Dave


---

Comment by drkirkby created at 2010-08-07 20:01:41

A fix can now be found. 

http://boxen.math.washington.edu/home/kirkby/patches/zn_poly-0.9.p5.spkg

A much more extensive test suite can now be run if `SAGE_CHECK` is exported to "yes". 

Dave


---

Attachment


---

Comment by drkirkby created at 2010-08-07 20:02:51

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-08-12 00:03:16

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-08-12 00:03:16

Looks good to me.  Builds successfully on lots of different platforms with SAGE_CHECK='yes' including t2 (both 32- and 64-bit) and fulvia (32-bit, and according to SAGE_CHECK, 64-bit -- since I don't have a working 64-bit build because of maxima, it's hard to be positive).


---

Comment by mpatel created at 2010-08-15 08:04:25

Resolution: fixed
