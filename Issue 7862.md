# Issue 7862: singular creates some 32-bit and some 64-bit objects on Open Solaris

Issue created by migration from https://trac.sagemath.org/ticket/7862

Original creator: drkirkby

Original creation time: 2010-01-06 23:45:18

Assignee: drkirkby

CC:  jsp dimpase

*== Build environment ==
 * Sun Ultra 27 3.333 GHz Intel Xeon. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)
 * gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
 * 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 

 == The problem ==
First we see g++ is compiling with the -m64 option, as is should do. 

```
g++ -c lgs.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -m64 -O3 -g -fPIC -o lgs.o
g++ -c singext.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -m64 -O3 -g -fPIC -o singext.o
```

So far so good. Then a library is created using 'ar'

```
ar cr libsingcf.a canonicalform.o cf_algorithm.o cf_binom.o cf_char.o cf_chinese.o cf_eval.o cf_factor.o cf_factory.o cf_gcd.o cf_gcd_charp.o cf_generator.o cf_globals.o cf_inline.o cf_irred.o cf_iter.o cf_iter_inline.o cf_linsys.o cf_map.o cf_ops.o cf_primes.o cf_random.o cf_resultant.o cf_reval.o cf_switches.o cf_util.o debug.o fac_berlekamp.o fac_cantzass.o fac_distrib.o fac_ezgcd.o fac_iterfor.o fac_multihensel.o fac_multivar.o fac_sqrfree.o fac_univar.o fac_util.o fieldGCD.o ffops.o ffreval.o gf_tabutil.o gfops.o imm.o initgmp.o int_cf.o int_int.o int_intdiv.o int_poly.o int_pp.o int_rat.o sm_sparsemod.o sm_util.o variable.o NTLconvert.o abs_fac.o bifac.o lgs.o singext.o
ranlib libsingcf.a
```

Again, that looks ok. But now see when further C code is compiled, so the -m64 option does not propogate, so the compiler makes 32-bit code. 

```
g++ -g -c canonicalform.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o canonicalform.og
g++ -g -c cf_algorithm.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_algorithm.og
g++ -g -c cf_binom.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_binom.og
g++ -g -c cf_char.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_char.og
g++ -g -c cf_chinese.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_chinese.og
g++ -g -c cf_eval.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_eval.og
g++ -g -c cf_factor.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_factor.og
In file included from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/ZZ.h:19,
                 from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/vec_ZZ.h:5,
                 from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/ZZX.h:5,
                 from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/ZZXFactoring.h:5,
                 from NTLconvert.h:23,
                 from cf_factor.cc:33:
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/tools.h:201: error: integer constant is too large for ‘long’ type
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/tools.h:201: error: integer constant is too large for ‘long’ type
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/tools.h:204: error: integer constant is too large for ‘long’ type
/export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/tools.h:204: error: integer constant is too large for ‘long’ type
```

 == Summary ==
It looks like a makefile is probably broken, and somehow -m64 is  not propagating like it should. 


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by chapoton created at 2020-07-09 15:24:59

Resolution: invalid
