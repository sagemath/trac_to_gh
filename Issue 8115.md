# Issue 8115: bad patching practice in cddlib-094f.p2.spkg

archive/issues_008115.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  vbraun mhampton\n\nKeywords: cddlib, polyhedra\n\nA problem with cddlib-094f.p2.spkg is that it patches upstream source using a patch file, rather than copying a patched file over to the appropriate place under the src/ directory. Consequently, there is no clean separation between upstream source and patches that we apply to cddlib-094f. Looking at spkg-install of cddlib-094f.p2.spkg, you get these two lines for applying Sage-specific patches:\n\n```\ncp patches/allfaces.c src/src/\n\npatch -p0 < patches/cdd_both_reps-make.patch\n```\n\nThe first line is the preferred way to patch an upstream source because it copies the patched file patches/allfaces.c over to src/src/.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8115\n\n",
    "created_at": "2010-01-29T09:51:05Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "bad patching practice in cddlib-094f.p2.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8115",
    "user": "mvngu"
}
```
Assignee: tbd

CC:  vbraun mhampton

Keywords: cddlib, polyhedra

A problem with cddlib-094f.p2.spkg is that it patches upstream source using a patch file, rather than copying a patched file over to the appropriate place under the src/ directory. Consequently, there is no clean separation between upstream source and patches that we apply to cddlib-094f. Looking at spkg-install of cddlib-094f.p2.spkg, you get these two lines for applying Sage-specific patches:

```
cp patches/allfaces.c src/src/

patch -p0 < patches/cdd_both_reps-make.patch
```

The first line is the preferred way to patch an upstream source because it copies the patched file patches/allfaces.c over to src/src/.

Issue created by migration from https://trac.sagemath.org/ticket/8115





---

archive/issue_comments_071246.json:
```json
{
    "body": "Updated spkg is up at\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/cddlib/cddlib-094f.p3.spkg\n\nChanges include:\n\n* clean separation between upstream source and Sage-specific patches\n* add function patch() to spkg-install for managing patches\n* use && for conditional \"and\" instead of \"-a\" in spkg-install",
    "created_at": "2010-01-29T09:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71246",
    "user": "mvngu"
}
```

Updated spkg is up at

http://sage.math.washington.edu/home/mvngu/spkg/standard/cddlib/cddlib-094f.p3.spkg

Changes include:

* clean separation between upstream source and Sage-specific patches
* add function patch() to spkg-install for managing patches
* use && for conditional "and" instead of "-a" in spkg-install



---

archive/issue_comments_071247.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-29T09:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71247",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071248.json:
```json
{
    "body": "The allfaces.c file is mentioned in the cddlib manual as an example file.  Its been in the sage spkg for a long time, I think.  Probably it was originally included to show sage developers how to use the library.  So it seems to make sense to get rid of it after #8115 is sorted out, since cdd_both_reps provides an example that is actually used.  \n\nMy apologies for missing this issue in review - makefiles and libraries are not my strong suit.\n\n-Marshall",
    "created_at": "2010-01-29T14:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71248",
    "user": "mhampton"
}
```

The allfaces.c file is mentioned in the cddlib manual as an example file.  Its been in the sage spkg for a long time, I think.  Probably it was originally included to show sage developers how to use the library.  So it seems to make sense to get rid of it after #8115 is sorted out, since cdd_both_reps provides an example that is actually used.  

My apologies for missing this issue in review - makefiles and libraries are not my strong suit.

-Marshall



---

archive/issue_comments_071249.json:
```json
{
    "body": "New version now has unmodified src (except for deleting unnecessary subdirectories). \n\nhttp://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg\n\nTo simplify review I'll attach spkg-install in verbatim. \n\nChanges: \n* libtool-ized, see http://trac.sagemath.org/sage_trac/ticket/3304\n  After implementing the changes, I found that tabbott proposed a\n  similar patch to the automake files earlier:\n  http://sagetrac.org/sage_trac/ticket/3304\n* renamed configure.in -> configure.ac (preferred usage)\n* renamed patches/cdd_both_reps-makefiles.patch -> patches/automake.patch \n* added check for required mpir (aka GMP) to spkg-install\n* added spkg-check\n* corrected src/patch usage\n* removed CFLAGS settings in spkg-install, not required.\n* Workaround for spkg-env setting RM=\"rm\"\n  http://trac.sagemath.org/sage_trac/ticket/7818#comment:28",
    "created_at": "2010-01-29T16:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71249",
    "user": "vbraun"
}
```

New version now has unmodified src (except for deleting unnecessary subdirectories). 

http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg

To simplify review I'll attach spkg-install in verbatim. 

Changes: 
* libtool-ized, see http://trac.sagemath.org/sage_trac/ticket/3304
  After implementing the changes, I found that tabbott proposed a
  similar patch to the automake files earlier:
  http://sagetrac.org/sage_trac/ticket/3304
* renamed configure.in -> configure.ac (preferred usage)
* renamed patches/cdd_both_reps-makefiles.patch -> patches/automake.patch 
* added check for required mpir (aka GMP) to spkg-install
* added spkg-check
* corrected src/patch usage
* removed CFLAGS settings in spkg-install, not required.
* Workaround for spkg-env setting RM="rm"
  http://trac.sagemath.org/sage_trac/ticket/7818#comment:28



---

archive/issue_comments_071250.json:
```json
{
    "body": "Attachment [spkg-install](tarball://root/attachments/some-uuid/ticket8115/spkg-install) by vbraun created at 2010-01-29 16:34:00\n\nspkg-install from cddlib-094f.p4.spkg",
    "created_at": "2010-01-29T16:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71250",
    "user": "vbraun"
}
```

Attachment [spkg-install](tarball://root/attachments/some-uuid/ticket8115/spkg-install) by vbraun created at 2010-01-29 16:34:00

spkg-install from cddlib-094f.p4.spkg



---

archive/issue_comments_071251.json:
```json
{
    "body": "There are outstanding changes in \n\nhttp://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg\n\nwhich must be first checked in:\n\n```\n[mvngu@mod cddlib-094f.p4]$ pwd\n/home/mvngu/cddlib-094f.p4\n[mvngu@mod cddlib-094f.p4]$ hg st\nM SPKG.txt\nM spkg-install\nA patches/autogenerated/INSTALL\nA patches/autogenerated/Makefile.in\nA patches/autogenerated/aclocal.m4\nA patches/autogenerated/config.guess\nA patches/autogenerated/config.sub\nA patches/autogenerated/configure\nA patches/autogenerated/configure.ac\nA patches/autogenerated/depcomp\nA patches/autogenerated/install-sh\nA patches/autogenerated/ltmain.sh\nA patches/autogenerated/m4/libtool.m4\nA patches/autogenerated/m4/ltoptions.m4\nA patches/autogenerated/m4/ltsugar.m4\nA patches/autogenerated/m4/ltversion.m4\nA patches/autogenerated/m4/lt~obsolete.m4\nA patches/autogenerated/missing\nA patches/autogenerated/mkinstalldirs\nA patches/automake.patch\nA patches/configure.ac\nA patches/lib-src-Makefile.am\nA patches/lib-src-gmp-Makefile.am\nA patches/src-Makefile.am\nA patches/src-gmp-Makefile.am\nA spkg-check\nR patches/cdd_both_reps-make.patch\n```\n",
    "created_at": "2010-01-31T01:35:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71251",
    "user": "mvngu"
}
```

There are outstanding changes in 

http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg

which must be first checked in:

```
[mvngu@mod cddlib-094f.p4]$ pwd
/home/mvngu/cddlib-094f.p4
[mvngu@mod cddlib-094f.p4]$ hg st
M SPKG.txt
M spkg-install
A patches/autogenerated/INSTALL
A patches/autogenerated/Makefile.in
A patches/autogenerated/aclocal.m4
A patches/autogenerated/config.guess
A patches/autogenerated/config.sub
A patches/autogenerated/configure
A patches/autogenerated/configure.ac
A patches/autogenerated/depcomp
A patches/autogenerated/install-sh
A patches/autogenerated/ltmain.sh
A patches/autogenerated/m4/libtool.m4
A patches/autogenerated/m4/ltoptions.m4
A patches/autogenerated/m4/ltsugar.m4
A patches/autogenerated/m4/ltversion.m4
A patches/autogenerated/m4/lt~obsolete.m4
A patches/autogenerated/missing
A patches/autogenerated/mkinstalldirs
A patches/automake.patch
A patches/configure.ac
A patches/lib-src-Makefile.am
A patches/lib-src-gmp-Makefile.am
A patches/src-Makefile.am
A patches/src-gmp-Makefile.am
A spkg-check
R patches/cdd_both_reps-make.patch
```




---

archive/issue_comments_071252.json:
```json
{
    "body": "I'm moving this to \"needs work\" until all changes have been checked in.",
    "created_at": "2010-01-31T01:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71252",
    "user": "mvngu"
}
```

I'm moving this to "needs work" until all changes have been checked in.



---

archive/issue_comments_071253.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-31T01:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71253",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071254.json:
```json
{
    "body": "Here's an updated spkg \n\nhttp://boxen.math.washington.edu/home/mvngu/patch/cddlib-094f.p4.spkg\n\nwhich commits all outstanding changes in vbraun's name. In this updated spkg, I inserted the following line in spkg-install:\n\n```\n[mvngu@mod cddlib-094f.p4]$ hg diff\ndiff -r 499a1b5d0357 spkg-install\n--- a/spkg-install\n+++ b/spkg-install\n@@ -47,6 +47,9 @@\n # See http://trac.sagemath.org/sage_trac/ticket/7818#comment:28\n unset RM\n \n+# apply patches on top of pristine upstream release under src/\n+patch\n+\n cd src\n \n ./configure --prefix=$SAGE_LOCAL\n```\n\nThis runs the function `patch()` in `spkg-install` so that the patching is done before configuring the upstream source under `src/`.",
    "created_at": "2010-01-31T02:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71254",
    "user": "mvngu"
}
```

Here's an updated spkg 

http://boxen.math.washington.edu/home/mvngu/patch/cddlib-094f.p4.spkg

which commits all outstanding changes in vbraun's name. In this updated spkg, I inserted the following line in spkg-install:

```
[mvngu@mod cddlib-094f.p4]$ hg diff
diff -r 499a1b5d0357 spkg-install
--- a/spkg-install
+++ b/spkg-install
@@ -47,6 +47,9 @@
 # See http://trac.sagemath.org/sage_trac/ticket/7818#comment:28
 unset RM
 
+# apply patches on top of pristine upstream release under src/
+patch
+
 cd src
 
 ./configure --prefix=$SAGE_LOCAL
```

This runs the function `patch()` in `spkg-install` so that the patching is done before configuring the upstream source under `src/`.



---

archive/issue_comments_071255.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-31T02:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71255",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071256.json:
```json
{
    "body": "I didn't know that I had commit rights to the mercurial repository! Also, I thought that the patch function would be called automatically, but clearly it is not and spkg-install has to call it manually. I did not catch that error because I did not delete $SAGE_LOCAL/*/cdd* before force-reinstalling.\n\nTesting the spkg properly, I now noticed that the main src/Makefile.m4 was not included in patches/, and other Makefile.am's were not copied to the right place.  Here is a fixed spkg:\n\nhttp://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg\n\nAlso, changes now checked into hg repo.",
    "created_at": "2010-01-31T12:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71256",
    "user": "vbraun"
}
```

I didn't know that I had commit rights to the mercurial repository! Also, I thought that the patch function would be called automatically, but clearly it is not and spkg-install has to call it manually. I did not catch that error because I did not delete $SAGE_LOCAL/*/cdd* before force-reinstalling.

Testing the spkg properly, I now noticed that the main src/Makefile.m4 was not included in patches/, and other Makefile.am's were not copied to the right place.  Here is a fixed spkg:

http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg

Also, changes now checked into hg repo.



---

archive/issue_comments_071257.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T22:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71257",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071258.json:
```json
{
    "body": "Replying to [comment:8 vbraun]:\n> I didn't know that I had commit rights to the mercurial repository! \n\nTo some extent, any Sage developer has commit rights. The idea is that one puts one's username in any Mercurial patch. For spkg updates, all changes need to be checked in before submitting them for review. In this way, people know who did what and when. As for patches against the Sage library, a release manager would commit a patch using the username of the developer who wrote that patch. This process can be made easier if the developer puts their username on their patch. By username, this is understood as being a developer's real name, not the username for logging into the Trac server.\n\n\n\n\n> Here is a fixed spkg:\n> \n> http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg\n> \n> Also, changes now checked into hg repo.\n\nThe updated spkg looks good. I longer see any binaries being moved to the script repository at `SAGE_ROOT/local/bin`. All doctests pass.",
    "created_at": "2010-01-31T22:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71258",
    "user": "mvngu"
}
```

Replying to [comment:8 vbraun]:
> I didn't know that I had commit rights to the mercurial repository! 

To some extent, any Sage developer has commit rights. The idea is that one puts one's username in any Mercurial patch. For spkg updates, all changes need to be checked in before submitting them for review. In this way, people know who did what and when. As for patches against the Sage library, a release manager would commit a patch using the username of the developer who wrote that patch. This process can be made easier if the developer puts their username on their patch. By username, this is understood as being a developer's real name, not the username for logging into the Trac server.




> Here is a fixed spkg:
> 
> http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg
> 
> Also, changes now checked into hg repo.

The updated spkg looks good. I longer see any binaries being moved to the script repository at `SAGE_ROOT/local/bin`. All doctests pass.



---

archive/issue_comments_071259.json:
```json
{
    "body": "Merged [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg) in the standard spkg repository.",
    "created_at": "2010-01-31T22:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71259",
    "user": "mvngu"
}
```

Merged [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg) in the standard spkg repository.



---

archive/issue_comments_071260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-31T22:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71260",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_071261.json:
```json
{
    "body": "This looks bad. I'm now getting a build error when forcing a re-installation of [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg):\n\n```\n[mvngu@mod sage-4.3.2.alpha0]$ ./sage -f http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg\n<compile-messages>\ncddcore.c:2072: error: expected \u2018)\u2019 before \u2018lc\u2019\ncddcore.c:2084: error: expected \u2018)\u2019 before \u2018prod\u2019\nmake[1]: *** [cddcore.lo] Error 1\nmake[1]: Leaving directory `/scratch/mvngu/release/sage-4.3.2.alpha0/spkg/build/cddlib-094f.p4/src/lib-src-gmp'\nmake: *** [all-recursive] Error 1\nError building cddlib\n\nreal    0m17.132s\nuser    0m8.960s\nsys     0m4.350s\nsage: An error occurred while installing cddlib-094f.p4\n```\n\nI'm reopening this ticket and backing [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg) out of Sage 4.3.2.alpha1.",
    "created_at": "2010-02-01T05:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71261",
    "user": "mvngu"
}
```

This looks bad. I'm now getting a build error when forcing a re-installation of [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg):

```
[mvngu@mod sage-4.3.2.alpha0]$ ./sage -f http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg
<compile-messages>
cddcore.c:2072: error: expected ‘)’ before ‘lc’
cddcore.c:2084: error: expected ‘)’ before ‘prod’
make[1]: *** [cddcore.lo] Error 1
make[1]: Leaving directory `/scratch/mvngu/release/sage-4.3.2.alpha0/spkg/build/cddlib-094f.p4/src/lib-src-gmp'
make: *** [all-recursive] Error 1
Error building cddlib

real    0m17.132s
user    0m8.960s
sys     0m4.350s
sage: An error occurred while installing cddlib-094f.p4
```

I'm reopening this ticket and backing [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg) out of Sage 4.3.2.alpha1.



---

archive/issue_comments_071262.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-02-01T05:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71262",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_071263.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-02-01T05:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71263",
    "user": "mvngu"
}
```

Changing status from closed to new.



---

archive/issue_comments_071264.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-02-01T05:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71264",
    "user": "mvngu"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_071265.json:
```json
{
    "body": "Which architecture is that error on? Full messages log?\n\nI dug around a bit and the autogenerated files were copied with `cp` instead of `cp -p`, which then tricks `make` into re-running some autotools. This might have been the problem, even though it shouldn't. Updated spkg is here:\n\nhttp://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg",
    "created_at": "2010-02-01T13:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71265",
    "user": "vbraun"
}
```

Which architecture is that error on? Full messages log?

I dug around a bit and the autogenerated files were copied with `cp` instead of `cp -p`, which then tricks `make` into re-running some autotools. This might have been the problem, even though it shouldn't. Updated spkg is here:

http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg



---

archive/issue_comments_071266.json:
```json
{
    "body": "Attachment [cddlib.log.bz2](tarball://root/attachments/some-uuid/ticket8115/cddlib.log.bz2) by mvngu created at 2010-02-01 19:10:56\n\ninstall log for cddlib-094f.p4.spkg",
    "created_at": "2010-02-01T19:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71266",
    "user": "mvngu"
}
```

Attachment [cddlib.log.bz2](tarball://root/attachments/some-uuid/ticket8115/cddlib.log.bz2) by mvngu created at 2010-02-01 19:10:56

install log for cddlib-094f.p4.spkg



---

archive/issue_comments_071267.json:
```json
{
    "body": "Replying to [comment:13 vbraun]:\n> Which architecture is that error on? Full messages log?\nHere is some relevant information about the machine on which I tried to force a re-installation of the previous version of cddlib-094f.p4.spkg:\n\n* OS version: Ubuntu 8.04.3 LTS\n* Machine name: mod.math.washington.edu\n* Architecture: Intel(R) Xeon(R) CPU X7460 `@` 2.66GHz\n* 32/64 bit: 64-bit\n* RAM: 124 GB\n* Compiler: GCC 4.2.4\n\nEven with the updated spkg you posted, forcing a re-installation also results in a build failure on the above machine. I have attached an install log.",
    "created_at": "2010-02-01T19:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71267",
    "user": "mvngu"
}
```

Replying to [comment:13 vbraun]:
> Which architecture is that error on? Full messages log?
Here is some relevant information about the machine on which I tried to force a re-installation of the previous version of cddlib-094f.p4.spkg:

* OS version: Ubuntu 8.04.3 LTS
* Machine name: mod.math.washington.edu
* Architecture: Intel(R) Xeon(R) CPU X7460 `@` 2.66GHz
* 32/64 bit: 64-bit
* RAM: 124 GB
* Compiler: GCC 4.2.4

Even with the updated spkg you posted, forcing a re-installation also results in a build failure on the above machine. I have attached an install log.



---

archive/issue_comments_071268.json:
```json
{
    "body": "The problem is that gmp/mpir headers are not found. On my machine, these are already installed in /usr/include, but not on mod.math.washington.edu. I was under the wrong impression that the sage build process would put $SAGE_LOCAL/include and $SAGE_LOCAL/lib at the beginning of CPPFLAGS and LDFLAGS, respectively. Apparently they need to be set manually in the spkg_install.\n\nHere is an updated spkg that sets these *FLAGS correctly. To test it, I uninstalled gmp on my machine and could still build the cddlib spgk successfully.\n\nhttp://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg",
    "created_at": "2010-02-01T21:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71268",
    "user": "vbraun"
}
```

The problem is that gmp/mpir headers are not found. On my machine, these are already installed in /usr/include, but not on mod.math.washington.edu. I was under the wrong impression that the sage build process would put $SAGE_LOCAL/include and $SAGE_LOCAL/lib at the beginning of CPPFLAGS and LDFLAGS, respectively. Apparently they need to be set manually in the spkg_install.

Here is an updated spkg that sets these *FLAGS correctly. To test it, I uninstalled gmp on my machine and could still build the cddlib spgk successfully.

http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg



---

archive/issue_comments_071269.json:
```json
{
    "body": "Replying to [comment:15 vbraun]:\n\n> \n> Here is an updated spkg that sets these *FLAGS correctly. To test it, I uninstalled gmp on my machine and could still build the cddlib spgk successfully.\n> \n> http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg\n\nThis one fails with:\n\n\n\n```\nconfig.status: creating lib-src/Makefile\nconfig.status: creating src/Makefile\nconfig.status: creating lib-src-gmp/Makefile\nconfig.status: creating src-gmp/Makefile\nconfig.status: creating Makefile\nconfig.status: executing depfiles commands\nconfig.status: executing libtool commands\nmake: Fatal error in reader: Makefile, line 706: Unexpected end of line seen\nError building cddlib\n\nreal    0m3.070s\nuser    0m0.743s\nsys     0m0.886s\nsage: An error occurred while installing cddlib-094f.p4\n\n```\n\n\nOn Open Solaris x64\n\nJaap",
    "created_at": "2010-02-02T15:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71269",
    "user": "jsp"
}
```

Replying to [comment:15 vbraun]:

> 
> Here is an updated spkg that sets these *FLAGS correctly. To test it, I uninstalled gmp on my machine and could still build the cddlib spgk successfully.
> 
> http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg

This one fails with:



```
config.status: creating lib-src/Makefile
config.status: creating src/Makefile
config.status: creating lib-src-gmp/Makefile
config.status: creating src-gmp/Makefile
config.status: creating Makefile
config.status: executing depfiles commands
config.status: executing libtool commands
make: Fatal error in reader: Makefile, line 706: Unexpected end of line seen
Error building cddlib

real    0m3.070s
user    0m0.743s
sys     0m0.886s
sage: An error occurred while installing cddlib-094f.p4

```


On Open Solaris x64

Jaap



---

archive/issue_comments_071270.json:
```json
{
    "body": "Replying to [comment:16 jsp]:\n\n> \n> On Open Solaris x64\n> \n\n\n\n\nSorry for the noise. This was due to a configuration error: no libtool in /usr/bin\n\nOn my Open Solaris in VirtualBox no such a problem. There are others!\n\nJaap",
    "created_at": "2010-02-02T16:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71270",
    "user": "jsp"
}
```

Replying to [comment:16 jsp]:

> 
> On Open Solaris x64
> 




Sorry for the noise. This was due to a configuration error: no libtool in /usr/bin

On my Open Solaris in VirtualBox no such a problem. There are others!

Jaap



---

archive/issue_comments_071271.json:
```json
{
    "body": "Attachment [cddlib-local-bin-hgignore.patch](tarball://root/attachments/some-uuid/ticket8115/cddlib-local-bin-hgignore.patch) by vbraun created at 2010-02-03 19:32:30\n\nAdd cdd_both_reps/cdd_both_reps_gmp binaries to .hgignore.",
    "created_at": "2010-02-03T19:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71271",
    "user": "vbraun"
}
```

Attachment [cddlib-local-bin-hgignore.patch](tarball://root/attachments/some-uuid/ticket8115/cddlib-local-bin-hgignore.patch) by vbraun created at 2010-02-03 19:32:30

Add cdd_both_reps/cdd_both_reps_gmp binaries to .hgignore.



---

archive/issue_comments_071272.json:
```json
{
    "body": "I don't know how long it would take to positively review this ticket. So I have moved [cddlib-local-bin-hgignore.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8115/cddlib-local-bin-hgignore.patch) over to #8179.",
    "created_at": "2010-02-03T19:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71272",
    "user": "mvngu"
}
```

I don't know how long it would take to positively review this ticket. So I have moved [cddlib-local-bin-hgignore.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8115/cddlib-local-bin-hgignore.patch) over to #8179.



---

archive/issue_comments_071273.json:
```json
{
    "body": "A reason why this ticket has been stalling is that we have been trying to do too many things at once. The original intention was to get `cddlib-094f.p2.spkg` into such a shape that there is a clear separation between Sage specific patches and upstream source. And also to use `cp` during the patching process. The updated package \n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/cddlib/cddlib-094f.p3.spkg\n\ndoes just the above two tasks. Once this spkg is in, we can open another ticket to tidy up cddlib. So only `cddlib-094f.p3.spkg` needs reviewing.",
    "created_at": "2010-02-17T01:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71273",
    "user": "mvngu"
}
```

A reason why this ticket has been stalling is that we have been trying to do too many things at once. The original intention was to get `cddlib-094f.p2.spkg` into such a shape that there is a clear separation between Sage specific patches and upstream source. And also to use `cp` during the patching process. The updated package 

http://sage.math.washington.edu/home/mvngu/spkg/standard/cddlib/cddlib-094f.p3.spkg

does just the above two tasks. Once this spkg is in, we can open another ticket to tidy up cddlib. So only `cddlib-094f.p3.spkg` needs reviewing.



---

archive/issue_comments_071274.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-17T01:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71274",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071275.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-17T01:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71275",
    "user": "vbraun"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071276.json:
```json
{
    "body": "The .p3 will break polyhedra.py, please don't apply that. You need those two parts:\n\n\n```\n    # Required by sage.geometry.polyhedra\n    cp patches/cdd_both_reps.c src/src/\n    cp patches/cdd_both_reps.c src/src-gmp/\n```\n\n\nTo actually compile these extra .c sources, you need the updated Makefile.am's and rerun autoconf/automake and keep track of the autogenerated files.\n\nCan you be a bit clearer on what you want to separate out? Do you want a spkg with all updates and fixes except the libtools stuff? I can split that out but I don't quite see the point. We'd have to test one new set of autotools-files and then, with the shared library update, trash those autogenerated files and try yet another set of autogenerated files.",
    "created_at": "2010-02-17T01:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71276",
    "user": "vbraun"
}
```

The .p3 will break polyhedra.py, please don't apply that. You need those two parts:


```
    # Required by sage.geometry.polyhedra
    cp patches/cdd_both_reps.c src/src/
    cp patches/cdd_both_reps.c src/src-gmp/
```


To actually compile these extra .c sources, you need the updated Makefile.am's and rerun autoconf/automake and keep track of the autogenerated files.

Can you be a bit clearer on what you want to separate out? Do you want a spkg with all updates and fixes except the libtools stuff? I can split that out but I don't quite see the point. We'd have to test one new set of autotools-files and then, with the shared library update, trash those autogenerated files and try yet another set of autogenerated files.



---

archive/issue_comments_071277.json:
```json
{
    "body": "Now I'm looking at [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg). I'm getting this:\n\n```\n[mvngu@sage cddlib-094f.p4]$ hg st\n! patches/autogenerated/configure.ac\n```\n",
    "created_at": "2010-02-17T01:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71277",
    "user": "mvngu"
}
```

Now I'm looking at [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg). I'm getting this:

```
[mvngu@sage cddlib-094f.p4]$ hg st
! patches/autogenerated/configure.ac
```




---

archive/issue_comments_071278.json:
```json
{
    "body": "Sorry I forgot to commit that change; Fixed now.\n\nSince configure.ac is one of the autotools source files, it belongs into patches/ and not into patches/autogenerated.",
    "created_at": "2010-02-17T12:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71278",
    "user": "vbraun"
}
```

Sorry I forgot to commit that change; Fixed now.

Since configure.ac is one of the autotools source files, it belongs into patches/ and not into patches/autogenerated.



---

archive/issue_comments_071279.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-17T12:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71279",
    "user": "vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071280.json:
```json
{
    "body": "Replying to [comment:24 vbraun]:\n> Sorry I forgot to commit that change; Fixed now.\n\nWhere is the updated spkg. I assume that this is the updated spkg:\n\nhttp://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg\n\nBut that one still gives:\n\n\n```\n[mvngu@sage cddlib-094f.p4]$ hg st\n! patches/autogenerated/configure.ac\n```\n",
    "created_at": "2010-02-17T14:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71280",
    "user": "mvngu"
}
```

Replying to [comment:24 vbraun]:
> Sorry I forgot to commit that change; Fixed now.

Where is the updated spkg. I assume that this is the updated spkg:

http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg

But that one still gives:


```
[mvngu@sage cddlib-094f.p4]$ hg st
! patches/autogenerated/configure.ac
```




---

archive/issue_comments_071281.json:
```json
{
    "body": "Oops. Copied updated spgk to\n\nhttp://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg",
    "created_at": "2010-02-17T15:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71281",
    "user": "vbraun"
}
```

Oops. Copied updated spgk to

http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg



---

archive/issue_comments_071282.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-17T20:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71282",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071283.json:
```json
{
    "body": "The package [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg) now builds on sage.math, bsd.math, rosemary.math, and machines on Skynet.",
    "created_at": "2010-02-17T20:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71283",
    "user": "mvngu"
}
```

The package [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg) now builds on sage.math, bsd.math, rosemary.math, and machines on Skynet.



---

archive/issue_comments_071284.json:
```json
{
    "body": "Merged [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg) in the standard spkg repository.",
    "created_at": "2010-02-17T20:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71284",
    "user": "mvngu"
}
```

Merged [cddlib-094f.p4.spkg](http://www.stp.dias.ie/~vbraun/cddlib-094f.p4.spkg) in the standard spkg repository.



---

archive/issue_comments_071285.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T20:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71285",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_071286.json:
```json
{
    "body": "Guys, it would be good to know how to do changes in this  framework of patches you created.\nThe current problem with this spkg is that gmp must be in $SAGE_LOCAL, and not in /usr/local\nThis stops the thing building on Solaris, see [http://groups.google.com/group/sage-release/msg/35b0c600a5ef250f](http://groups.google.com/group/sage-release/msg/35b0c600a5ef250f) and other messages in this thread.\nAnd gmpdir=/usr/local is hardwired in Makefile.am...\n\nThanks,\nDima",
    "created_at": "2010-04-20T13:04:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71286",
    "user": "dimpase"
}
```

Guys, it would be good to know how to do changes in this  framework of patches you created.
The current problem with this spkg is that gmp must be in $SAGE_LOCAL, and not in /usr/local
This stops the thing building on Solaris, see [http://groups.google.com/group/sage-release/msg/35b0c600a5ef250f](http://groups.google.com/group/sage-release/msg/35b0c600a5ef250f) and other messages in this thread.
And gmpdir=/usr/local is hardwired in Makefile.am...

Thanks,
Dima



---

archive/issue_comments_071287.json:
```json
{
    "body": "Dima, this ticket has already been closed. I created a new ticket with your problem at #8730, and will post updated spkg there.",
    "created_at": "2010-04-20T17:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8115",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8115#issuecomment-71287",
    "user": "vbraun"
}
```

Dima, this ticket has already been closed. I created a new ticket with your problem at #8730, and will post updated spkg there.
