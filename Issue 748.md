# Issue 748: iml autohell

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-24 20:58:43

Assignee: was

CC:  jpflori


```

2. For iml-1.0.1.p8, there is some autotools problem
that I have not been able to track down.  Is
everything up-to-date with configure, etc.
for this package?
```



---

Comment by was created at 2007-09-25 05:20:49

I've reverted the iml package that will be distributed with Sage to version 1.0.1.p6 (from sage-2.8.4)
until this gets resolved.


---

Comment by was created at 2007-09-25 05:21:05

The 1.0.1.p8 version is in sage-2.8.5


---

Comment by mabshoff created at 2008-06-15 23:52:51

A couple commets:

 * Arne merged the nullspace patch and a couple of the other fixes. Some of the other fixes no longer apply
 * spkg-install does odd things, i.e  fall back to non-ATLAS which is no longer needed
 * The SPKG needs some general cleanup
 * on OSX without creating 'repl' the build on the vanilla sources fails
 
Arne is putting together some 1.0.3 release which we can then test in Sage

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-15 23:52:51

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-06-15 23:52:51

Changing assignee from was to mabshoff.


---

Comment by jason created at 2009-10-06 19:22:12

Changing status from new to needs_info_new.


---

Comment by leif created at 2011-09-13 09:30:37

I'm closing this as a duplicate of #9568.


---

Comment by leif created at 2011-09-13 09:30:37

Changing keywords from "" to "spkg upgrade".


---

Comment by leif created at 2011-09-13 09:30:37

Resolution: duplicate


---

Comment by drkirkby created at 2012-05-28 05:20:56

Is it not more sensible for the duplicated ticket to be closed, rather than the original one? That's the way gcc handle it. If you report something that's a duplicate of an older ticket, the newer ticket gets closed - not the older one. 


Dave


---

Comment by kini created at 2012-05-28 05:52:45

I guess it depends on which ticket has the most useful comments / patches and the most relevant people CC'd to it. At least #13027 has an SPKG attached. #9568 and this ticket certainly have more useful comments than #13027, though.


---

Comment by kini created at 2012-05-28 05:55:36

Resolution changed from duplicate to 


---

Comment by kini created at 2012-05-28 05:55:36

I have no objection to reopening this ticket, anyway. In any case, once someone actually solves the problem, all three will be closed.


---

Comment by kini created at 2012-05-28 05:55:36

Changing status from closed to new.


---

Comment by kini created at 2012-05-28 05:55:36

Changing keywords from "spkg upgrade" to "spkg upgrade iml".


---

Comment by fbissey created at 2012-05-28 09:53:18

I have a patch for repl problem in sage-on-gentoo but all the autotool chain needs to be regenerated after you apply it.
[https://github.com/cschwan/sage-on-gentoo/blob/master/sci-libs/iml/files/iml-1.0.3-repl_removal.patch](https://github.com/cschwan/sage-on-gentoo/blob/master/sci-libs/iml/files/iml-1.0.3-repl_removal.patch)


---

Comment by kini created at 2012-05-28 16:32:44

Thanks, that will help. We cannot run autotools at build time, only at packaging time, since we don't have autotools as a dependency of Sage, nor do we package it in Sage. So rather than including your patch I guess I should apply it, run autotools, and then save *that* diff as a patch to apply at build time.

Before seeing your diff I had solved the repl problem like this:


```diff
diff --git a/repl/Makefile.am b/repl/Makefile.am
index 4cf001b..7be2e86 100644
--- a/repl/Makefile.am
+++ b/repl/Makefile.am
`@``@` -1,4 +1,4 `@``@`
 noinst_LTLIBRARIES      = librepl.la
-librepl_la_SOURCES   =
+librepl_la_SOURCES   = dummy.c
 librepl_la_LIBADD    = `@`LTLIBOBJS`@`
 
diff --git a/repl/Makefile.in b/repl/Makefile.in
index 5c65bfa..ba963ec 100644
--- a/repl/Makefile.in
+++ b/repl/Makefile.in
`@``@` -51,7 +51,7 `@``@` CONFIG_HEADER = $(top_builddir)/config.h
 CONFIG_CLEAN_FILES =
 LTLIBRARIES = $(noinst_LTLIBRARIES)
 librepl_la_DEPENDENCIES = `@`LTLIBOBJS`@`
-am_librepl_la_OBJECTS =
+am_librepl_la_OBJECTS = dummy.lo
 librepl_la_OBJECTS = $(am_librepl_la_OBJECTS)
 DEFAULT_INCLUDES = -I. -I$(srcdir) -I$(top_builddir)
 depcomp = $(SHELL) $(top_srcdir)/config/depcomp
`@``@` -172,7 +172,7 `@``@` sharedstatedir = `@`sharedstatedir`@`
 sysconfdir = `@`sysconfdir`@`
 target_alias = `@`target_alias`@`
 noinst_LTLIBRARIES = librepl.la
-librepl_la_SOURCES = 
+librepl_la_SOURCES = dummy.c
 librepl_la_LIBADD = `@`LTLIBOBJS`@`
 all: all-am
 
`@``@` -226,6 +226,7 `@``@` distclean-compile:
 	-rm -f *.tab.c
 
 `@`AMDEP_TRUE`@``@`am__include`@` `@`am__quote`@`$(DEPDIR)/realloc.Plo`@`am__quote`@`
+`@`AMDEP_TRUE`@``@`am__include`@` `@`am__quote`@`./$(DEPDIR)/dummy.Plo`@`am__quote`@`
 
 .c.o:
 `@`am__fastdepCC_TRUE`@`	if $(COMPILE) -MT $`@` -MD -MP -MF "$(DEPDIR)/$*.Tpo" -c -o $`@` $<; \
`@``@` -367,7 +368,7 `@``@` clean-am: clean-generic clean-libtool clean-noinstLTLIBRARIES \
 	mostlyclean-am
 
 distclean: distclean-am
-	-rm -rf $(DEPDIR)
+	-rm -rf $(DEPDIR) ./$(DEPDIR)
 	-rm -f Makefile
 distclean-am: clean-am distclean-compile distclean-generic \
 	distclean-libtool distclean-tags
`@``@` -393,7 +394,7 `@``@` install-man:
 installcheck-am:
 
 maintainer-clean: maintainer-clean-am
-	-rm -rf $(DEPDIR)
+	-rm -rf $(DEPDIR) ./$(DEPDIR)
 	-rm -f Makefile
 maintainer-clean-am: distclean-am maintainer-clean-generic
 
diff --git a/repl/dummy.c b/repl/dummy.c
new file mode 100644
index 0000000..39e7442
--- /dev/null
+++ b/repl/dummy.c
`@``@` -0,0 +1 `@``@`
+void dummy () { return; }
diff --git a/src/Makefile.in b/src/Makefile.in
index e9ca293..a1f5a81 100644
--- a/src/Makefile.in
+++ b/src/Makefile.in
`@``@` -223,6 +223,7 `@``@` libiml_la_CFLAGS = $(AM_CFLAGS)
 libiml_la_LIBADD = $(EXTERNLIB) \
 	 	   $(top_builddir)/repl/librepl.la
 
+libiml_la_LDFLAGS = -version-info 1:0:1
 all: all-am
 
 .SUFFIXES:
```


The first hunk is manually edited, as is the hunk adding the file `repl/dummy.c`; the rest are created by running automake in the src directory.

There are a couple of things that worry me, such as the `-version-info 1:0:1` near the end of the diff. Does that mean that autotools are misunderstanding the version of IML as 1.0.1 instead of 1.0.3? Why does a similar line not already exist in that file? As far as I can tell, I made sure I was using the same versions of autotools that the authors of IML were - autoconf 2.59, automake 1.9.6, and libtool 1.5.22.

Anyway, I'll try again with your patch instead of this dummy function and see what's different. This time I'll also try the whole autotools suite by running `autoreconf -i` (as recommended to me by Jeroen) - is this what you recommend too, fbissey?


---

Comment by kini created at 2012-05-28 16:34:58

Oh, I should mention that the patch I pasted in the previous comment actually does work to get rid of the build failure caused in `repl/`. Now the problem seems to be something with dynamic linking. To copy from #13027:


```
creating test-largeentry
dyld: lazy symbol binding failed: Symbol not found: _cblas_dgemm
  Referenced from: /Users/wstein/build/sage-5.0/spkg/build/iml-1.0.3.p0/src/src/.libs/libiml.0.dylib
  Expected in: flat namespace

dyld: Symbol not found: _cblas_dgemm
  Referenced from: /Users/wstein/build/sage-5.0/spkg/build/iml-1.0.3.p0/src/src/.libs/libiml.0.dylib
  Expected in: flat namespace

/bin/sh: line 1: 74987 Trace/BPT trap          ${dir}$tst
FAIL: test-smallentry
dyld: lazy symbol binding failed: Symbol not found: _cblas_dgemm
  Referenced from: /Users/wstein/build/sage-5.0/spkg/build/iml-1.0.3.p0/src/src/.libs/libiml.0.dylib
  Expected in: flat namespace

dyld: Symbol not found: _cblas_dgemm
  Referenced from: /Users/wstein/build/sage-5.0/spkg/build/iml-1.0.3.p0/src/src/.libs/libiml.0.dylib
  Expected in: flat namespace

/bin/sh: line 1: 75006 Trace/BPT trap          ${dir}$tst
FAIL: test-largeentry
===================
2 of 2 tests failed
===================
make[2]: *** [check-TESTS] Error 1
make[1]: *** [check-am] Error 2
make: *** [check-recursive] Error 1
Error testing IML
```


As you can see, this is during the testing phase, so building completes successfully with the patch I pasted in the previous comment.


---

Comment by kini created at 2012-05-28 16:37:27

If after five years we haven't heard anything from upstream, by the way, I don't think we should any longer "wait on upstream", so I'm changing the title of the ticket...


---

Comment by kini created at 2012-05-28 18:02:07

I spoke too soon - Arne Storjohann just contacted me to tell me that he has corrected the links on the IML webpage for older versions of IML, so now I have been able to produce a diff between clean upstream 1.0.1 and the version in the current standard spkg iml-1.0.1.p14.spkg. I will attach it after posting this comment, for reference.


---

Comment by fbissey created at 2012-05-28 19:28:50

I don't think I ever ran the test with the sage-on-gento ebuild on OS X. I will try that.What OS X version were you testing?


---

Comment by fbissey created at 2012-05-29 02:09:01

Reread the whole thing again. Yes autoreconf -i sounds good. Just for reference while upstream claims you need atlas cblas it doesn't use any atlas specific bits but the configure script is set to find atlas and nothing else.

When we regenerate configure we usually don't ship it as a patch, the diff is usually too big. Historically in the case of cddlib Id on't think we ship pristine source in that case but the patch we used and the recipe to regenerate configure and friends. cddlib is a spkg you could look at for reference.

Tests pass on sage-on-gentoo on OS X 10.5.8 by the way.


---

Comment by kini created at 2012-05-29 16:26:42

Changing keywords from "spkg upgrade iml" to "spkg upgrade iml sd40.5".


---

Comment by kini created at 2012-08-09 10:49:03

Hi jpflori! I was working on this a couple months ago, and as I recall I was running into a similar autotools dilemma to the one you were discussing on sage-devel recently. I never did get it to build on OS X...

Here's an unfinished SPKG if you want to take a look at what I did so far (not much): http://boxen.math.washington.edu/home/keshav/files/iml-1.0.3.p0.unfinished.spkg


---

Comment by fbissey created at 2012-08-09 10:56:44

What is happening to you on OS X?


---

Comment by kini created at 2012-08-09 11:08:03

As I recall, tests were failing because the built binaries weren't linking to the system's BLAS properly, or something. See earlier comments on this ticket and on #13027.


---

Comment by kini created at 2012-08-09 11:16:46

(Sorry, I see that I said I didn't get it to _build_ on OS X - that's incorrect, I got it to _build_ but not to _work_.)


---

Comment by fbissey created at 2012-08-09 11:19:08

Yes of course I should really have tried to be more helpful there. I'll look at what you have done so far. Using atlas on OS X may help here.


---

Comment by jpflori created at 2012-08-09 16:03:48

I've got no access to OS X based computers, so if the problem is mainly about that, I'll have trouble helping...

I mainly want to add -no-undefined to LDFLAGS on Cygwin (not the proper solution, if it works which has to be checked... we should only add it to the lib..._la_LDFLAGS in some Makefile.am, but that's looking for trouble, and adding it to LDFLAGS should be ok, even though it will be used all the time, even when it's useless, but a priori not harmful).


---

Comment by fbissey created at 2012-08-10 03:14:51

OK there are two options:
1 - we wait for sage to default to ATLAS-3.10 on OS X and use that
2 - rewrite the configure.ac to provide any cblas we want and regenerate configure. We are going to regenerate configure in the process anyway.


---

Comment by kini created at 2012-08-10 07:14:07

Do you have some nonzero expectation of Sage defaulting to building and using ATLAS on OS X rather than using the BLAS that's built into the operating system? When I was working on this I assumed waiting for ATLAS on OS X was a non-option, but maybe you know something I don't.

I only saw the second option remaining, and that's actually why I sort of gave up on this - I didn't want to start writing autotools scripts if possible, after seeing David Kirkby's dire warnings on sage-devel to the effect that in order to write autotools scripts you have to carefully read the autotools manual from cover to cover first...

I suppose a third option would be to ask the iml authors themselves to support generic BLAS.


---

Comment by fbissey created at 2012-08-10 09:02:34

You could say I know enough. And we have already done the work on gentoo. The gentoo solution itself cannot be adopted as it rely on blas/lapack installing pkgconfig files. But I know enough. The easiest thing is just to remove all traces of Atlas autodetection and provide the necessary stuff by compile flags. More sophisticated is to include a "--with-cblas" statement that would be basically do the same thing.

I am otherwise positive that #10508 is opening the possibility of ATLAS on OS X - but all spkg using blas/lapack need to be adjusted for it to be useful.

Patching the detection can be done orthogonally to getting atlas, the autodetection is a tricky business in this case.


---

Comment by fbissey created at 2012-10-26 10:43:41

I think I can spend a little bit of time sorting stuff on this in the next few days. I will try to future proof it for #10508 so that there is no need to change the spkg when it is changed to positive review.


---

Comment by jdemeyer created at 2013-06-12 12:46:02

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-06-12 12:47:43

*not yet doctested* but at least the spkg and its testsuite work on Linux and OS X.


---

Comment by leif created at 2013-06-12 13:28:35

I still get

```
./configure: line 18624: -O2: command not found
```



---

Comment by jdemeyer created at 2013-06-12 16:16:28

Replying to [comment:37 leif]:
> I still get
> {{{
> ./configure: line 18624: -O2: command not found
> }}}
Fixed in new spkg.

Doctests on boxen.math pass.


---

Comment by jpflori created at 2013-06-14 11:28:07

I already checked the spkg looks sane and installs fine.
Sage still pass its (not long) tests.

I just have to check the changes in the patches and I'll give it positive review.


---

Comment by jpflori created at 2013-06-14 12:52:14

Why merge tinyatlas.patch into sage1.patch?

On top of that I don't really get the use of the tinyatlas patch.
The function it defines (in a header file) is used nor in IML nor in Sage.
I'm testing Sage without it (no problems for IML).

So maybe renaming sage1.patch to memory.patch and discarding tinyatlas.patch would be enough.
And lets move the sage3_memleak.patch to memleak.patch while at it.


---

Comment by jdemeyer created at 2013-06-14 13:06:07

Replying to [comment:40 jpflori]:
> Why merge tinyatlas.patch into sage1.patch?
Because those patches seem related: `sage1.patch` adds some include for `tinyatlas.h`.

> On top of that I don't really get the use of the tinyatlas patch.
> The function it defines (in a header file) is used nor in IML nor in Sage.
That's certainly not true. The files `RNSop.c` and `certsolve.c` in the `src/src` directory in `IML` use `catlas_daxpby()`.

My guess is that's a function which normally comes from ATLAS, but which is needed on systems where ATLAS is not installed.


---

Comment by jpflori created at 2013-06-14 13:09:23

Replying to [comment:41 jdemeyer]:
> Replying to [comment:40 jpflori]:
> > Why merge tinyatlas.patch into sage1.patch?
> Because those patches seem related: `sage1.patch` adds some include for `tinyatlas.h`.
Ok, i thought the include was in tinyatlas.h as well, so I did not check.
> 
> > On top of that I don't really get the use of the tinyatlas patch.
> > The function it defines (in a header file) is used nor in IML nor in Sage.
> That's certainly not true. The files `RNSop.c` and `certsolve.c` in the `src/src` directory in `IML` use `catlas_daxpby()`.
> 
It seems to be true with IML 1.0.3 but not with 1.0.1 indeed.
(I mean the daxpby function was needed in 1.0.1 but is not anymore in 1.0.3.)
> My guess is that's a function which normally comes from ATLAS, but which is needed on systems where ATLAS is not installed.


---

Comment by jpflori created at 2013-06-14 13:11:28

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2013-06-14 13:12:34

Replying to [comment:42 jpflori]:
> It seems to be true with IML 1.0.3 but not with 1.0.1.
OK, right, I checked the old sources.


---

Comment by jdemeyer created at 2013-06-14 13:16:35

I confirm that `catlas_daxpby()` is indeed nowhere used outside of the ATLAS sources.

Working on new spkg...


---

Comment by jdemeyer created at 2013-06-14 13:23:27

Applying the following changes:

```diff
diff --git a/SPKG.txt b/SPKG.txt
--- a/SPKG.txt
+++ b/SPKG.txt
`@``@` -32,21 +32,27 `@``@`

 === Patches ===

- * rename_lift.patch: Change lift to iml_lift in padiclift.* and
-   nonsingsolve.*, since otherwise  on OSX you'll have horrible weird
-   conflict problems.
+ * blas_headers.patch: Add BLAS header files from GSL, needed in case
+   ATLAS has not been installed.
+ * build.patch: Made build scripts that work.
  * configure_default_cflags.patch: get rid of the following error
    during configure:
      ./configure: line 18624: -O3: command not found
- * Modified some of the examples, and made build scripts that work.
+ * examples.patch: Modified some of the examples.
+ * memleak.patch: use mpz_set_ui instead of mpz_init_set_ui on mpz
+   which is already allocated.
+ * remove_repl.patch: Do not build/install src/repl at all, since it
+   does nothing anyway and creating empty archives fails on OS X.

 == Changelog ==

 === iml-1.0.3.p0 (Jeroen Demeyer, 12 June 2013) ===
  * #748: Upgrade to latest upstream version, rebase patches.
  * Remove rename_lift.patch and sage2.patch, which were upstreamed.
- * Merged tinyatlas.patch into sage1.patch.
- * Apply sage3_memleak.patch in all 3 places with similar code.
+ * Removed tinyatlas.patch and #include "tinyatlas.h"
+ * Removed sage1.patch
+ * Apply sage3_memleak.patch in all 3 places with similar code, rename
+   to memleak.patch
  * Use -O3 optimization level by default.
  * Add configure_default_cflags.patch.

diff --git a/patches/sage3_memleak.patch b/patches/memleak.patch
rename from patches/sage3_memleak.patch
rename to patches/memleak.patch
diff --git a/patches/sage1.patch b/patches/sage1.patch
deleted file mode 100644
--- a/patches/sage1.patch
+++ /dev/null
`@``@` -1,80 +0,0 `@``@`
-diff -ruN b/src/RNSop.c a/src/RNSop.c
---- b/src/RNSop.c      2006-11-23 22:25:23.000000000 +0100
-+++ a/src/RNSop.c      2013-06-10 23:05:18.872404179 +0200
-`@``@` -46,6 +46,7 `@``@`
- 
- 
- #include "RNSop.h"
-+#include "tinyatlas.h"
- 
- /*
-  *
-diff -ruN b/src/memalloc.c a/src/memalloc.c
---- b/src/memalloc.c   2006-11-23 22:25:23.000000000 +0100
-+++ a/src/memalloc.c   2013-06-10 23:05:18.872404179 +0200
-`@``@` -48,13 +48,16 `@``@`
- 
- #include "error.h"
- #include "common.h"
-+#include "stdio.h"
- 
- void *
- xmalloc (size_t num)
- {
-   void * new = malloc(num);
--  if (!new)
--    iml_fatal ("Memory exhausted");
-+  if (!new) {
-+    printf("%ul\n", num);
-+    iml_fatal ("Memory exhausted in xmalloc");
-+  }
-   return new;
- }
- 
-`@``@` -65,8 +68,10 `@``@`
-   if (!p)
-     return xmalloc(num);
-   new = realloc(p, num);
--  if (!new)
--    iml_fatal("Memory exhausted");
-+  if (!new) {
-+    printf("%ul\n", num);
-+    iml_fatal("Memory exhausted in xrealloc");
-+  }
-   return new;
- }
- 
-`@``@` -76,8 +81,10 `@``@`
- {
- #if HAVE_CALLOC
-   void * new = calloc(num, size);
--  if (!new)
--    iml_fatal("Memory exhausted");
-+  if (!new) {
-+    printf("%ul\n", num);
-+    iml_fatal("Memory exhausted in xcalloc");
-+  }
- #else
-   void * new = xmalloc(num*size);
-   bzero(new, num*size);
-diff -ruN iml-1.0.1-sage/src/tinyatlas.h src/src/tinyatlas.h
---- iml-1.0.1-sage/src/tinyatlas.h     1970-01-01 01:00:00.000000000 +0100
-+++ src/src/tinyatlas.h        2007-03-01 04:11:42.000000000 +0100
-`@``@` -0,0 +1,17 `@``@`
-+/* 
-+Compute Y = alpha * X + beta * Y
-+
-+where 
-+   N = degree of each vector
-+   incX = X stride
-+   incY = Y stride
-+*/
-+
-+void catlas_daxpby(const int N, const double alpha, const double *X,
-+const int incX, const double beta, double *Y, const int incY) 
-+{
-+  int i;
-+  for(i=0; i < N; i++) {
-+    Y[i*incY] = alpha * X[i*incX] + beta * Y[i*incY];
-+  }
-+}
```



---

Attachment


---

Comment by jdemeyer created at 2013-06-14 13:27:23

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2013-06-14 13:27:46

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-19 12:24:23

Resolution: fixed


---

Comment by leif created at 2014-04-16 16:41:14

*Sign of life of IML upstream* on #14648 !!1!111!


---

Comment by leif created at 2014-04-16 16:42:58

Replying to [comment:50 leif]:
> *Sign of life of IML upstream* on #14648 !!1!111!

http://trac.sagemath.org/ticket/14648#comment:51 ff. that is.
