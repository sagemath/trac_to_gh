# Issue 9844: lcalc doesn't build on cygwin due to missing time.h include

archive/issues_009844.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @rishikesha @nexttime @jdemeyer\n\nOne needs to add\n\n```\n#include <time.h> \n```\n\nto `include/Lcommandline_numbertheory.h`\nto get lcalc to build on cygwin.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9845\n\n",
    "created_at": "2010-09-01T02:17:51Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "lcalc doesn't build on cygwin due to missing time.h include",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9844",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber

CC:  @rishikesha @nexttime @jdemeyer

One needs to add

```
#include <time.h> 
```

to `include/Lcommandline_numbertheory.h`
to get lcalc to build on cygwin.

Issue created by migration from https://trac.sagemath.org/ticket/9845





---

archive/issue_comments_096988.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-01T02:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96988",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096989.json:
```json
{
    "body": "Spkg here: http://sage.math.washington.edu/home/wstein/patches/lcalc-20100428-1.23.p4.spkg",
    "created_at": "2010-09-01T02:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96989",
    "user": "https://github.com/williamstein"
}
```

Spkg here: http://sage.math.washington.edu/home/wstein/patches/lcalc-20100428-1.23.p4.spkg



---

archive/issue_comments_096990.json:
```json
{
    "body": "I've posted a new spkg at http://sage.math.washington.edu/home/mhansen/lcalc-20100428-1.23.p4.spkg which contains some of the fixes pointed out at #9775",
    "created_at": "2010-09-01T22:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96990",
    "user": "https://github.com/mwhansen"
}
```

I've posted a new spkg at http://sage.math.washington.edu/home/mhansen/lcalc-20100428-1.23.p4.spkg which contains some of the fixes pointed out at #9775



---

archive/issue_comments_096991.json:
```json
{
    "body": "Thanks for fixing much of what I mentioned at #9775.\n\nI'm not sure if we should drop the usual \"sanity check\" at the top of `spkg-install`.\n(Btw, you missed the \"p2\" in its top comment.)\n\nThe first comment regarding `SAGE_DEBUG` and the message in the `else` part aren't current.\n(*\"Unset SAGE_DEBUG ...\"* should read *\"Set SAGE_DEBUG to yes ...\"*. Though I'd prefer adding `-g` independently of that setting, since it doesn't influence performance, and most other spkgs do so.)\n\nReplacing `-lmpir` by `-lgmp` is perhaps a minor issue; using `$MAKE` instead of `make` (`$(MAKE)` in Lcalc's Makefile itself, too) IMHO not. Unfortunately, the current `spkg/install` also uses `make` instead of `$MAKE` unless `SAGE_PARALLEL_SPKG_BUILD=yes`, which I consider a bug, since adding `-j` is not the only case in which one would set `MAKE`. One should never call `make` inside a Makefile or a script that's executed through *some* \"make\", because it might be a different one.",
    "created_at": "2010-09-02T00:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96991",
    "user": "https://github.com/nexttime"
}
```

Thanks for fixing much of what I mentioned at #9775.

I'm not sure if we should drop the usual "sanity check" at the top of `spkg-install`.
(Btw, you missed the "p2" in its top comment.)

The first comment regarding `SAGE_DEBUG` and the message in the `else` part aren't current.
(*"Unset SAGE_DEBUG ..."* should read *"Set SAGE_DEBUG to yes ..."*. Though I'd prefer adding `-g` independently of that setting, since it doesn't influence performance, and most other spkgs do so.)

Replacing `-lmpir` by `-lgmp` is perhaps a minor issue; using `$MAKE` instead of `make` (`$(MAKE)` in Lcalc's Makefile itself, too) IMHO not. Unfortunately, the current `spkg/install` also uses `make` instead of `$MAKE` unless `SAGE_PARALLEL_SPKG_BUILD=yes`, which I consider a bug, since adding `-j` is not the only case in which one would set `MAKE`. One should never call `make` inside a Makefile or a script that's executed through *some* "make", because it might be a different one.



---

archive/issue_comments_096992.json:
```json
{
    "body": "P.S.:\n\n```\nall:\n#       make print_vars\n        make libLfunction.so\n        make lcalc\n        make examples\n#       make find_L\n#       make test\n```\n\nshould simply (for our purposes) be\n\n```\nall:    libLfunction.so lcalc examples\n```\n\nor even just\n\n```\nall:    lcalc examples\n```\n\nbut one has to add the proper dependency, i.e.:\n\n```\nexamples: libLfunction.so\n        $(CC) $(CCFLAGS) $(INCLUDEFILES) example_programs/example.cc libLfunction.so -o example_programs/example $(GMP_FLAGS)\n```\n",
    "created_at": "2010-09-02T00:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96992",
    "user": "https://github.com/nexttime"
}
```

P.S.:

```
all:
#       make print_vars
        make libLfunction.so
        make lcalc
        make examples
#       make find_L
#       make test
```

should simply (for our purposes) be

```
all:    libLfunction.so lcalc examples
```

or even just

```
all:    lcalc examples
```

but one has to add the proper dependency, i.e.:

```
examples: libLfunction.so
        $(CC) $(CCFLAGS) $(INCLUDEFILES) example_programs/example.cc libLfunction.so -o example_programs/example $(GMP_FLAGS)
```




---

archive/issue_comments_096993.json:
```json
{
    "body": "Btw, the `-lmpir` (or `-lgmp`) is only needed if we build a *static* version of `lcalc`, since only the also linked PARI library directly uses it.",
    "created_at": "2010-09-02T21:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96993",
    "user": "https://github.com/nexttime"
}
```

Btw, the `-lmpir` (or `-lgmp`) is only needed if we build a *static* version of `lcalc`, since only the also linked PARI library directly uses it.



---

archive/issue_comments_096994.json:
```json
{
    "body": "Attachment [lcalc-20100428-1.23.p2-p4.diff](tarball://root/attachments/some-uuid/ticket9845/lcalc-20100428-1.23.p2-p4.diff) by @nexttime created at 2010-09-02 23:41:16\n\nDiff between the p2 (#9592) and Mike's p4 spkg - for review/reference.",
    "created_at": "2010-09-02T23:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96994",
    "user": "https://github.com/nexttime"
}
```

Attachment [lcalc-20100428-1.23.p2-p4.diff](tarball://root/attachments/some-uuid/ticket9845/lcalc-20100428-1.23.p2-p4.diff) by @nexttime created at 2010-09-02 23:41:16

Diff between the p2 (#9592) and Mike's p4 spkg - for review/reference.



---

archive/issue_comments_096995.json:
```json
{
    "body": "I've attached a diff between the lcalc-20100428-1.23.p2 spkg from #9592 and Mike's / William's lcalc-20100428-1.23.p4 for easier reviewing.\n\nNote that #9592 also still needs review!\n(We need this modified package for [upgrading PARI / Sage 4.6](http://wiki.sagemath.org/NewPARI).)",
    "created_at": "2010-09-02T23:58:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96995",
    "user": "https://github.com/nexttime"
}
```

I've attached a diff between the lcalc-20100428-1.23.p2 spkg from #9592 and Mike's / William's lcalc-20100428-1.23.p4 for easier reviewing.

Note that #9592 also still needs review!
(We need this modified package for [upgrading PARI / Sage 4.6](http://wiki.sagemath.org/NewPARI).)



---

archive/issue_comments_096996.json:
```json
{
    "body": "Also, the `dist/` (Debian) directory should be removed, cf. #5903.",
    "created_at": "2010-09-03T22:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96996",
    "user": "https://github.com/nexttime"
}
```

Also, the `dist/` (Debian) directory should be removed, cf. #5903.



---

archive/issue_comments_096997.json:
```json
{
    "body": "Mike, are there Windows virtual machines running Cygwin available to potential reviewers?  (We could give access instructions off-trac.)  It would be great to reduce the number of remaining build tickets at [CygwinPort](http://trac.sagemath.org/sage_trac/wiki/CygwinPort).  And remote Cygwin access might help with #9914 (see [comment:ticket:9914:4 comment 4ff]).",
    "created_at": "2010-09-18T08:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96997",
    "user": "https://github.com/qed777"
}
```

Mike, are there Windows virtual machines running Cygwin available to potential reviewers?  (We could give access instructions off-trac.)  It would be great to reduce the number of remaining build tickets at [CygwinPort](http://trac.sagemath.org/sage_trac/wiki/CygwinPort).  And remote Cygwin access might help with #9914 (see [comment:ticket:9914:4 comment 4ff]).



---

archive/issue_comments_096998.json:
```json
{
    "body": "Replying to [comment:10 mpatel]:\n> Mike, are there Windows virtual machines running Cygwin available to potential reviewers?  (We could give access instructions off-trac.)\n\nI wouldn't mind testing this if needed.",
    "created_at": "2010-09-19T16:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96998",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:10 mpatel]:
> Mike, are there Windows virtual machines running Cygwin available to potential reviewers?  (We could give access instructions off-trac.)

I wouldn't mind testing this if needed.



---

archive/issue_comments_096999.json:
```json
{
    "body": "I have made a trivial change to spkg-install (removed the comment \"# since 'success' relies on an exit code, call set +e before running it.\").  I also removed the dist directory.\n\nNew spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p4.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p4.spkg)",
    "created_at": "2010-09-19T16:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-96999",
    "user": "https://github.com/jdemeyer"
}
```

I have made a trivial change to spkg-install (removed the comment "# since 'success' relies on an exit code, call set +e before running it.").  I also removed the dist directory.

New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p4.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p4.spkg)



---

archive/issue_comments_097000.json:
```json
{
    "body": "I also made the other changes suggested by Leif.  New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p5.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p5.spkg)",
    "created_at": "2010-09-19T16:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-97000",
    "user": "https://github.com/jdemeyer"
}
```

I also made the other changes suggested by Leif.  New spkg: [http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p5.spkg](http://sage.math.washington.edu/home/jdemeyer/spkg/lcalc-20100428-1.23.p5.spkg)



---

archive/issue_comments_097001.json:
```json
{
    "body": "Attachment [lcalc-20100428-1.23.p2-p4.2.diff](tarball://root/attachments/some-uuid/ticket9845/lcalc-20100428-1.23.p2-p4.2.diff) by @jdemeyer created at 2010-09-19 16:35:01\n\nignore this file",
    "created_at": "2010-09-19T16:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-97001",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [lcalc-20100428-1.23.p2-p4.2.diff](tarball://root/attachments/some-uuid/ticket9845/lcalc-20100428-1.23.p2-p4.2.diff) by @jdemeyer created at 2010-09-19 16:35:01

ignore this file



---

archive/issue_comments_097002.json:
```json
{
    "body": "Attachment [lcalc-20100428-1.23.p4-p5.diff](tarball://root/attachments/some-uuid/ticket9845/lcalc-20100428-1.23.p4-p5.diff) by @jdemeyer created at 2010-09-19 16:42:01\n\nDiff between p4 and p5 - for review/reference.",
    "created_at": "2010-09-19T16:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-97002",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [lcalc-20100428-1.23.p4-p5.diff](tarball://root/attachments/some-uuid/ticket9845/lcalc-20100428-1.23.p4-p5.diff) by @jdemeyer created at 2010-09-19 16:42:01

Diff between p4 and p5 - for review/reference.



---

archive/issue_comments_097003.json:
```json
{
    "body": "Looks as if we no longer need `patches/Lcommandline_elliptic.cc.cygwin` (and `patches/Lcommandline_elliptic.cc.cygwin.diff`), since this patch isn't applied.\n\nMike (or Jeroen, if you can test this), is this Cygwin patch / addition obsolete:\n\n```C\n// SAGE -- used below -- needed for Cygwin.\n#ifndef llrint\ninline long long int llrint (double x)\n{\n    long long int llrintres;\n    asm\n    (\"fistpll %0\"\n    : \"=m\" (llrintres) : \"t\" (x) : \"st\");\n    return llrintres;\n}\n#endif\n```\n\n\n(It's *not* included in the generic patch to `Lcommandline_elliptic.cc`, nor upstream.)\n\nApart from old typos, an obsolete comment regarding `SAGE_DEBUG`, and the recent changelog headings lacking the upstream (snapshot?) date (20100428), I'm quite happy with the new spkg (i.e., the Sage part; the patched Makefile is still suboptimal, but never mind). :)\n\nIf this spkg really contains an upstream snapshot, it is unclear from SPKG.txt when this was taken / actually put into the spkg.",
    "created_at": "2010-09-19T19:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-97003",
    "user": "https://github.com/nexttime"
}
```

Looks as if we no longer need `patches/Lcommandline_elliptic.cc.cygwin` (and `patches/Lcommandline_elliptic.cc.cygwin.diff`), since this patch isn't applied.

Mike (or Jeroen, if you can test this), is this Cygwin patch / addition obsolete:

```C
// SAGE -- used below -- needed for Cygwin.
#ifndef llrint
inline long long int llrint (double x)
{
    long long int llrintres;
    asm
    ("fistpll %0"
    : "=m" (llrintres) : "t" (x) : "st");
    return llrintres;
}
#endif
```


(It's *not* included in the generic patch to `Lcommandline_elliptic.cc`, nor upstream.)

Apart from old typos, an obsolete comment regarding `SAGE_DEBUG`, and the recent changelog headings lacking the upstream (snapshot?) date (20100428), I'm quite happy with the new spkg (i.e., the Sage part; the patched Makefile is still suboptimal, but never mind). :)

If this spkg really contains an upstream snapshot, it is unclear from SPKG.txt when this was taken / actually put into the spkg.



---

archive/issue_comments_097004.json:
```json
{
    "body": "The new p5 spkg successfully installed on Sage 4.6.alpha1 (with `MAKE=\"make -j32\"`) and passed `ptestlong` on Ubuntu 10.04 x86_64, so I'm setting this to \"positive review\".\n\nFeel free to revert this in case any errors occur on other systems.",
    "created_at": "2010-09-19T19:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-97004",
    "user": "https://github.com/nexttime"
}
```

The new p5 spkg successfully installed on Sage 4.6.alpha1 (with `MAKE="make -j32"`) and passed `ptestlong` on Ubuntu 10.04 x86_64, so I'm setting this to "positive review".

Feel free to revert this in case any errors occur on other systems.



---

archive/issue_comments_097005.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-19T19:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-97005",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097006.json:
```json
{
    "body": "Replying to [comment:15 leif]:\n> The new p5 spkg successfully installed on Sage 4.6.alpha1 (with `MAKE=\"make -j32\"`) and passed `ptestlong` on Ubuntu 10.04 x86_64, [...]\n\nSame on Ubuntu 9.04 x86 (with `MAKE=\"make -j8\"`).",
    "created_at": "2010-09-19T23:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-97006",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:15 leif]:
> The new p5 spkg successfully installed on Sage 4.6.alpha1 (with `MAKE="make -j32"`) and passed `ptestlong` on Ubuntu 10.04 x86_64, [...]

Same on Ubuntu 9.04 x86 (with `MAKE="make -j8"`).



---

archive/issue_comments_097007.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9844#issuecomment-97007",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
