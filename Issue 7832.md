# Issue 7832: singular-3-1-0-4-20090818.p2 - fix compilation on FreeBSD

archive/issues_007832.json:
```json
{
    "body": "Assignee: @peterjeremy\n\nBy default, you get the following, which is corrected by the patch to singuname.sh:\n\n```\nmake[2]: Entering directory `/home/peter/sage/sage-4.3/spkg/build/singular-3-1-0-4-20090818.p2/src'\nmake[2]: *** No rule to make target `distclean'.  Stop.\nmake[2]: Leaving directory `/home/peter/sage/sage-4.3/spkg/build/singular-3-1-0-4-20090818.p2/src'\nrm: /home/peter/sage/sage-4.3/local/bin/Singular*: No such file or directory\ncreating cache ./config.cache\nchecking uname for singular... unknown\nconfigure: error: Unknown architecture: Check singuname.sh\nUnable to configure Singular.\n```\n\n\nCorrect configure script for amd64 by patching the autoconf inputs and re-running autoconf.  This corrects a problem where linking libsingular.so reports lots of undefined references to both internal `om`* functions and functions within libncurses.\n\nSeveral other trivial fixes to support dynamic linking on FreeBSD/amd64.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7832\n\n",
    "created_at": "2010-01-03T10:10:09Z",
    "labels": [
        "component: porting: bsd",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "singular-3-1-0-4-20090818.p2 - fix compilation on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7832",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: @peterjeremy

By default, you get the following, which is corrected by the patch to singuname.sh:

```
make[2]: Entering directory `/home/peter/sage/sage-4.3/spkg/build/singular-3-1-0-4-20090818.p2/src'
make[2]: *** No rule to make target `distclean'.  Stop.
make[2]: Leaving directory `/home/peter/sage/sage-4.3/spkg/build/singular-3-1-0-4-20090818.p2/src'
rm: /home/peter/sage/sage-4.3/local/bin/Singular*: No such file or directory
creating cache ./config.cache
checking uname for singular... unknown
configure: error: Unknown architecture: Check singuname.sh
Unable to configure Singular.
```


Correct configure script for amd64 by patching the autoconf inputs and re-running autoconf.  This corrects a problem where linking libsingular.so reports lots of undefined references to both internal `om`* functions and functions within libncurses.

Several other trivial fixes to support dynamic linking on FreeBSD/amd64.


Issue created by migration from https://trac.sagemath.org/ticket/7832





---

archive/issue_comments_067725.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T10:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67725",
    "user": "https://github.com/peterjeremy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067726.json:
```json
{
    "body": "Attachment [7832.singular.patch](tarball://root/attachments/some-uuid/ticket7832/7832.singular.patch) by @peterjeremy created at 2010-01-03 10:11:18",
    "created_at": "2010-01-03T10:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67726",
    "user": "https://github.com/peterjeremy"
}
```

Attachment [7832.singular.patch](tarball://root/attachments/some-uuid/ticket7832/7832.singular.patch) by @peterjeremy created at 2010-01-03 10:11:18



---

archive/issue_comments_067727.json:
```json
{
    "body": "Unless I am mistaken, you have modified the singular sources directly, which is not permitted. Instead, you should create new versions of the files, put them in the 'patches' directory, and have something in spkg-install like\n\n```\ncp patch/mod_raw.cc src/kernel/mod_raw.cc\n```\n\nLikewise, you should not change the configure script, or configure.ac, but instead have \n\n```\ncp patches/configure src/\n```\n\nand created a diff file between the old configure.ac and the new configure.ac and put that in the patches directory. \n\nOnce that is done, it would need testing on Solaris, OS X and Linux in addition to FreeBSD. \n\nDave",
    "created_at": "2010-02-22T00:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67727",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Unless I am mistaken, you have modified the singular sources directly, which is not permitted. Instead, you should create new versions of the files, put them in the 'patches' directory, and have something in spkg-install like

```
cp patch/mod_raw.cc src/kernel/mod_raw.cc
```

Likewise, you should not change the configure script, or configure.ac, but instead have 

```
cp patches/configure src/
```

and created a diff file between the old configure.ac and the new configure.ac and put that in the patches directory. 

Once that is done, it would need testing on Solaris, OS X and Linux in addition to FreeBSD. 

Dave



---

archive/issue_comments_067728.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-22T00:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67728",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067729.json:
```json
{
    "body": "Apparently the following attached patch was all that was needed for now by Stephen Montgomery-Smith.    This could be due to the fairly major upgrades in Singular.\n\n```\n\n--- singular-3-1-3-3.p3/src/omalloc/configure-orig\t2012-01-21 19:51:08.000000000 +0000\n+++ singular-3-1-3-3.p3/src/omalloc/configure\t2012-01-21 19:51:32.000000000 +0000\n@@ -1293,9 +1293,6 @@\n   echo \"$ac_t\"\"no\" 1>&6\n fi\n \n-if test \"$ac_cv_prog_AR\" != ar; then\n-  { echo \"configure: error: *** ar program not found\" 1>&2; exit 1; }\n-fi\n for ac_prog in perl\n do\n # Extract the first word of \"$ac_prog\", so it can be a program name with args.\n```\n",
    "created_at": "2012-01-31T01:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67729",
    "user": "https://github.com/kcrisman"
}
```

Apparently the following attached patch was all that was needed for now by Stephen Montgomery-Smith.    This could be due to the fairly major upgrades in Singular.

```

--- singular-3-1-3-3.p3/src/omalloc/configure-orig	2012-01-21 19:51:08.000000000 +0000
+++ singular-3-1-3-3.p3/src/omalloc/configure	2012-01-21 19:51:32.000000000 +0000
@@ -1293,9 +1293,6 @@
   echo "$ac_t""no" 1>&6
 fi
 
-if test "$ac_cv_prog_AR" != ar; then
-  { echo "configure: error: *** ar program not found" 1>&2; exit 1; }
-fi
 for ac_prog in perl
 do
 # Extract the first word of "$ac_prog", so it can be a program name with args.
```




---

archive/issue_comments_067730.json:
```json
{
    "body": "The patch by Stephen Montgomery-Smith, reported above by kcrisman, is only needed because when building using the FreeBSD port math/sage, the program ar is replaced by another program.\n\nIt would be really great if these three lines could be removed from the configure file.  As best as I can tell, they serve no purpose whatsoever for any OS.",
    "created_at": "2012-04-08T15:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67730",
    "user": "https://trac.sagemath.org/admin/accounts/users/stephen"
}
```

The patch by Stephen Montgomery-Smith, reported above by kcrisman, is only needed because when building using the FreeBSD port math/sage, the program ar is replaced by another program.

It would be really great if these three lines could be removed from the configure file.  As best as I can tell, they serve no purpose whatsoever for any OS.



---

archive/issue_comments_067731.json:
```json
{
    "body": "I've reported this upstream at [this Singular ticket](http://www.singular.uni-kl.de:8002/trac/ticket/418).",
    "created_at": "2012-04-15T02:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67731",
    "user": "https://github.com/kcrisman"
}
```

I've reported this upstream at [this Singular ticket](http://www.singular.uni-kl.de:8002/trac/ticket/418).



---

archive/issue_comments_067732.json:
```json
{
    "body": "I quote from the ticket:\n\n```\n\nfixed: do not abort configure, if ar is not found\n\nThis allows to define a different ar program\nbut if none is found, you are on your own.\nWill be changed with the new version anyway.\n```\n\n\nThis is pretty enigmatic.\n\nAnyway, this patch and the following diff for spkg-install are doing it for the [FreeBSD port](http://www.freebsd.org/cgi/cvsweb.cgi/ports/math/sage/).\n\n\n```diff\n--- singular-3-1-3-3.p6/spkg-install-orig\t2012-04-08 01:57:01.000000000 +0000\n+++ singular-3-1-3-3.p6/spkg-install\t2012-04-08 01:58:19.000000000 +0000\n@@ -108,7 +108,7 @@\n \n     patches=\"assert.h.diff sing_win.cc.diff Minor.h.patch os_x_ppc.patch \\\n \tSingular.configure.patch make_parallel.patch Singular.Makefile.in.shared.patch \\\n-\tfactory.GNUmakefile.in.patch\"\n+\tfactory.GNUmakefile.in.patch omalloc.configure.patch\"\n \n     if [ \"$UNAME\" = \"CYGWIN\" ]; then\n         patches=\"$patches IntegerProgramming-Makefile.in.diff\"\n```\n\n\nThis would have to be made into an spkg, of course.",
    "created_at": "2012-06-20T19:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67732",
    "user": "https://github.com/kcrisman"
}
```

I quote from the ticket:

```

fixed: do not abort configure, if ar is not found

This allows to define a different ar program
but if none is found, you are on your own.
Will be changed with the new version anyway.
```


This is pretty enigmatic.

Anyway, this patch and the following diff for spkg-install are doing it for the [FreeBSD port](http://www.freebsd.org/cgi/cvsweb.cgi/ports/math/sage/).


```diff
--- singular-3-1-3-3.p6/spkg-install-orig	2012-04-08 01:57:01.000000000 +0000
+++ singular-3-1-3-3.p6/spkg-install	2012-04-08 01:58:19.000000000 +0000
@@ -108,7 +108,7 @@
 
     patches="assert.h.diff sing_win.cc.diff Minor.h.patch os_x_ppc.patch \
 	Singular.configure.patch make_parallel.patch Singular.Makefile.in.shared.patch \
-	factory.GNUmakefile.in.patch"
+	factory.GNUmakefile.in.patch omalloc.configure.patch"
 
     if [ "$UNAME" = "CYGWIN" ]; then
         patches="$patches IntegerProgramming-Makefile.in.diff"
```


This would have to be made into an spkg, of course.



---

archive/issue_comments_067733.json:
```json
{
    "body": "Okay, [here](https://github.com/Singular/Sources/blob/spielwiese/omalloc/configure.ac#L110) is the current Singular code, which raises a message but doesn't stop compiling.",
    "created_at": "2012-06-20T19:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67733",
    "user": "https://github.com/kcrisman"
}
```

Okay, [here](https://github.com/Singular/Sources/blob/spielwiese/omalloc/configure.ac#L110) is the current Singular code, which raises a message but doesn't stop compiling.



---

archive/issue_comments_067734.json:
```json
{
    "body": "This has been fixed in sage-5.4, because it is fixed singular-3-1-5.p1.\n\nSo I suppose this ticket can be closed.",
    "created_at": "2012-09-12T03:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67734",
    "user": "https://trac.sagemath.org/admin/accounts/users/stephen"
}
```

This has been fixed in sage-5.4, because it is fixed singular-3-1-5.p1.

So I suppose this ticket can be closed.



---

archive/issue_comments_067735.json:
```json
{
    "body": "Good catch!  Sorry I haven't been better about helping move the !FreeBSD stuff along; I was nearly offline much of the summer, and since you are one of the only people to have such a machine easily available who frequents these tickets, it's hard to get independent review of the tickets.  Please please *please* keep reporting when these fixes are adopted upstream, it's so helpful!  Thanks.",
    "created_at": "2012-09-12T12:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67735",
    "user": "https://github.com/kcrisman"
}
```

Good catch!  Sorry I haven't been better about helping move the !FreeBSD stuff along; I was nearly offline much of the summer, and since you are one of the only people to have such a machine easily available who frequents these tickets, it's hard to get independent review of the tickets.  Please please *please* keep reporting when these fixes are adopted upstream, it's so helpful!  Thanks.



---

archive/issue_comments_067736.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-09-12T12:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67736",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_067737.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-09-13T22:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67737",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_067738.json:
```json
{
    "body": "Indeed, see #13237.",
    "created_at": "2012-09-13T22:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7832#issuecomment-67738",
    "user": "https://github.com/jdemeyer"
}
```

Indeed, see #13237.



---

archive/issue_events_008047.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-09-13T22:37:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7832",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7832#event-8047"
}
```
