# Issue 9875: Building PARI/GP with SAGE_CHECK=yes fails on rnfkummer on a PPC Mac OS X 10.4

archive/issues_009875.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  drkirkby mpatel georgsweber\n\n**This is an upstream problem with PARI/GP**\n\nOn one PPC Mac OS X 10.4 machine, the \"rnfkummer\" test in PARI's `make test-all` always fails.\n\nFor example, with this version:\n\n```\nGP/PARI CALCULATOR Version 2.4.3 (development svn-12594)\nPowerPC running darwin (PPC/GMP-5.0.1 kernel) 32-bit version\ncompiled: Sep  8 2010, gcc-4.5.1 (GCC)\n(readline v5.0 enabled, extended help enabled)\n```\n\n\nI get a failure in rnfkummer (both sta and dyn), I am attaching the dif and the output of Configure.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9876\n\n",
    "created_at": "2010-09-08T18:58:52Z",
    "labels": [
        "packages: standard",
        "critical",
        "bug"
    ],
    "title": "Building PARI/GP with SAGE_CHECK=yes fails on rnfkummer on a PPC Mac OS X 10.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9875",
    "user": "jdemeyer"
}
```
Assignee: tbd

CC:  drkirkby mpatel georgsweber

**This is an upstream problem with PARI/GP**

On one PPC Mac OS X 10.4 machine, the "rnfkummer" test in PARI's `make test-all` always fails.

For example, with this version:

```
GP/PARI CALCULATOR Version 2.4.3 (development svn-12594)
PowerPC running darwin (PPC/GMP-5.0.1 kernel) 32-bit version
compiled: Sep  8 2010, gcc-4.5.1 (GCC)
(readline v5.0 enabled, extended help enabled)
```


I get a failure in rnfkummer (both sta and dyn), I am attaching the dif and the output of Configure.

Issue created by migration from https://trac.sagemath.org/ticket/9876





---

archive/issue_comments_097710.json:
```json
{
    "body": "output of Configure",
    "created_at": "2010-09-08T18:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97710",
    "user": "jdemeyer"
}
```

output of Configure



---

archive/issue_comments_097711.json:
```json
{
    "body": "Attachment\n\ndiff from `make test-all`",
    "created_at": "2010-09-08T18:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97711",
    "user": "jdemeyer"
}
```

Attachment

diff from `make test-all`



---

archive/issue_comments_097712.json:
```json
{
    "body": "I get the same error on t2.math.washington.edu (Solaris on sparc).",
    "created_at": "2010-09-08T19:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97712",
    "user": "jhpalmieri"
}
```

I get the same error on t2.math.washington.edu (Solaris on sparc).



---

archive/issue_comments_097713.json:
```json
{
    "body": "So what does a Solaris sparc have in common with a PPC OS X which other systems do not have???",
    "created_at": "2010-09-08T19:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97713",
    "user": "jdemeyer"
}
```

So what does a Solaris sparc have in common with a PPC OS X which other systems do not have???



---

archive/issue_comments_097714.json:
```json
{
    "body": "I've put the build directory from t2 at `/home/palmieri/t2/pari-2.4.3.svn-12577.p5` in case any of the files there are helpful.  (Note that the /home directories are the same on t2 as on sage.math, so you can access this directory from sage.math.)",
    "created_at": "2010-09-08T20:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97714",
    "user": "jhpalmieri"
}
```

I've put the build directory from t2 at `/home/palmieri/t2/pari-2.4.3.svn-12577.p5` in case any of the files there are helpful.  (Note that the /home directories are the same on t2 as on sage.math, so you can access this directory from sage.math.)



---

archive/issue_comments_097715.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> I've put the build directory from t2 at `/home/palmieri/t2/pari-2.4.3.svn-12577.p5` in case any of the files there are helpful.  (Note that the /home directories are the same on t2 as on sage.math, so you can access this directory from sage.math.)\n\nPlease do `chmod 755 /home/palmieri/t2/pari-2.4.3.svn-12577.p5` and then I can actually access it.",
    "created_at": "2010-09-08T20:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97715",
    "user": "jdemeyer"
}
```

Replying to [comment:5 jhpalmieri]:
> I've put the build directory from t2 at `/home/palmieri/t2/pari-2.4.3.svn-12577.p5` in case any of the files there are helpful.  (Note that the /home directories are the same on t2 as on sage.math, so you can access this directory from sage.math.)

Please do `chmod 755 /home/palmieri/t2/pari-2.4.3.svn-12577.p5` and then I can actually access it.



---

archive/issue_comments_097716.json:
```json
{
    "body": "Thanks!  For reference, the PARI/GP build directory on t2 (a Solaris sparc) can be found on:\n[http://sage.math.washington.edu/home/palmieri/t2/pari-2.4.3.svn-12577.p5/src/](http://sage.math.washington.edu/home/palmieri/t2/pari-2.4.3.svn-12577.p5/src/)",
    "created_at": "2010-09-08T20:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97716",
    "user": "jdemeyer"
}
```

Thanks!  For reference, the PARI/GP build directory on t2 (a Solaris sparc) can be found on:
[http://sage.math.washington.edu/home/palmieri/t2/pari-2.4.3.svn-12577.p5/src/](http://sage.math.washington.edu/home/palmieri/t2/pari-2.4.3.svn-12577.p5/src/)



---

archive/issue_comments_097717.json:
```json
{
    "body": "Replying to [comment:4 jdemeyer]:\n> So what does a Solaris sparc have in common with a PPC OS X which other systems do not have???\n\n32-bit big endian machines?",
    "created_at": "2010-09-08T20:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97717",
    "user": "jdemeyer"
}
```

Replying to [comment:4 jdemeyer]:
> So what does a Solaris sparc have in common with a PPC OS X which other systems do not have???

32-bit big endian machines?



---

archive/issue_comments_097718.json:
```json
{
    "body": "I also get the same error on the skynet machine mark (a *very* slow sparc machine running solaris).  I didn't the problem with fulvia (x86 running solaris).",
    "created_at": "2010-09-09T04:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97718",
    "user": "jhpalmieri"
}
```

I also get the same error on the skynet machine mark (a *very* slow sparc machine running solaris).  I didn't the problem with fulvia (x86 running solaris).



---

archive/issue_comments_097719.json:
```json
{
    "body": "Replying to [comment:8 jdemeyer]:\n> Replying to [comment:4 jdemeyer]:\n> > So what does a Solaris sparc have in common with a PPC OS X which other systems do not have???\n> \n> 32-bit big endian machines?\n\nAll modern SPARC systems are 64-bit. The Sun Ultra 1, which was the first 64-bit machine from Sun, was bought out in 1995 - i.e. 15 years ago, well before any Intel or AMD chip was 64-bit. \n\nHowever, to maintain backward compatibility, and to increase performance, Sun chose to retain the default builds as 32-bit. So are in fact building Sage 32-bit on Solaris, though a 64-bit build is possible. \n\nThe fact John said the tests fail on 'mark' but pass on 'fulvia' does indicate it's very likely to be a big-endian issue. I have a machine running HP-UX which uses a PA-RISC processor. That is big-endian. I could try building Pari on there, though I'm not sure if it will work or not. I'd not be surprised if it failed to build on there. \n\nDave",
    "created_at": "2010-09-09T09:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97719",
    "user": "drkirkby"
}
```

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

archive/issue_comments_097720.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n> All modern SPARC systems are 64-bit. The Sun Ultra 1, which was the first 64-bit machine from Sun, was bought out in 1995 - i.e. 15 years ago, well before any Intel or AMD chip was 64-bit.\n\ni860? That were the days of SPARC V7... ;-)",
    "created_at": "2010-09-09T15:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97720",
    "user": "leif"
}
```

Replying to [comment:11 drkirkby]:
> All modern SPARC systems are 64-bit. The Sun Ultra 1, which was the first 64-bit machine from Sun, was bought out in 1995 - i.e. 15 years ago, well before any Intel or AMD chip was 64-bit.

i860? That were the days of SPARC V7... ;-)



---

archive/issue_comments_097721.json:
```json
{
    "body": "Attachment\n\nAdds doctest to catch this error in the future",
    "created_at": "2010-09-10T19:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97721",
    "user": "jdemeyer"
}
```

Attachment

Adds doctest to catch this error in the future



---

archive/issue_comments_097722.json:
```json
{
    "body": "Fix (spkg + doctest) tested on\n* 64-bit Intel Linux\n* 32-bit Intel Linux\n* 32-bit PPC OS X",
    "created_at": "2010-09-11T06:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97722",
    "user": "jdemeyer"
}
```

Fix (spkg + doctest) tested on
* 64-bit Intel Linux
* 32-bit Intel Linux
* 32-bit PPC OS X



---

archive/issue_comments_097723.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-11T06:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97723",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097724.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-09-11T07:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97724",
    "user": "leif"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_097725.json:
```json
{
    "body": "Assuming Mitesh is ok with that.",
    "created_at": "2010-09-11T07:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97725",
    "user": "leif"
}
```

Assuming Mitesh is ok with that.



---

archive/issue_comments_097726.json:
```json
{
    "body": "P.S.: Tell Mercurial some patches have been removed...",
    "created_at": "2010-09-11T07:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97726",
    "user": "leif"
}
```

P.S.: Tell Mercurial some patches have been removed...



---

archive/issue_comments_097727.json:
```json
{
    "body": "Can someone test the new spkg on MacOS X 10.**4** **Intel**? (The upstream fix only adds `-fno-common` on PPCs, not *Tiger* in general, which is afaik wrong.)",
    "created_at": "2010-09-11T08:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97727",
    "user": "leif"
}
```

Can someone test the new spkg on MacOS X 10.**4** **Intel**? (The upstream fix only adds `-fno-common` on PPCs, not *Tiger* in general, which is afaik wrong.)



---

archive/issue_comments_097728.json:
```json
{
    "body": "Last comment refers to\n\n```\n### pari-2.4.3.svn-12577.p6 (Jeroen Demeyer, September 10th, 2010)\n * Add upstream fix for config/get_dlcflags and remove the patch\n```\n\nwhich is\n\n```diff\n$ diff -Nau pari-2.4.3.svn-12577.p5/src/config/get_dlcflags pari-2.4.3.svn-12577.p6/src/config/get_dlcflags \n--- pari-2.4.3.svn-12577.p5/src/config/get_dlcflags\t2010-09-06 21:26:42.000000000 +0200\n+++ pari-2.4.3.svn-12577.p6/src/config/get_dlcflags\t2010-09-10 23:29:12.000000000 +0200\n@@ -2,6 +2,10 @@\n if test -n \"$__gnuc__\"; then\n   case $osname in\n     cygwin|mingw) DLCFLAGS=;;\n+    darwin) DLCFLAGS=-fPIC\n+      case $arch in\n+        ppc|ppc64) DLCFLAGS=\"$DLCFLAGS -fno-common\"\n+      esac;;\n     *) DLCFLAGS=-fPIC;;\n   esac\n else #assume native compiler\n```\n",
    "created_at": "2010-09-11T08:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97728",
    "user": "leif"
}
```

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
@@ -2,6 +2,10 @@
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

archive/issue_comments_097729.json:
```json
{
    "body": "Jeroen, could you also extend the message printed when `SAGE_TUNE_PARI=yes` to strongly recommend running PARI's test suite after tuning? (We could in principle do that automatically from `spkg-install` as well, but that's IMHO not a good idea since it then might get run twice, and also doing so wouldn't fit Sage's build/test process.)\n\nAs mentioned somewhere else (#9343?), one of PARI's self-tests fails *after \"successful\" tuning* on a Pentium 4 Prescott running Ubuntu 9.04 (gcc 4.3.3). I've yet only put a comment on the wiki page; will open a ticket for that later.\n\n----\n\nI'd prefer prepending `./` to `Configure`, since this will give an *appropriate* error message in any case where `src/Configure` does (for whatever reason) not exist. (Otherwise `bash` would then attempt to find it in `$PATH`, which might cause weird behavoir.)\n\n----\n\nWhile adding `-fno-common` on MacOS X 10.5 and 10.6, too, is perhaps a bit odd, it doesn't hurt; otherwise one should look for *Darwin 8* (10.4) with `uname ...`. (I currently don't know the exact string; the relevant part should be the same on PPC 10.4.).",
    "created_at": "2010-09-11T10:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97729",
    "user": "leif"
}
```

Jeroen, could you also extend the message printed when `SAGE_TUNE_PARI=yes` to strongly recommend running PARI's test suite after tuning? (We could in principle do that automatically from `spkg-install` as well, but that's IMHO not a good idea since it then might get run twice, and also doing so wouldn't fit Sage's build/test process.)

As mentioned somewhere else (#9343?), one of PARI's self-tests fails *after "successful" tuning* on a Pentium 4 Prescott running Ubuntu 9.04 (gcc 4.3.3). I've yet only put a comment on the wiki page; will open a ticket for that later.

----

I'd prefer prepending `./` to `Configure`, since this will give an *appropriate* error message in any case where `src/Configure` does (for whatever reason) not exist. (Otherwise `bash` would then attempt to find it in `$PATH`, which might cause weird behavoir.)

----

While adding `-fno-common` on MacOS X 10.5 and 10.6, too, is perhaps a bit odd, it doesn't hurt; otherwise one should look for *Darwin 8* (10.4) with `uname ...`. (I currently don't know the exact string; the relevant part should be the same on PPC 10.4.).



---

archive/issue_comments_097730.json:
```json
{
    "body": "Replying to [comment:19 leif]:\n> [...] otherwise one should look for *Darwin 8* (10.4) with `uname ...`. (I currently don't know the exact string; the relevant part should be the same on PPC 10.4.).\n\n``uname -r`` should start with `8` for MacOS X 10.4 / Tiger / Darwin 8.",
    "created_at": "2010-09-11T12:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97730",
    "user": "leif"
}
```

Replying to [comment:19 leif]:
> [...] otherwise one should look for *Darwin 8* (10.4) with `uname ...`. (I currently don't know the exact string; the relevant part should be the same on PPC 10.4.).

``uname -r`` should start with `8` for MacOS X 10.4 / Tiger / Darwin 8.



---

archive/issue_comments_097731.json:
```json
{
    "body": "Replying to [comment:17 leif]:\n> Can someone test the new spkg on MacOS X 10.**4** **Intel**? (The upstream fix only adds `-fno-common` on PPCs, not *Tiger* in general, which is afaik wrong.)\n\nI agree this certainly needs to be tested.",
    "created_at": "2010-09-11T12:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97731",
    "user": "jdemeyer"
}
```

Replying to [comment:17 leif]:
> Can someone test the new spkg on MacOS X 10.**4** **Intel**? (The upstream fix only adds `-fno-common` on PPCs, not *Tiger* in general, which is afaik wrong.)

I agree this certainly needs to be tested.



---

archive/issue_comments_097732.json:
```json
{
    "body": "patch for the PARI spkg with upstream fix and some cleanup",
    "created_at": "2010-09-11T13:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97732",
    "user": "jdemeyer"
}
```

patch for the PARI spkg with upstream fix and some cleanup



---

archive/issue_comments_097733.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:19 leif]:\n> Jeroen, could you also extend the message printed when `SAGE_TUNE_PARI=yes` to strongly recommend running PARI's test suite after tuning?\n> \n> ----\n> \n> I'd prefer prepending `./` to `Configure`, since this will give an *appropriate* error message in any case where `src/Configure` does (for whatever reason) not exist.\n\nDone. New spkg, same place: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p6.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p6.spkg)",
    "created_at": "2010-09-11T13:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97733",
    "user": "jdemeyer"
}
```

Attachment

Replying to [comment:19 leif]:
> Jeroen, could you also extend the message printed when `SAGE_TUNE_PARI=yes` to strongly recommend running PARI's test suite after tuning?
> 
> ----
> 
> I'd prefer prepending `./` to `Configure`, since this will give an *appropriate* error message in any case where `src/Configure` does (for whatever reason) not exist.

Done. New spkg, same place: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p6.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p6.spkg)



---

archive/issue_comments_097734.json:
```json
{
    "body": "Replying to [comment:21 jdemeyer]:\n> Replying to [comment:17 leif]:\n> > Can someone test the new spkg on MacOS X 10.**4** **Intel**? (The upstream fix only adds `-fno-common` on PPCs, not *Tiger* in general, which is afaik wrong.)\n> \n> I agree this certainly needs to be tested.\n\nWell, the incapability of 10.4's linker / loader to handle common symbols in conjunction with dynamic libraries is completely unrelated to the processor architecture; I doubt the one used on Intel processors in 10.4 will differ much from the one on PowerPCs. (PPC may imply Darwin 8, but not the other way around.)\n\nSo I'd prefer keeping *our* patch (which is already well-tested), or modify it to add a distinction on the Darwin release (``uname -r``, see above).",
    "created_at": "2010-09-11T14:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97734",
    "user": "leif"
}
```

Replying to [comment:21 jdemeyer]:
> Replying to [comment:17 leif]:
> > Can someone test the new spkg on MacOS X 10.**4** **Intel**? (The upstream fix only adds `-fno-common` on PPCs, not *Tiger* in general, which is afaik wrong.)
> 
> I agree this certainly needs to be tested.

Well, the incapability of 10.4's linker / loader to handle common symbols in conjunction with dynamic libraries is completely unrelated to the processor architecture; I doubt the one used on Intel processors in 10.4 will differ much from the one on PowerPCs. (PPC may imply Darwin 8, but not the other way around.)

So I'd prefer keeping *our* patch (which is already well-tested), or modify it to add a distinction on the Darwin release (``uname -r``, see above).



---

archive/issue_comments_097735.json:
```json
{
    "body": "The new spkg works (with SAGE_CHECK=yes) on t2.math.",
    "created_at": "2010-09-11T17:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97735",
    "user": "jhpalmieri"
}
```

The new spkg works (with SAGE_CHECK=yes) on t2.math.



---

archive/issue_comments_097736.json:
```json
{
    "body": "Replying to [comment:23 leif]:\n> Well, the incapability of 10.4's linker / loader to handle common symbols in conjunction with dynamic libraries is completely unrelated to the processor architecture; I doubt the one used on Intel processors in 10.4 will differ much from the one on PowerPCs. (PPC may imply Darwin 8, but not the other way around.)\n\nI sent an email to the PARI people about this, let's see what they say.",
    "created_at": "2010-09-12T08:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97736",
    "user": "jdemeyer"
}
```

Replying to [comment:23 leif]:
> Well, the incapability of 10.4's linker / loader to handle common symbols in conjunction with dynamic libraries is completely unrelated to the processor architecture; I doubt the one used on Intel processors in 10.4 will differ much from the one on PowerPCs. (PPC may imply Darwin 8, but not the other way around.)

I sent an email to the PARI people about this, let's see what they say.



---

archive/issue_comments_097737.json:
```json
{
    "body": "Replying to [comment:21 jdemeyer]:\n> Replying to [comment:17 leif]:\n> > Can someone test the new spkg on MacOS X 10.**4** **Intel**? (The upstream fix only adds `-fno-common` on PPCs, not *Tiger* in general, which is afaik wrong.)\n> \n> I agree this certainly needs to be tested.\n\nGeorg, perhaps you could confirm that `-fno-common` is also needed on MacOS X 10.4 **Intel** machines? (Or the opposite, but to me that's unlikely.)\n\nIt should be sufficient to just try\n\n```sh\n$ cd .../pari-2.4.3.svn-12577.p6/src\n$ ./Configure --graphic=none\n$ make gp\n```\n\n(with http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p6.spkg)",
    "created_at": "2010-09-17T15:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97737",
    "user": "leif"
}
```

Replying to [comment:21 jdemeyer]:
> Replying to [comment:17 leif]:
> > Can someone test the new spkg on MacOS X 10.**4** **Intel**? (The upstream fix only adds `-fno-common` on PPCs, not *Tiger* in general, which is afaik wrong.)
> 
> I agree this certainly needs to be tested.

Georg, perhaps you could confirm that `-fno-common` is also needed on MacOS X 10.4 **Intel** machines? (Or the opposite, but to me that's unlikely.)

It should be sufficient to just try

```sh
$ cd .../pari-2.4.3.svn-12577.p6/src
$ ./Configure --graphic=none
$ make gp
```

(with http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p6.spkg)



---

archive/issue_comments_097738.json:
```json
{
    "body": "The error we previously got on MacOS X 10.4 **PPC** looked like this:\n\n```\n/usr/bin/gcc  -o \"/Users/jdemeyer/pari-2.4.3.svn-12577/src/Odarwin-ppc\"/libpari-2.4.dylib -dynamiclib  -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer    -fPIC -Wl,-flat_namespace,-undefined,suppress  mp.o mpinl.o F2x.o FF.o Flx.o FpE.o FpV.o FpX.o Qfb.o RgV.o RgX.o ZV.o ZX.o alglin1.o alglin2.o arith1.o arith2.o base1.o base2.o base3.o base4.o base5.o bb_group.o bibli1.o bibli2.o bit.o buch1.o buch2.o buch3.o buch4.o concat.o ellanal.o elliptic.o galconj.o gen1.o gen2.o gen3.o hnf_snf.o ifactor1.o lll.o perm.o polarit1.o polarit2.o polarit3.o prime.o random.o rootpol.o subcyclo.o subgroup.o trans1.o trans2.o trans3.o anal.o compat.o compile.o default.o errmsg.o es.o eval.o hash.o init.o intnum.o members.o pariinl.o parse.o sumiter.o DedekZeta.o Hensel.o QX_factor.o aprcl.o elldata.o ellsea.o galois.o galpol.o groupid.o krasner.o kummer.o mpqs.o nffactor.o part.o stark.o subfield.o thue.o darwin.o\nld: common symbols not allowed with MH_DYLIB output format with the -multi_module option\ninit.o definition of common _DEBUGMEM (size 4)\ninit.o definition of common _avma (size 4)\ninit.o definition of common _bot (size 4)\n[...]\nes.o definition of common _pariErr (size 4)\nes.o definition of common _pariOut (size 4)\ninit.o definition of common _pari_errfile (size 4)\ninit.o definition of common _pari_infile (size 4)\ninit.o definition of common _pari_outfile (size 4)\ninit.o definition of common _cb_pari_err_recover (size 4)\ninit.o definition of common _foreignFuncFree (size 4)\ninit.o definition of common _cb_pari_handle_exception (size 4)\ninit.o definition of common _cb_pari_sigint (size 4)\ninit.o definition of common _cb_pari_whatnow (size 4)\ninit.o definition of common _foreignExprHandler (size 4)\ninit.o definition of common _foreignHandler (size 4)\ninit.o definition of common _memused (size 4)\n/usr/bin/libtool: internal link edit command failed\nmake[1]: *** [libpari-2.4.dylib] Error 1\nmake: *** [gp] Error 2\n```\n",
    "created_at": "2010-09-17T16:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97738",
    "user": "leif"
}
```

The error we previously got on MacOS X 10.4 **PPC** looked like this:

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

archive/issue_comments_097739.json:
```json
{
    "body": "Replying to [comment:25 jdemeyer]:\n> I sent an email to the PARI people about this, let's see what they say.\n\nI haven't had much luck, see [http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1088](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1088):\n\nBill Allombert wrote:\n> Jeroen Demeyer wrote:\n> > In that case, I strongly recommend you to apply the patch to ALL darwin\n> > architectures, not just ppc/ppc64.\n> Why ? Is there any documentation that recommend that ? gcc documentation certainly does not.\n\nI do agree with leif though, I will prepare a .p7 with the fix.",
    "created_at": "2010-09-17T20:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97739",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_097740.json:
```json
{
    "body": "Replying to [comment:28 jdemeyer]:\n> I do agree with leif though, I will prepare a .p7 with the fix.\n\nNew spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p7.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p7.spkg)",
    "created_at": "2010-09-19T08:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97740",
    "user": "jdemeyer"
}
```

Replying to [comment:28 jdemeyer]:
> I do agree with leif though, I will prepare a .p7 with the fix.

New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p7.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/pari-2.4.3.svn-12577.p7.spkg)



---

archive/issue_comments_097741.json:
```json
{
    "body": "Attachment\n\nPatch for the PARI spkg .p6 to .p7",
    "created_at": "2010-09-19T08:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97741",
    "user": "jdemeyer"
}
```

Attachment

Patch for the PARI spkg .p6 to .p7



---

archive/issue_comments_097742.json:
```json
{
    "body": "I think this is ready for review now.  The original issue seems to be fixed and the `get_dlcflags` change has been reverted.",
    "created_at": "2010-09-19T16:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97742",
    "user": "jdemeyer"
}
```

I think this is ready for review now.  The original issue seems to be fixed and the `get_dlcflags` change has been reverted.



---

archive/issue_comments_097743.json:
```json
{
    "body": "I've again tested the latest p7 (which includes only minor* changes w.r.t. the p6) and the new Sage library patch (additional regression doctest) on Ubuntu 10.04 x86_64 (`ptestlong` run twice, the second time with #9898 applied and the lcalc p5 spkg from #9845). (Also, the new spkg is \"sane\".)\n\nSince Jeroen has already successfully tested it on a PPC Mac (big-endian), and John on t2.math (I assume in 32-bit big-endian mode), and the patch to `get_dlcflags` has been reverted to what we already tested (which definitely works on MacOS X 10.**4** **Intel**, too), I set this to \"positive review\".\n\n----\n*Although I must admit I haven't yet verified that the newly updated upstream source files claiming to fix [PARI bug #1079](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079) achieve the same as the previously applied Sage patches (\"segmentation fault in `rnfequation(,,1)` over Q\").",
    "created_at": "2010-09-19T23:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97743",
    "user": "leif"
}
```

I've again tested the latest p7 (which includes only minor* changes w.r.t. the p6) and the new Sage library patch (additional regression doctest) on Ubuntu 10.04 x86_64 (`ptestlong` run twice, the second time with #9898 applied and the lcalc p5 spkg from #9845). (Also, the new spkg is "sane".)

Since Jeroen has already successfully tested it on a PPC Mac (big-endian), and John on t2.math (I assume in 32-bit big-endian mode), and the patch to `get_dlcflags` has been reverted to what we already tested (which definitely works on MacOS X 10.**4** **Intel**, too), I set this to "positive review".

----
*Although I must admit I haven't yet verified that the newly updated upstream source files claiming to fix [PARI bug #1079](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079) achieve the same as the previously applied Sage patches ("segmentation fault in `rnfequation(,,1)` over Q").



---

archive/issue_comments_097744.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-19T23:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97744",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097745.json:
```json
{
    "body": "Replying to [comment:31 leif]:\n> I haven't yet verified that the newly updated upstream source files claiming to fix [PARI bug #1079](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079) achieve the same as the previously applied Sage patches [...]\n\nAs far as I can tell they do. (And do not introduce other changes.)",
    "created_at": "2010-09-20T00:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97745",
    "user": "leif"
}
```

Replying to [comment:31 leif]:
> I haven't yet verified that the newly updated upstream source files claiming to fix [PARI bug #1079](http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1079) achieve the same as the previously applied Sage patches [...]

As far as I can tell they do. (And do not introduce other changes.)



---

archive/issue_comments_097746.json:
```json
{
    "body": "I also tested this again on t2 (32-bit) and also an a 10.6 OS X Intel Mac, just to make sure the new Darwin-only changes didn't mess that up.  No problems in either case.",
    "created_at": "2010-09-20T01:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97746",
    "user": "jhpalmieri"
}
```

I also tested this again on t2 (32-bit) and also an a 10.6 OS X Intel Mac, just to make sure the new Darwin-only changes didn't mess that up.  No problems in either case.



---

archive/issue_comments_097747.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9875#issuecomment-97747",
    "user": "mpatel"
}
```

Resolution: fixed
