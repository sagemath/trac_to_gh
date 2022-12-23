# Issue 9475: update M4RI to newest upstream release

archive/issues_009475.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mariah\n\nKeywords: M4RI, spkg-check\n\nThe new version improves elimination to some extend, comes with a cleaner API and has an option to suppress SSE instructions\n\nIssue created by migration from https://trac.sagemath.org/ticket/9475\n\n",
    "created_at": "2010-07-11T16:12:22Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "update M4RI to newest upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9475",
    "user": "malb"
}
```
Assignee: tbd

CC:  mariah

Keywords: M4RI, spkg-check

The new version improves elimination to some extend, comes with a cleaner API and has an option to suppress SSE instructions

Issue created by migration from https://trac.sagemath.org/ticket/9475





---

archive/issue_comments_090894.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-11T16:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90894",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090895.json:
```json
{
    "body": "I've uploaded an SPKG to\n\n  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.spkg\n\nThis SPKG also takes care of #9381 (SAGE_FAT_BINARY not being respected) and the M4RI part of #9281 (spkg-check)",
    "created_at": "2010-07-11T16:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90895",
    "user": "malb"
}
```

I've uploaded an SPKG to

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.spkg

This SPKG also takes care of #9381 (SAGE_FAT_BINARY not being respected) and the M4RI part of #9281 (spkg-check)



---

archive/issue_comments_090896.json:
```json
{
    "body": "I've run the M4RI self test (not the Sage test suite) on the following machines:\n\n* x86_64 Linux (Xeon, sage.math and eno);\n\n* x86 OSX (Xeon, bsd);\u00a0\n\n* ia64 Linux (iras); \n\n* UltraSPARC T2 Solaris using GCC (t2.math.washington.edu) \n\n* x86 Linux (VirtualBox);",
    "created_at": "2010-07-11T20:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90896",
    "user": "malb"
}
```

I've run the M4RI self test (not the Sage test suite) on the following machines:

* x86_64 Linux (Xeon, sage.math and eno);

* x86 OSX (Xeon, bsd); 

* ia64 Linux (iras); 

* UltraSPARC T2 Solaris using GCC (t2.math.washington.edu) 

* x86 Linux (VirtualBox);



---

archive/issue_comments_090897.json:
```json
{
    "body": "1. SPKG.txt under \"Releases\" says latest \nrelease is libm4ri-20100107, do you mean\nlibm4ri-20100701?\n\n2. Since spkg-check exists, in spkg-install \nthe commented out lines:\n\n\n```\n# $MAKE check\n# if [ $? -ne 0 ]; then\n#     echo \"libm4ri testsuite failed, please report upstream!\"\n#     exit 1\n# fi\n```\n\n\ncan be removed.\n\n3. In spkg-install, if SAGE_FAT_BINARY is yes, then\nsse2 is disabled.  What about sse3 as was the reported\nproblem in [#9381](http://trac.sagemath.org/sage_trac/ticket/9381)\n\n4. This version of libm4ri does not appear under the\ndownloads on the [m4ri](http://m4ri.sagemath.org) web site,\nthus no way to tell if the source in the spkg corresponds\nto the source under the claimed version.",
    "created_at": "2010-07-13T15:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90897",
    "user": "mariah"
}
```

1. SPKG.txt under "Releases" says latest 
release is libm4ri-20100107, do you mean
libm4ri-20100701?

2. Since spkg-check exists, in spkg-install 
the commented out lines:


```
# $MAKE check
# if [ $? -ne 0 ]; then
#     echo "libm4ri testsuite failed, please report upstream!"
#     exit 1
# fi
```


can be removed.

3. In spkg-install, if SAGE_FAT_BINARY is yes, then
sse2 is disabled.  What about sse3 as was the reported
problem in [#9381](http://trac.sagemath.org/sage_trac/ticket/9381)

4. This version of libm4ri does not appear under the
downloads on the [m4ri](http://m4ri.sagemath.org) web site,
thus no way to tell if the source in the spkg corresponds
to the source under the claimed version.



---

archive/issue_comments_090898.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-13T15:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90898",
    "user": "mariah"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090899.json:
```json
{
    "body": "Replying to [comment:3 mariah]:\n\n> 1. SPKG.txt under \"Releases\" says latest  release is libm4ri-20100107, do you mean libm4ri-20100701?\n\nFixed.\n\n> 2. Since spkg-check exists, in spkg-install\u00a0 the commented out lines: ` # $MAKE check # if [ $? -ne 0 ]; then #     echo \"libm4ri testsuite failed, please report upstream!\" #     exit 1 # fi ` can be removed.\n\nFixed.\n\n> 3. In spkg-install, if SAGE_FAT_BINARY is yes, then sse2 is disabled.  What about sse3 as was the reported problem in [#9381](http://trac.sagemath.org/sage_trac/ticket/9381)\n\nWe never use SSE3, but yeah all checks for SSEx instructions are suppressed in that case.\n\n> 4. This version of libm4ri does not appear under the downloads on the [m4ri](http://m4ri.sagemath.org) web site, thus no way to tell if the source in the spkg corresponds to the source under the claimed version.\n\nThis is because I am upstream and wanted to wait for portability issues before putting the release on the website. I'm putting it online now, if that makes your life easier.",
    "created_at": "2010-07-13T18:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90899",
    "user": "malb"
}
```

Replying to [comment:3 mariah]:

> 1. SPKG.txt under "Releases" says latest  release is libm4ri-20100107, do you mean libm4ri-20100701?

Fixed.

> 2. Since spkg-check exists, in spkg-install  the commented out lines: ` # $MAKE check # if [ $? -ne 0 ]; then #     echo "libm4ri testsuite failed, please report upstream!" #     exit 1 # fi ` can be removed.

Fixed.

> 3. In spkg-install, if SAGE_FAT_BINARY is yes, then sse2 is disabled.  What about sse3 as was the reported problem in [#9381](http://trac.sagemath.org/sage_trac/ticket/9381)

We never use SSE3, but yeah all checks for SSEx instructions are suppressed in that case.

> 4. This version of libm4ri does not appear under the downloads on the [m4ri](http://m4ri.sagemath.org) web site, thus no way to tell if the source in the spkg corresponds to the source under the claimed version.

This is because I am upstream and wanted to wait for portability issues before putting the release on the website. I'm putting it online now, if that makes your life easier.



---

archive/issue_comments_090900.json:
```json
{
    "body": "See\u00a0\n\nhttp://m4ri.sagemath.org\n\nand\n\nhttp://bitbucket.org/malb/m4ri/wiki/M4RI-20100701\u00a0 \n\nfor the new upstream release.",
    "created_at": "2010-07-13T18:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90900",
    "user": "malb"
}
```

See 

http://m4ri.sagemath.org

and

http://bitbucket.org/malb/m4ri/wiki/M4RI-20100701  

for the new upstream release.



---

archive/issue_comments_090901.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-13T18:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90901",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090902.json:
```json
{
    "body": "The changes to `SPKG.txt`, `spkg-install` and `spkg-check` are not checked in.",
    "created_at": "2010-07-14T13:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90902",
    "user": "leif"
}
```

The changes to `SPKG.txt`, `spkg-install` and `spkg-check` are not checked in.



---

archive/issue_comments_090903.json:
```json
{
    "body": "`SPKG.txt`:\n* *Author* should be *Author**s***\n* Is the given e-mail address still up-to-date?\n* I'd substitute *\"function names match what the function is doing now\"*\n  by *\"function names **now** match ... is doing\"*\n* s/supress/su**p**press/\n* s/SSE2 instruction/SSE2 instruction**s**/\n\n`spkg-install:`\n* Old typo, I guess: s/CLFAGS/CFLAGS/ twice\n* The choice of the variable name `SSE2_SUPPORT` isn't that nice; I'd rather call it `DISABLE_SSE2`, but never mind.\n\n`spkg-check:`\n* Uses `make` rather than `$MAKE` (in contrast to `spkg-install`), but shouldn't be a problem.",
    "created_at": "2010-07-14T14:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90903",
    "user": "leif"
}
```

`SPKG.txt`:
* *Author* should be *Author**s***
* Is the given e-mail address still up-to-date?
* I'd substitute *"function names match what the function is doing now"*
  by *"function names **now** match ... is doing"*
* s/supress/su**p**press/
* s/SSE2 instruction/SSE2 instruction**s**/

`spkg-install:`
* Old typo, I guess: s/CLFAGS/CFLAGS/ twice
* The choice of the variable name `SSE2_SUPPORT` isn't that nice; I'd rather call it `DISABLE_SSE2`, but never mind.

`spkg-check:`
* Uses `make` rather than `$MAKE` (in contrast to `spkg-install`), but shouldn't be a problem.



---

archive/issue_comments_090904.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-14T15:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90904",
    "user": "leif"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090905.json:
```json
{
    "body": "I'd suggest adding the (standard) section *Special Update/Build Instructions* to `SPKG.txt`, with the following:\n* Remove upstream Mercurial repository (directory `src/.hg`, file `src/.hgtags`)\n* Remove directory `src/autom4te.cache`, file `src/m4ri.vcproj`\n\nI've built a p1 spkg with the above mentioned files removed: 392KB vs. 1.2MB\n\nIf there are no dependencies on Sage packages (which is the case here), we don't need to add `$SAGE_LOCAL/include` to the preprocessor search path in `spkg-install` (`CFLAGS` and `CPPFLAGS`).\n\nPerhaps touch `src/configure`, because it has the same time stamp as `configure.*`.\n\nUpstream notes:\n* There is no target `clean`.\n* `src/NEWS` and `src/ChangeLog` are **empty** files. ;-)\n\nTests in progress,\n\nLeif",
    "created_at": "2010-07-14T15:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90905",
    "user": "leif"
}
```

I'd suggest adding the (standard) section *Special Update/Build Instructions* to `SPKG.txt`, with the following:
* Remove upstream Mercurial repository (directory `src/.hg`, file `src/.hgtags`)
* Remove directory `src/autom4te.cache`, file `src/m4ri.vcproj`

I've built a p1 spkg with the above mentioned files removed: 392KB vs. 1.2MB

If there are no dependencies on Sage packages (which is the case here), we don't need to add `$SAGE_LOCAL/include` to the preprocessor search path in `spkg-install` (`CFLAGS` and `CPPFLAGS`).

Perhaps touch `src/configure`, because it has the same time stamp as `configure.*`.

Upstream notes:
* There is no target `clean`.
* `src/NEWS` and `src/ChangeLog` are **empty** files. ;-)

Tests in progress,

Leif



---

archive/issue_comments_090906.json:
```json
{
    "body": "* Ubuntu 9.04 x86 (P4 Prescott, gcc 4.3.3) Sage 4.5.rc0 (with ECL 10.2.1.p1):\n\n   ptestlong: All tests passed.\n\n  * Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3) Sage 4.5.rc0:\n\n   ptestlong: All tests passed.\n   (with my stripped-down M4RI spkg, see above)\n\nI've only installed the new package (dated July 13th) and applied the patch, i.e. did not build Sage from scratch, and haven't (yet) run the testsuite.",
    "created_at": "2010-07-14T17:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90906",
    "user": "leif"
}
```

* Ubuntu 9.04 x86 (P4 Prescott, gcc 4.3.3) Sage 4.5.rc0 (with ECL 10.2.1.p1):

   ptestlong: All tests passed.

  * Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3) Sage 4.5.rc0:

   ptestlong: All tests passed.
   (with my stripped-down M4RI spkg, see above)

I've only installed the new package (dated July 13th) and applied the patch, i.e. did not build Sage from scratch, and haven't (yet) run the testsuite.



---

archive/issue_comments_090907.json:
```json
{
    "body": "Shame on me I missed that one:\n\n```sh\n./spkg-install: line 47: [x: command not found\n```\n\n\n```sh\nif [\"x$SAGE_FAT_BINARY\" = \"xyes\"]; then\n    SSE2_SUPPORT=\"--disable-sse2\"\nelse\n    SSE2_SUPPORT=\"\"\nfi\n```\n\nshould be\n\n```sh\nif [ \"x$SAGE_FAT_BINARY\" = \"xyes\" ]; then\n    ...\n```\n\nNote that `[` is actually a *command* (namely an alias for or link to `test`, depending on the shell), and `]` is its last parameter.\n\n----\n\nOn both of the above systems, the testsuite passed without errors.\n\n(I reinstalled the package(s) with `SAGE_CHECK=\"yes\"`.)",
    "created_at": "2010-07-14T18:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90907",
    "user": "leif"
}
```

Shame on me I missed that one:

```sh
./spkg-install: line 47: [x: command not found
```


```sh
if ["x$SAGE_FAT_BINARY" = "xyes"]; then
    SSE2_SUPPORT="--disable-sse2"
else
    SSE2_SUPPORT=""
fi
```

should be

```sh
if [ "x$SAGE_FAT_BINARY" = "xyes" ]; then
    ...
```

Note that `[` is actually a *command* (namely an alias for or link to `test`, depending on the shell), and `]` is its last parameter.

----

On both of the above systems, the testsuite passed without errors.

(I reinstalled the package(s) with `SAGE_CHECK="yes"`.)



---

archive/issue_comments_090908.json:
```json
{
    "body": "Just let me know if I should provide (a) reviewer patch(es) to the spkg (after a commit to the changes not yet checked in); I cannot upload an updated spkg to sage.math though.\n\nLeif",
    "created_at": "2010-07-14T19:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90908",
    "user": "leif"
}
```

Just let me know if I should provide (a) reviewer patch(es) to the spkg (after a commit to the changes not yet checked in); I cannot upload an updated spkg to sage.math though.

Leif



---

archive/issue_comments_090909.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n\n> * Remove upstream Mercurial repository (directory `src/.hg`, file `src/.hgtags`)\n> * Remove directory `src/autom4te.cache`, file `src/m4ri.vcproj`\n> I've built a p1 spkg with the above mentioned files removed: 392KB vs. 1.2MB\n\nIt's strange that there was an autom4te.cache, since I rm it in my release script. I'm okay with these changes.",
    "created_at": "2010-07-14T20:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90909",
    "user": "malb"
}
```

Replying to [comment:9 leif]:

> * Remove upstream Mercurial repository (directory `src/.hg`, file `src/.hgtags`)
> * Remove directory `src/autom4te.cache`, file `src/m4ri.vcproj`
> I've built a p1 spkg with the above mentioned files removed: 392KB vs. 1.2MB

It's strange that there was an autom4te.cache, since I rm it in my release script. I'm okay with these changes.



---

archive/issue_comments_090910.json:
```json
{
    "body": "Leif,\n\nI'd appreciate if you could update SPKG according to your suggestions, I'm okay with them all. If you upload the SPKG somewhere or send it my way I can upload it to sage.math.",
    "created_at": "2010-07-14T20:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90910",
    "user": "malb"
}
```

Leif,

I'd appreciate if you could update SPKG according to your suggestions, I'm okay with them all. If you upload the SPKG somewhere or send it my way I can upload it to sage.math.



---

archive/issue_comments_090911.json:
```json
{
    "body": "Replying to [comment:14 malb]:\n> I'd appreciate if you could update SPKG according to your suggestions, I'm okay with them all. If you upload the SPKG somewhere or send it my way I can upload it to sage.math.\u00a0\n\nOk, I'll create a cumulative spkg patch and a \"stripped-down\" p1 package in a few hours and then mail you both.\n\n(I assume your .ac.uk e-mail address in SPKG.txt is still appropriate as upstream contact.)\n  \n\nCurrently running stress-test builds of 4.5.rc1... ;-)\n\nLeif",
    "created_at": "2010-07-14T21:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90911",
    "user": "leif"
}
```

Replying to [comment:14 malb]:
> I'd appreciate if you could update SPKG according to your suggestions, I'm okay with them all. If you upload the SPKG somewhere or send it my way I can upload it to sage.math. 

Ok, I'll create a cumulative spkg patch and a "stripped-down" p1 package in a few hours and then mail you both.

(I assume your .ac.uk e-mail address in SPKG.txt is still appropriate as upstream contact.)
  

Currently running stress-test builds of 4.5.rc1... ;-)

Leif



---

archive/issue_comments_090912.json:
```json
{
    "body": "Yes, that's still current, however martinralbrecht`@` googleblablabla might be current for a longer time.\n\nThanks!",
    "created_at": "2010-07-14T21:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90912",
    "user": "malb"
}
```

Yes, that's still current, however martinralbrecht`@` googleblablabla might be current for a longer time.

Thanks!



---

archive/issue_comments_090913.json:
```json
{
    "body": "Attachment\n\nYou have to commit Martin's changes (\"p0\") first to apply this.",
    "created_at": "2010-07-16T02:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90913",
    "user": "leif"
}
```

Attachment

You have to commit Martin's changes ("p0") first to apply this.



---

archive/issue_comments_090914.json:
```json
{
    "body": "Patch for p1 Sage package is up. Remember to commit Martin's changes (of July 13th) first before you apply this patch. (This patch does *not* remove the unnecessary files in `src/` since they are not under *our* version control; they are of course deleted from the p1 spkg.)\n\n(Link to) **New libm4ri-20100701.p1.spkg is on the way.**\n\nTested with both 4.5.rc0 and rc1 (Ubuntu 9.04 x86_64).\n\nSorry for the delay.\n\n-Leif",
    "created_at": "2010-07-16T02:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90914",
    "user": "leif"
}
```

Patch for p1 Sage package is up. Remember to commit Martin's changes (of July 13th) first before you apply this patch. (This patch does *not* remove the unnecessary files in `src/` since they are not under *our* version control; they are of course deleted from the p1 spkg.)

(Link to) **New libm4ri-20100701.p1.spkg is on the way.**

Tested with both 4.5.rc0 and rc1 (Ubuntu 9.04 x86_64).

Sorry for the delay.

-Leif



---

archive/issue_comments_090915.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-16T02:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90915",
    "user": "leif"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_090916.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-16T09:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90916",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090917.json:
```json
{
    "body": "I uploaded Leif's SPKG to\u00a0\n\n\u00a0http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.p1.spkg\n\nand I give it a positive review.",
    "created_at": "2010-07-16T09:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90917",
    "user": "malb"
}
```

I uploaded Leif's SPKG to 

 http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.p1.spkg

and I give it a positive review.



---

archive/issue_comments_090918.json:
```json
{
    "body": "With a fresh build, sage doesn't start:\n\n```\nTraceback (most recent call last):\n File \"/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/bin/sage-eval\",\nline 4, in <module>\n   from sage.all import *\n File \"/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/all.py\",\nline 73, in <module>\n   from sage.matrix.all     import *\n File \"/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/all.py\",\nline 1, in <module>\n   from matrix_space import MatrixSpace, is_MatrixSpace\n File \"/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py\",\nline 40, in <module>\n   import matrix_mod2_dense\nImportError: /mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_mod2_dense.so:\nundefined symbol: mzd_lqup\nSage failed to startup.\n```\n",
    "created_at": "2010-07-18T20:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90918",
    "user": "rlm"
}
```

With a fresh build, sage doesn't start:

```
Traceback (most recent call last):
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/bin/sage-eval",
line 4, in <module>
   from sage.all import *
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/all.py",
line 73, in <module>
   from sage.matrix.all     import *
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/all.py",
line 1, in <module>
   from matrix_space import MatrixSpace, is_MatrixSpace
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py",
line 40, in <module>
   import matrix_mod2_dense
ImportError: /mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_mod2_dense.so:
undefined symbol: mzd_lqup
Sage failed to startup.
```




---

archive/issue_comments_090919.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-18T20:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90919",
    "user": "rlm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090920.json:
```json
{
    "body": "Replying to [comment:20 rlm]:\n> With a fresh build, sage doesn't start:\n\n```\nTraceback (most recent call last):\n File \"/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/bin/sage-eval\",line 4, in <module>\n   from sage.all import *\n File \"/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/all.py\", line 73, in <module>\n   from sage.matrix.all     import *\n File \"/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/all.py\", line 1, in <module>\n   from matrix_space import MatrixSpace, is_MatrixSpace\n File \"/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py\", line 40, in <module>\n   import matrix_mod2_dense\nImportError: /mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_mod2_dense.so:\nundefined symbol: mzd_lqup\nSage failed to startup.\n```\n\n\nLooks as if you haven't applied the Sage library patch (or didn't do `sage -b` after that).",
    "created_at": "2010-07-18T20:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90920",
    "user": "leif"
}
```

Replying to [comment:20 rlm]:
> With a fresh build, sage doesn't start:

```
Traceback (most recent call last):
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/bin/sage-eval",line 4, in <module>
   from sage.all import *
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/all.py", line 73, in <module>
   from sage.matrix.all     import *
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/all.py", line 1, in <module>
   from matrix_space import MatrixSpace, is_MatrixSpace
 File "/mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py", line 40, in <module>
   import matrix_mod2_dense
ImportError: /mnt/usb1/scratch/wstein/build/sage-4.5.1/local/lib/python2.6/site-packages/sage/matrix/matrix_mod2_dense.so:
undefined symbol: mzd_lqup
Sage failed to startup.
```


Looks as if you haven't applied the Sage library patch (or didn't do `sage -b` after that).



---

archive/issue_comments_090921.json:
```json
{
    "body": "Replying to [comment:21 leif]:\n> \n> Looks as if you haven't applied the Sage library patch (or didn't do `sage -b` after that).\n> \n\nI've been pretty bad about this lately... Sorry guys.",
    "created_at": "2010-07-18T20:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90921",
    "user": "rlm"
}
```

Replying to [comment:21 leif]:
> 
> Looks as if you haven't applied the Sage library patch (or didn't do `sage -b` after that).
> 

I've been pretty bad about this lately... Sorry guys.



---

archive/issue_comments_090922.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-18T20:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90922",
    "user": "rlm"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_090923.json:
```json
{
    "body": "\n```\nsage -t -long \"devel/sage-main/sage/crypto/mq/mpolynomialsystem.py\"\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occurred in Sage.\nThis probably occurred because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n```\n",
    "created_at": "2010-07-18T22:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90923",
    "user": "rlm"
}
```


```
sage -t -long "devel/sage-main/sage/crypto/mq/mpolynomialsystem.py"

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```




---

archive/issue_comments_090924.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-18T22:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90924",
    "user": "rlm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090925.json:
```json
{
    "body": "I tried to reproduce your segmentation fault, but I can't.\n\n\n```\nmalb@sage:~/scratch_sage/sage-4.4$ ./sage -t -long devel/sage-main/sage/crypto/mq/mpolynomialsystem.py\nsage -t -long \"devel/sage-main/sage/crypto/mq/mpolynomialsystem.py\"\n         [16.8 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 16.8 seconds\nmalb@sage:~/scratch_sage/sage-4.4$ cd devel/sage\nmalb@sage:~/scratch_sage/sage-4.4/devel/sage$ hg qap\nm4ri_new_version.patch\nsingular-3-1-1-4.patch\n\n```\n",
    "created_at": "2010-07-18T22:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90925",
    "user": "malb"
}
```

I tried to reproduce your segmentation fault, but I can't.


```
malb@sage:~/scratch_sage/sage-4.4$ ./sage -t -long devel/sage-main/sage/crypto/mq/mpolynomialsystem.py
sage -t -long "devel/sage-main/sage/crypto/mq/mpolynomialsystem.py"
         [16.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 16.8 seconds
malb@sage:~/scratch_sage/sage-4.4$ cd devel/sage
malb@sage:~/scratch_sage/sage-4.4/devel/sage$ hg qap
m4ri_new_version.patch
singular-3-1-1-4.patch

```




---

archive/issue_comments_090926.json:
```json
{
    "body": "Replying to [comment:23 rlm]:\n\n```\nsage -t -long \"devel/sage-main/sage/crypto/mq/mpolynomialsystem.py\"\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occurred in Sage.\n...\n```\n\n\nMachine, OS, platform? Parallel test? Whole library or just that single file?",
    "created_at": "2010-07-18T22:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90926",
    "user": "leif"
}
```

Replying to [comment:23 rlm]:

```
sage -t -long "devel/sage-main/sage/crypto/mq/mpolynomialsystem.py"

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
...
```


Machine, OS, platform? Parallel test? Whole library or just that single file?



---

archive/issue_comments_090927.json:
```json
{
    "body": "On geom.math, with a parallel build, in parallel and serial testing.",
    "created_at": "2010-07-19T07:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90927",
    "user": "rlm"
}
```

On geom.math, with a parallel build, in parallel and serial testing.



---

archive/issue_comments_090928.json:
```json
{
    "body": "\n```\nTrying:\n    C = mq.MPolynomialSystem(r2).connected_components(); C###line 76:_sage_    >>> C = mq.MPolynomialSystem(r2).connecte\nd_components(); C\nExpecting:\n    [Polynomial System with 16 Polynomials in 16 Variables,\n     Polynomial System with 16 Polynomials in 16 Variables]\nok\nTrying:\n    C[Integer(0)].groebner_basis()###line 80:_sage_    >>> C[0].groebner_basis()\nExpecting:\n    [x111*x110 + w113*x110 + w113*x112 + w113*x113 + w113*w111 + w113*w112 + x111 + x113 + w110 + w111 + w112,\n... (more output)\nBOOM\n```\n",
    "created_at": "2010-07-19T08:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90928",
    "user": "rlm"
}
```


```
Trying:
    C = mq.MPolynomialSystem(r2).connected_components(); C###line 76:_sage_    >>> C = mq.MPolynomialSystem(r2).connecte
d_components(); C
Expecting:
    [Polynomial System with 16 Polynomials in 16 Variables,
     Polynomial System with 16 Polynomials in 16 Variables]
ok
Trying:
    C[Integer(0)].groebner_basis()###line 80:_sage_    >>> C[0].groebner_basis()
Expecting:
    [x111*x110 + w113*x110 + w113*x112 + w113*x113 + w113*w111 + w113*w112 + x111 + x113 + w110 + w111 + w112,
... (more output)
BOOM
```




---

archive/issue_comments_090929.json:
```json
{
    "body": "I executed these steps\n\n* I got a clean 4.5\n* installed r-2.10.1.p3.spkg #9396\n* installed libm4ri-20100701.p1.spkg #9475\u00a0\n* applied m4ri_new_version.patch to devel/sage-main repo #9475\u00a0\n* merged trac_9507.patch to local/bin repo #9507\u00a0\n* replaced spkg/install with \"install.2\" from the ticket\u00a0#9528\n* ./sage -sdist 4.5.1\n* then extracted the tarball...\n* export SAGE_PARALLEL_SPKG_BUILD=yes\n* export MAKE=make -j20\n* make\n* since somehow libm4ri wasn't updated afterwards, I reinstalled\u00a0libm4ri-20100701.p1.spkg\n\n**Result:**\n\n\n```\nmalb@geom:~/scratch_sage/SIGSEGV/sage-4.5.1$ ./sage -t -long devel/sage/sage/crypto/mq/mpolynomialsystem.py \nsage -t -long \"devel/sage/sage/crypto/mq/mpolynomialsystem.py\"\n         [17.1 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 17.1 seconds\n\n```\n",
    "created_at": "2010-07-19T16:25:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90929",
    "user": "malb"
}
```

I executed these steps

* I got a clean 4.5
* installed r-2.10.1.p3.spkg #9396
* installed libm4ri-20100701.p1.spkg #9475 
* applied m4ri_new_version.patch to devel/sage-main repo #9475 
* merged trac_9507.patch to local/bin repo #9507 
* replaced spkg/install with "install.2" from the ticket #9528
* ./sage -sdist 4.5.1
* then extracted the tarball...
* export SAGE_PARALLEL_SPKG_BUILD=yes
* export MAKE=make -j20
* make
* since somehow libm4ri wasn't updated afterwards, I reinstalled libm4ri-20100701.p1.spkg

**Result:**


```
malb@geom:~/scratch_sage/SIGSEGV/sage-4.5.1$ ./sage -t -long devel/sage/sage/crypto/mq/mpolynomialsystem.py 
sage -t -long "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
         [17.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 17.1 seconds

```




---

archive/issue_comments_090930.json:
```json
{
    "body": "Well then, maybe it was a cosmic ray...",
    "created_at": "2010-07-19T16:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90930",
    "user": "rlm"
}
```

Well then, maybe it was a cosmic ray...



---

archive/issue_comments_090931.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-19T16:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90931",
    "user": "rlm"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_090932.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-07T02:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90932",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090933.json:
```json
{
    "body": "Do I need to apply \n\n  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.p1.spkg\n\n*and* [attachment:m4ri_new_version.patch]?  Can someone put the ticket number in the commit string?",
    "created_at": "2010-08-07T02:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90933",
    "user": "mpatel"
}
```

Do I need to apply 

  http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.p1.spkg

*and* [attachment:m4ri_new_version.patch]?  Can someone put the ticket number in the commit string?



---

archive/issue_comments_090934.json:
```json
{
    "body": "## Note to the release managers\n\n**Apply only [m4ri_new_version.v2.patch](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9475/m4ri_new_version.v2.patch) to the Sage library** when merging the [new M4RI spkg](http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.p1.spkg); that patch is identical to `m4ri_new_version.patch` except for the commit message. (I don't have the power to replace Martin's attachment.)",
    "created_at": "2010-08-07T07:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90934",
    "user": "leif"
}
```

## Note to the release managers

**Apply only [m4ri_new_version.v2.patch](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9475/m4ri_new_version.v2.patch) to the Sage library** when merging the [new M4RI spkg](http://sage.math.washington.edu/home/malb/spkgs/libm4ri-20100701.p1.spkg); that patch is identical to `m4ri_new_version.patch` except for the commit message. (I don't have the power to replace Martin's attachment.)



---

archive/issue_comments_090935.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-08-07T07:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90935",
    "user": "leif"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_090936.json:
```json
{
    "body": "Replying to [comment:30 mpatel]:\n> Can someone put the ticket number in the commit string?\n\nDone, but now we have yet another attachment since I couldn't replace Martin's.\n\n(I would have thought his patch's comment was sufficient to conclude that the patch has to be applied to the Sage library repository... ;-) )",
    "created_at": "2010-08-07T07:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90936",
    "user": "leif"
}
```

Replying to [comment:30 mpatel]:
> Can someone put the ticket number in the commit string?

Done, but now we have yet another attachment since I couldn't replace Martin's.

(I would have thought his patch's comment was sufficient to conclude that the patch has to be applied to the Sage library repository... ;-) )



---

archive/issue_comments_090937.json:
```json
{
    "body": "Note: I haven't merged this ticket into 4.5.3.alpha0, because I noticed some segfaults that appear to stem from the new package and/or patch, when I doctested various trial alpha0s on sage.math.  At the moment, it seems best to put out a 4.5.3.alpha0 with passing doctests and base on this any necessary efforts to merge the new M4RI into alpha1.",
    "created_at": "2010-08-09T23:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90937",
    "user": "mpatel"
}
```

Note: I haven't merged this ticket into 4.5.3.alpha0, because I noticed some segfaults that appear to stem from the new package and/or patch, when I doctested various trial alpha0s on sage.math.  At the moment, it seems best to put out a 4.5.3.alpha0 with passing doctests and base on this any necessary efforts to merge the new M4RI into alpha1.



---

archive/issue_comments_090938.json:
```json
{
    "body": "*Of course*, all long tests now pass (well, there are no reproducible failures) on sage.math with 4.5.3.alpha0 + #9475, so it seems no new efforts are necessary.  I'm checking bsd, redhawk, and t2 now.",
    "created_at": "2010-08-10T04:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90938",
    "user": "mpatel"
}
```

*Of course*, all long tests now pass (well, there are no reproducible failures) on sage.math with 4.5.3.alpha0 + #9475, so it seems no new efforts are necessary.  I'm checking bsd, redhawk, and t2 now.



---

archive/issue_comments_090939.json:
```json
{
    "body": "Replying to [comment:35 mpatel]:\n> *Of course*, all long tests now pass (well, there are no reproducible failures) on sage.math with 4.5.3.alpha0 + #9475, so it seems no new efforts are necessary.  I'm checking bsd, redhawk, and t2 now.\nThe long doctests also pass on bsd, redhawk, and t2.",
    "created_at": "2010-08-10T05:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90939",
    "user": "mpatel"
}
```

Replying to [comment:35 mpatel]:
> *Of course*, all long tests now pass (well, there are no reproducible failures) on sage.math with 4.5.3.alpha0 + #9475, so it seems no new efforts are necessary.  I'm checking bsd, redhawk, and t2 now.
The long doctests also pass on bsd, redhawk, and t2.



---

archive/issue_comments_090940.json:
```json
{
    "body": "There definitely is a bug in this new M4RI, I do get SIGSEGVs on my new laptop. I'll investigate.",
    "created_at": "2010-08-10T14:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90940",
    "user": "malb"
}
```

There definitely is a bug in this new M4RI, I do get SIGSEGVs on my new laptop. I'll investigate.



---

archive/issue_comments_090941.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-10T14:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90941",
    "user": "malb"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090942.json:
```json
{
    "body": "\n```\n        while(it!=end){\n            Exponent e=*it; \n                from_term_map_type::const_iterator from_it=eliminated2row_number.find(e);\n                assert(terms_as_exp_step1[row_start[from_it->second]]==e);\n                assert(from_it!=eliminated2row_number.end());\n ===>               int index=from_it->second;//...translate e->line number;\n                mzd_write_bit(mat_step2_factor,i,index,1);\n            it++;\n        }\n\n```\n\nThis is where pbori.pyx crashes for me. I installed a new GCC today, so maybe that's to blame?",
    "created_at": "2010-08-10T14:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90942",
    "user": "malb"
}
```


```
        while(it!=end){
            Exponent e=*it; 
                from_term_map_type::const_iterator from_it=eliminated2row_number.find(e);
                assert(terms_as_exp_step1[row_start[from_it->second]]==e);
                assert(from_it!=eliminated2row_number.end());
 ===>               int index=from_it->second;//...translate e->line number;
                mzd_write_bit(mat_step2_factor,i,index,1);
            it++;
        }

```

This is where pbori.pyx crashes for me. I installed a new GCC today, so maybe that's to blame?



---

archive/issue_comments_090943.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-08-10T15:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90943",
    "user": "malb"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_090944.json:
```json
{
    "body": "I think I got it: The[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) SPKG in 4.5.2 ships its own M4RI (and Boost) which conflicts with this new M4RI SPKG, thus since Leif removed this redundant copy of M4RI in the PolyBoRi, it works in 4.5.3.alpha0 but not before.",
    "created_at": "2010-08-10T15:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90944",
    "user": "malb"
}
```

I think I got it: The[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) SPKG in 4.5.2 ships its own M4RI (and Boost) which conflicts with this new M4RI SPKG, thus since Leif removed this redundant copy of M4RI in the PolyBoRi, it works in 4.5.3.alpha0 but not before.



---

archive/issue_comments_090945.json:
```json
{
    "body": "Replying to [comment:39 malb]:\n> I think I got it: The PolyBoRi SPKG in 4.5.2 ships its own M4RI (and Boost) which conflicts with this new M4RI SPKG, thus since Leif removed this redundant copy of M4RI in the PolyBoRi, it works in 4.5.3.alpha0 but not before.\n\nLOL! (Sometimes little clean-ups make more sense than expected...)",
    "created_at": "2010-08-10T15:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90945",
    "user": "leif"
}
```

Replying to [comment:39 malb]:
> I think I got it: The PolyBoRi SPKG in 4.5.2 ships its own M4RI (and Boost) which conflicts with this new M4RI SPKG, thus since Leif removed this redundant copy of M4RI in the PolyBoRi, it works in 4.5.3.alpha0 but not before.

LOL! (Sometimes little clean-ups make more sense than expected...)



---

archive/issue_comments_090946.json:
```json
{
    "body": "It seems this ticket is incompatible with#9717. On my laptop I always get SIGSEGVs in pbori.pyx",
    "created_at": "2010-08-11T15:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90946",
    "user": "malb"
}
```

It seems this ticket is incompatible with#9717. On my laptop I always get SIGSEGVs in pbori.pyx



---

archive/issue_comments_090947.json:
```json
{
    "body": "I tracked down the issue. The cause is some assumptions in[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) about M4RI which are not met anymore. This ticket can go in I say",
    "created_at": "2010-08-11T17:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90947",
    "user": "malb"
}
```

I tracked down the issue. The cause is some assumptions in[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) about M4RI which are not met anymore. This ticket can go in I say



---

archive/issue_comments_090948.json:
```json
{
    "body": "Actually, this ticket can only go in if a fix for[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) is also accepted, cf. #9717",
    "created_at": "2010-08-11T18:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90948",
    "user": "malb"
}
```

Actually, this ticket can only go in if a fix for[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) is also accepted, cf. #9717



---

archive/issue_comments_090949.json:
```json
{
    "body": "Minor thing: the documentation for rank still says:\n\nOn average 'lqup' should be faster than 'm4ri' and hence it is\n        the default choice.",
    "created_at": "2010-08-12T04:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90949",
    "user": "jason"
}
```

Minor thing: the documentation for rank still says:

On average 'lqup' should be faster than 'm4ri' and hence it is
        the default choice.



---

archive/issue_comments_090950.json:
```json
{
    "body": "#9717 has an updated, fixed[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) SPKG",
    "created_at": "2010-08-12T18:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90950",
    "user": "malb"
}
```

#9717 has an updated, fixed[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) SPKG



---

archive/issue_comments_090951.json:
```json
{
    "body": "The updated patch only replaces the mention of LQUP with PLS",
    "created_at": "2010-08-12T18:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90951",
    "user": "malb"
}
```

The updated patch only replaces the mention of LQUP with PLS



---

archive/issue_comments_090952.json:
```json
{
    "body": "Should someone review the latest changes?",
    "created_at": "2010-08-12T20:15:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90952",
    "user": "mpatel"
}
```

Should someone review the latest changes?



---

archive/issue_comments_090953.json:
```json
{
    "body": "The only change in the new version compared to the previous version of \u00a0m4ri_new_version.v2.patch is that one mention of LQUP was replaced by PLS in a docstring. That's all, this is why I didn't reset the status.",
    "created_at": "2010-08-12T20:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90953",
    "user": "malb"
}
```

The only change in the new version compared to the previous version of  m4ri_new_version.v2.patch is that one mention of LQUP was replaced by PLS in a docstring. That's all, this is why I didn't reset the status.



---

archive/issue_comments_090954.json:
```json
{
    "body": "Replying to [comment:48 malb]:\n> The only change in the new version compared to the previous version of \u00a0m4ri_new_version.v2.patch is that one mention of LQUP was replaced by PLS in a docstring. That's all, this is why I didn't reset the status.\n\nNot 100%:\n\n```patch\n--- m4ri_new_version.v2.patch.orig\t2010-08-07 09:00:21.000000000 +0200\n+++ m4ri_new_version.v2.patch\t2010-08-12 20:50:56.000000000 +0200\n@@ -1,14 +1,14 @@\n # HG changeset patch\n # User Martin Albrecht <malb@informatik.uni-bremen.de>\n # Date 1277764034 -3600\n-# Node ID 3365789479e6d70cb1930b2e97c7874cbd3310db\n-# Parent  ba36200d8a2f844179785580245fd95aa6401a51\n+# Node ID 3b116dd35a84e0b6bd8ea12a732b8fa1fbda796f\n+# Parent  0bb69a98789215c64a81c4602f46a50c0aeca5f0\n #9475 Adapts Sage library interface to new M4RI API (libm4ri-20100701)\n \n-diff -r ba36200d8a2f -r 3365789479e6 module_list.py\n---- a/module_list.py\tFri Jun 25 10:05:59 2010 +0100\n+diff -r 0bb69a987892 -r 3b116dd35a84 module_list.py\n+--- a/module_list.py\tTue Aug 10 13:46:10 2010 +0100\n +++ b/module_list.py\tMon Jun 28 23:27:14 2010 +0100\n-@@ -783,7 +783,7 @@\n+@@ -807,7 +807,7 @@\n      Extension('sage.matrix.matrix_mod2_dense',\n                sources = ['sage/matrix/matrix_mod2_dense.pyx'],\n                libraries = ['gmp','m4ri', 'gd', 'png12', 'z'],\n@@ -17,7 +17,7 @@\n  \n      Extension('sage.matrix.matrix_modn_dense',\n                sources = ['sage/matrix/matrix_modn_dense.pyx'],\n-@@ -971,7 +971,7 @@\n+@@ -995,7 +995,7 @@\n      Extension('sage.modules.vector_mod2_dense',\n                sources = ['sage/modules/vector_mod2_dense.pyx'],\n                libraries = ['gmp','m4ri', 'png12', 'gd'],\n@@ -26,8 +26,8 @@\n      \n      Extension('sage.modules.vector_rational_dense',\n                sources = ['sage/modules/vector_rational_dense.pyx'],\n-diff -r ba36200d8a2f -r 3365789479e6 sage/libs/m4ri.pxd\n---- a/sage/libs/m4ri.pxd\tFri Jun 25 10:05:59 2010 +0100\n+diff -r 0bb69a987892 -r 3b116dd35a84 sage/libs/m4ri.pxd\n+--- a/sage/libs/m4ri.pxd\tTue Aug 10 13:46:10 2010 +0100\n +++ b/sage/libs/m4ri.pxd\tMon Jun 28 23:27:14 2010 +0100\n @@ -141,6 +141,9 @@\n      # reduced row echelon form from upper triangular form\n@@ -60,8 +60,8 @@\n  \n      # reduced row echelon form using PLUQ factorization\n      cdef long mzd_echelonize_pluq(mzd_t *A, int full)\n-diff -r ba36200d8a2f -r 3365789479e6 sage/matrix/matrix_mod2_dense.pyx\n---- a/sage/matrix/matrix_mod2_dense.pyx\tFri Jun 25 10:05:59 2010 +0100\n+diff -r 0bb69a987892 -r 3b116dd35a84 sage/matrix/matrix_mod2_dense.pyx\n+--- a/sage/matrix/matrix_mod2_dense.pyx\tTue Aug 10 13:46:10 2010 +0100\n +++ b/sage/matrix/matrix_mod2_dense.pyx\tMon Jun 28 23:27:14 2010 +0100\n @@ -1010,15 +1010,16 @@\n      #    * Matrix windows -- only if you need strassen for that base\n@@ -116,7 +116,28 @@\n                  k = 0\n  \n              _sig_on\n-@@ -1681,7 +1691,7 @@\n+@@ -1106,6 +1116,20 @@\n+             self.cache('rank', r)\n+             self.cache('pivots', self._pivots())\n+ \n++        elif algorithm == 'top':\n++            \n++            self.check_mutability()\n++            self.clear_cache()        \n++\n++            _sig_on\n++            mzd_top_echelonize_m4ri(self._entries, 0)\n++            r = 0\n++            _sig_off\n++            \n++            self.cache('in_echelon_form',True)\n++            self.cache('rank', r)\n++            self.cache('pivots', self._pivots())\n++\n+         elif algorithm == 'linbox':\n+ \n+             #self._echelonize_linbox()\n+@@ -1681,7 +1705,7 @@\n              sage: float(d)\n              0.63184899999999999\n              sage: A.density(approx=True)\n@@ -125,7 +146,7 @@\n              sage: float(len(A.nonzero_positions())/1000^2)\n              0.63184899999999999\n          \"\"\"\n-@@ -1691,7 +1701,7 @@\n+@@ -1691,18 +1715,18 @@\n          else:\n              return matrix_dense.Matrix_dense.density(self)\n  \n@@ -134,7 +155,11 @@\n          \"\"\"\n          Return the rank of this matrix.\n  \n-@@ -1702,7 +1712,7 @@\n+-        On average 'lqup' should be faster than 'm4ri' and hence it is\n++        On average 'pls' should be faster than 'm4ri' and hence it is\n+         the default choice. However, for small - i.e. quite few\n+         thousand rows & columns - and sparse matrices 'm4ri' might be\n+         a better choice.\n  \n          INPUT:\n  \n@@ -143,7 +168,7 @@\n  \n          EXAMPLE::\n  \n-@@ -1722,10 +1732,10 @@\n+@@ -1722,10 +1746,10 @@\n          cdef mzd_t *A = mzd_copy(NULL, self._entries)\n          cdef mzp_t *P, *Q\n  \n@@ -156,7 +181,7 @@\n              mzp_free(P)\n              mzp_free(Q)\n          elif algorithm == 'm4ri':\n-@@ -2060,9 +2070,9 @@\n+@@ -2060,9 +2084,9 @@\n      mzp_free(q)\n      return B,P,Q\n  \n@@ -168,7 +193,7 @@\n  \n      INPUT:\n          A -- matrix\n-@@ -2074,14 +2084,14 @@\n+@@ -2074,14 +2098,14 @@\n  \n      EXAMPLE::\n  \n@@ -185,7 +210,7 @@\n          sage: LU\n          [1 0 0 1]\n          [1 1 0 0]\n-@@ -2095,7 +2105,7 @@\n+@@ -2095,7 +2119,7 @@\n          [0, 1, 2, 3]\n  \n          sage: A = random_matrix(GF(2),1000,1000)\n@@ -194,7 +219,7 @@\n          True\n      \"\"\"\n      cdef Matrix_mod2_dense B = A.__copy__()\n-@@ -2104,15 +2114,15 @@\n+@@ -2104,15 +2128,15 @@\n  \n      if algorithm == 'standard':\n          _sig_on\n```\n",
    "created_at": "2010-08-13T03:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90954",
    "user": "leif"
}
```

Replying to [comment:48 malb]:
> The only change in the new version compared to the previous version of  m4ri_new_version.v2.patch is that one mention of LQUP was replaced by PLS in a docstring. That's all, this is why I didn't reset the status.

Not 100%:

```patch
--- m4ri_new_version.v2.patch.orig	2010-08-07 09:00:21.000000000 +0200
+++ m4ri_new_version.v2.patch	2010-08-12 20:50:56.000000000 +0200
@@ -1,14 +1,14 @@
 # HG changeset patch
 # User Martin Albrecht <malb@informatik.uni-bremen.de>
 # Date 1277764034 -3600
-# Node ID 3365789479e6d70cb1930b2e97c7874cbd3310db
-# Parent  ba36200d8a2f844179785580245fd95aa6401a51
+# Node ID 3b116dd35a84e0b6bd8ea12a732b8fa1fbda796f
+# Parent  0bb69a98789215c64a81c4602f46a50c0aeca5f0
 #9475 Adapts Sage library interface to new M4RI API (libm4ri-20100701)
 
-diff -r ba36200d8a2f -r 3365789479e6 module_list.py
---- a/module_list.py	Fri Jun 25 10:05:59 2010 +0100
+diff -r 0bb69a987892 -r 3b116dd35a84 module_list.py
+--- a/module_list.py	Tue Aug 10 13:46:10 2010 +0100
 +++ b/module_list.py	Mon Jun 28 23:27:14 2010 +0100
-@@ -783,7 +783,7 @@
+@@ -807,7 +807,7 @@
      Extension('sage.matrix.matrix_mod2_dense',
                sources = ['sage/matrix/matrix_mod2_dense.pyx'],
                libraries = ['gmp','m4ri', 'gd', 'png12', 'z'],
@@ -17,7 +17,7 @@
  
      Extension('sage.matrix.matrix_modn_dense',
                sources = ['sage/matrix/matrix_modn_dense.pyx'],
-@@ -971,7 +971,7 @@
+@@ -995,7 +995,7 @@
      Extension('sage.modules.vector_mod2_dense',
                sources = ['sage/modules/vector_mod2_dense.pyx'],
                libraries = ['gmp','m4ri', 'png12', 'gd'],
@@ -26,8 +26,8 @@
      
      Extension('sage.modules.vector_rational_dense',
                sources = ['sage/modules/vector_rational_dense.pyx'],
-diff -r ba36200d8a2f -r 3365789479e6 sage/libs/m4ri.pxd
---- a/sage/libs/m4ri.pxd	Fri Jun 25 10:05:59 2010 +0100
+diff -r 0bb69a987892 -r 3b116dd35a84 sage/libs/m4ri.pxd
+--- a/sage/libs/m4ri.pxd	Tue Aug 10 13:46:10 2010 +0100
 +++ b/sage/libs/m4ri.pxd	Mon Jun 28 23:27:14 2010 +0100
 @@ -141,6 +141,9 @@
      # reduced row echelon form from upper triangular form
@@ -60,8 +60,8 @@
  
      # reduced row echelon form using PLUQ factorization
      cdef long mzd_echelonize_pluq(mzd_t *A, int full)
-diff -r ba36200d8a2f -r 3365789479e6 sage/matrix/matrix_mod2_dense.pyx
---- a/sage/matrix/matrix_mod2_dense.pyx	Fri Jun 25 10:05:59 2010 +0100
+diff -r 0bb69a987892 -r 3b116dd35a84 sage/matrix/matrix_mod2_dense.pyx
+--- a/sage/matrix/matrix_mod2_dense.pyx	Tue Aug 10 13:46:10 2010 +0100
 +++ b/sage/matrix/matrix_mod2_dense.pyx	Mon Jun 28 23:27:14 2010 +0100
 @@ -1010,15 +1010,16 @@
      #    * Matrix windows -- only if you need strassen for that base
@@ -116,7 +116,28 @@
                  k = 0
  
              _sig_on
-@@ -1681,7 +1691,7 @@
+@@ -1106,6 +1116,20 @@
+             self.cache('rank', r)
+             self.cache('pivots', self._pivots())
+ 
++        elif algorithm == 'top':
++            
++            self.check_mutability()
++            self.clear_cache()        
++
++            _sig_on
++            mzd_top_echelonize_m4ri(self._entries, 0)
++            r = 0
++            _sig_off
++            
++            self.cache('in_echelon_form',True)
++            self.cache('rank', r)
++            self.cache('pivots', self._pivots())
++
+         elif algorithm == 'linbox':
+ 
+             #self._echelonize_linbox()
+@@ -1681,7 +1705,7 @@
              sage: float(d)
              0.63184899999999999
              sage: A.density(approx=True)
@@ -125,7 +146,7 @@
              sage: float(len(A.nonzero_positions())/1000^2)
              0.63184899999999999
          """
-@@ -1691,7 +1701,7 @@
+@@ -1691,18 +1715,18 @@
          else:
              return matrix_dense.Matrix_dense.density(self)
  
@@ -134,7 +155,11 @@
          """
          Return the rank of this matrix.
  
-@@ -1702,7 +1712,7 @@
+-        On average 'lqup' should be faster than 'm4ri' and hence it is
++        On average 'pls' should be faster than 'm4ri' and hence it is
+         the default choice. However, for small - i.e. quite few
+         thousand rows & columns - and sparse matrices 'm4ri' might be
+         a better choice.
  
          INPUT:
  
@@ -143,7 +168,7 @@
  
          EXAMPLE::
  
-@@ -1722,10 +1732,10 @@
+@@ -1722,10 +1746,10 @@
          cdef mzd_t *A = mzd_copy(NULL, self._entries)
          cdef mzp_t *P, *Q
  
@@ -156,7 +181,7 @@
              mzp_free(P)
              mzp_free(Q)
          elif algorithm == 'm4ri':
-@@ -2060,9 +2070,9 @@
+@@ -2060,9 +2084,9 @@
      mzp_free(q)
      return B,P,Q
  
@@ -168,7 +193,7 @@
  
      INPUT:
          A -- matrix
-@@ -2074,14 +2084,14 @@
+@@ -2074,14 +2098,14 @@
  
      EXAMPLE::
  
@@ -185,7 +210,7 @@
          sage: LU
          [1 0 0 1]
          [1 1 0 0]
-@@ -2095,7 +2105,7 @@
+@@ -2095,7 +2119,7 @@
          [0, 1, 2, 3]
  
          sage: A = random_matrix(GF(2),1000,1000)
@@ -194,7 +219,7 @@
          True
      """
      cdef Matrix_mod2_dense B = A.__copy__()
-@@ -2104,15 +2114,15 @@
+@@ -2104,15 +2128,15 @@
  
      if algorithm == 'standard':
          _sig_on
```




---

archive/issue_comments_090955.json:
```json
{
    "body": "Argh, I'm an idiot! I'll update the patch, the 'top' stuff must be removed",
    "created_at": "2010-08-13T08:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90955",
    "user": "malb"
}
```

Argh, I'm an idiot! I'll update the patch, the 'top' stuff must be removed



---

archive/issue_comments_090956.json:
```json
{
    "body": "Sage library patch - needed to comply with new M4RI API (libm4ri-20100701). (Contains ticket number; apply only this one.)",
    "created_at": "2010-08-13T08:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90956",
    "user": "malb"
}
```

Sage library patch - needed to comply with new M4RI API (libm4ri-20100701). (Contains ticket number; apply only this one.)



---

archive/issue_comments_090957.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:50 malb]:\n> Argh, I'm an idiot! I'll update the patch, the 'top' stuff must be removed\n\nNevertheless, passed all long tests with Sage 4.5.3.alpha0 and PolyBoRi 0.6.4.p4 from #9717 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).\n\nThe newly uploaded patch contains only the desired changes.",
    "created_at": "2010-08-13T09:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90957",
    "user": "leif"
}
```

Attachment

Replying to [comment:50 malb]:
> Argh, I'm an idiot! I'll update the patch, the 'top' stuff must be removed

Nevertheless, passed all long tests with Sage 4.5.3.alpha0 and PolyBoRi 0.6.4.p4 from #9717 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).

The newly uploaded patch contains only the desired changes.



---

archive/issue_comments_090958.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-15T08:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9475#issuecomment-90958",
    "user": "mpatel"
}
```

Resolution: fixed
