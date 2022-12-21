# Issue 9875: Building PARI/GP with SAGE_CHECK=yes fails on rnfkummer on a PPC Mac OS X 10.4

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-09-08 18:58:52

Assignee: tbd

CC:  drkirkby mpatel georgsweber

*This is an upstream problem with PARI/GP*

On one PPC Mac OS X 10.4 machine, the "rnfkummer" test in PARI's `make test-all` always fails.

For example, with this version:

```
GP/PARI CALCULATOR Version 2.4.3 (development svn-12594)
PowerPC running darwin (PPC/GMP-5.0.1 kernel) 32-bit version
compiled: Sep  8 2010, gcc-4.5.1 (GCC)
(readline v5.0 enabled, extended help enabled)
```


I get a failure in rnfkummer (both sta and dyn), I am attaching the dif and the output of Configure.


---

Comment by jdemeyer created at 2010-09-08 18:59:07

output of Configure


---

Attachment

diff from `make test-all`


---

Comment by jhpalmieri created at 2010-09-08 19:52:23

I get the same error on t2.math.washington.edu (Solaris on sparc).


---

Comment by jdemeyer created at 2010-09-08 19:57:50

So what does a Solaris sparc have in common with a PPC OS X which other systems do not have???


---

Comment by jhpalmieri created at 2010-09-08 20:00:37

I've put the build directory from t2 at `/home/palmieri/t2/pari-2.4.3.svn-12577.p5` in case any of the files there are helpful.  (Note that the /home directories are the same on t2 as on sage.math, so you can access this directory from sage.math.)


---

Comment by jdemeyer created at 2010-09-08 20:06:29

Replying to [comment:5 jhpalmieri]:
> I've put the build directory from t2 at `/home/palmieri/t2/pari-2.4.3.svn-12577.p5` in case any of the files there are helpful.  (Note that the /home directories are the same on t2 as on sage.math, so you can access this directory from sage.math.)

Please do `chmod 755 /home/palmieri/t2/pari-2.4.3.svn-12577.p5` and then I can actually access it.


---

Comment by jdemeyer created at 2010-09-08 20:37:50

Thanks!  For reference, the PARI/GP build directory on t2 (a Solaris sparc) can be found on:
[http://sage.math.washington.edu/home/palmieri/t2/pari-2.4.3.svn-12577.p5/src/](http://sage.math.washington.edu/home/palmieri/t2/pari-2.4.3.svn-12577.p5/src/)


---

Comment by jdemeyer created at 2010-09-08 20:45:39

Replying to [comment:4 jdemeyer]:
> So what does a Solaris sparc have in common with a PPC OS X which other systems do not have???

32-bit big endian machines?


---

Comment by jhpalmieri created at 2010-09-09 04:47:31

I also get the same error on the skynet machine mark (a _very_ slow sparc machine running solaris).  I didn't the problem with fulvia (x86 running solaris).


---

Comment by drkirkby created at 2010-09-09 09:47:03

Replying to [comment:8 jdemeyer]:
> Replying to [comment:4 jdemeyer]:
> > So what does a Solaris sparc have in common with a PPC OS X which other systems do not have???
> 
> 32-bit big endian machines?

All modern SPARC systems are 64-bit. The Sun Ultra 1, which was the first 64-bit machine from Sun, was bought out in 1995 - i.e. 15 years ago, well before any Intel or AMD chip was 64-bit. 

However, to maintain backward compatibility, and to increase performance, Sun chose to retain the default builds as 32-bit. So are in fact building Sage 32-bit on Solaris, though a 64-bit build is possible. 

The fact John said the tests fail on 'mark' but pass on 'fulvia' does indicate it's very likely to be a big-endian issue. I have a machine running HP-UX which uses a PA-RISC processor. That is big-endian. I could try building Pari on there, though I'm not sure if it will work or not. I'd not be surprised if it failed to build on there. 

Dave


---

Comment by leif created at 2010-09-09 15:15:05

Replying to [comment:11 drkirkby]:
> All modern SPARC systems are 64-bit. The Sun Ultra 1, which was the first 64-bit machine from Sun, was bought out in 1995 - i.e. 15 years ago, well before any Intel or AMD chip was 64-bit.

i860? That were the days of SPARC V7... ;-)


---

Attachment

Adds doctest to catch this error in the future


---

Comment by jdemeyer created at 2010-09-11 06:40:11

Fix (spkg + doctest) tested on
 * 64-bit Intel Linux
 * 32-bit Intel Linux
 * 32-bit PPC OS X


---

Comment by jdemeyer created at 2010-09-11 06:40:11

Changing status from new to needs_review.


---

Comment by leif created at 2010-09-11 07:24:24

Changing priority from critical to blocker.


---

Comment by leif created at 2010-09-11 07:24:24

Assuming Mitesh is ok with that.


---

Comment by leif created at 2010-09-11 07:37:54

P.S.: Tell Mercurial some patches have been removed...


---

Comment by leif created at 2010-09-11 08:12:02

Can someone test the new spkg on MacOS X 10.*4* *Intel*? (The upstream fix only adds `-fno-common` on PPCs, not _Tiger_ in general, which is afaik wrong.)


---

Comment by leif created at 2010-09-11 08:21:41

Last comment refers to

```
### pari-2.4.3.svn-12577.p6 (Jeroen Demeyer, September 10th, 2010)
 * Add upstream fix for config/get_dlcflags and remove the patch
```

which is

```diff
$ diff -Nau pari-2.4.3.svn-12577.p5/src/config/get_dlcflags pari-2.4.3.svn-12577.p6/src/config/get_dlcflags 
--- pari-2.4.3.svn-12577.p5/src/config/get_dlcflags	2010-09-06 21:26:42.000000000 +0200
+++ pari-2.4.3.svn-12577.p6/src/config/get_dlcflags	2010-09-10 23:29:12.000000000 +0200
`@``@` -2,6 +2,10 `@``@`
 if test -n "$__gnuc__"; then
   case $osname in
     cygwin|mingw) DLCFLAGS=;;
+    darwin) DLCFLAGS=-fPIC
+      case $arch in
+        ppc|ppc64) DLCFLAGS="$DLCFLAGS -fno-common"
+      esac;;
     *) DLCFLAGS=-fPIC;;
   esac
 else #assume native compiler
```



---

Comment by leif created at 2010-09-11 10:53:34

Jeroen, could you also extend the message printed when `SAGE_TUNE_PARI=yes` to strongly recommend running PARI's test suite after tuning? (We could in principle do that automatically from `spkg-install` as well, but that's IMHO not a good idea since it then might get run twice, and also doing so wouldn't fit Sage's build/test process.)

As mentioned somewhere else (#9343?), one of PARI's self-tests fails _after "successful" tuning_ on a Pentium 4 Prescott running Ubuntu 9.04 (gcc 4.3.3). I've yet only put a comment on the wiki page; will open a ticket for that later.

----

I'd prefer prepending `./` to `Configure`, since this will give an _appropriate_ error message in any case where `src/Configure` does (for whatever reason) not exist. (Otherwise `bash` would then attempt to find it in `$PATH`, which might cause weird behavoir.)

----

While adding `-fno-common` on MacOS X 10.5 and 10.6, too, is perhaps a bit odd, it doesn't hurt; otherwise one should look for _Darwin 8_ (10.4) with `uname ...`. (I currently don't know the exact string; the relevant part should be the same on PPC 10.4.).


---

Comment by leif created at 2010-09-11 12:17:35

Replying to [comment:19 leif]:
> [...] otherwise one should look for _Darwin 8_ (10.4) with `uname ...`. (I currently don't know the exact string; the relevant part should be the same on PPC 10.4.).

``uname -r`` should start with `8` for MacOS X 10.4 / Tiger / Darwin 8.


---

Comment by jdemeyer created at 2010-09-11 12:55:09

Replying to [comment:17 leif]:
> Can someone test the new spkg on MacOS X 10.*4* *Intel*? (The upstream fix only adds `-fno-common` on PPCs, not _Tiger_ in general, which is afaik wrong.)

I agree this certainly needs to be tested.


---

Comment by jdemeyer created at 2010-09-11 13:10:07

patch for the PARI spkg with upstream fix and some cleanup


---

Attachment

Replying to [comment:19 leif]:
> Jeroen, could you also extend the message printed when `SAGE_TUNE_PARI=yes` to strongly recommend running PARI's test suite after tuning?
> 
> ----
> 
> I'd prefer prepending `./` to `Configure`, since this will give an _appropriate_ error message in any case where `src/Configure` does (for whatever reason) not exist.

Done. New spkg, same place: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p6.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p6.spkg)


---

Comment by leif created at 2010-09-11 14:20:52

Replying to [comment:21 jdemeyer]:
> Replying to [comment:17 leif]:
> > Can someone test the new spkg on MacOS X 10.*4* *Intel*? (The upstream fix only adds `-fno-common` on PPCs, not _Tiger_ in general, which is afaik wrong.)
> 
> I agree this certainly needs to be tested.

Well, the incapability of 10.4's linker / loader to handle common symbols in conjunction with dynamic libraries is completely unrelated to the processor architecture; I doubt the one used on Intel processors in 10.4 will differ much from the one on PowerPCs. (PPC may imply Darwin 8, but not the other way around.)

So I'd prefer keeping _our_ patch (which is already well-tested), or modify it to add a distinction on the Darwin release (``uname -r``, see above).


---

Comment by jhpalmieri created at 2010-09-11 17:15:42

The new spkg works (with SAGE_CHECK=yes) on t2.math.


---

Comment by jdemeyer created at 2010-09-12 08:16:34

Replying to [comment:23 leif]:
> Well, the incapability of 10.4's linker / loader to handle common symbols in conjunction with dynamic libraries is completely unrelated to the processor architecture; I doubt the one used on Intel processors in 10.4 will differ much from the one on PowerPCs. (PPC may imply Darwin 8, but not the other way around.)

I sent an email to the PARI people about this, let's see what they say.


---

Comment by leif created at 2010-09-17 15:55:53

Replying to [comment:21 jdemeyer]:
> Replying to [comment:17 leif]:
> > Can someone test the new spkg on MacOS X 10.*4* *Intel*? (The upstream fix only adds `-fno-common` on PPCs, not _Tiger_ in general, which is afaik wrong.)
> 
> I agree this certainly needs to be tested.

Georg, perhaps you could confirm that `-fno-common` is also needed on MacOS X 10.4 *Intel* machines? (Or the opposite, but to me that's unlikely.)

It should be sufficient to just try

```sh
$ cd .../pari-2.4.3.svn-12577.p6/src
$ ./Configure --graphic=none
$ make gp
```

(with http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p6.spkg)


---

Comment by leif created at 2010-09-17 16:14:12

The error we previously got on MacOS X 10.4 *PPC* looked like this:

```
/usr/bin/gcc  -o "/Users/jdemeyer/pari-2.4.3.svn-12577/src/Odarwin-ppc"/libpari-2.4.dylib -dynamiclib  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -fPIC -Wl,-flat_namespace,-undefined,suppress  mp.o mpinl.o F2x.o FF.o Flx.o FpE.o FpV.o FpX.o Qfb.o RgV.o RgX.o ZV.o ZX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bb_group.o bibli1.o bibli2.o bit.o buch1.o buch2.o buch3.o buch4.o concat.o ellanal.o elliptic.o galconj.o gen1.o gen2.o gen3.o hnf_snf.o ifactor1.o lll.o perm.o polarit1.o polarit2.o polarit3.o prime.o random.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o compile.o default.o errmsg.o es.o eval.o hash.o init.o intnum.o members.o pariinl.o parse.o sumiter.o DedekZeta.o Hensel.o QX_factor.o aprcl.o elldata.o ellsea.o galois.o galpol.o groupid.o krasner.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o darwin.o
ld: common symbols not allowed with MH_DYLIB output format with the -multi_module option
init.o definition of common _DEBUGMEM (size 4)
init.o definition of common _avma (size 4)
init.o definition of common _bot (size 4)
[...]
es.o definition of common _pariErr (size 4)
es.o definition of common _pariOut (size 4)
init.o definition of common _pari_errfile (size 4)
init.o definition of common _pari_infile (size 4)
init.o definition of common _pari_outfile (size 4)
init.o definition of common _cb_pari_err_recover (size 4)
init.o definition of common _foreignFuncFree (size 4)
init.o definition of common _cb_pari_handle_exception (size 4)
init.o definition of common _cb_pari_sigint (size 4)
init.o definition of common _cb_pari_whatnow (size 4)
init.o definition of common _foreignExprHandler (size 4)
init.o definition of common _foreignHandler (size 4)
init.o definition of common _memused (size 4)
/usr/bin/libtool: internal link edit command failed
make[1]: *** [libpari-2.4.dylib] Error 1
make: *** [gp] Error 2
```



---

Comment by jdemeyer created at 2010-09-17 20:10:22

Replying to [comment:25 jdemeyer]:
> I sent an email to the PARI people about this, let's see what they say.

I haven't had much luck, see [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1088](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1088):

Bill Allombert wrote:
> Jeroen Demeyer wrote:
> > In that case, I strongly recommend you to apply the patch to ALL darwin
> > architectures, not just ppc/ppc64.
> Why ? Is there any documentation that recommend that ? gcc documentation certainly does not.

I do agree with leif though, I will prepare a .p7 with the fix.


---

Comment by jdemeyer created at 2010-09-19 08:46:52

Replying to [comment:28 jdemeyer]:
> I do agree with leif though, I will prepare a .p7 with the fix.

New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p7.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p7.spkg)


---

Attachment

Patch for the PARI spkg .p6 to .p7


---

Comment by jdemeyer created at 2010-09-19 16:52:11

I think this is ready for review now.  The original issue seems to be fixed and the `get_dlcflags` change has been reverted.


---

Comment by leif created at 2010-09-19 23:24:55

I've again tested the latest p7 (which includes only minor* changes w.r.t. the p6) and the new Sage library patch (additional regression doctest) on Ubuntu 10.04 x86_64 (`ptestlong` run twice, the second time with #9898 applied and the lcalc p5 spkg from #9845). (Also, the new spkg is "sane".)

Since Jeroen has already successfully tested it on a PPC Mac (big-endian), and John on t2.math (I assume in 32-bit big-endian mode), and the patch to `get_dlcflags` has been reverted to what we already tested (which definitely works on MacOS X 10.*4* *Intel*, too), I set this to "positive review".

----
*Although I must admit I haven't yet verified that the newly updated upstream source files claiming to fix [PARI bug #1079](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079) achieve the same as the previously applied Sage patches ("segmentation fault in `rnfequation(,,1)` over Q").


---

Comment by leif created at 2010-09-19 23:24:55

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-20 00:44:15

Replying to [comment:31 leif]:
> I haven't yet verified that the newly updated upstream source files claiming to fix [PARI bug #1079](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079) achieve the same as the previously applied Sage patches [...]

As far as I can tell they do. (And do not introduce other changes.)


---

Comment by jhpalmieri created at 2010-09-20 01:49:08

I also tested this again on t2 (32-bit) and also an a 10.6 OS X Intel Mac, just to make sure the new Darwin-only changes didn't mess that up.  No problems in either case.


---

Comment by mpatel created at 2010-09-29 08:40:07

Resolution: fixed
