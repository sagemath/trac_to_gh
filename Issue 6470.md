# Issue 6470: sage-4.1.rc0: On OS X 10.5 Singular fails to build

archive/issues_006470.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  georgsweber @malb\n\n\n```\ng++ -O3 -g -fPIC -pipe -I. -I../kernel -I/Applications/sage_builds/\nsage-4.1.rc0/local/include -I/Applications/sage_builds/sage-4.1.rc0/\nlocal/include  -I/Applications/sage_builds/sage-4.1.rc0/local/include -\nfno-implicit-templates -DNDEBUG -DOM_NDEBUG -Dix86Mac_darwin -\nDHAVE_CONFIG_H -DLIBSINGULAR \\\n          -dynamic -twolevel_namespace -weak_reference_mismatches weak -\nundefined dynamic_lookup -o libsingular-tesths.o \\\n          -c tesths.cc\nlibtool -dynamic -twolevel_namespace -weak_reference_mismatches weak -\nundefined dynamic_lookup -single_module -o libsingular.dylib \\\n        libsingular-tesths.o iparith.o mpsr_Tok.o claptmpl.o \\\n        grammar.o scanner.o attrib.o eigenval_ip.o extra.o fehelp.o feOpt.o\nipassign.o ipconv.o ipid.o iplib.o ipprint.o ipshell.o lists.o sdb.o\nfglm.o interpolation.o silink.o subexpr.o janet.o wrapper.o libparse.o\nsing_win.o gms.o pcv.o maps_ip.o walk.o walk_ip.o cntrlc.o misc.o\ncalcSVD.o  slInit_Static.o mpsr_Put.o mpsr_PutPoly.o mpsr_GetPoly.o\nmpsr_sl.o mpsr_Get.o mpsr_GetMisc.o mpsr_Error.o ndbm.o sing_dbm.o -\nlkernel -L../kernel -L../factory -L../libfac -L/Applications/\nsage_builds/sage-4.1.rc0/local/lib -lsingfac -lsingcf -lntl -lreadline\n-lgmp -lomalloc\nlibtool: file: -lsingcf(canonicalform.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_algorithm.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_binom.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_char.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(cf_chinese.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_eval.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(cf_factor.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_factory.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_gcd.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(cf_gcd_charp.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_generator.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_globals.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_inline.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_irred.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_iter.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(cf_iter_inline.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_linsys.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_map.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(cf_ops.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(cf_primes.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_random.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_resultant.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_reval.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_switches.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(cf_util.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(debug.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(fac_berlekamp.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(fac_cantzass.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(fac_distrib.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(fac_ezgcd.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(fac_iterfor.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(fac_multihensel.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(fac_multivar.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(fac_sqrfree.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(fac_univar.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(fac_util.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(fieldGCD.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(ffops.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(ffreval.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(gf_tabutil.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(gfops.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(imm.cc) is not an object file (not allowed in\na library)\nlibtool: file: -lsingcf(initgmp.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(int_cf.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(int_int.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(int_intdiv.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(int_poly.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(int_pp.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(int_rat.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(sm_sparsemod.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(sm_util.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(variable.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(NTLconvert.cc) is not an object file (not\nallowed in a library)\nlibtool: file: -lsingcf(abs_fac.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(bifac.cc) is not an object file (not allowed\nin a library)\nlibtool: file: -lsingcf(lgs.cc) is not an object file (not allowed in\na library)\nlibtool: file: -lsingcf(singext.cc) is not an object file (not allowed\nin a library)\nmake[3]: *** [libsingular] Error 1\nmake[2]: *** [libsingular] Error 2\nUnable to build Singular.\n\nreal    6m56.224s\nuser    6m9.512s\nsys     0m38.659s\nsage: An error occurred while installing singular-3-1-0-4-20090703\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /Applications/sage_builds/sage-4.1.rc0/install.log.  Describe your\ncomputer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/Applications/sage_builds/sage-4.1.rc0/spkg/build/\nsingular-3-1-0-4-20090703 and type 'make'.\nInstead type \"/Applications/sage_builds/sage-4.1.rc0/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/Applications/sage_builds/sage-4.1.rc0/spkg/build/\nsingular-3-1-0-4-20090703\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\nmake[1]: *** [installed/singular-3-1-0-4-20090703] Error 1 \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6470\n\n",
    "created_at": "2009-07-06T17:37:00Z",
    "labels": [
        "component: distribution",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "sage-4.1.rc0: On OS X 10.5 Singular fails to build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6470",
    "user": "https://github.com/rlmill"
}
```
Assignee: tbd

CC:  georgsweber @malb


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


Issue created by migration from https://trac.sagemath.org/ticket/6470





---

archive/issue_comments_052204.json:
```json
{
    "body": "The version http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg that fixes gcc 4.4 issue but doesn't have the 3.1.0-4 that fails is put back on-line. **If** this wouldn't be solved on time for release, this version works on Mac (as reported on sage-devel) so upgrade to 3.1.0-4 can wait for 4.1.1 probably?",
    "created_at": "2009-07-06T19:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6470#issuecomment-52204",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

The version http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg that fixes gcc 4.4 issue but doesn't have the 3.1.0-4 that fails is put back on-line. **If** this wouldn't be solved on time for release, this version works on Mac (as reported on sage-devel) so upgrade to 3.1.0-4 can wait for 4.1.1 probably?



---

archive/issue_comments_052205.json:
```json
{
    "body": "In case it's helpful, I have logs of the successful build of singular-3-1-0-2-20090620.spkg and the failed build of singular-3-1-0-4-20090703:\n\n [http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-2-20090620.log](http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-2-20090620.log)\n\n [http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-4-20090703.log](http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-4-20090703.log)",
    "created_at": "2009-07-06T20:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6470#issuecomment-52205",
    "user": "https://github.com/jhpalmieri"
}
```

In case it's helpful, I have logs of the successful build of singular-3-1-0-2-20090620.spkg and the failed build of singular-3-1-0-4-20090703:

 [http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-2-20090620.log](http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-2-20090620.log)

 [http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-4-20090703.log](http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-4-20090703.log)



---

archive/issue_comments_052206.json:
```json
{
    "body": "Ups,\n\nI posted my findings on ticket #6362 instead of here. In short: the build issue seems to be solved, most probably the OS X \"make\" version is a bit too old for a certain programmer's short-cut newly used in GNUmakefile.in. Let's continue here -- should I repost my comments?\n\nCheers,\ngsw",
    "created_at": "2009-07-06T20:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6470#issuecomment-52206",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Ups,

I posted my findings on ticket #6362 instead of here. In short: the build issue seems to be solved, most probably the OS X "make" version is a bit too old for a certain programmer's short-cut newly used in GNUmakefile.in. Let's continue here -- should I repost my comments?

Cheers,
gsw



---

archive/issue_comments_052207.json:
```json
{
    "body": "Thinking about it, I do repost my comments from #6362:\n\nAs contained in Sage-4.1.rc0, singular-3-1-0-4-20090703.spkg does not even build on OS X, neither 10.4 nor 10.5. Changing the line 201 in /src/factory/GNUmakefile.in:\n\n```\nfactoryobj :=   $(factorysrc:%.cc=%.o) $(factorysrc:%.y=%.o)\n```\n\ninto the following two lines:\n\n```\nfactoryobj :=   $(factorysrc:%.cc=%.o)\nfactoryobj :=   $(factoryobj:%.y=%.o)\n```\n\nmade the resulting Singular spkg build on OS X 10.4. But after installing it into Sage-4.1.rc0, Sage doesn't even start, it fails with:\n\n```\nImportError: dlopen(/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so, 2): Symbol not found: ___eprintf\n  Referenced from: /Users/Shared/sage/sage-4.1.rc0/local/lib//libsingular.dylib\n  Expected in: dynamic lookup\n```\n\nThis might be due to the fact that I had dropped in the 3.1.0.2 Singular spkg before, so I am re-running the build from the start. (I doubt that it'll help, but let's see.)\n\nFor the record, skipping through the install logs, I spotted another error (this time \"copy'n'paste\") in the Singular 3.1.0.4 build scripts. In /src/libfac/Makefile.in, the two identical lines 157/158 read:\n\n```\n\t-$(RANLIB) ${libdir}/libsingfac_g.a\n\t-$(RANLIB) ${libdir}/libsingfac_g.a\n```\n\nand it is obvious from the surrounding lines, that the line 158 should end with \"..._p.a\" instead of \"..._g.a\".\n\n`@`Martin: Would you please report the findings so far upstream?",
    "created_at": "2009-07-06T20:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6470#issuecomment-52207",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

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

archive/issue_comments_052208.json:
```json
{
    "body": "No, building from scratch with the \"healed\" 3.1.0.4 Singular spkg didn't bring any news. Here's the full error message if one wants to start sage:\n\n```\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n\n/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67 \n     68 \n\n/Users/Shared/sage/sage-4.1.rc0/local/bin/ipy_profile_sage.py in <module>()\n      5     preparser(True)\n      6 \n----> 7     import sage.all_cmdline\n      8     sage.all_cmdline._init_cmdline(globals())\n      9 \n\n/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/all_cmdline.py in <module>()\n     12 try:\n     13 \n---> 14     from sage.all import *\n     15     from sage.calculus.predefined import x\n     16     preparser(on=True)\n\n/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/all.py in <module>()\n     70 get_sigs()\n     71 \n---> 72 from sage.rings.all      import *\n     73 from sage.matrix.all     import *\n     74 \n\n/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/all.py in <module>()\n     92 \n     93 # Algebraic numbers\n\n---> 94 from qqbar import (AlgebraicRealField, is_AlgebraicRealField, AA,\n     95                    AlgebraicReal, is_AlgebraicReal,\n     96                    AlgebraicField, is_AlgebraicField, QQbar,\n\n/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/qqbar.py in <module>()\n   1417 QQy = QQ['y']\n   1418 QQy_y = QQy.gen()\n-> 1419 QQxy = QQ['x', 'y']\n   1420 QQxy_x = QQxy.gen(0)\n   1421 QQxy_y = QQxy.gen(1)\n\n/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2676)()\n\n/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)\n    288             names = arg1\n    289             n = len(names)\n--> 290             R = _multi_variate(base_ring, names, n, sparse, order)\n    291 \n    292     if arg1 is None and arg2 is None:\n\n/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _multi_variate(base_ring, names, n, sparse, order)\n    388         return R\n    389 \n--> 390     from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular\n    391     if m.integral_domain.is_IntegralDomain(base_ring):\n    392         if n < 1:\n\nImportError: dlopen(/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so, 2): Symbol not found: ___eprintf\n  Referenced from: /Users/Shared/sage/sage-4.1.rc0/local/lib//libsingular.dylib\n  Expected in: dynamic lookup\n\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n\nsage:\n```\n\nThe sage prompt appears, but even \"version()\" does not work.",
    "created_at": "2009-07-07T04:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6470#issuecomment-52208",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

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

archive/issue_comments_052209.json:
```json
{
    "body": "Hmmm,\n\nin all of Singular and all of /devel/sage/sage/rings/, I can't seem to find some \"eprintf\".\nI'll try rebuilding from scratch again, but now from my superclean (Mac OS X) Sage build partition with nothing in its PATH but \"/bin:/sbin:/usr/bin:/usr/sbin\", no directory \"/usr/local/\" at all, and so on. Oh well.\n\nCheers,\ngsw",
    "created_at": "2009-07-07T06:00:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6470#issuecomment-52209",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hmmm,

in all of Singular and all of /devel/sage/sage/rings/, I can't seem to find some "eprintf".
I'll try rebuilding from scratch again, but now from my superclean (Mac OS X) Sage build partition with nothing in its PATH but "/bin:/sbin:/usr/bin:/usr/sbin", no directory "/usr/local/" at all, and so on. Oh well.

Cheers,
gsw



---

archive/issue_comments_052210.json:
```json
{
    "body": "Building in my \"clean room\" didn't bring anything new either.\n\nBut a Google search showed some interesting information w.r.t. Mac OS X:\n\n```\n__eprintf is used inside the assert macro, and defined in libgcc2.c:\n\n#include <stdio.h>\n/* This is used by the `assert' macro.  */\nvoid\n__eprintf (const char *string, const char *expression,\n           unsigned int line, const char *filename)\n{\n  fprintf (stderr, string, expression, line, filename);\n  fflush (stderr);\n  abort ();\n}\n\nIt then appears that you are not linking with libgcc.\n```\n\nI'm not sure whether it is reasonable to try to link dynamically against libgcc --- is this library available on Mac OS X also in the absence of the XCode Tools?",
    "created_at": "2009-07-07T18:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6470#issuecomment-52210",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

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

archive/issue_events_006708.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-07T20:19:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6470#event-6708"
}
```



---

archive/issue_comments_052211.json:
```json
{
    "body": "Merging\n\nhttp://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg\n\ninto Sage-4.1.rc1. I think the upgrade can wait for sage-4.1.1.",
    "created_at": "2009-07-07T20:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6470#issuecomment-52211",
    "user": "https://github.com/rlmill"
}
```

Merging

http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg

into Sage-4.1.rc1. I think the upgrade can wait for sage-4.1.1.



---

archive/issue_comments_052212.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-07T20:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6470#issuecomment-52212",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_052213.json:
```json
{
    "body": "See #6476.",
    "created_at": "2009-07-07T20:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6470#issuecomment-52213",
    "user": "https://github.com/rlmill"
}
```

See #6476.
