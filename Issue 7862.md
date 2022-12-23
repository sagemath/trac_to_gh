# Issue 7862: singular creates some 32-bit and some 64-bit objects on Open Solaris

archive/issues_007862.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jsp dimpase\n\n == Build environment ==\n* Sun Ultra 27 3.333 GHz Intel Xeon. 12 GB RAM\n* OpenSolaris 2009.06 snv_111b X86\n* Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)\n* gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.\n* 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. \n\n == The problem ==\nFirst we see g++ is compiling with the -m64 option, as is should do. \n\n```\ng++ -c lgs.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -m64 -O3 -g -fPIC -o lgs.o\ng++ -c singext.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -m64 -O3 -g -fPIC -o singext.o\n```\n\nSo far so good. Then a library is created using 'ar'\n\n```\nar cr libsingcf.a canonicalform.o cf_algorithm.o cf_binom.o cf_char.o cf_chinese.o cf_eval.o cf_factor.o cf_factory.o cf_gcd.o cf_gcd_charp.o cf_generator.o cf_globals.o cf_inline.o cf_irred.o cf_iter.o cf_iter_inline.o cf_linsys.o cf_map.o cf_ops.o cf_primes.o cf_random.o cf_resultant.o cf_reval.o cf_switches.o cf_util.o debug.o fac_berlekamp.o fac_cantzass.o fac_distrib.o fac_ezgcd.o fac_iterfor.o fac_multihensel.o fac_multivar.o fac_sqrfree.o fac_univar.o fac_util.o fieldGCD.o ffops.o ffreval.o gf_tabutil.o gfops.o imm.o initgmp.o int_cf.o int_int.o int_intdiv.o int_poly.o int_pp.o int_rat.o sm_sparsemod.o sm_util.o variable.o NTLconvert.o abs_fac.o bifac.o lgs.o singext.o\nranlib libsingcf.a\n```\n\nAgain, that looks ok. But now see when further C code is compiled, so the -m64 option does not propogate, so the compiler makes 32-bit code. \n\n```\ng++ -g -c canonicalform.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o canonicalform.og\ng++ -g -c cf_algorithm.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_algorithm.og\ng++ -g -c cf_binom.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_binom.og\ng++ -g -c cf_char.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_char.og\ng++ -g -c cf_chinese.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_chinese.og\ng++ -g -c cf_eval.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_eval.og\ng++ -g -c cf_factor.cc -w -fno-implicit-templates -I. -I. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -DHAVE_CONFIG_H -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include  -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -o cf_factor.og\nIn file included from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/ZZ.h:19,\n                 from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/vec_ZZ.h:5,\n                 from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/ZZX.h:5,\n                 from /export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/ZZXFactoring.h:5,\n                 from NTLconvert.h:23,\n                 from cf_factor.cc:33:\n/export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/tools.h:201: error: integer constant is too large for \u2018long\u2019 type\n/export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/tools.h:201: error: integer constant is too large for \u2018long\u2019 type\n/export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/tools.h:204: error: integer constant is too large for \u2018long\u2019 type\n/export/home/drkirkby/sage-4.3.1.alpha1/local/include/NTL/tools.h:204: error: integer constant is too large for \u2018long\u2019 type\n```\n\n == Summary ==\nIt looks like a makefile is probably broken, and somehow -m64 is  not propagating like it should. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7862\n\n",
    "created_at": "2010-01-06T23:45:18Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "singular creates some 32-bit and some 64-bit objects on Open Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7862",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  jsp dimpase

 == Build environment ==
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

Issue created by migration from https://trac.sagemath.org/ticket/7862





---

archive/issue_comments_068164.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7862#issuecomment-68164",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068165.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7862#issuecomment-68165",
    "user": "mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_068166.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-09T15:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7862#issuecomment-68166",
    "user": "chapoton"
}
```

Resolution: invalid
