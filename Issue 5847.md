# Issue 5847: Update GMP-ECM to 6.2.2

Issue created by migration from https://trac.sagemath.org/ticket/5847

Original creator: mabshoff

Original creation time: 2009-04-21 23:49:57

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


---

Comment by was created at 2010-06-02 02:20:00


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

Comment by mhansen created at 2010-08-17 18:15:00

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-08-17 18:15:00

There is a 6.3 spkg at http://sage.math.washington.edu/home/mhansen/ecm-6.3.spkg

I've checked that it works with MPIR 2.1.1 and all tests pass.


---

Comment by leif created at 2010-08-27 14:19:14

Since Sage with MPIR 2.1.1 (#8664) requires updating to this package, I report at that ticket.


---

Comment by leif created at 2010-09-02 22:57:57

Since MPIR 2.1.1 has a bug (see #9837), I've (successfully) built and tested Sage 4.6.prealpha3 (see #9343 and [the NewPARI Wiki page](http://wiki.sagemath.org/NewPARI)) *with GMP 5.0.1* and this new ECM 6.3 spkg on Ubuntu 10.04 x86_64 (Core2, gcc 4.4.3; parallel build from scratch with 32 jobs; native code with O3).

`ptestlong` passed all tests.


---

Comment by leif created at 2010-09-02 23:09:06

It also passed `ptestlong` on the same machine with Sage *4.5.3.alpha2* and *MPIR* 2.1.1 (because the MPIR bug apparently only shows up in combination with the new PARI package, which isn't included in that Sage version).

Same for Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4, parallel build with 6 jobs, rest dito).


---

Attachment

Suggested changes - NOT (yet) a Mercurial patch. (Minor fixes, some comments added, some clean-up.)


---

Comment by leif created at 2010-09-03 03:41:44

I've added a reviewer patch (ordinary context diff) with some changes:

 * Remove also the manual page of previous installations.
 * Typo: `rm -r` -> `rm -f` (header file)
 * Removed setting of `CXXFLAGS`, since we don't have C++ code.
 * Don't overwrite `CFLAGS` if `SAGE64=yes` (instead, append). Removed `-O2 -g` in that case. Make use of `CFLAG64` if set.
 * Quote `$SAGE_LOCAL` in the parameters to `configure`, too.
 * Use `$MAKE` in `spkg-check`, too.
 * Some messages changed (e.g. all failures now starting with _"Error"_), some added.
 * A few comments/notes added (`SPKG.txt`, `spkg-install`).

If you're ok with the changes, I can replace the diff with a Mercurial patch. Or simply merge them...


---

Comment by leif created at 2010-11-04 05:40:37

*New spkg: http://spkg-upload.googlecode.com/files/ecm-6.3.p0.spkg*

*md5sum:* `b9b1fcd5ebc2e3689fd379c1dba3a372  ecm-6.3.p0.spkg`

New spkg based on Mike's with some more changes (than mentioned above).

Should be installed with the MPIR 2.1.3 spkg from #8664. See instructions there.

(Tested with Sage 4.6.1.alpha0 on Ubuntu 9.04 x86 and Ubuntu 10.04 x86_64.)


---

Comment by leif created at 2010-11-04 05:40:37

Changing type from defect to enhancement.


---

Comment by leif created at 2010-11-04 05:46:20

SPKG "reviewer" patch, based on Mike's, i.e. ecm-6.3 vs. ecm-6.3.p0. For reference/review.


---

Attachment

Built and tested on sage.math.washington.edu without problems.


---

Comment by leif created at 2010-11-04 18:32:58

Changing assignee from mabshoff to leif.


---

Comment by jdemeyer created at 2010-11-04 19:55:10

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

Comment by jdemeyer created at 2010-11-04 19:55:42

Log file for failed build on OS X 10.4 powerpc G5


---

Attachment


---

Comment by leif created at 2010-11-05 02:09:22

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

Comment by leif created at 2010-11-05 02:32:59

Paul, perhaps you have an idea what's going wrong there (ECM trying to use "64-bit" instructions on MacOS X 10.4 PPC [G5], with MPIR 2.1.3).


---

Comment by leif created at 2010-11-05 03:13:56

Jeroen, can you try configuring with `--disable-asm-redc`?

(The 64-bit PPC asm code is new in 6.3 btw.)


---

Comment by fbissey created at 2010-11-05 07:48:36

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

Comment by zimmerma created at 2010-11-05 08:50:19

Replying to [comment:14 leif]:
> Paul, perhaps you have an idea what's going wrong there (ECM trying to use "64-bit" instructions on MacOS X 10.4 PPC [G5], with MPIR 2.1.3).

is this a 32-bit machine? What does ECM config.guess return? Can you try the svn version of
GMP-ECM using `svn checkout svn://scm.gforge.inria.fr/svn/ecm`?

Paul


---

Comment by zimmerma created at 2010-11-05 08:51:40

Replying to [comment:15 leif]:
> Jeroen, can you try configuring with `--disable-asm-redc`?
> 
> (The 64-bit PPC asm code is new in 6.3 btw.)

it should work with `--disable-asm-redc`.

Paul


---

Comment by jdemeyer created at 2010-11-05 08:56:18

Thanks for all the suggestions, I will try them but probably not today.


---

Comment by leif created at 2010-11-05 12:33:48

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

Worked for me _without patching_ with both MPIR 2.1.1 and [vanilla] GMP 5.0.1 on Ubuntu ([comment:5 see above]).


---

Comment by leif created at 2010-11-05 12:52:30

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

Comment by leif created at 2010-11-05 12:56:57

Any objections to enable (also) building a shared library?

(And also enabling the build of a _static_ MPIR library, which is better for ECM?)


---

Comment by leif created at 2010-11-05 13:05:51

I wonder how the GNU assembler (Linux PPC) behaves...

François, would you like to test this?


---

Comment by zimmerma created at 2010-11-05 15:40:00

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

Comment by dimpase created at 2010-11-05 17:27:02

Replying to [comment:21 leif]:

the required MPIR spkg does not build on PPC (see my comment on #8664)


---

Comment by jdemeyer created at 2010-11-05 21:12:31

Replying to [comment:15 leif]:
> Jeroen, can you try configuring with `--disable-asm-redc`?
The build (outside of Sage) *works*.

Replying to [comment:17 zimmerma]:
> is this a 32-bit machine?
Well, technically the processor is 64-bit capable (I believe) but it runs a 32-bit system and `gcc` produces 32-bit code by default.

> What does ECM config.guess return?
powerpc-apple-darwin8.11.0

Can you try the svn version of
> GMP-ECM using `svn checkout svn://scm.gforge.inria.fr/svn/ecm`?
This *works*.

Replying to [comment:24 zimmerma]:
> in fact this bug is already fixed upstream (in revision 1516)
>
> Please can you check it works correctly with this patch?
This *works*.

Replying to [comment:21 leif]:
> Setting `ABI=32` would perhaps also work.
No, it does *not*.


---

Comment by jdemeyer created at 2010-11-05 21:12:31

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-11-05 22:09:15

Replying to [comment:26 jdemeyer]:
> Replying to [comment:15 leif]:
> > Jeroen, can you try configuring with `--disable-asm-redc`?
> The build (outside of Sage) *works*.

Well, I'm a bit unsure what to do now. I can of course include the patch, but that does not what we actually want (it's just a work-around).

I think passing `-Wa,-force_cpusubtype_ALL` on MacOS PPCs should also work (which does *not* disable the assembly code, but avoids the odd assembler error, such that we get better performance).

Note that this worked on Dima's *G4* with MPIR, so I expect it to work with a G5, too.

Don't know if G3s run into the same problem, or support these instructions. We then might have to really disable the code on PPCs < G4.

We could of course just test this in `spkg-install`, i.e. feed some extended instruction set assembly code to the assembler with `-force_cpusubtype_ALL` and see if we get an error before we disable the redc asm code. (I'd have to look what option `gas` takes on _Linux_ PPC.)

Objections against adding yet another environment variable (`ECM_EXTRA_OPTS`, to add to ECM's `configure`, analoguous to `PARI_EXTRA_OPTS`), to ease working around potential problems showing up later?


---

Comment by leif created at 2010-11-05 22:41:16

From my `gas` manpage (relevant for *Linux* PPC only):

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

P.S.: That the _build_ works with `-force_cpusubtype_ALL` (_without_ `SAGE_CHECK=yes`) doesn't necessarily mean we couldn't get illegal instruction exceptions when actually _running_ the code.


---

Comment by leif created at 2010-11-05 22:41:16

Changing status from needs_work to needs_info.


---

Comment by fbissey created at 2010-11-06 03:25:27

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

Comment by leif created at 2010-11-06 04:41:15

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

Hmmm, we have to upgrade ECM _because of_ the upgrade of MPIR / GMP:
  
 *_Changes between ecm-6.2.3 and ecm-6.3:*_

   * _New assembly code for 64-bit PowerPC (thanks to Philip McLaughlin)_
   * _Allow several processes to write to the same -save file_
   * _More routines in new P+-1 stage 2 use multi-threading in OpenMP build_
   * *_Fixed incompatibility with GMP 5.0.0*_
   * _Fixed several bugs, and now check return value from malloc() calls_
   * _Fixed linking of GMP which prevented successful builds under Darwin (and presumably other systems)_
   * _Allow use of x86_64 asm code under MinGW_



> I add a bug report specifically on that in Gentoo and I could reproduce it on one
> of my machine which has GMP 5.0.1.


---

Comment by fbissey created at 2010-11-06 05:21:13

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
> Hmmm, we have to upgrade ECM _because of_ the upgrade of MPIR / GMP:
>   
>  *_Changes between ecm-6.2.3 and ecm-6.3:*_
> 
>    * _New assembly code for 64-bit PowerPC (thanks to Philip McLaughlin)_
>    * _Allow several processes to write to the same -save file_
>    * _More routines in new P+-1 stage 2 use multi-threading in OpenMP build_
>    * *_Fixed incompatibility with GMP 5.0.0*_
>    * _Fixed several bugs, and now check return value from malloc() calls_
>    * _Fixed linking of GMP which prevented successful builds under Darwin (and presumably other systems)_
>    * _Allow use of x86_64 asm code under MinGW_
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

Comment by dimpase created at 2010-11-06 14:23:57

Changing status from needs_info to needs_work.


---

Comment by dimpase created at 2010-11-06 14:23:57

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

Comment by leif created at 2010-11-06 17:29:48

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

Comment by leif created at 2010-11-06 17:54:57

Changing status from needs_work to needs_info.


---

Comment by dimpase created at 2010-11-07 04:50:04

macosx 10.5 ppc G4 failure of ./configure


---

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

Comment by dimpase created at 2010-11-07 05:48:18

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

Comment by dimpase created at 2010-11-07 06:17:50

Changing status from needs_info to needs_work.


---

Comment by dimpase created at 2010-11-07 06:17:50

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

Comment by dimpase created at 2010-11-07 06:43:29

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

Attachment

macosx 10.5 ppc G4 with tweaked ./configure --disable-asm-redc (adding extra command in conftes2.s)


---

Comment by jdemeyer created at 2010-11-07 10:06:46

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

Comment by jdemeyer created at 2010-11-07 10:07:32

Again, with proper formatting:

```
$ /usr/libexec/gcc/powerpc-apple-darwin9/4.2.1/ld --version
$ which ld
$ ld --version 
```



---

Comment by zimmerma created at 2010-11-07 11:50:55

[I write here as a developer of GMP-ECM]

the configure error reported in comment 32 seems to be a ld problem. User "dimpase", do you
manage to configure GMP successfully?

Also, which version of GMP-ECM did you use in comment 32? The svn version (see comment 24) should
fix the fact that 64-bit assembly is used on 32-bit machines. If not, please report the problem
upstream on http://ecm.gforge.inria.fr/.

Paul Zimmermann


---

Comment by dimpase created at 2010-11-07 12:49:53

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

Comment by dimpase created at 2010-11-07 13:03:56

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

Comment by zimmerma created at 2010-11-07 16:37:07

> do you want me to test the svn version on this machine?

yes, as upstream developer I cannot help unless you report a problem with the (vanilla) upstream version.

Of course you are also free to solve the problem within Sage, but if it is not due to the Sage
packaging, it would be useful to report it upstream.

Paul Zimmermann


---

Comment by dimpase created at 2010-11-07 17:30:53

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

Comment by jdemeyer created at 2010-11-07 17:35:45

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

Comment by zimmerma created at 2010-11-07 17:41:00

you can also try the snapshot from
http://www.loria.fr/~zimmerma/ecm-6.3.1.tar.gz
(note this is NOT a release).

Paul Zimmermann


---

Comment by dimpase created at 2010-11-07 17:44:31

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

Comment by dimpase created at 2010-11-08 02:21:07

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

Comment by dimpase created at 2010-11-08 04:43:31

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

Comment by zimmerma created at 2010-11-08 06:52:12

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

Comment by jdemeyer created at 2010-11-09 10:42:23

Replying to [comment:27 leif]:
> Replying to [comment:26 jdemeyer]:
> > Replying to [comment:15 leif]:
> > > Jeroen, can you try configuring with `--disable-asm-redc`?
> > The build (outside of Sage) *works*.
> 
> Well, I'm a bit unsure what to do now. I can of course include the patch, but that does not what we actually want (it's just a work-around).

Well, since the patch comes from upstream and fixes the problem is all known cases, I think it makes sense to make a new ecm spkg with this patch included.  Leif, what do you think (and could you make the spkg? YES/NO)


---

Comment by dimpase created at 2010-11-09 13:29:24

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

Comment by jdemeyer created at 2010-11-10 10:48:21

New spkg with upstream patch from comment:24: [http://sage.math.washington.edu/home/jdemeyer/spkg/ecm-6.3.p1.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/ecm-6.3.p1.spkg)

I still have to test it properly though.


---

Comment by jdemeyer created at 2010-11-10 10:48:21

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-11-10 10:48:44

patch from p0 to p1, for review


---

Attachment


---

Comment by jdemeyer created at 2010-11-11 13:32:11

Tested new spkg succesfully on the previously-failing OS X 10.4 PPC machine.


---

Comment by dimpase created at 2010-11-11 14:16:11

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2010-11-11 14:16:11

Replying to [comment:56 jdemeyer]:
> Tested new spkg succesfully on the previously-failing OS X 10.4 PPC machine.

works on MacOSX 10.5 PPC. Positive review!


---

Comment by jdemeyer created at 2010-11-11 19:37:09

Resolution: fixed


---

Comment by jdemeyer created at 2010-11-12 10:27:08

There is some serious trouble with this spkg: #10252


---

Comment by jdemeyer created at 2010-11-12 13:06:45

Changing status from closed to new.


---

Comment by jdemeyer created at 2010-11-12 13:06:45

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2010-11-12 13:07:04

Changing status from new to needs_work.


---

Comment by leif created at 2010-11-22 03:39:52

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

Comment by leif created at 2010-11-24 00:32:32

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-11-24 00:32:32

*New spkg: http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg*

*md5sum:* `85eabecaa8974a270d5587ef8de06da1  ecm-6.3.p2.spkg`

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

Comment by leif created at 2010-11-24 00:49:42

FWIW, you can also test this package with the old MPIR (1.2.2), or some older GMP. Should work as well.


---

Comment by leif created at 2010-11-24 01:24:15

Ooops, I just noticed I've cleaned up a little bit too much (and did _not_ enable building also a shared library by default).

As is, the Sage library won't build with the new package, unless you either install it with
 * `CFLAGS` containing (also) `-fPIC`, or
 * `ECM_EXTRA_OPTS=--enable-shared`.

(Both together also works. So yet another reason we *have to* pass our custom `CFLAGS`.)

I'll update the spkg later, after some feedback I think.


---

Comment by leif created at 2010-11-24 02:39:36

Replying to [comment:65 leif]:
> As is, the Sage library won't build with the new package, unless you either install it with 


>  * `CFLAGS` containing (also) `-fPIC`, or


>  * `ECM_EXTRA_OPTS=--enable-shared`.



Another option is to pass `ECM_EXTRA_OPTS=--with-pic`, not sure if this works on all platforms.


---

Comment by leif created at 2010-11-24 03:06:43

Just for the record: I'll also update the MPIR spkg s.t. we can get "tuned" `CFLAGS` from it (essentially some potentially better / more specific `-march=...` for non-x86 systems).

The current GMP-ECM spkg uses `-march=native` on x86 / x86_64 systems.


---

Comment by zimmerma created at 2010-11-24 07:21:39

just a comment: the ticket title mentions ECM 6.3, but the changes in the description refer to
changes between 6.2.1 and 6.2.2.

Paul


---

Comment by jdemeyer created at 2010-11-24 08:30:12

Leif: why not let ECM use MPIR's CFLAGS?  It seems to me like you're making this package more complicated that it should be.


---

Comment by jdemeyer created at 2010-11-24 08:31:09

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

Comment by jdemeyer created at 2010-11-24 08:31:09

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-11-24 10:23:25

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

Comment by leif created at 2010-11-24 10:26:17

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

(There are also notes on this in both the changelog and the _Special Update/Build Instructions_, see above.)

What C compilers _does_ Sage currently support (and will Sage support in the near future)?

Cf. [comment:ticket:10252:20 this comment]:
  _There's very little support for other compilers in Sage, and it's easy to add a distinction when the day it gets necessary comes, though I could add it now._


Btw, if a user decides or has to set `CC` for some reason (which might even be just to use a different `gcc`), GMP-ECM won't use MPIR's / GMP's `CFLAGS` either. And MPIR isn't omniscient...


---

Comment by leif created at 2010-11-24 10:30:25

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

Comment by leif created at 2010-11-24 10:33:39

P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.


---

Comment by jdemeyer created at 2010-11-24 10:38:02

Replying to [comment:73 leif]:
> What C compilers _does_ Sage currently support (and will Sage support in the near future)?

Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).

Anyway, the proper way to do this is to actually run `gcc -march=native` on some stupid .c file and check whether it compiles (there is no need to actually run the compiled program, so we can compile to `/dev/null`).


---

Comment by jdemeyer created at 2010-11-24 10:39:08

Replying to [comment:74 leif]:
> Do you read [the comments](http://trac.sagemath.org/sage_trac/ticket/5847#comment:65)?
Clearly, I did not...


---

Comment by leif created at 2010-11-24 11:23:26

Replying to [comment:76 jdemeyer]:
> Replying to [comment:73 leif]:
> > What C compilers _does_ Sage currently support (and will Sage support in the near future)?
> 
> Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).

At least since four years ago, don't know the exact version...

> Anyway, the proper way to do this is to actually run `gcc -march=native` on some stupid .c file and check whether it compiles (there is no need to actually run the compiled program, so we can compile to `/dev/null`).

`gcc -v -march=native` should be sufficient, since the preprocessor also needs to know about it.


---

Comment by leif created at 2010-11-24 12:10:37

Replying to [comment:78 leif]:
> Replying to [comment:76 jdemeyer]:
> > Replying to [comment:73 leif]:
> > > What C compilers _does_ Sage currently support (and will Sage support in the near future)?
> > 
> > Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).
> 
> At least since four years ago, don't know the exact version...

GCC 4.0.1 might not support it (could you test that on an x86 machine?); GCC 4.2.1 certainly does.


---

Comment by leif created at 2010-11-24 12:11:56

Replying to [comment:79 leif]:
> Replying to [comment:78 leif]:
> > Replying to [comment:76 jdemeyer]:
> > > Replying to [comment:73 leif]:
> > > > What C compilers _does_ Sage currently support (and will Sage support in the near future)?
> > > 
> > > Okay, I was referring to older versions of `gcc` which do not support `-march=native` (it is a relatively new command line option, so we cannot assume that it will work).
> > 
> > At least since four years ago, don't know the exact version...
> 
> GCC 4.0.1 might not support it (could you test that on an x86 machine?); GCC 4.2.1 certainly does.

... and 4.1.2 also does.


---

Comment by jdemeyer created at 2010-11-24 13:29:27

Replying to [comment:78 leif]:
> `gcc -v -march=native` should be sufficient, since the preprocessor also needs to know about it.

No, that's not sufficient to test it, it does not run the preprocessor.

If you want to run to preprocessor, the following works:

```
gcc -march=native -E -x c /dev/null -o /dev/null
```


Using this test, `-march=native` works for me on gcc 4.2.3, NOT on gcc 4.0.3


---

Comment by leif created at 2010-11-24 13:59:05

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

Comment by jdemeyer created at 2010-11-24 14:14:39

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

Comment by jdemeyer created at 2010-11-24 14:15:40

I'm still thinking that these changes should go to the mpir package and that ecm should use the default `CFLAGS` provided by mpir.


---

Comment by leif created at 2010-11-24 17:31:50

Replying to [comment:68 zimmerma]:
> just a comment: the ticket title mentions ECM 6.3, but the changes in the description refer to
> changes between 6.2.1 and 6.2.2.

That's a historical relict; I've now also added the other changes between Sage's current version and 6.3.


---

Comment by leif created at 2010-11-25 14:23:00

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-11-25 14:23:00

Changing keywords from "" to "MPIR elliptic curves libecm".


---

Comment by leif created at 2010-11-25 14:23:00

Replying to [comment:75 leif]:
> P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.

Although (or because) there's not much feedback yet, I've uploaded a corrected spkg (still p2) with also some other changes. This obsoletes setting `ECM_EXTRA_OPTS=--with-pic` or `-fPIC` in `CFLAGS` etc., works with all GCC 4.0.x on x86 as well and also uses processor-specific settings from MPIR if available.

*Updated spkg: http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg* (same place)

*md5sum:* `8246ca74be1ee07b312a84d2a88d9142  ecm-6.3.p2.spkg` (fortunately differs ;-) )

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

Attachment

Diff between the p1 and the p2 spkg. For reference / review.


---

Attachment

Mercurial patch to get the p2 from the p1 spkg. Except for the commit messages perhaps less readable. (6 changesets.)


---

Comment by dimpase created at 2010-11-25 16:39:34

Replying to [comment:86 leif]:
> Replying to [comment:75 leif]:
> > P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.

builts OK on OSX 10.5 PPC, with SAGE_CHECK=yes


---

Comment by leif created at 2010-11-25 16:59:42

Replying to [comment:87 dimpase]:
> Replying to [comment:86 leif]:
> > Replying to [comment:75 leif]:
> > > P.S.: As I said, I first want to get some test results (e.g. on PowerPCs etc.) before I upload further changes.
> 
> builts OK on OSX 10.5 PPC, with SAGE_CHECK=yes
> 

Happy to hear that. I wonder what happens on other MacOS X versions with GCC 4.2.1 (regarding the linker bus error in `configure` when `-g` was given to `gcc`).


---

Comment by jdemeyer created at 2010-11-26 08:29:04

Changing keywords from "MPIR elliptic curves libecm" to "MPIR elliptic curves libecm ecm spkg".


---

Comment by leif created at 2010-11-26 08:51:38

Replying to [comment:89 jdemeyer]:
> *Testing distribution* with new mpir (#8664) and new ecm: http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.1.alpha2-mpir/sage-4.6.1.alpha2-mpir.tar

Thanks.


---

Comment by jdemeyer created at 2010-11-28 15:10:17

Tested successfully on
 * sage.math.washington.edu
 * OS X 10.4 PPC
 * 32-bit Gentoo Linux Pentium 4


---

Comment by drkirkby created at 2011-05-09 21:13:25

`SAGE_FAT_BINARY` is unsupported in this package, but to compond the problem, the compiler option


```
-march=native
```


is added. That's just asking for trouble for distributing binaries.


---

Comment by mariah created at 2011-05-12 15:34:10

SAGE_FAT_BINARY needs to be supported.


---

Comment by mariah created at 2011-05-12 15:34:10

Changing status from needs_review to needs_work.


---

Comment by leif created at 2011-05-15 08:04:22

Replying to [comment:93 drkirkby]:
> `SAGE_FAT_BINARY` is unsupported in this package, but to compond the problem, the compiler option
> 

```
-march=native
```

> 
> is added.



Well, apparently `SAGE_FAT_BINARY` has _never been_ supported by the ECM spkg.

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

Comment by leif created at 2011-05-15 08:08:59

Replying to [comment:94 mariah]:
> SAGE_FAT_BINARY needs to be supported.



In which way / to what extent?

(See my previous post.)


---

Comment by leif created at 2011-05-15 08:08:59

Changing status from needs_work to needs_info.


---

Comment by mariah created at 2011-05-16 16:06:14

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

Comment by mariah created at 2011-05-16 16:06:14

Changing status from needs_info to needs_review.


---

Comment by mariah created at 2011-06-02 14:30:07

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


*Strongly* suggest ecm be built with same CFLAGS values as gmp/mpir as recommended by ecm INSTALL file.


---

Comment by mariah created at 2011-06-02 14:30:07

Changing status from needs_review to needs_work.


---

Comment by leif created at 2011-06-02 15:54:48

Changing status from needs_work to needs_info.


---

Comment by leif created at 2011-06-02 15:54:48

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
> *Strongly* suggest ecm be built with same CFLAGS values as gmp/mpir as recommended by ecm INSTALL file.



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

Comment by leif created at 2011-06-02 16:15:32

*Disclaimer for Dave:*

The patch above is a bit hackish. We should either pass the additional compiler flag _conditionally_ (on Linux systems only, where we can rely on a GNU linker), or perhaps instead use GCC's `--noexecstack` parameter, of which I currently don't know whether it is supported by ancient versions of GCC.


---

Comment by leif created at 2011-06-02 16:54:31

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

Comment by mariah created at 2011-06-02 17:25:01

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

Comment by leif created at 2011-06-02 17:53:34

Replying to [comment:102 mariah]:
> On skynet/flavius I get
> 

```
flavius% execstack -c local/lib/python/site-packages/sage/libs/libecm.so
execstack: Could not set security context for local/lib/python/site-packages/sage/libs/libecm.so: Operation not supported
flavius%
```




*Not supported?* WTF...

No idea what's causing that. Though I don't need it, I can toggle the flag here on Ubuntu (10.4) as I like.

Maybe an obsolete version of `execstack`? Or maybe just a wrong, misleading error message? The path is correct (relative to `SAGE_ROOT`)?

If all doesn't help, simply try applying the patch (to `devel/sage/module_list.py`), touch `devel/sage/sage/libs/libecm.pyx` and run `./sage -b`.


---

Comment by mariah created at 2011-06-02 18:32:22

Replying to [comment:103 leif]:

> If all doesn't help, simply try applying the patch (to `devel/sage/module_list.py`), touch `devel/sage/sage/libs/libecm.pyx` and run `./sage -b`.

This works.  Now the offending test passes.

(I _thought_ I did the execstack command in SAGE_ROOT.)

If you will add the patch to this ticket, I will
have another go at building on all the skynet machines.


---

Comment by leif created at 2011-06-02 18:49:39

Replying to [comment:104 mariah]:
> (I _thought_ I did the execstack command in SAGE_ROOT.)

Well, _my_ `execstack` (version 1.0) gives an appropriate error message on `non-existing.so`. Perhaps you have an old version installed that only supports 32-bit ELF.




> If you will add the patch to this ticket, I will
> have another go at building on all the skynet machines.

Ok, I'll make the extra linker flag depend on the OS (i.e., Linux).

May take 1-2 hours until I upload a Mercurial patch.


---

Attachment

Sage library patch. Fixes 'execstack' issue on Fedora with GCC 4.6.0. Based on Sage 4.7.rc2.


---

Comment by leif created at 2011-06-02 20:04:39

Patch (to the Sage library) is up.


---

Comment by leif created at 2011-06-02 20:04:39

Changing status from needs_info to needs_review.


---

Comment by mariah created at 2011-06-03 18:06:49

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

Comment by mariah created at 2011-06-03 18:06:49

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2011-06-09 19:41:35

Replying to [comment:110 jdemeyer]:

Jereon, please can you explain the change to "sage-feature", which means (correct me if I'm
wrong) that this ticket will never be merged?

Paul


---

Comment by jdemeyer created at 2011-06-10 08:19:00

Replying to [comment:111 zimmerma]:
> Replying to [comment:110 jdemeyer]:
> 
> Jereon, please can you explain the change to "sage-feature", which means (correct me if I'm
> wrong) that this ticket will never be merged?

It still has the non-trivial dependency on mpir (#8664).  It has been said that this ticket and #8664 should be merged together.


---

Comment by mariah created at 2011-06-10 14:45:16

Replying to [comment:112 jdemeyer]:

> It still has the non-trivial dependency on mpir (#8664).  It has been said that this ticket and #8664 should be merged together.

This ticket (#5847) does *not* depend on #8664.  I reviewed this ticket (#5847) using the version of mpir in sage-4.7.1.alpha1.  Rather the ticket #8664 depends on this ticket, as the description and comments say.


---

Comment by leif created at 2011-06-10 15:23:32

Replying to [comment:114 mariah]:
> This ticket (#5847) does *not* depend on #8664.  I reviewed this ticket (#5847) using the version of mpir in sage-4.7.1.alpha1.  Rather the ticket #8664 depends on this ticket, as the description and comments say.

Correct. #8664 just depends on this ticket because the *old* GMP-ECM (currently in Sage) uses deprecated functions MPIR 2.x does no longer support.


---

Comment by jdemeyer created at 2011-06-18 09:14:54

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-06-18 09:14:54

[attachment:trac_5847-module_list-fix_execstack-sagelib.patch] needs to be rebased to #11377.


---

Comment by leif created at 2011-06-18 17:21:15

Replying to [comment:119 jdemeyer]:
> [attachment:trac_5847-module_list-fix_execstack-sagelib.patch] needs to be rebased to #11377.

I can of course rebase the (one-line!) patch (or provide an alternate patch based on some later development version of Sage), but I don't really see a point in rebasing it [now] to an "unstable" version that hasn't been released or announced yet (cf. [comment:ticket:11377:14 this comment]).

Though positively reviewed (and independent of other tickets / spkgs), this ticket has been further postponed to Sage 4.7.2 anyway, for reasons I don't know. Doesn't make much sense to me to revert it to "needs work" at this point, also since people might want to use it or give it a try with current or older versions of Sage. (They most probably won't if it is tagged "needs work".)


---

Attachment

Sage library patch. Fixes 'execstack' issue on Fedora with GCC 4.6.0. Rebased to Sage 4.7.1.alpha4. (Cf. #11377)


---

Comment by leif created at 2011-07-05 11:02:02

Changing status from needs_work to needs_review.


---

Comment by leif created at 2011-07-05 11:05:39

I've added a rebased version of the patch to `module_list.py`, for Sage versions >= 4.7.1.alpha4.


---

Comment by mderickx created at 2011-08-23 04:11:45

Changing status from needs_review to positive_review.


---

Comment by mderickx created at 2011-08-23 04:11:45

The patch now applies clean and everything passes so it again can have a positive preview.


---

Comment by ohanar created at 2011-08-23 05:56:31

Replying to [comment:124 mderickx]:
> The patch now applies clean and everything passes so it again can have a positive preview.

I'm testing this on a few of the skynet machines as well. So far all looks good. :)


---

Comment by ohanar created at 2011-08-24 19:55:35

Replying to [comment:125 ohanar]:
> Replying to [comment:124 mderickx]:
> > The patch now applies clean and everything passes so it again can have a positive preview.
> 
> I'm testing this on a few of the skynet machines as well. So far all looks good. :)

I've verified that all tests pass with 4.7.1 stable on all the systems mariah tested, so +1 for positive review.


---

Comment by was created at 2011-08-24 23:36:21

Changing keywords from "MPIR elliptic curves libecm ecm spkg" to "sd32 MPIR elliptic curves libecm ecm spkg".


---

Comment by leif created at 2011-09-12 18:58:14

Resolution: fixed


---

Comment by leif created at 2011-09-23 05:09:46

Had to fix some old changelog entry.

Corrected spkg at new location.


---

Comment by zimmerma created at 2012-01-03 23:58:29

GMP-ECM 6.4 has just been released.

Paul
