# Issue 6453: MPFR test failures in Sage

Issue created by migration from https://trac.sagemath.org/ticket/6453

Original creator: drkirkby

Original creation time: 2009-07-01 04:09:23

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


---

Comment by drkirkby created at 2009-07-01 04:13:27

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2009-07-01 04:13:27

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

Comment by drkirkby created at 2009-07-01 04:13:27

Changing status from new to assigned.


---

Attachment

config.log showing no optimisation on the command line. Still 20 tests fail


---

Comment by drkirkby created at 2009-07-13 23:02:35

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

Comment by drkirkby created at 2009-07-13 23:03:59

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

Comment by zimmerma created at 2009-07-15 00:18:01

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

Comment by drkirkby created at 2009-07-16 11:58:13

Since this only appears so far to have happened on a Solaris machine with a T2+ processor, and the patch will slow down the code on every machine, I will create a patch which is only applied on Solaris and only on the sun4v architecture. There is reason to believe it will only affect this type of processor too - not all SPARC processors. (Apparently memset is implemented differently on that). 

I think that's a better solution than to apply it everywhere.

Leave it with me. I'll do this. 

Dave


---

Comment by drkirkby created at 2009-07-17 03:11:32

Changing keywords from "" to "compiler bug".


---

Comment by drkirkby created at 2009-07-17 03:11:32

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

Comment by drkirkby created at 2009-07-17 03:14:53

I forgot to give the location of the patch ! All relevant files are in the directory:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/mpfr/

The actual patch is http://sage.math.washington.edu/home/kirkby/Solaris-fixes/mpfr/mpfr-2.4.1p0.spkg


---

Comment by drkirkby created at 2009-07-17 23:47:50

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

Comment by drkirkby created at 2009-07-18 20:23:39

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

Comment by mvngu created at 2009-07-24 06:07:30

David: Here's an updated SPKG with all changes committed in your name:

http://sage.math.washington.edu/home/mvngu/patch/mpfr-2.4.1.p0.spkg

I have renamed it from `mpfr-2.4.1p0.spkg` to `mpfr-2.4.1.p0.spkg`; notice the period between 1 and p0.


---

Comment by mvngu created at 2009-07-24 06:58:59

Resolution: fixed


---

Comment by mvngu created at 2009-07-24 06:58:59

Successfully compiles on Solaris/t2. All 148 tests passed. (It even builds OK on Linux.)


---

Comment by drkirkby created at 2009-07-24 14:04:47

For the record, this is *not* a compiler bug, but a bug in Sun's implementation of memset() on the sun4v architecture (i.e. the CoolThreads machines). The bug has been confirmed by Sun.


---

Comment by mvngu created at 2009-07-24 14:08:41

The confirmation from Sun can be found at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/75962dd6d45f7ab0) thread.


---

Comment by drkirkby created at 2009-11-29 10:38:15

Oops, Sun have fixed this, not just acknowledged the bug. Hence I'm changing the 'Report Upstream' to reflect this.
