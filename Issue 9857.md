# Issue 9857: FLINT 1.5.0.p5's test suite fails to build with new GMP/MPIR

archive/issues_009857.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  burcin mhansen was davidloeffler\n\nKeywords: SAGE_CHECK mpz_random\n\nDue to the use of deprecated/obsolete GMP functions, the test suite of flint-1.5.0.p5 fails to build (i.e. the package's installation also currently fails if `SAGE_CHECK=yes`):\n\n\n```\n...\nSuccessfully installed flint-1.5.0.p5\nRunning the test suite.\n*************************************************\nRunning test suite. This should take 6-20 minutes\n   Please report all failures to sage-devel      \n*************************************************\nmake[2]: Entering directory `/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/spkg/build/flint-1.5.0.p5/src'\nmake[2]: warning: jobserver unavailable: using -j1.  Add `+' to parent make rule.\ngcc -std=c99 -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 -c F_mpz-test.c -o F_mpz-test.o\ngcc -std=c99 -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 -c test-support.c -o test-support.o\ng++  -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 F_mpz-test.o test-support.o -o F_mpz-test zn_mod.o misc.o mul_ks.o pack.o mul.o mulmid.o mulmid_ks.o ks_support.o mpn_mulmid.o nuss.o pmf.o pmfvec_fft.o tuning.o mul_fft.o mul_fft_dft.o array.o invert.o mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o zmod_poly.o theta.o zmod_mat.o F_mpz.o tinyQS.o factor_base.o poly.o sieve.o linear_algebra.o block_lanczos.o NTL-interface.o -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/ -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/  -lgmp -lpthread -lntl -lm \ngcc -std=c99 -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 -c mpn_extras-test.c -o mpn_extras-test.o\ng++  -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 mpn_extras-test.o test-support.o -o mpn_extras-test zn_mod.o misc.o mul_ks.o pack.o mul.o mulmid.o mulmid_ks.o ks_support.o mpn_mulmid.o nuss.o pmf.o pmfvec_fft.o tuning.o mul_fft.o mul_fft_dft.o array.o invert.o mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o zmod_poly.o theta.o zmod_mat.o F_mpz.o tinyQS.o factor_base.o poly.o sieve.o linear_algebra.o block_lanczos.o NTL-interface.o -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/ -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/  -lgmp -lpthread -lntl -lm \ngcc -std=c99 -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 -c fmpz_poly-test.c -o fmpz_poly-test.o\ng++  -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 fmpz_poly-test.o test-support.o -o fmpz_poly-test zn_mod.o misc.o mul_ks.o pack.o mul.o mulmid.o mulmid_ks.o ks_support.o mpn_mulmid.o nuss.o pmf.o pmfvec_fft.o tuning.o mul_fft.o mul_fft_dft.o array.o invert.o mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o zmod_poly.o theta.o zmod_mat.o F_mpz.o tinyQS.o factor_base.o poly.o sieve.o linear_algebra.o block_lanczos.o NTL-interface.o -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/ -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/  -lgmp -lpthread -lntl -lm \ngcc -std=c99 -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 -c fmpz-test.c -o fmpz-test.o\nfmpz-test.c: In function 'test___fmpz_normalise':\nfmpz-test.c:1379: warning: implicit declaration of function 'mpz_random'\ng++  -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 fmpz-test.o test-support.o -o fmpz-test zn_mod.o misc.o mul_ks.o pack.o mul.o mulmid.o mulmid_ks.o ks_support.o mpn_mulmid.o nuss.o pmf.o pmfvec_fft.o tuning.o mul_fft.o mul_fft_dft.o array.o invert.o mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o zmod_poly.o theta.o zmod_mat.o F_mpz.o tinyQS.o factor_base.o poly.o sieve.o linear_algebra.o block_lanczos.o NTL-interface.o -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/ -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/  -lgmp -lpthread -lntl -lm \nfmpz-test.o: In function `test___fmpz_normalise':\nfmpz-test.c:(.text+0x26a6): undefined reference to `mpz_random'\ncollect2: ld returned 1 exit status\nmake[2]: *** [fmpz-test] Error 1\nmake[2]: Leaving directory `/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/spkg/build/flint-1.5.0.p5/src'\nError building the test suite for FLINT\n*************************************\nError testing package ** flint-1.5.0.p5 **\n*************************************\nsage: An error occurred while testing flint-1.5.0.p5\n...\n```\n\n\n(This is actually Sage 4.6.prealpha3 with MPIR 2.1.**2** and [GMP-]ECM 6.3, see #9343/[NewPARI wiki page](http://wiki.sagemath.org/NewPARI), #8664 and #5847, respectively.)\n\nI guess Bill has already fixed that in FLINT 1.5.2, which was released a month ago. So simply updating the spkg might suffice.\n\nBtw, at least the current FLINT in Sage ignores user-provided `CFLAGS`; one could perhaps \"move\" them into some other environment variable used by FLINT.\n\n----\n\nUpstream: http://www.flintlib.org/\n\nIssue created by migration from https://trac.sagemath.org/ticket/9858\n\n",
    "created_at": "2010-09-05T20:51:28Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "FLINT 1.5.0.p5's test suite fails to build with new GMP/MPIR",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9857",
    "user": "leif"
}
```
Assignee: tbd

CC:  burcin mhansen was davidloeffler

Keywords: SAGE_CHECK mpz_random

Due to the use of deprecated/obsolete GMP functions, the test suite of flint-1.5.0.p5 fails to build (i.e. the package's installation also currently fails if `SAGE_CHECK=yes`):


```
...
Successfully installed flint-1.5.0.p5
Running the test suite.
*************************************************
Running test suite. This should take 6-20 minutes
   Please report all failures to sage-devel      
*************************************************
make[2]: Entering directory `/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/spkg/build/flint-1.5.0.p5/src'
make[2]: warning: jobserver unavailable: using -j1.  Add `+' to parent make rule.
gcc -std=c99 -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 -c F_mpz-test.c -o F_mpz-test.o
gcc -std=c99 -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 -c test-support.c -o test-support.o
g++  -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 F_mpz-test.o test-support.o -o F_mpz-test zn_mod.o misc.o mul_ks.o pack.o mul.o mulmid.o mulmid_ks.o ks_support.o mpn_mulmid.o nuss.o pmf.o pmfvec_fft.o tuning.o mul_fft.o mul_fft_dft.o array.o invert.o mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o zmod_poly.o theta.o zmod_mat.o F_mpz.o tinyQS.o factor_base.o poly.o sieve.o linear_algebra.o block_lanczos.o NTL-interface.o -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/ -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/  -lgmp -lpthread -lntl -lm 
gcc -std=c99 -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 -c mpn_extras-test.c -o mpn_extras-test.o
g++  -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 mpn_extras-test.o test-support.o -o mpn_extras-test zn_mod.o misc.o mul_ks.o pack.o mul.o mulmid.o mulmid_ks.o ks_support.o mpn_mulmid.o nuss.o pmf.o pmfvec_fft.o tuning.o mul_fft.o mul_fft_dft.o array.o invert.o mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o zmod_poly.o theta.o zmod_mat.o F_mpz.o tinyQS.o factor_base.o poly.o sieve.o linear_algebra.o block_lanczos.o NTL-interface.o -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/ -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/  -lgmp -lpthread -lntl -lm 
gcc -std=c99 -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 -c fmpz_poly-test.c -o fmpz_poly-test.o
g++  -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 fmpz_poly-test.o test-support.o -o fmpz_poly-test zn_mod.o misc.o mul_ks.o pack.o mul.o mulmid.o mulmid_ks.o ks_support.o mpn_mulmid.o nuss.o pmf.o pmfvec_fft.o tuning.o mul_fft.o mul_fft_dft.o array.o invert.o mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o zmod_poly.o theta.o zmod_mat.o F_mpz.o tinyQS.o factor_base.o poly.o sieve.o linear_algebra.o block_lanczos.o NTL-interface.o -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/ -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/  -lgmp -lpthread -lntl -lm 
gcc -std=c99 -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 -c fmpz-test.c -o fmpz-test.o
fmpz-test.c: In function 'test___fmpz_normalise':
fmpz-test.c:1379: warning: implicit declaration of function 'mpz_random'
g++  -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include/ -I/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/include  -fPIC -funroll-loops   -O2 fmpz-test.o test-support.o -o fmpz-test zn_mod.o misc.o mul_ks.o pack.o mul.o mulmid.o mulmid_ks.o ks_support.o mpn_mulmid.o nuss.o pmf.o pmfvec_fft.o tuning.o mul_fft.o mul_fft_dft.o array.o invert.o mpn_extras.o mpz_extras.o memory-manager.o ZmodF.o ZmodF_mul.o ZmodF_mul-tuning.o fmpz.o fmpz_poly.o mpz_poly-tuning.o mpz_poly.o ZmodF_poly.o long_extras.o zmod_poly.o theta.o zmod_mat.o F_mpz.o tinyQS.o factor_base.o poly.o sieve.o linear_algebra.o block_lanczos.o NTL-interface.o -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/ -L/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/local/lib/  -lgmp -lpthread -lntl -lm 
fmpz-test.o: In function `test___fmpz_normalise':
fmpz-test.c:(.text+0x26a6): undefined reference to `mpz_random'
collect2: ld returned 1 exit status
make[2]: *** [fmpz-test] Error 1
make[2]: Leaving directory `/home/sage/sage-4.6.prealpha3-with-mpir-2.1.1/spkg/build/flint-1.5.0.p5/src'
Error building the test suite for FLINT
*************************************
Error testing package ** flint-1.5.0.p5 **
*************************************
sage: An error occurred while testing flint-1.5.0.p5
...
```


(This is actually Sage 4.6.prealpha3 with MPIR 2.1.**2** and [GMP-]ECM 6.3, see #9343/[NewPARI wiki page](http://wiki.sagemath.org/NewPARI), #8664 and #5847, respectively.)

I guess Bill has already fixed that in FLINT 1.5.2, which was released a month ago. So simply updating the spkg might suffice.

Btw, at least the current FLINT in Sage ignores user-provided `CFLAGS`; one could perhaps "move" them into some other environment variable used by FLINT.

----

Upstream: http://www.flintlib.org/

Issue created by migration from https://trac.sagemath.org/ticket/9858





---

archive/issue_comments_097309.json:
```json
{
    "body": "Actually *five* months ago:\n\n```\nv 1.5.2 -- 08-Apr-10\n\n   * Added some defines for MPIR 1.3 support (use of deprecated functions)\n\n```\n\n\nAnd he did replace `mpz_random()` in `fmpz-test.c`.",
    "created_at": "2010-09-05T21:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97309",
    "user": "leif"
}
```

Actually *five* months ago:

```
v 1.5.2 -- 08-Apr-10

   * Added some defines for MPIR 1.3 support (use of deprecated functions)

```


And he did replace `mpz_random()` in `fmpz-test.c`.



---

archive/issue_comments_097310.json:
```json
{
    "body": "FLINT 1.6 was released on/for Chrismas (Dec. 24th).\n\nUnless somebody else already did/does I'll open a ticket to upgrade Sage's version to that one.\n\nSince Sage currently does weird things with the Makefile, providing a new, \"clean\" spkg will take some time (besides testing collaboration with the new FLINT of course).\n\n(Though FLINT is a **plain C** library, with a **separate** module to interface with NTL, which is C++ and hence the interface as well, Sage builds one monolithic \"FLINT\" library with that interface module included such that it always depends on the NTL library and the C++ standard library, which is totally odd and frequently causes trouble. Changing that requires changes to the *Sage library*, including `module_list.py` and perhaps `setup.py`, too.)\n\n----\n\nThe FLINT spkg also needs to be upgraded (to at least version 1.5.2, plus one simple patch) to work on Linux/ARM, see #10328.",
    "created_at": "2010-12-26T18:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97310",
    "user": "leif"
}
```

FLINT 1.6 was released on/for Chrismas (Dec. 24th).

Unless somebody else already did/does I'll open a ticket to upgrade Sage's version to that one.

Since Sage currently does weird things with the Makefile, providing a new, "clean" spkg will take some time (besides testing collaboration with the new FLINT of course).

(Though FLINT is a **plain C** library, with a **separate** module to interface with NTL, which is C++ and hence the interface as well, Sage builds one monolithic "FLINT" library with that interface module included such that it always depends on the NTL library and the C++ standard library, which is totally odd and frequently causes trouble. Changing that requires changes to the *Sage library*, including `module_list.py` and perhaps `setup.py`, too.)

----

The FLINT spkg also needs to be upgraded (to at least version 1.5.2, plus one simple patch) to work on Linux/ARM, see #10328.



---

archive/issue_comments_097311.json:
```json
{
    "body": "Just for the record:\n\nI have some flint-1.5.2.p1 around to address only the most important issues (changes not yet committed though).\n\nThere's **much** wrong with this spkg (including upstream), but in the light of FLINT 1.6.0 and 2.1.0 (already released), *this* ticket is mainly intended to prevent FLINT being a show stopper for #8664 and #5847.\n\nI'll perhaps include the patch from #10328, too.\n\nFeel free to ping me w.r.t. uploading a new spkg in case this ticket further drags... ;-)",
    "created_at": "2011-06-04T13:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97311",
    "user": "leif"
}
```

Just for the record:

I have some flint-1.5.2.p1 around to address only the most important issues (changes not yet committed though).

There's **much** wrong with this spkg (including upstream), but in the light of FLINT 1.6.0 and 2.1.0 (already released), *this* ticket is mainly intended to prevent FLINT being a show stopper for #8664 and #5847.

I'll perhaps include the patch from #10328, too.

Feel free to ping me w.r.t. uploading a new spkg in case this ticket further drags... ;-)



---

archive/issue_comments_097312.json:
```json
{
    "body": "Changing assignee from tbd to leif.",
    "created_at": "2011-06-04T13:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97312",
    "user": "leif"
}
```

Changing assignee from tbd to leif.



---

archive/issue_comments_097313.json:
```json
{
    "body": "Just for the record:\n\n  *\"[...] I assume Sage did not upgrade to flint 1.6. **This is a good thing** as it will be a very long time before we are able to cover factorisation of polynomials over the integers in flint2. It'll be worth waiting for though.*\n\n  *Bill.\"*\n(http://groups.google.com/group/flint-devel/msg/2dc5c1b7fba7520c)\n\n;-)",
    "created_at": "2011-06-18T19:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97313",
    "user": "leif"
}
```

Just for the record:

  *"[...] I assume Sage did not upgrade to flint 1.6. **This is a good thing** as it will be a very long time before we are able to cover factorisation of polynomials over the integers in flint2. It'll be worth waiting for though.*

  *Bill."*
(http://groups.google.com/group/flint-devel/msg/2dc5c1b7fba7520c)

;-)



---

archive/issue_comments_097314.json:
```json
{
    "body": "See also #11547 for a (very small, but important) change to the spkg-install needed for Cygwin - just so we don't forget that if this ticket ends up upgrading to p8 (see #11246 for p6 and p7).",
    "created_at": "2011-07-06T13:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97314",
    "user": "kcrisman"
}
```

See also #11547 for a (very small, but important) change to the spkg-install needed for Cygwin - just so we don't forget that if this ticket ends up upgrading to p8 (see #11246 for p6 and p7).



---

archive/issue_comments_097315.json:
```json
{
    "body": "Here is another issue - if one of the patches fails in the *current* Flint spkg, then the Cygwin-only move of `$SAGE_LOCAL/lib/libntl.a` to a temporary file is NOT rescinded.  So this should already happen if the patches do not apply.  Just a point for any upgrade to FLINT - this should be fixed.\n\n(I noticed this because one of the patches didn't apply for me.  Which makes no sense, because it was exactly right.  But whatever.)",
    "created_at": "2011-08-24T02:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97315",
    "user": "kcrisman"
}
```

Here is another issue - if one of the patches fails in the *current* Flint spkg, then the Cygwin-only move of `$SAGE_LOCAL/lib/libntl.a` to a temporary file is NOT rescinded.  So this should already happen if the patches do not apply.  Just a point for any upgrade to FLINT - this should be fixed.

(I noticed this because one of the patches didn't apply for me.  Which makes no sense, because it was exactly right.  But whatever.)



---

archive/issue_comments_097316.json:
```json
{
    "body": "See #11727 for that problem.",
    "created_at": "2011-08-24T02:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97316",
    "user": "kcrisman"
}
```

See #11727 for that problem.



---

archive/issue_comments_097317.json:
```json
{
    "body": "Since #8664 is now included in Sage 4.7.2.alpha3, this should be a blocker for the final Sage 4.7.2.",
    "created_at": "2011-09-29T19:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97317",
    "user": "leif"
}
```

Since #8664 is now included in Sage 4.7.2.alpha3, this should be a blocker for the final Sage 4.7.2.



---

archive/issue_comments_097318.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2011-09-29T19:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97318",
    "user": "leif"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_097319.json:
```json
{
    "body": "What are the plans for this ticket?  Upgrading to FLINT 1.5.2?  Upgrading to FLINT 1.6?  Upgrading to FLINT 2.x?  Fixing more odds and ends in the FLINT spkg?",
    "created_at": "2011-10-09T08:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97319",
    "user": "jdemeyer"
}
```

What are the plans for this ticket?  Upgrading to FLINT 1.5.2?  Upgrading to FLINT 1.6?  Upgrading to FLINT 2.x?  Fixing more odds and ends in the FLINT spkg?



---

archive/issue_comments_097320.json:
```json
{
    "body": "Replying to [comment:10 jdemeyer]:\n> What are the plans for this ticket?  Upgrading to FLINT 1.5.2?  Upgrading to FLINT 1.6?  Upgrading to FLINT 2.x?  Fixing more odds and ends in the FLINT spkg?\n\nUpgrading to FLINT 1.5.2, which fixes the original issue and a few other bugs in FLINT 1.5.0.\n\nMore precisely, rebasing the FLINT 1.5.2 spkg I already have (which also includes a couple of fixes to Sage's part) on the changes that were made to the 1.5.0 spkg in Sage since the p5.\n\nUpgrading to FLINT 1.6 shouldn't hurt, but would now be better done on a follow-up ticket.\n\nAs Bill meanwhile also disclosed on sage-release, they're working hard on a FLINT 2.x (planned as a Christmas present) that implements all features that Sage requires, since the current one doesn't yet provide all we need. (FLINT 2 is a complete rewrite of FLINT 1).  So upgrading to that is not an option at the moment.",
    "created_at": "2011-10-09T16:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97320",
    "user": "leif"
}
```

Replying to [comment:10 jdemeyer]:
> What are the plans for this ticket?  Upgrading to FLINT 1.5.2?  Upgrading to FLINT 1.6?  Upgrading to FLINT 2.x?  Fixing more odds and ends in the FLINT spkg?

Upgrading to FLINT 1.5.2, which fixes the original issue and a few other bugs in FLINT 1.5.0.

More precisely, rebasing the FLINT 1.5.2 spkg I already have (which also includes a couple of fixes to Sage's part) on the changes that were made to the 1.5.0 spkg in Sage since the p5.

Upgrading to FLINT 1.6 shouldn't hurt, but would now be better done on a follow-up ticket.

As Bill meanwhile also disclosed on sage-release, they're working hard on a FLINT 2.x (planned as a Christmas present) that implements all features that Sage requires, since the current one doesn't yet provide all we need. (FLINT 2 is a complete rewrite of FLINT 1).  So upgrading to that is not an option at the moment.



---

archive/issue_comments_097321.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2011-10-11T07:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97321",
    "user": "jdemeyer"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_097322.json:
```json
{
    "body": "For the record, I'm working on that, and not just since today btw.\n\nNevertheless, nobody should have touched the 1.5.0[.p5] spkg (or earlier ones) **without** upgrading to 1.5.2, since it fixes other critical bugs.",
    "created_at": "2011-10-11T15:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97322",
    "user": "leif"
}
```

For the record, I'm working on that, and not just since today btw.

Nevertheless, nobody should have touched the 1.5.0[.p5] spkg (or earlier ones) **without** upgrading to 1.5.2, since it fixes other critical bugs.



---

archive/issue_comments_097323.json:
```json
{
    "body": "I've made a FLINT 1.5.0.p10 spkg which just fixes the trivial test suite build error (see the ticket's description), since providing a *clean* FLINT 1.5.2 spkg based on the 1.5.0.p9 is tedious and still takes some time, hopefully just until tomorrow.\n\nPlease test (with `SAGE_CHECK=yes` of course, and an MPIR >=1.3.x or GMP 5.x, e.g. with Sage 4.7.2.alpha**3**) and review!\n\n(Unless you're happy with unmerging the overdue MPIR upgrade from Sage 4.7.2 just for this reason.)\n\nThanks in advance.",
    "created_at": "2011-10-11T19:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97323",
    "user": "leif"
}
```

I've made a FLINT 1.5.0.p10 spkg which just fixes the trivial test suite build error (see the ticket's description), since providing a *clean* FLINT 1.5.2 spkg based on the 1.5.0.p9 is tedious and still takes some time, hopefully just until tomorrow.

Please test (with `SAGE_CHECK=yes` of course, and an MPIR >=1.3.x or GMP 5.x, e.g. with Sage 4.7.2.alpha**3**) and review!

(Unless you're happy with unmerging the overdue MPIR upgrade from Sage 4.7.2 just for this reason.)

Thanks in advance.



---

archive/issue_comments_097324.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-10-11T19:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97324",
    "user": "leif"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097325.json:
```json
{
    "body": "Diff between the p9 and the p10. For reference / review only.",
    "created_at": "2011-10-11T19:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97325",
    "user": "leif"
}
```

Diff between the p9 and the p10. For reference / review only.



---

archive/issue_comments_097326.json:
```json
{
    "body": "Attachment [flint-1.5.0.p9-p10.diff](tarball://root/attachments/some-uuid/ticket9858/flint-1.5.0.p9-p10.diff) by leif created at 2011-10-11 19:41:10\n\nI've attached a diff between the p9 and the p10 spkg for review.",
    "created_at": "2011-10-11T19:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97326",
    "user": "leif"
}
```

Attachment [flint-1.5.0.p9-p10.diff](tarball://root/attachments/some-uuid/ticket9858/flint-1.5.0.p9-p10.diff) by leif created at 2011-10-11 19:41:10

I've attached a diff between the p9 and the p10 spkg for review.



---

archive/issue_comments_097327.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-12T08:28:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97327",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097328.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-14T09:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97328",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_097329.json:
```json
{
    "body": "Milestone sage-4.7.3 deleted",
    "created_at": "2011-11-03T16:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9857#issuecomment-97329",
    "user": "jdemeyer"
}
```

Milestone sage-4.7.3 deleted
