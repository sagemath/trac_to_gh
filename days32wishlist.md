# Sage Days 32 High Priority Wishlist

Check out

   http://trac.sagemath.org/sage_trac/report/42?asc=1&sort=status&USER=was

It's all the tickets with sd32 in their keyword field (thus everything below). You can interactively sort by status, component, etc.!    The stuff below is constantly out of date.

## Super-duper High Priority

### Super-duper High Priority: Startup time
  * [#8254](https://trac.sagemath.org/ticket/8254) - needs_work
  * [#11683](https://trac.sagemath.org/ticket/11683) - (in progress) speed up ell_curve_isogeny initialization
  * [#11040](https://trac.sagemath.org/ticket/11040) - needs_work
  * [#11043](https://trac.sagemath.org/ticket/11043) - needs_work
  * [#11714](https://trac.sagemath.org/ticket/11714) - possibly invalid; Make sure numpy does not get imported on startup
  * [#11716](https://trac.sagemath.org/ticket/11716) - positive review
  * [#11730](https://trac.sagemath.org/ticket/11730) - needs review
  * [#11732](https://trac.sagemath.org/ticket/11732) - needs review
  * [#11733](https://trac.sagemath.org/ticket/11733) - needs review
  * [#11734](https://trac.sagemath.org/ticket/11734) - needs review
  * [#11729](https://trac.sagemath.org/ticket/11729) - A cached importer that extends the Python module import framework with a persistent cache.
  * [the Sage forker](https://github.com/jasongrout/sage-forker)
  * [this article](http://artificialcode.blogspot.com/2009/04/short-circuiting-python-module-lookup.html)

### Super-duper High Priority: Porting Sage to ppc64

  * [#11705](https://trac.sagemath.org/ticket/11705) - new Port Sage to Power 7 (ppc64) -- there is a machine "silius" on skynet that should be used for this.  Only problem is building Maxima...

## High Priority

 * Upgrade MPIR ([#8664](https://trac.sagemath.org/ticket/8664) - positive_review, [#11616](https://trac.sagemath.org/ticket/11616) - needs_review), MPFR ([#11666](https://trac.sagemath.org/ticket/11666) new), MPFI to latest stable releases
 * [#5847](https://trac.sagemath.org/ticket/5847) positive_review - Update GMP-ECM to 6.3
 * [#11351](https://trac.sagemath.org/ticket/11351) - positive_review make flintqs-20070817 spkg build with -m64 rather than `-march=opteron` (Reviewer: Martin Albrecht)
 * latest jmol source (also [#9238](https://trac.sagemath.org/ticket/9238) - needs_review)
 * [#6329](https://trac.sagemath.org/ticket/6329) - needs_review optional doctest failure -- breakage in the sage<-->magma
 * [#10975](https://trac.sagemath.org/ticket/10975) - positive_review creation of certain prime finite fields is double dog slow

## Medium Priority

 * [#10826](https://trac.sagemath.org/ticket/10826) - needs_work, [#10827](https://trac.sagemath.org/ticket/10827) - needs_review, [#10828](https://trac.sagemath.org/ticket/10828) - needs_work, [#11197](https://trac.sagemath.org/ticket/11197) - needs_info SAGE_SPKG_INSTALL_DOCS
 * [#10152](https://trac.sagemath.org/ticket/10152) - closed as dup of [#10973](https://trac.sagemath.org/ticket/10973)
 * [#10973](https://trac.sagemath.org/ticket/10973) - needs_work; new integral points (Aly and Jen)
 * [#9668](https://trac.sagemath.org/ticket/9668) - new Fix hardcoding of paths in R binary
 * [#11710](https://trac.sagemath.org/ticket/11710) - new Experimental package Macaulay2 fails to build (also [#10117](https://trac.sagemath.org/ticket/10117) - new)
 * [#10976](https://trac.sagemath.org/ticket/10976) - new computing order of subgroup of a permutation group is slow
 * [#10801](https://trac.sagemath.org/ticket/10801) - needs_review; new Create a new option: "sage -strip"
 * [#8783](https://trac.sagemath.org/ticket/8783) - positive_review frobby optional spkg doesn't build with newer GCC's (Positive review: Benjamin Jones)
 * [#11427](https://trac.sagemath.org/ticket/11427) - needs_info optional spkg database_gap-4.4.12.p0.spkg fails test
 * [#11433](https://trac.sagemath.org/ticket/11433) - new optional spkg graphviz-2.16.1.p0.spkg fails to build
 * [#11438](https://trac.sagemath.org/ticket/11438) - new optional package libtheora-1.1.1.spkg does not build
 * [#11439](https://trac.sagemath.org/ticket/11439) - new optional package mpi4py-1.1.0.spkg does not build
 * [#11444](https://trac.sagemath.org/ticket/11444) - new optional package cbc-2.3.p2.spkg does not build
 * [#10981](https://trac.sagemath.org/ticket/10981) - positive_review -- new algebraic real field partial_fraction_decomposition bug (valiantly but unsuccessfully attempted: Simon Spicer); seems to be cuased by:
 * [#11728](https://trac.sagemath.org/ticket/11728) - (closed as dup) Multiplication(?) buggy in AA
 * [#7879](https://trac.sagemath.org/ticket/7879) - positive_review Remove unnecessary signal handling for low prec mpfr operations
 * [#8896](https://trac.sagemath.org/ticket/8896) - needs_info `0.0000000000000000000000000000` is parsed completely differently
 * [#10635](https://trac.sagemath.org/ticket/10635) - positive_review refactor polynomial_element.pyx factor function
 * [#4949](https://trac.sagemath.org/ticket/4949) - positive_review Optionally build spkgs in $SAGE_BUILD_TMPDIR (reviewed by maarten)
 * [#10970](https://trac.sagemath.org/ticket/10970) - positive_review Remove pipestatus from spkg/install
 * [#10271](https://trac.sagemath.org/ticket/10271) - needs_work Make big_oh notation work for any element that has degree()
 * [#5903](https://trac.sagemath.org/ticket/5903) - new; Remove dist directories from Sage distribution
 * [#10231](https://trac.sagemath.org/ticket/10231) - needs_work Don't repackage examples and extcode on sage-*dist
 * [#10952](https://trac.sagemath.org/ticket/10952) - positive_review; better numerical accuracy testing (Rob Beezer, William Stein)
 * [#6284](https://trac.sagemath.org/ticket/6284) - closed; fix the numerous broken optional magma doctests
 * [#8469](https://trac.sagemath.org/ticket/8469) - positive_review; add "Number Theory and the RSA Public Key Cryptosystem" (Rob Beezer, Martin Albrecht)
 * [#9487](https://trac.sagemath.org/ticket/9487) - new; Have an acurate description of what "supported platforms" are
 * [#9494](https://trac.sagemath.org/ticket/9494) - positive_review; Add a doctest to benchmark.py (Rob Beezer, Benjamin Jones)
 * [#10910](https://trac.sagemath.org/ticket/10910) - needs_work (basically it just depends on [#11130](https://trac.sagemath.org/ticket/11130), upgrading pari, and I don't see any additional work that is needed); Avoid nfinit while factoring polynomials
 * [#10951](https://trac.sagemath.org/ticket/10951) - needs_work; ecmfactor should take as optional argument the sigma value
 * [#5187](https://trac.sagemath.org/ticket/5187) - closed; fix optional magma doctests that changed in magma-2.15
 * [#6315](https://trac.sagemath.org/ticket/6315) - needs_review; optional doctest failure -- caused by mistakes in lectures
 * [#11421](https://trac.sagemath.org/ticket/11421) - positive_review; upgrade optional package NZMATH to version 1.1.0
 * [#7344](https://trac.sagemath.org/ticket/7344) - needs_work New libjpeg package
 * [#7345](https://trac.sagemath.org/ticket/7345) - needs_info New libtiff package
 * [#9975](https://trac.sagemath.org/ticket/9975) - needs_work; Update GnuTLS and clean up the package
 * [#11354](https://trac.sagemath.org/ticket/11354) - positive_review; remove dist directory from eclib spkg
 * [#11169](https://trac.sagemath.org/ticket/11169) - needs_info Make testcc.sh exit with an exit code of 1 if attempting
 * [#8321](https://trac.sagemath.org/ticket/8321) - needs_work; numerical integration with arbitrary precision (in-progress: Benjamin Jones)
 * [#11036](https://trac.sagemath.org/ticket/11036) - positive_review; improve solve_mod performance
 * [#6495](https://trac.sagemath.org/ticket/6495) - needs_review; build reference manual more quickly
 * [#7494](https://trac.sagemath.org/ticket/7494) - positive_review; remove/move the examples directory stuff already
 * [#6743](https://trac.sagemath.org/ticket/6743) - new; make more progress on making Sage build automatically on Cygwin
 * [#4260](https://trac.sagemath.org/ticket/4260) - needs_work; use LinBox as native matrix representation for dense matrices over GF(p)
 * [#9562](https://trac.sagemath.org/ticket/9562) - needs_review; add M4RIE to Sage (== fast linear algebra over `GF(2^n)` for n in 2..10

## Lower Priority (not from sponsor)

 * [#11722](https://trac.sagemath.org/ticket/11722) - positive_review document the SAGE_PARALLEL_SPKG_BUILD environment variable
 * [#11680](https://trac.sagemath.org/ticket/11680) - positive_review support extra_compile_args (e.g., C99) when loading/attaching .pyx (cython) files, and when using %cython in the notebook
 * [#11712](https://trac.sagemath.org/ticket/11712) - positive_review Make it so typing `cython?` results in one seeing documentation for all pragma's for %cython mode and load/attach .pyx file
 * [#11574](https://trac.sagemath.org/ticket/11574) - positive_review update M4RI
 * [#11731](https://trac.sagemath.org/ticket/11731) - Transfer ring-specific functionality of factor() and roots() in polynomial_element.pyx to the correct ring files - See [#10635](https://trac.sagemath.org/ticket/10635)
