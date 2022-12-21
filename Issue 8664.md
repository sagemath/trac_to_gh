# Issue 8664: upgrade sage's mpir spkg to version 2.0.0

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-09 04:10:07

Assignee: GeorgSWeber

CC:  was leif drkirkby jdemeyer wbhart jpflori


```
Hi,

OK, after all this, the build finally completed.  The only changes I made were:

* Updated mpir to rc3
* patched ecm as explained here:
    http://lists.gforge.inria.fr/pipermail/ecm-discuss/2009-August/004070.html
   (Though this had to be slightly modified -- just search for the same command, which moved.)


I then ran the long Sage test suite, and some tests fail.  

  http://sage.math.washington.edu/home/wstein/build/mpir2/sage-4.3.5/testlong.log

----------------------------------------------------------------------
The following tests failed:


        sage -t  -long "devel/sage/doc/en/tutorial/tour_numtheory.rst"
        sage -t  -long "devel/sage/doc/fr/tutorial/tour_numtheory.rst"
        sage -t  -long "devel/sage/sage/modular/cusps.py"
        sage -t  -long "devel/sage/sage/modular/modsym/boundary.py"
        sage -t  -long "devel/sage/sage/modular/modsym/ambient.py"
        sage -t  -long "devel/sage/sage/libs/pari/gen.pyx"
        sage -t  -long "devel/sage/sage/rings/arith.py"
        sage -t  -long "devel/sage/sage/rings/integer.pyx"
        sage -t  -long "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
        sage -t  -long "devel/sage/sage/tests/book_stein_ent.py"
        sage -t  -long "devel/sage/sage/schemes/elliptic_curves/heegner.py"
Total time for all tests: 7170.6 seconds

--

I looked and it appears that maybe all of these are the result of the XGCD behavior in MPIR changing again.  Has it changed to be like GMP now?  That would be convenient.

william
```



---

Comment by GeorgSWeber created at 2010-05-19 09:55:45

The XGCD issue needs some work w.r.t. doctests (but not only, see below), maybe David Harvey has something done already in this direction when preparing the optional "true" GMP spkg he maintains. (I don't find the thread right now, but I seem to remember he said something in this direction).

Snippet from a private communication by Bill Hart (MPIR upstream):

```
MPIR 2.0.1 will be required for Sage because it brings the gcdext
normalisation in line with GMP's (which is what Pari needs). I think
people have skipped MPIR 1.3.0 in favour of waiting for MPIR 2.0.1.
We're in the release phase of MPIR 2.0.1 ...
```

Also note that as soon as this ticket here is closed, we should mark #8455 as invalid.


---

Comment by mhansen created at 2010-08-17 18:33:48

This needs to be handled with #5847 and should take care of #9522 at the same time.


---

Comment by mhansen created at 2010-08-18 06:22:55

I've put an spkg at http://sage.math.washington.edu/home/mhansen/mpir-2.1.1.spkg

Interestingly, I did not get any of the failures listed above.


---

Comment by mhansen created at 2010-08-18 06:22:55

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-08-19 22:51:57

Changing component from build to packages.


---

Comment by leif created at 2010-08-26 22:48:28

Hmmm, `spkg-install` could be cleaned up further, e.g.
 * Dave's comment has somehow been truncated(?) a while ago (_"... if"_ what?)
 * `s/`uname`/$UNAME/`
 * Especially for parallel builds, it's more convenient to begin _every_ error message with `"Error"` (or at least the message should contain that word).
 * Simplify the "fat binary" section for Linux; it doesn't make sense to call `uname -m` three times, nor does it to compare its result again if it already matched one of the tested. A `case`-`esac` would be appropriate, also merging the identical `i386` and `i686` then-branches. Btw, `uname -m` can also be `i486` or `i586` on 32-bit Linuces.
 * Is the `! [ $? -eq 0 ]` some required Cygwin "idiom"?

Also, `spkg-check` doesn't print any messages, and uses `make` instead of `$MAKE`.

The dependencies ("None") in `SPKG.txt` are wrong; MPIR at least depends on iconv, which Sage ships, though Sage's version is only used/built on some systems. I'm not sure if readline should be added to `spkg/standard/deps`. (MPIR's `configure` looks for much more, but apparently - as currently shipped - doesn't need/use all of that.) The Changelog could perhaps mention further changes, too.

If nobody else wants to, I could make the changes, i.e. a reviewer patch. Just let me know...

Going to test the new spkg with Sage 4.5.3.alpha2 and 4.6.prealpha3 (on Linuces only).


---

Comment by leif created at 2010-08-26 23:08:19

Dave, as it seems you're addicted to testing, you could also test _this_ new spkg (e.g. on Solaris, OpenSolaris)... ;-)


---

Comment by leif created at 2010-08-27 01:41:54

I guess unless we bump the patch levels of all packages that depend on GMP/MPIR (and ECM), this package breaks upgrading Sage (at least with the current upgrade process), due to interface change (in conjunction with shared library versioning).

The same applies to testing this package (and/with ECM 6.3 from #5847); one has to either build from scratch or delete `spkg/installed/<package-name>` for all packages that depend on those two.

Perhaps one could simply (conditionally) do the latter in `spkg/install`, which also gets updated during upgrade.


---

Comment by leif created at 2010-08-27 03:32:44

Defining `SAGE_SPKG` to `sage-spkg -f` in `spkg/standard/deps` should _in principle_ also work, but doesn't... apparently because _not really all_ shared libraries that use `libgmpxx.so` get rebuilt, so some still refer to the old, deleted `libgmpxx.so.3`.

----

Rebuilding Sage 4.5.3.alpha2 with MPIR 2.1.1 and ECM 6.3 _from scratch_ worked on Ubuntu 10.04 x86_64 (parallel build with 32 jobs); `ptestlong` passed all tests.


---

Comment by leif created at 2010-08-28 01:18:47

Replying to [comment:10 leif]:
> Defining `SAGE_SPKG` to `sage-spkg -f` in `spkg/standard/deps` should _in principle_ also work, but doesn't... apparently because _not really all_ shared libraries that use `libgmpxx.so` get rebuilt, so some still refer to the old, deleted `libgmpxx.so.3`.

I think this could be fixed by making extension modules also depend on (some of) the libraries they use (in `module_list.py`), with the disadvantage that these modules would get rebuilt whenever their libraries "change", even if the interfaces stay the same (and even if just the modification time changed due to a rebuild/reinstallation). 

----
 
> Rebuilding Sage 4.5.3.alpha2 with MPIR 2.1.1 and ECM 6.3 _from scratch_ worked on Ubuntu 10.04 x86_64 (parallel build with 32 jobs); `ptestlong` passed all tests.

Same for Fedora 13 x86 (parallel build with 6 jobs), also `ptestlong`.

----

Unfortunately, there seems to be some incompatibility between the new PARI (2.4.3.svn-12577.p4) or - more precisely - the required changes to Sage's interface to PARI in order to upgrade PARI (Sage 4.6.prealpha3, see #9343 and [the NewPARI Wiki page](http://wiki.sagemath.org/NewPARI)) and MPIR 2.1.1:

On Ubuntu 10.04 x86_64 (Core2, gcc 4.4.3) exactly two of all doctests (`ptestlong`) *segfault* (in `sage/schemes/elliptic_curves/ell_point.py`).

On Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4) the same two doctests and another one in `ell_rational_field.py` segfault, and in addition one doctest in the latter file raises an unexpected exception (`TypeError`), which seems to be the result of some other failure.

Maybe all are due to memory (or stack) corruption. See http://trac.sagemath.org/sage_trac/ticket/9343#comment:327 ff. for details; we haven't yet opened a separate ticket.

(For testing with Sage 4.6.prealpha3, I copied the MPIR 2.1.1 and ECM 6.3 spkgs to `spkg/standard`, and built Sage from scratch - without problems. I also reinstalled the PARI, MPIR and ECM packages later with `env SAGE_CHECK=yes ./sage -f ...`; all test suites passed.)


---

Comment by leif created at 2010-08-29 15:26:35

Replying to [comment:11 leif]:
> Unfortunately, there seems to be some incompatibility between the new PARI (2.4.3.svn-12577.p4 / Sage 4.6.prealpha3, see #9343 and [the NewPARI Wiki page](http://wiki.sagemath.org/NewPARI)) and MPIR 2.1.1:

> On Ubuntu 10.04 x86_64 (Core2, gcc 4.4.3) exactly two of all doctests (`ptestlong`) *segfault* (in `sage/schemes/elliptic_curves/ell_point.py`).

> On Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4) the same two doctests and another one in `ell_rational_field.py` segfault, and in addition one doctest in the latter file raises an unexpected exception (`TypeError`), which seems to be the result of some other failure.

This is due to the new PARI using undocumented features of GMP (that MPIR doesn't support). and is now addressed at #9837.


---

Comment by leif created at 2010-08-29 18:32:49

Replying to [comment:12 leif]:
> This is due to the new PARI using undocumented features of GMP (that MPIR doesn't support). and is now addressed at #9837.

This is not necessarily the (only) cause. Jeroen has found a definite bug in MPIR 2.1.1 he'll report upstream; see #9837.

Leaving the ticket "needs review", though I don't think we should upgrade MPIR until that bug is fixed, in a later release.


---

Comment by mhansen created at 2010-08-29 18:34:04

Replying to [comment:13 leif]:
> Leaving the ticket "needs review", though I don't think we should upgrade MPIR until that bug is fixed, in a later release.

Sounds good to me.


---

Comment by jdemeyer created at 2010-09-04 21:17:26

The problem of ticket #9837 has been fixed in MPIR svn, it was purely a bug in MPIR 2.1.1.


---

Comment by jdemeyer created at 2010-09-05 12:20:11

Please upgrade to MPIR 2.1.2, where #9837 is fixed.


---

Comment by jdemeyer created at 2010-09-05 12:20:11

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-09-05 17:11:01

Apparently [they've released MPIR 2.1.2](http://www.mpir.org/) with just this bug fixed today.

Haven't tested that yet.


---

Comment by leif created at 2010-09-05 18:55:41

Replying to [comment:18 leif]:
> Apparently [they've released MPIR 2.1.2](http://www.mpir.org/) with just this bug fixed today.
> 
> Haven't tested that yet.

At least passes all (long) tests in `sage/schemes/elliptic_curves/` with Sage 4.6.prealpha3 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4), where previously the segfaults occurred.

The diff shows they just fixed that single bug, bumped the MPIR version number (patch level) and incremented the revision numbers of both shared libraries. (In addition, they changed _the date of_ the documentation without actually changing the docs themselves. The file `src/.gdbinit` in the MPIR 2.1.1 spkg must have been added by Mike or someone else.)


---

Comment by leif created at 2010-09-06 09:57:17

FLINT also needs to be updated (from 1.5.0[.p5] to 1.5.2) to work with the new MPIR; otherwise the test suite won't build. See #9858.


---

Comment by mpatel created at 2010-09-30 10:24:51

Before the 4.6.alphaX build fails on the ia64 Skynet machines cleo and iras because of a bug in GCC 4.5.1 (see #9863), there's an apparent parallel `make install` failure with MPIR:

```
[...]
make[6]: Entering directory `/home/mpatel/build/cleo/sage-4.6.alpha2/spkg/build/
mpir-1.2.2.p1/src'
make[6]: warning: -jN forced in submake: disabling jobserver mode.
(cd /home/mpatel/build/cleo/sage-4.6.alpha2/local/include  && rm -f gmp.h   && c
p mpir.h   gmp.h)
 /usr/bin/install -c -m 644 'mpir.h' '/home/mpatel/build/cleo/sage-4.6.alpha2/lo
cal/include/mpir.h'
cp: cannot stat `mpir.h': No such file or directory
make[6]: *** [install-data-hook] Error 1
make[6]: Leaving directory `/home/mpatel/build/cleo/sage-4.6.alpha2/spkg/build/mpir-1.2.2.p1/src'
make[5]: *** [install-data-am] Error 2
make[5]: *** Waiting for unfinished jobs....
[...]
```

Has anyone else seen this?  The full logs are [here](http://sage.math.washington.edu/home/mpatel/trac/8664/).

I noticed that [MPIR 2.1.3 is out](http://www.mpir.org/) with a fix in `mpf_get_d_2exp`.  But I don't think Sage uses (m)any of the `mpf_*` functions.


---

Comment by mpatel created at 2010-10-22 01:05:22

Replying to [comment:22 mpatel]:
> Before the 4.6.alphaX build fails on the ia64 Skynet machines cleo and iras because of a bug in GCC 4.5.1 (see #9863), there's an apparent parallel `make install` failure with MPIR:

I've also [seen this on Skynet's menas](http://build.sagemath.org/sage/builders/menas%20full/builds/39/steps/shell_1/logs/mpir).


---

Comment by leif created at 2010-10-22 07:34:51

Replying to [comment:22 mpatel]:
> Before the 4.6.alphaX build fails on the ia64 Skynet machines cleo and iras because of a bug in GCC 4.5.1 (see #9863), there's an apparent parallel `make install` failure with MPIR:

```
[...]
make[6]: Entering directory `/home/mpatel/build/cleo/sage-4.6.alpha2/spkg/build/
mpir-1.2.2.p1/src'
make[6]: warning: -jN forced in submake: disabling jobserver mode.
(cd /home/mpatel/build/cleo/sage-4.6.alpha2/local/include  && rm -f gmp.h   && cp mpir.h   gmp.h)
/usr/bin/install -c -m 644 'mpir.h' '/home/mpatel/build/cleo/sage-4.6.alpha2/local/include/mpir.h'
cp: cannot stat `mpir.h': No such file or directory
make[6]: *** [install-data-hook] Error 1
make[6]: Leaving directory `/home/mpatel/build/cleo/sage-4.6.alpha2/spkg/build/mpir-1.2.2.p1/src'
make[5]: *** [install-data-am] Error 2
make[5]: *** Waiting for unfinished jobs....
[...]
```

> Has anyone else seen this? 

Sorry for the delay; I frequently see this since a while on Ubuntus (9.04 & 10.04) when building Sage with e.g. 16 or 32 jobs, with the *old* MPIR, too; also reported elsewhere (but incidentally also first saw this with MPIR 2.1.1 and the new PARI).

I cannot find obvious errors in the Makefile though; the relevant parts are identical to those of GMP btw, IIRC.

As another incident, I ran into this race condition again yesterday when building Sage 4.4.4 (!) from scratch with `MAKE="make -j16"`.


---

Comment by leif created at 2010-10-22 07:51:25

W.r.t. the race condition, cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:324

(I currently don't recall if I reported this elsewhere, or my results of inspecting the Makefile... :( )


---

Comment by mpatel created at 2010-11-03 22:50:22

Replying to [comment:22 mpatel]:
> I noticed that [MPIR 2.1.3 is out](http://www.mpir.org/) with a fix in `mpf_get_d_2exp`.  But I don't think Sage uses (m)any of the `mpf_*` functions.

That last statement is *_wrong*_.  Bill Hart corrects me on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b40ef1bc8b0b7371/bdb322e7528a06bf#bdb322e7528a06bf):

```
cddlib, ecl, mpmath, mpfr, singular, sympy all, as far as I can see, make extensive use of mpf functions.
```

Sorry about my mistake!


---

Comment by leif created at 2010-11-03 23:39:21

I would have taken the latest version anyway...

----

A trivial fix for the executable stack issue is to add the following to `spkg-install`:

```sh
case "$UNAME" in
    Linux) # implies a GNU linker
        LDFLAGS="$LDFLAGS -Wl,z,noexecstack"
        # already exported by sage-env
        ;;
    # perhaps other platforms, too
esac
```



---

Comment by leif created at 2010-11-04 02:08:44

Copy and paste with typos included... It should of course be `-Wl,-z,noexecstack`.


---

Comment by leif created at 2010-11-04 06:45:18

Changing keywords from "" to "GMP ECM execstack Fedora 14".


---

Comment by leif created at 2010-11-04 06:45:18

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-11-04 06:45:18

*New spkg: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p0.spkg*

*md5sum:* `f65cbb309ee471d2a64f59e52e592494  mpir-2.1.3.p0.spkg`

New spkg with updated upstream, "reviewer" changes, fix for Fedora 14 (based on Mike's 2.1.1 spkg).

Setting this to needs review though we still need a patch to the Sage library to fix the extension module dependencies. Can be tested "stand-alone" (with `SAGE_CHECK=yes`), but should be installed together with the new ECM 6.3 spkg from #5847 (also needing review by a third person), since otherwise ECM doesn't build (i.e., the old version doesn't work with GMP 5.x or MPIR 2.x).

Steps to install:
 * Download the new MPIR spkg and the [ecm-6.3.p0.spkg](http://spkg-upload.googlecode.com/files/ecm-6.3.p0.spkg) from #5847.
 * Copy both files into `$SAGE_ROOT/spkg/standard` (such that 'make' will "see" them).
 * Then do:

```sh
$ export SAGE_CHECK=yes                # optional, but recommended
$ export SAGE_UPGRADING=yes            # required to rebuild all dependent spkgs, too

$ export SAGE_PARALLEL_SPKG_BUILD=yes  # optional
$ export MAKE="make -jN"               # optional; N: number of 'make' jobs

$ time make build                      # just rebuild Sage (without the documentation)
$                                      # (logs go to install.log and spkg/logs/*)
$ ./sage -ba-force                     # rebuild the whole Sage library, necessary until
                                       # we fix the dependencies in module_list.py
$ time make ptestlong NUM_THREADS=N    # Use N threads instead of the default number
                                       # (also rebuilds the documentation as needed)
```

 * Report back... ;-)

(I've so far tested both packages with Sage 4.6.1.alpha0 on Ubuntu 9.04 x86 and Ubuntu 10.04 x86_64.)


---

Attachment

SPKG patch, based on Mike's 2.1.1. For reference/review.


---

Comment by leif created at 2010-11-04 07:05:06

Ooops, I just noticed the hint to rerun `make` if the *install* failed is in the wrong place (it is actually shown if the *build* failed), but that's IMHO a minor issue I'll perhaps fix later.


---

Comment by jdemeyer created at 2010-11-04 15:49:47

Built and tested on sage.math.washington.edu without problems.


---

Attachment

Sage library patch. Fixes extension modules not getting rebuilt though depending on MPIR. Based on Sage 4.6.1.alpha0.


---

Comment by leif created at 2010-11-04 20:24:17

Changing keywords from "GMP ECM execstack Fedora 14" to "GMP ECM execstack Fedora 14 extension module library dependencies".


---

Comment by leif created at 2010-11-04 20:24:17

Replying to [comment:29 leif]:
> Setting this to needs review though we still need a patch to the Sage library to fix the extension module dependencies. [...]

I've attached a patch that fixes the dependency issue with extension modules of the Sage library.


*Updated steps to test / install:*
 * Download the [new MPIR spkg](http://spkg-upload.googlecode.com/files/mpir-2.1.3.p0.spkg) and the [ecm-6.3.p0.spkg](http://spkg-upload.googlecode.com/files/ecm-6.3.p0.spkg) from #5847.
 * Copy both files into `$SAGE_ROOT/spkg/standard` (such that `make` will "see" them).
 * Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). *Do not yet apply the patch.* (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)
 * Then do:

```sh
$ export SAGE_CHECK=yes                # optional, but recommended
$ export SAGE_UPGRADING=yes            # required to rebuild all dependent spkgs, too

$ export SAGE_PARALLEL_SPKG_BUILD=yes  # optional
$ export MAKE="make -jN"               # optional; N: number of 'make' jobs

$ time make build                      # just rebuild Sage (without the documentation)
$                                      # (logs go to install.log and spkg/logs/*)
$ cd devel/sage
$ hg import /path/to/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch
$ cd ../..
$ ./sage -b                            # rebuild the Sage library; only dependent modules

$ time make ptestlong NUM_THREADS=N    # Use N threads instead of the default number
                                       # (also rebuilds the documentation as needed)
```

 * Report back... ;-)


---

Comment by leif created at 2010-11-04 20:27:14

Replying to [comment:32 jdemeyer]:

Don't mess with my ticket while I'm posting... ;-)

Can you (or did you) include the patch to the Sage library?


---

Comment by leif created at 2010-11-04 20:33:49

P.S.: My patch shouldn't conflict with #10094, only the line numbers will change.


---

Comment by jdemeyer created at 2010-11-04 20:36:37

Replying to [comment:33 leif]:
>  * Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). *Do not yet apply the patch.* (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)

Please explain.  When can `setup.py` be overwritten?  This patched-files-being-overwritten-thing has bitten me already several times.


---

Comment by leif created at 2010-11-04 20:51:10

Replying to [comment:36 jdemeyer]:
> Replying to [comment:33 leif]:
> >  * Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). *Do not yet apply the patch.* (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)
> 
> Please explain.  When can `setup.py` be overwritten?  This patched-files-being-overwritten-thing has bitten me already several times.

I can only cite from the Sage library's `spkg-install`: ;-)

```python
...
    sage -sync-build

    # Pull in changes from the archive just downloaded. 
    hg pull "$CUR"
    hg merge tip
    hg ci -m "merge"
    # Make the pulled in changes take effect. 
    hg update 
...
```


`sage -sync-build` calls `local/bin/sage-sync-build.py`.


---

Comment by leif created at 2010-11-04 21:07:18

Replying to [comment:38 leif]:
> I can only cite from the Sage library's `spkg-install`: ;-)

_"In principle"_<sup>TM</sup>, this shouldn't invalidate newer patches already applied (and committed) to the Sage library.


---

Comment by jdemeyer created at 2010-11-04 22:50:08

Replying to [comment:34 leif]:
> Can you include the patch to the Sage library?

Now it should be also merged, same spkg file.


---

Comment by mpatel created at 2010-11-04 23:02:24

Does the problem in [comment:22 comment 22] occur during `$MAKE install`?


---

Comment by jdemeyer created at 2010-11-04 23:07:02

Replying to [comment:41 mpatel]:
> Does the problem in [comment:22 comment 22] occur during `$MAKE install`?

I have not encountered this problem (yet), I've built on `sage.math.washington.edu` without problems.

If you feel like it, you could put [http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.1.alpha0-mpir/sage-4.6.1.alpha0-mpir.tar](http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.1.alpha0-mpir/sage-4.6.1.alpha0-mpir.tar) on the buildbots and see what happens...


---

Comment by leif created at 2010-11-05 00:17:55

Replying to [comment:41 mpatel]:
> Does the problem in [comment:22 comment 22] occur during `$MAKE install`?


```sh
(cd /home/mpatel/build/cleo/sage-4.6.alpha2/local/include  && rm -f gmp.h   && cp mpir.h   gmp.h)
/usr/bin/install -c -m 644 'mpir.h' '/home/mpatel/build/cleo/sage-4.6.alpha2/local/include/mpir.h'
```


Smells like it does, doesn't it? ;-)

Or did I misunderstand you? (As mentioned in a comment above, the hint to rerun `make` is given in the wrong situation.)


```diff
diff --git a/spkg-install b/spkg-install
--- a/spkg-install
+++ b/spkg-install
`@``@` -123,18 +123,6 `@``@`
     $MAKE
     if [ $? -ne 0 ]; then
         echo "Error building MPIR."
-        echo ""
-        echo "If you see a message like:"
-        cat <<EOF
-    cp: cannot stat 'mpir.h': No such file or directory
-    make[6]: *** [install-data-hook] Error 1
-    make[6]: Leaving directory ...
-    make[5]: *** [install-data-am] Error 2
-    make[5]: *** Waiting for unfinished jobs....
-EOF
-        echo "above, this is just due to a rare race condition."
-        echo "Please simply rerun 'make' (or 'sage -i ...')."
-        echo ""
         exit 1
     fi 
 
`@``@` -146,6 +134,18 `@``@`
     if [ $? -ne 0 ]; then
         if [ "$UNAME" != "CYGWIN" ]; then  # On Cygwin an error is not fatal.
             echo "Error installing MPIR."
+            echo ""
+            echo "If you see a message like:"
+            cat <<EOF
+    cp: cannot stat 'mpir.h': No such file or directory
+    make[6]: *** [install-data-hook] Error 1
+    make[6]: Leaving directory ...
+    make[5]: *** [install-data-am] Error 2
+    make[5]: *** Waiting for unfinished jobs....
+EOF
+            echo "above, this is just due to a rare race condition."
+            echo "Please simply rerun 'make' (or 'sage -i ...')."
+            echo ""
             exit 1
         fi
     fi
```



---

Comment by mpatel created at 2010-11-05 00:30:05

Replying to [comment:43 leif]:
> Replying to [comment:41 mpatel]:
> Or did I misunderstand you? (As mentioned in a comment above, the hint to rerun `make` is given in the wrong situation.)

Oooops, I missed [comment:30 your comment].  Thanks for pointing it out.


---

Comment by leif created at 2010-11-05 03:07:39

Any reason to keep

```sh
    SAGE_CONF_OPTS="--enable-shared --disable-static"
```

(i.e., why not build the static library, too)?


---

Comment by dimpase created at 2010-11-05 17:23:53

Replying to [comment:33 leif]:

I tried to build mpir-2.1.3.p0.spkg on MacOSX 10.5 PPC, and it did not work; 
sage -f mpir-2.1.3.p0.spkg bails out  with the following:

```
...
 gcc -std=gnu99 -c -DHAVE_CONFIG_H -g -O3 -D__GMP_WITHIN_GMP -I.. -DOPERATION_popcount -I. -I.. tmp-popcount.s -fno-common -DPIC -o .libs/popcount.o
tmp-popcount.s:127:vspltisb vector instruction is optional for the PowerPC (not allowed without -force_cpusubtype_ALL option)
tmp-popcount.s:128:vspltisb vector instruction is optional for the PowerPC (not allowed without -force_cpusubtype_ALL option)

... etc etc etc ...

tmp-popcount.s:239:stvx vector instruction is optional for the PowerPC (not allowed without -force_cpusubtype_ALL option)
make[2]: *** [popcount.lo] Error 1
make[1]: *** [all-recursive] Error 1
make: *** [all] Error 2
Error building MPIR.

```



---

Comment by dimpase created at 2010-11-05 17:23:53

Changing status from needs_review to needs_work.


---

Comment by leif created at 2010-11-05 19:06:50

Replying to [comment:47 dimpase]:
> Replying to [comment:33 leif]:
> 
> I tried to build mpir-2.1.3.p0.spkg on MacOSX 10.5 PPC, and it did not work; 
> sage -f mpir-2.1.3.p0.spkg bails out  with [...]

```
...
tmp-popcount.s:127:vspltisb vector instruction is optional for the PowerPC (not allowed without -force_cpusubtype_ALL option)
...
```


Thanks for testing this.

Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work? (Unless `SAGE_FAT_BINARY=yes`... Don't know what to do in that case, i.e. if `--enable-fat` works in that case, too.)

(I think PPC implies [32-bit] MacOS X 10.4 or 10.5 in Sage.)

Or do we have to make further distinctions on the CPU type?

For 32-bit *x86* builds on MacOS X < 10.6 we currently remove a lot of assembly files:

```sh
remove_pic_osx_32_bit()
{
    # Assumes we are in src/
    echo "Deleting assembly files which depend on PIC assembly" \
        "working or 32 bit OSX on Intel hardware..."
    rm mpn/x86/dive_1.asm 
    rm mpn/x86/diveby3.asm 
    rm mpn/x86/pentium4/sse2/dive_1.asm 
    rm mpn/x86/pentium4/sse2/mode1o.asm 
    rm mpn/x86/pentium4/sse2/diveby3.asm 
    rm mpn/x86/pentium4/mmx/popham.asm 
    rm mpn/x86/pentium4/mmx/rshift.asm
    rm mpn/x86/p6/mode1o.asm
    rm mpn/x86/p6/dive_1.asm
    rm mpn/x86/pentium/hamdist.asm
    rm mpn/x86/pentium/mod_1.asm
    rm mpn/x86/pentium/popcount.asm
    rm mpn/x86/pentium/mode1o.asm
    rm mpn/x86/pentium/dive_1.asm
}
```


We should report this upstream. Bill, can you forward this?


---

Comment by leif created at 2010-11-05 19:15:14

Replying to [comment:48 leif]:
> Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?

I.e.

```sh
$ env CFLAGS="-Wa,-force_cpusubtype_ALL" ./sage -f mpir-2.1.3.p0.spkg
```


Even if this works for you, I'm not sure if MPIR only enables that code on CPUs that really support these instructions. Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.


---

Comment by dimpase created at 2010-11-05 20:06:22

Replying to [comment:49 leif]:
> Replying to [comment:48 leif]:
> > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?
> 
> 
> Even if this works for you, I'm not sure if MPIR only enables that code on CPUs that really support these instructions. Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.

yes, it at least builds without errors this way, on MacOSX 10.5 G4 PPC, with gcc 4.2.1 (Apple Inc. build 5577).
Tell me what I should test. (I don't want to rerun the whole Sage testsuite, as it takes ages on this machine, and I use it otherwise too)


---

Comment by jdemeyer created at 2010-11-05 20:29:55

Replying to [comment:49 leif]:
> Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.
Yes, I did.  If it helps, I've put the log at [http://sage.math.washington.edu/home/jdemeyer/moufang/mpir-2.1.3.p0.log](http://sage.math.washington.edu/home/jdemeyer/moufang/mpir-2.1.3.p0.log).


---

Comment by leif created at 2010-11-05 21:31:18

Replying to [comment:50 dimpase]:
> Replying to [comment:49 leif]:
> > Replying to [comment:48 leif]:
> > > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?
> > 
> > 
> > Even if this works for you, I'm not sure if MPIR only enables that code on CPUs that really support these instructions. Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.
> 
> yes, it at least builds without errors this way, on MacOSX 10.5 G4 PPC, with gcc 4.2.1 (Apple Inc. build 5577).
> Tell me what I should test. (I don't want to rerun the whole Sage testsuite, as it takes ages on this machine, and I use it otherwise too)

Nice, thanks.

Did you run MPIR's test suite (i.e., installed with `SAGE_CHECK=yes`)?

I'll update the ECM package (#5847) with the upstream patch, then you could also test this.

I don't know if you already broke your Sage installation by now having successfully installed the new MPIR, since we delete all older versions, which other parts of Sage will still try to use unless you also rebuild the dependent packages.

You can of course always force the reinstallation of the old MPIR (and ECM) package with `sage -f ...`, then Sage will again work as before.


---

Comment by leif created at 2010-11-05 21:41:34

Replying to [comment:52 leif]:
> Replying to [comment:50 dimpase]:
> > Replying to [comment:49 leif]:
> > > Replying to [comment:48 leif]:
> > > > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?

P.S.: Does Apple's XCode `gcc` understand `-force_cpusubtype_ALL` (i.e., without `-Wa,`)?

I just noticed at least recent "originals" do on Darwin, but it's perhaps safer to directly pass it to the assembler.

Still need to now what happens on _Linux_ PPC (with `gas`)...


---

Comment by leif created at 2010-11-06 02:04:01

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-11-06 02:04:01

*New spkg with Darwin fixes: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p1.spkg*

*md5sum:* `0f13106ed6c8af933f93fa4a8981c453  mpir-2.1.3.p1.spkg`

I've uploaded a new p1 spkg that fixes the assembler error on Darwin PPC. [Attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) reflects changes between this and the previous one (p0). Use [this link](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) to _download or apply_ the patch.

----

### mpir-2.1.3.p1 (Leif Leonhardy, November 5th, 2010)
 * #8664: Upgrade Sage's MPIR spkg to version 2.1.3
 * Fix Darwin assembler errors on PPC by passing the option to allow
   use of extended instruction set to it. (See also #5847.)
 * Enable the build of a static MPIR library, to be e.g. used by ECM.
 * Support additional 'configure' options given by MPIR_EXTRA_OPTS,
   and print messages how we configure.
 * Print various environment variable settings (CC, CFLAGS et al.).
 * Move hint to rerun 'make' on *install* errors to correct place.
 * Further comments added.


---

Comment by leif created at 2010-11-06 02:11:58

P.S.: Except for the filename, test / installation instructions remain the same. (See [above](http://trac.sagemath.org/sage_trac/ticket/8664#comment:33).)


---

Comment by dimpase created at 2010-11-06 04:46:56

Replying to [comment:54 leif]:
> *New spkg with Darwin fixes: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p1.spkg*
> 
> *md5sum:* `0f13106ed6c8af933f93fa4a8981c453  mpir-2.1.3.p1.spkg`
> 
> I've uploaded a new p1 spkg that fixes the assembler error on Darwin PPC. [Attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) reflects changes between this and the previous one (p0). Use [this link](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) to _download or apply_ the patch.

This won't work just like this. Ineed: 

```
$ uname -m                  
Power Macintosh
$ uname -a                
Darwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh
```


so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...


---

Comment by dimpase created at 2010-11-06 04:46:56

Changing status from needs_review to needs_work.


---

Comment by dimpase created at 2010-11-06 04:55:15

Replying to [comment:52 leif]:
> Replying to [comment:50 dimpase]:
> > Replying to [comment:49 leif]:
> > > Replying to [comment:48 leif]:
> > > > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?
> > > 
> > > 
> > > Even if this works for you, I'm not sure if MPIR only enables that code on CPUs that really support these instructions. Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.
> > 
> > yes, it at least builds without errors this way, on MacOSX 10.5 G4 PPC, with gcc 4.2.1 (Apple Inc. build 5577).
> > Tell me what I should test. (I don't want to rerun the whole Sage testsuite, as it takes ages on this machine, and I use it otherwise too)
> 
> Nice, thanks.
> 
> Did you run MPIR's test suite (i.e., installed with `SAGE_CHECK=yes`)?

I just re-run the installation of p0 with SAGE_CHECK=yes, and all the tests passed.
So I suppose it's very close, only that small config fix remains...


> 
> I'll update the ECM package (#5847) with the upstream patch, then you could also test this.
> 
> I don't know if you already broke your Sage installation by now having successfully installed the new MPIR, since we delete all older versions, which other parts of Sage will still try to use unless you also rebuild the dependent packages.
> 
> You can of course always force the reinstallation of the old MPIR (and ECM) package with `sage -f ...`, then Sage will again work as before.

Thanks for the reminder, but I am quite familiar with sage -f, spkg-install,  etc etc... I am involved in maintaining of *gap*.spkg and cvxopt*.spkg...


---

Comment by leif created at 2010-11-06 05:25:27

Replying to [comment:56 dimpase]:
> This won't work just like this. Ineed: 

```
$ uname -m                  
Power Macintosh
$ uname -a                
Darwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh
```

> 
> so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...

WTF? _Which_ `uname`? Some Apple XXXX?

I've never seen _any_ `configure` or `config.guess` script testing for "Power Macintosh", since this is neither a CPU nor an architecture. (The space is nice, too.)

I'll make a special case for your machine... ;-)

[Ok, I've searched now and the only one I've found is Singular's. Some others test for `Power*`.]


---

Comment by leif created at 2010-11-06 05:40:47

Replying to [comment:57 dimpase]:
> Replying to [comment:52 leif]:
> > I don't know if you already broke your Sage installation by now having successfully installed the new MPIR, since we delete all older versions, which other parts of Sage will still try to use unless you also rebuild the dependent packages.
> > 
> > You can of course always force the reinstallation of the old MPIR (and ECM) package with `sage -f ...`, then Sage will again work as before.
> 
> Thanks for the reminder, but I am quite familiar with sage -f, spkg-install,  etc etc... I am involved in maintaining of *gap*.spkg and cvxopt*.spkg...

:-) Certainly, just ignore... (cf.[this nice comment](http://trac.sagemath.org/sage_trac/ticket/9921#comment:7))

But there are other people less familiar with this. (In fact this is a slightly modified copy of what I mailed someone else. I then became aware of not having it mentioned here at all.)


---

Comment by dimpase created at 2010-11-06 05:44:31

Replying to [comment:58 leif]:


> > so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...
> 
> WTF? _Which_ `uname`? Some Apple XXXX?

What a Terrible Failure indeed:

/usr/bin/uname

The choice  "Power Macintosh" is undoubtedly the result of an out of court settlement between IBM and Apple :-)


---

Comment by dimpase created at 2010-11-06 06:27:35

Replying to [comment:53 leif]:
> Replying to [comment:52 leif]:
> > Replying to [comment:50 dimpase]:
> > > Replying to [comment:49 leif]:
> > > > Replying to [comment:48 leif]:
> > > > > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?
> 
> P.S.: Does Apple's XCode `gcc` understand `-force_cpusubtype_ALL` (i.e., without `-Wa,`)?

yes Apple's gcc 4.2.1 does. As well as gcc-4.0.1, which is probably more usual on OSX PPC...


---

Comment by leif created at 2010-11-06 06:28:30

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-11-06 06:28:30

*Updated p1 spkg: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p1.spkg (same place)*

*md5sum:* `08dfaa24301ba4e4481cfbbbc77156b3  mpir-2.1.3.p1.spkg`

Now also recognizes PPCs giving "`Power*`" as `uname -m`.


---

Comment by leif created at 2010-11-06 06:40:12

Replying to [comment:60 dimpase]:
> Replying to [comment:58 leif]:
> 
> 
> > > so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...
> > 
> > WTF? _Which_ `uname`? Some Apple XXXX?
> 
> What a Terrible Failure indeed:
> 
> /usr/bin/uname

What do `/bin/uname` and `/usr/local/bin/uname` give? 

(Consider installing GNU coreutils, and / or perhaps changing the `PATH`... ;-) )

There are other packages in Sage that won't recognize "Power Macintosh".


> The choice  "Power Macintosh" is undoubtedly the result of an out of court settlement between IBM and Apple :-)

Well, POWER<sup>TM</sup> is IBMs; the PowerPC was a later joint venture of Apple, IBM and Motorola.


---

Attachment

SPKG patch. Apply to MPIR 2.1.3.p0 to get the p1. Fixes Darwin assembler error, corrects hint; some improvements.


---

Comment by dimpase created at 2010-11-06 07:06:58

Replying to [comment:63 leif]:
> Replying to [comment:60 dimpase]:
> > Replying to [comment:58 leif]:
> > 
> > 
> > > > so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...
> > > 
> > > WTF? _Which_ `uname`? Some Apple XXXX?
> > 
> > What a Terrible Failure indeed:
> > 
> > /usr/bin/uname
> 
> What do `/bin/uname` and `/usr/local/bin/uname` give? 
> 
> (Consider installing GNU coreutils, and / or perhaps changing the `PATH`... ;-) )

GNU's uname says:

```
$ /usr/local/bin/uname -m
Power Macintosh
$ /usr/local/bin/uname -a
Darwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh powerpc PowerBook5,5 Darwin
```


> 
> There are other packages in Sage that won't recognize "Power Macintosh".
> 
> 
> > The choice  "Power Macintosh" is undoubtedly the result of an out of court settlement between IBM and Apple :-)
> 
> Well, POWER<sup>TM</sup> is IBMs; the PowerPC was a later joint venture of Apple, IBM and Motorola.


---

Comment by leif created at 2010-11-06 07:28:39

Replying to [comment:64 dimpase]:
> GNU's uname says:

```
$ /usr/local/bin/uname -m
Power Macintosh
$ /usr/local/bin/uname -a
Darwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh powerpc PowerBook5,5 Darwin
```


Report upstream... ;-)

I should have added `[Pp]ower*` :/


---

Comment by dimpase created at 2010-11-06 07:33:22

p1 builds and passes all tests on OSX 10.5 PPC (G4), with gcc-4.2.1.
Except that somewhere in the log I see:

```
...
make[4]: Entering directory `/usr/local/src/sage/sage-4.6/spkg/build/mpir-2.1.3.p1/src/tests/cxx'
...
PASS: t-istream
Replacing decimal point didn't work, tests skipped
PASS: t-locale
...
 }}}
This does not happen on Debian x64.
Probably a harmless (for Sage) C++-specific issue. Can this be ignored?


---

Comment by dimpase created at 2010-11-06 07:33:22

Changing status from needs_review to needs_info.


---

Comment by dimpase created at 2010-11-06 07:48:59

however, Sage does not start on OSX 10.5 PPC: I get 

```
$ ./sage -b
...
g++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/usr/local/src/sage/sage-4.6/local/lib -L/usr/local/src/sage/sage-4.6/local/lib/python/config -lntl -lgmp -lpari -lpython2.6
ld: file not found: /usr/local/src/sage/sage-4.6/local/lib/libgmp.3.dylib
collect2: ld returned 1 exit status
scons: *** [libcsage.dylib] Error 1
ERROR: There was an error building c_lib.
```

I don't know whether this is a result of this spkg upgrade, or something else was broken even before. I'll see.


---

Comment by leif created at 2010-11-06 08:57:45

Replying to [comment:67 dimpase]:
> however, Sage does not start on OSX 10.5 PPC: I get 

```
$ ./sage -b
...
g++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/usr/local/src/sage/sage-4.6/local/lib -L/usr/local/src/sage/sage-4.6/local/lib/python/config -lntl -lgmp -lpari -lpython2.6
ld: file not found: /usr/local/src/sage/sage-4.6/local/lib/libgmp.3.dylib
collect2: ld returned 1 exit status
scons: *** [libcsage.dylib] Error 1
ERROR: There was an error building c_lib.
```

> I don't know whether this is a result of this spkg upgrade, or something else was broken even before. I'll see.

Did you rebuild all dependent packages, i.e. use `SAGE_UPGRADING=yes`?

What MPIR versions do you have in `local/lib/`?

----

I guess the locale issue is a minor thing (hopefully). Perhaps Bill knows better.

(I almost always build with `LC_ALL=C`.)


---

Comment by leif created at 2010-11-06 09:02:22

P.S.: Could you attach the full MPIR build log, or its `make install` part?


---

Comment by dimpase created at 2010-11-06 11:49:58

Replying to [comment:68 leif]:


> Did you rebuild all dependent packages, i.e. use `SAGE_UPGRADING=yes`?

I tried

```
$ SAGE_UPGRADING=yes ../../sage -f mpir-2.1.3.p1.spkg
$ ../../sage -b
```

with the same outcome. 
Installing the version 1.* mpir spkg cures the installation, i.e. I get a working copy of Sage back.

> 
> What MPIR versions do you have in `local/lib/`?

here are mpirs and gmps I have:
 

```
-rwxr-xr-x  1 dima  wheel   500140 Nov  6 18:48 ../../local/lib/libmpir.8.2.3.dylib
lrwxr-xr-x  1 dima  wheel       19 Nov  6 18:48 ../../local/lib/libmpir.8.dylib -> libmpir.8.2.3.dylib
-rw-r--r--  1 dima  wheel  2487088 Nov  6 18:48 ../../local/lib/libmpir.a
lrwxr-xr-x  1 dima  wheel       19 Nov  6 18:48 ../../local/lib/libmpir.dylib -> libmpir.8.2.3.dylib
-rwxr-xr-x  1 dima  wheel      829 Nov  6 18:48 ../../local/lib/libmpir.la
-rwxr-xr-x  1 dima  wheel    25592 Nov  6 18:48 ../../local/lib/libmpirxx.2.2.11.dylib
lrwxr-xr-x  1 dima  wheel       22 Nov  6 18:48 ../../local/lib/libmpirxx.2.dylib -> libmpirxx.2.2.11.dylib
-rw-r--r--  1 dima  wheel   699424 Nov  6 18:48 ../../local/lib/libmpirxx.a
lrwxr-xr-x  1 dima  wheel       22 Nov  6 18:48 ../../local/lib/libmpirxx.dylib -> libmpirxx.2.2.11.dylib
-rwxr-xr-x  1 dima  wheel      894 Nov  6 18:48 ../../local/lib/libmpirxx.la

-rwxr-xr-x  1 dima  wheel   500140 Nov  6 18:48 ../../local/lib/libgmp.8.2.3.dylib
lrwxr-xr-x  1 dima  wheel       18 Nov  6 18:48 ../../local/lib/libgmp.8.dylib -> libgmp.8.2.3.dylib
-rw-r--r--  1 dima  wheel  2487088 Nov  6 18:48 ../../local/lib/libgmp.a
lrwxr-xr-x  1 dima  wheel       18 Nov  6 18:48 ../../local/lib/libgmp.dylib -> libgmp.8.2.3.dylib
-rwxr-xr-x  1 dima  wheel      822 Nov  6 18:48 ../../local/lib/libgmp.la
-rwxr-xr-x  1 dima  wheel    25592 Nov  6 18:48 ../../local/lib/libgmpxx.2.2.11.dylib
lrwxr-xr-x  1 dima  wheel       21 Nov  6 18:48 ../../local/lib/libgmpxx.2.dylib -> libgmpxx.2.2.11.dylib
-rw-r--r--  1 dima  wheel   699424 Nov  6 18:48 ../../local/lib/libgmpxx.a
lrwxr-xr-x  1 dima  wheel       21 Nov  6 18:48 ../../local/lib/libgmpxx.dylib -> libgmpxx.2.2.11.dylib
-rwxr-xr-x  1 dima  wheel      886 Nov  6 18:48 ../../local/lib/libgmpxx.la
```


I'm  trying the following:

```
$ cd local/lib
$ ln -s libgmp.dylib libgmp.3.dylib
$ ../../sage -b 
```

and this seems to work (triggering a large recompile of extensions that still is running)


---

Comment by leif created at 2010-11-06 16:27:21

Replying to [comment:70 dimpase]:
> Replying to [comment:68 leif]:
> > Did you rebuild all dependent packages, i.e. use `SAGE_UPGRADING=yes`? 
> I tried

```
$ SAGE_UPGRADING=yes ../../sage -f mpir-2.1.3.p1.spkg
$ ../../sage -b
```

> with the same outcome.

`SAGE_UPGRADING=yes` only works with `make`, not `sage -i ...` etc. (and only if all [new] spkgs are in `spkg/standard/`).





> Installing the version 1.* mpir spkg cures the installation, i.e. I get a working copy of Sage back.

Yep.




> > What MPIR versions do you have in `local/lib/`?
> 
> here are mpirs and gmps I have:

```
-rwxr-xr-x  1 dima  wheel   500140 Nov  6 18:48 ../../local/lib/libmpir.8.2.3.dylib
lrwxr-xr-x  1 dima  wheel       19 Nov  6 18:48 ../../local/lib/libmpir.8.dylib -> libmpir.8.2.3.dylib
-rw-r--r--  1 dima  wheel  2487088 Nov  6 18:48 ../../local/lib/libmpir.a
lrwxr-xr-x  1 dima  wheel       19 Nov  6 18:48 ../../local/lib/libmpir.dylib -> libmpir.8.2.3.dylib
-rwxr-xr-x  1 dima  wheel      829 Nov  6 18:48 ../../local/lib/libmpir.la
-rwxr-xr-x  1 dima  wheel    25592 Nov  6 18:48 ../../local/lib/libmpirxx.2.2.11.dylib
lrwxr-xr-x  1 dima  wheel       22 Nov  6 18:48 ../../local/lib/libmpirxx.2.dylib -> libmpirxx.2.2.11.dylib
-rw-r--r--  1 dima  wheel   699424 Nov  6 18:48 ../../local/lib/libmpirxx.a
lrwxr-xr-x  1 dima  wheel       22 Nov  6 18:48 ../../local/lib/libmpirxx.dylib -> libmpirxx.2.2.11.dylib
-rwxr-xr-x  1 dima  wheel      894 Nov  6 18:48 ../../local/lib/libmpirxx.la
...
```

These are the correct new ones, same basenames as on other systems. (Note that the version number of `libgmpxx*` is now _smaller_ than in MPIR 1.2.2, which was `3[.1.6]`.)




 
> I'm  trying the following:

```
$ cd local/lib
$ ln -s libgmp.dylib libgmp.3.dylib
$ ../../sage -b 
```

> and this seems to work (triggering a large recompile of extensions that still is running)

So the patch to the Sage library apparently works for you. :)

----

The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.

Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?
(Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be _below_ MPIR's.)


---

Comment by dimpase created at 2010-11-06 17:01:07

Replying to [comment:71 leif]:

> The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.
> 
> Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?
> (Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be _below_ MPIR's.)

Is ecm-6.2.1 compatible with  mpir 2.1.3?
Just wondering.

I'm going to rebuild Sage from scratch and with mpir 2.1.3.
It will take a night, but it's already pretty later over here.


---

Comment by leif created at 2010-11-06 17:54:03

Replying to [comment:72 dimpase]:
> Replying to [comment:71 leif]:
> 
> > The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.
> > 
> > Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?
> > (Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be _below_ MPIR's.)
> 
> Is ecm-6.2.1 compatible with  mpir 2.1.3?

Rather not. (See #5847.)


> I'm going to rebuild Sage from scratch and with mpir 2.1.3.
> It will take a night, but it's already pretty later over here.

You could try faking ecm-6.3.p0.spkg (or the old one if you haven't copied the new spkg) was already installed, then at least the build should pass.


---

Comment by mpatel created at 2010-11-06 20:22:06

I asked Bill by email about Leif's comments above.  Please see [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/892ce7f3c9c93b9f).


---

Comment by dimpase created at 2010-11-07 04:45:25

Replying to [comment:74 mpatel]:
> I asked Bill by email about Leif's comments above.  Please see [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/892ce7f3c9c93b9f).

I tried a vanilla build from the source, i.e. untarred the spkg, then

```
$ cd src/
$ ./configure
$ make
```

and it just works, picking up the flag -force_cpusubtype_ALL without any help.


---

Comment by dimpase created at 2010-11-09 05:07:45

Replying to [comment:72 dimpase]:
> Replying to [comment:71 leif]:
> 
> > The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.
> > 
> > Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?
> > (Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be _below_ MPIR's.)
> 
> Is ecm-6.2.1 compatible with  mpir 2.1.3?
> Just wondering.
> 
> I'm going to rebuild Sage from scratch and with mpir 2.1.3.
> It will take a night, but it's already pretty later over here.
> 

rebuilt Sage 4.6 from scratch with p1 spk of this ticket, the Sage library patch of this ticket applied to sage spkg, and with tweaked ECM spkg (see the ECM ticket). All works, as well as passes testlong (>12 hours on this machine).

Dima

It all worked, as well as all


---

Comment by dimpase created at 2010-11-09 05:07:45

Changing status from needs_info to needs_review.


---

Comment by dimpase created at 2010-11-09 05:08:55

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-09 08:35:31

Replying to [comment:76 dimpase]:
> and with tweaked ECM spkg (see #5847).

Which "tweaked" ECM spkg do you mean?


---

Comment by dimpase created at 2010-11-09 09:41:49

Replying to [comment:79 jdemeyer]:
> Replying to [comment:76 dimpase]:
> > and with tweaked ECM spkg (see #5847).
> 
> Which "tweaked" ECM spkg do you mean?

The one I made from the spkg on the ticket that 1) avoids the linker crash by supplying a longer assembler program in configure 2) runs ./configure --disable-asm-redc in spkg-install.

I did not yet try the configure patch suggested by Paul:

```
in fact this bug is already fixed upstream (in revision 1516), see
  https://gforge.inria.fr/tracker/index.php func=detail&aid=10646&group_id=135&atid=623
```



---

Comment by jdemeyer created at 2010-11-11 13:02:02

Resolution: fixed


---

Comment by jdemeyer created at 2010-11-12 13:07:10

Changing status from closed to new.


---

Comment by jdemeyer created at 2010-11-12 13:07:10

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2010-11-12 13:07:20

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-11-12 13:07:28

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-12 13:08:18

Unmerged from sage-4.6.1.alpha1 because of the problems with the ECM package, see #10252.


---

Comment by mpatel created at 2010-11-26 13:01:53

Replying to [comment:25 leif]:
> W.r.t. the race condition, cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:324
> 
> (I currently don't recall if I reported this elsewhere, or my results of inspecting the Makefile... :( )

I've reported the parallel `make install` error on [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/04928454886f34ab/e29bf19c2590d2d0?#e29bf19c2590d2d0).


---

Comment by leif created at 2010-11-26 13:21:49

Replying to [comment:88 mpatel]:
> Replying to [comment:25 leif]:
> > W.r.t. the race condition, cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:324
> > 
> > (I currently don't recall if I reported this elsewhere, or my results of inspecting the Makefile... :( )
> 
> I've reported the parallel `make install` error on [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/04928454886f34ab/e29bf19c2590d2d0?#e29bf19c2590d2d0).

Just yesterday ran into this for the first time on an old 32-bit single-core HT Pentium 4 (with 8 jobs); I previously only encountered it on Core2s with e.g. 16 or 32 jobs.


---

Comment by leif created at 2010-12-01 20:46:21

Replying to [comment:89 leif]:
> Replying to [comment:88 mpatel]:
> > I've reported the parallel `make install` error on [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/04928454886f34ab/e29bf19c2590d2d0?#e29bf19c2590d2d0).
> 
> Just yesterday ran into this for the first time on an old 32-bit single-core HT Pentium 4 (with 8 jobs); I previously only encountered it on Core2s with e.g. 16 or 32 jobs.

This has now been fixed in MPIR 2.1.4 (released today), but I'm not going to make any further changes _on this ticket_.

(I'll open a follow-up ticket anyway, since I already have an MPIR 2.1.3.p2 spkg with other improvements; MPIR 2.2 is on the way, too.)


---

Comment by leif created at 2010-12-02 18:04:23

Replying to [comment:90 leif]:
> This has now been fixed in MPIR 2.1.4 (released today), but I'm not going to make any further changes _on this ticket_.

> 
> (I'll open a follow-up ticket anyway, since I already have an MPIR 2.1.3.p2 spkg with other improvements; MPIR 2.2 is on the way, too.)

MPIR 2.2.0 was released today... ;-)


---

Comment by leif created at 2010-12-04 23:27:22

Replying to [comment:36 jdemeyer]:
> Replying to [comment:33 leif]:
> >  * Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). *Do not yet apply the patch.* (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)
> 
> Please explain.  When can `setup.py` be overwritten?  This patched-files-being-overwritten-thing has bitten me already several times.

A problem with `SAGE_UPGRADING` (whose "external" use is inofficial anyway) is that if the Sage library gets reinstalled because some of its dependencies got rebuilt (which is the typical case), Sage unconditionally switches back to the `main` branch without any warning, so previously applied patches to a clone take no longer effect (though they are still there, but no longer in the afterwards current branch, `sage-main`). It took me some time to realize that (or in fact track down weird errors caused by this)... ;-)

The Sage library's `spkg-install` should at least issue a warning when it switches the current branch; perhaps there should be some option to avoid this, since it is IMHO convenient to do e.g. `env SAGE_UPGRADING=yes make ptestlong` rather than patching the `main` branch or first building a new source distribution to build from scratch (or a new patched Sage library spkg to be installed).


---

Comment by jdemeyer created at 2011-01-12 19:06:30

The old mpir spkg compiles with -march=<...>, the new spkg here doesn't do that.  That is definately a bug.


---

Comment by jdemeyer created at 2011-01-12 19:06:30

Changing status from positive_review to needs_work.


---

Comment by dimpase created at 2011-01-12 19:24:24

Changing status from needs_work to needs_info.


---

Comment by dimpase created at 2011-01-12 19:24:24

Replying to [comment:94 jdemeyer]:
> The old mpir spkg compiles with -march=<...>, the new spkg here doesn't do that.  That is definately a bug.

isn't mpir's config intelligent enough to figure out the right arch?


---

Comment by jdemeyer created at 2011-01-12 20:01:34

Replying to [comment:95 dimpase]:
> isn't mpir's config intelligent enough to figure out the right arch?

Yes, but Sage's `CFLAGS` override `mpir`'s optimized `CFLAGS` (and this does not happen with the current mpir-1.2.2)


---

Comment by jdemeyer created at 2011-01-12 20:01:34

Changing status from needs_info to needs_work.


---

Comment by dimpase created at 2011-04-18 16:42:28

Replying to [comment:97 jdemeyer]:

as MPIR is at version 2.3.1 already, should all this be rebased?
(well, I don't know if it works with ECM 6.3...)

Dima


---

Comment by jdemeyer created at 2011-04-18 16:51:59

Probably, yes, it should be rebased.

But also the `CFLAGS` issue still needs to be fixed...


---

Comment by leif created at 2011-04-18 17:27:17

Replying to [comment:99 jdemeyer]:
> Probably, yes, it should be rebased.
> 
> But also the `CFLAGS` issue still needs to be fixed...

8S See [my comment above](http://trac.sagemath.org/sage_trac/ticket/8664#comment:90).

I still can't believe this ticket didn't get merged _month_ ago, just because (apparently) nobody felt able to give the ECM one (#5847) a final positive review.

The `CFLAGS` (or `-march=`) issue is IMHO completely unrelated -- if not irrelevant. ;-)

It's easy to extract and merge the _relevant_ parts of MPIR's `CFLAGS` without ignoring a user's settings, which I did in the follow-up spkg (IIRC), mentioned above.

I'll try to take a look at its state during the next days; I'm currently not even sure if I hadn't already uploaded it onto google code...

Cheers.


---

Comment by leif created at 2011-04-18 17:42:59

Oh, not to mention #9858 (FLINT). :)

(And I guess MPFR also still should be upgraded, an MPC spkg provided...)


---

Comment by jdemeyer created at 2011-04-18 18:44:23

Replying to [comment:100 leif]:
> The `CFLAGS` (or `-march=`) issue is IMHO completely unrelated -- if not irrelevant. ;-)

The current MPIR spkg _does_ use machine-specific CFLAGS, the new spkg on this ticket _does not_.  This is a step backwards.

If you think it is irrelevant, please explain why...


---

Comment by leif created at 2011-04-19 00:23:35

Replying to [comment:102 jdemeyer]:
> Replying to [comment:100 leif]:
> > The `CFLAGS` (or `-march=`) issue is IMHO completely unrelated -- if not irrelevant. ;-)
> 
> The current MPIR spkg _does_ use machine-specific CFLAGS, the new spkg on this ticket _does not_.  This is a step backwards.
> 
> If you think it is irrelevant, please explain why...

Give me a _realistic_ showcase where that matters... (i.e., causes a significant decrease in performance) ;-)

First of all, the important parts of MPIR are (more or less) hand-optimized assembly code, selected by MPIR's `configure` (or its parameters*) to best match the detected architecture (where MPIR's `config.guess` doesn't always necessarily choose the current nearest one btw.).

A properly configured GCC is usually sufficient, i.e. should default to something like `-march=native` (or a small subset of processors the actual CPU fits into), at least for people to whom performance is really crucial.

With my _current_ spkg here, the user can always (intentionally or not) use the "global" `CFLAGS`, i.e. specify whatever is most appropriate to him or her.

The spkg had been extensively tested -- as is, month ago. As always: New changes, new pitfalls. [And even more delay due to a new test / review cycle. That's why I did not make any further changes _on this ticket_. Speaking of the devil, can someone *please* give #5847 a positive review?]


----

* If I haven't already, one (or me) should implement `MPIR_EXTRA_OPTS` or whatever it was called (but I think I already did).

P.S.: Ah, I see. It's already in the p1 here.


---

Comment by mhansen created at 2011-05-09 18:19:42

We really need to get MPIR updated in Sage.  What's the status of this?


---

Comment by jdemeyer created at 2011-05-09 20:49:47

Replying to [comment:104 mhansen]:
> We really need to get MPIR updated in Sage.  What's the status of this?

The package builds and works.  However, there is still the CFLAGS issue.  Me and William Stein think the package should not be merged in its current state, but others disagree.


---

Comment by leif created at 2011-05-15 07:17:25

Replying to [comment:105 jdemeyer]:
> Replying to [comment:104 mhansen]:
> > We really need to get MPIR updated in Sage.  What's the status of this?
> 
> The package builds and works.  However, there is still the CFLAGS issue.  Me and William Stein think the package should not be merged in its current state, but others disagree.



Ok, I've asked Mercurial about my p2 (which was intended to be a follow-up):


```
+=== mpir-2.1.3.p2 (Leif Leonhardy, November 24th, 2010) ===
+ * #8664: Upgrade Sage's MPIR spkg to version 2.1.3
+ * Further improvements:
+   - Let MPIR select CPU-specific code generation parameters (for CFLAGS) even
+     if we (also) pass our own (or user-specified) CC and CFLAGS; these might
+     be used by MPFR and GMP-ECM later, too, since MPIR's settings are recorded
+     in 'gmp.h' / 'mpir.h'.
+     Don't override user-settings (and respect SAGE_FAT_BINARY, SAGE_DEBUG
+     etc.) though. Add '-march-native' if appropriate and supported.
+  * Recognize also lower-case 'power*' arch (from 'uname -m').
+  * Major restructuring / reformatting; more comments and messages added.
```


I'm not sure right now if it's ready for release, at least it is functional as far as I remember; haven't yet committed all changes though.

Still believe we could [and maybe should] merge the p1 as is; upstream has to be updated anyway (once again, sooner or later, but IMHO definitely on a follow-up ticket).


---

Comment by leif created at 2011-07-05 18:26:23

Sage library patch. Fixes extension modules not getting rebuilt though depending on MPIR. Rebased to Sage 4.7.1.alpha4.


---

Attachment

MPIR 2.4.0 has now been out over a month:  http://mpir.org/
We really, really need to get this upgraded.


---

Comment by leif created at 2011-07-18 06:10:42

Replying to [comment:108 was]:
> MPIR 2.4.0 has now been out over a month:  http://mpir.org/
> We really, really need to get this upgraded.

Well, we could have merged this last year...

Further upstream upgrades should IMHO be made on follow-ups, but shouldn't be a problem once this is in.

Hopefully I can make a FLINT 1.5.2 spkg (cf. #9858) this week, rebasing the one I already have on the latest changes to our 1.5.0, and check / finish the p2 mentioned above which fixes the "`CFLAGS` issue" (though I still consider that kind of ridiculous, at least not a reason to delay an overdue major upgrade for month).

The also required new GMP-ECM package at #5847 was reverted from positive review to "needs work" just because a more or less optional patch to the Sage library would have to be rebased on another that had not even been merged into the at that time current devel release. I did so, but it now again technically needs review.


---

Comment by leif created at 2011-07-18 08:30:51

Preliminary "preview" diff between the p1 and the upcoming p2 with improved option handling (CFLAGS etc.)


---

Attachment

I've attached a "preview" diff of the p2 in case that makes anyone happy...


---

Comment by leif created at 2011-07-18 22:08:22

I have a new p3, but now I'm having the "usual" trouble with PPL (in Sage 4.7.1.rc0).

I.e., installing MPIR works, but after the installation GCC is broken inside Sage, because it tries to use Sage's PPL which still refers to the old `libgmpxx.so.3` which got deleted upon installation. (Others are having trouble with unresolved symbols not provided by Sage's PPL.)

It was IMHO a very bad idea to include PPL into Sage using the same name for the shared library, apparently without taking any care of these issues. (GMP / MPIR, MPFR and the -- currently optional IIRC -- MPC, all used by more recent versions of GCC, are in principle likely dangerous.)

Fortunately<sup>TM</sup> I can just change my `CC` setting to cure the installation, not deleting or copying any libraries or creating symbolic links...

(Apropos, I by incident saw that GAP's `spkg-install` is *unsetting `CC`* because not doing so is said to "break the install". That's very very odd as well.)

I'll update the MPIR spkg again to not delete its old shared libraries as a quick fix.


---

Attachment

Diff between the formerly positively reviewed p1 and the p4. For reference / review.


---

Comment by leif created at 2011-07-20 04:42:50

Changing keywords from "GMP ECM execstack Fedora 14 extension module library dependencies" to "GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7".


---

Comment by leif created at 2011-07-20 04:42:50

New spkg is up:

 http://spkg-upload.googlecode.com/files/mpir-2.1.3.p4.spkg

 md5sum: `f84278504f4e1b696030c41cac6e4719  mpir-2.1.3.p4.spkg`

From a user's view, fixes the "`CFLAGS` issue", adds support for MacOS X 10.7 and some messages.

Installation instructions remain the same; I'll perhaps put them into the description later.

----

### mpir-2.1.3.p4 (Leif Leonhardy, July 19th, 2011)
 * #8664: Upgrade Sage's MPIR spkg to version 2.1.3
 * Do not delete old GMP/MPIR shared libraries as Sage's versions of libraries
   used by GCC might still refer to them, such that their deletion would break
   GCC inside Sage. (PPL e.g. refers to libgmpxx; MPFR and MPC are equally
   dangerous, since they're [also] used by recent versions of GCC.)
 * Some more messages (e.g on rebuilding the Sage library and other packages
   after installation) and comments added.
 * "Patches" section added.
 * Also refreshed the patched gmp-h.in for SunOS. ;-)

### mpir-2.1.3.p3 (Leif Leonhardy, July 18th, 2011)
 * #8664: Upgrade Sage's MPIR spkg to version 2.1.3
 * Support MacOS 10.7 (Darwin 11) and later.
 * Add warning if SAGE_DEBUG=yes since we then disable optimization.

### mpir-2.1.3.p2 (Leif Leonhardy, November 24th, 2010)
 * #8664: Upgrade Sage's MPIR spkg to version 2.1.3
 * Further improvements:
   - Let MPIR select CPU-specific code generation parameters (for CFLAGS) even
     if we (also) pass our own (or user-specified) CC and CFLAGS; these might
     be used by MPFR and GMP-ECM later, too, since MPIR's settings are recorded
     in 'gmp.h' / 'mpir.h'.
     Don't override user-settings (and respect SAGE_FAT_BINARY, SAGE_DEBUG
     etc.) though. Add '-march-native' if appropriate and supported.
  * Recognize also lower-case 'power*' arch (from 'uname -m').
  * Major restructuring / reformatting; more comments and messages added.

(Changes I made relative to the p1 which already had positive review, but got unmerged later.)

----

Further upstream upgrade to MPIR 2.4.0 (or 2.3.1 if more upstream issues should arise) will come soon _on another ticket_. We IMHO first should get this well-tested upstream release in.

Please build, test and review...


---

Comment by leif created at 2011-07-20 04:42:50

Changing status from needs_work to needs_review.


---

Comment by leif created at 2011-07-20 04:57:04

P.S.: It would perhaps be convenient to either have a testing distribution or at least a Sage (library) package with the patch here applied, since during the automatic rebuild of dependent packages Sage switches back to the "main" branch and may invalidate an already applied patch. The behavior seems to have meanwhile changed a bit though.


---

Comment by leif created at 2011-07-20 07:03:44

Ok, to ease testing, I've uploaded a [Sage 4.7.1.rc0 library spkg](http://spkg-upload.googlecode.com/files/sage-4.7.1.rc0-8664-5847.spkg) with both patches (from here and #5847) already applied.

You can either build Sage 4.7.1.rc0 from scratch with these three spkgs, or take a Sage 4.7.1.rc0 installation and just install them, automatically rebuilding (only) the dependent spkgs.

 1. Copy [the MPIR spkg](http://spkg-upload.googlecode.com/files/mpir-2.1.3.p4.spkg) and [the GMP-ECM spkg](http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg) into `$SAGE_ROOT/spkg/standard/`.
 1. *Replace* the `sage-4.7.1.rc0.spkg` with [this one](http://spkg-upload.googlecode.com/files/sage-4.7.1.rc0-8664-5847.spkg) (i.e., copy it to `$SAGE_ROOT/spkg/standard` and *delete* the original since `newest_version` would otherwise take the wrong one).
 1. Build:
    * For a build from scratch, simply type `make`.
    * For rebuilding an existing installation with the new spkgs, type

```sh
env SAGE_UPGRADING=yes make
```


Note that you currently must not set `SAGE_CHECK` to `yes` in the above procedures, since the test suite of our current FLINT won't build with the new MPIR.

To run MPIR's and GMP-ECM's test suites, I'd suggest to simply reinstall them afterwards with `env SAGE_CHECK=yes ./sage -f mpir-2.1.3.p4 ecm-6.3.p2`. Likewise, you can also play with different `CFLAGS` settings (empty, some non-processor-specific flags, with some `-march=...` or `-mtune=...` etc. included).

Then preferably run `make testlong` or `make ptestlong`, though both upstream releases have IMHO already been quite excessively tested.


---

Comment by dimpase created at 2011-07-21 11:02:21

Replying to [comment:114 leif]:


I'm currently running this on MacOSX 10.6. Will report as soon as it's done


---

Comment by leif created at 2011-07-22 07:39:46

Replying to [comment:115 dimpase]:
> I'm currently running this on MacOSX 10.6. Will report as soon as it's done

Thanks. If all tests pass and you're happy with the spkg _here_, you may want to take a look at #11616. ;-)


---

Comment by dimpase created at 2011-07-22 10:25:16

Replying to [comment:115 dimpase]:
> Replying to [comment:114 leif]:
> 
> 
> I'm currently running this on MacOSX 10.6. Will report as soon as it's done

I can confirm that the above procedure and "make ptestlong" works just fine on MacOSX 10.6.


---

Comment by dimpase created at 2011-07-22 10:29:32

Replying to [comment:116 leif]:
> Replying to [comment:115 dimpase]:
> > I'm currently running this on MacOSX 10.6. Will report as soon as it's done
> 
> Thanks. If all tests pass and you're happy with the spkg _here_, you may want to take a look at #11616. ;-)
> 

I think I can give this a positive review.


---

Comment by dimpase created at 2011-07-22 10:29:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-07-24 18:53:36

because it depends on a not-yet-positively-reviewed ticket


---

Comment by leif created at 2011-07-24 23:06:37

Replying to [comment:120 jdemeyer]:
> because it depends on a not-yet-positively-reviewed ticket

Well, can't you re-review #5847, which you set back to "needs work"?

The only single thing that has changed there is that the one-line patch to `module_list.py` got rebased to Sage 4.7.1.alpha4, in particular it is the same patch, differing just in line numbers (or, more precisely, a single after-context line):

```patch
--- ../patches/trac_5847-module_list-fix_execstack-sagelib.patch	2011-06-02 21:38:51.000000000 +0200
+++ ../patches/trac_5847-module_list-fix_execstack-sagelib-rebased_to_4.7.1.alpha4.patch	2011-07-20 07:08:13.000000000 +0200
`@``@` -1,22 +1,24 `@``@`
 # HG changeset patch
 # User Leif Leonhardy <not.really`@`online.de>
-# Date 1307043111 -7200
-# Node ID e7b1b631a38756bb37aa5edc7a0e31ff10eaa86a
-# Parent  fb00ec75853019eb9799fd863b193fe82ee97c74
+# Date 1309863032 -7200
+# Node ID 556a3825c961b6871451652dede6ec3742705482
+# Parent  8532a2ad1e558cbc91ddaaa6b7cc79956dd1e8ba
 #5847: Add 'noexecstack' flag when linking libecm extension module on Linux.
 
 (Not doing so caused trouble on a SkyNet Fedora machine with Sage 4.7.1.alpha1
  and GMP-ECM 6.3.p2 from #5847, GCC 4.6.0; didn't occur previously.)
 
-diff -r fb00ec758530 -r e7b1b631a387 module_list.py
---- a/module_list.py	Wed May 11 22:39:05 2011 +0000
-+++ b/module_list.py	Thu Jun 02 21:31:51 2011 +0200
-`@``@` -561,6 +561,8 `@``@`
+(Rebased patch for Sage 4.7.1.alpha4 / #11377)
+
+diff -r 8532a2ad1e55 -r 556a3825c961 module_list.py
+--- a/module_list.py	Sun Jul 03 14:23:12 2011 +0000
++++ b/module_list.py	Tue Jul 05 12:50:32 2011 +0200
+`@``@` -568,6 +568,8 `@``@`
      Extension('sage.libs.libecm',
                sources = ['sage/libs/libecm.pyx'],
                libraries = ['ecm', 'gmp'],
 +              extra_link_args = uname_specific("Linux", ["-Wl,-z,noexecstack"],
 +                                                        []),
-               depends = [SAGE_ROOT + "/local/include/ecm.h"]),
+               depends = [SAGE_INC + "ecm.h"]),
       
      Extension('sage.libs.mwrank.mwrank',
```



---

Comment by ohanar created at 2011-08-23 05:57:45

#5847 has a positive review again


---

Comment by was created at 2011-08-24 23:35:53

Changing keywords from "GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7" to "sd32, GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7".


---

Comment by leif created at 2011-08-31 21:45:49

Sage library patch. Fixes extension modules not getting rebuilt though depending on MPIR. Rebased on Sage 4.7.2.alpha2 / #11376.


---

Attachment


---

Comment by leif created at 2011-09-12 19:03:12

Resolution: fixed


---

Comment by leif created at 2011-09-12 19:03:12

Changing keywords from "sd32, GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7" to "sd32, GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7 Lion".


---

Comment by leif created at 2011-09-23 05:13:15

Had to fix the changelog and some file permissions.

Corrected spkg at new location.


---

Comment by strogdon created at 2011-10-03 01:45:29

I'm not sure if this is the best place to report this since the ticket has been merged, but in building vanilla sage-4.7.2.alpha3 on x86, mpir-2.1.3.p4 fails with


```
 ../strip_fPIC.sh ../yasm/yasm -I .. -f elf64 submul_1.as -o submul_1.o >/dev/null 2>&1
/bin/bash ../libtool --mode=c
 ../mpn/m4-ccas --m4=m4 gcc -std=gnu99 -c -DHAVE_CONFIG_H -m32 -O2 -fomit-frame-pointer -mtune=core2 -march=core2 -D__GMP_WITHIN_GMP -I.. -DOPERATION_lshift -I. -I.. lshift.asm  -fPIC -DPIC -o .libs/lshift.o
m4  -DHAVE_CONFIG_H -D__GMP_WITHIN_GMP -DOPERATION_lshift -DPIC lshift.asm >tmp-lshift.s
 gcc -std=gnu99 -c -DHAVE_CONFIG_H -m32 -O2 -fomit-frame-pointer -mtune=core2 -march=core2 -D__GMP_WITHIN_GMP -I.. -DOPERATION_lshift -I. -I.. tmp-lshift.s -fPIC -DPIC -o .libs/lshift.o
tmp-lshift.s: Assembler messages:
tmp-lshift.s:53: Error: bad register name `%rbx'
tmp-lshift.s:54: Error: bad register name `%rdx'
tmp-lshift.s:55: Error: bad register name `%rsi)'
tmp-lshift.s:56: Error: bad register name `%rdi)'
tmp-lshift.s:57: Error: bad register name `%rsi,%rbx,8)'
tmp-lshift.s:58: Error: bad register name `%rax'
tmp-lshift.s:59: Error: bad register name `%rdx'
tmp-lshift.s:60: Error: bad register name `%rbx'
tmp-lshift.s:64: Error: bad register name `%rsi,%rbx,8)'
tmp-lshift.s:65: Error: bad register name `%rsi,%rbx,8)'
tmp-lshift.s:66: Error: bad register name `%rsi,%rbx,8)'
tmp-lshift.s:67: Error: bad register name `%r8'
tmp-lshift.s:68: Error: bad register name `%rdx'
tmp-lshift.s:69: Error: bad register name `%r11'
tmp-lshift.s:70: Error: bad register name `%rsi,%rbx,8)'

...

tmp-lshift.s:118: Error: bad register name `%rsi,%rbx,8)'
tmp-lshift.s:119: Error: bad register name `%r8'
tmp-lshift.s:120: Error: bad register name `%rdx'
tmp-lshift.s:121: Error: bad register name `%r8'
tmp-lshift.s:122: Error: bad register name `%r8'
tmp-lshift.s:123: Error: bad register name `%rbx'
make[4]: *** [lshift.lo] Error 1
make[4]: Leaving directory `/storage/sage/sage-4.7.2.alpha3/spkg/build/mpir-2.1.3.p4/src/mpn'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/storage/sage/sage-4.7.2.alpha3/spkg/build/mpir-2.1.3.p4/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/storage/sage/sage-4.7.2.alpha3/spkg/build/mpir-2.1.3.p4/src'
Error building MPIR.
```

I've never seen this before. The machine is running debian, but the sage build was done from within a gentoo prefix. So the build is basically one using gentoo. There doesn't seem to be a problem on amd64. I still have the build log.


---

Comment by leif created at 2011-10-03 06:18:37

Replying to [comment:128 strogdon]:
> I'm not sure if this is the best place to report this since the ticket has been merged, but in building vanilla sage-4.7.2.alpha3 on x86, mpir-2.1.3.p4 fails with
> 

```
tmp-lshift.s: Assembler messages:
tmp-lshift.s:53: Error: bad register name `%rbx'
...
make[4]: *** [lshift.lo] Error 1
...
```

> I've never seen this before. The machine is running debian, but the sage build was done from within a gentoo prefix. So the build is basically one using gentoo. There doesn't seem to be a problem on amd64. I still have the build log.

See [sage-release](http://groups.google.com/group/sage-release/msg/c560179ee11e8692) and [this mpir-devel thread](http://groups.google.com/group/mpir-devel/browse_thread/thread/46ccdc5dfc3485cd#).

I'm sorry I didn't catch this earlier, but it's a waste of resources to run 32-bit operating systems (or software in general) on 64-bit processors... ;-)

I'll provide follow-up spkgs (also at #11616) that will fix this without the need to set `ABI`, but perhaps not that very soon.

By the way, MPIR 2.5.0 should get released in the next days as well, so I'll presumably also make an spkg based on that.


---

Comment by leif created at 2011-10-05 03:37:54

Replying to [comment:129 leif]:
> Replying to [comment:128 strogdon]:
> > I'm not sure if this is the best place to report this since the ticket has been merged, but in building vanilla sage-4.7.2.alpha3 on x86, mpir-2.1.3.p4 fails with
> > 

```
tmp-lshift.s: Assembler messages:
tmp-lshift.s:53: Error: bad register name `%rbx'
...
make[4]: *** [lshift.lo] Error 1
...
```

> I'll provide follow-up spkgs (also at #11616) that will fix this without the need to set `ABI`, but perhaps not that very soon.

An MPIR 2.1.3.p5 spkg fixing this is now available at #11896, currently needing review.


---

Comment by jdemeyer created at 2011-10-11 07:36:14

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2011-10-11 07:36:14

Changing status from closed to new.


---

Comment by jdemeyer created at 2011-10-11 07:36:14

Unmerging this because of #9858 and #11896.


---

Comment by jdemeyer created at 2011-10-11 07:38:24

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2011-10-11 07:38:32

Changing status from needs_review to positive_review.


---

Comment by leif created at 2011-10-11 22:27:23

Another cyclic dependency... ;-) (#11698 depends on this ticket)

----

A new FLINT spkg (still 1.5.0, a p10) fixing the FLINT test suite build error (occurring in combination with any recent GMP / MPIR version like the one here) by just applying an upstream patch from FLINT 1.5.2 is ready for review at #9858.

(FLINT 1.5.2 and 1.6 spkgs will now most probably be on follow-up tickets to #9858.)


---

Comment by leif created at 2011-10-11 22:32:56

Replying to [comment:134 leif]:
> Another cyclic dependency... ;-) (#11698 depends on this ticket)

Ooops, #11896 of course. XD

(But I'll try to review #11698 anyway.)


---

Comment by jdemeyer created at 2011-10-14 09:41:13

Resolution: fixed


---

Comment by jdemeyer created at 2011-11-03 16:14:43

Milestone sage-4.7.3 deleted


---

Comment by kcrisman created at 2011-12-03 19:08:37

Replying to [comment:46 leif]:
> Any reason to keep
> {{{
> #!sh
>     SAGE_CONF_OPTS="--enable-shared --disable-static"
> }}}
> (i.e., why not build the static library, too)?
> 
As it turns out, this change seems to break MPIR on Cygwin.  See [this sage-windows thread](http://groups.google.com/group/sage-windows/browse_thread/thread/be2b2af416351c9b).
