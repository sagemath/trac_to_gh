# Issue 5847: Update GMP-ECM to 6.2.2

archive/issues_005847.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  zimmerma dimpase\n\n\n```\nChanges between ecm-6.2.1 and ecm-6.2.2:\n* Updated build project files for Visual C by Brian Gladman, also adds\nmissing NTT_GFP_TWIDDLE_DI[FT]_BREAKOVER defines in VC parameter file\n* Fixed uninitialised parameter to P-1 probability computation\n* In tune.c : fixed generation of NTT_GFP_TWIDDLE_DI[FT]_BREAKOVER values,\navoid calling cputime() excessively often when timing short functions,\nfixed access to uninitialised memory\n* Fixed serious split infinitive in configure script (thanks Paul Leyland)\n* Removed unnecessary carry propagation in x86_64 mulredc code, slight\nspeedup (thanks Philip McLaughlin)\n* Fixed non-portable PIC code in x86_64/redc.asm\n* Fixed problem with pattern matching host type names in configure.in\n* Converted binary constants in spv.c and ntt_gfp.c to hexadecimal,\nsome assembler do not support binary constants\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5847\n\n",
    "created_at": "2009-04-21T23:49:57Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Update GMP-ECM to 6.2.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5847",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  zimmerma dimpase


```
Changes between ecm-6.2.1 and ecm-6.2.2:
* Updated build project files for Visual C by Brian Gladman, also adds
missing NTT_GFP_TWIDDLE_DI[FT]_BREAKOVER defines in VC parameter file
* Fixed uninitialised parameter to P-1 probability computation
* In tune.c : fixed generation of NTT_GFP_TWIDDLE_DI[FT]_BREAKOVER values,
avoid calling cputime() excessively often when timing short functions,
fixed access to uninitialised memory
* Fixed serious split infinitive in configure script (thanks Paul Leyland)
* Removed unnecessary carry propagation in x86_64 mulredc code, slight
speedup (thanks Philip McLaughlin)
* Fixed non-portable PIC code in x86_64/redc.asm
* Fixed problem with pattern matching host type names in configure.in
* Converted binary constants in spv.c and ntt_gfp.c to hexadecimal,
some assembler do not support binary constants
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5847





---

archive/issue_comments_045993.json:
```json
{
    "body": "\n```\nI think you may need the latest 6.3\n\n ./configure --with-gmp=/usr/local/\nmake -j\nmake -j check\nand it passed\nwithout specifing where gmp/mpir is , it got very confused , , they have their\nsearch paths mixed up.\n\nJason\n- Hide quoted text -\n\nOn Wednesday 02 June 2010 02:59:21 Bill Hart wrote:\n> There's an open ticket by Michael Abshoff to update to 6.2.2: :-)\n>\n> http://trac.sagemath.org/sage_trac/ticket/5847\n>\n> Bill.\n>\n> On 2 June 2010 02:54, Jason Moxham <jason@njkfrudils.plus.com> wrote:\n> > I had forgotten about this , gmp-ecm-6.2.1 is 2 years old , what is it\n> > doing in sage ? :) , they fixed it in a later release , perhaps about a\n> > year ago\n> >\n> > Jason\n> >\n> > On Wednesday 02 June 2010 02:46:58 Bill Hart wrote:\n> >> On 2 June 2010 02:40, William Stein <wstein@gmail.com> wrote:\n> >> > Hi,\n> >> >\n> >> > Building Sage fails with GMP-ECM, as before.   Yes, I know this is\n> >> > because of deprecation, etc...\n> >>\n> >> Sure. We announced a list of deprecated symbols on sage-devel and\n> >> mpir-devel. Then we permanently removed mpz_random and mpz_random2\n> >> *only* , the worst offenders.\n> >>\n> >> Bill.\n> >>\n> >> > ar cru .libs/libecm.a  ecm.o ecm2.o pm1.o pp1.o getprime.o listz.o\n> >> > lucas.o stage2.o toomcook.o mpmod.o mul_l\n> >> > o.o polyeval.o median.o schoen_strass.o ks-multiply.o rho.o bestd.o\n> >> > auxlib.o random.o factor.o sp.o spv.o sp\n> >> > m.o mpzspm.o mpzspv.o ntt_gfp.o ecm_ntt.o pm1fs2.o mul_fft.o\n> >> > sets_long.o auxarith.otune-tune.o: In function `tune_mpres_mul':\n> >> > tune.c:(.text+0xd1): undefined reference to `mpz_random'\n> >> > collect2: ld returned 1 exit status\n> >> > make[4]: *** [tune] Error 1\n> >> > make[4]: *** Waiting for unfinished jobs....\n> >> > ranlib .libs/libecm.a\n> >> > creating libecm.la\n> >> > (cd .libs && rm -f libecm.la && ln -s ../libecm.la libecm.la)\n> >> > make[4]: Leaving directory\n> >> > `/mnt/usb1/scratch/wstein/build/mpir2/sage-4.4.3.alpha1/spkg/build/ecm\n> >> >-6. 2.1.p2/s rc'\n> >> > make[3]: *** [all-recursive] Error 1\n> >> > make[3]: Leaving directory\n> >> > `/mnt/usb1/scratch/wstein/build/mpir2/sage-4.4.3.alpha1/spkg/build/ecm\n> >> >-6. 2.1.p2/src' make[2]: *** [all] Error 2make[2]: Leaving directory\n> >> > `/mnt/usb1/scratch/wstein/build/mpir2/sage-4.4.3.alpha1/spkg/build/ecm\n> >> >-6. 2.1.p2/s rc'\n> >> > There was a problem building GMP ECM.\n> >> >\n> >> > real    0m9.633s\n> >> > user    0m8.510s\n> >> > sys     0m8.950s\n> >> > sage: An error occurred while installing ecm-6.2.1.p2\n> >> > Please email sage-devel http://groups.google.com/group/sage-devel\n```\n",
    "created_at": "2010-06-02T02:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-45993",
    "user": "was"
}
```


```
I think you may need the latest 6.3

 ./configure --with-gmp=/usr/local/
make -j
make -j check
and it passed
without specifing where gmp/mpir is , it got very confused , , they have their
search paths mixed up.

Jason
- Hide quoted text -

On Wednesday 02 June 2010 02:59:21 Bill Hart wrote:
> There's an open ticket by Michael Abshoff to update to 6.2.2: :-)
>
> http://trac.sagemath.org/sage_trac/ticket/5847
>
> Bill.
>
> On 2 June 2010 02:54, Jason Moxham <jason@njkfrudils.plus.com> wrote:
> > I had forgotten about this , gmp-ecm-6.2.1 is 2 years old , what is it
> > doing in sage ? :) , they fixed it in a later release , perhaps about a
> > year ago
> >
> > Jason
> >
> > On Wednesday 02 June 2010 02:46:58 Bill Hart wrote:
> >> On 2 June 2010 02:40, William Stein <wstein@gmail.com> wrote:
> >> > Hi,
> >> >
> >> > Building Sage fails with GMP-ECM, as before.   Yes, I know this is
> >> > because of deprecation, etc...
> >>
> >> Sure. We announced a list of deprecated symbols on sage-devel and
> >> mpir-devel. Then we permanently removed mpz_random and mpz_random2
> >> *only* , the worst offenders.
> >>
> >> Bill.
> >>
> >> > ar cru .libs/libecm.a  ecm.o ecm2.o pm1.o pp1.o getprime.o listz.o
> >> > lucas.o stage2.o toomcook.o mpmod.o mul_l
> >> > o.o polyeval.o median.o schoen_strass.o ks-multiply.o rho.o bestd.o
> >> > auxlib.o random.o factor.o sp.o spv.o sp
> >> > m.o mpzspm.o mpzspv.o ntt_gfp.o ecm_ntt.o pm1fs2.o mul_fft.o
> >> > sets_long.o auxarith.otune-tune.o: In function `tune_mpres_mul':
> >> > tune.c:(.text+0xd1): undefined reference to `mpz_random'
> >> > collect2: ld returned 1 exit status
> >> > make[4]: *** [tune] Error 1
> >> > make[4]: *** Waiting for unfinished jobs....
> >> > ranlib .libs/libecm.a
> >> > creating libecm.la
> >> > (cd .libs && rm -f libecm.la && ln -s ../libecm.la libecm.la)
> >> > make[4]: Leaving directory
> >> > `/mnt/usb1/scratch/wstein/build/mpir2/sage-4.4.3.alpha1/spkg/build/ecm
> >> >-6. 2.1.p2/s rc'
> >> > make[3]: *** [all-recursive] Error 1
> >> > make[3]: Leaving directory
> >> > `/mnt/usb1/scratch/wstein/build/mpir2/sage-4.4.3.alpha1/spkg/build/ecm
> >> >-6. 2.1.p2/src' make[2]: *** [all] Error 2make[2]: Leaving directory
> >> > `/mnt/usb1/scratch/wstein/build/mpir2/sage-4.4.3.alpha1/spkg/build/ecm
> >> >-6. 2.1.p2/s rc'
> >> > There was a problem building GMP ECM.
> >> >
> >> > real    0m9.633s
> >> > user    0m8.510s
> >> > sys     0m8.950s
> >> > sage: An error occurred while installing ecm-6.2.1.p2
> >> > Please email sage-devel http://groups.google.com/group/sage-devel
```




---

archive/issue_comments_045994.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-17T18:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-45994",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_045995.json:
```json
{
    "body": "There is a 6.3 spkg at http://sage.math.washington.edu/home/mhansen/ecm-6.3.spkg\n\nI've checked that it works with MPIR 2.1.1 and all tests pass.",
    "created_at": "2010-08-17T18:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-45995",
    "user": "mhansen"
}
```

There is a 6.3 spkg at http://sage.math.washington.edu/home/mhansen/ecm-6.3.spkg

I've checked that it works with MPIR 2.1.1 and all tests pass.



---

archive/issue_comments_045996.json:
```json
{
    "body": "Since Sage with MPIR 2.1.1 (#8664) requires updating to this package, I report at that ticket.",
    "created_at": "2010-08-27T14:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-45996",
    "user": "leif"
}
```

Since Sage with MPIR 2.1.1 (#8664) requires updating to this package, I report at that ticket.



---

archive/issue_comments_045997.json:
```json
{
    "body": "Since MPIR 2.1.1 has a bug (see #9837), I've (successfully) built and tested Sage 4.6.prealpha3 (see #9343 and [the NewPARI Wiki page](http://wiki.sagemath.org/NewPARI)) **with GMP 5.0.1** and this new ECM 6.3 spkg on Ubuntu 10.04 x86_64 (Core2, gcc 4.4.3; parallel build from scratch with 32 jobs; native code with O3).\n\n`ptestlong` passed all tests.",
    "created_at": "2010-09-02T22:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-45997",
    "user": "leif"
}
```

Since MPIR 2.1.1 has a bug (see #9837), I've (successfully) built and tested Sage 4.6.prealpha3 (see #9343 and [the NewPARI Wiki page](http://wiki.sagemath.org/NewPARI)) **with GMP 5.0.1** and this new ECM 6.3 spkg on Ubuntu 10.04 x86_64 (Core2, gcc 4.4.3; parallel build from scratch with 32 jobs; native code with O3).

`ptestlong` passed all tests.



---

archive/issue_comments_045998.json:
```json
{
    "body": "It also passed `ptestlong` on the same machine with Sage **4.5.3.alpha2** and **MPIR** 2.1.1 (because the MPIR bug apparently only shows up in combination with the new PARI package, which isn't included in that Sage version).\n\nSame for Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4, parallel build with 6 jobs, rest dito).",
    "created_at": "2010-09-02T23:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-45998",
    "user": "leif"
}
```

It also passed `ptestlong` on the same machine with Sage **4.5.3.alpha2** and **MPIR** 2.1.1 (because the MPIR bug apparently only shows up in combination with the new PARI package, which isn't included in that Sage version).

Same for Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4, parallel build with 6 jobs, rest dito).



---

archive/issue_comments_045999.json:
```json
{
    "body": "Attachment\n\nSuggested changes - NOT (yet) a Mercurial patch. (Minor fixes, some comments added, some clean-up.)",
    "created_at": "2010-09-03T03:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-45999",
    "user": "leif"
}
```

Attachment

Suggested changes - NOT (yet) a Mercurial patch. (Minor fixes, some comments added, some clean-up.)



---

archive/issue_comments_046000.json:
```json
{
    "body": "I've added a reviewer patch (ordinary context diff) with some changes:\n\n* Remove also the manual page of previous installations.\n* Typo: `rm -r` -> `rm -f` (header file)\n* Removed setting of `CXXFLAGS`, since we don't have C++ code.\n* Don't overwrite `CFLAGS` if `SAGE64=yes` (instead, append). Removed `-O2 -g` in that case. Make use of `CFLAG64` if set.\n* Quote `$SAGE_LOCAL` in the parameters to `configure`, too.\n* Use `$MAKE` in `spkg-check`, too.\n* Some messages changed (e.g. all failures now starting with *\"Error\"*), some added.\n* A few comments/notes added (`SPKG.txt`, `spkg-install`).\n\nIf you're ok with the changes, I can replace the diff with a Mercurial patch. Or simply merge them...",
    "created_at": "2010-09-03T03:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46000",
    "user": "leif"
}
```

I've added a reviewer patch (ordinary context diff) with some changes:

* Remove also the manual page of previous installations.
* Typo: `rm -r` -> `rm -f` (header file)
* Removed setting of `CXXFLAGS`, since we don't have C++ code.
* Don't overwrite `CFLAGS` if `SAGE64=yes` (instead, append). Removed `-O2 -g` in that case. Make use of `CFLAG64` if set.
* Quote `$SAGE_LOCAL` in the parameters to `configure`, too.
* Use `$MAKE` in `spkg-check`, too.
* Some messages changed (e.g. all failures now starting with *"Error"*), some added.
* A few comments/notes added (`SPKG.txt`, `spkg-install`).

If you're ok with the changes, I can replace the diff with a Mercurial patch. Or simply merge them...



---

archive/issue_comments_046001.json:
```json
{
    "body": "**New spkg: http://spkg-upload.googlecode.com/files/ecm-6.3.p0.spkg**\n\n**md5sum:** `b9b1fcd5ebc2e3689fd379c1dba3a372  ecm-6.3.p0.spkg`\n\nNew spkg based on Mike's with some more changes (than mentioned above).\n\nShould be installed with the MPIR 2.1.3 spkg from #8664. See instructions there.\n\n(Tested with Sage 4.6.1.alpha0 on Ubuntu 9.04 x86 and Ubuntu 10.04 x86_64.)",
    "created_at": "2010-11-04T05:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46001",
    "user": "leif"
}
```

**New spkg: http://spkg-upload.googlecode.com/files/ecm-6.3.p0.spkg**

**md5sum:** `b9b1fcd5ebc2e3689fd379c1dba3a372  ecm-6.3.p0.spkg`

New spkg based on Mike's with some more changes (than mentioned above).

Should be installed with the MPIR 2.1.3 spkg from #8664. See instructions there.

(Tested with Sage 4.6.1.alpha0 on Ubuntu 9.04 x86 and Ubuntu 10.04 x86_64.)



---

archive/issue_comments_046002.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-11-04T05:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46002",
    "user": "leif"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_046003.json:
```json
{
    "body": "SPKG \"reviewer\" patch, based on Mike's, i.e. ecm-6.3 vs. ecm-6.3.p0. For reference/review.",
    "created_at": "2010-11-04T05:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46003",
    "user": "leif"
}
```

SPKG "reviewer" patch, based on Mike's, i.e. ecm-6.3 vs. ecm-6.3.p0. For reference/review.



---

archive/issue_comments_046004.json:
```json
{
    "body": "Attachment\n\nBuilt and tested on sage.math.washington.edu without problems.",
    "created_at": "2010-11-04T15:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46004",
    "user": "jdemeyer"
}
```

Attachment

Built and tested on sage.math.washington.edu without problems.



---

archive/issue_comments_046005.json:
```json
{
    "body": "Changing assignee from mabshoff to leif.",
    "created_at": "2010-11-04T18:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46005",
    "user": "leif"
}
```

Changing assignee from mabshoff to leif.



---

archive/issue_comments_046006.json:
```json
{
    "body": "This fails to compile on my OS X 10.4 powerpc G5 machine, full log attached but here is the interesting part:\n\n```\n****************************************************\nHost system\nuname -a:\nDarwin moufang.ugent.be 8.11.0 Darwin Kernel Version 8.11.0: Wed Oct 10 18:26:00 PDT 2007; root:xnu-792.24.17~1/RELEASE_PPC Power         Macintosh powerpc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: powerpc-apple-darwin8\nConfigured with: /private/var/tmp/gcc/gcc-5367.obj~1/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man -- enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-    slibdir=/usr/lib --build=powerpc-apple-darwin8 --host=powerpc-apple-darwin8 --target=powerpc-apple-darwin8\nThread model: posix\ngcc version 4.0.1 (Apple Computer, Inc. build 5367)\n****************************************************\n...\nchecking build system type... powerpc-apple-darwin8.11.0\nchecking host system type... powerpc-apple-darwin8.11.0\n...\nconfigure: Configuration:\nconfigure: Build for host type powerpc-apple-darwin8.11.0\nconfigure: CC=gcc, CFLAGS=-g -O3  -fPIC\nconfigure: Linking GMP with -lgmp\nconfigure: Using asm redc code from directory powerpc64\nconfigure: Not using SSE2 instructions in NTT code\nconfigure: Assertions disabled\nconfigure: Shell command execution disabled\nconfigure: OpenMP disabled\nconfigure: Memory debugging disabled\nmake  all-recursive\nMaking all in powerpc64\nm4 -I../ -DOPERATION_mulredc1 `test -f mulredc1.asm || echo './'`mulredc1.asm >mulredc1.s\n/bin/sh ../libtool   --mode=compile gcc  -g -O3  -fPIC -c -o mulredc1.lo mulredc1.s\nlibtool: compile:  gcc -g -O3 -fPIC -c mulredc1.s -o mulredc1.o\nmulredc1.s:40:mulld instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)\nmulredc1.s:41:mulhdu instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)\nmulredc1.s:42:mulld instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)\nmulredc1.s:43:mulld instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)\nmulredc1.s:44:mulhdu instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)\nmulredc1.s:47:std instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)\nmake[4]: *** [mulredc1.lo] Error 1\nrm mulredc1.s\nmake[3]: *** [all-recursive] Error 1\nmake[2]: *** [all] Error 2\nError building GMP-ECM.\n```\n",
    "created_at": "2010-11-04T19:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46006",
    "user": "jdemeyer"
}
```

This fails to compile on my OS X 10.4 powerpc G5 machine, full log attached but here is the interesting part:

```
****************************************************
Host system
uname -a:
Darwin moufang.ugent.be 8.11.0 Darwin Kernel Version 8.11.0: Wed Oct 10 18:26:00 PDT 2007; root:xnu-792.24.17~1/RELEASE_PPC Power         Macintosh powerpc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: powerpc-apple-darwin8
Configured with: /private/var/tmp/gcc/gcc-5367.obj~1/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man -- enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-    slibdir=/usr/lib --build=powerpc-apple-darwin8 --host=powerpc-apple-darwin8 --target=powerpc-apple-darwin8
Thread model: posix
gcc version 4.0.1 (Apple Computer, Inc. build 5367)
****************************************************
...
checking build system type... powerpc-apple-darwin8.11.0
checking host system type... powerpc-apple-darwin8.11.0
...
configure: Configuration:
configure: Build for host type powerpc-apple-darwin8.11.0
configure: CC=gcc, CFLAGS=-g -O3  -fPIC
configure: Linking GMP with -lgmp
configure: Using asm redc code from directory powerpc64
configure: Not using SSE2 instructions in NTT code
configure: Assertions disabled
configure: Shell command execution disabled
configure: OpenMP disabled
configure: Memory debugging disabled
make  all-recursive
Making all in powerpc64
m4 -I../ -DOPERATION_mulredc1 `test -f mulredc1.asm || echo './'`mulredc1.asm >mulredc1.s
/bin/sh ../libtool   --mode=compile gcc  -g -O3  -fPIC -c -o mulredc1.lo mulredc1.s
libtool: compile:  gcc -g -O3 -fPIC -c mulredc1.s -o mulredc1.o
mulredc1.s:40:mulld instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)
mulredc1.s:41:mulhdu instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)
mulredc1.s:42:mulld instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)
mulredc1.s:43:mulld instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)
mulredc1.s:44:mulhdu instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)
mulredc1.s:47:std instruction is only for 64-bit implementations (not allowed without -force_cpusubtype_ALL option)
make[4]: *** [mulredc1.lo] Error 1
rm mulredc1.s
make[3]: *** [all-recursive] Error 1
make[2]: *** [all] Error 2
Error building GMP-ECM.
```




---

archive/issue_comments_046007.json:
```json
{
    "body": "Log file for failed build on OS X 10.4 powerpc G5",
    "created_at": "2010-11-04T19:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46007",
    "user": "jdemeyer"
}
```

Log file for failed build on OS X 10.4 powerpc G5



---

archive/issue_comments_046008.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-11-04T19:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46008",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_046009.json:
```json
{
    "body": "Well, I think these are the relevant parts:\n\n```\n...\nchecking whether we can link against GMP... yes\nchecking if gmp.h version and libgmp version are the same... (5.0.1/5.0.1) yes\nchecking for __gmpn_add_nc... yes\nchecking for __gmpn_mod_34lsub1... yes\nchecking for __gmpn_redc_1... no\n...\nconfigure: Using asm redc code from directory powerpc64\n...\n```\n\n\nSo it's probably an upstream problem, either MPIR or ECM.\n\nOr should we pass `-force_cpusubtype_ALL`? (To the assembler?) I think rather not.\n\nWhat happens on other PPCs?\n\nCan you try installing it with GMP 5.0.1?",
    "created_at": "2010-11-05T02:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46009",
    "user": "leif"
}
```

Well, I think these are the relevant parts:

```
...
checking whether we can link against GMP... yes
checking if gmp.h version and libgmp version are the same... (5.0.1/5.0.1) yes
checking for __gmpn_add_nc... yes
checking for __gmpn_mod_34lsub1... yes
checking for __gmpn_redc_1... no
...
configure: Using asm redc code from directory powerpc64
...
```


So it's probably an upstream problem, either MPIR or ECM.

Or should we pass `-force_cpusubtype_ALL`? (To the assembler?) I think rather not.

What happens on other PPCs?

Can you try installing it with GMP 5.0.1?



---

archive/issue_comments_046010.json:
```json
{
    "body": "Paul, perhaps you have an idea what's going wrong there (ECM trying to use \"64-bit\" instructions on MacOS X 10.4 PPC [G5], with MPIR 2.1.3).",
    "created_at": "2010-11-05T02:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46010",
    "user": "leif"
}
```

Paul, perhaps you have an idea what's going wrong there (ECM trying to use "64-bit" instructions on MacOS X 10.4 PPC [G5], with MPIR 2.1.3).



---

archive/issue_comments_046011.json:
```json
{
    "body": "Jeroen, can you try configuring with `--disable-asm-redc`?\n\n(The 64-bit PPC asm code is new in 6.3 btw.)",
    "created_at": "2010-11-05T03:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46011",
    "user": "leif"
}
```

Jeroen, can you try configuring with `--disable-asm-redc`?

(The 64-bit PPC asm code is new in 6.3 btw.)



---

archive/issue_comments_046012.json:
```json
{
    "body": "Replying to [comment:13 leif]:\n> Well, I think these are the relevant parts:\n> {{{\n> ...\n> checking whether we can link against GMP... yes\n> checking if gmp.h version and libgmp version are the same... (5.0.1/5.0.1) yes\n> checking for __gmpn_add_nc... yes\n> checking for __gmpn_mod_34lsub1... yes\n> checking for __gmpn_redc_1... no\n> ...\n> configure: Using asm redc code from directory powerpc64\n> ...\n> }}}\n> \n> So it's probably an upstream problem, either MPIR or ECM.\n> \n> Or should we pass `-force_cpusubtype_ALL`? (To the assembler?) I think rather not.\n> \n> What happens on other PPCs?\n> \n> Can you try installing it with GMP 5.0.1?\n> \nA remark about installing with GMP 5. On Gentoo I had to apply the following\nfor it to compile\n\n```\n\t# fixes for gmp-5\n\tsed -i \"s:__GMP_BITS_PER_MP_LIMB:GMP_LIMB_BITS:g\" bestd.c mpmod.c \\\n\t\tschoen_strass.c sp.h || die \"failed to patch files for gmp-5\"\n```\n\nThis is backward compatible with GMP 4.3. I am a bit surprised that with the stuff\nthat mpir has deprecated, they didn't deprecate that as well.",
    "created_at": "2010-11-05T07:48:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46012",
    "user": "fbissey"
}
```

Replying to [comment:13 leif]:
> Well, I think these are the relevant parts:
> {{{
> ...
> checking whether we can link against GMP... yes
> checking if gmp.h version and libgmp version are the same... (5.0.1/5.0.1) yes
> checking for __gmpn_add_nc... yes
> checking for __gmpn_mod_34lsub1... yes
> checking for __gmpn_redc_1... no
> ...
> configure: Using asm redc code from directory powerpc64
> ...
> }}}
> 
> So it's probably an upstream problem, either MPIR or ECM.
> 
> Or should we pass `-force_cpusubtype_ALL`? (To the assembler?) I think rather not.
> 
> What happens on other PPCs?
> 
> Can you try installing it with GMP 5.0.1?
> 
A remark about installing with GMP 5. On Gentoo I had to apply the following
for it to compile

```
	# fixes for gmp-5
	sed -i "s:__GMP_BITS_PER_MP_LIMB:GMP_LIMB_BITS:g" bestd.c mpmod.c \
		schoen_strass.c sp.h || die "failed to patch files for gmp-5"
```

This is backward compatible with GMP 4.3. I am a bit surprised that with the stuff
that mpir has deprecated, they didn't deprecate that as well.



---

archive/issue_comments_046013.json:
```json
{
    "body": "Replying to [comment:14 leif]:\n> Paul, perhaps you have an idea what's going wrong there (ECM trying to use \"64-bit\" instructions on MacOS X 10.4 PPC [G5], with MPIR 2.1.3).\n\nis this a 32-bit machine? What does ECM config.guess return? Can you try the svn version of\nGMP-ECM using `svn checkout svn://scm.gforge.inria.fr/svn/ecm`?\n\nPaul",
    "created_at": "2010-11-05T08:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46013",
    "user": "zimmerma"
}
```

Replying to [comment:14 leif]:
> Paul, perhaps you have an idea what's going wrong there (ECM trying to use "64-bit" instructions on MacOS X 10.4 PPC [G5], with MPIR 2.1.3).

is this a 32-bit machine? What does ECM config.guess return? Can you try the svn version of
GMP-ECM using `svn checkout svn://scm.gforge.inria.fr/svn/ecm`?

Paul



---

archive/issue_comments_046014.json:
```json
{
    "body": "Replying to [comment:15 leif]:\n> Jeroen, can you try configuring with `--disable-asm-redc`?\n> \n> (The 64-bit PPC asm code is new in 6.3 btw.)\n\nit should work with `--disable-asm-redc`.\n\nPaul",
    "created_at": "2010-11-05T08:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46014",
    "user": "zimmerma"
}
```

Replying to [comment:15 leif]:
> Jeroen, can you try configuring with `--disable-asm-redc`?
> 
> (The 64-bit PPC asm code is new in 6.3 btw.)

it should work with `--disable-asm-redc`.

Paul



---

archive/issue_comments_046015.json:
```json
{
    "body": "Thanks for all the suggestions, I will try them but probably not today.",
    "created_at": "2010-11-05T08:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46015",
    "user": "jdemeyer"
}
```

Thanks for all the suggestions, I will try them but probably not today.



---

archive/issue_comments_046016.json:
```json
{
    "body": "Replying to [comment:16 fbissey]:\n> Replying to [comment:13 leif]:\n> > Can you try installing it with GMP 5.0.1?\n> > \n> A remark about installing with GMP 5. On Gentoo I had to apply the following for it to compile\n\n```\n\t# fixes for gmp-5\n\tsed -i \"s:__GMP_BITS_PER_MP_LIMB:GMP_LIMB_BITS:g\" bestd.c mpmod.c \\\n\t\tschoen_strass.c sp.h || die \"failed to patch files for gmp-5\"\n```\n\n> This is backward compatible with GMP 4.3. I am a bit surprised that with the stuff\n> that mpir has deprecated, they didn't deprecate that as well.\n\nWorked for me *without patching* with both MPIR 2.1.1 and [vanilla] GMP 5.0.1 on Ubuntu ([comment:5 see above]).",
    "created_at": "2010-11-05T12:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46016",
    "user": "leif"
}
```

Replying to [comment:16 fbissey]:
> Replying to [comment:13 leif]:
> > Can you try installing it with GMP 5.0.1?
> > 
> A remark about installing with GMP 5. On Gentoo I had to apply the following for it to compile

```
	# fixes for gmp-5
	sed -i "s:__GMP_BITS_PER_MP_LIMB:GMP_LIMB_BITS:g" bestd.c mpmod.c \
		schoen_strass.c sp.h || die "failed to patch files for gmp-5"
```

> This is backward compatible with GMP 4.3. I am a bit surprised that with the stuff
> that mpir has deprecated, they didn't deprecate that as well.

Worked for me *without patching* with both MPIR 2.1.1 and [vanilla] GMP 5.0.1 on Ubuntu ([comment:5 see above]).



---

archive/issue_comments_046017.json:
```json
{
    "body": "Replying to [comment:18 zimmerma]:\n> Replying to [comment:15 leif]:\n> > Jeroen, can you try configuring with `--disable-asm-redc`?\n> > \n> > (The 64-bit PPC asm code is new in 6.3 btw.)\n> \n> it should work with `--disable-asm-redc`.\n\nThanks!\n\nReplying to [comment:19 jdemeyer]:\n> Thanks for all the suggestions, I will try them but probably not today.\n\nShould I update the spkg / spkg patch to enable `--disable-asm-redc` (on MacOS X PPC 10.4 and perhaps 10.5, or simply PPC)?\n\nIIRC we don't support 64-bit builds (`SAGE64=yes`) on PowerPC (and MacOS X < 10.6) anyway, and Apple doesn't support MacOS X 10.6 on PPCs.\n\nSetting `ABI=32` would perhaps also work.",
    "created_at": "2010-11-05T12:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46017",
    "user": "leif"
}
```

Replying to [comment:18 zimmerma]:
> Replying to [comment:15 leif]:
> > Jeroen, can you try configuring with `--disable-asm-redc`?
> > 
> > (The 64-bit PPC asm code is new in 6.3 btw.)
> 
> it should work with `--disable-asm-redc`.

Thanks!

Replying to [comment:19 jdemeyer]:
> Thanks for all the suggestions, I will try them but probably not today.

Should I update the spkg / spkg patch to enable `--disable-asm-redc` (on MacOS X PPC 10.4 and perhaps 10.5, or simply PPC)?

IIRC we don't support 64-bit builds (`SAGE64=yes`) on PowerPC (and MacOS X < 10.6) anyway, and Apple doesn't support MacOS X 10.6 on PPCs.

Setting `ABI=32` would perhaps also work.



---

archive/issue_comments_046018.json:
```json
{
    "body": "Any objections to enable (also) building a shared library?\n\n(And also enabling the build of a *static* MPIR library, which is better for ECM?)",
    "created_at": "2010-11-05T12:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46018",
    "user": "leif"
}
```

Any objections to enable (also) building a shared library?

(And also enabling the build of a *static* MPIR library, which is better for ECM?)



---

archive/issue_comments_046019.json:
```json
{
    "body": "I wonder how the GNU assembler (Linux PPC) behaves...\n\nFran\u00e7ois, would you like to test this?",
    "created_at": "2010-11-05T13:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46019",
    "user": "leif"
}
```

I wonder how the GNU assembler (Linux PPC) behaves...

François, would you like to test this?



---

archive/issue_comments_046020.json:
```json
{
    "body": "in fact this bug is already fixed upstream (in revision 1516), see\nhttps://gforge.inria.fr/tracker/index.php?func=detail&aid=10646&group_id=135&atid=623\n\nThe patch is the following:\n\n```\n--- configure.in        (revision 1515)\n+++ configure.in        (revision 1516)\n@@ -195,7 +195,7 @@\n # asm_redc enabled by default for x86_64 and 64 bit PowerPC\n if test \"x$enable_asm_redc\" = x; then\n   case $host in\n-    x86_64* | powerpc-apple-darwin* | powerpc64-*-linux*) enable_asm_redc=yes;;\n+    x86_64*-*-* | powerpc-apple-darwin* | powerpc64-*-linux*) enable_asm_redc=yes;;\n     *) enable_asm_redc=no;;\n   esac\n fi\n@@ -203,8 +203,18 @@\n if test \"x$enable_asm_redc\" = xyes; then\n   case $host in\n     pentium4-*-* | pentium3-*-* | viac7-*-* | i786-*-*) ASMPATH=pentium4;;\n-    x86_64-*-*)  ASMPATH=x86_64;; \n-    powerpc-apple-darwin*) ASMPATH=powerpc64;;\n+    x86_64*-*-*)  ASMPATH=x86_64;; \n+# warning: with powerpc-apple-darwin* we can have ABI=32\n+# see bug #10646 on the bug tracker, where config.guess says\n+# powerpc-apple-darwin8.11.0 (this a 64-bit machine, but most applications\n+# are compiled in 32 bits). It works with --disable-asm-redc.\n+    powerpc-apple-darwin*)\n+AC_PREPROC_IFELSE([AC_LANG_PROGRAM([\n+#if defined(__ppc__)\n+#error\n+#endif])], [], [AC_MSG_NOTICE([32-bit PowerPC, disabling asm-redc])\n+                enable_asm_redc=no])\n+                          ASMPATH=powerpc64;;\n     powerpc64-*-linux*)\n                          ECM_INCLUDE([<\"$srcdir\"/powerpc64/powerpc-defs.m4>])\n                          ASMPATH=powerpc64;;\n@@ -213,7 +223,9 @@\n                          ASMPATH=athlon;;\n     *) AC_MSG_ERROR([[asm redc not available on this machine $host]]);;\n   esac\n+fi\n \n+if test \"x$enable_asm_redc\" = xyes; then\n # do the necessary definitions and includes\n   AC_DEFINE([NATIVE_REDC],1,[Define to 1 to use asm redc])\n   test \"x$CCAS\" != x || CCAS=\"$CC -c\"\n```\n\n\nPlease can you check it works correctly with this patch?\n\nPaul",
    "created_at": "2010-11-05T15:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46020",
    "user": "zimmerma"
}
```

in fact this bug is already fixed upstream (in revision 1516), see
https://gforge.inria.fr/tracker/index.php?func=detail&aid=10646&group_id=135&atid=623

The patch is the following:

```
--- configure.in        (revision 1515)
+++ configure.in        (revision 1516)
@@ -195,7 +195,7 @@
 # asm_redc enabled by default for x86_64 and 64 bit PowerPC
 if test "x$enable_asm_redc" = x; then
   case $host in
-    x86_64* | powerpc-apple-darwin* | powerpc64-*-linux*) enable_asm_redc=yes;;
+    x86_64*-*-* | powerpc-apple-darwin* | powerpc64-*-linux*) enable_asm_redc=yes;;
     *) enable_asm_redc=no;;
   esac
 fi
@@ -203,8 +203,18 @@
 if test "x$enable_asm_redc" = xyes; then
   case $host in
     pentium4-*-* | pentium3-*-* | viac7-*-* | i786-*-*) ASMPATH=pentium4;;
-    x86_64-*-*)  ASMPATH=x86_64;; 
-    powerpc-apple-darwin*) ASMPATH=powerpc64;;
+    x86_64*-*-*)  ASMPATH=x86_64;; 
+# warning: with powerpc-apple-darwin* we can have ABI=32
+# see bug #10646 on the bug tracker, where config.guess says
+# powerpc-apple-darwin8.11.0 (this a 64-bit machine, but most applications
+# are compiled in 32 bits). It works with --disable-asm-redc.
+    powerpc-apple-darwin*)
+AC_PREPROC_IFELSE([AC_LANG_PROGRAM([
+#if defined(__ppc__)
+#error
+#endif])], [], [AC_MSG_NOTICE([32-bit PowerPC, disabling asm-redc])
+                enable_asm_redc=no])
+                          ASMPATH=powerpc64;;
     powerpc64-*-linux*)
                          ECM_INCLUDE([<"$srcdir"/powerpc64/powerpc-defs.m4>])
                          ASMPATH=powerpc64;;
@@ -213,7 +223,9 @@
                          ASMPATH=athlon;;
     *) AC_MSG_ERROR([[asm redc not available on this machine $host]]);;
   esac
+fi
 
+if test "x$enable_asm_redc" = xyes; then
 # do the necessary definitions and includes
   AC_DEFINE([NATIVE_REDC],1,[Define to 1 to use asm redc])
   test "x$CCAS" != x || CCAS="$CC -c"
```


Please can you check it works correctly with this patch?

Paul



---

archive/issue_comments_046021.json:
```json
{
    "body": "Replying to [comment:21 leif]:\n\nthe required MPIR spkg does not build on PPC (see my comment on #8664)",
    "created_at": "2010-11-05T17:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46021",
    "user": "dimpase"
}
```

Replying to [comment:21 leif]:

the required MPIR spkg does not build on PPC (see my comment on #8664)



---

archive/issue_comments_046022.json:
```json
{
    "body": "Replying to [comment:15 leif]:\n> Jeroen, can you try configuring with `--disable-asm-redc`?\nThe build (outside of Sage) **works**.\n\nReplying to [comment:17 zimmerma]:\n> is this a 32-bit machine?\nWell, technically the processor is 64-bit capable (I believe) but it runs a 32-bit system and `gcc` produces 32-bit code by default.\n\n> What does ECM config.guess return?\npowerpc-apple-darwin8.11.0\n\nCan you try the svn version of\n> GMP-ECM using `svn checkout svn://scm.gforge.inria.fr/svn/ecm`?\nThis **works**.\n\nReplying to [comment:24 zimmerma]:\n> in fact this bug is already fixed upstream (in revision 1516)\n>\n> Please can you check it works correctly with this patch?\nThis **works**.\n\nReplying to [comment:21 leif]:\n> Setting `ABI=32` would perhaps also work.\nNo, it does **not**.",
    "created_at": "2010-11-05T21:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46022",
    "user": "jdemeyer"
}
```

Replying to [comment:15 leif]:
> Jeroen, can you try configuring with `--disable-asm-redc`?
The build (outside of Sage) **works**.

Replying to [comment:17 zimmerma]:
> is this a 32-bit machine?
Well, technically the processor is 64-bit capable (I believe) but it runs a 32-bit system and `gcc` produces 32-bit code by default.

> What does ECM config.guess return?
powerpc-apple-darwin8.11.0

Can you try the svn version of
> GMP-ECM using `svn checkout svn://scm.gforge.inria.fr/svn/ecm`?
This **works**.

Replying to [comment:24 zimmerma]:
> in fact this bug is already fixed upstream (in revision 1516)
>
> Please can you check it works correctly with this patch?
This **works**.

Replying to [comment:21 leif]:
> Setting `ABI=32` would perhaps also work.
No, it does **not**.



---

archive/issue_comments_046023.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-05T21:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46023",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_046024.json:
```json
{
    "body": "Replying to [comment:26 jdemeyer]:\n> Replying to [comment:15 leif]:\n> > Jeroen, can you try configuring with `--disable-asm-redc`?\n> The build (outside of Sage) **works**.\n\nWell, I'm a bit unsure what to do now. I can of course include the patch, but that does not what we actually want (it's just a work-around).\n\nI think passing `-Wa,-force_cpusubtype_ALL` on MacOS PPCs should also work (which does **not** disable the assembly code, but avoids the odd assembler error, such that we get better performance).\n\nNote that this worked on Dima's **G4** with MPIR, so I expect it to work with a G5, too.\n\nDon't know if G3s run into the same problem, or support these instructions. We then might have to really disable the code on PPCs < G4.\n\nWe could of course just test this in `spkg-install`, i.e. feed some extended instruction set assembly code to the assembler with `-force_cpusubtype_ALL` and see if we get an error before we disable the redc asm code. (I'd have to look what option `gas` takes on *Linux* PPC.)\n\nObjections against adding yet another environment variable (`ECM_EXTRA_OPTS`, to add to ECM's `configure`, analoguous to `PARI_EXTRA_OPTS`), to ease working around potential problems showing up later?",
    "created_at": "2010-11-05T22:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46024",
    "user": "leif"
}
```

Replying to [comment:26 jdemeyer]:
> Replying to [comment:15 leif]:
> > Jeroen, can you try configuring with `--disable-asm-redc`?
> The build (outside of Sage) **works**.

Well, I'm a bit unsure what to do now. I can of course include the patch, but that does not what we actually want (it's just a work-around).

I think passing `-Wa,-force_cpusubtype_ALL` on MacOS PPCs should also work (which does **not** disable the assembly code, but avoids the odd assembler error, such that we get better performance).

Note that this worked on Dima's **G4** with MPIR, so I expect it to work with a G5, too.

Don't know if G3s run into the same problem, or support these instructions. We then might have to really disable the code on PPCs < G4.

We could of course just test this in `spkg-install`, i.e. feed some extended instruction set assembly code to the assembler with `-force_cpusubtype_ALL` and see if we get an error before we disable the redc asm code. (I'd have to look what option `gas` takes on *Linux* PPC.)

Objections against adding yet another environment variable (`ECM_EXTRA_OPTS`, to add to ECM's `configure`, analoguous to `PARI_EXTRA_OPTS`), to ease working around potential problems showing up later?



---

archive/issue_comments_046025.json:
```json
{
    "body": "From my `gas` manpage (relevant for **Linux** PPC only):\n\n```\n...\n       Target PowerPC options:\n          [-mpwrx|-mpwr2|-mpwr|-m601|-mppc|-mppc32|-m603|-m604|\n           -m403|-m405|-mppc64|-m620|-mppc64bridge|-mbooke]\n          [-mcom|-many|-maltivec|-mvsx] [-memb]\n          [-mregnames|-mno-regnames]\n          [-mrelocatable|-mrelocatable-lib]\n          [-mlittle|-mlittle-endian|-mbig|-mbig-endian]\n          [-msolaris|-mno-solaris]\n...\n```\n\nThe options for other architectures in addition have more detailed descriptions, but unfortunately not the ones for PPC as the target. But it seems `gas` enables instruction set extensions by default.\n\n----\n\nP.S.: That the *build* works with `-force_cpusubtype_ALL` (*without* `SAGE_CHECK=yes`) doesn't necessarily mean we couldn't get illegal instruction exceptions when actually *running* the code.",
    "created_at": "2010-11-05T22:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46025",
    "user": "leif"
}
```

From my `gas` manpage (relevant for **Linux** PPC only):

```
...
       Target PowerPC options:
          [-mpwrx|-mpwr2|-mpwr|-m601|-mppc|-mppc32|-m603|-m604|
           -m403|-m405|-mppc64|-m620|-mppc64bridge|-mbooke]
          [-mcom|-many|-maltivec|-mvsx] [-memb]
          [-mregnames|-mno-regnames]
          [-mrelocatable|-mrelocatable-lib]
          [-mlittle|-mlittle-endian|-mbig|-mbig-endian]
          [-msolaris|-mno-solaris]
...
```

The options for other architectures in addition have more detailed descriptions, but unfortunately not the ones for PPC as the target. But it seems `gas` enables instruction set extensions by default.

----

P.S.: That the *build* works with `-force_cpusubtype_ALL` (*without* `SAGE_CHECK=yes`) doesn't necessarily mean we couldn't get illegal instruction exceptions when actually *running* the code.



---

archive/issue_comments_046026.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-11-05T22:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46026",
    "user": "leif"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_046027.json:
```json
{
    "body": "Replying to [comment:23 leif]:\n> I wonder how the GNU assembler (Linux PPC) behaves...\n> \n> Fran\u00e7ois, would you like to test this?\nI know that gmp-ecm-6.3 builds on my linux ppc system but I don't believe\nI have the assembler enabled. I will try that as soon as I have access to the machine\nnext week. I will also have a look at mpir. Note that my test machine is a G4.\n\nI am a bit surprised that no changes where needed to build it against GMP 5.0.1\nI add a bug report specifically on that in Gentoo and I could reproduce it on one\nof my machine which has GMP 5.0.1.",
    "created_at": "2010-11-06T03:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46027",
    "user": "fbissey"
}
```

Replying to [comment:23 leif]:
> I wonder how the GNU assembler (Linux PPC) behaves...
> 
> François, would you like to test this?
I know that gmp-ecm-6.3 builds on my linux ppc system but I don't believe
I have the assembler enabled. I will try that as soon as I have access to the machine
next week. I will also have a look at mpir. Note that my test machine is a G4.

I am a bit surprised that no changes where needed to build it against GMP 5.0.1
I add a bug report specifically on that in Gentoo and I could reproduce it on one
of my machine which has GMP 5.0.1.



---

archive/issue_comments_046028.json:
```json
{
    "body": "Replying to [comment:29 fbissey]:\n> Replying to [comment:23 leif]:\n> > I wonder how the GNU assembler (Linux PPC) behaves...\n> > \n> > Fran\u00e7ois, would you like to test this?\n> I know that gmp-ecm-6.3 builds on my linux ppc system but I don't believe\n> I have the assembler enabled. I will try that as soon as I have access to the machine\n> next week. I will also have a look at mpir. Note that my test machine is a G4.\n\nOk.\n\n> I am a bit surprised that no changes where needed to build it against GMP 5.0.1\n\nHmmm, we have to upgrade ECM *because of* the upgrade of MPIR / GMP:\n  \n ***Changes between ecm-6.2.3 and ecm-6.3:***\n\n* *New assembly code for 64-bit PowerPC (thanks to Philip McLaughlin)*\n* *Allow several processes to write to the same -save file*\n* *More routines in new P+-1 stage 2 use multi-threading in OpenMP build*\n* ***Fixed incompatibility with GMP 5.0.0***\n* *Fixed several bugs, and now check return value from malloc() calls*\n* *Fixed linking of GMP which prevented successful builds under Darwin (and presumably other systems)*\n* *Allow use of x86_64 asm code under MinGW*\n\n\n\n> I add a bug report specifically on that in Gentoo and I could reproduce it on one\n> of my machine which has GMP 5.0.1.",
    "created_at": "2010-11-06T04:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46028",
    "user": "leif"
}
```

Replying to [comment:29 fbissey]:
> Replying to [comment:23 leif]:
> > I wonder how the GNU assembler (Linux PPC) behaves...
> > 
> > François, would you like to test this?
> I know that gmp-ecm-6.3 builds on my linux ppc system but I don't believe
> I have the assembler enabled. I will try that as soon as I have access to the machine
> next week. I will also have a look at mpir. Note that my test machine is a G4.

Ok.

> I am a bit surprised that no changes where needed to build it against GMP 5.0.1

Hmmm, we have to upgrade ECM *because of* the upgrade of MPIR / GMP:
  
 ***Changes between ecm-6.2.3 and ecm-6.3:***

* *New assembly code for 64-bit PowerPC (thanks to Philip McLaughlin)*
* *Allow several processes to write to the same -save file*
* *More routines in new P+-1 stage 2 use multi-threading in OpenMP build*
* ***Fixed incompatibility with GMP 5.0.0***
* *Fixed several bugs, and now check return value from malloc() calls*
* *Fixed linking of GMP which prevented successful builds under Darwin (and presumably other systems)*
* *Allow use of x86_64 asm code under MinGW*



> I add a bug report specifically on that in Gentoo and I could reproduce it on one
> of my machine which has GMP 5.0.1.



---

archive/issue_comments_046029.json:
```json
{
    "body": "Replying to [comment:30 leif]:\n> Replying to [comment:29 fbissey]:\n> > Replying to [comment:23 leif]:\n> > > I wonder how the GNU assembler (Linux PPC) behaves...\n> > > \n> > > Fran\u00e7ois, would you like to test this?\n> > I know that gmp-ecm-6.3 builds on my linux ppc system but I don't believe\n> > I have the assembler enabled. I will try that as soon as I have access to the machine\n> > next week. I will also have a look at mpir. Note that my test machine is a G4.\n> \n> Ok.\n> \n> > I am a bit surprised that no changes where needed to build it against GMP 5.0.1\n> \n> Hmmm, we have to upgrade ECM *because of* the upgrade of MPIR / GMP:\n>   \n>  ***Changes between ecm-6.2.3 and ecm-6.3:***\n> \n>    * *New assembly code for 64-bit PowerPC (thanks to Philip McLaughlin)*\n>    * *Allow several processes to write to the same -save file*\n>    * *More routines in new P+-1 stage 2 use multi-threading in OpenMP build*\n>    * ***Fixed incompatibility with GMP 5.0.0***\n>    * *Fixed several bugs, and now check return value from malloc() calls*\n>    * *Fixed linking of GMP which prevented successful builds under Darwin (and presumably other systems)*\n>    * *Allow use of x86_64 asm code under MinGW*\n> \nI remember adding 6.3 to the sage-on-gentoo tree for GMP-5\n\n```\n# ChangeLog for sci-mathematics/ecm\n# Copyright 1999-2010 Gentoo Foundation; Distributed under the GPL v2\n# $Header: $\n\n  08 Sep 2010; Fran\u00e7ois Bissey <f.r.bissey@massey.ac.nz> metadata.xml:\n  fix metadata\n\n  03 Aug 2010; Christopher Schwan <cschwan@students.uni-mainz.de>\n  -ecm-6.2.3.ebuild, -ecm-6.3.ebuild:\n  Removed old versions\n\n*ecm-6.3-r1 (23 Jul 2010)\n\n  23 Jul 2010; Christopher Schwan <cschwan@students.uni-mainz.de>\n  +ecm-6.3-r1.ebuild:\n  Migrated to autotools-utils.eclass\n\n  08 Jul 2010; Fran\u00e7ois Bissey <f.r.bissey@massey.ac.nz> ecm-6.3.ebuild:\n  Hopefully fixed for gmp-5\n\n*ecm-6.3 (07 Jul 2010)\n\n  07 Jul 2010; Fran\u00e7ois Bissey <f.r.bissey@massey.ac.nz> +ecm-6.3.ebuild:\n  Version bump. Hopefully helpfull with gmp-5.\n```\n\nI'll have to check my inbox for the details. I imported it on the 7th of July\nbecause it said it was compatible with GMP-5 and one of our user was using that.\nThe user then reported that he still couldn't get ECM to build and I introduced the\nfix above the next day which solved the problem.\nA possibility is interference with by a patch to GMP Gentoo side.\n\nOn a positive note ECM 6.3 is the default in sage-on-gentoo since the 3rd of August so it has been extensively tested on x86, amd64 and ppc. However assembler code is at the user's discretion.",
    "created_at": "2010-11-06T05:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46029",
    "user": "fbissey"
}
```

Replying to [comment:30 leif]:
> Replying to [comment:29 fbissey]:
> > Replying to [comment:23 leif]:
> > > I wonder how the GNU assembler (Linux PPC) behaves...
> > > 
> > > François, would you like to test this?
> > I know that gmp-ecm-6.3 builds on my linux ppc system but I don't believe
> > I have the assembler enabled. I will try that as soon as I have access to the machine
> > next week. I will also have a look at mpir. Note that my test machine is a G4.
> 
> Ok.
> 
> > I am a bit surprised that no changes where needed to build it against GMP 5.0.1
> 
> Hmmm, we have to upgrade ECM *because of* the upgrade of MPIR / GMP:
>   
>  ***Changes between ecm-6.2.3 and ecm-6.3:***
> 
>    * *New assembly code for 64-bit PowerPC (thanks to Philip McLaughlin)*
>    * *Allow several processes to write to the same -save file*
>    * *More routines in new P+-1 stage 2 use multi-threading in OpenMP build*
>    * ***Fixed incompatibility with GMP 5.0.0***
>    * *Fixed several bugs, and now check return value from malloc() calls*
>    * *Fixed linking of GMP which prevented successful builds under Darwin (and presumably other systems)*
>    * *Allow use of x86_64 asm code under MinGW*
> 
I remember adding 6.3 to the sage-on-gentoo tree for GMP-5

```
# ChangeLog for sci-mathematics/ecm
# Copyright 1999-2010 Gentoo Foundation; Distributed under the GPL v2
# $Header: $

  08 Sep 2010; François Bissey <f.r.bissey@massey.ac.nz> metadata.xml:
  fix metadata

  03 Aug 2010; Christopher Schwan <cschwan@students.uni-mainz.de>
  -ecm-6.2.3.ebuild, -ecm-6.3.ebuild:
  Removed old versions

*ecm-6.3-r1 (23 Jul 2010)

  23 Jul 2010; Christopher Schwan <cschwan@students.uni-mainz.de>
  +ecm-6.3-r1.ebuild:
  Migrated to autotools-utils.eclass

  08 Jul 2010; François Bissey <f.r.bissey@massey.ac.nz> ecm-6.3.ebuild:
  Hopefully fixed for gmp-5

*ecm-6.3 (07 Jul 2010)

  07 Jul 2010; François Bissey <f.r.bissey@massey.ac.nz> +ecm-6.3.ebuild:
  Version bump. Hopefully helpfull with gmp-5.
```

I'll have to check my inbox for the details. I imported it on the 7th of July
because it said it was compatible with GMP-5 and one of our user was using that.
The user then reported that he still couldn't get ECM to build and I introduced the
fix above the next day which solved the problem.
A possibility is interference with by a patch to GMP Gentoo side.

On a positive note ECM 6.3 is the default in sage-on-gentoo since the 3rd of August so it has been extensively tested on x86, amd64 and ppc. However assembler code is at the user's discretion.



---

archive/issue_comments_046030.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-11-06T14:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46030",
    "user": "dimpase"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_046031.json:
```json
{
    "body": "on MacOSX 10.5 PPC (G4) I get\n\n\n```\nchecking what assembly label suffix to use... :\nchecking if globals are prefixed by underscore... configure: error: Test program links neither with nor without underscore.\nError configuring GMP-ECM.\n```\n\n\n$ gcc -v\n\nUsing built-in specs.\nTarget: powerpc-apple-darwin9\nConfigured with: /var/tmp/gcc_42/gcc_42-5577~1/src/configure --disable-checking --prefix=/usr --mandir=/usr/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/<sup>[cg][</sup>.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin9 --with-gxx-include-dir=/usr/include/c++/4.0.0 --program-prefix= --host=powerpc-apple-darwin9 --target=powerpc-apple-darwin9\nThread model: posix\ngcc version 4.2.1 (Apple Inc. build 5577)",
    "created_at": "2010-11-06T14:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46031",
    "user": "dimpase"
}
```

on MacOSX 10.5 PPC (G4) I get


```
checking what assembly label suffix to use... :
checking if globals are prefixed by underscore... configure: error: Test program links neither with nor without underscore.
Error configuring GMP-ECM.
```


$ gcc -v

Using built-in specs.
Target: powerpc-apple-darwin9
Configured with: /var/tmp/gcc_42/gcc_42-5577~1/src/configure --disable-checking --prefix=/usr --mandir=/usr/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/<sup>[cg][</sup>.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin9 --with-gxx-include-dir=/usr/include/c++/4.0.0 --program-prefix= --host=powerpc-apple-darwin9 --target=powerpc-apple-darwin9
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5577)



---

archive/issue_comments_046032.json:
```json
{
    "body": "Replying to [comment:32 dimpase]:\n> on MacOSX 10.5 PPC (G4) I get\n> \n\n```\nchecking what assembly label suffix to use... :\nchecking if globals are prefixed by underscore... configure: error: Test program links neither with nor without underscore.\nError configuring GMP-ECM.\n```\n\n\nCan you attach the `config.log`?\n\n(Maybe weird `CFLAGS` etc. settings in your environment?)",
    "created_at": "2010-11-06T17:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46032",
    "user": "leif"
}
```

Replying to [comment:32 dimpase]:
> on MacOSX 10.5 PPC (G4) I get
> 

```
checking what assembly label suffix to use... :
checking if globals are prefixed by underscore... configure: error: Test program links neither with nor without underscore.
Error configuring GMP-ECM.
```


Can you attach the `config.log`?

(Maybe weird `CFLAGS` etc. settings in your environment?)



---

archive/issue_comments_046033.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-11-06T17:54:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46033",
    "user": "leif"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_046034.json:
```json
{
    "body": "macosx 10.5 ppc G4 failure of ./configure",
    "created_at": "2010-11-07T04:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46034",
    "user": "dimpase"
}
```

macosx 10.5 ppc G4 failure of ./configure



---

archive/issue_comments_046035.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:33 leif]:\n> Replying to [comment:32 dimpase]:\n> > on MacOSX 10.5 PPC (G4) I get\n> > \n\n```\n checking what assembly label suffix to use... :\n checking if globals are prefixed by underscore... configure: error: Test program links neither with nor without underscore.\n Error configuring GMP-ECM.\n```\n\n \n> Can you attach the `config.log`?\n\ndone\n\n> \n> (Maybe weird `CFLAGS` etc. settings in your environment?)\nno, it's rather prosaic\n\n```\n$ gcc -g conftes1.o conftes2.o \ncollect2: ld terminated with signal 10 [Bus error]\nld warning: can't find atom for stabs FUN at 00000000 in conftes2.o\n```\n",
    "created_at": "2010-11-07T05:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46035",
    "user": "dimpase"
}
```

Attachment

Replying to [comment:33 leif]:
> Replying to [comment:32 dimpase]:
> > on MacOSX 10.5 PPC (G4) I get
> > 

```
 checking what assembly label suffix to use... :
 checking if globals are prefixed by underscore... configure: error: Test program links neither with nor without underscore.
 Error configuring GMP-ECM.
```

 
> Can you attach the `config.log`?

done

> 
> (Maybe weird `CFLAGS` etc. settings in your environment?)
no, it's rather prosaic

```
$ gcc -g conftes1.o conftes2.o 
collect2: ld terminated with signal 10 [Bus error]
ld warning: can't find atom for stabs FUN at 00000000 in conftes2.o
```




---

archive/issue_comments_046036.json:
```json
{
    "body": "Replying to [comment:35 dimpase]:\n\n\n```\n$ gcc -g conftes1.o conftes2.o \ncollect2: ld terminated with signal 10 [Bus error]\nld warning: can't find atom for stabs FUN at 00000000 in conftes2.o\n```\n\n\nmore details - it looks like \"-g\" flag does not work here:\n\n```\n\n$ cat conftes1.c\n#ifdef __cplusplus\nextern \"C\" { void underscore_test(); }\n#endif\nmain () { underscore_test(); }\n$\n$ cat conftes2.s\n      \t.text\n\t.globl _underscore_test\n_underscore_test:\n$\n$ gcc -g -o x conftes1.c conftes2.s\ncollect2: ld terminated with signal 10 [Bus error]\nld warning: can't find atom for stabs FUN at 00000000 in /var/folders/wg/wghOV5z8H7Ox9E0VSGnzm++++TM/-Tmp-//cc5M42pV.o\n$ gcc -o x conftes1.c conftes2.s\n$ ./x\n$ \n```\n\ncould it be due to \"empty\" conftes2.s ?",
    "created_at": "2010-11-07T05:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46036",
    "user": "dimpase"
}
```

Replying to [comment:35 dimpase]:


```
$ gcc -g conftes1.o conftes2.o 
collect2: ld terminated with signal 10 [Bus error]
ld warning: can't find atom for stabs FUN at 00000000 in conftes2.o
```


more details - it looks like "-g" flag does not work here:

```

$ cat conftes1.c
#ifdef __cplusplus
extern "C" { void underscore_test(); }
#endif
main () { underscore_test(); }
$
$ cat conftes2.s
      	.text
	.globl _underscore_test
_underscore_test:
$
$ gcc -g -o x conftes1.c conftes2.s
collect2: ld terminated with signal 10 [Bus error]
ld warning: can't find atom for stabs FUN at 00000000 in /var/folders/wg/wghOV5z8H7Ox9E0VSGnzm++++TM/-Tmp-//cc5M42pV.o
$ gcc -o x conftes1.c conftes2.s
$ ./x
$ 
```

could it be due to "empty" conftes2.s ?



---

archive/issue_comments_046037.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-11-07T06:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46037",
    "user": "dimpase"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_046038.json:
```json
{
    "body": "Replying to [comment:36 dimpase]:\n\n> more details - it looks like \"-g\" flag does not work here:\n\n```\n \n $ cat conftes1.c\n #ifdef __cplusplus\n extern \"C\" { void underscore_test(); }\n #endif\n main () { underscore_test(); }\n $\n $ cat conftes2.s\n       \t.text\n \t.globl _underscore_test\n _underscore_test:\n $\n $ gcc -g -o x conftes1.c conftes2.s\n collect2: ld terminated with signal 10 [Bus error]\nld warning: can't find atom for stabs FUN at 00000000 in /var/folders/wg/wghOV5z8H7Ox9E0VSGnzm++++TM/-Tmp-//cc5M42pV.o\n$ gcc -o x conftes1.c conftes2.s\n$ ./x\n$ \n```\n\n> could it be due to \"empty\" conftes2.s ?\n\nIndeed:\n\n```\n$ cat c2.s\n.text\n.globl _underscore_test\n_underscore_test:\n\tmflr r0\n$ gcc -g -o x conftes1.c c2.s\n$ ./x\n$ gcc -g -O2 -o x conftes1.c c2.s\n$ ./x\n$ gcc -o x conftes1.c c2.s\n$ ./x\n$  \n```\n\n\nSo, one (not me :-( )needs to explain this to the autoconf, I suppose",
    "created_at": "2010-11-07T06:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46038",
    "user": "dimpase"
}
```

Replying to [comment:36 dimpase]:

> more details - it looks like "-g" flag does not work here:

```
 
 $ cat conftes1.c
 #ifdef __cplusplus
 extern "C" { void underscore_test(); }
 #endif
 main () { underscore_test(); }
 $
 $ cat conftes2.s
       	.text
 	.globl _underscore_test
 _underscore_test:
 $
 $ gcc -g -o x conftes1.c conftes2.s
 collect2: ld terminated with signal 10 [Bus error]
ld warning: can't find atom for stabs FUN at 00000000 in /var/folders/wg/wghOV5z8H7Ox9E0VSGnzm++++TM/-Tmp-//cc5M42pV.o
$ gcc -o x conftes1.c conftes2.s
$ ./x
$ 
```

> could it be due to "empty" conftes2.s ?

Indeed:

```
$ cat c2.s
.text
.globl _underscore_test
_underscore_test:
	mflr r0
$ gcc -g -o x conftes1.c c2.s
$ ./x
$ gcc -g -O2 -o x conftes1.c c2.s
$ ./x
$ gcc -o x conftes1.c c2.s
$ ./x
$  
```


So, one (not me :-( )needs to explain this to the autoconf, I suppose



---

archive/issue_comments_046039.json:
```json
{
    "body": "Replying to [comment:37 dimpase]:\n\n> \n> So, one (not me :-( )needs to explain this to the autoconf, I suppose\n\nI went ahead and tweaked configure with the extra asm command in conftes2.s above. It passes, but then I get it misconfigured to ppc64, and then make does not work, as it wants to build ppc64-specific asm code. The following does it better:\n\n```\n$ ./configure --disable-asm-redc\n```\n\nwith this, both make and make check work OK. This is all so far out of Sage tree.\nI'll attach config.log, just in case.",
    "created_at": "2010-11-07T06:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46039",
    "user": "dimpase"
}
```

Replying to [comment:37 dimpase]:

> 
> So, one (not me :-( )needs to explain this to the autoconf, I suppose

I went ahead and tweaked configure with the extra asm command in conftes2.s above. It passes, but then I get it misconfigured to ppc64, and then make does not work, as it wants to build ppc64-specific asm code. The following does it better:

```
$ ./configure --disable-asm-redc
```

with this, both make and make check work OK. This is all so far out of Sage tree.
I'll attach config.log, just in case.



---

archive/issue_comments_046040.json:
```json
{
    "body": "Attachment\n\nmacosx 10.5 ppc G4 with tweaked ./configure --disable-asm-redc (adding extra command in conftes2.s)",
    "created_at": "2010-11-07T06:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46040",
    "user": "dimpase"
}
```

Attachment

macosx 10.5 ppc G4 with tweaked ./configure --disable-asm-redc (adding extra command in conftes2.s)



---

archive/issue_comments_046041.json:
```json
{
    "body": "Replying to [comment:35 dimpase]:\n> no, it's rather prosaic\n> {{{\n> $ gcc -g conftes1.o conftes2.o \n> collect2: ld terminated with signal 10 [Bus error]\n> ld warning: can't find atom for stabs FUN at 00000000 in conftes2.o\n> }}}\n\nPlease do\n$ /usr/libexec/gcc/powerpc-apple-darwin9/4.2.1/ld --version\n$ which ld\n$ ld --version",
    "created_at": "2010-11-07T10:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46041",
    "user": "jdemeyer"
}
```

Replying to [comment:35 dimpase]:
> no, it's rather prosaic
> {{{
> $ gcc -g conftes1.o conftes2.o 
> collect2: ld terminated with signal 10 [Bus error]
> ld warning: can't find atom for stabs FUN at 00000000 in conftes2.o
> }}}

Please do
$ /usr/libexec/gcc/powerpc-apple-darwin9/4.2.1/ld --version
$ which ld
$ ld --version



---

archive/issue_comments_046042.json:
```json
{
    "body": "Again, with proper formatting:\n\n```\n$ /usr/libexec/gcc/powerpc-apple-darwin9/4.2.1/ld --version\n$ which ld\n$ ld --version \n```\n",
    "created_at": "2010-11-07T10:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46042",
    "user": "jdemeyer"
}
```

Again, with proper formatting:

```
$ /usr/libexec/gcc/powerpc-apple-darwin9/4.2.1/ld --version
$ which ld
$ ld --version 
```




---

archive/issue_comments_046043.json:
```json
{
    "body": "[I write here as a developer of GMP-ECM]\n\nthe configure error reported in comment 32 seems to be a ld problem. User \"dimpase\", do you\nmanage to configure GMP successfully?\n\nAlso, which version of GMP-ECM did you use in comment 32? The svn version (see comment 24) should\nfix the fact that 64-bit assembly is used on 32-bit machines. If not, please report the problem\nupstream on http://ecm.gforge.inria.fr/.\n\nPaul Zimmermann",
    "created_at": "2010-11-07T11:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46043",
    "user": "zimmerma"
}
```

[I write here as a developer of GMP-ECM]

the configure error reported in comment 32 seems to be a ld problem. User "dimpase", do you
manage to configure GMP successfully?

Also, which version of GMP-ECM did you use in comment 32? The svn version (see comment 24) should
fix the fact that 64-bit assembly is used on 32-bit machines. If not, please report the problem
upstream on http://ecm.gforge.inria.fr/.

Paul Zimmermann



---

archive/issue_comments_046044.json:
```json
{
    "body": "Replying to [comment:40 jdemeyer]:\n\n```\n$ /usr/libexec/gcc/powerpc-apple-darwin9/4.2.1/ld -v\n@(#)PROGRAM:ld  PROJECT:ld64-85.2.1\n$ ld -v\n@(#)PROGRAM:ld  PROJECT:ld64-85.2.1\n$ which ld\n/usr/bin/ld\n```\n\n\nI think it's the latest ld available under Xcode for ppc.\n(Same for gcc-4.0.1)",
    "created_at": "2010-11-07T12:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46044",
    "user": "dimpase"
}
```

Replying to [comment:40 jdemeyer]:

```
$ /usr/libexec/gcc/powerpc-apple-darwin9/4.2.1/ld -v
@(#)PROGRAM:ld  PROJECT:ld64-85.2.1
$ ld -v
@(#)PROGRAM:ld  PROJECT:ld64-85.2.1
$ which ld
/usr/bin/ld
```


I think it's the latest ld available under Xcode for ppc.
(Same for gcc-4.0.1)



---

archive/issue_comments_046045.json:
```json
{
    "body": "Replying to [comment:41 zimmerma]:\n> [I write here as a developer of GMP-ECM]\n> \n> the configure error reported in comment 32 seems to be a ld problem. User \"dimpase\", do you\n> manage to configure GMP successfully?\n\nYes, I do. MPIR, to be more precise. The version on #8664.\n\n> \n> Also, which version of GMP-ECM did you use in comment 32? \n\nthe one packed in the spkg on this ticket.\n\nSubsequent experiments were made on the same version (without whatever patches in the spkg, however).\n\nI then packaged the configure fix and the extra config flag into Sage spkg and am building Sage using it and\nthe MPIR spkg on  #8664. (it's not done yet, this machine is slooooow...)\n\n\n\n> The svn version (see comment 24) should\n> fix the fact that 64-bit assembly is used on 32-bit machines. If not, please report the problem\n> upstream on http://ecm.gforge.inria.fr/.\n\ndo you want me to test the svn version on this machine?\n\n> \n> Paul Zimmermann\n\nDima Pasechnik",
    "created_at": "2010-11-07T13:03:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46045",
    "user": "dimpase"
}
```

Replying to [comment:41 zimmerma]:
> [I write here as a developer of GMP-ECM]
> 
> the configure error reported in comment 32 seems to be a ld problem. User "dimpase", do you
> manage to configure GMP successfully?

Yes, I do. MPIR, to be more precise. The version on #8664.

> 
> Also, which version of GMP-ECM did you use in comment 32? 

the one packed in the spkg on this ticket.

Subsequent experiments were made on the same version (without whatever patches in the spkg, however).

I then packaged the configure fix and the extra config flag into Sage spkg and am building Sage using it and
the MPIR spkg on  #8664. (it's not done yet, this machine is slooooow...)



> The svn version (see comment 24) should
> fix the fact that 64-bit assembly is used on 32-bit machines. If not, please report the problem
> upstream on http://ecm.gforge.inria.fr/.

do you want me to test the svn version on this machine?

> 
> Paul Zimmermann

Dima Pasechnik



---

archive/issue_comments_046046.json:
```json
{
    "body": "> do you want me to test the svn version on this machine?\n\nyes, as upstream developer I cannot help unless you report a problem with the (vanilla) upstream version.\n\nOf course you are also free to solve the problem within Sage, but if it is not due to the Sage\npackaging, it would be useful to report it upstream.\n\nPaul Zimmermann",
    "created_at": "2010-11-07T16:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46046",
    "user": "zimmerma"
}
```

> do you want me to test the svn version on this machine?

yes, as upstream developer I cannot help unless you report a problem with the (vanilla) upstream version.

Of course you are also free to solve the problem within Sage, but if it is not due to the Sage
packaging, it would be useful to report it upstream.

Paul Zimmermann



---

archive/issue_comments_046047.json:
```json
{
    "body": "Replying to [comment:44 zimmerma]:\n> > do you want me to test the svn version on this machine?\n> \n> yes, as upstream developer I cannot help unless you report a problem with the (vanilla) upstream version.\n\nOK, I got the svn version, cd to trunk, and am stuck:\n\n\n```\n$ autoconf\nconfigure.in:8: error: possibly undefined macro: AM_INIT_AUTOMAKE\n      If this token and others are legitimate, please use m4_pattern_allow.\n      See the Autoconf documentation.\nconfigure.in:81: error: possibly undefined macro: AM_CONDITIONAL\nconfigure.in:155: error: possibly undefined macro: AM_PROG_AS\nconfigure.in:156: error: possibly undefined macro: AM_PROG_CC_C_O\nconfigure.in:185: error: possibly undefined macro: AC_OPENMP\n```\n\n\nAm I doing something wrong, or my autoconf is too old?\n\n\nDima\n\n> \n> Of course you are also free to solve the problem within Sage, but if it is not due to the Sage\n> packaging, it would be useful to report it upstream.\n> \n> Paul Zimmermann",
    "created_at": "2010-11-07T17:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46047",
    "user": "dimpase"
}
```

Replying to [comment:44 zimmerma]:
> > do you want me to test the svn version on this machine?
> 
> yes, as upstream developer I cannot help unless you report a problem with the (vanilla) upstream version.

OK, I got the svn version, cd to trunk, and am stuck:


```
$ autoconf
configure.in:8: error: possibly undefined macro: AM_INIT_AUTOMAKE
      If this token and others are legitimate, please use m4_pattern_allow.
      See the Autoconf documentation.
configure.in:81: error: possibly undefined macro: AM_CONDITIONAL
configure.in:155: error: possibly undefined macro: AM_PROG_AS
configure.in:156: error: possibly undefined macro: AM_PROG_CC_C_O
configure.in:185: error: possibly undefined macro: AC_OPENMP
```


Am I doing something wrong, or my autoconf is too old?


Dima

> 
> Of course you are also free to solve the problem within Sage, but if it is not due to the Sage
> packaging, it would be useful to report it upstream.
> 
> Paul Zimmermann



---

archive/issue_comments_046048.json:
```json
{
    "body": "Replying to [comment:45 dimpase]:\n> {{{\n> $ autoconf\n> configure.in:8: error: possibly undefined macro: AM_INIT_AUTOMAKE\n>       If this token and others are legitimate, please use m4_pattern_allow.\n>       See the Autoconf documentation.\n> configure.in:81: error: possibly undefined macro: AM_CONDITIONAL\n> configure.in:155: error: possibly undefined macro: AM_PROG_AS\n> configure.in:156: error: possibly undefined macro: AM_PROG_CC_C_O\n> configure.in:185: error: possibly undefined macro: AC_OPENMP\n> }}}\n\nTry the following instead:\n\n```\n$ autoreconf -i\n```\n\nIf this doesn't work, please post the output of\n\n```\n$ autoconf --version\n$ automake --version\n```\n",
    "created_at": "2010-11-07T17:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46048",
    "user": "jdemeyer"
}
```

Replying to [comment:45 dimpase]:
> {{{
> $ autoconf
> configure.in:8: error: possibly undefined macro: AM_INIT_AUTOMAKE
>       If this token and others are legitimate, please use m4_pattern_allow.
>       See the Autoconf documentation.
> configure.in:81: error: possibly undefined macro: AM_CONDITIONAL
> configure.in:155: error: possibly undefined macro: AM_PROG_AS
> configure.in:156: error: possibly undefined macro: AM_PROG_CC_C_O
> configure.in:185: error: possibly undefined macro: AC_OPENMP
> }}}

Try the following instead:

```
$ autoreconf -i
```

If this doesn't work, please post the output of

```
$ autoconf --version
$ automake --version
```




---

archive/issue_comments_046049.json:
```json
{
    "body": "you can also try the snapshot from\nhttp://www.loria.fr/~zimmerma/ecm-6.3.1.tar.gz\n(note this is NOT a release).\n\nPaul Zimmermann",
    "created_at": "2010-11-07T17:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46049",
    "user": "zimmerma"
}
```

you can also try the snapshot from
http://www.loria.fr/~zimmerma/ecm-6.3.1.tar.gz
(note this is NOT a release).

Paul Zimmermann



---

archive/issue_comments_046050.json:
```json
{
    "body": "Replying to [comment:45 dimpase]:\n> Replying to [comment:44 zimmerma]:\n> > > do you want me to test the svn version on this machine?\n> > \n> > yes, as upstream developer I cannot help unless you report a problem with the (vanilla) upstream version.\n> \n> OK, I got the svn version, cd to trunk, and am stuck:\n\noops, please ignore this; I should have read README.dev...\n\nDima",
    "created_at": "2010-11-07T17:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46050",
    "user": "dimpase"
}
```

Replying to [comment:45 dimpase]:
> Replying to [comment:44 zimmerma]:
> > > do you want me to test the svn version on this machine?
> > 
> > yes, as upstream developer I cannot help unless you report a problem with the (vanilla) upstream version.
> 
> OK, I got the svn version, cd to trunk, and am stuck:

oops, please ignore this; I should have read README.dev...

Dima



---

archive/issue_comments_046051.json:
```json
{
    "body": "Replying to [comment:47 zimmerma]:\n> you can also try the snapshot from\n> http://www.loria.fr/~zimmerma/ecm-6.3.1.tar.gz\n\nthis one builds (with GMP provided by MPIR) and passes all tests on this computer (macosx 10.5 ppc G4),\nwithout any specific configure flags...\n\n> (note this is NOT a release).\n> \n> Paul Zimmermann\n\nDima",
    "created_at": "2010-11-08T02:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46051",
    "user": "dimpase"
}
```

Replying to [comment:47 zimmerma]:
> you can also try the snapshot from
> http://www.loria.fr/~zimmerma/ecm-6.3.1.tar.gz

this one builds (with GMP provided by MPIR) and passes all tests on this computer (macosx 10.5 ppc G4),
without any specific configure flags...

> (note this is NOT a release).
> 
> Paul Zimmermann

Dima



---

archive/issue_comments_046052.json:
```json
{
    "body": "Replying to [comment:46 jdemeyer]:\n> Try the following instead:\n\nwith current autotools from gnu.org:\n\n\n```\n$ autoreconf -i\nconfigure.in:106: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:106: the top level\nconfigure.in:111: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:111: the top level\nconfigure.in:139: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:139: the top level\nconfigure.in:106: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:106: the top level\nconfigure.in:111: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:111: the top level\nconfigure.in:139: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:139: the top level\nconfigure.in:106: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:106: the top level\nconfigure.in:111: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:111: the top level\nconfigure.in:139: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:139: the top level\nconfigure.in:106: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:106: the top level\nconfigure.in:111: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:111: the top level\nconfigure.in:139: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:139: the top level\nconfigure.in:106: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:106: the top level\nconfigure.in:111: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:111: the top level\nconfigure.in:139: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body\n../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...\nconfigure.in:139: the top level\nconfigure.in:156: installing `./compile'\nconfigure.in:10: installing `./config.guess'\nconfigure.in:10: installing `./config.sub'\nconfigure.in:8: installing `./install-sh'\nconfigure.in:8: installing `./missing'\nathlon/Makefile.am:9: Libtool library used but `LIBTOOL' is undefined\nathlon/Makefile.am:9:   The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'\nathlon/Makefile.am:9:   to `configure.in' and run `aclocal' and `autoconf' again.\nathlon/Makefile.am:9:   If `AC_PROG_LIBTOOL' is in `configure.in', make sure\nathlon/Makefile.am:9:   its definition is in aclocal's search path.\npentium4/Makefile.am:9: Libtool library used but `LIBTOOL' is undefined\npentium4/Makefile.am:9:   The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'\npentium4/Makefile.am:9:   to `configure.in' and run `aclocal' and `autoconf' again.\npentium4/Makefile.am:9:   If `AC_PROG_LIBTOOL' is in `configure.in', make sure\npentium4/Makefile.am:9:   its definition is in aclocal's search path.\npowerpc64/Makefile.am:10: Libtool library used but `LIBTOOL' is undefined\npowerpc64/Makefile.am:10:   The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'\npowerpc64/Makefile.am:10:   to `configure.in' and run `aclocal' and `autoconf' again.\npowerpc64/Makefile.am:10:   If `AC_PROG_LIBTOOL' is in `configure.in', make sure\npowerpc64/Makefile.am:10:   its definition is in aclocal's search path.\nx86_64/Makefile.am:12: Libtool library used but `LIBTOOL' is undefined\nx86_64/Makefile.am:12:   The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'\nx86_64/Makefile.am:12:   to `configure.in' and run `aclocal' and `autoconf' again.\nx86_64/Makefile.am:12:   If `AC_PROG_LIBTOOL' is in `configure.in', make sure\nx86_64/Makefile.am:12:   its definition is in aclocal's search path.\nMakefile.am:8: Libtool library used but `LIBTOOL' is undefined\nMakefile.am:8:   The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'\nMakefile.am:8:   to `configure.in' and run `aclocal' and `autoconf' again.\nMakefile.am:8:   If `AC_PROG_LIBTOOL' is in `configure.in', make sure\nMakefile.am:8:   its definition is in aclocal's search path.\nMakefile.am: installing `./depcomp'\nautoreconf: automake failed with exit status: 1\n$ \n```\n\n\n> If this doesn't work, please post the output of\n\n```\n$ autoconf --version\nautoconf (GNU Autoconf) 2.68\n[...]\nWritten by David J. MacKenzie and Akim Demaille.\n$ automake --version\nautomake (GNU automake) 1.11\n[...]\n```\n\n\n As well:\n \n\n```\n$ aclocal \n$ automake -c -a\n$ autoconf\n$ ./configure\n[...]\nchecking whether gcc and cc understand -c and -o together... yes\n./configure: line 4661: syntax error near unexpected token `2.2.6'\n./configure: line 4661: `LT_PREREQ(2.2.6)'\n```\n\n\nI see exactly the same error as the latter on Debian squeeze x86_64.",
    "created_at": "2010-11-08T04:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46052",
    "user": "dimpase"
}
```

Replying to [comment:46 jdemeyer]:
> Try the following instead:

with current autotools from gnu.org:


```
$ autoreconf -i
configure.in:106: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:106: the top level
configure.in:111: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:111: the top level
configure.in:139: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:139: the top level
configure.in:106: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:106: the top level
configure.in:111: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:111: the top level
configure.in:139: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:139: the top level
configure.in:106: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:106: the top level
configure.in:111: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:111: the top level
configure.in:139: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:139: the top level
configure.in:106: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:106: the top level
configure.in:111: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:111: the top level
configure.in:139: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:139: the top level
configure.in:106: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:106: the top level
configure.in:111: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:111: the top level
configure.in:139: warning: AC_LANG_CONFTEST: no AC_LANG_SOURCE call detected in body
../../lib/autoconf/lang.m4:198: AC_LANG_CONFTEST is expanded from...
configure.in:139: the top level
configure.in:156: installing `./compile'
configure.in:10: installing `./config.guess'
configure.in:10: installing `./config.sub'
configure.in:8: installing `./install-sh'
configure.in:8: installing `./missing'
athlon/Makefile.am:9: Libtool library used but `LIBTOOL' is undefined
athlon/Makefile.am:9:   The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'
athlon/Makefile.am:9:   to `configure.in' and run `aclocal' and `autoconf' again.
athlon/Makefile.am:9:   If `AC_PROG_LIBTOOL' is in `configure.in', make sure
athlon/Makefile.am:9:   its definition is in aclocal's search path.
pentium4/Makefile.am:9: Libtool library used but `LIBTOOL' is undefined
pentium4/Makefile.am:9:   The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'
pentium4/Makefile.am:9:   to `configure.in' and run `aclocal' and `autoconf' again.
pentium4/Makefile.am:9:   If `AC_PROG_LIBTOOL' is in `configure.in', make sure
pentium4/Makefile.am:9:   its definition is in aclocal's search path.
powerpc64/Makefile.am:10: Libtool library used but `LIBTOOL' is undefined
powerpc64/Makefile.am:10:   The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'
powerpc64/Makefile.am:10:   to `configure.in' and run `aclocal' and `autoconf' again.
powerpc64/Makefile.am:10:   If `AC_PROG_LIBTOOL' is in `configure.in', make sure
powerpc64/Makefile.am:10:   its definition is in aclocal's search path.
x86_64/Makefile.am:12: Libtool library used but `LIBTOOL' is undefined
x86_64/Makefile.am:12:   The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'
x86_64/Makefile.am:12:   to `configure.in' and run `aclocal' and `autoconf' again.
x86_64/Makefile.am:12:   If `AC_PROG_LIBTOOL' is in `configure.in', make sure
x86_64/Makefile.am:12:   its definition is in aclocal's search path.
Makefile.am:8: Libtool library used but `LIBTOOL' is undefined
Makefile.am:8:   The usual way to define `LIBTOOL' is to add `AC_PROG_LIBTOOL'
Makefile.am:8:   to `configure.in' and run `aclocal' and `autoconf' again.
Makefile.am:8:   If `AC_PROG_LIBTOOL' is in `configure.in', make sure
Makefile.am:8:   its definition is in aclocal's search path.
Makefile.am: installing `./depcomp'
autoreconf: automake failed with exit status: 1
$ 
```


> If this doesn't work, please post the output of

```
$ autoconf --version
autoconf (GNU Autoconf) 2.68
[...]
Written by David J. MacKenzie and Akim Demaille.
$ automake --version
automake (GNU automake) 1.11
[...]
```


 As well:
 

```
$ aclocal 
$ automake -c -a
$ autoconf
$ ./configure
[...]
checking whether gcc and cc understand -c and -o together... yes
./configure: line 4661: syntax error near unexpected token `2.2.6'
./configure: line 4661: `LT_PREREQ(2.2.6)'
```


I see exactly the same error as the latter on Debian squeeze x86_64.



---

archive/issue_comments_046053.json:
```json
{
    "body": "Replying to [comment:49 dimpase]:\n> Replying to [comment:47 zimmerma]:\n> > you can also try the snapshot from\n> > http://www.loria.fr/~zimmerma/ecm-6.3.1.tar.gz\n> \n> this one builds (with GMP provided by MPIR) and passes all tests on this computer (macosx 10.5 ppc G4),\n> without any specific configure flags...\n\nthis confirms the problem is fixed upstream, and the patch at comment 24 should be enough.\n\nPaul",
    "created_at": "2010-11-08T06:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46053",
    "user": "zimmerma"
}
```

Replying to [comment:49 dimpase]:
> Replying to [comment:47 zimmerma]:
> > you can also try the snapshot from
> > http://www.loria.fr/~zimmerma/ecm-6.3.1.tar.gz
> 
> this one builds (with GMP provided by MPIR) and passes all tests on this computer (macosx 10.5 ppc G4),
> without any specific configure flags...

this confirms the problem is fixed upstream, and the patch at comment 24 should be enough.

Paul



---

archive/issue_comments_046054.json:
```json
{
    "body": "Replying to [comment:27 leif]:\n> Replying to [comment:26 jdemeyer]:\n> > Replying to [comment:15 leif]:\n> > > Jeroen, can you try configuring with `--disable-asm-redc`?\n> > The build (outside of Sage) **works**.\n> \n> Well, I'm a bit unsure what to do now. I can of course include the patch, but that does not what we actually want (it's just a work-around).\n\nWell, since the patch comes from upstream and fixes the problem is all known cases, I think it makes sense to make a new ecm spkg with this patch included.  Leif, what do you think (and could you make the spkg? YES/NO)",
    "created_at": "2010-11-09T10:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46054",
    "user": "jdemeyer"
}
```

Replying to [comment:27 leif]:
> Replying to [comment:26 jdemeyer]:
> > Replying to [comment:15 leif]:
> > > Jeroen, can you try configuring with `--disable-asm-redc`?
> > The build (outside of Sage) **works**.
> 
> Well, I'm a bit unsure what to do now. I can of course include the patch, but that does not what we actually want (it's just a work-around).

Well, since the patch comes from upstream and fixes the problem is all known cases, I think it makes sense to make a new ecm spkg with this patch included.  Leif, what do you think (and could you make the spkg? YES/NO)



---

archive/issue_comments_046055.json:
```json
{
    "body": "Replying to [comment:24 zimmerma]:\n> in fact this bug is already fixed upstream (in revision 1516), see\n> https://gforge.inria.fr/tracker/index.php?func=detail&aid=10646&group_id=135&atid=623\n> \n> The patch is the following:\n> [...]\n>\n> Please can you check it works correctly with this patch?\n>\n\nI wish I could. The patch is against configure.in. But I cannot make autotools work on the package, neither on any local machine, nor on boxen (where autoreconf is version 2.61):\n\n```\ndima@boxen:/tmp/ecm-6.3.p0/src$ autoreconf -i\nRemember to add `AC_PROG_LIBTOOL' to `configure.in'.\nlibtoolize: `config.guess' exists: use `--force' to overwrite\nlibtoolize: `config.sub' exists: use `--force' to overwrite\nlibtoolize: `ltmain.sh' exists: use `--force' to overwrite\nconfigure.in:185: error: possibly undefined macro: AC_OPENMP\n      If this token and others are legitimate, please use m4_pattern_allow.\n      See the Autoconf documentation.\nautoreconf: /usr/bin/autoconf failed with exit status: 1\ndima@boxen:/tmp/ecm-6.3.p0/src$ \n```\n\n sorry...\n \nDima\n\n> Paul",
    "created_at": "2010-11-09T13:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46055",
    "user": "dimpase"
}
```

Replying to [comment:24 zimmerma]:
> in fact this bug is already fixed upstream (in revision 1516), see
> https://gforge.inria.fr/tracker/index.php?func=detail&aid=10646&group_id=135&atid=623
> 
> The patch is the following:
> [...]
>
> Please can you check it works correctly with this patch?
>

I wish I could. The patch is against configure.in. But I cannot make autotools work on the package, neither on any local machine, nor on boxen (where autoreconf is version 2.61):

```
dima@boxen:/tmp/ecm-6.3.p0/src$ autoreconf -i
Remember to add `AC_PROG_LIBTOOL' to `configure.in'.
libtoolize: `config.guess' exists: use `--force' to overwrite
libtoolize: `config.sub' exists: use `--force' to overwrite
libtoolize: `ltmain.sh' exists: use `--force' to overwrite
configure.in:185: error: possibly undefined macro: AC_OPENMP
      If this token and others are legitimate, please use m4_pattern_allow.
      See the Autoconf documentation.
autoreconf: /usr/bin/autoconf failed with exit status: 1
dima@boxen:/tmp/ecm-6.3.p0/src$ 
```

 sorry...
 
Dima

> Paul



---

archive/issue_comments_046056.json:
```json
{
    "body": "New spkg with upstream patch from comment:24: [http://sage.math.washington.edu/home/jdemeyer/spkg/ecm-6.3.p1.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/ecm-6.3.p1.spkg)\n\nI still have to test it properly though.",
    "created_at": "2010-11-10T10:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46056",
    "user": "jdemeyer"
}
```

New spkg with upstream patch from comment:24: [http://sage.math.washington.edu/home/jdemeyer/spkg/ecm-6.3.p1.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/ecm-6.3.p1.spkg)

I still have to test it properly though.



---

archive/issue_comments_046057.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-10T10:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46057",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046058.json:
```json
{
    "body": "patch from p0 to p1, for review",
    "created_at": "2010-11-10T10:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46058",
    "user": "jdemeyer"
}
```

patch from p0 to p1, for review



---

archive/issue_comments_046059.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-11-11T13:14:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46059",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_046060.json:
```json
{
    "body": "Tested new spkg succesfully on the previously-failing OS X 10.4 PPC machine.",
    "created_at": "2010-11-11T13:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46060",
    "user": "jdemeyer"
}
```

Tested new spkg succesfully on the previously-failing OS X 10.4 PPC machine.



---

archive/issue_comments_046061.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-11T14:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46061",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046062.json:
```json
{
    "body": "Replying to [comment:56 jdemeyer]:\n> Tested new spkg succesfully on the previously-failing OS X 10.4 PPC machine.\n\nworks on MacOSX 10.5 PPC. Positive review!",
    "created_at": "2010-11-11T14:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46062",
    "user": "dimpase"
}
```

Replying to [comment:56 jdemeyer]:
> Tested new spkg succesfully on the previously-failing OS X 10.4 PPC machine.

works on MacOSX 10.5 PPC. Positive review!



---

archive/issue_comments_046063.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-11T19:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46063",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_046064.json:
```json
{
    "body": "There is some serious trouble with this spkg: #10252",
    "created_at": "2010-11-12T10:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46064",
    "user": "jdemeyer"
}
```

There is some serious trouble with this spkg: #10252



---

archive/issue_comments_046065.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-11-12T13:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46065",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_046066.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-11-12T13:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46066",
    "user": "jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_046067.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-11-12T13:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46067",
    "user": "jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_046068.json:
```json
{
    "body": "Just for the record:\n\n```sh\n$ hg status \nM .hgignore\nM SPKG.txt\nM spkg-install\nA patches/configure.patch\n```\n\n\nI would still prefer to use the extended instruction set on capable PowerPCs (cf. [this comment above](http://trac.sagemath.org/sage_trac/ticket/5847#comment:27)), regardless if the operating system's ABI is 32 bit or not. (And the `configure` file in `patches/` is huge, as usual, though not under revision control.)",
    "created_at": "2010-11-22T03:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46068",
    "user": "leif"
}
```

Just for the record:

```sh
$ hg status 
M .hgignore
M SPKG.txt
M spkg-install
A patches/configure.patch
```


I would still prefer to use the extended instruction set on capable PowerPCs (cf. [this comment above](http://trac.sagemath.org/sage_trac/ticket/5847#comment:27)), regardless if the operating system's ABI is 32 bit or not. (And the `configure` file in `patches/` is huge, as usual, though not under revision control.)



---

archive/issue_comments_046069.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-24T00:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46069",
    "user": "leif"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046070.json:
```json
{
    "body": "**New spkg: http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg**\n\n**md5sum:** `85eabecaa8974a270d5587ef8de06da1  ecm-6.3.p2.spkg`\n\n----\n\n### ecm-6.3.p2 (Leif Leonhardy, November 23rd, 2010)\n* Apply another patch from upstream to 'configure.in' to fix compilation\n  on 32-bit x86 processors supporting SSE2. (#10252)\n  (There's only a single, cumulative patch file since both patches are to\n  'configure.in'.)\n* Work around linker bug on MacOS X 10.5 PPC (see Special Update/Build\n  Instructions above, and #5847 comment 35 ff.).\n* Allow passing extra arguments to 'configure' through ECM_EXTRA_OPTS.\n* Add \"-march=native\" to CFLAGS on platforms that support it if CFLAGS\n  do not already contain similar.\n* Print settings of CC, CFLAGS etc. and how we configure.\n* Print settings of CC and CFLAGS found in 'SAGE_LOCAL/include/gmp.h'\n  and eventually a system-wide 'gmp.h'; these aren't yet used though.\n* Further clean-up.\n\n----\n\n### Special Update/Build Instructions\n\n* src/ contains \"stable\" upstream code, to which we currently apply\n  two upstream patches (both to 'configure.in'). These (i.e. the\n  files 'patches/configure.in' and 'patches/configure') should be\n  removed on the next upgrade to a stable release.\n* GMP-ECM comes with a self-tuning feature; we could support\n  that as an option ($SAGE_TUNE_*=yes) in the future.\n* We currently work around a linker bug on MacOS X 10.5 PPC (with\n  GCC 4.2.1) which breaks 'configure' if debug symbols are enabled.\n  This *might* get fixed in later upstream releases.\n* ECM currently does not use the CC and CFLAGS settings from 'gmp.h'\n  since we pass (other) options in CFLAGS (though MPIR currently doesn't\n  use its own CFLAGS for the same reason); we could fix that somehow\n  s.t. \"optimized\" code generation options ('-mcpu=...', '-mtune=...')\n  are used by gcc. Of course a user can also manually enable them by\n  setting the \"global\" CFLAGS to e.g. \"-march=native\" on x86 systems.\n  Note that this doesn't affect the packages' selection of processor-\n  specific optimized [assembly] code.\n  'spkg-install' already reads those settings now, but doesn't yet\n  use them.\n  If SAGE_FAT_BINARY=\"yes\", we should avoid too specific settings of\n  \"-mcpu=...\", and perhaps pass a more generic \"--host=...\" to \n  'configure'.\n\n----\n\nPlease build, test and report!\n\n(As you know, it still requires the new MPIR spkg from #8664. Note that I didn't have the same versions of autotools, so the patched `configure` looks quite different and might give warnings, but works, at least for me.)",
    "created_at": "2010-11-24T00:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46070",
    "user": "leif"
}
```

**New spkg: http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg**

**md5sum:** `85eabecaa8974a270d5587ef8de06da1  ecm-6.3.p2.spkg`

----

### ecm-6.3.p2 (Leif Leonhardy, November 23rd, 2010)
* Apply another patch from upstream to 'configure.in' to fix compilation
  on 32-bit x86 processors supporting SSE2. (#10252)
  (There's only a single, cumulative patch file since both patches are to
  'configure.in'.)
* Work around linker bug on MacOS X 10.5 PPC (see Special Update/Build
  Instructions above, and #5847 comment 35 ff.).
* Allow passing extra arguments to 'configure' through ECM_EXTRA_OPTS.
* Add "-march=native" to CFLAGS on platforms that support it if CFLAGS
  do not already contain similar.
* Print settings of CC, CFLAGS etc. and how we configure.
* Print settings of CC and CFLAGS found in 'SAGE_LOCAL/include/gmp.h'
  and eventually a system-wide 'gmp.h'; these aren't yet used though.
* Further clean-up.

----

### Special Update/Build Instructions

* src/ contains "stable" upstream code, to which we currently apply
  two upstream patches (both to 'configure.in'). These (i.e. the
  files 'patches/configure.in' and 'patches/configure') should be
  removed on the next upgrade to a stable release.
* GMP-ECM comes with a self-tuning feature; we could support
  that as an option ($SAGE_TUNE_*=yes) in the future.
* We currently work around a linker bug on MacOS X 10.5 PPC (with
  GCC 4.2.1) which breaks 'configure' if debug symbols are enabled.
  This *might* get fixed in later upstream releases.
* ECM currently does not use the CC and CFLAGS settings from 'gmp.h'
  since we pass (other) options in CFLAGS (though MPIR currently doesn't
  use its own CFLAGS for the same reason); we could fix that somehow
  s.t. "optimized" code generation options ('-mcpu=...', '-mtune=...')
  are used by gcc. Of course a user can also manually enable them by
  setting the "global" CFLAGS to e.g. "-march=native" on x86 systems.
  Note that this doesn't affect the packages' selection of processor-
  specific optimized [assembly] code.
  'spkg-install' already reads those settings now, but doesn't yet
  use them.
  If SAGE_FAT_BINARY="yes", we should avoid too specific settings of
  "-mcpu=...", and perhaps pass a more generic "--host=..." to 
  'configure'.

----

Please build, test and report!

(As you know, it still requires the new MPIR spkg from #8664. Note that I didn't have the same versions of autotools, so the patched `configure` looks quite different and might give warnings, but works, at least for me.)



---

archive/issue_comments_046071.json:
```json
{
    "body": "FWIW, you can also test this package with the old MPIR (1.2.2), or some older GMP. Should work as well.",
    "created_at": "2010-11-24T00:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46071",
    "user": "leif"
}
```

FWIW, you can also test this package with the old MPIR (1.2.2), or some older GMP. Should work as well.



---

archive/issue_comments_046072.json:
```json
{
    "body": "Ooops, I just noticed I've cleaned up a little bit too much (and did *not* enable building also a shared library by default).\n\nAs is, the Sage library won't build with the new package, unless you either install it with\n* `CFLAGS` containing (also) `-fPIC`, or\n* `ECM_EXTRA_OPTS=--enable-shared`.\n\n(Both together also works. So yet another reason we **have to** pass our custom `CFLAGS`.)\n\nI'll update the spkg later, after some feedback I think.",
    "created_at": "2010-11-24T01:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46072",
    "user": "leif"
}
```

Ooops, I just noticed I've cleaned up a little bit too much (and did *not* enable building also a shared library by default).

As is, the Sage library won't build with the new package, unless you either install it with
* `CFLAGS` containing (also) `-fPIC`, or
* `ECM_EXTRA_OPTS=--enable-shared`.

(Both together also works. So yet another reason we **have to** pass our custom `CFLAGS`.)

I'll update the spkg later, after some feedback I think.



---

archive/issue_comments_046073.json:
```json
{
    "body": "Replying to [comment:65 leif]:\n> As is, the Sage library won't build with the new package, unless you either install it with \n\n\n>  * `CFLAGS` containing (also) `-fPIC`, or\n\n\n>  * `ECM_EXTRA_OPTS=--enable-shared`.\n\n\n\nAnother option is to pass `ECM_EXTRA_OPTS=--with-pic`, not sure if this works on all platforms.",
    "created_at": "2010-11-24T02:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46073",
    "user": "leif"
}
```

Replying to [comment:65 leif]:
> As is, the Sage library won't build with the new package, unless you either install it with 


>  * `CFLAGS` containing (also) `-fPIC`, or


>  * `ECM_EXTRA_OPTS=--enable-shared`.



Another option is to pass `ECM_EXTRA_OPTS=--with-pic`, not sure if this works on all platforms.



---

archive/issue_comments_046074.json:
```json
{
    "body": "Just for the record: I'll also update the MPIR spkg s.t. we can get \"tuned\" `CFLAGS` from it (essentially some potentially better / more specific `-march=...` for non-x86 systems).\n\nThe current GMP-ECM spkg uses `-march=native` on x86 / x86_64 systems.",
    "created_at": "2010-11-24T03:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46074",
    "user": "leif"
}
```

Just for the record: I'll also update the MPIR spkg s.t. we can get "tuned" `CFLAGS` from it (essentially some potentially better / more specific `-march=...` for non-x86 systems).

The current GMP-ECM spkg uses `-march=native` on x86 / x86_64 systems.



---

archive/issue_comments_046075.json:
```json
{
    "body": "just a comment: the ticket title mentions ECM 6.3, but the changes in the description refer to\nchanges between 6.2.1 and 6.2.2.\n\nPaul",
    "created_at": "2010-11-24T07:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46075",
    "user": "zimmerma"
}
```

just a comment: the ticket title mentions ECM 6.3, but the changes in the description refer to
changes between 6.2.1 and 6.2.2.

Paul



---

archive/issue_comments_046076.json:
```json
{
    "body": "Leif: why not let ECM use MPIR's CFLAGS?  It seems to me like you're making this package more complicated that it should be.",
    "created_at": "2010-11-24T08:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46076",
    "user": "jdemeyer"
}
```

Leif: why not let ECM use MPIR's CFLAGS?  It seems to me like you're making this package more complicated that it should be.



---

archive/issue_comments_046077.json:
```json
{
    "body": "Sorry, but this will totally break C compilers which do not support `-march=native`:\n\n\n```\n    case \"`uname -m`\" in\n        i[3456]86|i86pc|x86_64|amd64)\n            # Only add it if CFLAGS do not already contain similar:\n            if ! (echo \"$CFLAGS\" | egrep -- '-march=|-mcpu=|-mtune=' >/dev/null);\n            then\n                CFLAGS=\"-march=native $CFLAGS\"\n            fi;;\n    esac\n```\n",
    "created_at": "2010-11-24T08:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46077",
    "user": "jdemeyer"
}
```

Sorry, but this will totally break C compilers which do not support `-march=native`:


```
    case "`uname -m`" in
        i[3456]86|i86pc|x86_64|amd64)
            # Only add it if CFLAGS do not already contain similar:
            if ! (echo "$CFLAGS" | egrep -- '-march=|-mcpu=|-mtune=' >/dev/null);
            then
                CFLAGS="-march=native $CFLAGS"
            fi;;
    esac
```




---

archive/issue_comments_046078.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-24T08:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46078",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_046079.json:
```json
{
    "body": "On sage.math.washington.edu, I get a failure while installing the Sage library (sage-4.6.1.alpha2 + #8664 + #5847):\n\n```\nbuilding 'sage.ext.interpreters.wrapper_el' extension\ngcc -pthread -shared build/temp.linux-x86_64-2.6/sage/libs/libecm.o -L/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local//lib\n-L/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local/lib -lcsage -lecm -lgmp -lstdc++ -lntl -lpython2.6 -o build/lib.linux-x86_64-2.6/sage/libs/libecm.so\n/usr/bin/ld: /mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local//lib/libecm.a(libecm_la-factor.o): relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local//lib/libecm.a: could not read symbols: Bad value\ncollect2: ld returned 1 exit status\n```\n",
    "created_at": "2010-11-24T10:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46079",
    "user": "jdemeyer"
}
```

On sage.math.washington.edu, I get a failure while installing the Sage library (sage-4.6.1.alpha2 + #8664 + #5847):

```
building 'sage.ext.interpreters.wrapper_el' extension
gcc -pthread -shared build/temp.linux-x86_64-2.6/sage/libs/libecm.o -L/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local//lib
-L/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local/lib -lcsage -lecm -lgmp -lstdc++ -lntl -lpython2.6 -o build/lib.linux-x86_64-2.6/sage/libs/libecm.so
/usr/bin/ld: /mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local//lib/libecm.a(libecm_la-factor.o): relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC
/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local//lib/libecm.a: could not read symbols: Bad value
collect2: ld returned 1 exit status
```




---

archive/issue_comments_046080.json:
```json
{
    "body": "Replying to [comment:70 jdemeyer]:\n> Sorry, but this will totally break C compilers which do not support `-march=native`:\n\n```\n    case \"`uname -m`\" in\n        i[3456]86|i86pc|x86_64|amd64)\n            # Only add it if CFLAGS do not already contain similar:\n            if ! (echo \"$CFLAGS\" | egrep -- '-march=|-mcpu=|-mtune=' >/dev/null);\n            then\n                CFLAGS=\"-march=native $CFLAGS\"\n            fi;;\n    esac\n```\n\n\nWell, cite properly:\n\n```sh\n...\nif [ \"$SAGE_FAT_BINARY\" = yes ]; then\n    echo \"Warning: SAGE_FAT_BINARY is currently not really supported by this package.\"\n    # XXX Disable SSE2 on x86? (by passing '--enable-sse2=no' to 'configure')\n    # XXX Disable asm-redc? Or pass some \"generic\" '--host=...' to 'configure'?\nelse\n    # XXX We don't yet test if CC is really gcc here.\n    # gcc's \"-march=native\" only works on some platforms:\n    case \"`uname -m`\" in\n        i[3456]86|i86pc|x86_64|amd64)\n            # Only add it if CFLAGS do not already contain similar:\n            if ! (echo \"$CFLAGS\" | egrep -- '-march=|-mcpu=|-mtune=' >/dev/null);\n            then\n                CFLAGS=\"-march=native $CFLAGS\"\n            fi;;\n    esac\nfi\n...\n```\n\n(There are also notes on this in both the changelog and the *Special Update/Build Instructions*, see above.)\n\nWhat C compilers *does* Sage currently support (and will Sage support in the near future)?\n\nCf. [comment:ticket:10252:20 this comment]:\n   *There's very little support for other compilers in Sage, and it's easy to add a distinction when the day it gets necessary comes, though I could add it now.*\n\n\nBtw, if a user decides or has to set `CC` for some reason (which might even be just to use a different `gcc`), GMP-ECM won't use MPIR's / GMP's `CFLAGS` either. And MPIR isn't omniscient...",
    "created_at": "2010-11-24T10:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46080",
    "user": "leif"
}
```

Replying to [comment:70 jdemeyer]:
> Sorry, but this will totally break C compilers which do not support `-march=native`:

```
    case "`uname -m`" in
        i[3456]86|i86pc|x86_64|amd64)
            # Only add it if CFLAGS do not already contain similar:
            if ! (echo "$CFLAGS" | egrep -- '-march=|-mcpu=|-mtune=' >/dev/null);
            then
                CFLAGS="-march=native $CFLAGS"
            fi;;
    esac
```


Well, cite properly:

```sh
...
if [ "$SAGE_FAT_BINARY" = yes ]; then
    echo "Warning: SAGE_FAT_BINARY is currently not really supported by this package."
    # XXX Disable SSE2 on x86? (by passing '--enable-sse2=no' to 'configure')
    # XXX Disable asm-redc? Or pass some "generic" '--host=...' to 'configure'?
else
    # XXX We don't yet test if CC is really gcc here.
    # gcc's "-march=native" only works on some platforms:
    case "`uname -m`" in
        i[3456]86|i86pc|x86_64|amd64)
            # Only add it if CFLAGS do not already contain similar:
            if ! (echo "$CFLAGS" | egrep -- '-march=|-mcpu=|-mtune=' >/dev/null);
            then
                CFLAGS="-march=native $CFLAGS"
            fi;;
    esac
fi
...
```

(There are also notes on this in both the changelog and the *Special Update/Build Instructions*, see above.)

What C compilers *does* Sage currently support (and will Sage support in the near future)?

Cf. [comment:ticket:10252:20 this comment]:
   *There's very little support for other compilers in Sage, and it's easy to add a distinction when the day it gets necessary comes, though I could add it now.*


Btw, if a user decides or has to set `CC` for some reason (which might even be just to use a different `gcc`), GMP-ECM won't use MPIR's / GMP's `CFLAGS` either. And MPIR isn't omniscient...



---

archive/issue_comments_046081.json:
```json
{
    "body": "Replying to [comment:71 jdemeyer]:\n> On sage.math.washington.edu, I get a failure while installing the Sage library (sage-4.6.1.alpha2 + #8664 + #5847):\n\n```\nbuilding 'sage.ext.interpreters.wrapper_el' extension\ngcc -pthread -shared build/temp.linux-x86_64-2.6/sage/libs/libecm.o -L/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local//lib -L/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local/lib -lcsage -lecm -lgmp -lstdc++ -lntl -lpython2.6 -o build/lib.linux-x86_64-2.6/sage/libs/libecm.so\n/usr/bin/ld: /mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/loca//lib/libecm.a(libecm_la-factor.o): relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local//lib/libecm.a: could not read symbols: Bad value\ncollect2: ld returned 1 exit status\n```\n\n\nDo you read [the comments](http://trac.sagemath.org/sage_trac/ticket/5847#comment:65)?",
    "created_at": "2010-11-24T10:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46081",
    "user": "leif"
}
```

Replying to [comment:71 jdemeyer]:
> On sage.math.washington.edu, I get a failure while installing the Sage library (sage-4.6.1.alpha2 + #8664 + #5847):

```
building 'sage.ext.interpreters.wrapper_el' extension
gcc -pthread -shared build/temp.linux-x86_64-2.6/sage/libs/libecm.o -L/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local//lib -L/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local/lib -lcsage -lecm -lgmp -lstdc++ -lntl -lpython2.6 -o build/lib.linux-x86_64-2.6/sage/libs/libecm.so
/usr/bin/ld: /mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/loca//lib/libecm.a(libecm_la-factor.o): relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC
/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha2-mpir/local//lib/libecm.a: could not read symbols: Bad value
collect2: ld returned 1 exit status
```


Do you read [the comments](http://trac.sagemath.org/sage_trac/ticket/5847#comment:65)?



---

archive/issue_comments_046082.json:
```json
{
    "body": "P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.",
    "created_at": "2010-11-24T10:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46082",
    "user": "leif"
}
```

P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.



---

archive/issue_comments_046083.json:
```json
{
    "body": "Replying to [comment:73 leif]:\n> What C compilers *does* Sage currently support (and will Sage support in the near future)?\n\nOkay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).\n\nAnyway, the proper way to do this is to actually run `gcc -march=native` on some stupid .c file and check whether it compiles (there is no need to actually run the compiled program, so we can compile to `/dev/null`).",
    "created_at": "2010-11-24T10:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46083",
    "user": "jdemeyer"
}
```

Replying to [comment:73 leif]:
> What C compilers *does* Sage currently support (and will Sage support in the near future)?

Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).

Anyway, the proper way to do this is to actually run `gcc -march=native` on some stupid .c file and check whether it compiles (there is no need to actually run the compiled program, so we can compile to `/dev/null`).



---

archive/issue_comments_046084.json:
```json
{
    "body": "Replying to [comment:74 leif]:\n> Do you read [the comments](http://trac.sagemath.org/sage_trac/ticket/5847#comment:65)?\nClearly, I did not...",
    "created_at": "2010-11-24T10:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46084",
    "user": "jdemeyer"
}
```

Replying to [comment:74 leif]:
> Do you read [the comments](http://trac.sagemath.org/sage_trac/ticket/5847#comment:65)?
Clearly, I did not...



---

archive/issue_comments_046085.json:
```json
{
    "body": "Replying to [comment:76 jdemeyer]:\n> Replying to [comment:73 leif]:\n> > What C compilers *does* Sage currently support (and will Sage support in the near future)?\n> \n> Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).\n\nAt least since four years ago, don't know the exact version...\n\n> Anyway, the proper way to do this is to actually run `gcc -march=native` on some stupid .c file and check whether it compiles (there is no need to actually run the compiled program, so we can compile to `/dev/null`).\n\n`gcc -v -march=native` should be sufficient, since the preprocessor also needs to know about it.",
    "created_at": "2010-11-24T11:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46085",
    "user": "leif"
}
```

Replying to [comment:76 jdemeyer]:
> Replying to [comment:73 leif]:
> > What C compilers *does* Sage currently support (and will Sage support in the near future)?
> 
> Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).

At least since four years ago, don't know the exact version...

> Anyway, the proper way to do this is to actually run `gcc -march=native` on some stupid .c file and check whether it compiles (there is no need to actually run the compiled program, so we can compile to `/dev/null`).

`gcc -v -march=native` should be sufficient, since the preprocessor also needs to know about it.



---

archive/issue_comments_046086.json:
```json
{
    "body": "Replying to [comment:78 leif]:\n> Replying to [comment:76 jdemeyer]:\n> > Replying to [comment:73 leif]:\n> > > What C compilers *does* Sage currently support (and will Sage support in the near future)?\n> > \n> > Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).\n> \n> At least since four years ago, don't know the exact version...\n\nGCC 4.0.1 might not support it (could you test that on an x86 machine?); GCC 4.2.1 certainly does.",
    "created_at": "2010-11-24T12:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46086",
    "user": "leif"
}
```

Replying to [comment:78 leif]:
> Replying to [comment:76 jdemeyer]:
> > Replying to [comment:73 leif]:
> > > What C compilers *does* Sage currently support (and will Sage support in the near future)?
> > 
> > Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).
> 
> At least since four years ago, don't know the exact version...

GCC 4.0.1 might not support it (could you test that on an x86 machine?); GCC 4.2.1 certainly does.



---

archive/issue_comments_046087.json:
```json
{
    "body": "Replying to [comment:79 leif]:\n> Replying to [comment:78 leif]:\n> > Replying to [comment:76 jdemeyer]:\n> > > Replying to [comment:73 leif]:\n> > > > What C compilers *does* Sage currently support (and will Sage support in the near future)?\n> > > \n> > > Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).\n> > \n> > At least since four years ago, don't know the exact version...\n> \n> GCC 4.0.1 might not support it (could you test that on an x86 machine?); GCC 4.2.1 certainly does.\n\n... and 4.1.2 also does.",
    "created_at": "2010-11-24T12:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46087",
    "user": "leif"
}
```

Replying to [comment:79 leif]:
> Replying to [comment:78 leif]:
> > Replying to [comment:76 jdemeyer]:
> > > Replying to [comment:73 leif]:
> > > > What C compilers *does* Sage currently support (and will Sage support in the near future)?
> > > 
> > > Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).
> > 
> > At least since four years ago, don't know the exact version...
> 
> GCC 4.0.1 might not support it (could you test that on an x86 machine?); GCC 4.2.1 certainly does.

... and 4.1.2 also does.



---

archive/issue_comments_046088.json:
```json
{
    "body": "Replying to [comment:78 leif]:\n> `gcc -v -march=native` should be sufficient, since the preprocessor also needs to know about it.\n\nNo, that's not sufficient to test it, it does not run the preprocessor.\n\nIf you want to run to preprocessor, the following works:\n\n```\ngcc -march=native -E -x c /dev/null -o /dev/null\n```\n\n\nUsing this test, `-march=native` works for me on gcc 4.2.3, NOT on gcc 4.0.3",
    "created_at": "2010-11-24T13:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46088",
    "user": "jdemeyer"
}
```

Replying to [comment:78 leif]:
> `gcc -v -march=native` should be sufficient, since the preprocessor also needs to know about it.

No, that's not sufficient to test it, it does not run the preprocessor.

If you want to run to preprocessor, the following works:

```
gcc -march=native -E -x c /dev/null -o /dev/null
```


Using this test, `-march=native` works for me on gcc 4.2.3, NOT on gcc 4.0.3



---

archive/issue_comments_046089.json:
```json
{
    "body": "Replying to [comment:81 jdemeyer]:\n> Replying to [comment:78 leif]:\n> > `gcc -v -march=native` should be sufficient, since the preprocessor also needs to know about it.\n> \n> No, that's not sufficient to test it, it does not run the preprocessor.\n> \n> If you want to run to preprocessor, the following works:\n\n```\ngcc -march=native -E -x c /dev/null -o /dev/null\n```\n\n\n`gcc -march=... -dM -E -x c /dev/null` e.g. outputs the definitions of predefined macros like `__i386__`, `__core2__`, `__SSE2__` etc.\n\n\n\n\n> Using this test, `-march=native` works for me on gcc 4.2.3, NOT on gcc 4.0.3\n\nThanks, I use:\n\n```sh\n    if touch foo.c && $CC -march=native -c foo.c &>/dev/null; then\n       ...\n    fi\n    rm -f foo.*\n```\n\n\nFunny: GCC 4.3.3 and 4.4.3 don't build GCC 4.0.1 on Ubuntu 9.04 or 10.04... ;-)",
    "created_at": "2010-11-24T13:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46089",
    "user": "leif"
}
```

Replying to [comment:81 jdemeyer]:
> Replying to [comment:78 leif]:
> > `gcc -v -march=native` should be sufficient, since the preprocessor also needs to know about it.
> 
> No, that's not sufficient to test it, it does not run the preprocessor.
> 
> If you want to run to preprocessor, the following works:

```
gcc -march=native -E -x c /dev/null -o /dev/null
```


`gcc -march=... -dM -E -x c /dev/null` e.g. outputs the definitions of predefined macros like `__i386__`, `__core2__`, `__SSE2__` etc.




> Using this test, `-march=native` works for me on gcc 4.2.3, NOT on gcc 4.0.3

Thanks, I use:

```sh
    if touch foo.c && $CC -march=native -c foo.c &>/dev/null; then
       ...
    fi
    rm -f foo.*
```


Funny: GCC 4.3.3 and 4.4.3 don't build GCC 4.0.1 on Ubuntu 9.04 or 10.04... ;-)



---

archive/issue_comments_046090.json:
```json
{
    "body": "Replying to [comment:82 leif]:\n> Thanks, I use:\n> {{{\n> #!sh\n>     if touch foo.c && $CC -march=native -c foo.c &>/dev/null; then\n>        ...\n>     fi\n>     rm -f foo.*\n> }}}\n\nThat's the best way. I would add `-o /dev/null` so you don't need `rm -f foo.*` but that's a minor point.",
    "created_at": "2010-11-24T14:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46090",
    "user": "jdemeyer"
}
```

Replying to [comment:82 leif]:
> Thanks, I use:
> {{{
> #!sh
>     if touch foo.c && $CC -march=native -c foo.c &>/dev/null; then
>        ...
>     fi
>     rm -f foo.*
> }}}

That's the best way. I would add `-o /dev/null` so you don't need `rm -f foo.*` but that's a minor point.



---

archive/issue_comments_046091.json:
```json
{
    "body": "I'm still thinking that these changes should go to the mpir package and that ecm should use the default `CFLAGS` provided by mpir.",
    "created_at": "2010-11-24T14:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46091",
    "user": "jdemeyer"
}
```

I'm still thinking that these changes should go to the mpir package and that ecm should use the default `CFLAGS` provided by mpir.



---

archive/issue_comments_046092.json:
```json
{
    "body": "Replying to [comment:68 zimmerma]:\n> just a comment: the ticket title mentions ECM 6.3, but the changes in the description refer to\n> changes between 6.2.1 and 6.2.2.\n\nThat's a historical relict; I've now also added the other changes between Sage's current version and 6.3.",
    "created_at": "2010-11-24T17:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46092",
    "user": "leif"
}
```

Replying to [comment:68 zimmerma]:
> just a comment: the ticket title mentions ECM 6.3, but the changes in the description refer to
> changes between 6.2.1 and 6.2.2.

That's a historical relict; I've now also added the other changes between Sage's current version and 6.3.



---

archive/issue_comments_046093.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-25T14:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46093",
    "user": "leif"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046094.json:
```json
{
    "body": "Changing keywords from \"\" to \"MPIR elliptic curves libecm\".",
    "created_at": "2010-11-25T14:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46094",
    "user": "leif"
}
```

Changing keywords from "" to "MPIR elliptic curves libecm".



---

archive/issue_comments_046095.json:
```json
{
    "body": "Replying to [comment:75 leif]:\n> P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.\n\nAlthough (or because) there's not much feedback yet, I've uploaded a corrected spkg (still p2) with also some other changes. This obsoletes setting `ECM_EXTRA_OPTS=--with-pic` or `-fPIC` in `CFLAGS` etc., works with all GCC 4.0.x on x86 as well and also uses processor-specific settings from MPIR if available.\n\n**Updated spkg: http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg** (same place)\n\n**md5sum:** `8246ca74be1ee07b312a84d2a88d9142  ecm-6.3.p2.spkg` (fortunately differs ;-) )\n\n----\n\n### ecm-6.3.p2 (Leif Leonhardy, November 25th, 2010)\n* #5847: Apply another patch from upstream to 'configure.in' to fix com-\n  pilation on 32-bit x86 processors supporting SSE2. (Also #10252.)\n  (There's only a single, cumulative patch file since both patches are to\n  'configure.in'.)\n* Work around linker bug on MacOS X 10.5 PPC (see Special Update/Build\n  Instructions above, and #5847 comment 35 ff.).\n* Allow passing extra arguments to 'configure' through ECM_EXTRA_OPTS.\n* Add \"-march=native\" to CFLAGS on platforms that support it, or use\n  processor-specific CFLAGS from GMP's / MPIR's 'gmp.h' if available,\n  but only if CFLAGS do not already contain similar (i.e., don't over-\n  ride a user's choice). [Subject to further improvement.]\n* Print settings of CC, CFLAGS etc. and how we configure.\n* Print settings of CC and CFLAGS found in 'SAGE_LOCAL/include/gmp.h'\n  and eventually a system-wide 'gmp.h', although the latter aren't (yet)\n  used at all, and only processor-specific parts of the former.\n* Add '-fPIC' conditionally, i.e. not if we're also building a shared\n  library (or '--with-pic' was given).\n* Don't delete previous installations unless the build succeeded.\n* Further clean-up.\n\n\n### Special Update/Build Instructions\n\n [...]\n* ECM currently does not (by itself) use the CC and CFLAGS settings\n  from 'gmp.h' since we pass (other) options in CFLAGS, and CC is set\n  by Sage and might got set by the user (though MPIR currently doesn't\n  use its own CFLAGS for the same reason, which is fixed in an MPIR\n  2.1.3.p2 spkg). We now at least partially fix that s.t. \"optimized\"\n  code generation options ('-mcpu=...', '-mtune=...') are used by gcc.\n  Of course a user can also manually enable them by setting the \"global\"\n  CFLAGS to e.g. '-march=native' on x86[_64] systems, or '-mcpu=...' and\n  '-mtune=...' on other architectures where \"native\" isn't supported.\n  Note that this doesn't affect the packages' selection of processor-\n  specific optimized [assembly] code.\n  'spkg-install' already reads the settings from Sage's and also a\n  system-wide GMP / MPIR now, but doesn't (yet) use all of them.\n  If SAGE_FAT_BINARY=\"yes\", we should avoid too specific settings of\n  \"-mcpu=...\", and perhaps pass a more generic \"--host=...\" to \n  'configure'. (MPIR honors '--enable-fat' to some extent, but this\n  option isn't used on anything other than x86 / x86_64.)\n\n\n----\n\nA new MPIR (2.1.3.p2) spkg which handles `CFLAGS` better (allowing us to use processor-specific settings chosen by MPIR) is on the way, but will live on another ticket (not #8664). Just haven't committed the changes yet.",
    "created_at": "2010-11-25T14:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46095",
    "user": "leif"
}
```

Replying to [comment:75 leif]:
> P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.

Although (or because) there's not much feedback yet, I've uploaded a corrected spkg (still p2) with also some other changes. This obsoletes setting `ECM_EXTRA_OPTS=--with-pic` or `-fPIC` in `CFLAGS` etc., works with all GCC 4.0.x on x86 as well and also uses processor-specific settings from MPIR if available.

**Updated spkg: http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg** (same place)

**md5sum:** `8246ca74be1ee07b312a84d2a88d9142  ecm-6.3.p2.spkg` (fortunately differs ;-) )

----

### ecm-6.3.p2 (Leif Leonhardy, November 25th, 2010)
* #5847: Apply another patch from upstream to 'configure.in' to fix com-
  pilation on 32-bit x86 processors supporting SSE2. (Also #10252.)
  (There's only a single, cumulative patch file since both patches are to
  'configure.in'.)
* Work around linker bug on MacOS X 10.5 PPC (see Special Update/Build
  Instructions above, and #5847 comment 35 ff.).
* Allow passing extra arguments to 'configure' through ECM_EXTRA_OPTS.
* Add "-march=native" to CFLAGS on platforms that support it, or use
  processor-specific CFLAGS from GMP's / MPIR's 'gmp.h' if available,
  but only if CFLAGS do not already contain similar (i.e., don't over-
  ride a user's choice). [Subject to further improvement.]
* Print settings of CC, CFLAGS etc. and how we configure.
* Print settings of CC and CFLAGS found in 'SAGE_LOCAL/include/gmp.h'
  and eventually a system-wide 'gmp.h', although the latter aren't (yet)
  used at all, and only processor-specific parts of the former.
* Add '-fPIC' conditionally, i.e. not if we're also building a shared
  library (or '--with-pic' was given).
* Don't delete previous installations unless the build succeeded.
* Further clean-up.


### Special Update/Build Instructions

 [...]
* ECM currently does not (by itself) use the CC and CFLAGS settings
  from 'gmp.h' since we pass (other) options in CFLAGS, and CC is set
  by Sage and might got set by the user (though MPIR currently doesn't
  use its own CFLAGS for the same reason, which is fixed in an MPIR
  2.1.3.p2 spkg). We now at least partially fix that s.t. "optimized"
  code generation options ('-mcpu=...', '-mtune=...') are used by gcc.
  Of course a user can also manually enable them by setting the "global"
  CFLAGS to e.g. '-march=native' on x86[_64] systems, or '-mcpu=...' and
  '-mtune=...' on other architectures where "native" isn't supported.
  Note that this doesn't affect the packages' selection of processor-
  specific optimized [assembly] code.
  'spkg-install' already reads the settings from Sage's and also a
  system-wide GMP / MPIR now, but doesn't (yet) use all of them.
  If SAGE_FAT_BINARY="yes", we should avoid too specific settings of
  "-mcpu=...", and perhaps pass a more generic "--host=..." to 
  'configure'. (MPIR honors '--enable-fat' to some extent, but this
  option isn't used on anything other than x86 / x86_64.)


----

A new MPIR (2.1.3.p2) spkg which handles `CFLAGS` better (allowing us to use processor-specific settings chosen by MPIR) is on the way, but will live on another ticket (not #8664). Just haven't committed the changes yet.



---

archive/issue_comments_046096.json:
```json
{
    "body": "Attachment\n\nDiff between the p1 and the p2 spkg. For reference / review.",
    "created_at": "2010-11-25T14:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46096",
    "user": "leif"
}
```

Attachment

Diff between the p1 and the p2 spkg. For reference / review.



---

archive/issue_comments_046097.json:
```json
{
    "body": "Attachment\n\nMercurial patch to get the p2 from the p1 spkg. Except for the commit messages perhaps less readable. (6 changesets.)",
    "created_at": "2010-11-25T15:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46097",
    "user": "leif"
}
```

Attachment

Mercurial patch to get the p2 from the p1 spkg. Except for the commit messages perhaps less readable. (6 changesets.)



---

archive/issue_comments_046098.json:
```json
{
    "body": "Replying to [comment:86 leif]:\n> Replying to [comment:75 leif]:\n> > P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.\n\nbuilts OK on OSX 10.5 PPC, with SAGE_CHECK=yes",
    "created_at": "2010-11-25T16:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46098",
    "user": "dimpase"
}
```

Replying to [comment:86 leif]:
> Replying to [comment:75 leif]:
> > P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.

builts OK on OSX 10.5 PPC, with SAGE_CHECK=yes



---

archive/issue_comments_046099.json:
```json
{
    "body": "Replying to [comment:87 dimpase]:\n> Replying to [comment:86 leif]:\n> > Replying to [comment:75 leif]:\n> > > P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.\n> \n> builts OK on OSX 10.5 PPC, with SAGE_CHECK=yes\n> \n\nHappy to hear that. I wonder what happens on other MacOS X versions with GCC 4.2.1 (regarding the linker bus error in `configure` when `-g` was given to `gcc`).",
    "created_at": "2010-11-25T16:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46099",
    "user": "leif"
}
```

Replying to [comment:87 dimpase]:
> Replying to [comment:86 leif]:
> > Replying to [comment:75 leif]:
> > > P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.
> 
> builts OK on OSX 10.5 PPC, with SAGE_CHECK=yes
> 

Happy to hear that. I wonder what happens on other MacOS X versions with GCC 4.2.1 (regarding the linker bus error in `configure` when `-g` was given to `gcc`).



---

archive/issue_comments_046100.json:
```json
{
    "body": "Changing keywords from \"MPIR elliptic curves libecm\" to \"MPIR elliptic curves libecm ecm spkg\".",
    "created_at": "2010-11-26T08:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46100",
    "user": "jdemeyer"
}
```

Changing keywords from "MPIR elliptic curves libecm" to "MPIR elliptic curves libecm ecm spkg".



---

archive/issue_comments_046101.json:
```json
{
    "body": "Replying to [comment:89 jdemeyer]:\n> **Testing distribution** with new mpir (#8664) and new ecm: http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.1.alpha2-mpir/sage-4.6.1.alpha2-mpir.tar\n\nThanks.",
    "created_at": "2010-11-26T08:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46101",
    "user": "leif"
}
```

Replying to [comment:89 jdemeyer]:
> **Testing distribution** with new mpir (#8664) and new ecm: http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.1.alpha2-mpir/sage-4.6.1.alpha2-mpir.tar

Thanks.



---

archive/issue_comments_046102.json:
```json
{
    "body": "Tested successfully on\n* sage.math.washington.edu\n* OS X 10.4 PPC\n* 32-bit Gentoo Linux Pentium 4",
    "created_at": "2010-11-28T15:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46102",
    "user": "jdemeyer"
}
```

Tested successfully on
* sage.math.washington.edu
* OS X 10.4 PPC
* 32-bit Gentoo Linux Pentium 4



---

archive/issue_comments_046103.json:
```json
{
    "body": "`SAGE_FAT_BINARY` is unsupported in this package, but to compond the problem, the compiler option\n\n\n```\n-march=native\n```\n\n\nis added. That's just asking for trouble for distributing binaries.",
    "created_at": "2011-05-09T21:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46103",
    "user": "drkirkby"
}
```

`SAGE_FAT_BINARY` is unsupported in this package, but to compond the problem, the compiler option


```
-march=native
```


is added. That's just asking for trouble for distributing binaries.



---

archive/issue_comments_046104.json:
```json
{
    "body": "SAGE_FAT_BINARY needs to be supported.",
    "created_at": "2011-05-12T15:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46104",
    "user": "mariah"
}
```

SAGE_FAT_BINARY needs to be supported.



---

archive/issue_comments_046105.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-05-12T15:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46105",
    "user": "mariah"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_046106.json:
```json
{
    "body": "Replying to [comment:93 drkirkby]:\n> `SAGE_FAT_BINARY` is unsupported in this package, but to compond the problem, the compiler option\n> \n\n```\n-march=native\n```\n\n> \n> is added.\n\n\n\nWell, apparently `SAGE_FAT_BINARY` has *never been* supported by the ECM spkg.\n\nAnd no, `-march=native` isn't added by `spkg-install` in case `SAGE_FAT_BINARY=yes`:\n\n```sh\nif [ \"$SAGE_FAT_BINARY\" = yes ]; then\n    # XXX Disable SSE2 on x86? (by passing '--enable-sse2=no' to 'configure')\n    # XXX Disable asm-redc? Or pass some \"generic\" '--host=...' to 'configure'?\n    echo \"Warning: SAGE_FAT_BINARY is currently not really supported by this package.\"\n    echo \"         Add e.g. '--disable-asm-redc' and/or '--enable-sse2=no'\"\n    echo \"         to ECM_EXTRA_OPTS if you run into problems.\"\nelse\n    # Tune the code generation to the machine we build on:\n\n    ...\nfi\n```\n\n(Note that some 'optimized' parameters may come from `gmp.h` anyway, but these aren't used either if `SAGE_FAT_BINARY=yes`.)\n\nWe had some discussion on that before, and Paul said they're considering adding a `--enable-fat` switch to ECM's `configure` IIRC. There are also a few comments in ECM's `SPKG.txt`.",
    "created_at": "2011-05-15T08:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46106",
    "user": "leif"
}
```

Replying to [comment:93 drkirkby]:
> `SAGE_FAT_BINARY` is unsupported in this package, but to compond the problem, the compiler option
> 

```
-march=native
```

> 
> is added.



Well, apparently `SAGE_FAT_BINARY` has *never been* supported by the ECM spkg.

And no, `-march=native` isn't added by `spkg-install` in case `SAGE_FAT_BINARY=yes`:

```sh
if [ "$SAGE_FAT_BINARY" = yes ]; then
    # XXX Disable SSE2 on x86? (by passing '--enable-sse2=no' to 'configure')
    # XXX Disable asm-redc? Or pass some "generic" '--host=...' to 'configure'?
    echo "Warning: SAGE_FAT_BINARY is currently not really supported by this package."
    echo "         Add e.g. '--disable-asm-redc' and/or '--enable-sse2=no'"
    echo "         to ECM_EXTRA_OPTS if you run into problems."
else
    # Tune the code generation to the machine we build on:

    ...
fi
```

(Note that some 'optimized' parameters may come from `gmp.h` anyway, but these aren't used either if `SAGE_FAT_BINARY=yes`.)

We had some discussion on that before, and Paul said they're considering adding a `--enable-fat` switch to ECM's `configure` IIRC. There are also a few comments in ECM's `SPKG.txt`.



---

archive/issue_comments_046107.json:
```json
{
    "body": "Replying to [comment:94 mariah]:\n> SAGE_FAT_BINARY needs to be supported.\n\n\n\nIn which way / to what extent?\n\n(See my previous post.)",
    "created_at": "2011-05-15T08:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46107",
    "user": "leif"
}
```

Replying to [comment:94 mariah]:
> SAGE_FAT_BINARY needs to be supported.



In which way / to what extent?

(See my previous post.)



---

archive/issue_comments_046108.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-05-15T08:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46108",
    "user": "leif"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_046109.json:
```json
{
    "body": "Replying to [comment:96 leif]:\n> Replying to [comment:94 mariah]:\n> > SAGE_FAT_BINARY needs to be supported.\n> \n\n> \n> In which way / to what extent?\n> \n> (See my previous post.)\n\nIf I build a SAGE_FAT_BINARY version of sage on one of the skynet x86_64 machines, then move that build to another skynet x86_64 machine, then all the tests should pass.  That is my understanding of what SAGE_FAT_BINARY should accomplish.\n\nIn spite of ecm not explicitly recognizing SAGE_FAT_BINARY, when\nI have built SAGE_FAT_BINARY versions of previous versions of sage (for example 4.6.2), I have not run into any problems.  (Perhaps\nI have just been lucky.)\n\nDoes this spkg maintain this SAGE_FAT_BINARY functionality?",
    "created_at": "2011-05-16T16:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46109",
    "user": "mariah"
}
```

Replying to [comment:96 leif]:
> Replying to [comment:94 mariah]:
> > SAGE_FAT_BINARY needs to be supported.
> 

> 
> In which way / to what extent?
> 
> (See my previous post.)

If I build a SAGE_FAT_BINARY version of sage on one of the skynet x86_64 machines, then move that build to another skynet x86_64 machine, then all the tests should pass.  That is my understanding of what SAGE_FAT_BINARY should accomplish.

In spite of ecm not explicitly recognizing SAGE_FAT_BINARY, when
I have built SAGE_FAT_BINARY versions of previous versions of sage (for example 4.6.2), I have not run into any problems.  (Perhaps
I have just been lucky.)

Does this spkg maintain this SAGE_FAT_BINARY functionality?



---

archive/issue_comments_046110.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-05-16T16:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46110",
    "user": "mariah"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_046111.json:
```json
{
    "body": "sage-4.7.1-alpha1 built with http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg on skynet/flavius (x86_64-Linux-k8-fc) fails test:\n\n\n```\nflavius% ./sage -t -long -force_lib \"devel/sage/sage/libs/libecm.pyx\"\nsage -t -long -force_lib \"devel/sage/sage/libs/libecm.pyx\"  \n**********************************************************************\nFile \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/devel/sage/sage/libs/libecm.pyx\", line 14:\n    sage: import sage.libs.libecm\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[2]>\", line 1, in <module>\n        import sage.libs.libecm###line 14:\n    sage: import sage.libs.libecm\n    ImportError: /home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/local/lib/python/site-packages/sage/libs/libecm.so: cannot enable executable stack as shared object requires: Permission denied\n**********************************************************************\n```\n\n\nLooking at the build I see\n\n\n```\nCopying patched files...\nAdding '-fPIC' to CFLAGS since we don't (also) build a shared library.\nUsing additional host-specific CFLAGS: -march=native\n\nSettings from SAGE_LOCAL/include/gmp.h:\n    CC=gcc \n    CFLAGS=-O2 -m64 -march=k8 -mtune=k8 \nUsing CC=gcc\nUsing CFLAGS=-march=native -g -O3  -fPIC\nUsing CPPFLAGS=\nUsing LDFLAGS=\nUsing ABI=\n(These settings may get overridden by 'configure' or Makefiles.)\n```\n\n\n**Strongly** suggest ecm be built with same CFLAGS values as gmp/mpir as recommended by ecm INSTALL file.",
    "created_at": "2011-06-02T14:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46111",
    "user": "mariah"
}
```

sage-4.7.1-alpha1 built with http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg on skynet/flavius (x86_64-Linux-k8-fc) fails test:


```
flavius% ./sage -t -long -force_lib "devel/sage/sage/libs/libecm.pyx"
sage -t -long -force_lib "devel/sage/sage/libs/libecm.pyx"  
**********************************************************************
File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/devel/sage/sage/libs/libecm.pyx", line 14:
    sage: import sage.libs.libecm
Exception raised:
    Traceback (most recent call last):
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        import sage.libs.libecm###line 14:
    sage: import sage.libs.libecm
    ImportError: /home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/local/lib/python/site-packages/sage/libs/libecm.so: cannot enable executable stack as shared object requires: Permission denied
**********************************************************************
```


Looking at the build I see


```
Copying patched files...
Adding '-fPIC' to CFLAGS since we don't (also) build a shared library.
Using additional host-specific CFLAGS: -march=native

Settings from SAGE_LOCAL/include/gmp.h:
    CC=gcc 
    CFLAGS=-O2 -m64 -march=k8 -mtune=k8 
Using CC=gcc
Using CFLAGS=-march=native -g -O3  -fPIC
Using CPPFLAGS=
Using LDFLAGS=
Using ABI=
(These settings may get overridden by 'configure' or Makefiles.)
```


**Strongly** suggest ecm be built with same CFLAGS values as gmp/mpir as recommended by ecm INSTALL file.



---

archive/issue_comments_046112.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-02T14:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46112",
    "user": "mariah"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_046113.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-06-02T15:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46113",
    "user": "leif"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_046114.json:
```json
{
    "body": "Replying to [comment:98 mariah]:\n> sage-4.7.1-alpha1 built with http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg on skynet/flavius (x86_64-Linux-k8-fc) fails test:\n\n```\n...\n    ImportError: /home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/local/lib/python/site-packages/sage/libs/libecm.so: cannot enable executable stack as shared object requires: Permission denied\n```\n\n> \n> Looking at the build I see\n> \n\n```\n...\nAdding '-fPIC' to CFLAGS since we don't (also) build a shared library.\n...\nSettings from SAGE_LOCAL/include/gmp.h:\n    CC=gcc \n    CFLAGS=-O2 -m64 -march=k8 -mtune=k8 \nUsing CC=gcc\nUsing CFLAGS=-march=native -g -O3  -fPIC\nUsing CPPFLAGS=\nUsing LDFLAGS=\n...\n```\n\n> \n> **Strongly** suggest ecm be built with same CFLAGS values as gmp/mpir as recommended by ecm INSTALL file.\n\n\n\nHi Mariah,\n\nthis failure is rather unrelated to the GMP-ECM package itself (since we only build a static library, see above), but a \"common\" Fedora (>=14 / SELinux) / GCC problem; cf. e.g. #10188.\n\nThe `libecm.so` extension module -- which erroneously carries the \"executable stack\" flag -- is built by Cython from `libecm.pyx`.\n\nCould you please first try\n\n```sh\n$ execstack -c local/lib/python/site-packages/sage/libs/libecm.so\n```\n\nand rerun the test?\n\n(Taking the flags from MPIR / `gmp.h` wouldn't help anyway in this case.)\n\n----\n\nIf the above works, you could then patch `module_list.py`:\n\n```diff\ndiff --git a/module_list.py b/module_list.py\n--- a/module_list.py\n+++ b/module_list.py\n@@ -561,6 +561,7 @@\n     Extension('sage.libs.libecm',\n               sources = ['sage/libs/libecm.pyx'],\n               libraries = ['ecm', 'gmp'],\n+              extra_compile_args=[\"-Wl,-z,noexecstack\"],\n               depends = [SAGE_ROOT + \"/local/include/ecm.h\"]),\n      \n     Extension('sage.libs.mwrank.mwrank',\n```\n\nThen you probably have to touch `libecm.pyx` in order to convince Cython to rebuild the module before issuing `./sage -b`. Afterwards the tests should pass without the need to rerun `execstack`. (You can check the flag's setting by running `execstack -q ...`.)\n\nLet me know if the above works and/or if you need a Mercurial patch for that... ;-)\n\n(Just curious: Which GCC version are you using now? The problem may or should have arised with earlier version of Sage on Fedora, too.)",
    "created_at": "2011-06-02T15:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46114",
    "user": "leif"
}
```

Replying to [comment:98 mariah]:
> sage-4.7.1-alpha1 built with http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg on skynet/flavius (x86_64-Linux-k8-fc) fails test:

```
...
    ImportError: /home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-k8-fc-review-5847/local/lib/python/site-packages/sage/libs/libecm.so: cannot enable executable stack as shared object requires: Permission denied
```

> 
> Looking at the build I see
> 

```
...
Adding '-fPIC' to CFLAGS since we don't (also) build a shared library.
...
Settings from SAGE_LOCAL/include/gmp.h:
    CC=gcc 
    CFLAGS=-O2 -m64 -march=k8 -mtune=k8 
Using CC=gcc
Using CFLAGS=-march=native -g -O3  -fPIC
Using CPPFLAGS=
Using LDFLAGS=
...
```

> 
> **Strongly** suggest ecm be built with same CFLAGS values as gmp/mpir as recommended by ecm INSTALL file.



Hi Mariah,

this failure is rather unrelated to the GMP-ECM package itself (since we only build a static library, see above), but a "common" Fedora (>=14 / SELinux) / GCC problem; cf. e.g. #10188.

The `libecm.so` extension module -- which erroneously carries the "executable stack" flag -- is built by Cython from `libecm.pyx`.

Could you please first try

```sh
$ execstack -c local/lib/python/site-packages/sage/libs/libecm.so
```

and rerun the test?

(Taking the flags from MPIR / `gmp.h` wouldn't help anyway in this case.)

----

If the above works, you could then patch `module_list.py`:

```diff
diff --git a/module_list.py b/module_list.py
--- a/module_list.py
+++ b/module_list.py
@@ -561,6 +561,7 @@
     Extension('sage.libs.libecm',
               sources = ['sage/libs/libecm.pyx'],
               libraries = ['ecm', 'gmp'],
+              extra_compile_args=["-Wl,-z,noexecstack"],
               depends = [SAGE_ROOT + "/local/include/ecm.h"]),
      
     Extension('sage.libs.mwrank.mwrank',
```

Then you probably have to touch `libecm.pyx` in order to convince Cython to rebuild the module before issuing `./sage -b`. Afterwards the tests should pass without the need to rerun `execstack`. (You can check the flag's setting by running `execstack -q ...`.)

Let me know if the above works and/or if you need a Mercurial patch for that... ;-)

(Just curious: Which GCC version are you using now? The problem may or should have arised with earlier version of Sage on Fedora, too.)



---

archive/issue_comments_046115.json:
```json
{
    "body": "**Disclaimer for Dave:**\n\nThe patch above is a bit hackish. We should either pass the additional compiler flag *conditionally* (on Linux systems only, where we can rely on a GNU linker), or perhaps instead use GCC's `--noexecstack` parameter, of which I currently don't know whether it is supported by ancient versions of GCC.",
    "created_at": "2011-06-02T16:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46115",
    "user": "leif"
}
```

**Disclaimer for Dave:**

The patch above is a bit hackish. We should either pass the additional compiler flag *conditionally* (on Linux systems only, where we can rely on a GNU linker), or perhaps instead use GCC's `--noexecstack` parameter, of which I currently don't know whether it is supported by ancient versions of GCC.



---

archive/issue_comments_046116.json:
```json
{
    "body": "Hmmm, apparently the patch should read:\n\n```diff\ndiff --git a/module_list.py b/module_list.py\n--- a/module_list.py\n+++ b/module_list.py\n@@ -561,6 +561,7 @@\n     Extension('sage.libs.libecm',\n               sources = ['sage/libs/libecm.pyx'],\n               libraries = ['ecm', 'gmp'],\n+              extra_link_args=[\"-Wl,-z,noexecstack\"],\n               depends = [SAGE_ROOT + \"/local/include/ecm.h\"]),\n      \n     Extension('sage.libs.mwrank.mwrank',\n```\n\n(Still hackish though.)",
    "created_at": "2011-06-02T16:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46116",
    "user": "leif"
}
```

Hmmm, apparently the patch should read:

```diff
diff --git a/module_list.py b/module_list.py
--- a/module_list.py
+++ b/module_list.py
@@ -561,6 +561,7 @@
     Extension('sage.libs.libecm',
               sources = ['sage/libs/libecm.pyx'],
               libraries = ['ecm', 'gmp'],
+              extra_link_args=["-Wl,-z,noexecstack"],
               depends = [SAGE_ROOT + "/local/include/ecm.h"]),
      
     Extension('sage.libs.mwrank.mwrank',
```

(Still hackish though.)



---

archive/issue_comments_046117.json:
```json
{
    "body": "On skynet/flavius I get\n\n\n```\nflavius% execstack -c local/lib/python/site-packages/sage/libs/libecm.so\nexecstack: Could not set security context for local/lib/python/site-packages/sage/libs/libecm.so: Operation not supported\nflavius%\n```\n\n\nI built with gcc-4.6.0:\n\n\n```\nflavius% gcc -v\nUsing built-in specs.\nCOLLECT_GCC=gcc\nCOLLECT_LTO_WRAPPER=/usr/local/gcc-4.6.0/x86_64-Linux-k8-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.6.0/lto-wrapper\nTarget: x86_64-unknown-linux-gnu\nConfigured with: /usr/local/gcc-4.6.0/src/gcc-4.6.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-as=/usr/local/binutils-2.21/x86_64-Linux-k8-fc-gcc-4.5.1-rh/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.21/x86_64-Linux-k8-fc-gcc-4.5.1-rh/bin/ld --with-gmp=/usr/local/mpir-2.3.0/x86_64-Linux-k8-fc-gcc-4.5.1-rh --with-mpfr=/usr/local/mpfr-3.0.0/x86_64-Linux-k8-fc-mpir-2.3.0-gcc-4.5.1-rh --with-mpc=/usr/local/mpc-0.9/x86_64-Linux-k8-fc-mpir-2.3.0-mpfr-3.0.0-gcc-4.5.1-rh --prefix=/usr/local/gcc-4.6.0/x86_64-Linux-k8-fc\nThread model: posix\ngcc version 4.6.0 (GCC) \nflavius%\n```\n",
    "created_at": "2011-06-02T17:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46117",
    "user": "mariah"
}
```

On skynet/flavius I get


```
flavius% execstack -c local/lib/python/site-packages/sage/libs/libecm.so
execstack: Could not set security context for local/lib/python/site-packages/sage/libs/libecm.so: Operation not supported
flavius%
```


I built with gcc-4.6.0:


```
flavius% gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.6.0/x86_64-Linux-k8-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.6.0/lto-wrapper
Target: x86_64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.6.0/src/gcc-4.6.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-as=/usr/local/binutils-2.21/x86_64-Linux-k8-fc-gcc-4.5.1-rh/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.21/x86_64-Linux-k8-fc-gcc-4.5.1-rh/bin/ld --with-gmp=/usr/local/mpir-2.3.0/x86_64-Linux-k8-fc-gcc-4.5.1-rh --with-mpfr=/usr/local/mpfr-3.0.0/x86_64-Linux-k8-fc-mpir-2.3.0-gcc-4.5.1-rh --with-mpc=/usr/local/mpc-0.9/x86_64-Linux-k8-fc-mpir-2.3.0-mpfr-3.0.0-gcc-4.5.1-rh --prefix=/usr/local/gcc-4.6.0/x86_64-Linux-k8-fc
Thread model: posix
gcc version 4.6.0 (GCC) 
flavius%
```




---

archive/issue_comments_046118.json:
```json
{
    "body": "Replying to [comment:102 mariah]:\n> On skynet/flavius I get\n> \n\n```\nflavius% execstack -c local/lib/python/site-packages/sage/libs/libecm.so\nexecstack: Could not set security context for local/lib/python/site-packages/sage/libs/libecm.so: Operation not supported\nflavius%\n```\n\n\n\n\n**Not supported?** WTF...\n\nNo idea what's causing that. Though I don't need it, I can toggle the flag here on Ubuntu (10.4) as I like.\n\nMaybe an obsolete version of `execstack`? Or maybe just a wrong, misleading error message? The path is correct (relative to `SAGE_ROOT`)?\n\nIf all doesn't help, simply try applying the patch (to `devel/sage/module_list.py`), touch `devel/sage/sage/libs/libecm.pyx` and run `./sage -b`.",
    "created_at": "2011-06-02T17:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46118",
    "user": "leif"
}
```

Replying to [comment:102 mariah]:
> On skynet/flavius I get
> 

```
flavius% execstack -c local/lib/python/site-packages/sage/libs/libecm.so
execstack: Could not set security context for local/lib/python/site-packages/sage/libs/libecm.so: Operation not supported
flavius%
```




**Not supported?** WTF...

No idea what's causing that. Though I don't need it, I can toggle the flag here on Ubuntu (10.4) as I like.

Maybe an obsolete version of `execstack`? Or maybe just a wrong, misleading error message? The path is correct (relative to `SAGE_ROOT`)?

If all doesn't help, simply try applying the patch (to `devel/sage/module_list.py`), touch `devel/sage/sage/libs/libecm.pyx` and run `./sage -b`.



---

archive/issue_comments_046119.json:
```json
{
    "body": "Replying to [comment:103 leif]:\n\n> If all doesn't help, simply try applying the patch (to `devel/sage/module_list.py`), touch `devel/sage/sage/libs/libecm.pyx` and run `./sage -b`.\n\nThis works.  Now the offending test passes.\n\n(I *thought* I did the execstack command in SAGE_ROOT.)\n\nIf you will add the patch to this ticket, I will\nhave another go at building on all the skynet machines.",
    "created_at": "2011-06-02T18:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46119",
    "user": "mariah"
}
```

Replying to [comment:103 leif]:

> If all doesn't help, simply try applying the patch (to `devel/sage/module_list.py`), touch `devel/sage/sage/libs/libecm.pyx` and run `./sage -b`.

This works.  Now the offending test passes.

(I *thought* I did the execstack command in SAGE_ROOT.)

If you will add the patch to this ticket, I will
have another go at building on all the skynet machines.



---

archive/issue_comments_046120.json:
```json
{
    "body": "Replying to [comment:104 mariah]:\n> (I *thought* I did the execstack command in SAGE_ROOT.)\n\nWell, *my* `execstack` (version 1.0) gives an appropriate error message on `non-existing.so`. Perhaps you have an old version installed that only supports 32-bit ELF.\n\n\n\n\n> If you will add the patch to this ticket, I will\n> have another go at building on all the skynet machines.\n\nOk, I'll make the extra linker flag depend on the OS (i.e., Linux).\n\nMay take 1-2 hours until I upload a Mercurial patch.",
    "created_at": "2011-06-02T18:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46120",
    "user": "leif"
}
```

Replying to [comment:104 mariah]:
> (I *thought* I did the execstack command in SAGE_ROOT.)

Well, *my* `execstack` (version 1.0) gives an appropriate error message on `non-existing.so`. Perhaps you have an old version installed that only supports 32-bit ELF.




> If you will add the patch to this ticket, I will
> have another go at building on all the skynet machines.

Ok, I'll make the extra linker flag depend on the OS (i.e., Linux).

May take 1-2 hours until I upload a Mercurial patch.



---

archive/issue_comments_046121.json:
```json
{
    "body": "Attachment\n\nSage library patch. Fixes 'execstack' issue on Fedora with GCC 4.6.0. Based on Sage 4.7.rc2.",
    "created_at": "2011-06-02T19:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46121",
    "user": "leif"
}
```

Attachment

Sage library patch. Fixes 'execstack' issue on Fedora with GCC 4.6.0. Based on Sage 4.7.rc2.



---

archive/issue_comments_046122.json:
```json
{
    "body": "Patch (to the Sage library) is up.",
    "created_at": "2011-06-02T20:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46122",
    "user": "leif"
}
```

Patch (to the Sage library) is up.



---

archive/issue_comments_046123.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-06-02T20:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46123",
    "user": "leif"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_046124.json:
```json
{
    "body": "I built sage-4.7.1.alpha1 with http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg and the attachment http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5847/trac_5847-module_list-fix_execstack-sagelib.patch on the following skynet machines and did 'make testlong'.  \n\n\n```\nia64-Linux-rhel           cleo\nia64-Linux-suse           iras\nx86_64-Linux-core2-fc     eno\nx86_64-Linux-k10-fc       lena\nx86_64-Linux-k8-fc        flavius\nx86_64-Linux-nehalem-fc   taurus\nx86_64-Linux-netburst-fc  sextus2\nx86-Linux-pentium4-fc     cicero\n```\n\n\nAll tests passed.  Positive review!",
    "created_at": "2011-06-03T18:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46124",
    "user": "mariah"
}
```

I built sage-4.7.1.alpha1 with http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg and the attachment http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5847/trac_5847-module_list-fix_execstack-sagelib.patch on the following skynet machines and did 'make testlong'.  


```
ia64-Linux-rhel           cleo
ia64-Linux-suse           iras
x86_64-Linux-core2-fc     eno
x86_64-Linux-k10-fc       lena
x86_64-Linux-k8-fc        flavius
x86_64-Linux-nehalem-fc   taurus
x86_64-Linux-netburst-fc  sextus2
x86-Linux-pentium4-fc     cicero
```


All tests passed.  Positive review!



---

archive/issue_comments_046125.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-03T18:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46125",
    "user": "mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046126.json:
```json
{
    "body": "Replying to [comment:110 jdemeyer]:\n\nJereon, please can you explain the change to \"sage-feature\", which means (correct me if I'm\nwrong) that this ticket will never be merged?\n\nPaul",
    "created_at": "2011-06-09T19:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46126",
    "user": "zimmerma"
}
```

Replying to [comment:110 jdemeyer]:

Jereon, please can you explain the change to "sage-feature", which means (correct me if I'm
wrong) that this ticket will never be merged?

Paul



---

archive/issue_comments_046127.json:
```json
{
    "body": "Replying to [comment:111 zimmerma]:\n> Replying to [comment:110 jdemeyer]:\n> \n> Jereon, please can you explain the change to \"sage-feature\", which means (correct me if I'm\n> wrong) that this ticket will never be merged?\n\nIt still has the non-trivial dependency on mpir (#8664).  It has been said that this ticket and #8664 should be merged together.",
    "created_at": "2011-06-10T08:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46127",
    "user": "jdemeyer"
}
```

Replying to [comment:111 zimmerma]:
> Replying to [comment:110 jdemeyer]:
> 
> Jereon, please can you explain the change to "sage-feature", which means (correct me if I'm
> wrong) that this ticket will never be merged?

It still has the non-trivial dependency on mpir (#8664).  It has been said that this ticket and #8664 should be merged together.



---

archive/issue_comments_046128.json:
```json
{
    "body": "Replying to [comment:112 jdemeyer]:\n\n> It still has the non-trivial dependency on mpir (#8664).  It has been said that this ticket and #8664 should be merged together.\n\nThis ticket (#5847) does **not** depend on #8664.  I reviewed this ticket (#5847) using the version of mpir in sage-4.7.1.alpha1.  Rather the ticket #8664 depends on this ticket, as the description and comments say.",
    "created_at": "2011-06-10T14:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46128",
    "user": "mariah"
}
```

Replying to [comment:112 jdemeyer]:

> It still has the non-trivial dependency on mpir (#8664).  It has been said that this ticket and #8664 should be merged together.

This ticket (#5847) does **not** depend on #8664.  I reviewed this ticket (#5847) using the version of mpir in sage-4.7.1.alpha1.  Rather the ticket #8664 depends on this ticket, as the description and comments say.



---

archive/issue_comments_046129.json:
```json
{
    "body": "Replying to [comment:114 mariah]:\n> This ticket (#5847) does **not** depend on #8664.  I reviewed this ticket (#5847) using the version of mpir in sage-4.7.1.alpha1.  Rather the ticket #8664 depends on this ticket, as the description and comments say.\n\nCorrect. #8664 just depends on this ticket because the **old** GMP-ECM (currently in Sage) uses deprecated functions MPIR 2.x does no longer support.",
    "created_at": "2011-06-10T15:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46129",
    "user": "leif"
}
```

Replying to [comment:114 mariah]:
> This ticket (#5847) does **not** depend on #8664.  I reviewed this ticket (#5847) using the version of mpir in sage-4.7.1.alpha1.  Rather the ticket #8664 depends on this ticket, as the description and comments say.

Correct. #8664 just depends on this ticket because the **old** GMP-ECM (currently in Sage) uses deprecated functions MPIR 2.x does no longer support.



---

archive/issue_comments_046130.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-06-18T09:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46130",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_046131.json:
```json
{
    "body": "[attachment:trac_5847-module_list-fix_execstack-sagelib.patch] needs to be rebased to #11377.",
    "created_at": "2011-06-18T09:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46131",
    "user": "jdemeyer"
}
```

[attachment:trac_5847-module_list-fix_execstack-sagelib.patch] needs to be rebased to #11377.



---

archive/issue_comments_046132.json:
```json
{
    "body": "Replying to [comment:119 jdemeyer]:\n> [attachment:trac_5847-module_list-fix_execstack-sagelib.patch] needs to be rebased to #11377.\n\nI can of course rebase the (one-line!) patch (or provide an alternate patch based on some later development version of Sage), but I don't really see a point in rebasing it [now] to an \"unstable\" version that hasn't been released or announced yet (cf. [comment:ticket:11377:14 this comment]).\n\nThough positively reviewed (and independent of other tickets / spkgs), this ticket has been further postponed to Sage 4.7.2 anyway, for reasons I don't know. Doesn't make much sense to me to revert it to \"needs work\" at this point, also since people might want to use it or give it a try with current or older versions of Sage. (They most probably won't if it is tagged \"needs work\".)",
    "created_at": "2011-06-18T17:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46132",
    "user": "leif"
}
```

Replying to [comment:119 jdemeyer]:
> [attachment:trac_5847-module_list-fix_execstack-sagelib.patch] needs to be rebased to #11377.

I can of course rebase the (one-line!) patch (or provide an alternate patch based on some later development version of Sage), but I don't really see a point in rebasing it [now] to an "unstable" version that hasn't been released or announced yet (cf. [comment:ticket:11377:14 this comment]).

Though positively reviewed (and independent of other tickets / spkgs), this ticket has been further postponed to Sage 4.7.2 anyway, for reasons I don't know. Doesn't make much sense to me to revert it to "needs work" at this point, also since people might want to use it or give it a try with current or older versions of Sage. (They most probably won't if it is tagged "needs work".)



---

archive/issue_comments_046133.json:
```json
{
    "body": "Attachment\n\nSage library patch. Fixes 'execstack' issue on Fedora with GCC 4.6.0. Rebased to Sage 4.7.1.alpha4. (Cf. #11377)",
    "created_at": "2011-07-05T10:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46133",
    "user": "leif"
}
```

Attachment

Sage library patch. Fixes 'execstack' issue on Fedora with GCC 4.6.0. Rebased to Sage 4.7.1.alpha4. (Cf. #11377)



---

archive/issue_comments_046134.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-07-05T11:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46134",
    "user": "leif"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046135.json:
```json
{
    "body": "I've added a rebased version of the patch to `module_list.py`, for Sage versions >= 4.7.1.alpha4.",
    "created_at": "2011-07-05T11:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46135",
    "user": "leif"
}
```

I've added a rebased version of the patch to `module_list.py`, for Sage versions >= 4.7.1.alpha4.



---

archive/issue_comments_046136.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-23T04:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46136",
    "user": "mderickx"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_046137.json:
```json
{
    "body": "The patch now applies clean and everything passes so it again can have a positive preview.",
    "created_at": "2011-08-23T04:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46137",
    "user": "mderickx"
}
```

The patch now applies clean and everything passes so it again can have a positive preview.



---

archive/issue_comments_046138.json:
```json
{
    "body": "Replying to [comment:124 mderickx]:\n> The patch now applies clean and everything passes so it again can have a positive preview.\n\nI'm testing this on a few of the skynet machines as well. So far all looks good. :)",
    "created_at": "2011-08-23T05:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46138",
    "user": "ohanar"
}
```

Replying to [comment:124 mderickx]:
> The patch now applies clean and everything passes so it again can have a positive preview.

I'm testing this on a few of the skynet machines as well. So far all looks good. :)



---

archive/issue_comments_046139.json:
```json
{
    "body": "Replying to [comment:125 ohanar]:\n> Replying to [comment:124 mderickx]:\n> > The patch now applies clean and everything passes so it again can have a positive preview.\n> \n> I'm testing this on a few of the skynet machines as well. So far all looks good. :)\n\nI've verified that all tests pass with 4.7.1 stable on all the systems mariah tested, so +1 for positive review.",
    "created_at": "2011-08-24T19:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46139",
    "user": "ohanar"
}
```

Replying to [comment:125 ohanar]:
> Replying to [comment:124 mderickx]:
> > The patch now applies clean and everything passes so it again can have a positive preview.
> 
> I'm testing this on a few of the skynet machines as well. So far all looks good. :)

I've verified that all tests pass with 4.7.1 stable on all the systems mariah tested, so +1 for positive review.



---

archive/issue_comments_046140.json:
```json
{
    "body": "Changing keywords from \"MPIR elliptic curves libecm ecm spkg\" to \"sd32 MPIR elliptic curves libecm ecm spkg\".",
    "created_at": "2011-08-24T23:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46140",
    "user": "was"
}
```

Changing keywords from "MPIR elliptic curves libecm ecm spkg" to "sd32 MPIR elliptic curves libecm ecm spkg".



---

archive/issue_comments_046141.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-12T18:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46141",
    "user": "leif"
}
```

Resolution: fixed



---

archive/issue_comments_046142.json:
```json
{
    "body": "Had to fix some old changelog entry.\n\nCorrected spkg at new location.",
    "created_at": "2011-09-23T05:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46142",
    "user": "leif"
}
```

Had to fix some old changelog entry.

Corrected spkg at new location.



---

archive/issue_comments_046143.json:
```json
{
    "body": "GMP-ECM 6.4 has just been released.\n\nPaul",
    "created_at": "2012-01-03T23:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5847#issuecomment-46143",
    "user": "zimmerma"
}
```

GMP-ECM 6.4 has just been released.

Paul
