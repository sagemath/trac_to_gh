# Issue 6453: MPFR test failures in Sage

archive/issues_006453.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.net paul.zimmermann@loria.fr nguyenminh2@gmail.com\n\nI found that when trying to build Sage on t2.math.washington.edu there \nare problems with 'mpfr', with 20 out of 148 test failures.\n\n```\ngmake  check-TESTS\ngmake[2]: Entering directory `/tmp/mpfr-2.4.1/tests'\nPASS: tversion\nPASS: tinternals\nPASS: tinits\nPASS: tisqrt\nPASS: tsgn\nPASS: tcheck\nPASS: tisnan\nPASS: texceptions\nPASS: tset_exp\nPASS: tset\nPASS: tabs\nPASS: tset_d\nPASS: tset_f\nPASS: tset_q\nPASS: tset_si\nPASS: tset_str\nPASS: tset_z\nPASS: tset_ld\nPASS: tset_sj\nPASS: tswap\nPASS: tcopysign\nPASS: tcmp\nPASS: tcmp2\nPASS: tcmpabs\nPASS: tcmp_d\nPASS: tcmp_ld\nPASS: tcomparisons\nPASS: teq\nPASS: tadd\nPASS: tsub\n/bin/bash: line 1: 24097 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tmul\n/bin/bash: line 1: 24116 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tdiv\nPASS: tsub1sp\nPASS: tadd1sp\nPASS: tadd_ui\nPASS: tsub_ui\nPASS: tcmp_ui\nPASS: tdiv_ui\nPASS: tmul_ui\nPASS: tsqrt_ui\nPASS: tui_div\nPASS: tui_sub\n/bin/bash: line 1: 24305 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tadd_d\nPASS: tsub_d\nPASS: td_sub\nPASS: tmul_d\nPASS: tdiv_d\nPASS: td_div\nPASS: tgmpop\nPASS: tsi_op\nPASS: tmul_2exp\n/bin/bash: line 1: 24460 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tfma\n/bin/bash: line 1: 24479 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tfms\nPASS: tsum\nPASS: tdim\nPASS: tminmax\n/bin/bash: line 1: 24549 Arithmetic Exception    (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tnext\nPASS: tfits\nPASS: tget_d\nPASS: tget_d_2exp\nPASS: tget_z\n/bin/bash: line 1: 24636 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tget_str\nPASS: tget_sj\nPASS: tout_str\nPASS: tinp_str\nPASS: toutimpl\nPASS: tcan_round\nPASS: tround_prec\n/bin/bash: line 1: 24757 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tsqrt\nPASS: tconst_log2\nPASS: tconst_pi\nPASS: tconst_euler\nPASS: trandom\nPASS: ttrunc\nPASS: trint\nPASS: tfrac\n/bin/bash: line 1: 24895 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tmodf\nPASS: texp\nPASS: texp2\nPASS: texp10\nPASS: texpm1\nPASS: tlog\nPASS: tlog2\nPASS: tlog10\nPASS: tlog1p\n/bin/bash: line 1: 25050 Arithmetic Exception    (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tpow\n/bin/bash: line 1: 25069 Arithmetic Exception    (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tui_pow\nPASS: tpow3\nPASS: tcosh\nPASS: tsinh\nPASS: ttanh\nPASS: tsinh_cosh\nPASS: tacosh\nPASS: tasinh\nPASS: tatanh\nPASS: thyperbolic\nPASS: tasin\nPASS: tacos\nPASS: tcos\n/bin/bash: line 1: 25292 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tatan\n/bin/bash: line 1: 25311 Arithmetic Exception    (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tsin\n/bin/bash: line 1: 25330 Arithmetic Exception    (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: ttan\nPASS: tsin_cos\nPASS: tagm\nPASS: thypot\nPASS: tfactorial\n/bin/bash: line 1: 25417 Arithmetic Exception    (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tgamma\nPASS: terf\nPASS: tcbrt\nPASS: tzeta\nPASS: mpf_compat\nPASS: mpfr_compat\nPASS: reuse\nPASS: tsqr\n/bin/bash: line 1: 25556 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tstrtofr\nPASS: tpow_z\nPASS: tget_f\nPASS: tconst_catalan\nPASS: troot\nPASS: tsec\nPASS: tcsc\nPASS: tcot\nPASS: teint\nPASS: tcoth\nPASS: tcsch\nPASS: tsech\nPASS: tstckintc\nPASS: tsubnormal\nPASS: tlngamma\nPASS: tlgamma\nPASS: tzeta_ui\nPASS: tget_ld_2exp\nPASS: tget_set_d64\nPASS: tj0\nPASS: tj1\nPASS: tjn\nPASS: ty0\nPASS: ty1\nPASS: tyn\nPASS: tremquo\nPASS: tfmod\nPASS: tl2b\nPASS: tli2\n/bin/bash: line 1: 26051 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tprintf\n/bin/bash: line 1: 26070 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tsprintf\n/bin/bash: line 1: 26089 Segmentation Fault      (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tfprintf\nPASS: trec_sqrt\n/bin/bash: line 1: 26125 Arithmetic Exception    (core dumped) \nMPFR_QUIET=1 ${dir}$tst\nFAIL: tpow_all\n======================\n20 of 148 tests failed\n======================\n\n```\n\n\n\nI downloaded the mpfr 2.4.1 source, compiled that with the same gcc \noptimisation level as used in Sage (-O2). Again mpfr failed 20 tests. \n\nI then changed to an optimsation level of 1 in the MPFR source (outside sage). Again 20 tests failed.\n\nI then used no optimsisation, which resultsed in 100% pass rate. \n\nOn my Blade 2000 (hostname kestrel), things are very different, as the following table shows.\n\n\n```\nMachine  Optimiation     Failures\n\nt2          -O2                20\nt2          -O1                20\nt2          none                0\nkestrel     -O2                 0\nkestrel     -O1          untested\nkestrel     none                0\n```\n\n\n(kestrel runs Solaris 10 update 6)\n\n(t2 runs Solaris 10 update 4)\n\nI assumed this problem was due to optimisation in Sage and that removing the optimisation on Solaris would solve this. But that is not the case. \n\nThe reason for the failures is still unknown. \n\nThere may be some advantage in recompiling mpir with lower optimisation, despite the fact mpir did pass all tests, since this mpfr relies upon mpir. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6453\n\n",
    "created_at": "2009-07-01T04:09:23Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "MPFR test failures in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6453",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.net paul.zimmermann@loria.fr nguyenminh2@gmail.com

I found that when trying to build Sage on t2.math.washington.edu there 
are problems with 'mpfr', with 20 out of 148 test failures.

```
gmake  check-TESTS
gmake[2]: Entering directory `/tmp/mpfr-2.4.1/tests'
PASS: tversion
PASS: tinternals
PASS: tinits
PASS: tisqrt
PASS: tsgn
PASS: tcheck
PASS: tisnan
PASS: texceptions
PASS: tset_exp
PASS: tset
PASS: tabs
PASS: tset_d
PASS: tset_f
PASS: tset_q
PASS: tset_si
PASS: tset_str
PASS: tset_z
PASS: tset_ld
PASS: tset_sj
PASS: tswap
PASS: tcopysign
PASS: tcmp
PASS: tcmp2
PASS: tcmpabs
PASS: tcmp_d
PASS: tcmp_ld
PASS: tcomparisons
PASS: teq
PASS: tadd
PASS: tsub
/bin/bash: line 1: 24097 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tmul
/bin/bash: line 1: 24116 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tdiv
PASS: tsub1sp
PASS: tadd1sp
PASS: tadd_ui
PASS: tsub_ui
PASS: tcmp_ui
PASS: tdiv_ui
PASS: tmul_ui
PASS: tsqrt_ui
PASS: tui_div
PASS: tui_sub
/bin/bash: line 1: 24305 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tadd_d
PASS: tsub_d
PASS: td_sub
PASS: tmul_d
PASS: tdiv_d
PASS: td_div
PASS: tgmpop
PASS: tsi_op
PASS: tmul_2exp
/bin/bash: line 1: 24460 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tfma
/bin/bash: line 1: 24479 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tfms
PASS: tsum
PASS: tdim
PASS: tminmax
/bin/bash: line 1: 24549 Arithmetic Exception    (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tnext
PASS: tfits
PASS: tget_d
PASS: tget_d_2exp
PASS: tget_z
/bin/bash: line 1: 24636 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tget_str
PASS: tget_sj
PASS: tout_str
PASS: tinp_str
PASS: toutimpl
PASS: tcan_round
PASS: tround_prec
/bin/bash: line 1: 24757 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tsqrt
PASS: tconst_log2
PASS: tconst_pi
PASS: tconst_euler
PASS: trandom
PASS: ttrunc
PASS: trint
PASS: tfrac
/bin/bash: line 1: 24895 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tmodf
PASS: texp
PASS: texp2
PASS: texp10
PASS: texpm1
PASS: tlog
PASS: tlog2
PASS: tlog10
PASS: tlog1p
/bin/bash: line 1: 25050 Arithmetic Exception    (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tpow
/bin/bash: line 1: 25069 Arithmetic Exception    (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tui_pow
PASS: tpow3
PASS: tcosh
PASS: tsinh
PASS: ttanh
PASS: tsinh_cosh
PASS: tacosh
PASS: tasinh
PASS: tatanh
PASS: thyperbolic
PASS: tasin
PASS: tacos
PASS: tcos
/bin/bash: line 1: 25292 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tatan
/bin/bash: line 1: 25311 Arithmetic Exception    (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tsin
/bin/bash: line 1: 25330 Arithmetic Exception    (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: ttan
PASS: tsin_cos
PASS: tagm
PASS: thypot
PASS: tfactorial
/bin/bash: line 1: 25417 Arithmetic Exception    (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tgamma
PASS: terf
PASS: tcbrt
PASS: tzeta
PASS: mpf_compat
PASS: mpfr_compat
PASS: reuse
PASS: tsqr
/bin/bash: line 1: 25556 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tstrtofr
PASS: tpow_z
PASS: tget_f
PASS: tconst_catalan
PASS: troot
PASS: tsec
PASS: tcsc
PASS: tcot
PASS: teint
PASS: tcoth
PASS: tcsch
PASS: tsech
PASS: tstckintc
PASS: tsubnormal
PASS: tlngamma
PASS: tlgamma
PASS: tzeta_ui
PASS: tget_ld_2exp
PASS: tget_set_d64
PASS: tj0
PASS: tj1
PASS: tjn
PASS: ty0
PASS: ty1
PASS: tyn
PASS: tremquo
PASS: tfmod
PASS: tl2b
PASS: tli2
/bin/bash: line 1: 26051 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tprintf
/bin/bash: line 1: 26070 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tsprintf
/bin/bash: line 1: 26089 Segmentation Fault      (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tfprintf
PASS: trec_sqrt
/bin/bash: line 1: 26125 Arithmetic Exception    (core dumped) 
MPFR_QUIET=1 ${dir}$tst
FAIL: tpow_all
======================
20 of 148 tests failed
======================

```



I downloaded the mpfr 2.4.1 source, compiled that with the same gcc 
optimisation level as used in Sage (-O2). Again mpfr failed 20 tests. 

I then changed to an optimsation level of 1 in the MPFR source (outside sage). Again 20 tests failed.

I then used no optimsisation, which resultsed in 100% pass rate. 

On my Blade 2000 (hostname kestrel), things are very different, as the following table shows.


```
Machine  Optimiation     Failures

t2          -O2                20
t2          -O1                20
t2          none                0
kestrel     -O2                 0
kestrel     -O1          untested
kestrel     none                0
```


(kestrel runs Solaris 10 update 6)

(t2 runs Solaris 10 update 4)

I assumed this problem was due to optimisation in Sage and that removing the optimisation on Solaris would solve this. But that is not the case. 

The reason for the failures is still unknown. 

There may be some advantage in recompiling mpir with lower optimisation, despite the fact mpir did pass all tests, since this mpfr relies upon mpir. 

Issue created by migration from https://trac.sagemath.org/ticket/6453





---

archive/issue_comments_051847.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2009-07-01T04:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51847",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_051848.json:
```json
{
    "body": "I should have stated the versions of the software. \n\nOn t2, gcc was configured as:\n\n\n\n```\nkirkby@t2:[~] $ gcc -v\nUsing built-in specs.\nTarget: sparc-sun-solaris2.10\nConfigured with: /home/kirkby/gcc-4.4.0/configure CC=/usr/sfw/bin/gcc --prefix=/usr/local/gcc-4.4.0-sun-linker --without-gnu-as --without-gnu-ld --with-as=/usr/ccs/bin/as --with-ld=/usr/ccs/bin/ld --enable-languages=c,c++,fortran --with-mpfr-lib=/usr/local/lib --with-mpfr-include=/usr/local/include --with-gmp-include=/usr/local/include --with-gmp-lib=/usr/local/lib --with-libiconv-prefix=/usr/lib/iconv\nThread model: posix\ngcc version 4.4.0 (GCC)\n```\n\n\nkirkby`@`t2:[~] $ cat /etc/release\n                       Solaris 10 8/07 s10s_u4wos_12b SPARC\n           Copyright 2007 Sun Microsystems, Inc.  All Rights Reserved.\n                        Use is subject to license terms.\n                            Assembled 16 August 2007\n\nkirkby`@`t2:[~] $ uname -a\nSunOS t2 5.10 Generic_127111-09 sun4v sparc SUNW,T5240\n\nsage-4.1.alpha2, mpfr-2.4.1 with no patches applied.",
    "created_at": "2009-07-01T04:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51848",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I should have stated the versions of the software. 

On t2, gcc was configured as:



```
kirkby@t2:[~] $ gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: /home/kirkby/gcc-4.4.0/configure CC=/usr/sfw/bin/gcc --prefix=/usr/local/gcc-4.4.0-sun-linker --without-gnu-as --without-gnu-ld --with-as=/usr/ccs/bin/as --with-ld=/usr/ccs/bin/ld --enable-languages=c,c++,fortran --with-mpfr-lib=/usr/local/lib --with-mpfr-include=/usr/local/include --with-gmp-include=/usr/local/include --with-gmp-lib=/usr/local/lib --with-libiconv-prefix=/usr/lib/iconv
Thread model: posix
gcc version 4.4.0 (GCC)
```


kirkby`@`t2:[~] $ cat /etc/release
                       Solaris 10 8/07 s10s_u4wos_12b SPARC
           Copyright 2007 Sun Microsystems, Inc.  All Rights Reserved.
                        Use is subject to license terms.
                            Assembled 16 August 2007

kirkby`@`t2:[~] $ uname -a
SunOS t2 5.10 Generic_127111-09 sun4v sparc SUNW,T5240

sage-4.1.alpha2, mpfr-2.4.1 with no patches applied.



---

archive/issue_comments_051849.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-01T04:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51849",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to assigned.



---

archive/issue_comments_051850.json:
```json
{
    "body": "Attachment [config.log](tarball://root/attachments/some-uuid/ticket6453/config.log) by drkirkby created at 2009-07-01 04:17:21\n\nconfig.log showing no optimisation on the command line. Still 20 tests fail",
    "created_at": "2009-07-01T04:17:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51850",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [config.log](tarball://root/attachments/some-uuid/ticket6453/config.log) by drkirkby created at 2009-07-01 04:17:21

config.log showing no optimisation on the command line. Still 20 tests fail



---

archive/issue_comments_051851.json:
```json
{
    "body": "One 'fix' appears to be to use a gcc no later than 4.2.4\n\nSee table below of the number of failures with each version of gcc. \n\ngcc-3.4.3 : 0 MPFR failures\ngcc-4.1.1 : 0 MPFR failures\ngcc-4.2.1 : 0 MPFR failures\ngcc-4.2.4 : 0 MPFR failures\ngcc-4.3.0 : gcc 4.3.0 builds, but will not install for me.\ngcc-4.3.1 : 20 MPFR failures\ngcc-4.3.3 : 20 MPFR failures\ngcc-4.4.0 : 20 MPFR failures \n\nOn my own machine, there are none no matter what version of gcc I use. \n\nAt the time I first reported this, 't2' run Solaris 10 update 4. It is now running Solaris 10 update 7, but this has not changed the result.",
    "created_at": "2009-07-13T23:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51851",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

One 'fix' appears to be to use a gcc no later than 4.2.4

See table below of the number of failures with each version of gcc. 

gcc-3.4.3 : 0 MPFR failures
gcc-4.1.1 : 0 MPFR failures
gcc-4.2.1 : 0 MPFR failures
gcc-4.2.4 : 0 MPFR failures
gcc-4.3.0 : gcc 4.3.0 builds, but will not install for me.
gcc-4.3.1 : 20 MPFR failures
gcc-4.3.3 : 20 MPFR failures
gcc-4.4.0 : 20 MPFR failures 

On my own machine, there are none no matter what version of gcc I use. 

At the time I first reported this, 't2' run Solaris 10 update 4. It is now running Solaris 10 update 7, but this has not changed the result.



---

archive/issue_comments_051852.json:
```json
{
    "body": "Sorry, here is the data in a table.\n\n```\ngcc-3.4.3 : 0 MPFR failures\ngcc-4.1.1 : 0 MPFR failures\ngcc-4.2.1 : 0 MPFR failures\ngcc-4.2.4 : 0 MPFR failures\ngcc-4.3.0 : gcc 4.3.0 builds, but will not install for me.\ngcc-4.3.1 : 20 MPFR failures\ngcc-4.3.3 : 20 MPFR failures\ngcc-4.4.0 : 20 MPFR failures\n```\n",
    "created_at": "2009-07-13T23:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51852",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Sorry, here is the data in a table.

```
gcc-3.4.3 : 0 MPFR failures
gcc-4.1.1 : 0 MPFR failures
gcc-4.2.1 : 0 MPFR failures
gcc-4.2.4 : 0 MPFR failures
gcc-4.3.0 : gcc 4.3.0 builds, but will not install for me.
gcc-4.3.1 : 20 MPFR failures
gcc-4.3.3 : 20 MPFR failures
gcc-4.4.0 : 20 MPFR failures
```




---

archive/issue_comments_051853.json:
```json
{
    "body": "This is a compiler bug. See http://websympa.loria.fr/wwsympa/arc/mpfr/2009-07/msg00049.html.\nA possible fix is the following:\n\n```\nzimmerma@t2:/tmp/mpfr-2.4.1$ diff mpn_exp.c.orig mpn_exp.c\n74c74\n<   MPN_ZERO (a, n - 1);\n---\n>   if (n > 1) MPN_ZERO (a, n - 1);\n```\n",
    "created_at": "2009-07-15T00:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51853",
    "user": "https://github.com/zimmermann6"
}
```

This is a compiler bug. See http://websympa.loria.fr/wwsympa/arc/mpfr/2009-07/msg00049.html.
A possible fix is the following:

```
zimmerma@t2:/tmp/mpfr-2.4.1$ diff mpn_exp.c.orig mpn_exp.c
74c74
<   MPN_ZERO (a, n - 1);
---
>   if (n > 1) MPN_ZERO (a, n - 1);
```




---

archive/issue_comments_051854.json:
```json
{
    "body": "Since this only appears so far to have happened on a Solaris machine with a T2+ processor, and the patch will slow down the code on every machine, I will create a patch which is only applied on Solaris and only on the sun4v architecture. There is reason to believe it will only affect this type of processor too - not all SPARC processors. (Apparently memset is implemented differently on that). \n\nI think that's a better solution than to apply it everywhere.\n\nLeave it with me. I'll do this. \n\nDave",
    "created_at": "2009-07-16T11:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51854",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Since this only appears so far to have happened on a Solaris machine with a T2+ processor, and the patch will slow down the code on every machine, I will create a patch which is only applied on Solaris and only on the sun4v architecture. There is reason to believe it will only affect this type of processor too - not all SPARC processors. (Apparently memset is implemented differently on that). 

I think that's a better solution than to apply it everywhere.

Leave it with me. I'll do this. 

Dave



---

archive/issue_comments_051855.json:
```json
{
    "body": "Changing keywords from \"\" to \"compiler bug\".",
    "created_at": "2009-07-17T03:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51855",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing keywords from "" to "compiler bug".



---

archive/issue_comments_051856.json:
```json
{
    "body": "I've implemented Paul's patch, but in a way which should cause minimal impact on performance. \n\n1) The patch is only ever applied on Solaris.\n\n2) By default, the patch is applied only on sun4v systems (those based on the Sun T1, T2 and T2+ processors) as the library with memset() is different on that architecture to most others. \n\nThe machine 't2' is sun4v, as it has two Sun T2+ processors. Hence the patch will not be applied on more common machines like my Sun Blade 2000 with its UltraSPARC II processors, which is a sun4u system. \n\n3) It is possible to force the patch to be installed, or force it to not be installed, by setting the environment variable INCLUDE_MPFR_PATCH\n\n\n```\n$ export INCLUDE_MPFR_PATCH=1   (force patch to install)\n$ export INCLUDE_MPFR_PATCH=0   (will not install the patch)\n$ export INCLUDE_MPFR_PATCH=foobar (User mistake. Apply the patch).\n$ unset  INCLUDE_MPFR_PATCH  (Defaults to installing on sun4v only.)\n```\n\n\n\nWhen we distribute binaries for Sage, I suggest they should be built on a Sun with the very first release of Solaris 10 (i.e. NOT 't2', which runs Solaris 10 update 7). I can set up an old machine for that purpose. When building binaries we should set INCLUDE_MPFR_PATCH to 1, so the patch is applied. Then the code should work, on any Solaris 10 SPARC system. (Since my Sun Blade 2000 is not sun4v, the patch would not normally be installed, but I would force it to be installed in this case). \n\nHow to test. \n\n1) Change your setup to use gcc 4.4.0, as that causes the 20 test failures to occur. \n\n\n```\n$ source /usr/local/gcc-4.4.0-sun-linker/gcc440sun\n```\n\n \n\n2) Verify mpfr passes all tests on 't2' with gcc 4.4.0. Previously 20 failures occurred with gcc 4.4.0\n\n3) Check the effects on the messages sent to the screen depend on the settings of the variable INCLUDE_MPFR_PATCH. You do not need to build mpfr with every combination, but after the files are extracted, there will be some messages. Just break the build, and read that they make sense. Compare to what looks logical from spkg-install. \n\nThere is a reasonably comprehensive set of messages, which are output on any Solaris system. The last few messages are specific to the machine's architecture and setting of the variable INCLUDE_MPFR_PATCH. \n\nHere's the specific last part of the message on my personal machine, which is sun4u, and so not the troublesome sun4v, so there is no need for me to patch this. (I say troublesome, but I expect this is a compiler bug). \n\n1) The default, with the variable unset:\n\n\n```\n$ unset INCLUDE_MPFR_PATCH\n$ make\n<SNIP>\nSince this is not a sun4v system, the MPFR binary will not\nbe patched\nWARNING: Problems may occur if you try to run this SPARC\nbinary on a sun4v system (T1, T2 or T2+ processors). Binaries created like\nthis should not distributed unless you know the end users system will not\nbe sun4v. Set INCLUDE_MPFR_PATCH to 1, to include the patch, if you are unsure.\n\n```\n\n\n2) Force the patch to be installed. \n\n\n```\n$ export INCLUDE_MPFR_PATCH=1\n$ make\n<SNIP>\nSince INCLUDE_MPFR_PATCH was set to 1, the MPFR library will be patched.\nThe binaries should be safe on any Solaris system\n```\n\n\n\n3) Force the patch not to be applied (it would not be applied on my machine anyway, but it would be on t2)\n\n\n\n```\n$ export INCLUDE_MPFR_PATCH=0\n$ make\n<SNIP>\nSince INCLUDE_MPFR_PATCH was set to 0, the MPFR library will not\nbe patched. You would be unwise to distribute SPARC binaries\nunless you are sure they will not be used on sun4v systems\n```\n\n\n\n4) Set the environment variable INCLUDE_MPFR_PATCH to some nonsense value\n\n$ export INCLUDE_MPFR_PATCH=foobar\n\n\n```\n$ make\n<SNIP>\nThe environment variable INCLUDE_MPFR_PATCH was set incorrectly The MPFR\nlibrary will be patched as a precaution.\n```\n\n\n\n\n5) Set the environment variable to nothing. This is considered an error \n\n\n```\n$ export INCLUDE_MPFR_PATCH=\n$ make\n<SNIP>\nThe environment variable INCLUDE_MPFR_PATCH was set incorrectly The MPFR\nlibrary will be patched as a precaution.\n```\n\n\nA few others things are done in this patch.\n\n* Removed a comment at the bottom of spkg-install to bypass the checks\n  on release systems. Given failures have occurred, it would be unwise to \n  bypass any checks. \n\n* Add a comment to remind people not to bypass the tests. \n\n* Update the source to use the latest patches, as strongly recommenced in the \n  INSTALL file. This brings the code to MPFR 2.4.1 patch level 5, though I'm\n  considering it mpfr-2.4.1p0 for Sage purposes.",
    "created_at": "2009-07-17T03:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51856",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've implemented Paul's patch, but in a way which should cause minimal impact on performance. 

1) The patch is only ever applied on Solaris.

2) By default, the patch is applied only on sun4v systems (those based on the Sun T1, T2 and T2+ processors) as the library with memset() is different on that architecture to most others. 

The machine 't2' is sun4v, as it has two Sun T2+ processors. Hence the patch will not be applied on more common machines like my Sun Blade 2000 with its UltraSPARC II processors, which is a sun4u system. 

3) It is possible to force the patch to be installed, or force it to not be installed, by setting the environment variable INCLUDE_MPFR_PATCH


```
$ export INCLUDE_MPFR_PATCH=1   (force patch to install)
$ export INCLUDE_MPFR_PATCH=0   (will not install the patch)
$ export INCLUDE_MPFR_PATCH=foobar (User mistake. Apply the patch).
$ unset  INCLUDE_MPFR_PATCH  (Defaults to installing on sun4v only.)
```



When we distribute binaries for Sage, I suggest they should be built on a Sun with the very first release of Solaris 10 (i.e. NOT 't2', which runs Solaris 10 update 7). I can set up an old machine for that purpose. When building binaries we should set INCLUDE_MPFR_PATCH to 1, so the patch is applied. Then the code should work, on any Solaris 10 SPARC system. (Since my Sun Blade 2000 is not sun4v, the patch would not normally be installed, but I would force it to be installed in this case). 

How to test. 

1) Change your setup to use gcc 4.4.0, as that causes the 20 test failures to occur. 


```
$ source /usr/local/gcc-4.4.0-sun-linker/gcc440sun
```

 

2) Verify mpfr passes all tests on 't2' with gcc 4.4.0. Previously 20 failures occurred with gcc 4.4.0

3) Check the effects on the messages sent to the screen depend on the settings of the variable INCLUDE_MPFR_PATCH. You do not need to build mpfr with every combination, but after the files are extracted, there will be some messages. Just break the build, and read that they make sense. Compare to what looks logical from spkg-install. 

There is a reasonably comprehensive set of messages, which are output on any Solaris system. The last few messages are specific to the machine's architecture and setting of the variable INCLUDE_MPFR_PATCH. 

Here's the specific last part of the message on my personal machine, which is sun4u, and so not the troublesome sun4v, so there is no need for me to patch this. (I say troublesome, but I expect this is a compiler bug). 

1) The default, with the variable unset:


```
$ unset INCLUDE_MPFR_PATCH
$ make
<SNIP>
Since this is not a sun4v system, the MPFR binary will not
be patched
WARNING: Problems may occur if you try to run this SPARC
binary on a sun4v system (T1, T2 or T2+ processors). Binaries created like
this should not distributed unless you know the end users system will not
be sun4v. Set INCLUDE_MPFR_PATCH to 1, to include the patch, if you are unsure.

```


2) Force the patch to be installed. 


```
$ export INCLUDE_MPFR_PATCH=1
$ make
<SNIP>
Since INCLUDE_MPFR_PATCH was set to 1, the MPFR library will be patched.
The binaries should be safe on any Solaris system
```



3) Force the patch not to be applied (it would not be applied on my machine anyway, but it would be on t2)



```
$ export INCLUDE_MPFR_PATCH=0
$ make
<SNIP>
Since INCLUDE_MPFR_PATCH was set to 0, the MPFR library will not
be patched. You would be unwise to distribute SPARC binaries
unless you are sure they will not be used on sun4v systems
```



4) Set the environment variable INCLUDE_MPFR_PATCH to some nonsense value

$ export INCLUDE_MPFR_PATCH=foobar


```
$ make
<SNIP>
The environment variable INCLUDE_MPFR_PATCH was set incorrectly The MPFR
library will be patched as a precaution.
```




5) Set the environment variable to nothing. This is considered an error 


```
$ export INCLUDE_MPFR_PATCH=
$ make
<SNIP>
The environment variable INCLUDE_MPFR_PATCH was set incorrectly The MPFR
library will be patched as a precaution.
```


A few others things are done in this patch.

* Removed a comment at the bottom of spkg-install to bypass the checks
  on release systems. Given failures have occurred, it would be unwise to 
  bypass any checks. 

* Add a comment to remind people not to bypass the tests. 

* Update the source to use the latest patches, as strongly recommenced in the 
  INSTALL file. This brings the code to MPFR 2.4.1 patch level 5, though I'm
  considering it mpfr-2.4.1p0 for Sage purposes.



---

archive/issue_comments_051857.json:
```json
{
    "body": "I forgot to give the location of the patch ! All relevant files are in the directory:\n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/mpfr/\n\nThe actual patch is http://sage.math.washington.edu/home/kirkby/Solaris-fixes/mpfr/mpfr-2.4.1p0.spkg",
    "created_at": "2009-07-17T03:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51857",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I forgot to give the location of the patch ! All relevant files are in the directory:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/mpfr/

The actual patch is http://sage.math.washington.edu/home/kirkby/Solaris-fixes/mpfr/mpfr-2.4.1p0.spkg



---

archive/issue_comments_051858.json:
```json
{
    "body": "I updated the package changing just some text, which appeared to have caused some confusion to a potential reviewer. In particular, I did not enable any checks in MPFR - they were already enabled. So my patch will not slow the build process. \n\nPreviously I posted outputs from my own Sun Blade 2000 computer, which is a sun4u architecture and so did NOT need patching. \n\n\n```\n$ make\n<SNIP>\nSince this is not a sun4v system, the MPFR binary will not\nbe patched\nWARNING: Problems may occur if you try to run this SPARC\nbinary on a sun4v system (T1, T2 or T2+ processors). Binaries created like\nthis should not distributed unless you know the end users system will not\nbe sun4v. Set INCLUDE_MPFR_PATCH to 1, to include the patch, if you are unsure.\n```\n\n\nHere's the default output seen on 't2' with this new patch:\n\n```\n$ make \n<SNIP>\nThis is a sun4v system, so the MPFR library will be patched. The binaries\nshould run correctly on any SPARC system whose operating system is\nno older than the system used to build the binaries.\n```\n\n\nNotice how it differs from that on my own machine ? Here's the output from 'uname' and 'arch -k' on both my Sun Blade 2000 (kestrel) and a Sun T5240 (t2)\n\nFirst 't2'\n\n```\nkirkby@t2:[~] $ uname -a\nuname -a\nSunOS t2 5.10 Generic_141414-02 sun4v sparc SUNW,T5240\nkirkby@t2:[~] $ arch -k\narch -k\nsun4v\n```\n\nnow my home machine 'kestrel', which is actually a Blade 2000, not a Blade 1000 as the output says. The two machines share the same motherboard. \n\n```\ndrkirkby@kestrel:[~] $ arch -k\nsun4u\ndrkirkby@kestrel:[~] $ uname -a\nSunOS kestrel 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n```\n\n\n\n* Sun Blade 2000 ('kestrel') has a sun4u architecture, so does not need patching\n\n* Sun T5240 ('t2') has a sun4v architecture, so does need patching\n\nOn either system it is possible to override the default.\n\nI've put the code in /tmp/kirkby/sage-4.1/ on 't2' and changed the permissions of all files so any user can write to them. It will allow testing by others. (Of course it could break too, if two people start testing together, but that is a risk I will take).\n\nIt should be noted that were are not really any closer to solving this, as at least 4 explanations have been given by different people:\n\n* It's an MPFR bug\n\n* It's an MPIR bug \n\n* It's a gcc bug\n\n* It's a bug in the Solaris implementation of memset on sun4v systems. \n\nNote, although I don't believe there is any plans to support Solaris 9, I don't actually see why Sage should not work on a Solaris 9 system. A Solaris 9 system could be using the even older sun4m architecture. Although I've not checked it, the updated .spkg file should work on that too, but will not apply the patch by default.\n\nDave",
    "created_at": "2009-07-17T23:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51858",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I updated the package changing just some text, which appeared to have caused some confusion to a potential reviewer. In particular, I did not enable any checks in MPFR - they were already enabled. So my patch will not slow the build process. 

Previously I posted outputs from my own Sun Blade 2000 computer, which is a sun4u architecture and so did NOT need patching. 


```
$ make
<SNIP>
Since this is not a sun4v system, the MPFR binary will not
be patched
WARNING: Problems may occur if you try to run this SPARC
binary on a sun4v system (T1, T2 or T2+ processors). Binaries created like
this should not distributed unless you know the end users system will not
be sun4v. Set INCLUDE_MPFR_PATCH to 1, to include the patch, if you are unsure.
```


Here's the default output seen on 't2' with this new patch:

```
$ make 
<SNIP>
This is a sun4v system, so the MPFR library will be patched. The binaries
should run correctly on any SPARC system whose operating system is
no older than the system used to build the binaries.
```


Notice how it differs from that on my own machine ? Here's the output from 'uname' and 'arch -k' on both my Sun Blade 2000 (kestrel) and a Sun T5240 (t2)

First 't2'

```
kirkby@t2:[~] $ uname -a
uname -a
SunOS t2 5.10 Generic_141414-02 sun4v sparc SUNW,T5240
kirkby@t2:[~] $ arch -k
arch -k
sun4v
```

now my home machine 'kestrel', which is actually a Blade 2000, not a Blade 1000 as the output says. The two machines share the same motherboard. 

```
drkirkby@kestrel:[~] $ arch -k
sun4u
drkirkby@kestrel:[~] $ uname -a
SunOS kestrel 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
```



* Sun Blade 2000 ('kestrel') has a sun4u architecture, so does not need patching

* Sun T5240 ('t2') has a sun4v architecture, so does need patching

On either system it is possible to override the default.

I've put the code in /tmp/kirkby/sage-4.1/ on 't2' and changed the permissions of all files so any user can write to them. It will allow testing by others. (Of course it could break too, if two people start testing together, but that is a risk I will take).

It should be noted that were are not really any closer to solving this, as at least 4 explanations have been given by different people:

* It's an MPFR bug

* It's an MPIR bug 

* It's a gcc bug

* It's a bug in the Solaris implementation of memset on sun4v systems. 

Note, although I don't believe there is any plans to support Solaris 9, I don't actually see why Sage should not work on a Solaris 9 system. A Solaris 9 system could be using the even older sun4m architecture. Although I've not checked it, the updated .spkg file should work on that too, but will not apply the patch by default.

Dave



---

archive/issue_comments_051859.json:
```json
{
    "body": "This looks more and more like a Solaris bug, as the following bit of code, compiled in 32-bit mode should add the number 2 raised to the power of 31 to another number of 2 raised to the power of 31 so get a total of 2 raised to the power of 32, which is 0 in 32-bit mode. But it dumps core on 't2', and not on my Sun Blade 2000 or any other non-Solaris machine for which people have tested this. \n\n[ You might wonder why I spelled out 'raised to the power of' but the formatting goes a bit crazy if I write 2^31 plus 2^31 is equal to 2^32) perhaps you see that]\n\nIt also dumps core with the Sun compiler. \n\n\n```\nkirkby@t2:[~] $ /opt/SUNWspro/bin/cc check4.c\nkirkby@t2:[~] $ ./a.out\nn=0\nn=1\nAbort (core dumped)\nkirkby@t2:[~] $ cat check4.c\n#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nvolatile size_t i = 0x80000000U, j = 0x80000000U;\nchar buf[16];\n\nint main (void)\n{\n  int n;\n\n  for (n=0 ; n <=10;++n) {\n    printf(\"n=%d\\n\",n);\n    if (sizeof (size_t) != 4)\n      return 0;\n    buf[n] = 6;\n    memset (buf+n, 0, i + j);\n    if (buf[n] != 6)\n      abort ();\n  }\n  return 0;\n}\n```\n\n\n\nI still believe in the short term, the fix here should be applied. Even if it can't be guaranteed to work in every case, it is allows MPFR to build and pasts all the tests, it will allow progress to be made in Sage. \n\nThe fact I have been careful to only apply this to sun4v machines, should ensure it has no impact on anywhere else. \n\nDave",
    "created_at": "2009-07-18T20:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51859",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This looks more and more like a Solaris bug, as the following bit of code, compiled in 32-bit mode should add the number 2 raised to the power of 31 to another number of 2 raised to the power of 31 so get a total of 2 raised to the power of 32, which is 0 in 32-bit mode. But it dumps core on 't2', and not on my Sun Blade 2000 or any other non-Solaris machine for which people have tested this. 

[ You might wonder why I spelled out 'raised to the power of' but the formatting goes a bit crazy if I write 2^31 plus 2^31 is equal to 2^32) perhaps you see that]

It also dumps core with the Sun compiler. 


```
kirkby@t2:[~] $ /opt/SUNWspro/bin/cc check4.c
kirkby@t2:[~] $ ./a.out
n=0
n=1
Abort (core dumped)
kirkby@t2:[~] $ cat check4.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

volatile size_t i = 0x80000000U, j = 0x80000000U;
char buf[16];

int main (void)
{
  int n;

  for (n=0 ; n <=10;++n) {
    printf("n=%d\n",n);
    if (sizeof (size_t) != 4)
      return 0;
    buf[n] = 6;
    memset (buf+n, 0, i + j);
    if (buf[n] != 6)
      abort ();
  }
  return 0;
}
```



I still believe in the short term, the fix here should be applied. Even if it can't be guaranteed to work in every case, it is allows MPFR to build and pasts all the tests, it will allow progress to be made in Sage. 

The fact I have been careful to only apply this to sun4v machines, should ensure it has no impact on anywhere else. 

Dave



---

archive/issue_comments_051860.json:
```json
{
    "body": "David: Here's an updated SPKG with all changes committed in your name:\n\nhttp://sage.math.washington.edu/home/mvngu/patch/mpfr-2.4.1.p0.spkg\n\nI have renamed it from `mpfr-2.4.1p0.spkg` to `mpfr-2.4.1.p0.spkg`; notice the period between 1 and p0.",
    "created_at": "2009-07-24T06:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51860",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

David: Here's an updated SPKG with all changes committed in your name:

http://sage.math.washington.edu/home/mvngu/patch/mpfr-2.4.1.p0.spkg

I have renamed it from `mpfr-2.4.1p0.spkg` to `mpfr-2.4.1.p0.spkg`; notice the period between 1 and p0.



---

archive/issue_comments_051861.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-24T06:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51861",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_051862.json:
```json
{
    "body": "Successfully compiles on Solaris/t2. All 148 tests passed. (It even builds OK on Linux.)",
    "created_at": "2009-07-24T06:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51862",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Successfully compiles on Solaris/t2. All 148 tests passed. (It even builds OK on Linux.)



---

archive/issue_events_015240.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-24T06:58:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6453#event-15240"
}
```



---

archive/issue_comments_051863.json:
```json
{
    "body": "For the record, this is **not** a compiler bug, but a bug in Sun's implementation of memset() on the sun4v architecture (i.e. the CoolThreads machines). The bug has been confirmed by Sun.",
    "created_at": "2009-07-24T14:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51863",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

For the record, this is **not** a compiler bug, but a bug in Sun's implementation of memset() on the sun4v architecture (i.e. the CoolThreads machines). The bug has been confirmed by Sun.



---

archive/issue_comments_051864.json:
```json
{
    "body": "The confirmation from Sun can be found at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/75962dd6d45f7ab0) thread.",
    "created_at": "2009-07-24T14:08:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51864",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The confirmation from Sun can be found at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/75962dd6d45f7ab0) thread.



---

archive/issue_comments_051865.json:
```json
{
    "body": "Oops, Sun have fixed this, not just acknowledged the bug. Hence I'm changing the 'Report Upstream' to reflect this.",
    "created_at": "2009-11-29T10:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6453",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6453#issuecomment-51865",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Oops, Sun have fixed this, not just acknowledged the bug. Hence I'm changing the 'Report Upstream' to reflect this.
