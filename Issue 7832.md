# Issue 7832: singular-3-1-0-4-20090818.p2 - fix compilation on FreeBSD

Issue created by migration from https://trac.sagemath.org/ticket/7832

Original creator: pjeremy

Original creation time: 2010-01-03 10:10:09

Assignee: pjeremy

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



---

Comment by pjeremy created at 2010-01-03 10:11:18

Changing status from new to needs_review.


---

Attachment


---

Comment by drkirkby created at 2010-02-22 00:12:00

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

Comment by drkirkby created at 2010-02-22 00:12:00

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-01-31 01:56:00

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

Comment by stephen created at 2012-04-08 15:03:19

The patch by Stephen Montgomery-Smith, reported above by kcrisman, is only needed because when building using the FreeBSD port math/sage, the program ar is replaced by another program.

It would be really great if these three lines could be removed from the configure file.  As best as I can tell, they serve no purpose whatsoever for any OS.


---

Comment by kcrisman created at 2012-04-15 02:26:03

I've reported this upstream at [this Singular ticket](http://www.singular.uni-kl.de:8002/trac/ticket/418).


---

Comment by kcrisman created at 2012-06-20 19:03:34

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

Comment by kcrisman created at 2012-06-20 19:05:32

Okay, [here](https://github.com/Singular/Sources/blob/spielwiese/omalloc/configure.ac#L110) is the current Singular code, which raises a message but doesn't stop compiling.


---

Comment by stephen created at 2012-09-12 03:39:27

This has been fixed in sage-5.4, because it is fixed singular-3-1-5.p1.

So I suppose this ticket can be closed.


---

Comment by kcrisman created at 2012-09-12 12:09:32

Good catch!  Sorry I haven't been better about helping move the !FreeBSD stuff along; I was nearly offline much of the summer, and since you are one of the only people to have such a machine easily available who frequents these tickets, it's hard to get independent review of the tickets.  Please please _please_ keep reporting when these fixes are adopted upstream, it's so helpful!  Thanks.


---

Comment by kcrisman created at 2012-09-12 12:09:32

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-09-13 22:37:41

Resolution: duplicate


---

Comment by jdemeyer created at 2012-09-13 22:37:41

Indeed, see #13237.
