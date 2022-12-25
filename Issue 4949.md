# Issue 4949: Optionally build spkgs in $SAGE_BUILD_TMPDIR

archive/issues_004949.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  drkirkby @nexttime\n\n$HOME can be slow in case it is NFS mounted for example. So using local scratch space or even better a RAM disk should speed up the build by a nice factor. To so so use $SAGE_BUILD_TMPDIR in case it exists instead of $SAGE_ROOT/spkg/build.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4949\n\n",
    "created_at": "2009-01-07T05:20:19Z",
    "labels": [
        "component: build",
        "critical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "Optionally build spkgs in $SAGE_BUILD_TMPDIR",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4949",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  drkirkby @nexttime

$HOME can be slow in case it is NFS mounted for example. So using local scratch space or even better a RAM disk should speed up the build by a nice factor. To so so use $SAGE_BUILD_TMPDIR in case it exists instead of $SAGE_ROOT/spkg/build.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4949





---

archive/issue_comments_037498.json:
```json
{
    "body": "As a temporary hack to see how this \"feels\" you could delete spkg/build, then make it a symlink to /tmp/build/.",
    "created_at": "2009-01-09T17:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37498",
    "user": "https://github.com/williamstein"
}
```

As a temporary hack to see how this "feels" you could delete spkg/build, then make it a symlink to /tmp/build/.



---

archive/issue_comments_037499.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2010-08-06T21:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37499",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from critical to minor.



---

archive/issue_comments_037500.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-06T21:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37500",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_037501.json:
```json
{
    "body": "Here's a patch.  This implements both `SAGE_BUILD_TMPDIR` and `SAGE_KEEP_BUILT_SPKGS` -- see #9444.  (This is an incremental change rather than a complete reworking of the sage-spkg script, which might be called for.)",
    "created_at": "2010-08-06T21:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37501",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch.  This implements both `SAGE_BUILD_TMPDIR` and `SAGE_KEEP_BUILT_SPKGS` -- see #9444.  (This is an incremental change rather than a complete reworking of the sage-spkg script, which might be called for.)



---

archive/issue_comments_037502.json:
```json
{
    "body": "A little explanation: BUILD is defined (as \"build\") by sage-env, but it was used sporadically in sage-spkg.  With this patch, it is used more consistently.",
    "created_at": "2010-08-06T22:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37502",
    "user": "https://github.com/jhpalmieri"
}
```

A little explanation: BUILD is defined (as "build") by sage-env, but it was used sporadically in sage-spkg.  With this patch, it is used more consistently.



---

archive/issue_comments_037503.json:
```json
{
    "body": "If/when this merges, we should consider closing #6550.  `SAGE_KEEP_BUILT_SPKGS` is a much better name than `SAGE_KEEP_SPKG_BUILD`.",
    "created_at": "2010-08-06T22:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37503",
    "user": "https://github.com/qed777"
}
```

If/when this merges, we should consider closing #6550.  `SAGE_KEEP_BUILT_SPKGS` is a much better name than `SAGE_KEEP_SPKG_BUILD`.



---

archive/issue_comments_037504.json:
```json
{
    "body": "Nice to see progress in the build process... :)\n\nSee also http://trac.sagemath.org/sage_trac/ticket/6550#comment:7 .",
    "created_at": "2010-08-06T22:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37504",
    "user": "https://github.com/nexttime"
}
```

Nice to see progress in the build process... :)

See also http://trac.sagemath.org/sage_trac/ticket/6550#comment:7 .



---

archive/issue_comments_037505.json:
```json
{
    "body": "Should `SAGE_BUILD_TMPDIR` default to `SAGE_TMPDIR`?\n\n(We have btw. lots of - in some cases not very well-named - environment variables.)\n\nMaking use of e.g. a RAM disk (or some user-provided directory) for doctesting is also worth doing.",
    "created_at": "2010-08-06T22:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37505",
    "user": "https://github.com/nexttime"
}
```

Should `SAGE_BUILD_TMPDIR` default to `SAGE_TMPDIR`?

(We have btw. lots of - in some cases not very well-named - environment variables.)

Making use of e.g. a RAM disk (or some user-provided directory) for doctesting is also worth doing.



---

archive/issue_comments_037506.json:
```json
{
    "body": "Replying to [comment:7 leif]:\n> Making use of e.g. a RAM disk (or some user-provided directory) for doctesting is also worth doing.\n\nYou can already set `SAGE_TESTDIR` (or `DOT_SAGE`) to do this.  Or maybe I misunderstand?",
    "created_at": "2010-08-19T21:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37506",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:7 leif]:
> Making use of e.g. a RAM disk (or some user-provided directory) for doctesting is also worth doing.

You can already set `SAGE_TESTDIR` (or `DOT_SAGE`) to do this.  Or maybe I misunderstand?



---

archive/issue_comments_037507.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-05-20T14:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37507",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_037508.json:
```json
{
    "body": "[attachment: trac_4949-scripts.patch] does not apply:\n\n\n```\nsage: hg_sage.apply(\"/home/mariah/trac_4949-scripts.patch\")\ncd \"/home/mariah/sage/sage-4.7.rc2-x86_64-Linux-core2-fc/devel/sage\" && hg status\ncd \"/home/mariah/sage/sage-4.7.rc2-x86_64-Linux-core2-fc/devel/sage\" && hg status\ncd \"/home/mariah/sage/sage-4.7.rc2-x86_64-Linux-core2-fc/devel/sage\" && hg import   \"/home/mariah/trac_4949-scripts.patch\"\napplying /home/mariah/trac_4949-scripts.patch\nunable to find 'sage-spkg' for patching\n5 out of 5 hunks FAILED -- saving rejects to file sage-spkg.rej\nabort: patch failed to apply\nsage: \n```\n",
    "created_at": "2011-05-20T14:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37508",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

[attachment: trac_4949-scripts.patch] does not apply:


```
sage: hg_sage.apply("/home/mariah/trac_4949-scripts.patch")
cd "/home/mariah/sage/sage-4.7.rc2-x86_64-Linux-core2-fc/devel/sage" && hg status
cd "/home/mariah/sage/sage-4.7.rc2-x86_64-Linux-core2-fc/devel/sage" && hg status
cd "/home/mariah/sage/sage-4.7.rc2-x86_64-Linux-core2-fc/devel/sage" && hg import   "/home/mariah/trac_4949-scripts.patch"
applying /home/mariah/trac_4949-scripts.patch
unable to find 'sage-spkg' for patching
5 out of 5 hunks FAILED -- saving rejects to file sage-spkg.rej
abort: patch failed to apply
sage: 
```




---

archive/issue_comments_037509.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-05-20T14:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37509",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_037510.json:
```json
{
    "body": "Here's a rebased version of [attachment:trac_4949-scripts.patch].  Note that it's for the scripts repository, so you have to apply it with \"hg_scripts.apply(...)\" rather than \"hg_sage.apply(...)\".",
    "created_at": "2011-05-20T14:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37510",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a rebased version of [attachment:trac_4949-scripts.patch].  Note that it's for the scripts repository, so you have to apply it with "hg_scripts.apply(...)" rather than "hg_sage.apply(...)".



---

archive/issue_comments_037511.json:
```json
{
    "body": "I applied the patch [attachment:trac_4949-scripts.patch], then moved\nthe modified sage-spkg file to a fresh source directory of sage-4.7.rc4.  I set SAGE_BUILD_TMPDIR and SAGE_KEEP_BUILT_SPKGS, and\ndid 'make testlong'.  The builds took place in the location SAGE_BUILD_TMPDIR and all tests passed.  I applied the patch [attachment: trac_4949-installation.patch], did 'sage -b', then 'sage -docbuild installation html' and verified that the documentation change was made and makes sense.  Positive review.",
    "created_at": "2011-05-25T13:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37511",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

I applied the patch [attachment:trac_4949-scripts.patch], then moved
the modified sage-spkg file to a fresh source directory of sage-4.7.rc4.  I set SAGE_BUILD_TMPDIR and SAGE_KEEP_BUILT_SPKGS, and
did 'make testlong'.  The builds took place in the location SAGE_BUILD_TMPDIR and all tests passed.  I applied the patch [attachment: trac_4949-installation.patch], did 'sage -b', then 'sage -docbuild installation html' and verified that the documentation change was made and makes sense.  Positive review.



---

archive/issue_comments_037512.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-25T13:35:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37512",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037513.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-05-27T08:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37513",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_037514.json:
```json
{
    "body": "I think one should add a note in the documentation about how much disk space this is expected to use.  Are the spkgs first all built and then all deleted or are they built-deleted one by one?",
    "created_at": "2011-05-27T08:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37514",
    "user": "https://github.com/jdemeyer"
}
```

I think one should add a note in the documentation about how much disk space this is expected to use.  Are the spkgs first all built and then all deleted or are they built-deleted one by one?



---

archive/issue_comments_037515.json:
```json
{
    "body": "Wouldn't it be sufficient to just (keep the -- perhaps slightly modified -- documentation and the three lines honoring `SAGE_KEEP_BUILT_SPKGS` and) change the variable `BUILD` (bad name btw.) in `sage-env` if `SAGE_BUILD_TMPDIR` is set?\n\nThat way this ticket would hardly collide with #11021, which fixes a lot in `sage-spkg` (and a bug in `sage-env` w.r.t. `BUILD`), also using `$BUILD` consistently there.\n\nI also would use `SAGE_BUILD_TMPDIR` \"directly\", without creating yet another subdirectory (`build`) in it; the spkgs are extracted into their own directories anyway.",
    "created_at": "2011-08-03T14:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37515",
    "user": "https://github.com/nexttime"
}
```

Wouldn't it be sufficient to just (keep the -- perhaps slightly modified -- documentation and the three lines honoring `SAGE_KEEP_BUILT_SPKGS` and) change the variable `BUILD` (bad name btw.) in `sage-env` if `SAGE_BUILD_TMPDIR` is set?

That way this ticket would hardly collide with #11021, which fixes a lot in `sage-spkg` (and a bug in `sage-env` w.r.t. `BUILD`), also using `$BUILD` consistently there.

I also would use `SAGE_BUILD_TMPDIR` "directly", without creating yet another subdirectory (`build`) in it; the spkgs are extracted into their own directories anyway.



---

archive/issue_comments_037516.json:
```json
{
    "body": "Ooops, unfortunately it's not *that* easy, because `$BUILD` is also just used as a *sub*directory name in `sage-spkg`.",
    "created_at": "2011-08-03T14:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37516",
    "user": "https://github.com/nexttime"
}
```

Ooops, unfortunately it's not *that* easy, because `$BUILD` is also just used as a *sub*directory name in `sage-spkg`.



---

archive/issue_comments_037517.json:
```json
{
    "body": "Replying to [comment:13 jdemeyer]:\n> I think one should add a note in the documentation about how much disk space this is expected to use.  Are the spkgs first all built and then all deleted or are they built-deleted one by one?\n\nI've modified the documentation to try to address this.  I built Sage on various machines (sage.math, David Kirkby's machine hawk, various skynet machines), and found that\n\n- the single largest subdirectory of \"build\" can be up to 1165M (building eclib on the skynet machines iras and cleo, ia64 processors).  On all of the other machines, it took at most 880M.  On sage.math, cicero, and my mac, the largest took 320M.\n\n- the total amount of disk space, if you keep all of the subdirectories can be as large as 5.3G (iras and cleo again) or as small as 2.2G (hawk).\n\nI've put in conservative estimates for these in the documentation.",
    "created_at": "2011-08-04T15:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37517",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:13 jdemeyer]:
> I think one should add a note in the documentation about how much disk space this is expected to use.  Are the spkgs first all built and then all deleted or are they built-deleted one by one?

I've modified the documentation to try to address this.  I built Sage on various machines (sage.math, David Kirkby's machine hawk, various skynet machines), and found that

- the single largest subdirectory of "build" can be up to 1165M (building eclib on the skynet machines iras and cleo, ia64 processors).  On all of the other machines, it took at most 880M.  On sage.math, cicero, and my mac, the largest took 320M.

- the total amount of disk space, if you keep all of the subdirectories can be as large as 5.3G (iras and cleo again) or as small as 2.2G (hawk).

I've put in conservative estimates for these in the documentation.



---

archive/issue_comments_037518.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-08-04T15:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37518",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_037519.json:
```json
{
    "body": "Replying to [comment:16 jhpalmieri]:\n> I've modified the documentation to try to address this.\n\nThe usage of `$` is a bit inconsistent: `:file:`$SAGE_ROOT/...`` vs. `:file:`SAGE_BUILD_TMPDIR/...``.\n\nI would add a warning that `SAGE_BUILD_TMPDIR` must not contain spaces, and should be an absolute path (starting with a slash or whatever). Note that none of this is checked in `sage-spkg`; also, a broken `test` might return `true` for an empty string, so I would also `test -n \"$SAGE_BUILD_TMPDIR\"`.\n\nAlso, if `SAGE_BUILD_TMPDIR` is set but the directory does not exist, no warning or error message is printed.\n\n\n\n\n> I built Sage on various machines [...] and found that [...]\n> I've put in conservative estimates for these in the documentation.\n\nThe actual space required or used does hardly depend on the platform, but the file system characteristics, i.e. the block size.\n\nThe worst case space usage is theoretically unlimited when taking into account rebuilds and (re)installations of newer packages, as old build dirs are moved to the `$BUILD/old/` directory if `-s` was specified or `SAGE_KEEP_BUILT_SPKGS=yes`.\n\n(Btw., for some reason the build dirs of the base packages never get deleted. Perhaps that's a side-effect of the \"`BUILD` bug\", haven't tracked this down.)\n\nI would mention the relationship to the `-s` parameter when installing packages with `sage`; the main reason for the additional environment variable is that there's no other way to achieve what `-s` does when using `make`.",
    "created_at": "2011-08-04T18:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37519",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:16 jhpalmieri]:
> I've modified the documentation to try to address this.

The usage of `$` is a bit inconsistent: `:file:`$SAGE_ROOT/...`` vs. `:file:`SAGE_BUILD_TMPDIR/...``.

I would add a warning that `SAGE_BUILD_TMPDIR` must not contain spaces, and should be an absolute path (starting with a slash or whatever). Note that none of this is checked in `sage-spkg`; also, a broken `test` might return `true` for an empty string, so I would also `test -n "$SAGE_BUILD_TMPDIR"`.

Also, if `SAGE_BUILD_TMPDIR` is set but the directory does not exist, no warning or error message is printed.




> I built Sage on various machines [...] and found that [...]
> I've put in conservative estimates for these in the documentation.

The actual space required or used does hardly depend on the platform, but the file system characteristics, i.e. the block size.

The worst case space usage is theoretically unlimited when taking into account rebuilds and (re)installations of newer packages, as old build dirs are moved to the `$BUILD/old/` directory if `-s` was specified or `SAGE_KEEP_BUILT_SPKGS=yes`.

(Btw., for some reason the build dirs of the base packages never get deleted. Perhaps that's a side-effect of the "`BUILD` bug", haven't tracked this down.)

I would mention the relationship to the `-s` parameter when installing packages with `sage`; the main reason for the additional environment variable is that there's no other way to achieve what `-s` does when using `make`.



---

archive/issue_comments_037520.json:
```json
{
    "body": "Replying to [comment:17 leif]:\n> The actual space required or used does hardly depend on the platform, but the file system characteristics, i.e. the block size.\n\nWell, many of the systems on which I tested were on skynet, built in subdirectories of a shared home directory -- all of the skynet machines use the same $HOME.  On some of those machines, building eclib took over 1 gigabyte, while on others, it took under 320 megabytes.  There are certainly differences between the types of libraries produced: .so files on linux, .dylib files on darwin, etc.  I would also guess that the size of the library files might vary depending on the compiler, whether it's 32- or 64-bit, etc.\n\n> The worst case space usage is theoretically unlimited when taking into account rebuilds and (re)installations of newer packages, as old build dirs are moved to the $BUILD/old/ directory if -s was specified or SAGE_KEEP_BUILT_SPKGS=yes.\n\nRight, but the documentation as written is accurate (\"After a full build of Sage...\") and I think is good enough.  Anyone who sets this variable should be paying attention to the build directory anyway.\n\n> (Btw., for some reason the build dirs of the base packages never get deleted. Perhaps that's a side-effect of the \"BUILD bug\", haven't tracked this down.)\n\n`prereq` and `bzip` are not installed by sage-spkg but by their own install scripts (`prereq-0.9-install` and `bzip2-1.0.5-install`), which create subdirectories of `build` but don't delete them when they're done.\n\nAdding a comment about the relationship to the `-s` option is a good idea.  I'll try to add some tests for `SAGE_BUILD_TEMPDIR`, too.",
    "created_at": "2011-08-07T20:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37520",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:17 leif]:
> The actual space required or used does hardly depend on the platform, but the file system characteristics, i.e. the block size.

Well, many of the systems on which I tested were on skynet, built in subdirectories of a shared home directory -- all of the skynet machines use the same $HOME.  On some of those machines, building eclib took over 1 gigabyte, while on others, it took under 320 megabytes.  There are certainly differences between the types of libraries produced: .so files on linux, .dylib files on darwin, etc.  I would also guess that the size of the library files might vary depending on the compiler, whether it's 32- or 64-bit, etc.

> The worst case space usage is theoretically unlimited when taking into account rebuilds and (re)installations of newer packages, as old build dirs are moved to the $BUILD/old/ directory if -s was specified or SAGE_KEEP_BUILT_SPKGS=yes.

Right, but the documentation as written is accurate ("After a full build of Sage...") and I think is good enough.  Anyone who sets this variable should be paying attention to the build directory anyway.

> (Btw., for some reason the build dirs of the base packages never get deleted. Perhaps that's a side-effect of the "BUILD bug", haven't tracked this down.)

`prereq` and `bzip` are not installed by sage-spkg but by their own install scripts (`prereq-0.9-install` and `bzip2-1.0.5-install`), which create subdirectories of `build` but don't delete them when they're done.

Adding a comment about the relationship to the `-s` option is a good idea.  I'll try to add some tests for `SAGE_BUILD_TEMPDIR`, too.



---

archive/issue_comments_037521.json:
```json
{
    "body": "Here are two new patches.  The scripts patch checks for the existence of SAGE_BUILD_TMPDIR, and it also should correctly delete the build subdirectories afterwards -- I had missed this in the previous patch.",
    "created_at": "2011-08-08T03:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37521",
    "user": "https://github.com/jhpalmieri"
}
```

Here are two new patches.  The scripts patch checks for the existence of SAGE_BUILD_TMPDIR, and it also should correctly delete the build subdirectories afterwards -- I had missed this in the previous patch.



---

archive/issue_comments_037522.json:
```json
{
    "body": "scripts repo",
    "created_at": "2011-08-08T03:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37522",
    "user": "https://github.com/jhpalmieri"
}
```

scripts repo



---

archive/issue_comments_037523.json:
```json
{
    "body": "Attachment [trac_4949-scripts.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-scripts.patch) by @nexttime created at 2011-08-08 12:58:06\n\nThere's a `$` missing in\n\n```\n:file:`$SAGE_ROOT/spkg/build` or :file:`SAGE_BUILD_TMPDIR/build`\n```\n\n\nI would clarify that `SAGE_KEEP_BUILT_SPKGS=yes` affects *all* spkg installations (whether with `./sage [-i|-f]` or `make`, the latter also when *re*building [parts of] Sage), and that the build directory (within the Sage tree or in `$SAGE_BUILD_TMPDIR/`) will definitely grow over time, i.e., whenever new packages get installed or already existing / built packages reinstalled, unless one unsets `SAGE_KEEP_BUILT_SPKGS` at some point (which of course doesn't delete existing subdirectories in the first place).\n\n\n\n\nYour observations regarding the build tree sizes on skynet are interesting; there IMHO shouldn't be such a large difference, at least not when doing \"the same thing\".\n\nThere are differences in object code size between RISC and CISC architectures (on the former usually larger, but *at most* by a factor of 2 I think) and between 32-bit and 64-bit (mostly on RISC architectures, and also if there's a lot of static data involving e.g. pointers or integers of different size); other differences might be due to debug symbols and *how and what* we build (e.g. assembly implementations, static or dynamic libraries in addition) on a specific platform.\n\nI would mention the effect of the block size of the file system though (as a note perhaps), since many packages consist of a large number of small files.",
    "created_at": "2011-08-08T12:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37523",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_4949-scripts.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-scripts.patch) by @nexttime created at 2011-08-08 12:58:06

There's a `$` missing in

```
:file:`$SAGE_ROOT/spkg/build` or :file:`SAGE_BUILD_TMPDIR/build`
```


I would clarify that `SAGE_KEEP_BUILT_SPKGS=yes` affects *all* spkg installations (whether with `./sage [-i|-f]` or `make`, the latter also when *re*building [parts of] Sage), and that the build directory (within the Sage tree or in `$SAGE_BUILD_TMPDIR/`) will definitely grow over time, i.e., whenever new packages get installed or already existing / built packages reinstalled, unless one unsets `SAGE_KEEP_BUILT_SPKGS` at some point (which of course doesn't delete existing subdirectories in the first place).




Your observations regarding the build tree sizes on skynet are interesting; there IMHO shouldn't be such a large difference, at least not when doing "the same thing".

There are differences in object code size between RISC and CISC architectures (on the former usually larger, but *at most* by a factor of 2 I think) and between 32-bit and 64-bit (mostly on RISC architectures, and also if there's a lot of static data involving e.g. pointers or integers of different size); other differences might be due to debug symbols and *how and what* we build (e.g. assembly implementations, static or dynamic libraries in addition) on a specific platform.

I would mention the effect of the block size of the file system though (as a note perhaps), since many packages consist of a large number of small files.



---

archive/issue_comments_037524.json:
```json
{
    "body": "Attachment [trac_4949-installation.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-installation.patch) by @jhpalmieri created at 2011-08-08 15:39:55\n\nsage repo: update installation guide",
    "created_at": "2011-08-08T15:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37524",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-installation.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-installation.patch) by @jhpalmieri created at 2011-08-08 15:39:55

sage repo: update installation guide



---

archive/issue_comments_037525.json:
```json
{
    "body": "Replying to [comment:20 leif]:\n> I would clarify that `SAGE_KEEP_BUILT_SPKGS=yes` affects *all* spkg installations.\n\nDone\n\n> and that the build directory will definitely grow over time\n\nI've added some explanation.  It doesn't grow quite as fast as it might, since pre-existing subdirectories are moved to SAGE_ROOT/spkg/build/old/, *overwriting* copies that were already there.  So just reinstalling Sage over and over again will just use twice as much as space as doing it once.  Upgrading will then take up more space.\n\n> Your observations regarding the build tree sizes on skynet are interesting; there IMHO shouldn't be such a large difference, at least not when doing \"the same thing\".\n\n\"eclib\" is the usual culprit.  There are huge differences in the amount of disk space it uses, so on some systems it is by far the largest, and on others, it isn't.  On the skynet machines, \"moin\" uses a consistent 320 megabytes, whereas eclib ranges from something under that to over 1 gig, depending on the OS and the processor.\n\n> I would mention the effect of the block size of the file system though (as a note perhaps), since many packages consist of a large number of small files.\n\nDone.",
    "created_at": "2011-08-08T16:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37525",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:20 leif]:
> I would clarify that `SAGE_KEEP_BUILT_SPKGS=yes` affects *all* spkg installations.

Done

> and that the build directory will definitely grow over time

I've added some explanation.  It doesn't grow quite as fast as it might, since pre-existing subdirectories are moved to SAGE_ROOT/spkg/build/old/, *overwriting* copies that were already there.  So just reinstalling Sage over and over again will just use twice as much as space as doing it once.  Upgrading will then take up more space.

> Your observations regarding the build tree sizes on skynet are interesting; there IMHO shouldn't be such a large difference, at least not when doing "the same thing".

"eclib" is the usual culprit.  There are huge differences in the amount of disk space it uses, so on some systems it is by far the largest, and on others, it isn't.  On the skynet machines, "moin" uses a consistent 320 megabytes, whereas eclib ranges from something under that to over 1 gig, depending on the OS and the processor.

> I would mention the effect of the block size of the file system though (as a note perhaps), since many packages consist of a large number of small files.

Done.



---

archive/issue_comments_037526.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-24T02:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37526",
    "user": "https://github.com/koffie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037527.json:
```json
{
    "body": "I've build sage entirely from scratch after applying the patch and replacing the bootstrap version of sage-spkg in SAGE_ROOT/spkg/base and passing all doctest . Both with and without the environment variables set. So I think this one is ready to get merged.",
    "created_at": "2011-08-24T02:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37527",
    "user": "https://github.com/koffie"
}
```

I've build sage entirely from scratch after applying the patch and replacing the bootstrap version of sage-spkg in SAGE_ROOT/spkg/base and passing all doctest . Both with and without the environment variables set. So I think this one is ready to get merged.



---

archive/issue_comments_037528.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37528",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_037529.json:
```json
{
    "body": "Then all of the changes of #11021 will have to be rebased on this one...\n\nPerhaps easier the other way around. (Note that I still haven't updated the patches there though.)",
    "created_at": "2011-08-25T05:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37529",
    "user": "https://github.com/nexttime"
}
```

Then all of the changes of #11021 will have to be rebased on this one...

Perhaps easier the other way around. (Note that I still haven't updated the patches there though.)



---

archive/issue_comments_037530.json:
```json
{
    "body": "By the way, regarding \"After applying, replace the bootstrap version of `sage-spkg` in `$SAGE_ROOT/spkg/base/` with the new version\": this is taken care of automatically by the `sage-sdist` script, if one is making a new source distribution.  You just have to make sure that the version in local/bin is up to date.",
    "created_at": "2011-09-09T22:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37530",
    "user": "https://github.com/jhpalmieri"
}
```

By the way, regarding "After applying, replace the bootstrap version of `sage-spkg` in `$SAGE_ROOT/spkg/base/` with the new version": this is taken care of automatically by the `sage-sdist` script, if one is making a new source distribution.  You just have to make sure that the version in local/bin is up to date.



---

archive/issue_comments_037531.json:
```json
{
    "body": "Replying to [comment:27 jhpalmieri]:\n> By the way, regarding \"After applying, replace the bootstrap version of `sage-spkg` in `$SAGE_ROOT/spkg/base/` with the new version\": this is taken care of automatically by the `sage-sdist` script, if one is making a new source distribution.  You just have to make sure that the version in local/bin is up to date.\n\nYep.\n\nHope you don't mind me temporarily moving this to \"sage-pending\"; I intend to finish #11021 and rebase the patch(es) here on that, the latter presumably much easier than the other way around.\n\nIf I don't find the time, I'll set the milestone back to 4.7.2 of course.",
    "created_at": "2011-09-09T22:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37531",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:27 jhpalmieri]:
> By the way, regarding "After applying, replace the bootstrap version of `sage-spkg` in `$SAGE_ROOT/spkg/base/` with the new version": this is taken care of automatically by the `sage-sdist` script, if one is making a new source distribution.  You just have to make sure that the version in local/bin is up to date.

Yep.

Hope you don't mind me temporarily moving this to "sage-pending"; I intend to finish #11021 and rebase the patch(es) here on that, the latter presumably much easier than the other way around.

If I don't find the time, I'll set the milestone back to 4.7.2 of course.



---

archive/issue_comments_037532.json:
```json
{
    "body": "See also #329 which touches sage-spkg, although not in a very complicated way.",
    "created_at": "2011-09-10T01:35:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37532",
    "user": "https://github.com/jhpalmieri"
}
```

See also #329 which touches sage-spkg, although not in a very complicated way.



---

archive/issue_comments_037533.json:
```json
{
    "body": "Is there any update to this?  It has been several months since the last update, and some of us are eagerly anticipating this. :)",
    "created_at": "2012-01-22T21:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37533",
    "user": "https://github.com/swenson"
}
```

Is there any update to this?  It has been several months since the last update, and some of us are eagerly anticipating this. :)



---

archive/issue_comments_037534.json:
```json
{
    "body": "I've rebased this to Sage 5.0.beta1.  It had a positive review already, so I'm leaving it that way.",
    "created_at": "2012-01-23T15:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37534",
    "user": "https://github.com/jhpalmieri"
}
```

I've rebased this to Sage 5.0.beta1.  It had a positive review already, so I'm leaving it that way.



---

archive/issue_comments_037535.json:
```json
{
    "body": "Attachment [trac_4949-root.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root.patch) by @jhpalmieri created at 2012-01-23 15:49:45\n\nroot repo",
    "created_at": "2012-01-23T15:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37535",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-root.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root.patch) by @jhpalmieri created at 2012-01-23 15:49:45

root repo



---

archive/issue_comments_037536.json:
```json
{
    "body": "Do we *really* want\n\n```\nBUILD=build\n```\n\n?\n\nI think we have too many variables already.\n\nAlso, why introduce a new variable `$BUILD_DIR` instead of using `$SAGE_BUILD_TMPDIR`?",
    "created_at": "2012-01-23T16:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37536",
    "user": "https://github.com/jdemeyer"
}
```

Do we *really* want

```
BUILD=build
```

?

I think we have too many variables already.

Also, why introduce a new variable `$BUILD_DIR` instead of using `$SAGE_BUILD_TMPDIR`?



---

archive/issue_comments_037537.json:
```json
{
    "body": "Replying to [comment:32 jdemeyer]:\n> Do we *really* want\n {{{\n BUILD=build\n }}}\n> ?\n\nI don't see a reason for it, it was there before.  Should I create a new patch which removes it?  I think that would fix one or two of the issues from #11021.\n\n> Also, why introduce a new variable `$BUILD_DIR` instead of using `$SAGE_BUILD_TMPDIR`?\n\nThe code says, roughly\n\n```\nif $SAGE_BUILD_TMPDIR is not empty and points to an existing directory:\n    BUILD_DIR=$SAGE_BUILD_TMPDIR\nelse\n    BUILD_DIR=$SAGE_PACKAGES\nfi\n\nbuild Sage in $BUILD_DIR\n```\n",
    "created_at": "2012-01-23T18:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37537",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:32 jdemeyer]:
> Do we *really* want
 {{{
 BUILD=build
 }}}
> ?

I don't see a reason for it, it was there before.  Should I create a new patch which removes it?  I think that would fix one or two of the issues from #11021.

> Also, why introduce a new variable `$BUILD_DIR` instead of using `$SAGE_BUILD_TMPDIR`?

The code says, roughly

```
if $SAGE_BUILD_TMPDIR is not empty and points to an existing directory:
    BUILD_DIR=$SAGE_BUILD_TMPDIR
else
    BUILD_DIR=$SAGE_PACKAGES
fi

build Sage in $BUILD_DIR
```




---

archive/issue_comments_037538.json:
```json
{
    "body": "But why not simplify this to:\n\n```\nif $SAGE_BUILD_TMPDIR is not empty:\n    sanity check $SAGE_BUILD_TMPDIR but don't change any variables\nelse\n    SAGE_BUILD_TMPDIR=$SAGE_PACKAGES\nfi\n\nbuild Sage in $SAGE_BUILD_TMPDIR\n```\n",
    "created_at": "2012-01-23T18:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37538",
    "user": "https://github.com/jdemeyer"
}
```

But why not simplify this to:

```
if $SAGE_BUILD_TMPDIR is not empty:
    sanity check $SAGE_BUILD_TMPDIR but don't change any variables
else
    SAGE_BUILD_TMPDIR=$SAGE_PACKAGES
fi

build Sage in $SAGE_BUILD_TMPDIR
```




---

archive/issue_comments_037539.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-01-23T18:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37539",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_037540.json:
```json
{
    "body": "Concerning `$BUILD`: it existed before, but was almost not used.  If the variable serves no purpose and is not meant to be customized, it is cleaner to delete it.",
    "created_at": "2012-01-23T18:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37540",
    "user": "https://github.com/jdemeyer"
}
```

Concerning `$BUILD`: it existed before, but was almost not used.  If the variable serves no purpose and is not meant to be customized, it is cleaner to delete it.



---

archive/issue_comments_037541.json:
```json
{
    "body": "Something else: do we really want to build in\n\n```\n$SAGE_BUILD_TMPDIR/build/atlas-3.8.4.p1/\n```\n\n\nI would find it more natural to build in\n\n```\n$SAGE_BUILD_TMPDIR/atlas-3.8.4.p1/\n```\n\n\nAnd therefore, let $SAGE_BUILD_TMPDIR by default be equal to\n\n```\n$SAGE_ROOT/spkg/build/\n```\n\n\nAnd perhaps drop the requirement for `$SAGE_BUILD_TMPDIR` to be an existing directory: just create it if needed.\n\n(This is just an idea: I don't have strong feelings about this)",
    "created_at": "2012-01-23T18:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37541",
    "user": "https://github.com/jdemeyer"
}
```

Something else: do we really want to build in

```
$SAGE_BUILD_TMPDIR/build/atlas-3.8.4.p1/
```


I would find it more natural to build in

```
$SAGE_BUILD_TMPDIR/atlas-3.8.4.p1/
```


And therefore, let $SAGE_BUILD_TMPDIR by default be equal to

```
$SAGE_ROOT/spkg/build/
```


And perhaps drop the requirement for `$SAGE_BUILD_TMPDIR` to be an existing directory: just create it if needed.

(This is just an idea: I don't have strong feelings about this)



---

archive/issue_comments_037542.json:
```json
{
    "body": "If you run \"sage -i blah\"  and \"blah\" is an optional spkg which needs to be downloaded, would it make more sense to save the spkg in $SAGE_ROOT/spkg/optional/ or in $SAGE_BUILD_TMPDIR/optional? The previous versions of the patch do the second of these, but I think it makes more sense to do the first: downloading spkg files for optional packages is not the same as building, so setting SAGE_BUILD_TMPDIR shouldn't cause the spkg files to end up somewhere nonstandard.  Another way to say it: I don't view downloaded spkg files for optional spkgs as temporary, the way build directories are.\n\nHere's a new patch.  I've removed the variables \"BUILD\" and \"BUILD_DIR\", and I've appended \"build\" to the setting of \"$SAGE_BUILD_TMPDIR\".  I still check whether `$SAGE_BUILD_TMPDIR` exists, as a safeguard against typos, for example.  Optional spkgs are kept in `$SAGE_PACKAGES/optional` regardless of the setting of `$SAGE_BUILD_TMPDIR.`",
    "created_at": "2012-01-23T23:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37542",
    "user": "https://github.com/jhpalmieri"
}
```

If you run "sage -i blah"  and "blah" is an optional spkg which needs to be downloaded, would it make more sense to save the spkg in $SAGE_ROOT/spkg/optional/ or in $SAGE_BUILD_TMPDIR/optional? The previous versions of the patch do the second of these, but I think it makes more sense to do the first: downloading spkg files for optional packages is not the same as building, so setting SAGE_BUILD_TMPDIR shouldn't cause the spkg files to end up somewhere nonstandard.  Another way to say it: I don't view downloaded spkg files for optional spkgs as temporary, the way build directories are.

Here's a new patch.  I've removed the variables "BUILD" and "BUILD_DIR", and I've appended "build" to the setting of "$SAGE_BUILD_TMPDIR".  I still check whether `$SAGE_BUILD_TMPDIR` exists, as a safeguard against typos, for example.  Optional spkgs are kept in `$SAGE_PACKAGES/optional` regardless of the setting of `$SAGE_BUILD_TMPDIR.`



---

archive/issue_comments_037543.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-01-23T23:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37543",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_037544.json:
```json
{
    "body": "Attachment [trac_4949-root.v2.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root.v2.patch) by @jhpalmieri created at 2012-01-23 23:13:37\n\nroot repo",
    "created_at": "2012-01-23T23:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37544",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-root.v2.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root.v2.patch) by @jhpalmieri created at 2012-01-23 23:13:37

root repo



---

archive/issue_comments_037545.json:
```json
{
    "body": "`make clean` does not clean ` $SAGE_BUILD_TMPDIR `...\n\nI would also like ` $SAGE_BUILD_TMPDIR ` to be created if it does not exist, but I can live without.",
    "created_at": "2012-02-10T10:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37545",
    "user": "https://github.com/ohanar"
}
```

`make clean` does not clean ` $SAGE_BUILD_TMPDIR `...

I would also like ` $SAGE_BUILD_TMPDIR ` to be created if it does not exist, but I can live without.



---

archive/issue_comments_037546.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-02-10T10:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37546",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_037547.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-10T22:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37547",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_037548.json:
```json
{
    "body": "Okay, here are new patches.  `make clean` and `make distclean` now clean `$SAGE_BUILD_TMPDIR`, and in sage-spkg, if the directory doesn't exist, it is created.  The documentation has been changed to reflect this.  (The \"delta\" patches are the differences between the old versions and the new ones, for reference.)",
    "created_at": "2012-02-10T22:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37548",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, here are new patches.  `make clean` and `make distclean` now clean `$SAGE_BUILD_TMPDIR`, and in sage-spkg, if the directory doesn't exist, it is created.  The documentation has been changed to reflect this.  (The "delta" patches are the differences between the old versions and the new ones, for reference.)



---

archive/issue_comments_037549.json:
```json
{
    "body": "root repo",
    "created_at": "2012-02-10T22:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37549",
    "user": "https://github.com/jhpalmieri"
}
```

root repo



---

archive/issue_comments_037550.json:
```json
{
    "body": "Attachment [trac_4949-root.v3.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root.v3.patch) by @jhpalmieri created at 2012-02-10 22:38:12\n\nroot repo: diff between v2 and v3",
    "created_at": "2012-02-10T22:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37550",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-root.v3.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root.v3.patch) by @jhpalmieri created at 2012-02-10 22:38:12

root repo: diff between v2 and v3



---

archive/issue_comments_037551.json:
```json
{
    "body": "Attachment [trac_4949-root-delta2to3.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root-delta2to3.patch) by @jhpalmieri created at 2012-02-10 22:38:33\n\nsage repo: update installation guide",
    "created_at": "2012-02-10T22:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37551",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-root-delta2to3.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root-delta2to3.patch) by @jhpalmieri created at 2012-02-10 22:38:33

sage repo: update installation guide



---

archive/issue_comments_037552.json:
```json
{
    "body": "Attachment [trac_4949-installation-delta1to2.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-installation-delta1to2.patch) by @jhpalmieri created at 2012-02-10 22:38:52\n\nsage repo: diff between original and v2",
    "created_at": "2012-02-10T22:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37552",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-installation-delta1to2.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-installation-delta1to2.patch) by @jhpalmieri created at 2012-02-10 22:38:52

sage repo: diff between original and v2



---

archive/issue_comments_037553.json:
```json
{
    "body": "Replying to [comment:37 jhpalmieri]:\n> Optional spkgs are kept in `$SAGE_PACKAGES/optional` regardless of the setting of `$SAGE_BUILD_TMPDIR.`\nI totally agree on this.",
    "created_at": "2012-02-12T12:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37553",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:37 jhpalmieri]:
> Optional spkgs are kept in `$SAGE_PACKAGES/optional` regardless of the setting of `$SAGE_BUILD_TMPDIR.`
I totally agree on this.



---

archive/issue_comments_037554.json:
```json
{
    "body": "Replying to [comment:37 jhpalmieri]:\n> I've appended \"build\" to the setting of \"$SAGE_BUILD_TMPDIR\".\n\nI ask you again: why???",
    "created_at": "2012-02-12T12:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37554",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:37 jhpalmieri]:
> I've appended "build" to the setting of "$SAGE_BUILD_TMPDIR".

I ask you again: why???



---

archive/issue_comments_037555.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2012-02-12T12:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37555",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_037556.json:
```json
{
    "body": "Replying to [comment:41 jdemeyer]:\n> Replying to [comment:37 jhpalmieri]:\n> > I've appended \"build\" to the setting of \"$SAGE_BUILD_TMPDIR\".\n> \n> I ask you again: why???\n\nIt feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.  It's easier to clean up by hand, and `make clean` is easier to implement this way; otherwise, I suppose it would have to delete `/tmp/atlas-3.8.4.p1/`, `/tmp/blas-...`, etc.  Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should \"Also delete files in other directories if they are created by this makefile.\"",
    "created_at": "2012-02-12T16:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37556",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:41 jdemeyer]:
> Replying to [comment:37 jhpalmieri]:
> > I've appended "build" to the setting of "$SAGE_BUILD_TMPDIR".
> 
> I ask you again: why???

It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.  It's easier to clean up by hand, and `make clean` is easier to implement this way; otherwise, I suppose it would have to delete `/tmp/atlas-3.8.4.p1/`, `/tmp/blas-...`, etc.  Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should "Also delete files in other directories if they are created by this makefile."



---

archive/issue_comments_037557.json:
```json
{
    "body": "Replying to [comment:42 jhpalmieri]:\n> Replying to [comment:41 jdemeyer]:\n> > Replying to [comment:37 jhpalmieri]:\n> > > I've appended \"build\" to the setting of \"$SAGE_BUILD_TMPDIR\".\n> > \n> > I ask you again: why???\n> \n> It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.\nMy opinion is that the user should set `SAGE_BUILD_TMPDIR=/tmp/build` if that's what he wants.\n\n> Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should \"Also delete files in other directories if they are created by this makefile.\"  \nI think it does make sense if `make clean` would always clean `$SAGE_ROOT/spkg/build` and not `SAGE_BUILD_TMPDIR`.\n\nAnyway: I don't want to fight over this.  I'm happy with whatever the outcome.  The last thing I want is that this ticket gets abandoned.",
    "created_at": "2012-02-14T09:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37557",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:42 jhpalmieri]:
> Replying to [comment:41 jdemeyer]:
> > Replying to [comment:37 jhpalmieri]:
> > > I've appended "build" to the setting of "$SAGE_BUILD_TMPDIR".
> > 
> > I ask you again: why???
> 
> It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.
My opinion is that the user should set `SAGE_BUILD_TMPDIR=/tmp/build` if that's what he wants.

> Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should "Also delete files in other directories if they are created by this makefile."  
I think it does make sense if `make clean` would always clean `$SAGE_ROOT/spkg/build` and not `SAGE_BUILD_TMPDIR`.

Anyway: I don't want to fight over this.  I'm happy with whatever the outcome.  The last thing I want is that this ticket gets abandoned.



---

archive/issue_comments_037558.json:
```json
{
    "body": "One other small thing: I would prefer the directory `build/old` to be created only when needed: replace the line\n\n```\nmkdir -p \"$SAGE_BUILD_TMPDIR/build/old\"\n```\n\nby\n\n```\nmkdir -p \"$SAGE_BUILD_TMPDIR/build\"\n```\n\n(and change the error message below)\n\nAnd also replace\n\n```\n\n    mv -f \"$PKG_BASE-\"* old/  2>/dev/null\n```\n\nby\n\n```\n    mkdir -p old\n    if [ $? -ne 0 ]; then\n        echo >&2 \"Error creating directory $SAGE_BUILD_TMPDIR/old.\"\n        exit 1\n    fi\n    mv -f \"$PKG_BASE-\"* old/\n```\n",
    "created_at": "2012-02-14T09:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37558",
    "user": "https://github.com/jdemeyer"
}
```

One other small thing: I would prefer the directory `build/old` to be created only when needed: replace the line

```
mkdir -p "$SAGE_BUILD_TMPDIR/build/old"
```

by

```
mkdir -p "$SAGE_BUILD_TMPDIR/build"
```

(and change the error message below)

And also replace

```

    mv -f "$PKG_BASE-"* old/  2>/dev/null
```

by

```
    mkdir -p old
    if [ $? -ne 0 ]; then
        echo >&2 "Error creating directory $SAGE_BUILD_TMPDIR/old."
        exit 1
    fi
    mv -f "$PKG_BASE-"* old/
```




---

archive/issue_comments_037559.json:
```json
{
    "body": "If you really want to go with the \"build\" subdirectory, I would prefer appending it immediately:\n\n```\nif [ -n \"$SAGE_BUILD_TMPDIR\" ]; then\n    SAGE_BUILD_TMPDIR=\"$SAGE_BUILD_TMPDIR/build\"\n    if [ ! -d \"$SAGE_BUILD_TMPDIR\" ]; then\n        echo \"Creating directory \\$SAGE_BUILD_TMPDIR (=$SAGE_BUILD_TMPDIR).\"\n        mkdir -p \"$SAGE_BUILD_TMPDIR\"\n    fi\n    echo \"Building in $SAGE_BUILD_TMPDIR.\"\nelse\n    SAGE_BUILD_TMPDIR=\"$SAGE_PACKAGES/build\"\nfi\n```\n\n(Actually, the whole `if [ ! -d ] ... fi` block can be removed).",
    "created_at": "2012-02-14T09:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37559",
    "user": "https://github.com/jdemeyer"
}
```

If you really want to go with the "build" subdirectory, I would prefer appending it immediately:

```
if [ -n "$SAGE_BUILD_TMPDIR" ]; then
    SAGE_BUILD_TMPDIR="$SAGE_BUILD_TMPDIR/build"
    if [ ! -d "$SAGE_BUILD_TMPDIR" ]; then
        echo "Creating directory \$SAGE_BUILD_TMPDIR (=$SAGE_BUILD_TMPDIR)."
        mkdir -p "$SAGE_BUILD_TMPDIR"
    fi
    echo "Building in $SAGE_BUILD_TMPDIR."
else
    SAGE_BUILD_TMPDIR="$SAGE_PACKAGES/build"
fi
```

(Actually, the whole `if [ ! -d ] ... fi` block can be removed).



---

archive/issue_comments_037560.json:
```json
{
    "body": "Replying to [comment:42 jhpalmieri]:\n> Replying to [comment:41 jdemeyer]:\n> > I ask you again: why???\n> \n> It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.  It's easier to clean up by hand, and `make clean` is easier to implement this way; otherwise, I suppose it would have to delete `/tmp/atlas-3.8.4.p1/`, `/tmp/blas-...`, etc.  Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should \"Also delete files in other directories if they are created by this makefile.\"  \n\nJohn, \n\nhow do you avoid a possible race condition if two or more instances of Sage (or some other program), want to use /tmp/build? Perhaps /tmp/$user-sage-$SageVersion.$$ might be better. Someone can then find their own Sage-related files easily (for example \n\n\n```\nrm -rf /tmp/drkirkby-sage-4.5.6*\n```\n\nwithout risk of their being any race condition. \n\n\nDave",
    "created_at": "2012-02-14T22:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37560",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:42 jhpalmieri]:
> Replying to [comment:41 jdemeyer]:
> > I ask you again: why???
> 
> It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.  It's easier to clean up by hand, and `make clean` is easier to implement this way; otherwise, I suppose it would have to delete `/tmp/atlas-3.8.4.p1/`, `/tmp/blas-...`, etc.  Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should "Also delete files in other directories if they are created by this makefile."  

John, 

how do you avoid a possible race condition if two or more instances of Sage (or some other program), want to use /tmp/build? Perhaps /tmp/$user-sage-$SageVersion.$$ might be better. Someone can then find their own Sage-related files easily (for example 


```
rm -rf /tmp/drkirkby-sage-4.5.6*
```

without risk of their being any race condition. 


Dave



---

archive/issue_comments_037561.json:
```json
{
    "body": "Replying to [comment:47 drkirkby]:\n> Replying to [comment:42 jhpalmieri]:\n> > Replying to [comment:41 jdemeyer]:\n> > > I ask you again: why???\n> > \n> > It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.  It's easier to clean up by hand, and `make clean` is easier to implement this way; otherwise, I suppose it would have to delete `/tmp/atlas-3.8.4.p1/`, `/tmp/blas-...`, etc.  Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should \"Also delete files in other directories if they are created by this makefile.\"  \n> \n> John, \n> \n> how do you avoid a possible race condition if two or more instances of Sage (or some other program), want to use /tmp/build? \n\nI don't.  If someone wants to set `$SAGE_BUILD_TMPDIR`, then I'm making it their responsibility to make sure that the directory is available and in good shape.  (If someone does `export SAGE_BUILD_TMPDIR=/tmp/sage` and then we mangle the file name somehow, I think that will lead to confusion much more often than it will help.  We could instead build in `SAGE_BUILD_TMPDIR/subdir` where we choose `subdir` to avoid race conditions.  But I'm not going to do that.)\n\nMeanwhile, I have new versions of the patches.  I'm going to give in on the \"build\" subdirectory: Sage will now build in `SAGE_BUILD_TMPDIR`.  Oh, and I changed the name to `SAGE_BUILD_DIR` instead; I think that name makes more sense.  I also patched bzip2 and prereq so they build in `SAGE_BUILD_DIR` as well \u2014 easy to do now that the base repo has been merged with the root repo.  `make clean` no longer touches `SAGE_BUILD_DIR`, nor does `make distclean`.  (Also, `make clean` no longer recreates `spkg/build` or `spkg/archive` \u2014 what's that directory for, anyway?).\n\nI updated the documentation accordingly.",
    "created_at": "2012-02-14T23:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37561",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:47 drkirkby]:
> Replying to [comment:42 jhpalmieri]:
> > Replying to [comment:41 jdemeyer]:
> > > I ask you again: why???
> > 
> > It feels cleaner to me: if I set `$SAGE_BUILD_TMPDIR=/tmp`, then rather than producing many subdirectories of `tmp`, everything will live in `/tmp/build`.  It's easier to clean up by hand, and `make clean` is easier to implement this way; otherwise, I suppose it would have to delete `/tmp/atlas-3.8.4.p1/`, `/tmp/blas-...`, etc.  Or `make clean` could not modify SAGE_BUILD_TMPDIR at all, but the Make manual suggests that `make clean` (and `make distclean`) should "Also delete files in other directories if they are created by this makefile."  
> 
> John, 
> 
> how do you avoid a possible race condition if two or more instances of Sage (or some other program), want to use /tmp/build? 

I don't.  If someone wants to set `$SAGE_BUILD_TMPDIR`, then I'm making it their responsibility to make sure that the directory is available and in good shape.  (If someone does `export SAGE_BUILD_TMPDIR=/tmp/sage` and then we mangle the file name somehow, I think that will lead to confusion much more often than it will help.  We could instead build in `SAGE_BUILD_TMPDIR/subdir` where we choose `subdir` to avoid race conditions.  But I'm not going to do that.)

Meanwhile, I have new versions of the patches.  I'm going to give in on the "build" subdirectory: Sage will now build in `SAGE_BUILD_TMPDIR`.  Oh, and I changed the name to `SAGE_BUILD_DIR` instead; I think that name makes more sense.  I also patched bzip2 and prereq so they build in `SAGE_BUILD_DIR` as well — easy to do now that the base repo has been merged with the root repo.  `make clean` no longer touches `SAGE_BUILD_DIR`, nor does `make distclean`.  (Also, `make clean` no longer recreates `spkg/build` or `spkg/archive` — what's that directory for, anyway?).

I updated the documentation accordingly.



---

archive/issue_comments_037562.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-02-14T23:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37562",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_037563.json:
```json
{
    "body": "installation guide: diff between v2 and v3",
    "created_at": "2012-02-14T23:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37563",
    "user": "https://github.com/jhpalmieri"
}
```

installation guide: diff between v2 and v3



---

archive/issue_comments_037564.json:
```json
{
    "body": "Attachment [trac_4949-installation-delta2to3.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-installation-delta2to3.patch) by @jhpalmieri created at 2012-02-14 23:20:44\n\nsage repo: update installation guide",
    "created_at": "2012-02-14T23:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37564",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-installation-delta2to3.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-installation-delta2to3.patch) by @jhpalmieri created at 2012-02-14 23:20:44

sage repo: update installation guide



---

archive/issue_comments_037565.json:
```json
{
    "body": "Attachment [trac_4949-installation.v3.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-installation.v3.patch) by @jhpalmieri created at 2012-02-14 23:21:02\n\nroot repo: diff between v3 and v4",
    "created_at": "2012-02-14T23:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37565",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-installation.v3.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-installation.v3.patch) by @jhpalmieri created at 2012-02-14 23:21:02

root repo: diff between v3 and v4



---

archive/issue_comments_037566.json:
```json
{
    "body": "Attachment [trac_4949-root-delta3to4.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root-delta3to4.patch) by @jhpalmieri created at 2012-02-14 23:21:11\n\nroot repo",
    "created_at": "2012-02-14T23:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37566",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-root-delta3to4.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root-delta3to4.patch) by @jhpalmieri created at 2012-02-14 23:21:11

root repo



---

archive/issue_comments_037567.json:
```json
{
    "body": "Attachment [trac_4949-root.v4.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root.v4.patch) by @jhpalmieri created at 2012-02-14 23:21:36",
    "created_at": "2012-02-14T23:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37567",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-root.v4.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root.v4.patch) by @jhpalmieri created at 2012-02-14 23:21:36



---

archive/issue_comments_037568.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-02-15T08:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37568",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_037569.json:
```json
{
    "body": "Lines 210 and 216 of `sage-spkg`: you have twice cd \"$SAGE_BUILD_DIR\".  Remove the second and move the check (line 219) up, after the first cd.  You probably want to \"exit 1\" if cd fails.\n\nLine 227 of `sage-spkg`: replace\n\n```\nif [ -e \"$dir\" ]; then\n```\n\nby\n\n```\nif [ -d \"$dir\" ]; then\n```\n",
    "created_at": "2012-02-15T08:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37569",
    "user": "https://github.com/jdemeyer"
}
```

Lines 210 and 216 of `sage-spkg`: you have twice cd "$SAGE_BUILD_DIR".  Remove the second and move the check (line 219) up, after the first cd.  You probably want to "exit 1" if cd fails.

Line 227 of `sage-spkg`: replace

```
if [ -e "$dir" ]; then
```

by

```
if [ -d "$dir" ]; then
```




---

archive/issue_comments_037570.json:
```json
{
    "body": "Line 235: why \"mv -f\" and not simply \"mv\"?",
    "created_at": "2012-02-15T09:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37570",
    "user": "https://github.com/jdemeyer"
}
```

Line 235: why "mv -f" and not simply "mv"?



---

archive/issue_comments_037571.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-15T18:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37571",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_037572.json:
```json
{
    "body": "Replying to [comment:50 jdemeyer]:\n> Lines 210 and 216 of `sage-spkg`: you have twice cd \"$SAGE_BUILD_DIR\".  Remove the second and move the check (line 219) up, after the first cd.  You probably want to \"exit 1\" if cd fails.\n\nWell, the old version had a second 'cd' command, justified by the comment\n\n```\n# Make triply sure that we are in the build directory before doing  \n# a scary \"rm -rf\"\n```\n\nSo I left the second one in.  You think I should change this?  In any case, you're right about the \"exit 1\".\n\n> Line 227 of `sage-spkg`: replace\n\n```\nif [ -e \"$dir\" ]; then\n```\n\n> by\n\n```\nif [ -d \"$dir\" ]; then\n```\n\n\nOn the off-chance that there is a file (not a directory) in the build directory with the wrong name, shouldn't we move it, too?\n\nReplying to [comment:51 jdemeyer]:\n> Line 235: why \"mv -f\" and not simply \"mv\"?\n\nLeft over from the previous version. I can fix that.",
    "created_at": "2012-02-15T18:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37572",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:50 jdemeyer]:
> Lines 210 and 216 of `sage-spkg`: you have twice cd "$SAGE_BUILD_DIR".  Remove the second and move the check (line 219) up, after the first cd.  You probably want to "exit 1" if cd fails.

Well, the old version had a second 'cd' command, justified by the comment

```
# Make triply sure that we are in the build directory before doing  
# a scary "rm -rf"
```

So I left the second one in.  You think I should change this?  In any case, you're right about the "exit 1".

> Line 227 of `sage-spkg`: replace

```
if [ -e "$dir" ]; then
```

> by

```
if [ -d "$dir" ]; then
```


On the off-chance that there is a file (not a directory) in the build directory with the wrong name, shouldn't we move it, too?

Replying to [comment:51 jdemeyer]:
> Line 235: why "mv -f" and not simply "mv"?

Left over from the previous version. I can fix that.



---

archive/issue_comments_037573.json:
```json
{
    "body": "Attachment [trac_4949-root-delta4to5.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root-delta4to5.patch) by @jhpalmieri created at 2012-02-15 18:09:24",
    "created_at": "2012-02-15T18:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37573",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-root-delta4to5.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root-delta4to5.patch) by @jhpalmieri created at 2012-02-15 18:09:24



---

archive/issue_comments_037574.json:
```json
{
    "body": "Attachment [trac_4949-root.v5.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root.v5.patch) by @jhpalmieri created at 2012-02-15 18:09:37",
    "created_at": "2012-02-15T18:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37574",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_4949-root.v5.patch](tarball://root/attachments/some-uuid/ticket4949/trac_4949-root.v5.patch) by @jhpalmieri created at 2012-02-15 18:09:37



---

archive/issue_comments_037575.json:
```json
{
    "body": "Attachment [4949_review.patch](tarball://root/attachments/some-uuid/ticket4949/4949_review.patch) by @jdemeyer created at 2012-02-15 18:39:01",
    "created_at": "2012-02-15T18:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37575",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [4949_review.patch](tarball://root/attachments/some-uuid/ticket4949/4949_review.patch) by @jdemeyer created at 2012-02-15 18:39:01



---

archive/issue_comments_037576.json:
```json
{
    "body": "The review patch looks okay to me.",
    "created_at": "2012-02-15T21:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37576",
    "user": "https://github.com/jhpalmieri"
}
```

The review patch looks okay to me.



---

archive/issue_comments_037577.json:
```json
{
    "body": "Looks good to me too.",
    "created_at": "2012-02-16T21:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37577",
    "user": "https://github.com/jdemeyer"
}
```

Looks good to me too.



---

archive/issue_comments_037578.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-16T21:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37578",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_037579.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-22T10:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37579",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_037580.json:
```json
{
    "body": "See #12637 for a followup.",
    "created_at": "2012-03-06T19:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4949#issuecomment-37580",
    "user": "https://github.com/jhpalmieri"
}
```

See #12637 for a followup.
