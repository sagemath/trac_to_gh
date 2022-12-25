# Issue 8664: upgrade sage's mpir spkg to version 2.0.0

archive/issues_008664.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @williamstein @nexttime drkirkby @jdemeyer wbhart jpflori\n\n```\nHi,\n\nOK, after all this, the build finally completed.  The only changes I made were:\n\n* Updated mpir to rc3\n* patched ecm as explained here:\n    http://lists.gforge.inria.fr/pipermail/ecm-discuss/2009-August/004070.html\n   (Though this had to be slightly modified -- just search for the same command, which moved.)\n\n\nI then ran the long Sage test suite, and some tests fail.  \n\n  http://sage.math.washington.edu/home/wstein/build/mpir2/sage-4.3.5/testlong.log\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  -long \"devel/sage/doc/en/tutorial/tour_numtheory.rst\"\n        sage -t  -long \"devel/sage/doc/fr/tutorial/tour_numtheory.rst\"\n        sage -t  -long \"devel/sage/sage/modular/cusps.py\"\n        sage -t  -long \"devel/sage/sage/modular/modsym/boundary.py\"\n        sage -t  -long \"devel/sage/sage/modular/modsym/ambient.py\"\n        sage -t  -long \"devel/sage/sage/libs/pari/gen.pyx\"\n        sage -t  -long \"devel/sage/sage/rings/arith.py\"\n        sage -t  -long \"devel/sage/sage/rings/integer.pyx\"\n        sage -t  -long \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n        sage -t  -long \"devel/sage/sage/tests/book_stein_ent.py\"\n        sage -t  -long \"devel/sage/sage/schemes/elliptic_curves/heegner.py\"\nTotal time for all tests: 7170.6 seconds\n\n--\n\nI looked and it appears that maybe all of these are the result of the XGCD behavior in MPIR changing again.  Has it changed to be like GMP now?  That would be convenient.\n\nwilliam\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8664\n\n",
    "created_at": "2010-04-09T04:10:07Z",
    "labels": [
        "component: build"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "upgrade sage's mpir spkg to version 2.0.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8664",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber

CC:  @williamstein @nexttime drkirkby @jdemeyer wbhart jpflori

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

Issue created by migration from https://trac.sagemath.org/ticket/8664





---

archive/issue_comments_078550.json:
```json
{
    "body": "The XGCD issue needs some work w.r.t. doctests (but not only, see below), maybe David Harvey has something done already in this direction when preparing the optional \"true\" GMP spkg he maintains. (I don't find the thread right now, but I seem to remember he said something in this direction).\n\nSnippet from a private communication by Bill Hart (MPIR upstream):\n\n```\nMPIR 2.0.1 will be required for Sage because it brings the gcdext\nnormalisation in line with GMP's (which is what Pari needs). I think\npeople have skipped MPIR 1.3.0 in favour of waiting for MPIR 2.0.1.\nWe're in the release phase of MPIR 2.0.1 ...\n```\nAlso note that as soon as this ticket here is closed, we should mark #8455 as invalid.",
    "created_at": "2010-05-19T09:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78550",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

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

archive/issue_comments_078551.json:
```json
{
    "body": "This needs to be handled with #5847 and should take care of #9522 at the same time.",
    "created_at": "2010-08-17T18:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78551",
    "user": "https://github.com/mwhansen"
}
```

This needs to be handled with #5847 and should take care of #9522 at the same time.



---

archive/issue_comments_078552.json:
```json
{
    "body": "I've put an spkg at http://sage.math.washington.edu/home/mhansen/mpir-2.1.1.spkg\n\nInterestingly, I did not get any of the failures listed above.",
    "created_at": "2010-08-18T06:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78552",
    "user": "https://github.com/mwhansen"
}
```

I've put an spkg at http://sage.math.washington.edu/home/mhansen/mpir-2.1.1.spkg

Interestingly, I did not get any of the failures listed above.



---

archive/issue_comments_078553.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-18T06:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78553",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078554.json:
```json
{
    "body": "Changing component from build to packages.",
    "created_at": "2010-08-19T22:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78554",
    "user": "https://github.com/qed777"
}
```

Changing component from build to packages.



---

archive/issue_comments_078555.json:
```json
{
    "body": "Hmmm, `spkg-install` could be cleaned up further, e.g.\n* Dave's comment has somehow been truncated(?) a while ago (*\"... if\"* what?)\n* `s/`uname`/$UNAME/`\n* Especially for parallel builds, it's more convenient to begin *every* error message with `\"Error\"` (or at least the message should contain that word).\n* Simplify the \"fat binary\" section for Linux; it doesn't make sense to call `uname -m` three times, nor does it to compare its result again if it already matched one of the tested. A `case`-`esac` would be appropriate, also merging the identical `i386` and `i686` then-branches. Btw, `uname -m` can also be `i486` or `i586` on 32-bit Linuces.\n* Is the `! [ $? -eq 0 ]` some required Cygwin \"idiom\"?\n\nAlso, `spkg-check` doesn't print any messages, and uses `make` instead of `$MAKE`.\n\nThe dependencies (\"None\") in `SPKG.txt` are wrong; MPIR at least depends on iconv, which Sage ships, though Sage's version is only used/built on some systems. I'm not sure if readline should be added to `spkg/standard/deps`. (MPIR's `configure` looks for much more, but apparently - as currently shipped - doesn't need/use all of that.) The Changelog could perhaps mention further changes, too.\n\nIf nobody else wants to, I could make the changes, i.e. a reviewer patch. Just let me know...\n\nGoing to test the new spkg with Sage 4.5.3.alpha2 and 4.6.prealpha3 (on Linuces only).",
    "created_at": "2010-08-26T22:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78555",
    "user": "https://github.com/nexttime"
}
```

Hmmm, `spkg-install` could be cleaned up further, e.g.
* Dave's comment has somehow been truncated(?) a while ago (*"... if"* what?)
* `s/`uname`/$UNAME/`
* Especially for parallel builds, it's more convenient to begin *every* error message with `"Error"` (or at least the message should contain that word).
* Simplify the "fat binary" section for Linux; it doesn't make sense to call `uname -m` three times, nor does it to compare its result again if it already matched one of the tested. A `case`-`esac` would be appropriate, also merging the identical `i386` and `i686` then-branches. Btw, `uname -m` can also be `i486` or `i586` on 32-bit Linuces.
* Is the `! [ $? -eq 0 ]` some required Cygwin "idiom"?

Also, `spkg-check` doesn't print any messages, and uses `make` instead of `$MAKE`.

The dependencies ("None") in `SPKG.txt` are wrong; MPIR at least depends on iconv, which Sage ships, though Sage's version is only used/built on some systems. I'm not sure if readline should be added to `spkg/standard/deps`. (MPIR's `configure` looks for much more, but apparently - as currently shipped - doesn't need/use all of that.) The Changelog could perhaps mention further changes, too.

If nobody else wants to, I could make the changes, i.e. a reviewer patch. Just let me know...

Going to test the new spkg with Sage 4.5.3.alpha2 and 4.6.prealpha3 (on Linuces only).



---

archive/issue_comments_078556.json:
```json
{
    "body": "Dave, as it seems you're addicted to testing, you could also test *this* new spkg (e.g. on Solaris, OpenSolaris)... ;-)",
    "created_at": "2010-08-26T23:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78556",
    "user": "https://github.com/nexttime"
}
```

Dave, as it seems you're addicted to testing, you could also test *this* new spkg (e.g. on Solaris, OpenSolaris)... ;-)



---

archive/issue_comments_078557.json:
```json
{
    "body": "I guess unless we bump the patch levels of all packages that depend on GMP/MPIR (and ECM), this package breaks upgrading Sage (at least with the current upgrade process), due to interface change (in conjunction with shared library versioning).\n\nThe same applies to testing this package (and/with ECM 6.3 from #5847); one has to either build from scratch or delete `spkg/installed/<package-name>` for all packages that depend on those two.\n\nPerhaps one could simply (conditionally) do the latter in `spkg/install`, which also gets updated during upgrade.",
    "created_at": "2010-08-27T01:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78557",
    "user": "https://github.com/nexttime"
}
```

I guess unless we bump the patch levels of all packages that depend on GMP/MPIR (and ECM), this package breaks upgrading Sage (at least with the current upgrade process), due to interface change (in conjunction with shared library versioning).

The same applies to testing this package (and/with ECM 6.3 from #5847); one has to either build from scratch or delete `spkg/installed/<package-name>` for all packages that depend on those two.

Perhaps one could simply (conditionally) do the latter in `spkg/install`, which also gets updated during upgrade.



---

archive/issue_comments_078558.json:
```json
{
    "body": "Defining `SAGE_SPKG` to `sage-spkg -f` in `spkg/standard/deps` should *in principle* also work, but doesn't... apparently because *not really all* shared libraries that use `libgmpxx.so` get rebuilt, so some still refer to the old, deleted `libgmpxx.so.3`.\n\n---\n\nRebuilding Sage 4.5.3.alpha2 with MPIR 2.1.1 and ECM 6.3 *from scratch* worked on Ubuntu 10.04 x86_64 (parallel build with 32 jobs); `ptestlong` passed all tests.",
    "created_at": "2010-08-27T03:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78558",
    "user": "https://github.com/nexttime"
}
```

Defining `SAGE_SPKG` to `sage-spkg -f` in `spkg/standard/deps` should *in principle* also work, but doesn't... apparently because *not really all* shared libraries that use `libgmpxx.so` get rebuilt, so some still refer to the old, deleted `libgmpxx.so.3`.

---

Rebuilding Sage 4.5.3.alpha2 with MPIR 2.1.1 and ECM 6.3 *from scratch* worked on Ubuntu 10.04 x86_64 (parallel build with 32 jobs); `ptestlong` passed all tests.



---

archive/issue_comments_078559.json:
```json
{
    "body": "Replying to [comment:10 leif]:\n> Defining `SAGE_SPKG` to `sage-spkg -f` in `spkg/standard/deps` should *in principle* also work, but doesn't... apparently because *not really all* shared libraries that use `libgmpxx.so` get rebuilt, so some still refer to the old, deleted `libgmpxx.so.3`.\n\n\nI think this could be fixed by making extension modules also depend on (some of) the libraries they use (in `module_list.py`), with the disadvantage that these modules would get rebuilt whenever their libraries \"change\", even if the interfaces stay the same (and even if just the modification time changed due to a rebuild/reinstallation). \n\n---\n \n> Rebuilding Sage 4.5.3.alpha2 with MPIR 2.1.1 and ECM 6.3 *from scratch* worked on Ubuntu 10.04 x86_64 (parallel build with 32 jobs); `ptestlong` passed all tests.\n\n\nSame for Fedora 13 x86 (parallel build with 6 jobs), also `ptestlong`.\n\n---\n\nUnfortunately, there seems to be some incompatibility between the new PARI (2.4.3.svn-12577.p4) or - more precisely - the required changes to Sage's interface to PARI in order to upgrade PARI (Sage 4.6.prealpha3, see #9343 and [the NewPARI Wiki page](http://wiki.sagemath.org/NewPARI)) and MPIR 2.1.1:\n\nOn Ubuntu 10.04 x86_64 (Core2, gcc 4.4.3) exactly two of all doctests (`ptestlong`) **segfault** (in `sage/schemes/elliptic_curves/ell_point.py`).\n\nOn Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4) the same two doctests and another one in `ell_rational_field.py` segfault, and in addition one doctest in the latter file raises an unexpected exception (`TypeError`), which seems to be the result of some other failure.\n\nMaybe all are due to memory (or stack) corruption. See http://trac.sagemath.org/sage_trac/ticket/9343#comment:327 ff. for details; we haven't yet opened a separate ticket.\n\n(For testing with Sage 4.6.prealpha3, I copied the MPIR 2.1.1 and ECM 6.3 spkgs to `spkg/standard`, and built Sage from scratch - without problems. I also reinstalled the PARI, MPIR and ECM packages later with `env SAGE_CHECK=yes ./sage -f ...`; all test suites passed.)",
    "created_at": "2010-08-28T01:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78559",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:10 leif]:
> Defining `SAGE_SPKG` to `sage-spkg -f` in `spkg/standard/deps` should *in principle* also work, but doesn't... apparently because *not really all* shared libraries that use `libgmpxx.so` get rebuilt, so some still refer to the old, deleted `libgmpxx.so.3`.


I think this could be fixed by making extension modules also depend on (some of) the libraries they use (in `module_list.py`), with the disadvantage that these modules would get rebuilt whenever their libraries "change", even if the interfaces stay the same (and even if just the modification time changed due to a rebuild/reinstallation). 

---
 
> Rebuilding Sage 4.5.3.alpha2 with MPIR 2.1.1 and ECM 6.3 *from scratch* worked on Ubuntu 10.04 x86_64 (parallel build with 32 jobs); `ptestlong` passed all tests.


Same for Fedora 13 x86 (parallel build with 6 jobs), also `ptestlong`.

---

Unfortunately, there seems to be some incompatibility between the new PARI (2.4.3.svn-12577.p4) or - more precisely - the required changes to Sage's interface to PARI in order to upgrade PARI (Sage 4.6.prealpha3, see #9343 and [the NewPARI Wiki page](http://wiki.sagemath.org/NewPARI)) and MPIR 2.1.1:

On Ubuntu 10.04 x86_64 (Core2, gcc 4.4.3) exactly two of all doctests (`ptestlong`) **segfault** (in `sage/schemes/elliptic_curves/ell_point.py`).

On Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4) the same two doctests and another one in `ell_rational_field.py` segfault, and in addition one doctest in the latter file raises an unexpected exception (`TypeError`), which seems to be the result of some other failure.

Maybe all are due to memory (or stack) corruption. See http://trac.sagemath.org/sage_trac/ticket/9343#comment:327 ff. for details; we haven't yet opened a separate ticket.

(For testing with Sage 4.6.prealpha3, I copied the MPIR 2.1.1 and ECM 6.3 spkgs to `spkg/standard`, and built Sage from scratch - without problems. I also reinstalled the PARI, MPIR and ECM packages later with `env SAGE_CHECK=yes ./sage -f ...`; all test suites passed.)



---

archive/issue_comments_078560.json:
```json
{
    "body": "Replying to [comment:11 leif]:\n> Unfortunately, there seems to be some incompatibility between the new PARI (2.4.3.svn-12577.p4 / Sage 4.6.prealpha3, see #9343 and [the NewPARI Wiki page](http://wiki.sagemath.org/NewPARI)) and MPIR 2.1.1:\n\n\n> On Ubuntu 10.04 x86_64 (Core2, gcc 4.4.3) exactly two of all doctests (`ptestlong`) **segfault** (in `sage/schemes/elliptic_curves/ell_point.py`).\n\n\n> On Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4) the same two doctests and another one in `ell_rational_field.py` segfault, and in addition one doctest in the latter file raises an unexpected exception (`TypeError`), which seems to be the result of some other failure.\n\n\nThis is due to the new PARI using undocumented features of GMP (that MPIR doesn't support). and is now addressed at #9837.",
    "created_at": "2010-08-29T15:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78560",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:11 leif]:
> Unfortunately, there seems to be some incompatibility between the new PARI (2.4.3.svn-12577.p4 / Sage 4.6.prealpha3, see #9343 and [the NewPARI Wiki page](http://wiki.sagemath.org/NewPARI)) and MPIR 2.1.1:


> On Ubuntu 10.04 x86_64 (Core2, gcc 4.4.3) exactly two of all doctests (`ptestlong`) **segfault** (in `sage/schemes/elliptic_curves/ell_point.py`).


> On Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4) the same two doctests and another one in `ell_rational_field.py` segfault, and in addition one doctest in the latter file raises an unexpected exception (`TypeError`), which seems to be the result of some other failure.


This is due to the new PARI using undocumented features of GMP (that MPIR doesn't support). and is now addressed at #9837.



---

archive/issue_comments_078561.json:
```json
{
    "body": "Replying to [comment:12 leif]:\n> This is due to the new PARI using undocumented features of GMP (that MPIR doesn't support). and is now addressed at #9837.\n\n\nThis is not necessarily the (only) cause. Jeroen has found a definite bug in MPIR 2.1.1 he'll report upstream; see #9837.\n\nLeaving the ticket \"needs review\", though I don't think we should upgrade MPIR until that bug is fixed, in a later release.",
    "created_at": "2010-08-29T18:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78561",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:12 leif]:
> This is due to the new PARI using undocumented features of GMP (that MPIR doesn't support). and is now addressed at #9837.


This is not necessarily the (only) cause. Jeroen has found a definite bug in MPIR 2.1.1 he'll report upstream; see #9837.

Leaving the ticket "needs review", though I don't think we should upgrade MPIR until that bug is fixed, in a later release.



---

archive/issue_comments_078562.json:
```json
{
    "body": "Replying to [comment:13 leif]:\n> Leaving the ticket \"needs review\", though I don't think we should upgrade MPIR until that bug is fixed, in a later release.\n\n\nSounds good to me.",
    "created_at": "2010-08-29T18:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78562",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:13 leif]:
> Leaving the ticket "needs review", though I don't think we should upgrade MPIR until that bug is fixed, in a later release.


Sounds good to me.



---

archive/issue_comments_078563.json:
```json
{
    "body": "The problem of ticket #9837 has been fixed in MPIR svn, it was purely a bug in MPIR 2.1.1.",
    "created_at": "2010-09-04T21:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78563",
    "user": "https://github.com/jdemeyer"
}
```

The problem of ticket #9837 has been fixed in MPIR svn, it was purely a bug in MPIR 2.1.1.



---

archive/issue_comments_078564.json:
```json
{
    "body": "Please upgrade to MPIR 2.1.2, where #9837 is fixed.",
    "created_at": "2010-09-05T12:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78564",
    "user": "https://github.com/jdemeyer"
}
```

Please upgrade to MPIR 2.1.2, where #9837 is fixed.



---

archive/issue_comments_078565.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-05T12:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78565",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078566.json:
```json
{
    "body": "Apparently [they've released MPIR 2.1.2](http://www.mpir.org/) with just this bug fixed today.\n\nHaven't tested that yet.",
    "created_at": "2010-09-05T17:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78566",
    "user": "https://github.com/nexttime"
}
```

Apparently [they've released MPIR 2.1.2](http://www.mpir.org/) with just this bug fixed today.

Haven't tested that yet.



---

archive/issue_comments_078567.json:
```json
{
    "body": "Replying to [comment:18 leif]:\n> Apparently [they've released MPIR 2.1.2](http://www.mpir.org/) with just this bug fixed today.\n> \n> Haven't tested that yet.\n\n\nAt least passes all (long) tests in `sage/schemes/elliptic_curves/` with Sage 4.6.prealpha3 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4), where previously the segfaults occurred.\n\nThe diff shows they just fixed that single bug, bumped the MPIR version number (patch level) and incremented the revision numbers of both shared libraries. (In addition, they changed *the date of* the documentation without actually changing the docs themselves. The file `src/.gdbinit` in the MPIR 2.1.1 spkg must have been added by Mike or someone else.)",
    "created_at": "2010-09-05T18:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78567",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:18 leif]:
> Apparently [they've released MPIR 2.1.2](http://www.mpir.org/) with just this bug fixed today.
> 
> Haven't tested that yet.


At least passes all (long) tests in `sage/schemes/elliptic_curves/` with Sage 4.6.prealpha3 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4), where previously the segfaults occurred.

The diff shows they just fixed that single bug, bumped the MPIR version number (patch level) and incremented the revision numbers of both shared libraries. (In addition, they changed *the date of* the documentation without actually changing the docs themselves. The file `src/.gdbinit` in the MPIR 2.1.1 spkg must have been added by Mike or someone else.)



---

archive/issue_events_020984.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2010-09-05T18:55:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20984"
}
```



---

archive/issue_comments_078568.json:
```json
{
    "body": "FLINT also needs to be updated (from 1.5.0[.p5] to 1.5.2) to work with the new MPIR; otherwise the test suite won't build. See #9858.",
    "created_at": "2010-09-06T09:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78568",
    "user": "https://github.com/nexttime"
}
```

FLINT also needs to be updated (from 1.5.0[.p5] to 1.5.2) to work with the new MPIR; otherwise the test suite won't build. See #9858.



---

archive/issue_comments_078569.json:
```json
{
    "body": "Before the 4.6.alphaX build fails on the ia64 Skynet machines cleo and iras because of a bug in GCC 4.5.1 (see #9863), there's an apparent parallel `make install` failure with MPIR:\n\n```\n[...]\nmake[6]: Entering directory `/home/mpatel/build/cleo/sage-4.6.alpha2/spkg/build/\nmpir-1.2.2.p1/src'\nmake[6]: warning: -jN forced in submake: disabling jobserver mode.\n(cd /home/mpatel/build/cleo/sage-4.6.alpha2/local/include  && rm -f gmp.h   && c\np mpir.h   gmp.h)\n /usr/bin/install -c -m 644 'mpir.h' '/home/mpatel/build/cleo/sage-4.6.alpha2/lo\ncal/include/mpir.h'\ncp: cannot stat `mpir.h': No such file or directory\nmake[6]: *** [install-data-hook] Error 1\nmake[6]: Leaving directory `/home/mpatel/build/cleo/sage-4.6.alpha2/spkg/build/mpir-1.2.2.p1/src'\nmake[5]: *** [install-data-am] Error 2\nmake[5]: *** Waiting for unfinished jobs....\n[...]\n```\nHas anyone else seen this?  The full logs are [here](http://sage.math.washington.edu/home/mpatel/trac/8664/).\n\nI noticed that [MPIR 2.1.3 is out](http://www.mpir.org/) with a fix in `mpf_get_d_2exp`.  But I don't think Sage uses (m)any of the `mpf_*` functions.",
    "created_at": "2010-09-30T10:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78569",
    "user": "https://github.com/qed777"
}
```

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

archive/issue_comments_078570.json:
```json
{
    "body": "Replying to [comment:22 mpatel]:\n> Before the 4.6.alphaX build fails on the ia64 Skynet machines cleo and iras because of a bug in GCC 4.5.1 (see #9863), there's an apparent parallel `make install` failure with MPIR:\n\n\nI've also [seen this on Skynet's menas](http://build.sagemath.org/sage/builders/menas%20full/builds/39/steps/shell_1/logs/mpir).",
    "created_at": "2010-10-22T01:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78570",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:22 mpatel]:
> Before the 4.6.alphaX build fails on the ia64 Skynet machines cleo and iras because of a bug in GCC 4.5.1 (see #9863), there's an apparent parallel `make install` failure with MPIR:


I've also [seen this on Skynet's menas](http://build.sagemath.org/sage/builders/menas%20full/builds/39/steps/shell_1/logs/mpir).



---

archive/issue_comments_078571.json:
```json
{
    "body": "Replying to [comment:22 mpatel]:\n> Before the 4.6.alphaX build fails on the ia64 Skynet machines cleo and iras because of a bug in GCC 4.5.1 (see #9863), there's an apparent parallel `make install` failure with MPIR:\n\n{{{\n[...]\nmake[6]: Entering directory `/home/mpatel/build/cleo/sage-4.6.alpha2/spkg/build/\nmpir-1.2.2.p1/src'\nmake[6]: warning: -jN forced in submake: disabling jobserver mode.\n(cd /home/mpatel/build/cleo/sage-4.6.alpha2/local/include  && rm -f gmp.h   && cp mpir.h   gmp.h)\n/usr/bin/install -c -m 644 'mpir.h' '/home/mpatel/build/cleo/sage-4.6.alpha2/local/include/mpir.h'\ncp: cannot stat `mpir.h': No such file or directory\nmake[6]: *** [install-data-hook] Error 1\nmake[6]: Leaving directory `/home/mpatel/build/cleo/sage-4.6.alpha2/spkg/build/mpir-1.2.2.p1/src'\nmake[5]: *** [install-data-am] Error 2\nmake[5]: *** Waiting for unfinished jobs....\n[...]\n}}}\n> Has anyone else seen this? \n\n\nSorry for the delay; I frequently see this since a while on Ubuntus (9.04 & 10.04) when building Sage with e.g. 16 or 32 jobs, with the **old** MPIR, too; also reported elsewhere (but incidentally also first saw this with MPIR 2.1.1 and the new PARI).\n\nI cannot find obvious errors in the Makefile though; the relevant parts are identical to those of GMP btw, IIRC.\n\nAs another incident, I ran into this race condition again yesterday when building Sage 4.4.4 (!) from scratch with `MAKE=\"make -j16\"`.",
    "created_at": "2010-10-22T07:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78571",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:22 mpatel]:
> Before the 4.6.alphaX build fails on the ia64 Skynet machines cleo and iras because of a bug in GCC 4.5.1 (see #9863), there's an apparent parallel `make install` failure with MPIR:

{{{
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
}}}
> Has anyone else seen this? 


Sorry for the delay; I frequently see this since a while on Ubuntus (9.04 & 10.04) when building Sage with e.g. 16 or 32 jobs, with the **old** MPIR, too; also reported elsewhere (but incidentally also first saw this with MPIR 2.1.1 and the new PARI).

I cannot find obvious errors in the Makefile though; the relevant parts are identical to those of GMP btw, IIRC.

As another incident, I ran into this race condition again yesterday when building Sage 4.4.4 (!) from scratch with `MAKE="make -j16"`.



---

archive/issue_comments_078572.json:
```json
{
    "body": "W.r.t. the race condition, cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:324\n\n(I currently don't recall if I reported this elsewhere, or my results of inspecting the Makefile... :( )",
    "created_at": "2010-10-22T07:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78572",
    "user": "https://github.com/nexttime"
}
```

W.r.t. the race condition, cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:324

(I currently don't recall if I reported this elsewhere, or my results of inspecting the Makefile... :( )



---

archive/issue_comments_078573.json:
```json
{
    "body": "Replying to [comment:22 mpatel]:\n> I noticed that [MPIR 2.1.3 is out](http://www.mpir.org/) with a fix in `mpf_get_d_2exp`.  But I don't think Sage uses (m)any of the `mpf_*` functions.\n\n\nThat last statement is ***wrong***.  Bill Hart corrects me on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b40ef1bc8b0b7371/bdb322e7528a06bf#bdb322e7528a06bf):\n\n```\ncddlib, ecl, mpmath, mpfr, singular, sympy all, as far as I can see, make extensive use of mpf functions.\n```\nSorry about my mistake!",
    "created_at": "2010-11-03T22:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78573",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:22 mpatel]:
> I noticed that [MPIR 2.1.3 is out](http://www.mpir.org/) with a fix in `mpf_get_d_2exp`.  But I don't think Sage uses (m)any of the `mpf_*` functions.


That last statement is ***wrong***.  Bill Hart corrects me on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b40ef1bc8b0b7371/bdb322e7528a06bf#bdb322e7528a06bf):

```
cddlib, ecl, mpmath, mpfr, singular, sympy all, as far as I can see, make extensive use of mpf functions.
```
Sorry about my mistake!



---

archive/issue_comments_078574.json:
```json
{
    "body": "I would have taken the latest version anyway...\n\n---\n\nA trivial fix for the executable stack issue is to add the following to `spkg-install`:\n\n```sh\ncase \"$UNAME\" in\n    Linux) # implies a GNU linker\n        LDFLAGS=\"$LDFLAGS -Wl,z,noexecstack\"\n        # already exported by sage-env\n        ;;\n    # perhaps other platforms, too\nesac\n```",
    "created_at": "2010-11-03T23:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78574",
    "user": "https://github.com/nexttime"
}
```

I would have taken the latest version anyway...

---

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

archive/issue_comments_078575.json:
```json
{
    "body": "Copy and paste with typos included... It should of course be `-Wl,-z,noexecstack`.",
    "created_at": "2010-11-04T02:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78575",
    "user": "https://github.com/nexttime"
}
```

Copy and paste with typos included... It should of course be `-Wl,-z,noexecstack`.



---

archive/issue_comments_078576.json:
```json
{
    "body": "Changing keywords from \"\" to \"GMP ECM execstack Fedora 14\".",
    "created_at": "2010-11-04T06:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78576",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "" to "GMP ECM execstack Fedora 14".



---

archive/issue_comments_078577.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-04T06:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78577",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078578.json:
```json
{
    "body": "**New spkg: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p0.spkg**\n\n**md5sum:** `f65cbb309ee471d2a64f59e52e592494  mpir-2.1.3.p0.spkg`\n\nNew spkg with updated upstream, \"reviewer\" changes, fix for Fedora 14 (based on Mike's 2.1.1 spkg).\n\nSetting this to needs review though we still need a patch to the Sage library to fix the extension module dependencies. Can be tested \"stand-alone\" (with `SAGE_CHECK=yes`), but should be installed together with the new ECM 6.3 spkg from #5847 (also needing review by a third person), since otherwise ECM doesn't build (i.e., the old version doesn't work with GMP 5.x or MPIR 2.x).\n\nSteps to install:\n* Download the new MPIR spkg and the [ecm-6.3.p0.spkg](http://spkg-upload.googlecode.com/files/ecm-6.3.p0.spkg) from #5847.\n* Copy both files into `$SAGE_ROOT/spkg/standard` (such that 'make' will \"see\" them).\n* Then do:\n\n```sh\n$ export SAGE_CHECK=yes                # optional, but recommended\n$ export SAGE_UPGRADING=yes            # required to rebuild all dependent spkgs, too\n\n$ export SAGE_PARALLEL_SPKG_BUILD=yes  # optional\n$ export MAKE=\"make -jN\"               # optional; N: number of 'make' jobs\n\n$ time make build                      # just rebuild Sage (without the documentation)\n$                                      # (logs go to install.log and spkg/logs/*)\n$ ./sage -ba-force                     # rebuild the whole Sage library, necessary until\n                                       # we fix the dependencies in module_list.py\n$ time make ptestlong NUM_THREADS=N    # Use N threads instead of the default number\n                                       # (also rebuilds the documentation as needed)\n```\n* Report back... ;-)\n\n(I've so far tested both packages with Sage 4.6.1.alpha0 on Ubuntu 9.04 x86 and Ubuntu 10.04 x86_64.)",
    "created_at": "2010-11-04T06:45:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78578",
    "user": "https://github.com/nexttime"
}
```

**New spkg: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p0.spkg**

**md5sum:** `f65cbb309ee471d2a64f59e52e592494  mpir-2.1.3.p0.spkg`

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

archive/issue_comments_078579.json:
```json
{
    "body": "Attachment [trac_8664-mpir-2.1.1_vs._2.1.3.p0-spkg.patch](tarball://root/attachments/some-uuid/ticket8664/trac_8664-mpir-2.1.1_vs._2.1.3.p0-spkg.patch) by @nexttime created at 2010-11-04 06:47:36\n\nSPKG patch, based on Mike's 2.1.1. For reference/review.",
    "created_at": "2010-11-04T06:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78579",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_8664-mpir-2.1.1_vs._2.1.3.p0-spkg.patch](tarball://root/attachments/some-uuid/ticket8664/trac_8664-mpir-2.1.1_vs._2.1.3.p0-spkg.patch) by @nexttime created at 2010-11-04 06:47:36

SPKG patch, based on Mike's 2.1.1. For reference/review.



---

archive/issue_comments_078580.json:
```json
{
    "body": "Ooops, I just noticed the hint to rerun `make` if the **install** failed is in the wrong place (it is actually shown if the **build** failed), but that's IMHO a minor issue I'll perhaps fix later.",
    "created_at": "2010-11-04T07:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78580",
    "user": "https://github.com/nexttime"
}
```

Ooops, I just noticed the hint to rerun `make` if the **install** failed is in the wrong place (it is actually shown if the **build** failed), but that's IMHO a minor issue I'll perhaps fix later.



---

archive/issue_comments_078581.json:
```json
{
    "body": "Built and tested on sage.math.washington.edu without problems.",
    "created_at": "2010-11-04T15:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78581",
    "user": "https://github.com/jdemeyer"
}
```

Built and tested on sage.math.washington.edu without problems.



---

archive/issue_comments_078582.json:
```json
{
    "body": "Attachment [trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch](tarball://root/attachments/some-uuid/ticket8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch) by @nexttime created at 2010-11-04 19:58:26\n\nSage library patch. Fixes extension modules not getting rebuilt though depending on MPIR. Based on Sage 4.6.1.alpha0.",
    "created_at": "2010-11-04T19:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78582",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch](tarball://root/attachments/some-uuid/ticket8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch) by @nexttime created at 2010-11-04 19:58:26

Sage library patch. Fixes extension modules not getting rebuilt though depending on MPIR. Based on Sage 4.6.1.alpha0.



---

archive/issue_comments_078583.json:
```json
{
    "body": "Changing keywords from \"GMP ECM execstack Fedora 14\" to \"GMP ECM execstack Fedora 14 extension module library dependencies\".",
    "created_at": "2010-11-04T20:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78583",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "GMP ECM execstack Fedora 14" to "GMP ECM execstack Fedora 14 extension module library dependencies".



---

archive/issue_comments_078584.json:
```json
{
    "body": "Replying to [comment:29 leif]:\n> Setting this to needs review though we still need a patch to the Sage library to fix the extension module dependencies. [...]\n\n\nI've attached a patch that fixes the dependency issue with extension modules of the Sage library.\n\n\n**Updated steps to test / install:**\n* Download the [new MPIR spkg](http://spkg-upload.googlecode.com/files/mpir-2.1.3.p0.spkg) and the [ecm-6.3.p0.spkg](http://spkg-upload.googlecode.com/files/ecm-6.3.p0.spkg) from #5847.\n* Copy both files into `$SAGE_ROOT/spkg/standard` (such that `make` will \"see\" them).\n* Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). **Do not yet apply the patch.** (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)\n* Then do:\n\n```sh\n$ export SAGE_CHECK=yes                # optional, but recommended\n$ export SAGE_UPGRADING=yes            # required to rebuild all dependent spkgs, too\n\n$ export SAGE_PARALLEL_SPKG_BUILD=yes  # optional\n$ export MAKE=\"make -jN\"               # optional; N: number of 'make' jobs\n\n$ time make build                      # just rebuild Sage (without the documentation)\n$                                      # (logs go to install.log and spkg/logs/*)\n$ cd devel/sage\n$ hg import /path/to/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch\n$ cd ../..\n$ ./sage -b                            # rebuild the Sage library; only dependent modules\n\n$ time make ptestlong NUM_THREADS=N    # Use N threads instead of the default number\n                                       # (also rebuilds the documentation as needed)\n```\n* Report back... ;-)",
    "created_at": "2010-11-04T20:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78584",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:29 leif]:
> Setting this to needs review though we still need a patch to the Sage library to fix the extension module dependencies. [...]


I've attached a patch that fixes the dependency issue with extension modules of the Sage library.


**Updated steps to test / install:**
* Download the [new MPIR spkg](http://spkg-upload.googlecode.com/files/mpir-2.1.3.p0.spkg) and the [ecm-6.3.p0.spkg](http://spkg-upload.googlecode.com/files/ecm-6.3.p0.spkg) from #5847.
* Copy both files into `$SAGE_ROOT/spkg/standard` (such that `make` will "see" them).
* Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). **Do not yet apply the patch.** (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)
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

archive/issue_comments_078585.json:
```json
{
    "body": "Replying to [comment:32 jdemeyer]:\n\nDon't mess with my ticket while I'm posting... ;-)\n\nCan you (or did you) include the patch to the Sage library?",
    "created_at": "2010-11-04T20:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78585",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:32 jdemeyer]:

Don't mess with my ticket while I'm posting... ;-)

Can you (or did you) include the patch to the Sage library?



---

archive/issue_comments_078586.json:
```json
{
    "body": "P.S.: My patch shouldn't conflict with #10094, only the line numbers will change.",
    "created_at": "2010-11-04T20:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78586",
    "user": "https://github.com/nexttime"
}
```

P.S.: My patch shouldn't conflict with #10094, only the line numbers will change.



---

archive/issue_comments_078587.json:
```json
{
    "body": "Replying to [comment:33 leif]:\n>  * Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). **Do not yet apply the patch.** (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)\n\n\nPlease explain.  When can `setup.py` be overwritten?  This patched-files-being-overwritten-thing has bitten me already several times.",
    "created_at": "2010-11-04T20:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78587",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:33 leif]:
>  * Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). **Do not yet apply the patch.** (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)


Please explain.  When can `setup.py` be overwritten?  This patched-files-being-overwritten-thing has bitten me already several times.



---

archive/issue_comments_078588.json:
```json
{
    "body": "Replying to [comment:36 jdemeyer]:\n> Replying to [comment:33 leif]:\n> >  * Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). **Do not yet apply the patch.** (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)\n \n> \n> Please explain.  When can `setup.py` be overwritten?  This patched-files-being-overwritten-thing has bitten me already several times.\n\n\nI can only cite from the Sage library's `spkg-install`: ;-)\n\n```python\n...\n    sage -sync-build\n\n    # Pull in changes from the archive just downloaded. \n    hg pull \"$CUR\"\n    hg merge tip\n    hg ci -m \"merge\"\n    # Make the pulled in changes take effect. \n    hg update \n...\n```\n\n`sage -sync-build` calls `local/bin/sage-sync-build.py`.",
    "created_at": "2010-11-04T20:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78588",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:36 jdemeyer]:
> Replying to [comment:33 leif]:
> >  * Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). **Do not yet apply the patch.** (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)
 
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

archive/issue_comments_078589.json:
```json
{
    "body": "Replying to [comment:38 leif]:\n> I can only cite from the Sage library's `spkg-install`: ;-)\n\n\n*\"In principle\"*<sup>TM</sup>, this shouldn't invalidate newer patches already applied (and committed) to the Sage library.",
    "created_at": "2010-11-04T21:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78589",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:38 leif]:
> I can only cite from the Sage library's `spkg-install`: ;-)


*"In principle"*<sup>TM</sup>, this shouldn't invalidate newer patches already applied (and committed) to the Sage library.



---

archive/issue_comments_078590.json:
```json
{
    "body": "Replying to [comment:34 leif]:\n> Can you include the patch to the Sage library?\n\n\nNow it should be also merged, same spkg file.",
    "created_at": "2010-11-04T22:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78590",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:34 leif]:
> Can you include the patch to the Sage library?


Now it should be also merged, same spkg file.



---

archive/issue_comments_078591.json:
```json
{
    "body": "Does the problem in [comment:22 comment 22] occur during `$MAKE install`?",
    "created_at": "2010-11-04T23:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78591",
    "user": "https://github.com/qed777"
}
```

Does the problem in [comment:22 comment 22] occur during `$MAKE install`?



---

archive/issue_comments_078592.json:
```json
{
    "body": "Replying to [comment:41 mpatel]:\n> Does the problem in [comment:22 comment 22] occur during `$MAKE install`?\n\n\nI have not encountered this problem (yet), I've built on `sage.math.washington.edu` without problems.\n\nIf you feel like it, you could put [http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.1.alpha0-mpir/sage-4.6.1.alpha0-mpir.tar](http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.1.alpha0-mpir/sage-4.6.1.alpha0-mpir.tar) on the buildbots and see what happens...",
    "created_at": "2010-11-04T23:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78592",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:41 mpatel]:
> Does the problem in [comment:22 comment 22] occur during `$MAKE install`?


I have not encountered this problem (yet), I've built on `sage.math.washington.edu` without problems.

If you feel like it, you could put [http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.1.alpha0-mpir/sage-4.6.1.alpha0-mpir.tar](http://sage.math.washington.edu/home/jdemeyer/release/sage-4.6.1.alpha0-mpir/sage-4.6.1.alpha0-mpir.tar) on the buildbots and see what happens...



---

archive/issue_comments_078593.json:
```json
{
    "body": "Replying to [comment:41 mpatel]:\n> Does the problem in [comment:22 comment 22] occur during `$MAKE install`?\n\n\n```sh\n(cd /home/mpatel/build/cleo/sage-4.6.alpha2/local/include  && rm -f gmp.h   && cp mpir.h   gmp.h)\n/usr/bin/install -c -m 644 'mpir.h' '/home/mpatel/build/cleo/sage-4.6.alpha2/local/include/mpir.h'\n```\n\nSmells like it does, doesn't it? ;-)\n\nOr did I misunderstand you? (As mentioned in a comment above, the hint to rerun `make` is given in the wrong situation.)\n\n```diff\ndiff --git a/spkg-install b/spkg-install\n--- a/spkg-install\n+++ b/spkg-install\n@@ -123,18 +123,6 @@\n     $MAKE\n     if [ $? -ne 0 ]; then\n         echo \"Error building MPIR.\"\n-        echo \"\"\n-        echo \"If you see a message like:\"\n-        cat <<EOF\n-    cp: cannot stat 'mpir.h': No such file or directory\n-    make[6]: *** [install-data-hook] Error 1\n-    make[6]: Leaving directory ...\n-    make[5]: *** [install-data-am] Error 2\n-    make[5]: *** Waiting for unfinished jobs....\n-EOF\n-        echo \"above, this is just due to a rare race condition.\"\n-        echo \"Please simply rerun 'make' (or 'sage -i ...').\"\n-        echo \"\"\n         exit 1\n     fi \n \n@@ -146,6 +134,18 @@\n     if [ $? -ne 0 ]; then\n         if [ \"$UNAME\" != \"CYGWIN\" ]; then  # On Cygwin an error is not fatal.\n             echo \"Error installing MPIR.\"\n+            echo \"\"\n+            echo \"If you see a message like:\"\n+            cat <<EOF\n+    cp: cannot stat 'mpir.h': No such file or directory\n+    make[6]: *** [install-data-hook] Error 1\n+    make[6]: Leaving directory ...\n+    make[5]: *** [install-data-am] Error 2\n+    make[5]: *** Waiting for unfinished jobs....\n+EOF\n+            echo \"above, this is just due to a rare race condition.\"\n+            echo \"Please simply rerun 'make' (or 'sage -i ...').\"\n+            echo \"\"\n             exit 1\n         fi\n     fi\n```",
    "created_at": "2010-11-05T00:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78593",
    "user": "https://github.com/nexttime"
}
```

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
@@ -123,18 +123,6 @@
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
 
@@ -146,6 +134,18 @@
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

archive/issue_comments_078594.json:
```json
{
    "body": "Replying to [comment:43 leif]:\n> Replying to [comment:41 mpatel]:\n> Or did I misunderstand you? (As mentioned in a comment above, the hint to rerun `make` is given in the wrong situation.)\n\n\nOooops, I missed [comment:30 your comment].  Thanks for pointing it out.",
    "created_at": "2010-11-05T00:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78594",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:43 leif]:
> Replying to [comment:41 mpatel]:
> Or did I misunderstand you? (As mentioned in a comment above, the hint to rerun `make` is given in the wrong situation.)


Oooops, I missed [comment:30 your comment].  Thanks for pointing it out.



---

archive/issue_comments_078595.json:
```json
{
    "body": "Any reason to keep\n\n```sh\n    SAGE_CONF_OPTS=\"--enable-shared --disable-static\"\n```\n(i.e., why not build the static library, too)?",
    "created_at": "2010-11-05T03:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78595",
    "user": "https://github.com/nexttime"
}
```

Any reason to keep

```sh
    SAGE_CONF_OPTS="--enable-shared --disable-static"
```
(i.e., why not build the static library, too)?



---

archive/issue_comments_078596.json:
```json
{
    "body": "Replying to [comment:33 leif]:\n\nI tried to build mpir-2.1.3.p0.spkg on MacOSX 10.5 PPC, and it did not work; \nsage -f mpir-2.1.3.p0.spkg bails out  with the following:\n\n```\n...\n gcc -std=gnu99 -c -DHAVE_CONFIG_H -g -O3 -D__GMP_WITHIN_GMP -I.. -DOPERATION_popcount -I. -I.. tmp-popcount.s -fno-common -DPIC -o .libs/popcount.o\ntmp-popcount.s:127:vspltisb vector instruction is optional for the PowerPC (not allowed without -force_cpusubtype_ALL option)\ntmp-popcount.s:128:vspltisb vector instruction is optional for the PowerPC (not allowed without -force_cpusubtype_ALL option)\n\n... etc etc etc ...\n\ntmp-popcount.s:239:stvx vector instruction is optional for the PowerPC (not allowed without -force_cpusubtype_ALL option)\nmake[2]: *** [popcount.lo] Error 1\nmake[1]: *** [all-recursive] Error 1\nmake: *** [all] Error 2\nError building MPIR.\n\n```",
    "created_at": "2010-11-05T17:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78596",
    "user": "https://github.com/dimpase"
}
```

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

archive/issue_comments_078597.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-05T17:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78597",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078598.json:
```json
{
    "body": "Replying to [comment:47 dimpase]:\n> Replying to [comment:33 leif]:\n> \n> I tried to build mpir-2.1.3.p0.spkg on MacOSX 10.5 PPC, and it did not work; \n> sage -f mpir-2.1.3.p0.spkg bails out  with [...]\n\n{{{\n...\ntmp-popcount.s:127:vspltisb vector instruction is optional for the PowerPC (not allowed without -force_cpusubtype_ALL option)\n...\n}}}\n\nThanks for testing this.\n\nWould adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work? (Unless `SAGE_FAT_BINARY=yes`... Don't know what to do in that case, i.e. if `--enable-fat` works in that case, too.)\n\n(I think PPC implies [32-bit] MacOS X 10.4 or 10.5 in Sage.)\n\nOr do we have to make further distinctions on the CPU type?\n\nFor 32-bit **x86** builds on MacOS X < 10.6 we currently remove a lot of assembly files:\n\n```sh\nremove_pic_osx_32_bit()\n{\n    # Assumes we are in src/\n    echo \"Deleting assembly files which depend on PIC assembly\" \\\n        \"working or 32 bit OSX on Intel hardware...\"\n    rm mpn/x86/dive_1.asm \n    rm mpn/x86/diveby3.asm \n    rm mpn/x86/pentium4/sse2/dive_1.asm \n    rm mpn/x86/pentium4/sse2/mode1o.asm \n    rm mpn/x86/pentium4/sse2/diveby3.asm \n    rm mpn/x86/pentium4/mmx/popham.asm \n    rm mpn/x86/pentium4/mmx/rshift.asm\n    rm mpn/x86/p6/mode1o.asm\n    rm mpn/x86/p6/dive_1.asm\n    rm mpn/x86/pentium/hamdist.asm\n    rm mpn/x86/pentium/mod_1.asm\n    rm mpn/x86/pentium/popcount.asm\n    rm mpn/x86/pentium/mode1o.asm\n    rm mpn/x86/pentium/dive_1.asm\n}\n```\n\nWe should report this upstream. Bill, can you forward this?",
    "created_at": "2010-11-05T19:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78598",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:47 dimpase]:
> Replying to [comment:33 leif]:
> 
> I tried to build mpir-2.1.3.p0.spkg on MacOSX 10.5 PPC, and it did not work; 
> sage -f mpir-2.1.3.p0.spkg bails out  with [...]

{{{
...
tmp-popcount.s:127:vspltisb vector instruction is optional for the PowerPC (not allowed without -force_cpusubtype_ALL option)
...
}}}

Thanks for testing this.

Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work? (Unless `SAGE_FAT_BINARY=yes`... Don't know what to do in that case, i.e. if `--enable-fat` works in that case, too.)

(I think PPC implies [32-bit] MacOS X 10.4 or 10.5 in Sage.)

Or do we have to make further distinctions on the CPU type?

For 32-bit **x86** builds on MacOS X < 10.6 we currently remove a lot of assembly files:

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

archive/issue_comments_078599.json:
```json
{
    "body": "Replying to [comment:48 leif]:\n> Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?\n\n\nI.e.\n\n```sh\n$ env CFLAGS=\"-Wa,-force_cpusubtype_ALL\" ./sage -f mpir-2.1.3.p0.spkg\n```\n\nEven if this works for you, I'm not sure if MPIR only enables that code on CPUs that really support these instructions. Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.",
    "created_at": "2010-11-05T19:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78599",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:48 leif]:
> Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?


I.e.

```sh
$ env CFLAGS="-Wa,-force_cpusubtype_ALL" ./sage -f mpir-2.1.3.p0.spkg
```

Even if this works for you, I'm not sure if MPIR only enables that code on CPUs that really support these instructions. Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.



---

archive/issue_comments_078600.json:
```json
{
    "body": "Replying to [comment:49 leif]:\n> Replying to [comment:48 leif]:\n> > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?\n\n> \n> \n> Even if this works for you, I'm not sure if MPIR only enables that code on CPUs that really support these instructions. Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.\n\n\nyes, it at least builds without errors this way, on MacOSX 10.5 G4 PPC, with gcc 4.2.1 (Apple Inc. build 5577).\nTell me what I should test. (I don't want to rerun the whole Sage testsuite, as it takes ages on this machine, and I use it otherwise too)",
    "created_at": "2010-11-05T20:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78600",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:49 leif]:
> Replying to [comment:48 leif]:
> > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?

> 
> 
> Even if this works for you, I'm not sure if MPIR only enables that code on CPUs that really support these instructions. Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.


yes, it at least builds without errors this way, on MacOSX 10.5 G4 PPC, with gcc 4.2.1 (Apple Inc. build 5577).
Tell me what I should test. (I don't want to rerun the whole Sage testsuite, as it takes ages on this machine, and I use it otherwise too)



---

archive/issue_comments_078601.json:
```json
{
    "body": "Replying to [comment:49 leif]:\n> Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.\n\nYes, I did.  If it helps, I've put the log at [http://sage.math.washington.edu/home/jdemeyer/moufang/mpir-2.1.3.p0.log](http://sage.math.washington.edu/home/jdemeyer/moufang/mpir-2.1.3.p0.log).",
    "created_at": "2010-11-05T20:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78601",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:49 leif]:
> Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.

Yes, I did.  If it helps, I've put the log at [http://sage.math.washington.edu/home/jdemeyer/moufang/mpir-2.1.3.p0.log](http://sage.math.washington.edu/home/jdemeyer/moufang/mpir-2.1.3.p0.log).



---

archive/issue_comments_078602.json:
```json
{
    "body": "Replying to [comment:50 dimpase]:\n> Replying to [comment:49 leif]:\n> > Replying to [comment:48 leif]:\n> > > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?\n\n> > \n> > \n> > Even if this works for you, I'm not sure if MPIR only enables that code on CPUs that really support these instructions. Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.\n\n> \n> yes, it at least builds without errors this way, on MacOSX 10.5 G4 PPC, with gcc 4.2.1 (Apple Inc. build 5577).\n> Tell me what I should test. (I don't want to rerun the whole Sage testsuite, as it takes ages on this machine, and I use it otherwise too)\n\n\nNice, thanks.\n\nDid you run MPIR's test suite (i.e., installed with `SAGE_CHECK=yes`)?\n\nI'll update the ECM package (#5847) with the upstream patch, then you could also test this.\n\nI don't know if you already broke your Sage installation by now having successfully installed the new MPIR, since we delete all older versions, which other parts of Sage will still try to use unless you also rebuild the dependent packages.\n\nYou can of course always force the reinstallation of the old MPIR (and ECM) package with `sage -f ...`, then Sage will again work as before.",
    "created_at": "2010-11-05T21:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78602",
    "user": "https://github.com/nexttime"
}
```

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

archive/issue_comments_078603.json:
```json
{
    "body": "Replying to [comment:52 leif]:\n> Replying to [comment:50 dimpase]:\n> > Replying to [comment:49 leif]:\n> > > Replying to [comment:48 leif]:\n> > > > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?\n\n\nP.S.: Does Apple's XCode `gcc` understand `-force_cpusubtype_ALL` (i.e., without `-Wa,`)?\n\nI just noticed at least recent \"originals\" do on Darwin, but it's perhaps safer to directly pass it to the assembler.\n\nStill need to now what happens on *Linux* PPC (with `gas`)...",
    "created_at": "2010-11-05T21:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78603",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:52 leif]:
> Replying to [comment:50 dimpase]:
> > Replying to [comment:49 leif]:
> > > Replying to [comment:48 leif]:
> > > > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?


P.S.: Does Apple's XCode `gcc` understand `-force_cpusubtype_ALL` (i.e., without `-Wa,`)?

I just noticed at least recent "originals" do on Darwin, but it's perhaps safer to directly pass it to the assembler.

Still need to now what happens on *Linux* PPC (with `gas`)...



---

archive/issue_comments_078604.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-06T02:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78604",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078605.json:
```json
{
    "body": "**New spkg with Darwin fixes: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p1.spkg**\n\n**md5sum:** `0f13106ed6c8af933f93fa4a8981c453  mpir-2.1.3.p1.spkg`\n\nI've uploaded a new p1 spkg that fixes the assembler error on Darwin PPC. [Attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) reflects changes between this and the previous one (p0). Use [this link](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) to *download or apply* the patch.\n\n---\n\n### mpir-2.1.3.p1 (Leif Leonhardy, November 5th, 2010)\n* #8664: Upgrade Sage's MPIR spkg to version 2.1.3\n* Fix Darwin assembler errors on PPC by passing the option to allow\n  use of extended instruction set to it. (See also #5847.)\n* Enable the build of a static MPIR library, to be e.g. used by ECM.\n* Support additional 'configure' options given by MPIR_EXTRA_OPTS,\n  and print messages how we configure.\n* Print various environment variable settings (CC, CFLAGS et al.).\n* Move hint to rerun 'make' on *install* errors to correct place.\n* Further comments added.",
    "created_at": "2010-11-06T02:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78605",
    "user": "https://github.com/nexttime"
}
```

**New spkg with Darwin fixes: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p1.spkg**

**md5sum:** `0f13106ed6c8af933f93fa4a8981c453  mpir-2.1.3.p1.spkg`

I've uploaded a new p1 spkg that fixes the assembler error on Darwin PPC. [Attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) reflects changes between this and the previous one (p0). Use [this link](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) to *download or apply* the patch.

---

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

archive/issue_comments_078606.json:
```json
{
    "body": "P.S.: Except for the filename, test / installation instructions remain the same. (See [above](http://trac.sagemath.org/sage_trac/ticket/8664#comment:33).)",
    "created_at": "2010-11-06T02:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78606",
    "user": "https://github.com/nexttime"
}
```

P.S.: Except for the filename, test / installation instructions remain the same. (See [above](http://trac.sagemath.org/sage_trac/ticket/8664#comment:33).)



---

archive/issue_comments_078607.json:
```json
{
    "body": "Replying to [comment:54 leif]:\n> **New spkg with Darwin fixes: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p1.spkg**\n> \n> **md5sum:** `0f13106ed6c8af933f93fa4a8981c453  mpir-2.1.3.p1.spkg`\n> \n> I've uploaded a new p1 spkg that fixes the assembler error on Darwin PPC. [Attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) reflects changes between this and the previous one (p0). Use [this link](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) to *download or apply* the patch.\n\n\nThis won't work just like this. Ineed: \n\n```\n$ uname -m                  \nPower Macintosh\n$ uname -a                \nDarwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh\n```\n\nso it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...",
    "created_at": "2010-11-06T04:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78607",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:54 leif]:
> **New spkg with Darwin fixes: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p1.spkg**
> 
> **md5sum:** `0f13106ed6c8af933f93fa4a8981c453  mpir-2.1.3.p1.spkg`
> 
> I've uploaded a new p1 spkg that fixes the assembler error on Darwin PPC. [Attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) reflects changes between this and the previous one (p0). Use [this link](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) to *download or apply* the patch.


This won't work just like this. Ineed: 

```
$ uname -m                  
Power Macintosh
$ uname -a                
Darwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh
```

so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...



---

archive/issue_comments_078608.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-06T04:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78608",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078609.json:
```json
{
    "body": "Replying to [comment:52 leif]:\n> Replying to [comment:50 dimpase]:\n> > Replying to [comment:49 leif]:\n> > > Replying to [comment:48 leif]:\n> > > > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?\n\n> > > \n> > > \n> > > Even if this works for you, I'm not sure if MPIR only enables that code on CPUs that really support these instructions. Jeroen apparently has built this spkg on a MacOS X 10.4 PPC G5.\n\n> > \n> > yes, it at least builds without errors this way, on MacOSX 10.5 G4 PPC, with gcc 4.2.1 (Apple Inc. build 5577).\n> > Tell me what I should test. (I don't want to rerun the whole Sage testsuite, as it takes ages on this machine, and I use it otherwise too)\n\n> \n> Nice, thanks.\n> \n> Did you run MPIR's test suite (i.e., installed with `SAGE_CHECK=yes`)?\n\n\nI just re-run the installation of p0 with SAGE_CHECK=yes, and all the tests passed.\nSo I suppose it's very close, only that small config fix remains...\n\n\n> \n> I'll update the ECM package (#5847) with the upstream patch, then you could also test this.\n> \n> I don't know if you already broke your Sage installation by now having successfully installed the new MPIR, since we delete all older versions, which other parts of Sage will still try to use unless you also rebuild the dependent packages.\n> \n> You can of course always force the reinstallation of the old MPIR (and ECM) package with `sage -f ...`, then Sage will again work as before.\n\n\nThanks for the reminder, but I am quite familiar with sage -f, spkg-install,  etc etc... I am involved in maintaining of *gap*.spkg and cvxopt*.spkg...",
    "created_at": "2010-11-06T04:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78609",
    "user": "https://github.com/dimpase"
}
```

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

archive/issue_comments_078610.json:
```json
{
    "body": "Replying to [comment:56 dimpase]:\n> This won't work just like this. Ineed: \n\n{{{\n$ uname -m                  \nPower Macintosh\n$ uname -a                \nDarwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh\n}}}\n> \n> so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...\n\n\nWTF? *Which* `uname`? Some Apple XXXX?\n\nI've never seen *any* `configure` or `config.guess` script testing for \"Power Macintosh\", since this is neither a CPU nor an architecture. (The space is nice, too.)\n\nI'll make a special case for your machine... ;-)\n\n[Ok, I've searched now and the only one I've found is Singular's. Some others test for `Power*`.]",
    "created_at": "2010-11-06T05:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78610",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:56 dimpase]:
> This won't work just like this. Ineed: 

{{{
$ uname -m                  
Power Macintosh
$ uname -a                
Darwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh
}}}
> 
> so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...


WTF? *Which* `uname`? Some Apple XXXX?

I've never seen *any* `configure` or `config.guess` script testing for "Power Macintosh", since this is neither a CPU nor an architecture. (The space is nice, too.)

I'll make a special case for your machine... ;-)

[Ok, I've searched now and the only one I've found is Singular's. Some others test for `Power*`.]



---

archive/issue_comments_078611.json:
```json
{
    "body": "Replying to [comment:57 dimpase]:\n> Replying to [comment:52 leif]:\n> > I don't know if you already broke your Sage installation by now having successfully installed the new MPIR, since we delete all older versions, which other parts of Sage will still try to use unless you also rebuild the dependent packages.\n> > \n> > You can of course always force the reinstallation of the old MPIR (and ECM) package with `sage -f ...`, then Sage will again work as before.\n\n> \n> Thanks for the reminder, but I am quite familiar with sage -f, spkg-install,  etc etc... I am involved in maintaining of *gap*.spkg and cvxopt*.spkg...\n\n\n:-) Certainly, just ignore... (cf.[this nice comment](http://trac.sagemath.org/sage_trac/ticket/9921#comment:7))\n\nBut there are other people less familiar with this. (In fact this is a slightly modified copy of what I mailed someone else. I then became aware of not having it mentioned here at all.)",
    "created_at": "2010-11-06T05:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78611",
    "user": "https://github.com/nexttime"
}
```

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

archive/issue_comments_078612.json:
```json
{
    "body": "Replying to [comment:58 leif]:\n\n\n> > so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...\n\n> \n> WTF? *Which* `uname`? Some Apple XXXX?\n\n\nWhat a Terrible Failure indeed:\n\n/usr/bin/uname\n\nThe choice  \"Power Macintosh\" is undoubtedly the result of an out of court settlement between IBM and Apple :-)",
    "created_at": "2010-11-06T05:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78612",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:58 leif]:


> > so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...

> 
> WTF? *Which* `uname`? Some Apple XXXX?


What a Terrible Failure indeed:

/usr/bin/uname

The choice  "Power Macintosh" is undoubtedly the result of an out of court settlement between IBM and Apple :-)



---

archive/issue_comments_078613.json:
```json
{
    "body": "Replying to [comment:53 leif]:\n> Replying to [comment:52 leif]:\n> > Replying to [comment:50 dimpase]:\n> > > Replying to [comment:49 leif]:\n> > > > Replying to [comment:48 leif]:\n> > > > > Would adding `-Wa,-force_cpusubtype_ALL` on MacOS PPCs work?\n\n> \n> P.S.: Does Apple's XCode `gcc` understand `-force_cpusubtype_ALL` (i.e., without `-Wa,`)?\n\n\nyes Apple's gcc 4.2.1 does. As well as gcc-4.0.1, which is probably more usual on OSX PPC...",
    "created_at": "2010-11-06T06:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78613",
    "user": "https://github.com/dimpase"
}
```

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

archive/issue_comments_078614.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-06T06:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78614",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078615.json:
```json
{
    "body": "**Updated p1 spkg: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p1.spkg (same place)**\n\n**md5sum:** `08dfaa24301ba4e4481cfbbbc77156b3  mpir-2.1.3.p1.spkg`\n\nNow also recognizes PPCs giving \"`Power*`\" as `uname -m`.",
    "created_at": "2010-11-06T06:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78615",
    "user": "https://github.com/nexttime"
}
```

**Updated p1 spkg: http://spkg-upload.googlecode.com/files/mpir-2.1.3.p1.spkg (same place)**

**md5sum:** `08dfaa24301ba4e4481cfbbbc77156b3  mpir-2.1.3.p1.spkg`

Now also recognizes PPCs giving "`Power*`" as `uname -m`.



---

archive/issue_comments_078616.json:
```json
{
    "body": "Replying to [comment:60 dimpase]:\n> Replying to [comment:58 leif]:\n> \n> \n> > > so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...\n\n> > \n> > WTF? *Which* `uname`? Some Apple XXXX?\n\n> \n> What a Terrible Failure indeed:\n> \n> /usr/bin/uname\n\n\nWhat do `/bin/uname` and `/usr/local/bin/uname` give? \n\n(Consider installing GNU coreutils, and / or perhaps changing the `PATH`... ;-) )\n\nThere are other packages in Sage that won't recognize \"Power Macintosh\".\n\n\n> The choice  \"Power Macintosh\" is undoubtedly the result of an out of court settlement between IBM and Apple :-)\n\n\nWell, POWER<sup>TM</sup> is IBMs; the PowerPC was a later joint venture of Apple, IBM and Motorola.",
    "created_at": "2010-11-06T06:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78616",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:60 dimpase]:
> Replying to [comment:58 leif]:
> 
> 
> > > so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...

> > 
> > WTF? *Which* `uname`? Some Apple XXXX?

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

archive/issue_comments_078617.json:
```json
{
    "body": "Attachment [trac_8664-mpir-2.1.3.p0-p1.spkg.patch](tarball://root/attachments/some-uuid/ticket8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) by @nexttime created at 2010-11-06 06:45:51\n\nSPKG patch. Apply to MPIR 2.1.3.p0 to get the p1. Fixes Darwin assembler error, corrects hint; some improvements.",
    "created_at": "2010-11-06T06:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78617",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_8664-mpir-2.1.3.p0-p1.spkg.patch](tarball://root/attachments/some-uuid/ticket8664/trac_8664-mpir-2.1.3.p0-p1.spkg.patch) by @nexttime created at 2010-11-06 06:45:51

SPKG patch. Apply to MPIR 2.1.3.p0 to get the p1. Fixes Darwin assembler error, corrects hint; some improvements.



---

archive/issue_comments_078618.json:
```json
{
    "body": "Replying to [comment:63 leif]:\n> Replying to [comment:60 dimpase]:\n> > Replying to [comment:58 leif]:\n> > \n> > \n> > > > so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...\n\n> > > \n> > > WTF? *Which* `uname`? Some Apple XXXX?\n\n> > \n> > What a Terrible Failure indeed:\n> > \n> > /usr/bin/uname\n\n> \n> What do `/bin/uname` and `/usr/local/bin/uname` give? \n> \n> (Consider installing GNU coreutils, and / or perhaps changing the `PATH`... ;-) )\n\n\nGNU's uname says:\n\n```\n$ /usr/local/bin/uname -m\nPower Macintosh\n$ /usr/local/bin/uname -a\nDarwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh powerpc PowerBook5,5 Darwin\n```\n\n> \n> There are other packages in Sage that won't recognize \"Power Macintosh\".\n> \n> \n> > The choice  \"Power Macintosh\" is undoubtedly the result of an out of court settlement between IBM and Apple :-)\n\n> \n> Well, POWER<sup>TM</sup> is IBMs; the PowerPC was a later joint venture of Apple, IBM and Motorola.",
    "created_at": "2010-11-06T07:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78618",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:63 leif]:
> Replying to [comment:60 dimpase]:
> > Replying to [comment:58 leif]:
> > 
> > 
> > > > so it's not 'ppc', it's 'Power Macintosh' on OSX 10.5, apparently...

> > > 
> > > WTF? *Which* `uname`? Some Apple XXXX?

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

archive/issue_comments_078619.json:
```json
{
    "body": "Replying to [comment:64 dimpase]:\n> GNU's uname says:\n\n{{{\n$ /usr/local/bin/uname -m\nPower Macintosh\n$ /usr/local/bin/uname -a\nDarwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh powerpc PowerBook5,5 Darwin\n}}}\n\nReport upstream... ;-)\n\nI should have added `[Pp]ower*` :/",
    "created_at": "2010-11-06T07:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78619",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:64 dimpase]:
> GNU's uname says:

{{{
$ /usr/local/bin/uname -m
Power Macintosh
$ /usr/local/bin/uname -a
Darwin cantor.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:57:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_PPC Power Macintosh powerpc PowerBook5,5 Darwin
}}}

Report upstream... ;-)

I should have added `[Pp]ower*` :/



---

archive/issue_comments_078620.json:
```json
{
    "body": "p1 builds and passes all tests on OSX 10.5 PPC (G4), with gcc-4.2.1.\nExcept that somewhere in the log I see:\n\n```\n...\nmake[4]: Entering directory `/usr/local/src/sage/sage-4.6/spkg/build/mpir-2.1.3.p1/src/tests/cxx'\n...\nPASS: t-istream\nReplacing decimal point didn't work, tests skipped\nPASS: t-locale\n...\n }}}\nThis does not happen on Debian x64.\nProbably a harmless (for Sage) C++-specific issue. Can this be ignored?",
    "created_at": "2010-11-06T07:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78620",
    "user": "https://github.com/dimpase"
}
```

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

archive/issue_comments_078621.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-11-06T07:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78621",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_078622.json:
```json
{
    "body": "however, Sage does not start on OSX 10.5 PPC: I get \n\n```\n$ ./sage -b\n...\ng++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/usr/local/src/sage/sage-4.6/local/lib -L/usr/local/src/sage/sage-4.6/local/lib/python/config -lntl -lgmp -lpari -lpython2.6\nld: file not found: /usr/local/src/sage/sage-4.6/local/lib/libgmp.3.dylib\ncollect2: ld returned 1 exit status\nscons: *** [libcsage.dylib] Error 1\nERROR: There was an error building c_lib.\n```\nI don't know whether this is a result of this spkg upgrade, or something else was broken even before. I'll see.",
    "created_at": "2010-11-06T07:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78622",
    "user": "https://github.com/dimpase"
}
```

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

archive/issue_comments_078623.json:
```json
{
    "body": "Replying to [comment:67 dimpase]:\n> however, Sage does not start on OSX 10.5 PPC: I get \n\n{{{\n$ ./sage -b\n...\ng++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/usr/local/src/sage/sage-4.6/local/lib -L/usr/local/src/sage/sage-4.6/local/lib/python/config -lntl -lgmp -lpari -lpython2.6\nld: file not found: /usr/local/src/sage/sage-4.6/local/lib/libgmp.3.dylib\ncollect2: ld returned 1 exit status\nscons: *** [libcsage.dylib] Error 1\nERROR: There was an error building c_lib.\n}}}\n> I don't know whether this is a result of this spkg upgrade, or something else was broken even before. I'll see.\n\n\nDid you rebuild all dependent packages, i.e. use `SAGE_UPGRADING=yes`?\n\nWhat MPIR versions do you have in `local/lib/`?\n\n---\n\nI guess the locale issue is a minor thing (hopefully). Perhaps Bill knows better.\n\n(I almost always build with `LC_ALL=C`.)",
    "created_at": "2010-11-06T08:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78623",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:67 dimpase]:
> however, Sage does not start on OSX 10.5 PPC: I get 

{{{
$ ./sage -b
...
g++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/usr/local/src/sage/sage-4.6/local/lib -L/usr/local/src/sage/sage-4.6/local/lib/python/config -lntl -lgmp -lpari -lpython2.6
ld: file not found: /usr/local/src/sage/sage-4.6/local/lib/libgmp.3.dylib
collect2: ld returned 1 exit status
scons: *** [libcsage.dylib] Error 1
ERROR: There was an error building c_lib.
}}}
> I don't know whether this is a result of this spkg upgrade, or something else was broken even before. I'll see.


Did you rebuild all dependent packages, i.e. use `SAGE_UPGRADING=yes`?

What MPIR versions do you have in `local/lib/`?

---

I guess the locale issue is a minor thing (hopefully). Perhaps Bill knows better.

(I almost always build with `LC_ALL=C`.)



---

archive/issue_comments_078624.json:
```json
{
    "body": "P.S.: Could you attach the full MPIR build log, or its `make install` part?",
    "created_at": "2010-11-06T09:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78624",
    "user": "https://github.com/nexttime"
}
```

P.S.: Could you attach the full MPIR build log, or its `make install` part?



---

archive/issue_comments_078625.json:
```json
{
    "body": "Replying to [comment:68 leif]:\n\n\n> Did you rebuild all dependent packages, i.e. use `SAGE_UPGRADING=yes`?\n\n\nI tried\n\n```\n$ SAGE_UPGRADING=yes ../../sage -f mpir-2.1.3.p1.spkg\n$ ../../sage -b\n```\nwith the same outcome. \nInstalling the version 1.* mpir spkg cures the installation, i.e. I get a working copy of Sage back.\n\n> \n> What MPIR versions do you have in `local/lib/`?\n\n\nhere are mpirs and gmps I have:\n \n```\n-rwxr-xr-x  1 dima  wheel   500140 Nov  6 18:48 ../../local/lib/libmpir.8.2.3.dylib\nlrwxr-xr-x  1 dima  wheel       19 Nov  6 18:48 ../../local/lib/libmpir.8.dylib -> libmpir.8.2.3.dylib\n-rw-r--r--  1 dima  wheel  2487088 Nov  6 18:48 ../../local/lib/libmpir.a\nlrwxr-xr-x  1 dima  wheel       19 Nov  6 18:48 ../../local/lib/libmpir.dylib -> libmpir.8.2.3.dylib\n-rwxr-xr-x  1 dima  wheel      829 Nov  6 18:48 ../../local/lib/libmpir.la\n-rwxr-xr-x  1 dima  wheel    25592 Nov  6 18:48 ../../local/lib/libmpirxx.2.2.11.dylib\nlrwxr-xr-x  1 dima  wheel       22 Nov  6 18:48 ../../local/lib/libmpirxx.2.dylib -> libmpirxx.2.2.11.dylib\n-rw-r--r--  1 dima  wheel   699424 Nov  6 18:48 ../../local/lib/libmpirxx.a\nlrwxr-xr-x  1 dima  wheel       22 Nov  6 18:48 ../../local/lib/libmpirxx.dylib -> libmpirxx.2.2.11.dylib\n-rwxr-xr-x  1 dima  wheel      894 Nov  6 18:48 ../../local/lib/libmpirxx.la\n\n-rwxr-xr-x  1 dima  wheel   500140 Nov  6 18:48 ../../local/lib/libgmp.8.2.3.dylib\nlrwxr-xr-x  1 dima  wheel       18 Nov  6 18:48 ../../local/lib/libgmp.8.dylib -> libgmp.8.2.3.dylib\n-rw-r--r--  1 dima  wheel  2487088 Nov  6 18:48 ../../local/lib/libgmp.a\nlrwxr-xr-x  1 dima  wheel       18 Nov  6 18:48 ../../local/lib/libgmp.dylib -> libgmp.8.2.3.dylib\n-rwxr-xr-x  1 dima  wheel      822 Nov  6 18:48 ../../local/lib/libgmp.la\n-rwxr-xr-x  1 dima  wheel    25592 Nov  6 18:48 ../../local/lib/libgmpxx.2.2.11.dylib\nlrwxr-xr-x  1 dima  wheel       21 Nov  6 18:48 ../../local/lib/libgmpxx.2.dylib -> libgmpxx.2.2.11.dylib\n-rw-r--r--  1 dima  wheel   699424 Nov  6 18:48 ../../local/lib/libgmpxx.a\nlrwxr-xr-x  1 dima  wheel       21 Nov  6 18:48 ../../local/lib/libgmpxx.dylib -> libgmpxx.2.2.11.dylib\n-rwxr-xr-x  1 dima  wheel      886 Nov  6 18:48 ../../local/lib/libgmpxx.la\n```\n\nI'm  trying the following:\n\n```\n$ cd local/lib\n$ ln -s libgmp.dylib libgmp.3.dylib\n$ ../../sage -b \n```\nand this seems to work (triggering a large recompile of extensions that still is running)",
    "created_at": "2010-11-06T11:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78625",
    "user": "https://github.com/dimpase"
}
```

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

archive/issue_comments_078626.json:
```json
{
    "body": "Replying to [comment:70 dimpase]:\n> Replying to [comment:68 leif]:\n> > Did you rebuild all dependent packages, i.e. use `SAGE_UPGRADING=yes`? \n\n> I tried\n\n```\n$ SAGE_UPGRADING=yes ../../sage -f mpir-2.1.3.p1.spkg\n$ ../../sage -b\n```\n> with the same outcome.\n\n\n`SAGE_UPGRADING=yes` only works with `make`, not `sage -i ...` etc. (and only if all [new] spkgs are in `spkg/standard/`).\n\n\n\n\n\n> Installing the version 1.* mpir spkg cures the installation, i.e. I get a working copy of Sage back.\n\n\nYep.\n\n\n\n\n> > What MPIR versions do you have in `local/lib/`?\n\n> \n> here are mpirs and gmps I have:\n\n{{{\n-rwxr-xr-x  1 dima  wheel   500140 Nov  6 18:48 ../../local/lib/libmpir.8.2.3.dylib\nlrwxr-xr-x  1 dima  wheel       19 Nov  6 18:48 ../../local/lib/libmpir.8.dylib -> libmpir.8.2.3.dylib\n-rw-r--r--  1 dima  wheel  2487088 Nov  6 18:48 ../../local/lib/libmpir.a\nlrwxr-xr-x  1 dima  wheel       19 Nov  6 18:48 ../../local/lib/libmpir.dylib -> libmpir.8.2.3.dylib\n-rwxr-xr-x  1 dima  wheel      829 Nov  6 18:48 ../../local/lib/libmpir.la\n-rwxr-xr-x  1 dima  wheel    25592 Nov  6 18:48 ../../local/lib/libmpirxx.2.2.11.dylib\nlrwxr-xr-x  1 dima  wheel       22 Nov  6 18:48 ../../local/lib/libmpirxx.2.dylib -> libmpirxx.2.2.11.dylib\n-rw-r--r--  1 dima  wheel   699424 Nov  6 18:48 ../../local/lib/libmpirxx.a\nlrwxr-xr-x  1 dima  wheel       22 Nov  6 18:48 ../../local/lib/libmpirxx.dylib -> libmpirxx.2.2.11.dylib\n-rwxr-xr-x  1 dima  wheel      894 Nov  6 18:48 ../../local/lib/libmpirxx.la\n...\n}}}\nThese are the correct new ones, same basenames as on other systems. (Note that the version number of `libgmpxx*` is now *smaller* than in MPIR 1.2.2, which was `3[.1.6]`.)\n\n\n\n\n \n> I'm  trying the following:\n\n{{{\n$ cd local/lib\n$ ln -s libgmp.dylib libgmp.3.dylib\n$ ../../sage -b \n}}}\n> and this seems to work (triggering a large recompile of extensions that still is running)\n\n\nSo the patch to the Sage library apparently works for you. :)\n\n---\n\nThe `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.\n\nCan you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?\n(Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be *below* MPIR's.)",
    "created_at": "2010-11-06T16:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78626",
    "user": "https://github.com/nexttime"
}
```

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

{{{
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
}}}
These are the correct new ones, same basenames as on other systems. (Note that the version number of `libgmpxx*` is now *smaller* than in MPIR 1.2.2, which was `3[.1.6]`.)




 
> I'm  trying the following:

{{{
$ cd local/lib
$ ln -s libgmp.dylib libgmp.3.dylib
$ ../../sage -b 
}}}
> and this seems to work (triggering a large recompile of extensions that still is running)


So the patch to the Sage library apparently works for you. :)

---

The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.

Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?
(Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be *below* MPIR's.)



---

archive/issue_comments_078627.json:
```json
{
    "body": "Replying to [comment:71 leif]:\n\n> The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.\n> \n> Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?\n> (Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be *below* MPIR's.)\n\n\nIs ecm-6.2.1 compatible with  mpir 2.1.3?\nJust wondering.\n\nI'm going to rebuild Sage from scratch and with mpir 2.1.3.\nIt will take a night, but it's already pretty later over here.",
    "created_at": "2010-11-06T17:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78627",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:71 leif]:

> The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.
> 
> Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?
> (Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be *below* MPIR's.)


Is ecm-6.2.1 compatible with  mpir 2.1.3?
Just wondering.

I'm going to rebuild Sage from scratch and with mpir 2.1.3.
It will take a night, but it's already pretty later over here.



---

archive/issue_comments_078628.json:
```json
{
    "body": "Replying to [comment:72 dimpase]:\n> Replying to [comment:71 leif]:\n> \n> > The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.\n> > \n> > Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?\n> > (Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be *below* MPIR's.)\n\n> \n> Is ecm-6.2.1 compatible with  mpir 2.1.3?\n\n\nRather not. (See #5847.)\n\n\n> I'm going to rebuild Sage from scratch and with mpir 2.1.3.\n> It will take a night, but it's already pretty later over here.\n\n\nYou could try faking ecm-6.3.p0.spkg (or the old one if you haven't copied the new spkg) was already installed, then at least the build should pass.",
    "created_at": "2010-11-06T17:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78628",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:72 dimpase]:
> Replying to [comment:71 leif]:
> 
> > The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.
> > 
> > Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?
> > (Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be *below* MPIR's.)

> 
> Is ecm-6.2.1 compatible with  mpir 2.1.3?


Rather not. (See #5847.)


> I'm going to rebuild Sage from scratch and with mpir 2.1.3.
> It will take a night, but it's already pretty later over here.


You could try faking ecm-6.3.p0.spkg (or the old one if you haven't copied the new spkg) was already installed, then at least the build should pass.



---

archive/issue_comments_078629.json:
```json
{
    "body": "I asked Bill by email about Leif's comments above.  Please see [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/892ce7f3c9c93b9f).",
    "created_at": "2010-11-06T20:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78629",
    "user": "https://github.com/qed777"
}
```

I asked Bill by email about Leif's comments above.  Please see [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/892ce7f3c9c93b9f).



---

archive/issue_comments_078630.json:
```json
{
    "body": "Replying to [comment:74 mpatel]:\n> I asked Bill by email about Leif's comments above.  Please see [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/892ce7f3c9c93b9f).\n\n\nI tried a vanilla build from the source, i.e. untarred the spkg, then\n\n```\n$ cd src/\n$ ./configure\n$ make\n```\nand it just works, picking up the flag -force_cpusubtype_ALL without any help.",
    "created_at": "2010-11-07T04:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78630",
    "user": "https://github.com/dimpase"
}
```

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

archive/issue_comments_078631.json:
```json
{
    "body": "Replying to [comment:72 dimpase]:\n> Replying to [comment:71 leif]:\n> \n> > The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.\n> > \n> > Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?\n> > (Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be *below* MPIR's.)\n\n> \n> Is ecm-6.2.1 compatible with  mpir 2.1.3?\n> Just wondering.\n> \n> I'm going to rebuild Sage from scratch and with mpir 2.1.3.\n> It will take a night, but it's already pretty later over here.\n> \n\n\nrebuilt Sage 4.6 from scratch with p1 spk of this ticket, the Sage library patch of this ticket applied to sage spkg, and with tweaked ECM spkg (see the ECM ticket). All works, as well as passes testlong (>12 hours on this machine).\n\nDima\n\nIt all worked, as well as all",
    "created_at": "2010-11-09T05:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78631",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:72 dimpase]:
> Replying to [comment:71 leif]:
> 
> > The `libcsage` linker error occurs because some other library (NTL or PARI) still refers to the old MPIR library, i.e. hasn't been rebuilt.
> > 
> > Can you check the modification times of `spkg/installed/*` (e.g. `ls -rtl spkg/installed`)?
> > (Or just `ls -1rt local/lib/lib{gmp,ntl,pari}*`; all PARI and NTL libraries should be *below* MPIR's.)

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

archive/issue_comments_078632.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-11-09T05:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78632",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_078633.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-09T05:08:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78633",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078634.json:
```json
{
    "body": "Replying to [comment:76 dimpase]:\n> and with tweaked ECM spkg (see #5847).\n\n\nWhich \"tweaked\" ECM spkg do you mean?",
    "created_at": "2010-11-09T08:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78634",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:76 dimpase]:
> and with tweaked ECM spkg (see #5847).


Which "tweaked" ECM spkg do you mean?



---

archive/issue_comments_078635.json:
```json
{
    "body": "Replying to [comment:79 jdemeyer]:\n> Replying to [comment:76 dimpase]:\n> > and with tweaked ECM spkg (see #5847).\n\n> \n> Which \"tweaked\" ECM spkg do you mean?\n\n\nThe one I made from the spkg on the ticket that 1) avoids the linker crash by supplying a longer assembler program in configure 2) runs ./configure --disable-asm-redc in spkg-install.\n\nI did not yet try the configure patch suggested by Paul:\n\n```\nin fact this bug is already fixed upstream (in revision 1516), see\n  https://gforge.inria.fr/tracker/index.php func=detail&aid=10646&group_id=135&atid=623\n```",
    "created_at": "2010-11-09T09:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78635",
    "user": "https://github.com/dimpase"
}
```

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

archive/issue_events_020985.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-11T13:02:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20985"
}
```



---

archive/issue_comments_078636.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-11T13:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78636",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_078637.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-11-12T13:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78637",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_020986.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-12T13:07:10Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20986"
}
```



---

archive/issue_comments_078638.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-11-12T13:07:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78638",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_078639.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-12T13:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78639",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078640.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-12T13:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78640",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078641.json:
```json
{
    "body": "Unmerged from sage-4.6.1.alpha1 because of the problems with the ECM package, see #10252.",
    "created_at": "2010-11-12T13:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78641",
    "user": "https://github.com/jdemeyer"
}
```

Unmerged from sage-4.6.1.alpha1 because of the problems with the ECM package, see #10252.



---

archive/issue_events_020987.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-20T10:06:09Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20987"
}
```



---

archive/issue_events_020988.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-20T10:06:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20988"
}
```



---

archive/issue_comments_078642.json:
```json
{
    "body": "Replying to [comment:25 leif]:\n> W.r.t. the race condition, cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:324\n> \n> (I currently don't recall if I reported this elsewhere, or my results of inspecting the Makefile... :( )\n\n\nI've reported the parallel `make install` error on [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/04928454886f34ab/e29bf19c2590d2d0?#e29bf19c2590d2d0).",
    "created_at": "2010-11-26T13:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78642",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:25 leif]:
> W.r.t. the race condition, cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:324
> 
> (I currently don't recall if I reported this elsewhere, or my results of inspecting the Makefile... :( )


I've reported the parallel `make install` error on [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/04928454886f34ab/e29bf19c2590d2d0?#e29bf19c2590d2d0).



---

archive/issue_comments_078643.json:
```json
{
    "body": "Replying to [comment:88 mpatel]:\n> Replying to [comment:25 leif]:\n> > W.r.t. the race condition, cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:324\n> > \n> > (I currently don't recall if I reported this elsewhere, or my results of inspecting the Makefile... :( )\n\n> \n> I've reported the parallel `make install` error on [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/04928454886f34ab/e29bf19c2590d2d0?#e29bf19c2590d2d0).\n\n\nJust yesterday ran into this for the first time on an old 32-bit single-core HT Pentium 4 (with 8 jobs); I previously only encountered it on Core2s with e.g. 16 or 32 jobs.",
    "created_at": "2010-11-26T13:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78643",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:88 mpatel]:
> Replying to [comment:25 leif]:
> > W.r.t. the race condition, cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:324
> > 
> > (I currently don't recall if I reported this elsewhere, or my results of inspecting the Makefile... :( )

> 
> I've reported the parallel `make install` error on [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/04928454886f34ab/e29bf19c2590d2d0?#e29bf19c2590d2d0).


Just yesterday ran into this for the first time on an old 32-bit single-core HT Pentium 4 (with 8 jobs); I previously only encountered it on Core2s with e.g. 16 or 32 jobs.



---

archive/issue_comments_078644.json:
```json
{
    "body": "Replying to [comment:89 leif]:\n> Replying to [comment:88 mpatel]:\n> > I've reported the parallel `make install` error on [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/04928454886f34ab/e29bf19c2590d2d0?#e29bf19c2590d2d0).\n\n> \n> Just yesterday ran into this for the first time on an old 32-bit single-core HT Pentium 4 (with 8 jobs); I previously only encountered it on Core2s with e.g. 16 or 32 jobs.\n\n\nThis has now been fixed in MPIR 2.1.4 (released today), but I'm not going to make any further changes *on this ticket*.\n\n(I'll open a follow-up ticket anyway, since I already have an MPIR 2.1.3.p2 spkg with other improvements; MPIR 2.2 is on the way, too.)",
    "created_at": "2010-12-01T20:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78644",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:89 leif]:
> Replying to [comment:88 mpatel]:
> > I've reported the parallel `make install` error on [mpir-devel](http://groups.google.com/group/mpir-devel/browse_thread/thread/04928454886f34ab/e29bf19c2590d2d0?#e29bf19c2590d2d0).

> 
> Just yesterday ran into this for the first time on an old 32-bit single-core HT Pentium 4 (with 8 jobs); I previously only encountered it on Core2s with e.g. 16 or 32 jobs.


This has now been fixed in MPIR 2.1.4 (released today), but I'm not going to make any further changes *on this ticket*.

(I'll open a follow-up ticket anyway, since I already have an MPIR 2.1.3.p2 spkg with other improvements; MPIR 2.2 is on the way, too.)



---

archive/issue_comments_078645.json:
```json
{
    "body": "Replying to [comment:90 leif]:\n> This has now been fixed in MPIR 2.1.4 (released today), but I'm not going to make any further changes *on this ticket*.\n\n\n> \n> (I'll open a follow-up ticket anyway, since I already have an MPIR 2.1.3.p2 spkg with other improvements; MPIR 2.2 is on the way, too.)\n\n\nMPIR 2.2.0 was released today... ;-)",
    "created_at": "2010-12-02T18:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78645",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:90 leif]:
> This has now been fixed in MPIR 2.1.4 (released today), but I'm not going to make any further changes *on this ticket*.


> 
> (I'll open a follow-up ticket anyway, since I already have an MPIR 2.1.3.p2 spkg with other improvements; MPIR 2.2 is on the way, too.)


MPIR 2.2.0 was released today... ;-)



---

archive/issue_comments_078646.json:
```json
{
    "body": "Replying to [comment:36 jdemeyer]:\n> Replying to [comment:33 leif]:\n> >  * Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). **Do not yet apply the patch.** (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)\n \n> \n> Please explain.  When can `setup.py` be overwritten?  This patched-files-being-overwritten-thing has bitten me already several times.\n\n\nA problem with `SAGE_UPGRADING` (whose \"external\" use is inofficial anyway) is that if the Sage library gets reinstalled because some of its dependencies got rebuilt (which is the typical case), Sage unconditionally switches back to the `main` branch without any warning, so previously applied patches to a clone take no longer effect (though they are still there, but no longer in the afterwards current branch, `sage-main`). It took me some time to realize that (or in fact track down weird errors caused by this)... ;-)\n\nThe Sage library's `spkg-install` should at least issue a warning when it switches the current branch; perhaps there should be some option to avoid this, since it is IMHO convenient to do e.g. `env SAGE_UPGRADING=yes make ptestlong` rather than patching the `main` branch or first building a new source distribution to build from scratch (or a new patched Sage library spkg to be installed).",
    "created_at": "2010-12-04T23:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78646",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:36 jdemeyer]:
> Replying to [comment:33 leif]:
> >  * Download the [patch to the Sage library](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib.patch). **Do not yet apply the patch.** (We first rebuild / reinstall dependent spkgs, of which the Sage library is one, so the patched version could get overwritten.)
 
> 
> Please explain.  When can `setup.py` be overwritten?  This patched-files-being-overwritten-thing has bitten me already several times.


A problem with `SAGE_UPGRADING` (whose "external" use is inofficial anyway) is that if the Sage library gets reinstalled because some of its dependencies got rebuilt (which is the typical case), Sage unconditionally switches back to the `main` branch without any warning, so previously applied patches to a clone take no longer effect (though they are still there, but no longer in the afterwards current branch, `sage-main`). It took me some time to realize that (or in fact track down weird errors caused by this)... ;-)

The Sage library's `spkg-install` should at least issue a warning when it switches the current branch; perhaps there should be some option to avoid this, since it is IMHO convenient to do e.g. `env SAGE_UPGRADING=yes make ptestlong` rather than patching the `main` branch or first building a new source distribution to build from scratch (or a new patched Sage library spkg to be installed).



---

archive/issue_comments_078647.json:
```json
{
    "body": "The old mpir spkg compiles with -march=<...>, the new spkg here doesn't do that.  That is definately a bug.",
    "created_at": "2011-01-12T19:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78647",
    "user": "https://github.com/jdemeyer"
}
```

The old mpir spkg compiles with -march=<...>, the new spkg here doesn't do that.  That is definately a bug.



---

archive/issue_comments_078648.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-12T19:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78648",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_078649.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-01-12T19:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78649",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_078650.json:
```json
{
    "body": "Replying to [comment:94 jdemeyer]:\n> The old mpir spkg compiles with -march=<...>, the new spkg here doesn't do that.  That is definately a bug.\n\n\nisn't mpir's config intelligent enough to figure out the right arch?",
    "created_at": "2011-01-12T19:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78650",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:94 jdemeyer]:
> The old mpir spkg compiles with -march=<...>, the new spkg here doesn't do that.  That is definately a bug.


isn't mpir's config intelligent enough to figure out the right arch?



---

archive/issue_comments_078651.json:
```json
{
    "body": "Replying to [comment:95 dimpase]:\n> isn't mpir's config intelligent enough to figure out the right arch?\n\n\nYes, but Sage's `CFLAGS` override `mpir`'s optimized `CFLAGS` (and this does not happen with the current mpir-1.2.2)",
    "created_at": "2011-01-12T20:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78651",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:95 dimpase]:
> isn't mpir's config intelligent enough to figure out the right arch?


Yes, but Sage's `CFLAGS` override `mpir`'s optimized `CFLAGS` (and this does not happen with the current mpir-1.2.2)



---

archive/issue_comments_078652.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2011-01-12T20:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78652",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_078653.json:
```json
{
    "body": "Replying to [comment:97 jdemeyer]:\n\nas MPIR is at version 2.3.1 already, should all this be rebased?\n(well, I don't know if it works with ECM 6.3...)\n\nDima",
    "created_at": "2011-04-18T16:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78653",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:97 jdemeyer]:

as MPIR is at version 2.3.1 already, should all this be rebased?
(well, I don't know if it works with ECM 6.3...)

Dima



---

archive/issue_comments_078654.json:
```json
{
    "body": "Probably, yes, it should be rebased.\n\nBut also the `CFLAGS` issue still needs to be fixed...",
    "created_at": "2011-04-18T16:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78654",
    "user": "https://github.com/jdemeyer"
}
```

Probably, yes, it should be rebased.

But also the `CFLAGS` issue still needs to be fixed...



---

archive/issue_comments_078655.json:
```json
{
    "body": "Replying to [comment:99 jdemeyer]:\n> Probably, yes, it should be rebased.\n> \n> But also the `CFLAGS` issue still needs to be fixed...\n\n\n8S See [my comment above](http://trac.sagemath.org/sage_trac/ticket/8664#comment:90).\n\nI still can't believe this ticket didn't get merged *month* ago, just because (apparently) nobody felt able to give the ECM one (#5847) a final positive review.\n\nThe `CFLAGS` (or `-march=`) issue is IMHO completely unrelated -- if not irrelevant. ;-)\n\nIt's easy to extract and merge the *relevant* parts of MPIR's `CFLAGS` without ignoring a user's settings, which I did in the follow-up spkg (IIRC), mentioned above.\n\nI'll try to take a look at its state during the next days; I'm currently not even sure if I hadn't already uploaded it onto google code...\n\nCheers.",
    "created_at": "2011-04-18T17:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78655",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:99 jdemeyer]:
> Probably, yes, it should be rebased.
> 
> But also the `CFLAGS` issue still needs to be fixed...


8S See [my comment above](http://trac.sagemath.org/sage_trac/ticket/8664#comment:90).

I still can't believe this ticket didn't get merged *month* ago, just because (apparently) nobody felt able to give the ECM one (#5847) a final positive review.

The `CFLAGS` (or `-march=`) issue is IMHO completely unrelated -- if not irrelevant. ;-)

It's easy to extract and merge the *relevant* parts of MPIR's `CFLAGS` without ignoring a user's settings, which I did in the follow-up spkg (IIRC), mentioned above.

I'll try to take a look at its state during the next days; I'm currently not even sure if I hadn't already uploaded it onto google code...

Cheers.



---

archive/issue_comments_078656.json:
```json
{
    "body": "Oh, not to mention #9858 (FLINT). :)\n\n(And I guess MPFR also still should be upgraded, an MPC spkg provided...)",
    "created_at": "2011-04-18T17:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78656",
    "user": "https://github.com/nexttime"
}
```

Oh, not to mention #9858 (FLINT). :)

(And I guess MPFR also still should be upgraded, an MPC spkg provided...)



---

archive/issue_comments_078657.json:
```json
{
    "body": "Replying to [comment:100 leif]:\n> The `CFLAGS` (or `-march=`) issue is IMHO completely unrelated -- if not irrelevant. ;-)\n\n\nThe current MPIR spkg *does* use machine-specific CFLAGS, the new spkg on this ticket *does not*.  This is a step backwards.\n\nIf you think it is irrelevant, please explain why...",
    "created_at": "2011-04-18T18:44:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78657",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:100 leif]:
> The `CFLAGS` (or `-march=`) issue is IMHO completely unrelated -- if not irrelevant. ;-)


The current MPIR spkg *does* use machine-specific CFLAGS, the new spkg on this ticket *does not*.  This is a step backwards.

If you think it is irrelevant, please explain why...



---

archive/issue_comments_078658.json:
```json
{
    "body": "Replying to [comment:102 jdemeyer]:\n> Replying to [comment:100 leif]:\n> > The `CFLAGS` (or `-march=`) issue is IMHO completely unrelated -- if not irrelevant. ;-)\n\n> \n> The current MPIR spkg *does* use machine-specific CFLAGS, the new spkg on this ticket *does not*.  This is a step backwards.\n> \n> If you think it is irrelevant, please explain why...\n\n\nGive me a *realistic* showcase where that matters... (i.e., causes a significant decrease in performance) ;-)\n\nFirst of all, the important parts of MPIR are (more or less) hand-optimized assembly code, selected by MPIR's `configure` (or its parameters*) to best match the detected architecture (where MPIR's `config.guess` doesn't always necessarily choose the current nearest one btw.).\n\nA properly configured GCC is usually sufficient, i.e. should default to something like `-march=native` (or a small subset of processors the actual CPU fits into), at least for people to whom performance is really crucial.\n\nWith my *current* spkg here, the user can always (intentionally or not) use the \"global\" `CFLAGS`, i.e. specify whatever is most appropriate to him or her.\n\nThe spkg had been extensively tested -- as is, month ago. As always: New changes, new pitfalls. [And even more delay due to a new test / review cycle. That's why I did not make any further changes *on this ticket*. Speaking of the devil, can someone **please** give #5847 a positive review?]\n\n\n---\n\n* If I haven't already, one (or me) should implement `MPIR_EXTRA_OPTS` or whatever it was called (but I think I already did).\n\nP.S.: Ah, I see. It's already in the p1 here.",
    "created_at": "2011-04-19T00:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78658",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:102 jdemeyer]:
> Replying to [comment:100 leif]:
> > The `CFLAGS` (or `-march=`) issue is IMHO completely unrelated -- if not irrelevant. ;-)

> 
> The current MPIR spkg *does* use machine-specific CFLAGS, the new spkg on this ticket *does not*.  This is a step backwards.
> 
> If you think it is irrelevant, please explain why...


Give me a *realistic* showcase where that matters... (i.e., causes a significant decrease in performance) ;-)

First of all, the important parts of MPIR are (more or less) hand-optimized assembly code, selected by MPIR's `configure` (or its parameters*) to best match the detected architecture (where MPIR's `config.guess` doesn't always necessarily choose the current nearest one btw.).

A properly configured GCC is usually sufficient, i.e. should default to something like `-march=native` (or a small subset of processors the actual CPU fits into), at least for people to whom performance is really crucial.

With my *current* spkg here, the user can always (intentionally or not) use the "global" `CFLAGS`, i.e. specify whatever is most appropriate to him or her.

The spkg had been extensively tested -- as is, month ago. As always: New changes, new pitfalls. [And even more delay due to a new test / review cycle. That's why I did not make any further changes *on this ticket*. Speaking of the devil, can someone **please** give #5847 a positive review?]


---

* If I haven't already, one (or me) should implement `MPIR_EXTRA_OPTS` or whatever it was called (but I think I already did).

P.S.: Ah, I see. It's already in the p1 here.



---

archive/issue_comments_078659.json:
```json
{
    "body": "We really need to get MPIR updated in Sage.  What's the status of this?",
    "created_at": "2011-05-09T18:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78659",
    "user": "https://github.com/mwhansen"
}
```

We really need to get MPIR updated in Sage.  What's the status of this?



---

archive/issue_comments_078660.json:
```json
{
    "body": "Replying to [comment:104 mhansen]:\n> We really need to get MPIR updated in Sage.  What's the status of this?\n\n\nThe package builds and works.  However, there is still the CFLAGS issue.  Me and William Stein think the package should not be merged in its current state, but others disagree.",
    "created_at": "2011-05-09T20:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78660",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:104 mhansen]:
> We really need to get MPIR updated in Sage.  What's the status of this?


The package builds and works.  However, there is still the CFLAGS issue.  Me and William Stein think the package should not be merged in its current state, but others disagree.



---

archive/issue_comments_078661.json:
```json
{
    "body": "Replying to [comment:105 jdemeyer]:\n> Replying to [comment:104 mhansen]:\n> > We really need to get MPIR updated in Sage.  What's the status of this?\n\n> \n> The package builds and works.  However, there is still the CFLAGS issue.  Me and William Stein think the package should not be merged in its current state, but others disagree.\n\n\n\n\nOk, I've asked Mercurial about my p2 (which was intended to be a follow-up):\n\n```\n+=== mpir-2.1.3.p2 (Leif Leonhardy, November 24th, 2010) ===\n+ * #8664: Upgrade Sage's MPIR spkg to version 2.1.3\n+ * Further improvements:\n+   - Let MPIR select CPU-specific code generation parameters (for CFLAGS) even\n+     if we (also) pass our own (or user-specified) CC and CFLAGS; these might\n+     be used by MPFR and GMP-ECM later, too, since MPIR's settings are recorded\n+     in 'gmp.h' / 'mpir.h'.\n+     Don't override user-settings (and respect SAGE_FAT_BINARY, SAGE_DEBUG\n+     etc.) though. Add '-march-native' if appropriate and supported.\n+  * Recognize also lower-case 'power*' arch (from 'uname -m').\n+  * Major restructuring / reformatting; more comments and messages added.\n```\n\nI'm not sure right now if it's ready for release, at least it is functional as far as I remember; haven't yet committed all changes though.\n\nStill believe we could [and maybe should] merge the p1 as is; upstream has to be updated anyway (once again, sooner or later, but IMHO definitely on a follow-up ticket).",
    "created_at": "2011-05-15T07:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78661",
    "user": "https://github.com/nexttime"
}
```

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

archive/issue_comments_078662.json:
```json
{
    "body": "Sage library patch. Fixes extension modules not getting rebuilt though depending on MPIR. Rebased to Sage 4.7.1.alpha4.",
    "created_at": "2011-07-05T18:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78662",
    "user": "https://github.com/nexttime"
}
```

Sage library patch. Fixes extension modules not getting rebuilt though depending on MPIR. Rebased to Sage 4.7.1.alpha4.



---

archive/issue_comments_078663.json:
```json
{
    "body": "Attachment [trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib-rebased_to_4.7.1.alpha4.patch](tarball://root/attachments/some-uuid/ticket8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib-rebased_to_4.7.1.alpha4.patch) by @williamstein created at 2011-07-18 05:21:21\n\nMPIR 2.4.0 has now been out over a month:  http://mpir.org/\nWe really, really need to get this upgraded.",
    "created_at": "2011-07-18T05:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78663",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib-rebased_to_4.7.1.alpha4.patch](tarball://root/attachments/some-uuid/ticket8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib-rebased_to_4.7.1.alpha4.patch) by @williamstein created at 2011-07-18 05:21:21

MPIR 2.4.0 has now been out over a month:  http://mpir.org/
We really, really need to get this upgraded.



---

archive/issue_comments_078664.json:
```json
{
    "body": "Replying to [comment:108 was]:\n> MPIR 2.4.0 has now been out over a month:  http://mpir.org/\n> We really, really need to get this upgraded.\n\n\nWell, we could have merged this last year...\n\nFurther upstream upgrades should IMHO be made on follow-ups, but shouldn't be a problem once this is in.\n\nHopefully I can make a FLINT 1.5.2 spkg (cf. #9858) this week, rebasing the one I already have on the latest changes to our 1.5.0, and check / finish the p2 mentioned above which fixes the \"`CFLAGS` issue\" (though I still consider that kind of ridiculous, at least not a reason to delay an overdue major upgrade for month).\n\nThe also required new GMP-ECM package at #5847 was reverted from positive review to \"needs work\" just because a more or less optional patch to the Sage library would have to be rebased on another that had not even been merged into the at that time current devel release. I did so, but it now again technically needs review.",
    "created_at": "2011-07-18T06:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78664",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:108 was]:
> MPIR 2.4.0 has now been out over a month:  http://mpir.org/
> We really, really need to get this upgraded.


Well, we could have merged this last year...

Further upstream upgrades should IMHO be made on follow-ups, but shouldn't be a problem once this is in.

Hopefully I can make a FLINT 1.5.2 spkg (cf. #9858) this week, rebasing the one I already have on the latest changes to our 1.5.0, and check / finish the p2 mentioned above which fixes the "`CFLAGS` issue" (though I still consider that kind of ridiculous, at least not a reason to delay an overdue major upgrade for month).

The also required new GMP-ECM package at #5847 was reverted from positive review to "needs work" just because a more or less optional patch to the Sage library would have to be rebased on another that had not even been merged into the at that time current devel release. I did so, but it now again technically needs review.



---

archive/issue_comments_078665.json:
```json
{
    "body": "Preliminary \"preview\" diff between the p1 and the upcoming p2 with improved option handling (CFLAGS etc.)",
    "created_at": "2011-07-18T08:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78665",
    "user": "https://github.com/nexttime"
}
```

Preliminary "preview" diff between the p1 and the upcoming p2 with improved option handling (CFLAGS etc.)



---

archive/issue_comments_078666.json:
```json
{
    "body": "Attachment [mpir-2.1.3.p1-mpir-2.1.3.p2.diff](tarball://root/attachments/some-uuid/ticket8664/mpir-2.1.3.p1-mpir-2.1.3.p2.diff) by @nexttime created at 2011-07-18 08:33:17\n\nI've attached a \"preview\" diff of the p2 in case that makes anyone happy...",
    "created_at": "2011-07-18T08:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78666",
    "user": "https://github.com/nexttime"
}
```

Attachment [mpir-2.1.3.p1-mpir-2.1.3.p2.diff](tarball://root/attachments/some-uuid/ticket8664/mpir-2.1.3.p1-mpir-2.1.3.p2.diff) by @nexttime created at 2011-07-18 08:33:17

I've attached a "preview" diff of the p2 in case that makes anyone happy...



---

archive/issue_comments_078667.json:
```json
{
    "body": "I have a new p3, but now I'm having the \"usual\" trouble with PPL (in Sage 4.7.1.rc0).\n\nI.e., installing MPIR works, but after the installation GCC is broken inside Sage, because it tries to use Sage's PPL which still refers to the old `libgmpxx.so.3` which got deleted upon installation. (Others are having trouble with unresolved symbols not provided by Sage's PPL.)\n\nIt was IMHO a very bad idea to include PPL into Sage using the same name for the shared library, apparently without taking any care of these issues. (GMP / MPIR, MPFR and the -- currently optional IIRC -- MPC, all used by more recent versions of GCC, are in principle likely dangerous.)\n\nFortunately<sup>TM</sup> I can just change my `CC` setting to cure the installation, not deleting or copying any libraries or creating symbolic links...\n\n(Apropos, I by incident saw that GAP's `spkg-install` is **unsetting `CC`** because not doing so is said to \"break the install\". That's very very odd as well.)\n\nI'll update the MPIR spkg again to not delete its old shared libraries as a quick fix.",
    "created_at": "2011-07-18T22:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78667",
    "user": "https://github.com/nexttime"
}
```

I have a new p3, but now I'm having the "usual" trouble with PPL (in Sage 4.7.1.rc0).

I.e., installing MPIR works, but after the installation GCC is broken inside Sage, because it tries to use Sage's PPL which still refers to the old `libgmpxx.so.3` which got deleted upon installation. (Others are having trouble with unresolved symbols not provided by Sage's PPL.)

It was IMHO a very bad idea to include PPL into Sage using the same name for the shared library, apparently without taking any care of these issues. (GMP / MPIR, MPFR and the -- currently optional IIRC -- MPC, all used by more recent versions of GCC, are in principle likely dangerous.)

Fortunately<sup>TM</sup> I can just change my `CC` setting to cure the installation, not deleting or copying any libraries or creating symbolic links...

(Apropos, I by incident saw that GAP's `spkg-install` is **unsetting `CC`** because not doing so is said to "break the install". That's very very odd as well.)

I'll update the MPIR spkg again to not delete its old shared libraries as a quick fix.



---

archive/issue_comments_078668.json:
```json
{
    "body": "Attachment [mpir-2.1.3.p1-mpir-2.1.3.p4.diff](tarball://root/attachments/some-uuid/ticket8664/mpir-2.1.3.p1-mpir-2.1.3.p4.diff) by @nexttime created at 2011-07-20 04:16:11\n\nDiff between the formerly positively reviewed p1 and the p4. For reference / review.",
    "created_at": "2011-07-20T04:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78668",
    "user": "https://github.com/nexttime"
}
```

Attachment [mpir-2.1.3.p1-mpir-2.1.3.p4.diff](tarball://root/attachments/some-uuid/ticket8664/mpir-2.1.3.p1-mpir-2.1.3.p4.diff) by @nexttime created at 2011-07-20 04:16:11

Diff between the formerly positively reviewed p1 and the p4. For reference / review.



---

archive/issue_comments_078669.json:
```json
{
    "body": "Changing keywords from \"GMP ECM execstack Fedora 14 extension module library dependencies\" to \"GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7\".",
    "created_at": "2011-07-20T04:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78669",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "GMP ECM execstack Fedora 14 extension module library dependencies" to "GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7".



---

archive/issue_comments_078670.json:
```json
{
    "body": "New spkg is up:\n\n http://spkg-upload.googlecode.com/files/mpir-2.1.3.p4.spkg\n\n md5sum: `f84278504f4e1b696030c41cac6e4719  mpir-2.1.3.p4.spkg`\n\nFrom a user's view, fixes the \"`CFLAGS` issue\", adds support for MacOS X 10.7 and some messages.\n\nInstallation instructions remain the same; I'll perhaps put them into the description later.\n\n---\n\n### mpir-2.1.3.p4 (Leif Leonhardy, July 19th, 2011)\n* #8664: Upgrade Sage's MPIR spkg to version 2.1.3\n* Do not delete old GMP/MPIR shared libraries as Sage's versions of libraries\n  used by GCC might still refer to them, such that their deletion would break\n  GCC inside Sage. (PPL e.g. refers to libgmpxx; MPFR and MPC are equally\n  dangerous, since they're [also] used by recent versions of GCC.)\n* Some more messages (e.g on rebuilding the Sage library and other packages\n  after installation) and comments added.\n* \"Patches\" section added.\n* Also refreshed the patched gmp-h.in for SunOS. ;-)\n\n### mpir-2.1.3.p3 (Leif Leonhardy, July 18th, 2011)\n* #8664: Upgrade Sage's MPIR spkg to version 2.1.3\n* Support MacOS 10.7 (Darwin 11) and later.\n* Add warning if SAGE_DEBUG=yes since we then disable optimization.\n\n### mpir-2.1.3.p2 (Leif Leonhardy, November 24th, 2010)\n* #8664: Upgrade Sage's MPIR spkg to version 2.1.3\n* Further improvements:\n  - Let MPIR select CPU-specific code generation parameters (for CFLAGS) even\n    if we (also) pass our own (or user-specified) CC and CFLAGS; these might\n    be used by MPFR and GMP-ECM later, too, since MPIR's settings are recorded\n    in 'gmp.h' / 'mpir.h'.\n    Don't override user-settings (and respect SAGE_FAT_BINARY, SAGE_DEBUG\n    etc.) though. Add '-march-native' if appropriate and supported.\n  * Recognize also lower-case 'power*' arch (from 'uname -m').\n  * Major restructuring / reformatting; more comments and messages added.\n\n(Changes I made relative to the p1 which already had positive review, but got unmerged later.)\n\n---\n\nFurther upstream upgrade to MPIR 2.4.0 (or 2.3.1 if more upstream issues should arise) will come soon *on another ticket*. We IMHO first should get this well-tested upstream release in.\n\nPlease build, test and review...",
    "created_at": "2011-07-20T04:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78670",
    "user": "https://github.com/nexttime"
}
```

New spkg is up:

 http://spkg-upload.googlecode.com/files/mpir-2.1.3.p4.spkg

 md5sum: `f84278504f4e1b696030c41cac6e4719  mpir-2.1.3.p4.spkg`

From a user's view, fixes the "`CFLAGS` issue", adds support for MacOS X 10.7 and some messages.

Installation instructions remain the same; I'll perhaps put them into the description later.

---

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

---

Further upstream upgrade to MPIR 2.4.0 (or 2.3.1 if more upstream issues should arise) will come soon *on another ticket*. We IMHO first should get this well-tested upstream release in.

Please build, test and review...



---

archive/issue_comments_078671.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-07-20T04:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78671",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078672.json:
```json
{
    "body": "P.S.: It would perhaps be convenient to either have a testing distribution or at least a Sage (library) package with the patch here applied, since during the automatic rebuild of dependent packages Sage switches back to the \"main\" branch and may invalidate an already applied patch. The behavior seems to have meanwhile changed a bit though.",
    "created_at": "2011-07-20T04:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78672",
    "user": "https://github.com/nexttime"
}
```

P.S.: It would perhaps be convenient to either have a testing distribution or at least a Sage (library) package with the patch here applied, since during the automatic rebuild of dependent packages Sage switches back to the "main" branch and may invalidate an already applied patch. The behavior seems to have meanwhile changed a bit though.



---

archive/issue_comments_078673.json:
```json
{
    "body": "Ok, to ease testing, I've uploaded a [Sage 4.7.1.rc0 library spkg](http://spkg-upload.googlecode.com/files/sage-4.7.1.rc0-8664-5847.spkg) with both patches (from here and #5847) already applied.\n\nYou can either build Sage 4.7.1.rc0 from scratch with these three spkgs, or take a Sage 4.7.1.rc0 installation and just install them, automatically rebuilding (only) the dependent spkgs.\n\n1. Copy [the MPIR spkg](http://spkg-upload.googlecode.com/files/mpir-2.1.3.p4.spkg) and [the GMP-ECM spkg](http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg) into `$SAGE_ROOT/spkg/standard/`.\n2. **Replace** the `sage-4.7.1.rc0.spkg` with [this one](http://spkg-upload.googlecode.com/files/sage-4.7.1.rc0-8664-5847.spkg) (i.e., copy it to `$SAGE_ROOT/spkg/standard` and **delete** the original since `newest_version` would otherwise take the wrong one).\n3. Build:\n   * For a build from scratch, simply type `make`.\n   * For rebuilding an existing installation with the new spkgs, type\n\n```sh\nenv SAGE_UPGRADING=yes make\n```\n\nNote that you currently must not set `SAGE_CHECK` to `yes` in the above procedures, since the test suite of our current FLINT won't build with the new MPIR.\n\nTo run MPIR's and GMP-ECM's test suites, I'd suggest to simply reinstall them afterwards with `env SAGE_CHECK=yes ./sage -f mpir-2.1.3.p4 ecm-6.3.p2`. Likewise, you can also play with different `CFLAGS` settings (empty, some non-processor-specific flags, with some `-march=...` or `-mtune=...` etc. included).\n\nThen preferably run `make testlong` or `make ptestlong`, though both upstream releases have IMHO already been quite excessively tested.",
    "created_at": "2011-07-20T07:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78673",
    "user": "https://github.com/nexttime"
}
```

Ok, to ease testing, I've uploaded a [Sage 4.7.1.rc0 library spkg](http://spkg-upload.googlecode.com/files/sage-4.7.1.rc0-8664-5847.spkg) with both patches (from here and #5847) already applied.

You can either build Sage 4.7.1.rc0 from scratch with these three spkgs, or take a Sage 4.7.1.rc0 installation and just install them, automatically rebuilding (only) the dependent spkgs.

1. Copy [the MPIR spkg](http://spkg-upload.googlecode.com/files/mpir-2.1.3.p4.spkg) and [the GMP-ECM spkg](http://spkg-upload.googlecode.com/files/ecm-6.3.p2.spkg) into `$SAGE_ROOT/spkg/standard/`.
2. **Replace** the `sage-4.7.1.rc0.spkg` with [this one](http://spkg-upload.googlecode.com/files/sage-4.7.1.rc0-8664-5847.spkg) (i.e., copy it to `$SAGE_ROOT/spkg/standard` and **delete** the original since `newest_version` would otherwise take the wrong one).
3. Build:
   * For a build from scratch, simply type `make`.
   * For rebuilding an existing installation with the new spkgs, type

```sh
env SAGE_UPGRADING=yes make
```

Note that you currently must not set `SAGE_CHECK` to `yes` in the above procedures, since the test suite of our current FLINT won't build with the new MPIR.

To run MPIR's and GMP-ECM's test suites, I'd suggest to simply reinstall them afterwards with `env SAGE_CHECK=yes ./sage -f mpir-2.1.3.p4 ecm-6.3.p2`. Likewise, you can also play with different `CFLAGS` settings (empty, some non-processor-specific flags, with some `-march=...` or `-mtune=...` etc. included).

Then preferably run `make testlong` or `make ptestlong`, though both upstream releases have IMHO already been quite excessively tested.



---

archive/issue_comments_078674.json:
```json
{
    "body": "Replying to [comment:114 leif]:\n\n\nI'm currently running this on MacOSX 10.6. Will report as soon as it's done",
    "created_at": "2011-07-21T11:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78674",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:114 leif]:


I'm currently running this on MacOSX 10.6. Will report as soon as it's done



---

archive/issue_comments_078675.json:
```json
{
    "body": "Replying to [comment:115 dimpase]:\n> I'm currently running this on MacOSX 10.6. Will report as soon as it's done\n\n\nThanks. If all tests pass and you're happy with the spkg *here*, you may want to take a look at #11616. ;-)",
    "created_at": "2011-07-22T07:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78675",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:115 dimpase]:
> I'm currently running this on MacOSX 10.6. Will report as soon as it's done


Thanks. If all tests pass and you're happy with the spkg *here*, you may want to take a look at #11616. ;-)



---

archive/issue_comments_078676.json:
```json
{
    "body": "Replying to [comment:115 dimpase]:\n> Replying to [comment:114 leif]:\n> \n> \n> I'm currently running this on MacOSX 10.6. Will report as soon as it's done\n\n\nI can confirm that the above procedure and \"make ptestlong\" works just fine on MacOSX 10.6.",
    "created_at": "2011-07-22T10:25:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78676",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:115 dimpase]:
> Replying to [comment:114 leif]:
> 
> 
> I'm currently running this on MacOSX 10.6. Will report as soon as it's done


I can confirm that the above procedure and "make ptestlong" works just fine on MacOSX 10.6.



---

archive/issue_comments_078677.json:
```json
{
    "body": "Replying to [comment:116 leif]:\n> Replying to [comment:115 dimpase]:\n> > I'm currently running this on MacOSX 10.6. Will report as soon as it's done\n\n> \n> Thanks. If all tests pass and you're happy with the spkg *here*, you may want to take a look at #11616. ;-)\n> \n\n\nI think I can give this a positive review.",
    "created_at": "2011-07-22T10:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78677",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:116 leif]:
> Replying to [comment:115 dimpase]:
> > I'm currently running this on MacOSX 10.6. Will report as soon as it's done

> 
> Thanks. If all tests pass and you're happy with the spkg *here*, you may want to take a look at #11616. ;-)
> 


I think I can give this a positive review.



---

archive/issue_comments_078678.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-07-22T10:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78678",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020989.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-07-22T12:52:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20989"
}
```



---

archive/issue_events_020990.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-07-22T12:52:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-4.7.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20990"
}
```



---

archive/issue_comments_078679.json:
```json
{
    "body": "because it depends on a not-yet-positively-reviewed ticket",
    "created_at": "2011-07-24T18:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78679",
    "user": "https://github.com/jdemeyer"
}
```

because it depends on a not-yet-positively-reviewed ticket



---

archive/issue_events_020991.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-07-24T18:53:36Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-4.7.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20991"
}
```



---

archive/issue_events_020992.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-07-24T18:53:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20992"
}
```



---

archive/issue_comments_078680.json:
```json
{
    "body": "Replying to [comment:120 jdemeyer]:\n> because it depends on a not-yet-positively-reviewed ticket\n\n\nWell, can't you re-review #5847, which you set back to \"needs work\"?\n\nThe only single thing that has changed there is that the one-line patch to `module_list.py` got rebased to Sage 4.7.1.alpha4, in particular it is the same patch, differing just in line numbers (or, more precisely, a single after-context line):\n\n```patch\n--- ../patches/trac_5847-module_list-fix_execstack-sagelib.patch\t2011-06-02 21:38:51.000000000 +0200\n+++ ../patches/trac_5847-module_list-fix_execstack-sagelib-rebased_to_4.7.1.alpha4.patch\t2011-07-20 07:08:13.000000000 +0200\n@@ -1,22 +1,24 @@\n # HG changeset patch\n # User Leif Leonhardy <not.really@online.de>\n-# Date 1307043111 -7200\n-# Node ID e7b1b631a38756bb37aa5edc7a0e31ff10eaa86a\n-# Parent  fb00ec75853019eb9799fd863b193fe82ee97c74\n+# Date 1309863032 -7200\n+# Node ID 556a3825c961b6871451652dede6ec3742705482\n+# Parent  8532a2ad1e558cbc91ddaaa6b7cc79956dd1e8ba\n #5847: Add 'noexecstack' flag when linking libecm extension module on Linux.\n \n (Not doing so caused trouble on a SkyNet Fedora machine with Sage 4.7.1.alpha1\n  and GMP-ECM 6.3.p2 from #5847, GCC 4.6.0; didn't occur previously.)\n \n-diff -r fb00ec758530 -r e7b1b631a387 module_list.py\n---- a/module_list.py\tWed May 11 22:39:05 2011 +0000\n-+++ b/module_list.py\tThu Jun 02 21:31:51 2011 +0200\n-@@ -561,6 +561,8 @@\n+(Rebased patch for Sage 4.7.1.alpha4 / #11377)\n+\n+diff -r 8532a2ad1e55 -r 556a3825c961 module_list.py\n+--- a/module_list.py\tSun Jul 03 14:23:12 2011 +0000\n++++ b/module_list.py\tTue Jul 05 12:50:32 2011 +0200\n+@@ -568,6 +568,8 @@\n      Extension('sage.libs.libecm',\n                sources = ['sage/libs/libecm.pyx'],\n                libraries = ['ecm', 'gmp'],\n +              extra_link_args = uname_specific(\"Linux\", [\"-Wl,-z,noexecstack\"],\n +                                                        []),\n-               depends = [SAGE_ROOT + \"/local/include/ecm.h\"]),\n+               depends = [SAGE_INC + \"ecm.h\"]),\n       \n      Extension('sage.libs.mwrank.mwrank',\n```",
    "created_at": "2011-07-24T23:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78680",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:120 jdemeyer]:
> because it depends on a not-yet-positively-reviewed ticket


Well, can't you re-review #5847, which you set back to "needs work"?

The only single thing that has changed there is that the one-line patch to `module_list.py` got rebased to Sage 4.7.1.alpha4, in particular it is the same patch, differing just in line numbers (or, more precisely, a single after-context line):

```patch
--- ../patches/trac_5847-module_list-fix_execstack-sagelib.patch	2011-06-02 21:38:51.000000000 +0200
+++ ../patches/trac_5847-module_list-fix_execstack-sagelib-rebased_to_4.7.1.alpha4.patch	2011-07-20 07:08:13.000000000 +0200
@@ -1,22 +1,24 @@
 # HG changeset patch
 # User Leif Leonhardy <not.really@online.de>
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
-@@ -561,6 +561,8 @@
+(Rebased patch for Sage 4.7.1.alpha4 / #11377)
+
+diff -r 8532a2ad1e55 -r 556a3825c961 module_list.py
+--- a/module_list.py	Sun Jul 03 14:23:12 2011 +0000
++++ b/module_list.py	Tue Jul 05 12:50:32 2011 +0200
+@@ -568,6 +568,8 @@
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

archive/issue_comments_078681.json:
```json
{
    "body": "#5847 has a positive review again",
    "created_at": "2011-08-23T05:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78681",
    "user": "https://github.com/ohanar"
}
```

#5847 has a positive review again



---

archive/issue_events_020993.json:
```json
{
    "actor": "https://github.com/ohanar",
    "created_at": "2011-08-23T05:57:45Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20993"
}
```



---

archive/issue_events_020994.json:
```json
{
    "actor": "https://github.com/ohanar",
    "created_at": "2011-08-23T05:57:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-4.7.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20994"
}
```



---

archive/issue_comments_078682.json:
```json
{
    "body": "Changing keywords from \"GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7\" to \"sd32, GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7\".",
    "created_at": "2011-08-24T23:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78682",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7" to "sd32, GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7".



---

archive/issue_comments_078683.json:
```json
{
    "body": "Sage library patch. Fixes extension modules not getting rebuilt though depending on MPIR. Rebased on Sage 4.7.2.alpha2 / #11376.",
    "created_at": "2011-08-31T21:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78683",
    "user": "https://github.com/nexttime"
}
```

Sage library patch. Fixes extension modules not getting rebuilt though depending on MPIR. Rebased on Sage 4.7.2.alpha2 / #11376.



---

archive/issue_comments_078684.json:
```json
{
    "body": "Attachment [trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib-rebased_to_4.7.2.alpha2.patch](tarball://root/attachments/some-uuid/ticket8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib-rebased_to_4.7.2.alpha2.patch) by @nexttime created at 2011-08-31 21:49:09",
    "created_at": "2011-08-31T21:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78684",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib-rebased_to_4.7.2.alpha2.patch](tarball://root/attachments/some-uuid/ticket8664/trac_8664-fix_extmod_deps_for_MPIR_generically-sagelib-rebased_to_4.7.2.alpha2.patch) by @nexttime created at 2011-08-31 21:49:09



---

archive/issue_comments_078685.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-12T19:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78685",
    "user": "https://github.com/nexttime"
}
```

Resolution: fixed



---

archive/issue_comments_078686.json:
```json
{
    "body": "Changing keywords from \"sd32, GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7\" to \"sd32, GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7 Lion\".",
    "created_at": "2011-09-12T19:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78686",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "sd32, GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7" to "sd32, GMP ECM execstack Fedora 14 extension module library dependencies Darwin 11 MacOS X 10.7 Lion".



---

archive/issue_events_020995.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2011-09-12T19:03:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20995"
}
```



---

archive/issue_comments_078687.json:
```json
{
    "body": "Had to fix the changelog and some file permissions.\n\nCorrected spkg at new location.",
    "created_at": "2011-09-23T05:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78687",
    "user": "https://github.com/nexttime"
}
```

Had to fix the changelog and some file permissions.

Corrected spkg at new location.



---

archive/issue_comments_078688.json:
```json
{
    "body": "I'm not sure if this is the best place to report this since the ticket has been merged, but in building vanilla sage-4.7.2.alpha3 on x86, mpir-2.1.3.p4 fails with\n\n```\n ../strip_fPIC.sh ../yasm/yasm -I .. -f elf64 submul_1.as -o submul_1.o >/dev/null 2>&1\n/bin/bash ../libtool --mode=c\n ../mpn/m4-ccas --m4=m4 gcc -std=gnu99 -c -DHAVE_CONFIG_H -m32 -O2 -fomit-frame-pointer -mtune=core2 -march=core2 -D__GMP_WITHIN_GMP -I.. -DOPERATION_lshift -I. -I.. lshift.asm  -fPIC -DPIC -o .libs/lshift.o\nm4  -DHAVE_CONFIG_H -D__GMP_WITHIN_GMP -DOPERATION_lshift -DPIC lshift.asm >tmp-lshift.s\n gcc -std=gnu99 -c -DHAVE_CONFIG_H -m32 -O2 -fomit-frame-pointer -mtune=core2 -march=core2 -D__GMP_WITHIN_GMP -I.. -DOPERATION_lshift -I. -I.. tmp-lshift.s -fPIC -DPIC -o .libs/lshift.o\ntmp-lshift.s: Assembler messages:\ntmp-lshift.s:53: Error: bad register name `%rbx'\ntmp-lshift.s:54: Error: bad register name `%rdx'\ntmp-lshift.s:55: Error: bad register name `%rsi)'\ntmp-lshift.s:56: Error: bad register name `%rdi)'\ntmp-lshift.s:57: Error: bad register name `%rsi,%rbx,8)'\ntmp-lshift.s:58: Error: bad register name `%rax'\ntmp-lshift.s:59: Error: bad register name `%rdx'\ntmp-lshift.s:60: Error: bad register name `%rbx'\ntmp-lshift.s:64: Error: bad register name `%rsi,%rbx,8)'\ntmp-lshift.s:65: Error: bad register name `%rsi,%rbx,8)'\ntmp-lshift.s:66: Error: bad register name `%rsi,%rbx,8)'\ntmp-lshift.s:67: Error: bad register name `%r8'\ntmp-lshift.s:68: Error: bad register name `%rdx'\ntmp-lshift.s:69: Error: bad register name `%r11'\ntmp-lshift.s:70: Error: bad register name `%rsi,%rbx,8)'\n\n...\n\ntmp-lshift.s:118: Error: bad register name `%rsi,%rbx,8)'\ntmp-lshift.s:119: Error: bad register name `%r8'\ntmp-lshift.s:120: Error: bad register name `%rdx'\ntmp-lshift.s:121: Error: bad register name `%r8'\ntmp-lshift.s:122: Error: bad register name `%r8'\ntmp-lshift.s:123: Error: bad register name `%rbx'\nmake[4]: *** [lshift.lo] Error 1\nmake[4]: Leaving directory `/storage/sage/sage-4.7.2.alpha3/spkg/build/mpir-2.1.3.p4/src/mpn'\nmake[3]: *** [all-recursive] Error 1\nmake[3]: Leaving directory `/storage/sage/sage-4.7.2.alpha3/spkg/build/mpir-2.1.3.p4/src'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/storage/sage/sage-4.7.2.alpha3/spkg/build/mpir-2.1.3.p4/src'\nError building MPIR.\n```\nI've never seen this before. The machine is running debian, but the sage build was done from within a gentoo prefix. So the build is basically one using gentoo. There doesn't seem to be a problem on amd64. I still have the build log.",
    "created_at": "2011-10-03T01:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78688",
    "user": "https://github.com/strogdon"
}
```

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

archive/issue_comments_078689.json:
```json
{
    "body": "Replying to [comment:128 strogdon]:\n> I'm not sure if this is the best place to report this since the ticket has been merged, but in building vanilla sage-4.7.2.alpha3 on x86, mpir-2.1.3.p4 fails with\n> \n\n{{{\ntmp-lshift.s: Assembler messages:\ntmp-lshift.s:53: Error: bad register name `%rbx'\n...\nmake[4]: *** [lshift.lo] Error 1\n...\n}}}\n> I've never seen this before. The machine is running debian, but the sage build was done from within a gentoo prefix. So the build is basically one using gentoo. There doesn't seem to be a problem on amd64. I still have the build log.\n\n\nSee [sage-release](http://groups.google.com/group/sage-release/msg/c560179ee11e8692) and [this mpir-devel thread](http://groups.google.com/group/mpir-devel/browse_thread/thread/46ccdc5dfc3485cd#).\n\nI'm sorry I didn't catch this earlier, but it's a waste of resources to run 32-bit operating systems (or software in general) on 64-bit processors... ;-)\n\nI'll provide follow-up spkgs (also at #11616) that will fix this without the need to set `ABI`, but perhaps not that very soon.\n\nBy the way, MPIR 2.5.0 should get released in the next days as well, so I'll presumably also make an spkg based on that.",
    "created_at": "2011-10-03T06:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78689",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:128 strogdon]:
> I'm not sure if this is the best place to report this since the ticket has been merged, but in building vanilla sage-4.7.2.alpha3 on x86, mpir-2.1.3.p4 fails with
> 

{{{
tmp-lshift.s: Assembler messages:
tmp-lshift.s:53: Error: bad register name `%rbx'
...
make[4]: *** [lshift.lo] Error 1
...
}}}
> I've never seen this before. The machine is running debian, but the sage build was done from within a gentoo prefix. So the build is basically one using gentoo. There doesn't seem to be a problem on amd64. I still have the build log.


See [sage-release](http://groups.google.com/group/sage-release/msg/c560179ee11e8692) and [this mpir-devel thread](http://groups.google.com/group/mpir-devel/browse_thread/thread/46ccdc5dfc3485cd#).

I'm sorry I didn't catch this earlier, but it's a waste of resources to run 32-bit operating systems (or software in general) on 64-bit processors... ;-)

I'll provide follow-up spkgs (also at #11616) that will fix this without the need to set `ABI`, but perhaps not that very soon.

By the way, MPIR 2.5.0 should get released in the next days as well, so I'll presumably also make an spkg based on that.



---

archive/issue_comments_078690.json:
```json
{
    "body": "Replying to [comment:129 leif]:\n> Replying to [comment:128 strogdon]:\n> > I'm not sure if this is the best place to report this since the ticket has been merged, but in building vanilla sage-4.7.2.alpha3 on x86, mpir-2.1.3.p4 fails with\n> > \n\n{{{\ntmp-lshift.s: Assembler messages:\ntmp-lshift.s:53: Error: bad register name `%rbx'\n...\nmake[4]: *** [lshift.lo] Error 1\n...\n}}}\n> I'll provide follow-up spkgs (also at #11616) that will fix this without the need to set `ABI`, but perhaps not that very soon.\n\n\nAn MPIR 2.1.3.p5 spkg fixing this is now available at #11896, currently needing review.",
    "created_at": "2011-10-05T03:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78690",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:129 leif]:
> Replying to [comment:128 strogdon]:
> > I'm not sure if this is the best place to report this since the ticket has been merged, but in building vanilla sage-4.7.2.alpha3 on x86, mpir-2.1.3.p4 fails with
> > 

{{{
tmp-lshift.s: Assembler messages:
tmp-lshift.s:53: Error: bad register name `%rbx'
...
make[4]: *** [lshift.lo] Error 1
...
}}}
> I'll provide follow-up spkgs (also at #11616) that will fix this without the need to set `ABI`, but perhaps not that very soon.


An MPIR 2.1.3.p5 spkg fixing this is now available at #11896, currently needing review.



---

archive/issue_events_020996.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-11T07:36:14Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-4.7.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20996"
}
```



---

archive/issue_comments_078691.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-10-11T07:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78691",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_078692.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-10-11T07:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78692",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_020997.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-11T07:36:14Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20997"
}
```



---

archive/issue_comments_078693.json:
```json
{
    "body": "Unmerging this because of #9858 and #11896.",
    "created_at": "2011-10-11T07:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78693",
    "user": "https://github.com/jdemeyer"
}
```

Unmerging this because of #9858 and #11896.



---

archive/issue_comments_078694.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-10-11T07:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78694",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078695.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-11T07:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78695",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078696.json:
```json
{
    "body": "Another cyclic dependency... ;-) (#11698 depends on this ticket)\n\n---\n\nA new FLINT spkg (still 1.5.0, a p10) fixing the FLINT test suite build error (occurring in combination with any recent GMP / MPIR version like the one here) by just applying an upstream patch from FLINT 1.5.2 is ready for review at #9858.\n\n(FLINT 1.5.2 and 1.6 spkgs will now most probably be on follow-up tickets to #9858.)",
    "created_at": "2011-10-11T22:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78696",
    "user": "https://github.com/nexttime"
}
```

Another cyclic dependency... ;-) (#11698 depends on this ticket)

---

A new FLINT spkg (still 1.5.0, a p10) fixing the FLINT test suite build error (occurring in combination with any recent GMP / MPIR version like the one here) by just applying an upstream patch from FLINT 1.5.2 is ready for review at #9858.

(FLINT 1.5.2 and 1.6 spkgs will now most probably be on follow-up tickets to #9858.)



---

archive/issue_comments_078697.json:
```json
{
    "body": "Replying to [comment:134 leif]:\n> Another cyclic dependency... ;-) (#11698 depends on this ticket)\n\n\nOoops, #11896 of course. XD\n\n(But I'll try to review #11698 anyway.)",
    "created_at": "2011-10-11T22:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78697",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:134 leif]:
> Another cyclic dependency... ;-) (#11698 depends on this ticket)


Ooops, #11896 of course. XD

(But I'll try to review #11698 anyway.)



---

archive/issue_events_020998.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-14T09:41:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20998"
}
```



---

archive/issue_comments_078698.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-10-14T09:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78698",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_078699.json:
```json
{
    "body": "Milestone sage-4.7.3 deleted",
    "created_at": "2011-11-03T16:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78699",
    "user": "https://github.com/jdemeyer"
}
```

Milestone sage-4.7.3 deleted



---

archive/issue_events_020999.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-11-03T16:15:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "milestone": "sage-4.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8664#event-20999"
}
```



---

archive/issue_comments_078700.json:
```json
{
    "body": "Replying to [comment:46 leif]:\n> Any reason to keep\n> \n> ```\n> #!sh\n>     SAGE_CONF_OPTS=\"--enable-shared --disable-static\"\n> ```\n> (i.e., why not build the static library, too)?\n> \n\nAs it turns out, this change seems to break MPIR on Cygwin.  See [this sage-windows thread](http://groups.google.com/group/sage-windows/browse_thread/thread/be2b2af416351c9b).",
    "created_at": "2011-12-03T19:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8664#issuecomment-78700",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:46 leif]:
> Any reason to keep
> 
> ```
> #!sh
>     SAGE_CONF_OPTS="--enable-shared --disable-static"
> ```
> (i.e., why not build the static library, too)?
> 

As it turns out, this change seems to break MPIR on Cygwin.  See [this sage-windows thread](http://groups.google.com/group/sage-windows/browse_thread/thread/be2b2af416351c9b).
