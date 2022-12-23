# Issue 6470: sage-4.1.rc0: On OS X 10.5 Singular fails to build

Issue created by migration from https://trac.sagemath.org/ticket/6470

Original creator: rlm

Original creation time: 2009-07-06 17:37:00

Assignee: tbd

CC:  georgsweber malb


```
g++ -O3 -g -fPIC -pipe -I. -I../kernel -I/Applications/sage_builds/
sage-4.1.rc0/local/include -I/Applications/sage_builds/sage-4.1.rc0/
local/include  -I/Applications/sage_builds/sage-4.1.rc0/local/include -
fno-implicit-templates -DNDEBUG -DOM_NDEBUG -Dix86Mac_darwin -
DHAVE_CONFIG_H -DLIBSINGULAR \
          -dynamic -twolevel_namespace -weak_reference_mismatches weak -
undefined dynamic_lookup -o libsingular-tesths.o \
          -c tesths.cc
libtool -dynamic -twolevel_namespace -weak_reference_mismatches weak -
undefined dynamic_lookup -single_module -o libsingular.dylib \
        libsingular-tesths.o iparith.o mpsr_Tok.o claptmpl.o \
        grammar.o scanner.o attrib.o eigenval_ip.o extra.o fehelp.o feOpt.o
ipassign.o ipconv.o ipid.o iplib.o ipprint.o ipshell.o lists.o sdb.o
fglm.o interpolation.o silink.o subexpr.o janet.o wrapper.o libparse.o
sing_win.o gms.o pcv.o maps_ip.o walk.o walk_ip.o cntrlc.o misc.o
calcSVD.o  slInit_Static.o mpsr_Put.o mpsr_PutPoly.o mpsr_GetPoly.o
mpsr_sl.o mpsr_Get.o mpsr_GetMisc.o mpsr_Error.o ndbm.o sing_dbm.o -
lkernel -L../kernel -L../factory -L../libfac -L/Applications/
sage_builds/sage-4.1.rc0/local/lib -lsingfac -lsingcf -lntl -lreadline
-lgmp -lomalloc
libtool: file: -lsingcf(canonicalform.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_algorithm.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_binom.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_char.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(cf_chinese.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_eval.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(cf_factor.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_factory.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_gcd.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(cf_gcd_charp.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_generator.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_globals.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_inline.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_irred.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_iter.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(cf_iter_inline.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_linsys.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_map.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(cf_ops.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(cf_primes.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_random.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_resultant.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_reval.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_switches.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(cf_util.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(debug.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(fac_berlekamp.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(fac_cantzass.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(fac_distrib.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(fac_ezgcd.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(fac_iterfor.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(fac_multihensel.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(fac_multivar.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(fac_sqrfree.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(fac_univar.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(fac_util.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(fieldGCD.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(ffops.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(ffreval.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(gf_tabutil.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(gfops.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(imm.cc) is not an object file (not allowed in
a library)
libtool: file: -lsingcf(initgmp.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(int_cf.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(int_int.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(int_intdiv.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(int_poly.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(int_pp.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(int_rat.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(sm_sparsemod.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(sm_util.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(variable.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(NTLconvert.cc) is not an object file (not
allowed in a library)
libtool: file: -lsingcf(abs_fac.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(bifac.cc) is not an object file (not allowed
in a library)
libtool: file: -lsingcf(lgs.cc) is not an object file (not allowed in
a library)
libtool: file: -lsingcf(singext.cc) is not an object file (not allowed
in a library)
make[3]: *** [libsingular] Error 1
make[2]: *** [libsingular] Error 2
Unable to build Singular.

real    6m56.224s
user    6m9.512s
sys     0m38.659s
sage: An error occurred while installing singular-3-1-0-4-20090703
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Applications/sage_builds/sage-4.1.rc0/install.log.  Describe your
computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Applications/sage_builds/sage-4.1.rc0/spkg/build/
singular-3-1-0-4-20090703 and type 'make'.
Instead type "/Applications/sage_builds/sage-4.1.rc0/sage -sh"
in order to set all environment variables correctly, then cd to
/Applications/sage_builds/sage-4.1.rc0/spkg/build/
singular-3-1-0-4-20090703
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/singular-3-1-0-4-20090703] Error 1 
```



---

Comment by aginiewicz created at 2009-07-06 19:44:58

The version http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg that fixes gcc 4.4 issue but doesn't have the 3.1.0-4 that fails is put back on-line. *If* this wouldn't be solved on time for release, this version works on Mac (as reported on sage-devel) so upgrade to 3.1.0-4 can wait for 4.1.1 probably?


---

Comment by jhpalmieri created at 2009-07-06 20:01:32

In case it's helpful, I have logs of the successful build of singular-3-1-0-2-20090620.spkg and the failed build of singular-3-1-0-4-20090703:

 [http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-2-20090620.log](http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-2-20090620.log)

 [http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-4-20090703.log](http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-4-20090703.log)


---

Comment by GeorgSWeber created at 2009-07-06 20:09:02

Ups,

I posted my findings on ticket #6362 instead of here. In short: the build issue seems to be solved, most probably the OS X "make" version is a bit too old for a certain programmer's short-cut newly used in GNUmakefile.in. Let's continue here -- should I repost my comments?

Cheers,
gsw


---

Comment by GeorgSWeber created at 2009-07-06 20:17:20

Thinking about it, I do repost my comments from #6362:

As contained in Sage-4.1.rc0, singular-3-1-0-4-20090703.spkg does not even build on OS X, neither 10.4 nor 10.5. Changing the line 201 in /src/factory/GNUmakefile.in:

```
factoryobj :=   $(factorysrc:%.cc=%.o) $(factorysrc:%.y=%.o)
```

into the following two lines:

```
factoryobj :=   $(factorysrc:%.cc=%.o)
factoryobj :=   $(factoryobj:%.y=%.o)
```

made the resulting Singular spkg build on OS X 10.4. But after installing it into Sage-4.1.rc0, Sage doesn't even start, it fails with:

```
ImportError: dlopen(/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so, 2): Symbol not found: ___eprintf
  Referenced from: /Users/Shared/sage/sage-4.1.rc0/local/lib//libsingular.dylib
  Expected in: dynamic lookup
```

This might be due to the fact that I had dropped in the 3.1.0.2 Singular spkg before, so I am re-running the build from the start. (I doubt that it'll help, but let's see.)

For the record, skipping through the install logs, I spotted another error (this time "copy'n'paste") in the Singular 3.1.0.4 build scripts. In /src/libfac/Makefile.in, the two identical lines 157/158 read:

```
	-$(RANLIB) ${libdir}/libsingfac_g.a
	-$(RANLIB) ${libdir}/libsingfac_g.a
```

and it is obvious from the surrounding lines, that the line 158 should end with "..._p.a" instead of "..._g.a".

`@`Martin: Would you please report the findings so far upstream?


---

Comment by GeorgSWeber created at 2009-07-07 04:28:58

No, building from scratch with the "healed" 3.1.0.4 Singular spkg didn't bring any news. Here's the full error message if one wants to start sage:

```
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/Users/Shared/sage/sage-4.1.rc0/local/bin/ipy_profile_sage.py in <module>()
      5     preparser(True)
      6 
----> 7     import sage.all_cmdline
      8     sage.all_cmdline._init_cmdline(globals())
      9 

/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()
     12 try:
     13 
---> 14     from sage.all import *
     15     from sage.calculus.predefined import x
     16     preparser(on=True)

/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/all.py in <module>()
     70 get_sigs()
     71 
---> 72 from sage.rings.all      import *
     73 from sage.matrix.all     import *
     74 

/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/all.py in <module>()
     92 
     93 # Algebraic numbers

---> 94 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,
     95                    AlgebraicReal, is_AlgebraicReal,
     96                    AlgebraicField, is_AlgebraicField, QQbar,

/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/qqbar.py in <module>()
   1417 QQy = QQ['y']
   1418 QQy_y = QQy.gen()
-> 1419 QQxy = QQ['x', 'y']
   1420 QQxy_x = QQxy.gen(0)
   1421 QQxy_y = QQxy.gen(1)

/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2676)()

/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)
    288             names = arg1
    289             n = len(names)
--> 290             R = _multi_variate(base_ring, names, n, sparse, order)
    291 
    292     if arg1 is None and arg2 is None:

/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _multi_variate(base_ring, names, n, sparse, order)
    388         return R
    389 
--> 390     from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular
    391     if m.integral_domain.is_IntegralDomain(base_ring):
    392         if n < 1:

ImportError: dlopen(/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so, 2): Symbol not found: ___eprintf
  Referenced from: /Users/Shared/sage/sage-4.1.rc0/local/lib//libsingular.dylib
  Expected in: dynamic lookup

Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.

sage:
```

The sage prompt appears, but even "version()" does not work.


---

Comment by GeorgSWeber created at 2009-07-07 06:00:21

Hmmm,

in all of Singular and all of /devel/sage/sage/rings/, I can't seem to find some "eprintf".
I'll try rebuilding from scratch again, but now from my superclean (Mac OS X) Sage build partition with nothing in its PATH but "/bin:/sbin:/usr/bin:/usr/sbin", no directory "/usr/local/" at all, and so on. Oh well.

Cheers,
gsw


---

Comment by GeorgSWeber created at 2009-07-07 18:13:33

Building in my "clean room" didn't bring anything new either.

But a Google search showed some interesting information w.r.t. Mac OS X:

```
__eprintf is used inside the assert macro, and defined in libgcc2.c:

#include <stdio.h>
/* This is used by the `assert' macro.  */
void
__eprintf (const char *string, const char *expression,
           unsigned int line, const char *filename)
{
  fprintf (stderr, string, expression, line, filename);
  fflush (stderr);
  abort ();
}

It then appears that you are not linking with libgcc.
```

I'm not sure whether it is reasonable to try to link dynamically against libgcc --- is this library available on Mac OS X also in the absence of the XCode Tools?


---

Comment by rlm created at 2009-07-07 20:19:13

Merging

http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg

into Sage-4.1.rc1. I think the upgrade can wait for sage-4.1.1.


---

Comment by rlm created at 2009-07-07 20:19:13

Resolution: fixed


---

Comment by rlm created at 2009-07-07 20:22:36

See #6476.
