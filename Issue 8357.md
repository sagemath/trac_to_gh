# Issue 8357: eclib: suppress / delete files left by doctests and check, fix building in parallel

archive/issues_008357.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nFrom [John Palmieri](http://groups.google.com/group/sage-devel/browse_thread/thread/976cf8ecb4896e7c):\n\n```\nWhen I run doctests on the file ell_rational_field.py, I end up with a\nsmall file called PRIMES in the current directory. This shouldn't\nhappen: running doctests shouldn't produce files in a non-temporary\ndirectory.\n[...]\n```\n\nThis is a follow-up to #7575.  Please see [comment:ticket:7575:24 comment 24+] for some progress.\n\nA new spkg is available at\n\n* http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.spkg\n\nIt includes the `PRIMES`, `1`, and `make check` fixes mentioned below and parallel build fixes (cf. #8306). \n\n**Note to release manager:** Merge only the spkg.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8357\n\n",
    "closed_at": "2010-03-07T00:23:05Z",
    "created_at": "2010-02-25T06:05:03Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "eclib: suppress / delete files left by doctests and check, fix building in parallel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8357",
    "user": "https://github.com/qed777"
}
```
Assignee: @JohnCremona

From [John Palmieri](http://groups.google.com/group/sage-devel/browse_thread/thread/976cf8ecb4896e7c):

```
When I run doctests on the file ell_rational_field.py, I end up with a
small file called PRIMES in the current directory. This shouldn't
happen: running doctests shouldn't produce files in a non-temporary
directory.
[...]
```

This is a follow-up to #7575.  Please see [comment:ticket:7575:24 comment 24+] for some progress.

A new spkg is available at

* http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.spkg

It includes the `PRIMES`, `1`, and `make check` fixes mentioned below and parallel build fixes (cf. #8306). 

**Note to release manager:** Merge only the spkg.

Issue created by migration from https://trac.sagemath.org/ticket/8357





---

archive/issue_comments_074527.json:
```json
{
    "body": "The quickest quick fix would be just to comment out line 372 in src/procs/marith.cc (in eclib).\n\nAnything else requires thought and testing, which I don't have time for i nthe next several days.",
    "created_at": "2010-02-25T09:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74527",
    "user": "https://github.com/JohnCremona"
}
```

The quickest quick fix would be just to comment out line 372 in src/procs/marith.cc (in eclib).

Anything else requires thought and testing, which I don't have time for i nthe next several days.



---

archive/issue_events_020029.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-28T00:24:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "milestone": "sage-4.3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8357#event-20029"
}
```



---

archive/issue_comments_074528.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-28T00:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74528",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074529.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-28T06:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74529",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074530.json:
```json
{
    "body": "There's still a timing(?) problem ([log](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.log)).",
    "created_at": "2010-02-28T06:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74530",
    "user": "https://github.com/qed777"
}
```

There's still a timing(?) problem ([log](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.log)).



---

archive/issue_comments_074531.json:
```json
{
    "body": "Attachment [trac_8357-eclib_makefiles.patch](tarball://root/attachments/some-uuid/ticket8357/trac_8357-eclib_makefiles.patch) by @qed777 created at 2010-02-28 13:29:51\n\nTweak `MAKEFILE`s for parallel builds.  eclib src repo.",
    "created_at": "2010-02-28T13:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74531",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8357-eclib_makefiles.patch](tarball://root/attachments/some-uuid/ticket8357/trac_8357-eclib_makefiles.patch) by @qed777 created at 2010-02-28 13:29:51

Tweak `MAKEFILE`s for parallel builds.  eclib src repo.



---

archive/issue_comments_074532.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n\n> There's still a timing(?) problem ([log](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.log)).\n\n\nI think the problem is that make sometimes attempts to build a target in `progs` before it's done building a requisite shared library, e.g., `install_so`.  I've updated the \"makefiles\" patch and spkg with a fix that I'm testing now.",
    "created_at": "2010-02-28T13:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74532",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:3 mpatel]:

> There's still a timing(?) problem ([log](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.log)).


I think the problem is that make sometimes attempts to build a target in `progs` before it's done building a requisite shared library, e.g., `install_so`.  I've updated the "makefiles" patch and spkg with a fix that I'm testing now.



---

archive/issue_comments_074533.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Replying to [comment:3 mpatel]:\n> \n> > There's still a timing(?) problem ([log](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.log)).\n\n> \n> I think the problem is that make sometimes attempts to build a target in `progs` before it's done building a requisite shared library, e.g., `install_so`.  I've updated the \"makefiles\" patch and spkg with a fix that I'm testing now.\n\n\nThat sounds likely.  We (I) should probably tidy this up;  there are several useful executables which are built, but the only one actually used by and accessible from Sage after the build is mwrank.  So i should change the targets so that the other progs are only built when doing a make check.",
    "created_at": "2010-02-28T13:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74533",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:4 mpatel]:
> Replying to [comment:3 mpatel]:
> 
> > There's still a timing(?) problem ([log](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.log)).

> 
> I think the problem is that make sometimes attempts to build a target in `progs` before it's done building a requisite shared library, e.g., `install_so`.  I've updated the "makefiles" patch and spkg with a fix that I'm testing now.


That sounds likely.  We (I) should probably tidy this up;  there are several useful executables which are built, but the only one actually used by and accessible from Sage after the build is mwrank.  So i should change the targets so that the other progs are only built when doing a make check.



---

archive/issue_comments_074534.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> [...] I've updated the \"makefiles\" patch and spkg with a fix that I'm testing now.\n\nIt seems to work and it survives a stress test on sage.math, e.g.,\n\n```sh\nexport MAKE=\"make -j20\"  # And NTL_PREFIX, etc.\nmake veryclean && make && make so && make veryclean && make && make so && [lots of reps] && ls\n```",
    "created_at": "2010-02-28T14:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74534",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:4 mpatel]:
> [...] I've updated the "makefiles" patch and spkg with a fix that I'm testing now.

It seems to work and it survives a stress test on sage.math, e.g.,

```sh
export MAKE="make -j20"  # And NTL_PREFIX, etc.
make veryclean && make && make so && make veryclean && make && make so && [lots of reps] && ls
```



---

archive/issue_comments_074535.json:
```json
{
    "body": "mpatel:  if possible could you make he following additional edits to src/procs/Makefile (in eclib...p10):\n\n```\ndiff -r 809e34b4c146 procs/Makefile\n--- a/procs/Makefile\tSat Feb 27 15:42:31 2010 -0800\n+++ b/procs/Makefile\tSun Feb 28 20:08:44 2010 +0000\n@@ -105,7 +105,7 @@\n \tgzip procs.tar\n \n check: $(TESTS)\n-\trm -f PRIMES t\n+\trm -f PRIMES t 1\n \t./vectest1 < vectest.in >  t && diff t vectest.out\n \t./vectest2 < vectest.in >  t && diff t vectest.out\n \t./mattest1 < mattest.in >  t && diff t mattest.out\n@@ -128,7 +128,7 @@\n \t./rcubic < rcubic.in > t && diff t rcubic.out\n \t./lcubic < lcubic.in > t && diff t lcubic.out\n \t./tp2points < tp2points.in > t && diff t tp2points.out\n-\trm -f PRIMES t\n+\trm -f PRIMES t 1\n```\nIt's another temp file which gets left behind, this time after \"make check\".\n\nIf that's too much hassle I'll do it next time I make changes to the eclib spkg, but it would be convenient to do it now.",
    "created_at": "2010-02-28T20:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74535",
    "user": "https://github.com/JohnCremona"
}
```

mpatel:  if possible could you make he following additional edits to src/procs/Makefile (in eclib...p10):

```
diff -r 809e34b4c146 procs/Makefile
--- a/procs/Makefile	Sat Feb 27 15:42:31 2010 -0800
+++ b/procs/Makefile	Sun Feb 28 20:08:44 2010 +0000
@@ -105,7 +105,7 @@
 	gzip procs.tar
 
 check: $(TESTS)
-	rm -f PRIMES t
+	rm -f PRIMES t 1
 	./vectest1 < vectest.in >  t && diff t vectest.out
 	./vectest2 < vectest.in >  t && diff t vectest.out
 	./mattest1 < mattest.in >  t && diff t mattest.out
@@ -128,7 +128,7 @@
 	./rcubic < rcubic.in > t && diff t rcubic.out
 	./lcubic < lcubic.in > t && diff t lcubic.out
 	./tp2points < tp2points.in > t && diff t tp2points.out
-	rm -f PRIMES t
+	rm -f PRIMES t 1
```
It's another temp file which gets left behind, this time after "make check".

If that's too much hassle I'll do it next time I make changes to the eclib spkg, but it would be convenient to do it now.



---

archive/issue_comments_074536.json:
```json
{
    "body": "Diff of `spkg-install`, `SPKG.txt`.  eclib spkg repo.",
    "created_at": "2010-03-01T00:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74536",
    "user": "https://github.com/qed777"
}
```

Diff of `spkg-install`, `SPKG.txt`.  eclib spkg repo.



---

archive/issue_comments_074537.json:
```json
{
    "body": "Attachment [trac_8357-suppress_PRIMES.patch](tarball://root/attachments/some-uuid/ticket8357/trac_8357-suppress_PRIMES.patch) by @qed777 created at 2010-03-01 00:18:24\n\nDon't write `PRIMES`. Delete `1` after check.  eclib src repo",
    "created_at": "2010-03-01T00:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74537",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8357-suppress_PRIMES.patch](tarball://root/attachments/some-uuid/ticket8357/trac_8357-suppress_PRIMES.patch) by @qed777 created at 2010-03-01 00:18:24

Don't write `PRIMES`. Delete `1` after check.  eclib src repo



---

archive/issue_comments_074538.json:
```json
{
    "body": "Replying to [comment:7 cremona]:\n> If that's too much hassle I'll do it next time I make changes to the eclib spkg, but it would be convenient to do it now.\n\nDone!  I've updated spkg and two patches.",
    "created_at": "2010-03-01T00:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74538",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:7 cremona]:
> If that's too much hassle I'll do it next time I make changes to the eclib spkg, but it would be convenient to do it now.

Done!  I've updated spkg and two patches.



---

archive/issue_comments_074539.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-01T00:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74539",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074540.json:
```json
{
    "body": "I noticed a different problem with `make check` on t2:\n\n```\nmake[3]: Entering directory `/scratch/mpatel/sage-4.3.0.1/spkg/build/eclib-20080310.p10/src/g0n'\nrm -f PRIMES t\n./modtest < modtest.in > t 2>/dev/null && diff t modtest.out \n./homtest < homtest.in > t && diff t homtest.out\n./hecketest < hecketest.in > t 2>/dev/null && diff t hecketest.out \n./mhcount < mhcount.in > t && diff t  mhcount.out\nrm -rf tmp_nf_dir\nmkdir tmp_nf_dir\nexport NF_DIR=tmp_nf_dir && ./tmanin < tmanin.in > t 2>/dev/null && diff t tmanin.out\n/bin/sh: NF_DIR=tmp_nf_dir: is not an identifier\nmake[3]: *** [check] Error 1\nmake[3]: Leaving directory `/scratch/mpatel/sage-4.3.0.1/spkg/build/eclib-20080310.p10/src/g0n'\n```\nI think we can fix this with, e.g.,\n\n```sh\nenv NF_DIR=tmp_nf_dir ./tmanin < tmanin.in > t 2>/dev/null && diff t tmanin.out\n```",
    "created_at": "2010-03-01T04:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74540",
    "user": "https://github.com/qed777"
}
```

I noticed a different problem with `make check` on t2:

```
make[3]: Entering directory `/scratch/mpatel/sage-4.3.0.1/spkg/build/eclib-20080310.p10/src/g0n'
rm -f PRIMES t
./modtest < modtest.in > t 2>/dev/null && diff t modtest.out 
./homtest < homtest.in > t && diff t homtest.out
./hecketest < hecketest.in > t 2>/dev/null && diff t hecketest.out 
./mhcount < mhcount.in > t && diff t  mhcount.out
rm -rf tmp_nf_dir
mkdir tmp_nf_dir
export NF_DIR=tmp_nf_dir && ./tmanin < tmanin.in > t 2>/dev/null && diff t tmanin.out
/bin/sh: NF_DIR=tmp_nf_dir: is not an identifier
make[3]: *** [check] Error 1
make[3]: Leaving directory `/scratch/mpatel/sage-4.3.0.1/spkg/build/eclib-20080310.p10/src/g0n'
```
I think we can fix this with, e.g.,

```sh
env NF_DIR=tmp_nf_dir ./tmanin < tmanin.in > t 2>/dev/null && diff t tmanin.out
```



---

archive/issue_comments_074541.json:
```json
{
    "body": "I tested the current version of the spkg.  (This does nto have the suggested changes to the handling of NF_DIR).  All was well.\n\nI did not make new changes (for the NF_DIR thing) since I thought that would be too confusing.  But I'll be happy to check the next version of p10 in due course.",
    "created_at": "2010-03-01T14:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74541",
    "user": "https://github.com/JohnCremona"
}
```

I tested the current version of the spkg.  (This does nto have the suggested changes to the handling of NF_DIR).  All was well.

I did not make new changes (for the NF_DIR thing) since I thought that would be too confusing.  But I'll be happy to check the next version of p10 in due course.



---

archive/issue_comments_074542.json:
```json
{
    "body": "There is a  simpler solution to the problem with \"export NF_DIR\".  The code uses a default directory name for this, namely \"newforms\",  which can be over-ridden by the use of the environment variable NF_DIR.  For this test therefore we can replace the 2 lines \"rm -rf tmp_nf_dir\" by \"rm -rf newforms\" (strictly only the second one is needed) and remove all the starts of lines of the form \"export NF_DIR=tmp_nf_dir && \".\n(This is in src/g0n/Makefile).\n\nHere's why I did not do this in the first place: by own private copy of this code has a newforms directory which contains 3.4G of data which took many many processor-years to compute.  I do not want a simple \"make check\" to delete that so I put in this temporary (and non-default) tmp_nf_dir thing instead.  But for the Sage distribution that is not needed.\n\nI can attach a replacement Makefile here if that would be convenient, for yet another version of p10.",
    "created_at": "2010-03-01T19:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74542",
    "user": "https://github.com/JohnCremona"
}
```

There is a  simpler solution to the problem with "export NF_DIR".  The code uses a default directory name for this, namely "newforms",  which can be over-ridden by the use of the environment variable NF_DIR.  For this test therefore we can replace the 2 lines "rm -rf tmp_nf_dir" by "rm -rf newforms" (strictly only the second one is needed) and remove all the starts of lines of the form "export NF_DIR=tmp_nf_dir && ".
(This is in src/g0n/Makefile).

Here's why I did not do this in the first place: by own private copy of this code has a newforms directory which contains 3.4G of data which took many many processor-years to compute.  I do not want a simple "make check" to delete that so I put in this temporary (and non-default) tmp_nf_dir thing instead.  But for the Sage distribution that is not needed.

I can attach a replacement Makefile here if that would be convenient, for yet another version of p10.



---

archive/issue_comments_074543.json:
```json
{
    "body": "Sure, that sounds good.",
    "created_at": "2010-03-01T21:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74543",
    "user": "https://github.com/qed777"
}
```

Sure, that sounds good.



---

archive/issue_comments_074544.json:
```json
{
    "body": "replacement src/g0n/Makefile",
    "created_at": "2010-03-01T22:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74544",
    "user": "https://github.com/JohnCremona"
}
```

replacement src/g0n/Makefile



---

archive/issue_comments_074545.json:
```json
{
    "body": "Attachment [Makefile](tarball://root/attachments/some-uuid/ticket8357/Makefile) by @JohnCremona created at 2010-03-01 22:04:17\n\nReplying to [comment:12 mpatel]:\n> Sure, that sounds good.\n\nI have attached the replacement Makefile -- could you update the spkg with it?",
    "created_at": "2010-03-01T22:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74545",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [Makefile](tarball://root/attachments/some-uuid/ticket8357/Makefile) by @JohnCremona created at 2010-03-01 22:04:17

Replying to [comment:12 mpatel]:
> Sure, that sounds good.

I have attached the replacement Makefile -- could you update the spkg with it?



---

archive/issue_comments_074546.json:
```json
{
    "body": "Done!  The package now builds in parallel and `make check` now works for me on t2 and sage.math.",
    "created_at": "2010-03-02T22:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74546",
    "user": "https://github.com/qed777"
}
```

Done!  The package now builds in parallel and `make check` now works for me on t2 and sage.math.



---

archive/issue_comments_074547.json:
```json
{
    "body": "Attachment [trac_8357-newforms_dir.patch](tarball://root/attachments/some-uuid/ticket8357/trac_8357-newforms_dir.patch) by @qed777 created at 2010-03-02 22:34:35\n\nSimplify `g0n/Makefile`.  eclib src repo.",
    "created_at": "2010-03-02T22:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74547",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8357-newforms_dir.patch](tarball://root/attachments/some-uuid/ticket8357/trac_8357-newforms_dir.patch) by @qed777 created at 2010-03-02 22:34:35

Simplify `g0n/Makefile`.  eclib src repo.



---

archive/issue_comments_074548.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T23:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74548",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074549.json:
```json
{
    "body": "The updated eclib package [eclib-20080310.p10.spkg](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.spkg) looks good. It solves the unexpected annoyance introduced by #7575.",
    "created_at": "2010-03-06T23:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74549",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The updated eclib package [eclib-20080310.p10.spkg](http://sage.math.washington.edu/home/mpatel/trac/8357/eclib-20080310.p10.spkg) looks good. It solves the unexpected annoyance introduced by #7575.



---

archive/issue_events_020030.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-07T00:23:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8357#event-20030"
}
```



---

archive/issue_comments_074550.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-07T00:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8357#issuecomment-74550",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
