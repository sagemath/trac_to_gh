# Issue 8306: Parallel inter/intra-spkg builds

archive/issues_008306.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  mhansen mvngu\n\nAlong with a primed [ccache](http://ccache.samba.org/), compiling multiple spkgs in parallel may significantly speed up Sage builds on multicore machines.\n\nSee [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/4c915ae814dd6514) for some information.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8306\n\n",
    "created_at": "2010-02-19T11:31:16Z",
    "labels": [
        "build",
        "major",
        "enhancement"
    ],
    "title": "Parallel inter/intra-spkg builds",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8306",
    "user": "mpatel"
}
```
Assignee: GeorgSWeber

CC:  mhansen mvngu

Along with a primed [ccache](http://ccache.samba.org/), compiling multiple spkgs in parallel may significantly speed up Sage builds on multicore machines.

See [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/4c915ae814dd6514) for some information.

Issue created by migration from https://trac.sagemath.org/ticket/8306





---

archive/issue_comments_073598.json:
```json
{
    "body": "See #7943 and #8191 for recent changes to `makefile`, `spkg/install`, and `spkg/standard/deps`.",
    "created_at": "2010-02-25T11:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73598",
    "user": "mpatel"
}
```

See #7943 and #8191 for recent changes to `makefile`, `spkg/install`, and `spkg/standard/deps`.



---

archive/issue_comments_073599.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-25T17:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73599",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073600.json:
```json
{
    "body": "With a \"primed\" compiler cache, i.e., I've already built Sage at least once, I can build Sage sans docs in about 15-20 minutes on an otherwise mostly idle sage.math --- with `make -j20`.  The long doctests pass (after I've built the docs).",
    "created_at": "2010-02-25T17:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73600",
    "user": "mpatel"
}
```

With a "primed" compiler cache, i.e., I've already built Sage at least once, I can build Sage sans docs in about 15-20 minutes on an otherwise mostly idle sage.math --- with `make -j20`.  The long doctests pass (after I've built the docs).



---

archive/issue_comments_073601.json:
```json
{
    "body": "What is it about eclib which makes this fail?  I would be happy to change it if only I knew -- the \"exceptionally clear explanation\" you refer to was not quite clear enough for me...  John",
    "created_at": "2010-02-25T19:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73601",
    "user": "cremona"
}
```

What is it about eclib which makes this fail?  I would be happy to change it if only I knew -- the "exceptionally clear explanation" you refer to was not quite clear enough for me...  John



---

archive/issue_comments_073602.json:
```json
{
    "body": "Oops.  That was an attempt at humor.\n\nI don't know why the build fails.  [Here's a log](http://sage.math.washington.edu/home/mpatel/trac/8306/eclib-20080310.p9.log) from building eclib with `+`.\n\nA possibly related problem is that the top-level make doesn't notice the error.  It keeps going until \"Sage build/upgrade complete!\".  I'll see what happens if I add `$(INST)/$(ECLIB)` to \"all\"'s list of dependencies.",
    "created_at": "2010-02-26T23:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73602",
    "user": "mpatel"
}
```

Oops.  That was an attempt at humor.

I don't know why the build fails.  [Here's a log](http://sage.math.washington.edu/home/mpatel/trac/8306/eclib-20080310.p9.log) from building eclib with `+`.

A possibly related problem is that the top-level make doesn't notice the error.  It keeps going until "Sage build/upgrade complete!".  I'll see what happens if I add `$(INST)/$(ECLIB)` to "all"'s list of dependencies.



---

archive/issue_comments_073603.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> [...] I'll see what happens if I add `$(INST)/$(ECLIB)` to \"all\"'s list of dependencies.\nSame result.  All of the other spkgs build properly.  But I definitely need to figure out why this happens with eclib and check the other spkgs for similar potential behavior.",
    "created_at": "2010-02-27T03:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73603",
    "user": "mpatel"
}
```

Replying to [comment:6 mpatel]:
> [...] I'll see what happens if I add `$(INST)/$(ECLIB)` to "all"'s list of dependencies.
Same result.  All of the other spkgs build properly.  But I definitely need to figure out why this happens with eclib and check the other spkgs for similar potential behavior.



---

archive/issue_comments_073604.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-27T03:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73604",
    "user": "mpatel"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073605.json:
```json
{
    "body": "Attachment\n\nTweak eclib `Makefile`s so it builds with `+`.  eclib src repo.",
    "created_at": "2010-02-27T05:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73605",
    "user": "mpatel"
}
```

Attachment

Tweak eclib `Makefile`s so it builds with `+`.  eclib src repo.



---

archive/issue_comments_073606.json:
```json
{
    "body": "[attachment:eclib_makefiles.patch This patch] gets eclib to build with `+`.  I noticed that eclib's `spkg-install` contains\n\n```sh\nif [ \"$MAKE\" == gmake ]; then \n   echo \"using gmake\"\nelse\n   echo \"Disabling parallel make for now\"\n   MAKE=make; export $MAKE\nfi\n```\n\nIs there a particular reason for this?",
    "created_at": "2010-02-27T05:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73606",
    "user": "mpatel"
}
```

[attachment:eclib_makefiles.patch This patch] gets eclib to build with `+`.  I noticed that eclib's `spkg-install` contains

```sh
if [ "$MAKE" == gmake ]; then 
   echo "using gmake"
else
   echo "Disabling parallel make for now"
   MAKE=make; export $MAKE
fi
```

Is there a particular reason for this?



---

archive/issue_comments_073607.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-27T06:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73607",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073608.json:
```json
{
    "body": "I've updated the attachments so the usual build behavior is the default.  To tell make it's OK to build multiple spkgs at a time, set `PARALLEL_SPKG_BUILD=\"yes\"` near the top of `spkg/standard/deps`.\n\nThe new `deps` \"depends\" on an eclib spkg with [attachment:eclib_makefiles.patch] (or an equivalent).  Should I make it part of #8357?",
    "created_at": "2010-02-27T07:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73608",
    "user": "mpatel"
}
```

I've updated the attachments so the usual build behavior is the default.  To tell make it's OK to build multiple spkgs at a time, set `PARALLEL_SPKG_BUILD="yes"` near the top of `spkg/standard/deps`.

The new `deps` "depends" on an eclib spkg with [attachment:eclib_makefiles.patch] (or an equivalent).  Should I make it part of #8357?



---

archive/issue_comments_073609.json:
```json
{
    "body": "Replying to [comment:10 mpatel]:\n> I've updated the attachments so the usual build behavior is the default.  To tell make it's OK to build multiple spkgs at a time, set `PARALLEL_SPKG_BUILD=\"yes\"` near the top of `spkg/standard/deps`.\nThat should be \"near the top of `spkg/install`.\"",
    "created_at": "2010-02-27T07:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73609",
    "user": "mpatel"
}
```

Replying to [comment:10 mpatel]:
> I've updated the attachments so the usual build behavior is the default.  To tell make it's OK to build multiple spkgs at a time, set `PARALLEL_SPKG_BUILD="yes"` near the top of `spkg/standard/deps`.
That should be "near the top of `spkg/install`."



---

archive/issue_comments_073610.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-27T10:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73610",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073611.json:
```json
{
    "body": "The idea seems excellent. Ir is such a waste on modern machines to \n\nI think it would be a lot better if an environment variable SAGE_PARALLEL_BUILD or SAGE_PARALLEL_SPKG_BUILD was set to \"yes\", rather than require the user to edit the spkg/install. Since virtually all other environement variables are prefixed with SAGE (e.g. SAGE_FORTRAN, SAGE_FORTRAN_LIB, SAGE64 ...) I would do likewise for consistency. \n\nIt would be necessary to test this on different architectures and operating systems. It is quite possible that the time different packages take to build differs vastly by the processor and operating system. It is likely that package X always builds in parallel before package Y on sage.math, but Y would build before X on another system. That could well mean there are dependencies existing that are not apparerent in serial builds. \n\nFor example, ATLAS takes at least 10x as long to build on 't2' as it does on my own SPARC, simply because there are no default tuning parameters for ATLAS on t2, so it is tuned each time. That is an extreme example, but it is well known some machine are faster at some tasks than others, but slower on other tasks. Some packages have assembly language support for certain processors, but not others. Several packages go through some sort of tuning process to determine the optimal build parameters. So the timings could be expected to be different on different operating systems. \n\nAt the very least, this should be tested on t2 and bsd, as they run Solaris and OS X repectively. (When testing on t2, I would suggest using j of 256 or 512. That machine has 128 threads). For t2, one would need to use sage 4.3.0.1. (I think any changes to spkg/install and spkg/standard/deps should minimal between 4.3.0.1 and 4.3.3.  There are probably no changes at all. \n\nIt would be safer to compare the md5 checksums of libraries & binaries built in series and parallel to prove they are indeed the same. It is quite possible that there are failures that just do not get exercised by doctests. However, that may not be fully possible, as perhaps some would have the build time information encoded in some way. But I would at least investigate. \n\nOverall, I think this is a really **excellent** idea, but it needs further testing before I'd want to give it a positive review. \n\nDave",
    "created_at": "2010-02-27T10:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73611",
    "user": "drkirkby"
}
```

The idea seems excellent. Ir is such a waste on modern machines to 

I think it would be a lot better if an environment variable SAGE_PARALLEL_BUILD or SAGE_PARALLEL_SPKG_BUILD was set to "yes", rather than require the user to edit the spkg/install. Since virtually all other environement variables are prefixed with SAGE (e.g. SAGE_FORTRAN, SAGE_FORTRAN_LIB, SAGE64 ...) I would do likewise for consistency. 

It would be necessary to test this on different architectures and operating systems. It is quite possible that the time different packages take to build differs vastly by the processor and operating system. It is likely that package X always builds in parallel before package Y on sage.math, but Y would build before X on another system. That could well mean there are dependencies existing that are not apparerent in serial builds. 

For example, ATLAS takes at least 10x as long to build on 't2' as it does on my own SPARC, simply because there are no default tuning parameters for ATLAS on t2, so it is tuned each time. That is an extreme example, but it is well known some machine are faster at some tasks than others, but slower on other tasks. Some packages have assembly language support for certain processors, but not others. Several packages go through some sort of tuning process to determine the optimal build parameters. So the timings could be expected to be different on different operating systems. 

At the very least, this should be tested on t2 and bsd, as they run Solaris and OS X repectively. (When testing on t2, I would suggest using j of 256 or 512. That machine has 128 threads). For t2, one would need to use sage 4.3.0.1. (I think any changes to spkg/install and spkg/standard/deps should minimal between 4.3.0.1 and 4.3.3.  There are probably no changes at all. 

It would be safer to compare the md5 checksums of libraries & binaries built in series and parallel to prove they are indeed the same. It is quite possible that there are failures that just do not get exercised by doctests. However, that may not be fully possible, as perhaps some would have the build time information encoded in some way. But I would at least investigate. 

Overall, I think this is a really **excellent** idea, but it needs further testing before I'd want to give it a positive review. 

Dave



---

archive/issue_comments_073612.json:
```json
{
    "body": "I didn't write eclib's spkg-install, and I know that several people have changed it in the past -- there's at least one ticket out there specifically about managing eclib's Makefiles.\n\nNext time someone edits it they should change the two occurrences of \"cremona\" in error messages to \"eclib\".",
    "created_at": "2010-02-27T11:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73612",
    "user": "cremona"
}
```

I didn't write eclib's spkg-install, and I know that several people have changed it in the past -- there's at least one ticket out there specifically about managing eclib's Makefiles.

Next time someone edits it they should change the two occurrences of "cremona" in error messages to "eclib".



---

archive/issue_comments_073613.json:
```json
{
    "body": "Replying to [comment:14 cremona]:\n> I didn't write eclib's spkg-install, and I know that several people have changed it in the past -- there's at least one ticket out there specifically about managing eclib's Makefiles.\nIndeed, the workaround is from #4228.\n> Next time someone edits it they should change the two occurrences of \"cremona\" in error messages to \"eclib\".\nI'll make a new spkg available at #8357.",
    "created_at": "2010-02-27T22:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73613",
    "user": "mpatel"
}
```

Replying to [comment:14 cremona]:
> I didn't write eclib's spkg-install, and I know that several people have changed it in the past -- there's at least one ticket out there specifically about managing eclib's Makefiles.
Indeed, the workaround is from #4228.
> Next time someone edits it they should change the two occurrences of "cremona" in error messages to "eclib".
I'll make a new spkg available at #8357.



---

archive/issue_comments_073614.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> I'll make a new spkg available at #8357.\nDone, with a provisional version, at least.",
    "created_at": "2010-02-28T00:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73614",
    "user": "mpatel"
}
```

Replying to [comment:15 mpatel]:
> I'll make a new spkg available at #8357.
Done, with a provisional version, at least.



---

archive/issue_comments_073615.json:
```json
{
    "body": "Replying to [comment:13 drkirkby]:\n\n> The idea seems excellent. Ir is such a waste on modern machines to\n\nThanks!  I'll get an account on bsd and try to test on both bsd and t2, as well.\n\n`SAGE_PARALLEL_SPKG_BUILD` looks good.\n\nMy motivation for making the new feature optional, for now, is so we can get feedback (via sage-devel) from early testers about a much wider range of build conditions and configurations.  It's likely they'll report problems, and we can attempt to solve them before we make it the default for everyone.",
    "created_at": "2010-02-28T01:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73615",
    "user": "mpatel"
}
```

Replying to [comment:13 drkirkby]:

> The idea seems excellent. Ir is such a waste on modern machines to

Thanks!  I'll get an account on bsd and try to test on both bsd and t2, as well.

`SAGE_PARALLEL_SPKG_BUILD` looks good.

My motivation for making the new feature optional, for now, is so we can get feedback (via sage-devel) from early testers about a much wider range of build conditions and configurations.  It's likely they'll report problems, and we can attempt to solve them before we make it the default for everyone.



---

archive/issue_comments_073616.json:
```json
{
    "body": "Attachment\n\nMake `sage -i foo.spkg` also append to `spkg/logs/foo.spkg`.  **scripts** repo.",
    "created_at": "2010-03-01T05:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73616",
    "user": "mpatel"
}
```

Attachment

Make `sage -i foo.spkg` also append to `spkg/logs/foo.spkg`.  **scripts** repo.



---

archive/issue_comments_073617.json:
```json
{
    "body": "Again, against 4.3.3 on sage.math, this appears to work well.  With `SAGE_CHECK=\"yes\"`, I get the same known errors\n\n```\n     sage: An error occurred while testing sagetex-2.2.3\n     sage: An error occurred while testing pyprocessing-0.52.p0\n     sage: An error occurred while testing sqlalchemy-0.4.6.p1\n```\n\nwith and without parallel spkg builds.  All the docs build and the long doctests pass.\n\nAgainst 4.3.0.1 on t2: It builds and runs --- I used a stand-in atlas spkg that just copies the files from the [existing binary build](http://boxen.math.washington.edu/sage/solaris/index.html).  \"Several\" doctests still fail or segfault.  With `SAGE_CHECK=\"yes\"`, I get the known testing errors, a known testing error with eclib (see #8357),  and *maybe* a testing error with R.  I ran out of patience with the latter.  I don't have time to test further on t2 / *Solaris.  It's probably better that someone else test with 4.3.3+ on a capable machine.\n\nIf I have time (and an account), I'll run a few tests on `bsd.math`.\n\nNote: With `SAGE_PARALLEL_SPKG_BUILD=\"yes\"`, I find it useful to run one of\n\n```sh\ngrep \"An error occurred\" SAGE_ROOT/install.log\nls -l SAGE_ROOT/spkg/installed | wc\n```\n\nwhen I see `\"Sage build/upgrade complete!\"`.  Maybe we should add a similar check at the end of `install`?\n\nPlease test and let us know what happens.  I didn't log detailed statistics, but with a warm compiler cache, I noticed a roughly three-fold speedup.  From a recent run on sage.math:\n\n```\nSage build/upgrade complete!\n\nreal    15m44.846s\nuser    45m55.780s\nsys     11m10.470s\n```\n",
    "created_at": "2010-03-01T16:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73617",
    "user": "mpatel"
}
```

Again, against 4.3.3 on sage.math, this appears to work well.  With `SAGE_CHECK="yes"`, I get the same known errors

```
     sage: An error occurred while testing sagetex-2.2.3
     sage: An error occurred while testing pyprocessing-0.52.p0
     sage: An error occurred while testing sqlalchemy-0.4.6.p1
```

with and without parallel spkg builds.  All the docs build and the long doctests pass.

Against 4.3.0.1 on t2: It builds and runs --- I used a stand-in atlas spkg that just copies the files from the [existing binary build](http://boxen.math.washington.edu/sage/solaris/index.html).  "Several" doctests still fail or segfault.  With `SAGE_CHECK="yes"`, I get the known testing errors, a known testing error with eclib (see #8357),  and *maybe* a testing error with R.  I ran out of patience with the latter.  I don't have time to test further on t2 / *Solaris.  It's probably better that someone else test with 4.3.3+ on a capable machine.

If I have time (and an account), I'll run a few tests on `bsd.math`.

Note: With `SAGE_PARALLEL_SPKG_BUILD="yes"`, I find it useful to run one of

```sh
grep "An error occurred" SAGE_ROOT/install.log
ls -l SAGE_ROOT/spkg/installed | wc
```

when I see `"Sage build/upgrade complete!"`.  Maybe we should add a similar check at the end of `install`?

Please test and let us know what happens.  I didn't log detailed statistics, but with a warm compiler cache, I noticed a roughly three-fold speedup.  From a recent run on sage.math:

```
Sage build/upgrade complete!

real    15m44.846s
user    45m55.780s
sys     11m10.470s
```




---

archive/issue_comments_073618.json:
```json
{
    "body": "Replying to [comment:19 mpatel]:\n\n> [... ...] with a warm compiler cache, I noticed a roughly three-fold speedup. [... ...]\n\nI should add that this could be very useful to a release manager.",
    "created_at": "2010-03-01T16:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73618",
    "user": "mpatel"
}
```

Replying to [comment:19 mpatel]:

> [... ...] with a warm compiler cache, I noticed a roughly three-fold speedup. [... ...]

I should add that this could be very useful to a release manager.



---

archive/issue_comments_073619.json:
```json
{
    "body": "Replying to [comment:20 mpatel]:\n\n> I should add that this could be very useful to a release manager.\nWhat exactly is a \"warm compiler cache\" ? A Google on the term only shows only references to Sage.",
    "created_at": "2010-03-01T16:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73619",
    "user": "drkirkby"
}
```

Replying to [comment:20 mpatel]:

> I should add that this could be very useful to a release manager.
What exactly is a "warm compiler cache" ? A Google on the term only shows only references to Sage.



---

archive/issue_comments_073620.json:
```json
{
    "body": "Oops.  I just mean that I've set up [ccache](http://ccache.samba.org/) and compiled Sage twice, say.  Stats from t2:\n\n```\nmpatel@t2 ~$ ccache -s\ncache directory                     /home/mpatel/.ccache\ncache hit                          34598\ncache miss                         23288\ncalled for link                     5050\nmultiple source files                 14\ncompiler produced stdout              10\ncompile failed                       774\npreprocessor error                   465\ncouldn't find the compiler            39\nnot a C/C++ file                    3409\nautoconf compile/link               7006\nunsupported compiler option         2815\nno input file                       3107\nfiles in cache                     45248\ncache size                           2.3 Gbytes\nmax cache size                       5.0 Gbytes\n```\n\n(I think it'll be faster in `/scratch`, but I don't know by how much.)  From sage.math:\n\n```\nmpatel@sage ~$ ccache -s\ncache directory                     /scratch/mpatel/.ccache\ncache hit                         371602\ncache miss                         61435\ncalled for link                    48342\nmultiple source files                131\ncompiler produced stdout              78\ncompile failed                      2635\nccache internal error                  2\npreprocessor error                  2433\ncache file missing                     4\nnot a C/C++ file                   15851\nautoconf compile/link              39762\nunsupported compiler option        21463\nno input file                      18871\nfiles in cache                    106837\ncache size                           4.6 Gbytes\nmax cache size                      10.0 Gbytes\n```\n\n(Lots of testing with different `X` values.)  I've been using ccache 2.4.  I don't know how 3.0pre0 compares.",
    "created_at": "2010-03-01T16:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73620",
    "user": "mpatel"
}
```

Oops.  I just mean that I've set up [ccache](http://ccache.samba.org/) and compiled Sage twice, say.  Stats from t2:

```
mpatel@t2 ~$ ccache -s
cache directory                     /home/mpatel/.ccache
cache hit                          34598
cache miss                         23288
called for link                     5050
multiple source files                 14
compiler produced stdout              10
compile failed                       774
preprocessor error                   465
couldn't find the compiler            39
not a C/C++ file                    3409
autoconf compile/link               7006
unsupported compiler option         2815
no input file                       3107
files in cache                     45248
cache size                           2.3 Gbytes
max cache size                       5.0 Gbytes
```

(I think it'll be faster in `/scratch`, but I don't know by how much.)  From sage.math:

```
mpatel@sage ~$ ccache -s
cache directory                     /scratch/mpatel/.ccache
cache hit                         371602
cache miss                         61435
called for link                    48342
multiple source files                131
compiler produced stdout              78
compile failed                      2635
ccache internal error                  2
preprocessor error                  2433
cache file missing                     4
not a C/C++ file                   15851
autoconf compile/link              39762
unsupported compiler option        21463
no input file                      18871
files in cache                    106837
cache size                           4.6 Gbytes
max cache size                      10.0 Gbytes
```

(Lots of testing with different `X` values.)  I've been using ccache 2.4.  I don't know how 3.0pre0 compares.



---

archive/issue_comments_073621.json:
```json
{
    "body": "Reminder: Update #8263, if it's necessary.",
    "created_at": "2010-03-02T23:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73621",
    "user": "mpatel"
}
```

Reminder: Update #8263, if it's necessary.



---

archive/issue_comments_073622.json:
```json
{
    "body": "Ticket #8432 adds iconv to the dependency rule for building gd. So you don't need to implement that rule here.",
    "created_at": "2010-03-04T04:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73622",
    "user": "mvngu"
}
```

Ticket #8432 adds iconv to the dependency rule for building gd. So you don't need to implement that rule here.



---

archive/issue_comments_073623.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-05T01:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73623",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073624.json:
```json
{
    "body": "I've attached updates rebased vs. #7943 and #8432.",
    "created_at": "2010-03-05T01:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73624",
    "user": "mpatel"
}
```

I've attached updates rebased vs. #7943 and #8432.



---

archive/issue_comments_073625.json:
```json
{
    "body": "Adding Mike Hansen to the Cc: list.",
    "created_at": "2010-03-05T01:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73625",
    "user": "mpatel"
}
```

Adding Mike Hansen to the Cc: list.



---

archive/issue_comments_073626.json:
```json
{
    "body": "Strange error when building on sage.math with `MAKE=\"make -j23 -l25\"` and `SAGE_PARALLEL_SPKG_BUILD` **not** set:\n\n```\nNow install rpy\n**************************************************************************\nYou must compile Sage first using 'make' in the Sage root directory.\n(If you have already compiled Sage, you must set the SAGE_ROOT variable in \nthe file '/mnt/usb1/scratch/mpatel/tmp/sage-4.3.4.alpha0/sage').\n**************************************************************************\nError installing rpy.\n```\n",
    "created_at": "2010-03-05T03:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73626",
    "user": "mpatel"
}
```

Strange error when building on sage.math with `MAKE="make -j23 -l25"` and `SAGE_PARALLEL_SPKG_BUILD` **not** set:

```
Now install rpy
**************************************************************************
You must compile Sage first using 'make' in the Sage root directory.
(If you have already compiled Sage, you must set the SAGE_ROOT variable in 
the file '/mnt/usb1/scratch/mpatel/tmp/sage-4.3.4.alpha0/sage').
**************************************************************************
Error installing rpy.
```




---

archive/issue_comments_073627.json:
```json
{
    "body": "Fixed by appending `SAGE_SCRIPTS` to `BASE`.  I'm putting the updates here:\n\n* http://sage.math.washington.edu/home/mpatel/trac/8306",
    "created_at": "2010-03-05T04:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73627",
    "user": "mpatel"
}
```

Fixed by appending `SAGE_SCRIPTS` to `BASE`.  I'm putting the updates here:

* http://sage.math.washington.edu/home/mpatel/trac/8306



---

archive/issue_comments_073628.json:
```json
{
    "body": "With Sage 4.3.4.alpha0 on sage.math, I updated \"deps\" and \"install\" with [deps](http://sage.math.washington.edu/home/mpatel/trac/8306/deps) and [install](http://sage.math.washington.edu/home/mpatel/trac/8306/install). I exported these environment variables:\n\n```\nexport SAGE_PARALLEL_SPKG_BUILD=\"yes\"\nexport MAKE=\"make -j4\"\nmake \n```\n\nThe build failed with \n\n```\nSuccessfully installed gap-4.4.12.p1\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing gap-4.4.12.p1.spkg\nmake[1]: Leaving directory `/dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/spkg'\n\nreal    45m12.933s\nuser    105m39.580s\nsys     15m46.550s\nError building Sage.\nTraceback (most recent call last):\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/local/bin/sage-preparse\", line 230, in <module>\n    do_preparse(f)\n  File \"/dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/local/bin/sage-preparse\", line 118, in do_preparse\n    from sage.misc.preparser  import preparse_file\nImportError: No module named sage.misc.preparser\n```\n",
    "created_at": "2010-03-07T04:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73628",
    "user": "mvngu"
}
```

With Sage 4.3.4.alpha0 on sage.math, I updated "deps" and "install" with [deps](http://sage.math.washington.edu/home/mpatel/trac/8306/deps) and [install](http://sage.math.washington.edu/home/mpatel/trac/8306/install). I exported these environment variables:

```
export SAGE_PARALLEL_SPKG_BUILD="yes"
export MAKE="make -j4"
make 
```

The build failed with 

```
Successfully installed gap-4.4.12.p1
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing gap-4.4.12.p1.spkg
make[1]: Leaving directory `/dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/spkg'

real    45m12.933s
user    105m39.580s
sys     15m46.550s
Error building Sage.
Traceback (most recent call last):
  File "/dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/local/bin/sage-preparse", line 230, in <module>
    do_preparse(f)
  File "/dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/local/bin/sage-preparse", line 118, in do_preparse
    from sage.misc.preparser  import preparse_file
ImportError: No module named sage.misc.preparser
```




---

archive/issue_comments_073629.json:
```json
{
    "body": "The eclib and sage packages did not build:\n\n```sh\n$ grep \"An error occurred\" /dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/spkg/logs/*\neclib-20080310.p9.log:sage: An error occurred while installing eclib-20080310.p9\nsage-4.3.4.alpha0.log:sage: An error occurred while installing sage-4.3.4.alpha0\n```\n\nTicket #8357's `eclib-*.spkg` should fix this.  I apologize for not mentioning it in \"To test the changes\".\n\nQuestions:\n\n* If I untar `sage-*.tar`, copy over `install`, etc., and start the build, then at some point, `install` is overwritten with the original version.  Do you know which package or script does this?  For my tests, I've run `chmod u-w install` before `make`.\n\n* I don't know why the build didn't stop when eclib failed to build.  This seems strange.  The file `installed/eclib*` is missing and according to `deps`, it's required for the `sage` target.  Similarly, `installed/sage*` is a prerequisite for gap.  Does anyone know why this happens?  Can we modify `deps` to avoid it?",
    "created_at": "2010-03-07T05:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73629",
    "user": "mpatel"
}
```

The eclib and sage packages did not build:

```sh
$ grep "An error occurred" /dev/shm/mvngu/sandbox/sage-4.3.4.alpha0/spkg/logs/*
eclib-20080310.p9.log:sage: An error occurred while installing eclib-20080310.p9
sage-4.3.4.alpha0.log:sage: An error occurred while installing sage-4.3.4.alpha0
```

Ticket #8357's `eclib-*.spkg` should fix this.  I apologize for not mentioning it in "To test the changes".

Questions:

* If I untar `sage-*.tar`, copy over `install`, etc., and start the build, then at some point, `install` is overwritten with the original version.  Do you know which package or script does this?  For my tests, I've run `chmod u-w install` before `make`.

* I don't know why the build didn't stop when eclib failed to build.  This seems strange.  The file `installed/eclib*` is missing and according to `deps`, it's required for the `sage` target.  Similarly, `installed/sage*` is a prerequisite for gap.  Does anyone know why this happens?  Can we modify `deps` to avoid it?



---

archive/issue_comments_073630.json:
```json
{
    "body": "To install and use ccache, I did this\n\n```sh\nwget http://samba.org/ftp/ccache/ccache-2.4.tar.gz\ntar zxvf ccache-2.4.tar.gz\ncd ccache-2.4\n./configure\nmake\ncp ccache ~/bin\n```\n\nBecause I set\n\n```sh\nPATH=\".:$HOME/bin:$HOME/apps/sage/local/bin:$PATH\"\n```\n\nin `~/.profile`, I did\n\n```sh\ncd ~/bin\nln -s c++ ccache\nln -s cc ccache\nln -s g++ ccache\nln -s g++-3.4 ccache\nln -s g++-4.2 ccache\nln -s gcc ccache\nln -s gcc-3.4 ccache\nln -s gcc-4.1 ccache\nln -s gcc-4.2 ccache\nln -s x86_64-linux-gnu-g++ ccache\nln -s x86_64-linux-gnu-g++-3.4 ccache\nln -s x86_64-linux-gnu-g++-4.2 ccache\nln -s x86_64-linux-gnu-gcc ccache\nln -s x86_64-linux-gnu-gcc-3.4 ccache\nln -s x86_64-linux-gnu-gcc-4.1 ccache\nln -s x86_64-linux-gnu-gcc-4.2 ccache\nln -s x86_64-linux-gnu-gcj-4.2 ccache\nln -s x86_64-linux-gnu-gfortran ccache\nln -s x86_64-linux-gnu-gfortran-4.1 ccache\nln -s x86_64-linux-gnu-gfortran-4.2 ccache\n```\n\nThis may be overkill.  In `~/.bashrc`, I've put\n\n```sh\nexport CCACHE_DIR=/scratch/mpatel/.ccache\n```\n",
    "created_at": "2010-03-07T06:31:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73630",
    "user": "mpatel"
}
```

To install and use ccache, I did this

```sh
wget http://samba.org/ftp/ccache/ccache-2.4.tar.gz
tar zxvf ccache-2.4.tar.gz
cd ccache-2.4
./configure
make
cp ccache ~/bin
```

Because I set

```sh
PATH=".:$HOME/bin:$HOME/apps/sage/local/bin:$PATH"
```

in `~/.profile`, I did

```sh
cd ~/bin
ln -s c++ ccache
ln -s cc ccache
ln -s g++ ccache
ln -s g++-3.4 ccache
ln -s g++-4.2 ccache
ln -s gcc ccache
ln -s gcc-3.4 ccache
ln -s gcc-4.1 ccache
ln -s gcc-4.2 ccache
ln -s x86_64-linux-gnu-g++ ccache
ln -s x86_64-linux-gnu-g++-3.4 ccache
ln -s x86_64-linux-gnu-g++-4.2 ccache
ln -s x86_64-linux-gnu-gcc ccache
ln -s x86_64-linux-gnu-gcc-3.4 ccache
ln -s x86_64-linux-gnu-gcc-4.1 ccache
ln -s x86_64-linux-gnu-gcc-4.2 ccache
ln -s x86_64-linux-gnu-gcj-4.2 ccache
ln -s x86_64-linux-gnu-gfortran ccache
ln -s x86_64-linux-gnu-gfortran-4.1 ccache
ln -s x86_64-linux-gnu-gfortran-4.2 ccache
```

This may be overkill.  In `~/.bashrc`, I've put

```sh
export CCACHE_DIR=/scratch/mpatel/.ccache
```




---

archive/issue_comments_073631.json:
```json
{
    "body": "I also set a larger ccache size with `ccache -M 10G`.  To print statistics run `ccache -s`.",
    "created_at": "2010-03-07T06:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73631",
    "user": "mpatel"
}
```

I also set a larger ccache size with `ccache -M 10G`.  To print statistics run `ccache -s`.



---

archive/issue_comments_073632.json:
```json
{
    "body": "The patch [trac_8306_scripts-spkg_log_files.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8306/trac_8306_scripts-spkg_log_files.patch) introduces the environment variable\n\n```\nSAGE_LOGS=\"$SAGE_ROOT/spkg/logs\"\n```\n\nfor storing build logs of spkg's. A closely related idea, but for MD5 integrity check files, can be found at #7617. What could be implemented is an environment variable like\n\n```\nSAGE_SPKG_MD5=\"$SAGE_ROOT/spkg/md5\"\n```\n\nAs of Sage 4.3.3, the SageTeX package is the only standard package that has an MD5 file bundled together with the package itself to result in an spkg. Whenever the SageTeX spkg is built, its MD5 file is extracted and lingers under \n\n```\nSAGE_ROOT/spkg/build\n```\n\nPerhaps a more appropriate place is to deposit MD5 files of spkg's under\n\n```\nSAGE_ROOT/spkg/md5\n```\n\nThis would nicely solve ticket #329 after more than 3 years.",
    "created_at": "2010-03-07T06:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73632",
    "user": "mvngu"
}
```

The patch [trac_8306_scripts-spkg_log_files.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8306/trac_8306_scripts-spkg_log_files.patch) introduces the environment variable

```
SAGE_LOGS="$SAGE_ROOT/spkg/logs"
```

for storing build logs of spkg's. A closely related idea, but for MD5 integrity check files, can be found at #7617. What could be implemented is an environment variable like

```
SAGE_SPKG_MD5="$SAGE_ROOT/spkg/md5"
```

As of Sage 4.3.3, the SageTeX package is the only standard package that has an MD5 file bundled together with the package itself to result in an spkg. Whenever the SageTeX spkg is built, its MD5 file is extracted and lingers under 

```
SAGE_ROOT/spkg/build
```

Perhaps a more appropriate place is to deposit MD5 files of spkg's under

```
SAGE_ROOT/spkg/md5
```

This would nicely solve ticket #329 after more than 3 years.



---

archive/issue_comments_073633.json:
```json
{
    "body": "We could do the integrity check and relocation (`mv -f foo.md5 \"$SAGE_SPKG_MD5\"`) in `spkg-checksum`, say, call this script in `sage-spkg`, test `$?`, print a message, etc.  Or we could just delete `foo.md5`.  How useful is the file outside the archive?",
    "created_at": "2010-03-07T09:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73633",
    "user": "mpatel"
}
```

We could do the integrity check and relocation (`mv -f foo.md5 "$SAGE_SPKG_MD5"`) in `spkg-checksum`, say, call this script in `sage-spkg`, test `$?`, print a message, etc.  Or we could just delete `foo.md5`.  How useful is the file outside the archive?



---

archive/issue_comments_073634.json:
```json
{
    "body": "Replying to [comment:32 mpatel]:\n>  * I don't know why the build didn't stop when eclib failed to build.  This seems strange.  The file `installed/eclib*` is missing and according to `deps`, it's required for the `sage` target.  Similarly, `installed/sage*` is a prerequisite for gap.  Does anyone know why this happens?  Can we modify `deps` to avoid it?\n\nThe problem is that the exit status `$?` of\n\n```sh\n$(SAGE_SPKG) $(FOO) 2>&1 | tee -a $(SAGE_LOGS)/$(FOO).log\n```\n\nis the exit status of `tee`, but we need the exit status of `sage-spkg`.  (I found some other workarounds [here](http://www.unix.com/shell-programming-scripting/92163-command-does-not-return-exit-status-due-tee.html).)  We can get this with `$PIPESTATUS` in `bash`.  We could add a helper script somewhere that runs the pipeline and exits with the status of `sage-spkg`.\n\nOr we could use\n\n```sh\n$(SAGE_SPKG) $(FOO) 2>&1 | tee -a $(SAGE_LOGS)/$(FOO).log | grep \"sage: An error occurred while\"\n```\n\nif we test the status of `grep`.  The `sage-spkg` script prints this error string when `spkg-install` or `spkg-check` fails.   We could also print the string in a few other places in `sage-spkg` (search for `exit 1`).\n\nThoughts?",
    "created_at": "2010-03-07T14:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73634",
    "user": "mpatel"
}
```

Replying to [comment:32 mpatel]:
>  * I don't know why the build didn't stop when eclib failed to build.  This seems strange.  The file `installed/eclib*` is missing and according to `deps`, it's required for the `sage` target.  Similarly, `installed/sage*` is a prerequisite for gap.  Does anyone know why this happens?  Can we modify `deps` to avoid it?

The problem is that the exit status `$?` of

```sh
$(SAGE_SPKG) $(FOO) 2>&1 | tee -a $(SAGE_LOGS)/$(FOO).log
```

is the exit status of `tee`, but we need the exit status of `sage-spkg`.  (I found some other workarounds [here](http://www.unix.com/shell-programming-scripting/92163-command-does-not-return-exit-status-due-tee.html).)  We can get this with `$PIPESTATUS` in `bash`.  We could add a helper script somewhere that runs the pipeline and exits with the status of `sage-spkg`.

Or we could use

```sh
$(SAGE_SPKG) $(FOO) 2>&1 | tee -a $(SAGE_LOGS)/$(FOO).log | grep "sage: An error occurred while"
```

if we test the status of `grep`.  The `sage-spkg` script prints this error string when `spkg-install` or `spkg-check` fails.   We could also print the string in a few other places in `sage-spkg` (search for `exit 1`).

Thoughts?



---

archive/issue_comments_073635.json:
```json
{
    "body": "I have a helper script that I'm testing.  So far, it's working well, *if* I force palp to build serially.  The spkg at #8477 does this.",
    "created_at": "2010-03-07T18:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73635",
    "user": "mpatel"
}
```

I have a helper script that I'm testing.  So far, it's working well, *if* I force palp to build serially.  The spkg at #8477 does this.



---

archive/issue_comments_073636.json:
```json
{
    "body": "Replying to [comment:35 mvngu]:\n\n> Perhaps a more appropriate place is to deposit MD5 files of spkg's under\n> {{{\n> SAGE_ROOT/spkg/md5\n> }}}\n> This would nicely solve ticket #329 after more than 3 years.\n\nSee my comment on #329. The problem with md5 is that there is no standard command for getting the md5 checksum. I've seen\n\n* md5\n* md5sum\n* digest -a md5 ('digest' is part of OpenSSL, and is what I use on Solaris)\n\nIt is not a standard POSIX command. In contrast, 'cksum' is much more portable, as it is defined by POSIX. \n\nhttp://www.opengroup.org/onlinepubs/9699919799/utilities/cksum.html\n\nIt is a 32-bit bit number, so the probability of an error not being detected is around 2.3 x 10^-10.  \n\nAvoid using 'sum' - that is not portable, as the algorithm is implementation dependent. \n\nDave",
    "created_at": "2010-03-08T00:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73636",
    "user": "drkirkby"
}
```

Replying to [comment:35 mvngu]:

> Perhaps a more appropriate place is to deposit MD5 files of spkg's under
> {{{
> SAGE_ROOT/spkg/md5
> }}}
> This would nicely solve ticket #329 after more than 3 years.

See my comment on #329. The problem with md5 is that there is no standard command for getting the md5 checksum. I've seen

* md5
* md5sum
* digest -a md5 ('digest' is part of OpenSSL, and is what I use on Solaris)

It is not a standard POSIX command. In contrast, 'cksum' is much more portable, as it is defined by POSIX. 

http://www.opengroup.org/onlinepubs/9699919799/utilities/cksum.html

It is a 32-bit bit number, so the probability of an error not being detected is around 2.3 x 10^-10.  

Avoid using 'sum' - that is not portable, as the algorithm is implementation dependent. 

Dave



---

archive/issue_comments_073637.json:
```json
{
    "body": "I've updated the description with what seems to work.  With `SAGE_PARALLEL_SPKG_BUILD=\"yes\"`, `make` should now *not* start building new spkgs if it encounters a fatal error with a package.  It'll just wait for the other processes to stop.\n\nFeel free to find a better place or name for the short `pipestatus` script.",
    "created_at": "2010-03-09T04:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73637",
    "user": "mpatel"
}
```

I've updated the description with what seems to work.  With `SAGE_PARALLEL_SPKG_BUILD="yes"`, `make` should now *not* start building new spkgs if it encounters a fatal error with a package.  It'll just wait for the other processes to stop.

Feel free to find a better place or name for the short `pipestatus` script.



---

archive/issue_comments_073638.json:
```json
{
    "body": "Is the intension to use SAGE_CHECK=\"ok\", rather than SAGE_CHECK=\"yes\". I'm not sure if that's a typo in your revised description.",
    "created_at": "2010-03-09T11:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73638",
    "user": "drkirkby"
}
```

Is the intension to use SAGE_CHECK="ok", rather than SAGE_CHECK="yes". I'm not sure if that's a typo in your revised description.



---

archive/issue_comments_073639.json:
```json
{
    "body": "It's just to avoid running some [comment:ticket:8262:2 tests twice].",
    "created_at": "2010-03-09T11:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73639",
    "user": "mpatel"
}
```

It's just to avoid running some [comment:ticket:8262:2 tests twice].



---

archive/issue_comments_073640.json:
```json
{
    "body": "Building spkgs in parallel with 4.3.4.alpha1 per the description:\n\nsage.math: Still works.  Long doctests pass.\n\nbsd: Works, but sometimes palp doesn't build properly.  I think this is a problem with palp's makefiles.  I'll update #8477.  Long doctests pass.\n\nt2: Works with the [stand-in atlas package](http://sage.math.washington.edu/home/mpatel/trac/8306/atlas-3.8.3.p13.spkg) mentioned earlier and modulo a problem with cddlib that happens even with serial builds ([log](http://sage.math.washington.edu/home/mpatel/trac/8306/cddlib-094f.p5.log)).  Long doctests pass, except for `ell_rational_field`, `ell_curve_isogeny`, and `ssmod`, which timed out.  Their short versions pass.",
    "created_at": "2010-03-11T04:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73640",
    "user": "mpatel"
}
```

Building spkgs in parallel with 4.3.4.alpha1 per the description:

sage.math: Still works.  Long doctests pass.

bsd: Works, but sometimes palp doesn't build properly.  I think this is a problem with palp's makefiles.  I'll update #8477.  Long doctests pass.

t2: Works with the [stand-in atlas package](http://sage.math.washington.edu/home/mpatel/trac/8306/atlas-3.8.3.p13.spkg) mentioned earlier and modulo a problem with cddlib that happens even with serial builds ([log](http://sage.math.washington.edu/home/mpatel/trac/8306/cddlib-094f.p5.log)).  Long doctests pass, except for `ell_rational_field`, `ell_curve_isogeny`, and `ssmod`, which timed out.  Their short versions pass.



---

archive/issue_comments_073641.json:
```json
{
    "body": "On my Blade 1000 (900 MHz), bought for the US equivalent of about $75, all those tests pass, in the times indicated below: \n\n\n```\nsage -t  -long \"devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py\"\n         [933.6 s]\n\nsage -t  -long \"devel/sage/sage/modular/ssmod/ssmod.py\"     \n         [1737.7 s]\n\nsage -t  -long \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n         [1590.4 s]\n```\n\n\nGiven my Blade 1000 is faster than 't2', and the default value for SAGE_TIMOUT_LONG is 1800s, it is no surprise these timeout. You will need to increase that variable. I think 10000 s should be safe (actually I rekon 4000 s will be, but I'd play it safe). \n\nI'm surprised the short ones passed if you used the default 300 s timeout. \n\nDave",
    "created_at": "2010-03-11T05:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73641",
    "user": "drkirkby"
}
```

On my Blade 1000 (900 MHz), bought for the US equivalent of about $75, all those tests pass, in the times indicated below: 


```
sage -t  -long "devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py"
         [933.6 s]

sage -t  -long "devel/sage/sage/modular/ssmod/ssmod.py"     
         [1737.7 s]

sage -t  -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
         [1590.4 s]
```


Given my Blade 1000 is faster than 't2', and the default value for SAGE_TIMOUT_LONG is 1800s, it is no surprise these timeout. You will need to increase that variable. I think 10000 s should be safe (actually I rekon 4000 s will be, but I'd play it safe). 

I'm surprised the short ones passed if you used the default 300 s timeout. 

Dave



---

archive/issue_comments_073642.json:
```json
{
    "body": "I increased the timeout for the short tests.  I've also increased the timeout for the long tests and rerun the timed-out tests.  They pass.\n\nAlso: As far as I can tell, this ticket does not break builds where `SAGE_PARALLEL_SPKG_BUILD != \"yes\"`.",
    "created_at": "2010-03-12T09:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73642",
    "user": "mpatel"
}
```

I increased the timeout for the short tests.  I've also increased the timeout for the long tests and rerun the timed-out tests.  They pass.

Also: As far as I can tell, this ticket does not break builds where `SAGE_PARALLEL_SPKG_BUILD != "yes"`.



---

archive/issue_comments_073643.json:
```json
{
    "body": "Two comments: \n\n- Note that the sage_scripts spkg overwrites the file spkg/install, so a few minutes after you've run \"make\", that file no longer has the parallel build changes in it.  I assume that this doesn't interfere with the current build (?).  This would be fixed by implementing the changes here and making a source distribution, thereby producing a new sage_scripts spkg.  Is that the only way?  Or at least the best way?\n\n- Running \"make distclean\" should delete spkg/logs/*.  Here's a patch.",
    "created_at": "2010-04-06T05:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73643",
    "user": "jhpalmieri"
}
```

Two comments: 

- Note that the sage_scripts spkg overwrites the file spkg/install, so a few minutes after you've run "make", that file no longer has the parallel build changes in it.  I assume that this doesn't interfere with the current build (?).  This would be fixed by implementing the changes here and making a source distribution, thereby producing a new sage_scripts spkg.  Is that the only way?  Or at least the best way?

- Running "make distclean" should delete spkg/logs/*.  Here's a patch.



---

archive/issue_comments_073644.json:
```json
{
    "body": "Attachment\n\nnew version of SAGE_ROOT/makefile",
    "created_at": "2010-04-06T05:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73644",
    "user": "jhpalmieri"
}
```

Attachment

new version of SAGE_ROOT/makefile



---

archive/issue_comments_073645.json:
```json
{
    "body": "diff of SAGE_ROOT/makefile",
    "created_at": "2010-04-06T05:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73645",
    "user": "jhpalmieri"
}
```

diff of SAGE_ROOT/makefile



---

archive/issue_comments_073646.json:
```json
{
    "body": "Attachment\n\nscripts repo: add pipestatus to source distribution",
    "created_at": "2010-04-06T21:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73646",
    "user": "jhpalmieri"
}
```

Attachment

scripts repo: add pipestatus to source distribution



---

archive/issue_comments_073647.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-06T22:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73647",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073648.json:
```json
{
    "body": "Attachment\n\nRunning \"sage -sdist\" with these changes doesn't work because pipestatus doesn't get copied over.  The patch \"trac_8306_scripts-pipestatus.patch\" fixes this.\n\nI was able to successfully build this on sage.math, but I had problems on my mac (with two cores, using \"make -j2\").  I think it's with singular; I get lots of lines like\n\n```\nsage/libs/singular/singular.cpp:162:21: error: factory.h: No such file or directory\n```\n\nIt seems to be building singular at the same time as the main Sage spkg; does that sound okay?",
    "created_at": "2010-04-06T22:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73648",
    "user": "jhpalmieri"
}
```

Attachment

Running "sage -sdist" with these changes doesn't work because pipestatus doesn't get copied over.  The patch "trac_8306_scripts-pipestatus.patch" fixes this.

I was able to successfully build this on sage.math, but I had problems on my mac (with two cores, using "make -j2").  I think it's with singular; I get lots of lines like

```
sage/libs/singular/singular.cpp:162:21: error: factory.h: No such file or directory
```

It seems to be building singular at the same time as the main Sage spkg; does that sound okay?



---

archive/issue_comments_073649.json:
```json
{
    "body": "From spkg/logs/singular-3-1-0-4-20100214.log:\n\n```\nmake install in omalloc\ngcc -O3 -g -fPIC -I. -I/Applications/sage_builds/sage-4.3.5.1/local/include  -I/Applications/sage_builds/sage-4.3.5.1/local/include -DHAVE_CONFIG_H -DOM_GENERATE_INC omTables.c -o omTables\n./makeheader om_Alloc.h omalloc.h\nmakeheader: Include file omTables.h not found\nmake[4]: *** [omalloc.h] Error 1\nmake[3]: *** [install] Error 1\nmake[2]: *** [/Applications/sage_builds/sage-4.3.5.1/local/bin/Singular-3-1-0] Error 2\nUnable to build Singular.\n```\n",
    "created_at": "2010-04-06T22:21:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73649",
    "user": "jhpalmieri"
}
```

From spkg/logs/singular-3-1-0-4-20100214.log:

```
make install in omalloc
gcc -O3 -g -fPIC -I. -I/Applications/sage_builds/sage-4.3.5.1/local/include  -I/Applications/sage_builds/sage-4.3.5.1/local/include -DHAVE_CONFIG_H -DOM_GENERATE_INC omTables.c -o omTables
./makeheader om_Alloc.h omalloc.h
makeheader: Include file omTables.h not found
make[4]: *** [omalloc.h] Error 1
make[3]: *** [install] Error 1
make[2]: *** [/Applications/sage_builds/sage-4.3.5.1/local/bin/Singular-3-1-0] Error 2
Unable to build Singular.
```




---

archive/issue_comments_073650.json:
```json
{
    "body": "Typo in deps: \n\n```\n$(SAGE_LOGS)/$(FLINGQS).log\n```\n\nshould say \n\n```\n$(SAGE_LOGS)/$(FLINTQS).log\n                   ^\n```\n",
    "created_at": "2010-04-07T04:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73650",
    "user": "jhpalmieri"
}
```

Typo in deps: 

```
$(SAGE_LOGS)/$(FLINGQS).log
```

should say 

```
$(SAGE_LOGS)/$(FLINTQS).log
                   ^
```




---

archive/issue_comments_073651.json:
```json
{
    "body": "On my iMac, the following packages failed to build with SAGE_CHECK='1':\n\n- iconv (failed because spkg-check failed; this should be fixed by the new iconv spkg at #8638)\n- sagetex (failed because spkg-check failed; this is because spkg-check requires the main Sage library, but Sage is not a prerequisite for sagetex in spkg/standard/deps - ought to be fixable, but I'm not sure what the right prerequisites are: sage, maxima, gap?  Perhaps should be done independently of this ticket?)\n- ecl (failed, but I don't know why -- see the log file [here](http://sage.math.washington.edu/home/palmieri/misc/ecl-10.2.1.log))\n- maxima (failed because ecl failed, although I don't know why the build process didn't just stop when ecl failed)\n- singular (failed, but I don't know why -- see the log file [here](http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-4-20100214.log))\n- sage (failed because singular failed)\n\nFor both singular and ecl, I was able to build them by turning off parallel building just for them (by hand).  Then after turning off SAGE_CHECK, everything else built successfully.",
    "created_at": "2010-04-07T06:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73651",
    "user": "jhpalmieri"
}
```

On my iMac, the following packages failed to build with SAGE_CHECK='1':

- iconv (failed because spkg-check failed; this should be fixed by the new iconv spkg at #8638)
- sagetex (failed because spkg-check failed; this is because spkg-check requires the main Sage library, but Sage is not a prerequisite for sagetex in spkg/standard/deps - ought to be fixable, but I'm not sure what the right prerequisites are: sage, maxima, gap?  Perhaps should be done independently of this ticket?)
- ecl (failed, but I don't know why -- see the log file [here](http://sage.math.washington.edu/home/palmieri/misc/ecl-10.2.1.log))
- maxima (failed because ecl failed, although I don't know why the build process didn't just stop when ecl failed)
- singular (failed, but I don't know why -- see the log file [here](http://sage.math.washington.edu/home/palmieri/misc/singular-3-1-0-4-20100214.log))
- sage (failed because singular failed)

For both singular and ecl, I was able to build them by turning off parallel building just for them (by hand).  Then after turning off SAGE_CHECK, everything else built successfully.



---

archive/issue_comments_073652.json:
```json
{
    "body": "From irc:\n\n```\n<_leif> we don't need \"pipestatus\" either\n<_leif> \"set -o pipefail;\"\n<_leif> that will set the exit status of a pipe to the last non-zero one\n```\n\nSome random web page says that this was introduced in version 3 of bash and doesn't work on the Mac, but it does work on my Mac running OS X 10.6.  I guess this may not work on OS X 10.4, as that seems to have included version 2.",
    "created_at": "2010-04-10T23:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73652",
    "user": "jhpalmieri"
}
```

From irc:

```
<_leif> we don't need "pipestatus" either
<_leif> "set -o pipefail;"
<_leif> that will set the exit status of a pipe to the last non-zero one
```

Some random web page says that this was introduced in version 3 of bash and doesn't work on the Mac, but it does work on my Mac running OS X 10.6.  I guess this may not work on OS X 10.4, as that seems to have included version 2.



---

archive/issue_comments_073653.json:
```json
{
    "body": "Replying to [comment:53 jhpalmieri]:\n> Some random web page says that this was introduced in version 3 of bash and doesn't work on the Mac, but it does work on my Mac running OS X 10.6.  I guess this may not work on OS X 10.4, as that seems to have included version 2.\n\nThe `bash` ChangeLog states it was introduced in version 3.0-alpha.\n\nTo avoid side effects, the setting should be done just for a/the subshell, i.e. replacing\n\n```\n    cmd1 | cmd2 | ... | cmdN | tee logfile\n```\n\nby\n\n```\n    (set -o pipefail; cmd1 | cmd2 | ... | cmdN | tee logfile)\n```\n\n\nSufficiently recent versions of bash should at least be *available* for all OSs currently supported by Sage (including OS X).",
    "created_at": "2010-04-11T00:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73653",
    "user": "leif"
}
```

Replying to [comment:53 jhpalmieri]:
> Some random web page says that this was introduced in version 3 of bash and doesn't work on the Mac, but it does work on my Mac running OS X 10.6.  I guess this may not work on OS X 10.4, as that seems to have included version 2.

The `bash` ChangeLog states it was introduced in version 3.0-alpha.

To avoid side effects, the setting should be done just for a/the subshell, i.e. replacing

```
    cmd1 | cmd2 | ... | cmdN | tee logfile
```

by

```
    (set -o pipefail; cmd1 | cmd2 | ... | cmdN | tee logfile)
```


Sufficiently recent versions of bash should at least be *available* for all OSs currently supported by Sage (including OS X).



---

archive/issue_comments_073654.json:
```json
{
    "body": "Replying to [comment:54 leif]:\n> Sufficiently recent versions of bash should at least be *available* for all OSs currently supported by Sage (including OS X).\n\nRecent versions may be available, but we don't necessarily want to require people to install a newer version of bash just to use Sage.  So (if for example OS X 10.4 is officially supported by Sage) we would have to write a script that tests the version of bash (using `${BASH_VERSINFO[0]`}, I guess), and if less than 3, then do something else.\n\nOr since parallel building is an enhancement, I suppose we could make bash 3 a prerequisite for it.  We would have to write SAGE_ROOT/spkg/standard/deps in a way which works with all versions, though.",
    "created_at": "2010-04-11T01:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73654",
    "user": "jhpalmieri"
}
```

Replying to [comment:54 leif]:
> Sufficiently recent versions of bash should at least be *available* for all OSs currently supported by Sage (including OS X).

Recent versions may be available, but we don't necessarily want to require people to install a newer version of bash just to use Sage.  So (if for example OS X 10.4 is officially supported by Sage) we would have to write a script that tests the version of bash (using `${BASH_VERSINFO[0]`}, I guess), and if less than 3, then do something else.

Or since parallel building is an enhancement, I suppose we could make bash 3 a prerequisite for it.  We would have to write SAGE_ROOT/spkg/standard/deps in a way which works with all versions, though.



---

archive/issue_comments_073655.json:
```json
{
    "body": "Replying to [comment:55 jhpalmieri]:\n> Or since parallel building is an enhancement, I suppose we could make bash 3 a prerequisite for it.  We would have to write SAGE_ROOT/spkg/standard/deps in a way which works with all versions, though.\n\nWell, `bash` 3.0 was released nearly six years ago (and there are pre-built binaries of it available), so I'd say it *should* be OK to make it a prerequisite - it's central and ubiquitous, and I'd call 2.x deprecated.\n\nBut that's only *my* opinion, though in general I'd prefer omitting as much GNUism as possible, trying to stay within POSIX scope (which for example the shell's `trap` mechanism is).\n\n[Sorry, maybe too off-topic.]",
    "created_at": "2010-04-11T05:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73655",
    "user": "leif"
}
```

Replying to [comment:55 jhpalmieri]:
> Or since parallel building is an enhancement, I suppose we could make bash 3 a prerequisite for it.  We would have to write SAGE_ROOT/spkg/standard/deps in a way which works with all versions, though.

Well, `bash` 3.0 was released nearly six years ago (and there are pre-built binaries of it available), so I'd say it *should* be OK to make it a prerequisite - it's central and ubiquitous, and I'd call 2.x deprecated.

But that's only *my* opinion, though in general I'd prefer omitting as much GNUism as possible, trying to stay within POSIX scope (which for example the shell's `trap` mechanism is).

[Sorry, maybe too off-topic.]



---

archive/issue_comments_073656.json:
```json
{
    "body": "I too would rather POSIX was used, and not basisms. The -o option is specified by POSIX\n\nhttp://www.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#set\n\nbut note the comment about \"unspecified format\". If it's possible to avoid that I would, since even bash could change at a later date.",
    "created_at": "2010-04-11T08:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73656",
    "user": "drkirkby"
}
```

I too would rather POSIX was used, and not basisms. The -o option is specified by POSIX

http://www.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#set

but note the comment about "unspecified format". If it's possible to avoid that I would, since even bash could change at a later date.



---

archive/issue_comments_073657.json:
```json
{
    "body": "> note the comment about \"unspecified format\".\n\nI read that comment to be about \"set -o\" with no further options, not about \"set -o OPTION\". \"pipefail\" is documented here, by the way:\n\n http://www.gnu.org/software/bash/manual/bashref.html#The-Set-Builtin\n\nI don't see anything wrong with bashisms, as long as we have #!/usr/bin/env bash at the top of the file. In any case, I'm happy for *any* solution to the pipe situation here: in a command of the form ($1) | ($2), we want the exit code of ($1).\n\nI'm posting experimental versions of pipestatus and deps which test for the bash version and if at least 3, use pipefail.\n\nBy the way, I still can't get singular and ecl to compile on my iMac if SAGE_PARALLEL_SPKG_BUILD is set to \"yes\". Any help with that issue would be appreciated.",
    "created_at": "2010-04-11T15:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73657",
    "user": "jhpalmieri"
}
```

> note the comment about "unspecified format".

I read that comment to be about "set -o" with no further options, not about "set -o OPTION". "pipefail" is documented here, by the way:

 http://www.gnu.org/software/bash/manual/bashref.html#The-Set-Builtin

I don't see anything wrong with bashisms, as long as we have #!/usr/bin/env bash at the top of the file. In any case, I'm happy for *any* solution to the pipe situation here: in a command of the form ($1) | ($2), we want the exit code of ($1).

I'm posting experimental versions of pipestatus and deps which test for the bash version and if at least 3, use pipefail.

By the way, I still can't get singular and ecl to compile on my iMac if SAGE_PARALLEL_SPKG_BUILD is set to "yes". Any help with that issue would be appreciated.



---

archive/issue_comments_073658.json:
```json
{
    "body": "Attachment\n\nversion of pipestatus using pipefail",
    "created_at": "2010-04-11T15:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73658",
    "user": "jhpalmieri"
}
```

Attachment

version of pipestatus using pipefail



---

archive/issue_comments_073659.json:
```json
{
    "body": "Replying to [comment:58 jhpalmieri]:\n> I'm posting experimental versions of pipestatus and deps which test for the bash version and if at least 3, use pipefail.\n\nIt appears that `deps-new` is based on a version of `deps` that predates the [latest] version at\n\n* http://sage.math.washington.edu/home/mpatel/trac/8306/\n\n(last modified on 8 March).  Is there a particular reason for this?  For example, it turns out that we shouldn't use `$(PLUS)`, which can sometimes force an unwanted parallel build within an spkg (i.e., it's better to leave the decision to `spkg-install`).  The 8 March version also fixes [comment:ticket:8306:29 this problem].  But this version still has the `FLINTQS` typo [comment:ticket:8306:51 mentioned above].\n\n> By the way, I still can't get singular and ecl to compile on my iMac if SAGE_PARALLEL_SPKG_BUILD is set to \"yes\". Any help with that issue would be appreciated.\n\nI'll try to investigate soon.",
    "created_at": "2010-06-03T09:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73659",
    "user": "mpatel"
}
```

Replying to [comment:58 jhpalmieri]:
> I'm posting experimental versions of pipestatus and deps which test for the bash version and if at least 3, use pipefail.

It appears that `deps-new` is based on a version of `deps` that predates the [latest] version at

* http://sage.math.washington.edu/home/mpatel/trac/8306/

(last modified on 8 March).  Is there a particular reason for this?  For example, it turns out that we shouldn't use `$(PLUS)`, which can sometimes force an unwanted parallel build within an spkg (i.e., it's better to leave the decision to `spkg-install`).  The 8 March version also fixes [comment:ticket:8306:29 this problem].  But this version still has the `FLINTQS` typo [comment:ticket:8306:51 mentioned above].

> By the way, I still can't get singular and ecl to compile on my iMac if SAGE_PARALLEL_SPKG_BUILD is set to "yes". Any help with that issue would be appreciated.

I'll try to investigate soon.



---

archive/issue_comments_073660.json:
```json
{
    "body": "Allow redirection of stderr and other file descriptors.  Add comp.os.unix FAQ reference.",
    "created_at": "2010-06-08T08:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73660",
    "user": "mpatel"
}
```

Allow redirection of stderr and other file descriptors.  Add comp.os.unix FAQ reference.



---

archive/issue_comments_073661.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:59 mpatel]:\n> > By the way, I still can't get singular and ecl to compile on my iMac if SAGE_PARALLEL_SPKG_BUILD is set to \"yes\". Any help with that issue would be appreciated.\n> \n> I'll try to investigate soon.\n\nI've attached updated versions of `deps`, `install`, and `pipestatus` to accompany the `makefile` and the two `trac_8306_scripts-*` patches.  With these and the forthcoming spkgs at #9185, #9186, and #9187, I can build 4.4.4.alpha0 with SAGE_PARALLEL_SPKG_BUILD=\"yes\"`.",
    "created_at": "2010-06-08T09:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73661",
    "user": "mpatel"
}
```

Attachment

Replying to [comment:59 mpatel]:
> > By the way, I still can't get singular and ecl to compile on my iMac if SAGE_PARALLEL_SPKG_BUILD is set to "yes". Any help with that issue would be appreciated.
> 
> I'll try to investigate soon.

I've attached updated versions of `deps`, `install`, and `pipestatus` to accompany the `makefile` and the two `trac_8306_scripts-*` patches.  With these and the forthcoming spkgs at #9185, #9186, and #9187, I can build 4.4.4.alpha0 with SAGE_PARALLEL_SPKG_BUILD="yes"`.



---

archive/issue_comments_073662.json:
```json
{
    "body": "Replying to [comment:60 mpatel]:\n> I've attached updated versions of `deps`, `install`, and `pipestatus` to accompany the `makefile` and the two `trac_8306_scripts-*` patches.  With these and the forthcoming spkgs at #9185, #9186, and #9187, I can build 4.4.4.alpha0 with SAGE_PARALLEL_SPKG_BUILD=\"yes\"`.\n\nI also need the latest Maxima spkg at #8731.",
    "created_at": "2010-06-09T03:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73662",
    "user": "mpatel"
}
```

Replying to [comment:60 mpatel]:
> I've attached updated versions of `deps`, `install`, and `pipestatus` to accompany the `makefile` and the two `trac_8306_scripts-*` patches.  With these and the forthcoming spkgs at #9185, #9186, and #9187, I can build 4.4.4.alpha0 with SAGE_PARALLEL_SPKG_BUILD="yes"`.

I also need the latest Maxima spkg at #8731.



---

archive/issue_comments_073663.json:
```json
{
    "body": "Rebased for 4.4.4.alpha0.  Replaces previous version.",
    "created_at": "2010-06-09T07:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73663",
    "user": "mpatel"
}
```

Rebased for 4.4.4.alpha0.  Replaces previous version.



---

archive/issue_comments_073664.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-09T09:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73664",
    "user": "mpatel"
}
```

Attachment



---

archive/issue_comments_073665.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-09T09:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73665",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073666.json:
```json
{
    "body": "I'm testing this now: I've applied the patches, put the new spkg's in place, etc., and run \"sage -sdist ...\".  Then I unpacked the new tar file and tried building.  It failed on my mac: I needed to change the line (in \"deps\") from\n\n```\nINSTALL = pipestatus\n```\n\nto\n\n```\nINSTALL = $(SAGE_ROOT)/spkg/pipestatus\n```\n\nAfter making that change, it's building right now.  I'll report on the outcome when it's done.",
    "created_at": "2010-06-09T15:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73666",
    "user": "jhpalmieri"
}
```

I'm testing this now: I've applied the patches, put the new spkg's in place, etc., and run "sage -sdist ...".  Then I unpacked the new tar file and tried building.  It failed on my mac: I needed to change the line (in "deps") from

```
INSTALL = pipestatus
```

to

```
INSTALL = $(SAGE_ROOT)/spkg/pipestatus
```

After making that change, it's building right now.  I'll report on the outcome when it's done.



---

archive/issue_comments_073667.json:
```json
{
    "body": "Things look good.  It's worked successfully on sage.math (took 30 minutes!), a Mac, on the skynet machine \"lena\" (`x86_64-Linux-k10 (with NVIDIA GeForce GPUs)`).  It's still building on t2, although I cheated a bit: I used a build of atlas from a previous Sage install to save myself 11 hours of build time.  It has a chance to finish in 6 or 8 hours instead of the previous time of 17 hours (sans atlas and docs).\n\nI'll report back when the t2 build is done, but once the small change to \"deps\" is made, I think this will be done (modulo #8731, #9185, #9186, and #9187).",
    "created_at": "2010-06-09T21:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73667",
    "user": "jhpalmieri"
}
```

Things look good.  It's worked successfully on sage.math (took 30 minutes!), a Mac, on the skynet machine "lena" (`x86_64-Linux-k10 (with NVIDIA GeForce GPUs)`).  It's still building on t2, although I cheated a bit: I used a build of atlas from a previous Sage install to save myself 11 hours of build time.  It has a chance to finish in 6 or 8 hours instead of the previous time of 17 hours (sans atlas and docs).

I'll report back when the t2 build is done, but once the small change to "deps" is made, I think this will be done (modulo #8731, #9185, #9186, and #9187).



---

archive/issue_comments_073668.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-09T23:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73668",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073669.json:
```json
{
    "body": "The t2 build has completed successfully, in just over 4 hours -- much better than the 17 hours previously required, and even better than the 6 or 8 that I was predicting.  So if you'll fix deps, I'll give this a positive review.",
    "created_at": "2010-06-09T23:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73669",
    "user": "jhpalmieri"
}
```

The t2 build has completed successfully, in just over 4 hours -- much better than the 17 hours previously required, and even better than the 6 or 8 that I was predicting.  So if you'll fix deps, I'll give this a positive review.



---

archive/issue_comments_073670.json:
```json
{
    "body": "I've updated `deps` and `deps.diff`.  Thanks very much to everyone for their help with patches, typos, builds, testing, and other advice!\n\nAdditional data: I've had successful builds on bsd, sage.math, and t2.  The long tests pass, up to those to be fixed at #8731 and a [pre-existing failure](http://groups.google.com/group/sage-devel/browse_thread/thread/26b2aae934131c92/4faf6a32bd792962?q=solaris+bsd.py+group:sage-devel#4faf6a32bd792962) in `BSD.py` on Solaris.  Builds with `SAGE_CHECK` set also succeed, except for R on t2, but this appears to be a separate problem (see a later comment).\n\nShould `$(BASE)` be an (in)direct prerequisite for all non-base packages, including Fortran and Cephes?  So far, I haven't had any problems with these.  Pending reports on sage-devel, we could open a separate ticket about making the dependencies in `deps` more explicit/strict.",
    "created_at": "2010-06-09T23:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73670",
    "user": "mpatel"
}
```

I've updated `deps` and `deps.diff`.  Thanks very much to everyone for their help with patches, typos, builds, testing, and other advice!

Additional data: I've had successful builds on bsd, sage.math, and t2.  The long tests pass, up to those to be fixed at #8731 and a [pre-existing failure](http://groups.google.com/group/sage-devel/browse_thread/thread/26b2aae934131c92/4faf6a32bd792962?q=solaris+bsd.py+group:sage-devel#4faf6a32bd792962) in `BSD.py` on Solaris.  Builds with `SAGE_CHECK` set also succeed, except for R on t2, but this appears to be a separate problem (see a later comment).

Should `$(BASE)` be an (in)direct prerequisite for all non-base packages, including Fortran and Cephes?  So far, I haven't had any problems with these.  Pending reports on sage-devel, we could open a separate ticket about making the dependencies in `deps` more explicit/strict.



---

archive/issue_comments_073671.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-09T23:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73671",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_073672.json:
```json
{
    "body": "From R's `make check` on t2:\n\n```\nCollecting examples for package \u2018stats\u2019\n  Extracting from parsed Rd's ..............................\nRunning examples in package \u2018stats\u2019\nError: testing 'stats' failed\nExecution halted\nmake[5]: *** [test-Examples-Base] Error 1\n```\n\nSome detail from `src/tests/Examples/stats-Ex.Rout.fail`:\n\n```\n> contrasts(ffs) <- contr.sum(5, sparse=TRUE)[,1:2]; contrasts(ffs)\nError in .Diag(levels, sparse = sparse) : \n  contr*(.., sparse=TRUE) needs package \"Matrix\" correctly installed\nCalls: contr.sum -> .Diag\nExecution halted\n```\n\nAccording to [this log](http://sage.math.washington.edu/home/mpatel/trac/8306/r-2.10.1.p2.log), R's Matrix package isn't built/installed successfully on t2:\n\n```\nLoading required package: Matrix\nError in dyn.load(file, DLLpath = DLLpath, ...) : \n  unable to load shared library '/scratch/mpatel/sage-4.4.4.alpha0-j64-par-chk/spkg/build/r-2.10.1.p2/src/library/Matrix/libs/Matrix.so':\n  ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory\nError : require(Matrix, save = FALSE) is not TRUE\n```\n\nAn alternative is to compare the output of `ls SAGE_LOCAL/lib/R/library` on non-#8306 sage.math and t2 builds.  I think we're also missing class, mgcv, nnet, rpart, spatial, and survival on t2.\n\nBut I think this is independent of this ticket --- see, e.g., `/rootpool2/local/kirkby/sage-4.4.3/install.log` on t2.",
    "created_at": "2010-06-10T00:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73672",
    "user": "mpatel"
}
```

From R's `make check` on t2:

```
Collecting examples for package ‘stats’
  Extracting from parsed Rd's ..............................
Running examples in package ‘stats’
Error: testing 'stats' failed
Execution halted
make[5]: *** [test-Examples-Base] Error 1
```

Some detail from `src/tests/Examples/stats-Ex.Rout.fail`:

```
> contrasts(ffs) <- contr.sum(5, sparse=TRUE)[,1:2]; contrasts(ffs)
Error in .Diag(levels, sparse = sparse) : 
  contr*(.., sparse=TRUE) needs package "Matrix" correctly installed
Calls: contr.sum -> .Diag
Execution halted
```

According to [this log](http://sage.math.washington.edu/home/mpatel/trac/8306/r-2.10.1.p2.log), R's Matrix package isn't built/installed successfully on t2:

```
Loading required package: Matrix
Error in dyn.load(file, DLLpath = DLLpath, ...) : 
  unable to load shared library '/scratch/mpatel/sage-4.4.4.alpha0-j64-par-chk/spkg/build/r-2.10.1.p2/src/library/Matrix/libs/Matrix.so':
  ld.so.1: R: fatal: libgcc_s.so.1: open failed: No such file or directory
Error : require(Matrix, save = FALSE) is not TRUE
```

An alternative is to compare the output of `ls SAGE_LOCAL/lib/R/library` on non-#8306 sage.math and t2 builds.  I think we're also missing class, mgcv, nnet, rpart, spatial, and survival on t2.

But I think this is independent of this ticket --- see, e.g., `/rootpool2/local/kirkby/sage-4.4.3/install.log` on t2.



---

archive/issue_comments_073673.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-10T01:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73673",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073674.json:
```json
{
    "body": "I agree that the R issue can go on another ticket.  I'm marking this as positive review.\n\nDepends on #8731, #9185, #9186, and #9187.",
    "created_at": "2010-06-10T01:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73674",
    "user": "jhpalmieri"
}
```

I agree that the R issue can go on another ticket.  I'm marking this as positive review.

Depends on #8731, #9185, #9186, and #9187.



---

archive/issue_comments_073675.json:
```json
{
    "body": "Replying to [comment:68 jhpalmieri]:\n> I agree that the R issue can go on another ticket.\nI've opened #9201 for this problem.",
    "created_at": "2010-06-10T07:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73675",
    "user": "mpatel"
}
```

Replying to [comment:68 jhpalmieri]:
> I agree that the R issue can go on another ticket.
I've opened #9201 for this problem.



---

archive/issue_comments_073676.json:
```json
{
    "body": "Attachment\n\n`spkg/install`.  Rebased for 4.4.4.",
    "created_at": "2010-06-24T07:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73676",
    "user": "mpatel"
}
```

Attachment

`spkg/install`.  Rebased for 4.4.4.



---

archive/issue_comments_073677.json:
```json
{
    "body": "Attachment\n\n`spkg/standard/deps`.  Rebased for 4.4.4.",
    "created_at": "2010-06-24T07:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73677",
    "user": "mpatel"
}
```

Attachment

`spkg/standard/deps`.  Rebased for 4.4.4.



---

archive/issue_comments_073678.json:
```json
{
    "body": "I've updated `deps` and `install` (and diffs) for Sage 4.4.4's removal of GHMM.",
    "created_at": "2010-06-24T07:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73678",
    "user": "mpatel"
}
```

I've updated `deps` and `install` (and diffs) for Sage 4.4.4's removal of GHMM.



---

archive/issue_comments_073679.json:
```json
{
    "body": "Dependencies: #8645, #9185, #9186, #9264.",
    "created_at": "2010-06-24T07:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73679",
    "user": "mpatel"
}
```

Dependencies: #8645, #9185, #9186, #9264.



---

archive/issue_comments_073680.json:
```json
{
    "body": "For what it's worth, I think that your \"diff\" files for deps and install are backwards, showing the diffs from the new version to the old, rather than from the old to the new.\n\nThe deps file is a bit off: first, under the target \"all\", `$(INST)/$(SAGENB)` is listed, but it's not in the \"real\" version of deps.  I think this is good, and I think it's a bug in the version of deps distributed with Sage.  Other targets are missing from \"all\", though:\n\n```\n  $(INST)/$(JINJA)\n  $(INST)/$(JINJA2)\n  $(INST)/$(PYGMENTS)\n  $(INST)/$(SPHINX)\n  $(INST)/$(SQLALCHEMY)\n  $(INST)/$(TWISTED)\n  $(INST)/$(TWISTEDWEB2)\n```\n  \nAlso, the following lines are missing:\n\n```\n$(INST)/$(TWISTEDWEB2): $(INST)/$(TWISTED)\n\t$(INSTALL) \"$(SAGE_SPKG) $(TWISTEDWEB2) 2>&1\" \"tee -a $(SAGE_LOGS)/$(TWISTEDWEB2).log\"\n```\n\nI'm attaching \"deps-new\" and \"deps-new.diff\" to fix this.",
    "created_at": "2010-06-24T20:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73680",
    "user": "jhpalmieri"
}
```

For what it's worth, I think that your "diff" files for deps and install are backwards, showing the diffs from the new version to the old, rather than from the old to the new.

The deps file is a bit off: first, under the target "all", `$(INST)/$(SAGENB)` is listed, but it's not in the "real" version of deps.  I think this is good, and I think it's a bug in the version of deps distributed with Sage.  Other targets are missing from "all", though:

```
  $(INST)/$(JINJA)
  $(INST)/$(JINJA2)
  $(INST)/$(PYGMENTS)
  $(INST)/$(SPHINX)
  $(INST)/$(SQLALCHEMY)
  $(INST)/$(TWISTED)
  $(INST)/$(TWISTEDWEB2)
```
  
Also, the following lines are missing:

```
$(INST)/$(TWISTEDWEB2): $(INST)/$(TWISTED)
	$(INSTALL) "$(SAGE_SPKG) $(TWISTEDWEB2) 2>&1" "tee -a $(SAGE_LOGS)/$(TWISTEDWEB2).log"
```

I'm attaching "deps-new" and "deps-new.diff" to fix this.



---

archive/issue_comments_073681.json:
```json
{
    "body": "Okay, now I'm confused.\n\n```\n  $(INST)/$(TWISTEDWEB2)\n```\n\nWhat is this package?  It's included in the target \"all\", and the current version of deps has lines\n\n```\n$(INST)/$(TWISTEDWEB2): $(INST)/$(TWISTED)\n\t$(SAGE_SPKG) $(TWISTEDWEB2) 2>&1\n```\n\nbut it doesn't look like there's an actual package there.  For instance, there are **no** lines like this in install:\n\n```\nTWISTEDWEB2 =`$newest twistedweb2`\nexport TWISTEDWEB2\n```\n",
    "created_at": "2010-06-24T23:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73681",
    "user": "jhpalmieri"
}
```

Okay, now I'm confused.

```
  $(INST)/$(TWISTEDWEB2)
```

What is this package?  It's included in the target "all", and the current version of deps has lines

```
$(INST)/$(TWISTEDWEB2): $(INST)/$(TWISTED)
	$(SAGE_SPKG) $(TWISTEDWEB2) 2>&1
```

but it doesn't look like there's an actual package there.  For instance, there are **no** lines like this in install:

```
TWISTEDWEB2 =`$newest twistedweb2`
export TWISTEDWEB2
```




---

archive/issue_comments_073682.json:
```json
{
    "body": "I think twistedweb2 used to be a package but is no longer.  I can't find the relevant ticket, but I'm going to remove references to it from deps.  (See also a comment at #9274.)",
    "created_at": "2010-06-25T00:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73682",
    "user": "jhpalmieri"
}
```

I think twistedweb2 used to be a package but is no longer.  I can't find the relevant ticket, but I'm going to remove references to it from deps.  (See also a comment at #9274.)



---

archive/issue_comments_073683.json:
```json
{
    "body": "spkg/standard/deps. Rebased for 4.4.4.",
    "created_at": "2010-06-25T00:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73683",
    "user": "jhpalmieri"
}
```

spkg/standard/deps. Rebased for 4.4.4.



---

archive/issue_comments_073684.json:
```json
{
    "body": "Attachment\n\ndiff between \"deps\" in 4.4.4 and \"deps-new\"",
    "created_at": "2010-06-25T00:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73684",
    "user": "jhpalmieri"
}
```

Attachment

diff between "deps" in 4.4.4 and "deps-new"



---

archive/issue_comments_073685.json:
```json
{
    "body": "Attachment\n\ndiff between mpatel's \"deps\" and \"deps-new\"",
    "created_at": "2010-06-25T00:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73685",
    "user": "jhpalmieri"
}
```

Attachment

diff between mpatel's "deps" and "deps-new"



---

archive/issue_comments_073686.json:
```json
{
    "body": "I tried this again on t2 yesterday.  With `MAKE=\"make -j4\"`, it worked, building Sage (except for Atlas, which I installed by hand) in 4 hours.  For future tickets, we might want to pursue the following: with `MAKE=\"make -j36\"`, the installation failed on the packages `lapack`, `mpir`, `r`, and `sage`.  (After each failure, I switched to \"make -j4\" until the problematic package was built, then switched back to \"j36\".)",
    "created_at": "2010-06-25T15:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73686",
    "user": "jhpalmieri"
}
```

I tried this again on t2 yesterday.  With `MAKE="make -j4"`, it worked, building Sage (except for Atlas, which I installed by hand) in 4 hours.  For future tickets, we might want to pursue the following: with `MAKE="make -j36"`, the installation failed on the packages `lapack`, `mpir`, `r`, and `sage`.  (After each failure, I switched to "make -j4" until the problematic package was built, then switched back to "j36".)



---

archive/issue_comments_073687.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73687",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_073688.json:
```json
{
    "body": "Attachment\n\nDiff of `spkg/standard/deps` vs 4.4.4.",
    "created_at": "2010-06-26T07:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73688",
    "user": "mpatel"
}
```

Attachment

Diff of `spkg/standard/deps` vs 4.4.4.



---

archive/issue_comments_073689.json:
```json
{
    "body": "Diff of `spkg/install` vs 4.4.4.",
    "created_at": "2010-06-26T07:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73689",
    "user": "mpatel"
}
```

Diff of `spkg/install` vs 4.4.4.



---

archive/issue_comments_073690.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:75 jhpalmieri]:\n> I think twistedweb2 used to be a package but is no longer.  I can't find the relevant ticket, but I'm going to remove references to it from deps.  (See also a comment at #9274.)\n\nI mentioned twistedweb2 in an [older version of the description](http://trac.sagemath.org/sage_trac/ticket/8306?action=diff&version=70&old_version=3).\n\nMaybe we should add the missing targets (Sphinx, etc.) at #9274?  It does seem better to be explicit about the dependencies.",
    "created_at": "2010-06-26T08:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8306#issuecomment-73690",
    "user": "mpatel"
}
```

Attachment

Replying to [comment:75 jhpalmieri]:
> I think twistedweb2 used to be a package but is no longer.  I can't find the relevant ticket, but I'm going to remove references to it from deps.  (See also a comment at #9274.)

I mentioned twistedweb2 in an [older version of the description](http://trac.sagemath.org/sage_trac/ticket/8306?action=diff&version=70&old_version=3).

Maybe we should add the missing targets (Sphinx, etc.) at #9274?  It does seem better to be explicit about the dependencies.
