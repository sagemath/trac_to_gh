# Issue 8191: Add iconv need for Solaris, and possibly Cygwin too.

Issue created by migration from https://trac.sagemath.org/ticket/8191

Original creator: drkirkby

Original creation time: 2010-02-05 10:32:33

Assignee: drkirkby

CC:  mhansen was

Keywords: iconv solaris cygwin

The latest version of R in Sage 2.10.1, needs a powerful version of iconv. The version of iconv in Solaris is not sufficiently powerful.  This is documented in the 'R Installation and Administration' manual under the _Solaris_ section.

http://cran.r-project.org/doc/manuals/R-admin.pdf


#3381 added a command line option to the configure script to disable the use of iconv. 

For a long time R has been reporting messages that this option would be removed, and it would be necessary to install iconv. Well that time has come.


```
checking for cblas_cdotu_sub in vecLib framework... no
checking iconv.h usability... yes
checking iconv.h presence... yes
checking for iconv.h... yes
checking for iconv... yes
checking whether iconv accepts "UTF-8", "latin1" and "UCS-*"... no
configure: error: a suitable iconv is essential
Error configuring R.

real    2m15.532s
user    0m47.020s
sys    1m9.582s
sage: An error occurred while installing r-2.10.1
```


So we must have an inconv package. I will create one. 

It looks as though this will be needed on Cygwin also - see #7319. 



---

Comment by drkirkby created at 2010-02-05 10:38:52

I'm cc'in Mike on this ticket, as I believe it has implications for his ticket #7319

Dave


---

Comment by drkirkby created at 2010-02-14 04:07:36

I've created iconv-1.13.1.spkg which is the latest release. 

I have *not* added the Mercurial repository, as I was not exactly sure how to do it. This will need to go as a standard package, and another part of Sage will need to ensure that inconv gets built. 

I've marked it as 'needs info' rather than for review, as at this stage there is no Mercurial repository. But perhaps people can test it out. 

http://boxen.math.washington.edu/home/kirkby/new-packages/iconv

I've personally tested it on the following. If the self-tests are uncommented, (see spkg-install), then all tests do pass except on Solaris 10 (SPARC), where ./check-subst dumps core in both 32-bit and 64-bit mode on two separate machines. 

 * sage.math Linux (defaults to 64-bit) 
 * bsd.math OS X (defaults to 64-bit)
 * OpenSolaris 06/2009 on a Sun Ultra 27 (Intel Xeon processor) - 32-bit
 * OpenSolaris 06/2009 on a Sun Ultra 27 (Intel Xeon processor) - 64-bit. 
 * Solaris 10 03/2005 on a Sun Blade 1000 (UltraSPARC III+ processor) - 32-bit 
 * Solaris 10 03/2005 on a Sun Blade 1000 (UltraSPARC III+ processor) - 64-bit 

There is still an issue with R 2.10.1 building on Solaris (SPARC), but it gets a lot further with this iconv package built. We can sort out the problems with R later. There are tons of options given to the R configure script, at least one of which is not valid. I suspect by changing the options and removing the invalid code in R's spkg-install file, then R can be made to build on Solaris. 

Dave


---

Comment by drkirkby created at 2010-02-14 04:07:36

Changing status from new to needs_info.


---

Comment by drkirkby created at 2010-02-15 11:28:57

I believe the iconv package is now ready for review. 

 * spkg-check has been added. 
 * The Mercurial repository has been added. 
 * As shown below, iconv is tested by R and found to be suitable. 


```
Disabling libiconv support on Solaris
checking iconv.h usability... yes
checking iconv.h presence... yes
checking for iconv.h... yes
checking for iconv... in libiconv
checking whether iconv accepts "UTF-8", "latin1" and "UCS-*"... yes
checking for iconvlist... yes
checking for iconv... yes
```


The message 


```
Disabling libiconv support on Solaris
```

is from R's spkg-install, so needs to be removed. That is ticket #8272

It should be noted that.  
 * The test failure seen on Solaris 10 (SPARC) but not on OS X, Linux or OpenSolaris has a trac item for it. #8271
 * The failure of iconv's 'make check' to actually exit with a non-zero exit code when it encounters a failure has a trac ticket for it #8270.


---

Comment by drkirkby created at 2010-02-15 11:28:57

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-02-15 11:28:57

Changing component from solaris to packages.


---

Comment by drkirkby created at 2010-02-15 11:33:19

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-02-15 11:33:19

Oops, I forget to attach the revised spkg/install and spkg/standard/deps. I'll do that in a minute.


---

Attachment

New $SAGE_ROOT/spkg/install to add support for the new iconv package


---

Attachment

Diff for for $SAGE_ROOT/spkg/install


---

Comment by drkirkby created at 2010-02-15 11:52:58

New $SAGE_ROOT/spkg/standard/deps


---

Attachment

Diff file for $SAGE_ROOT/spkg/standard/deps


---

Attachment

I've attached the following two files, in addition to diffs to their originals. Neither file appear to be are under revision control, so I assume these two files will have to be manually integrated.  


```
$SAGE_ROOT/spkg/standard/deps 
$SAGE_ROOT/spkg/install 
```


I've made gdmodule, Python and R all depend on iconv, as all of them check for iconv. 

*This is now ready for review!!!*

Dave


---

Comment by drkirkby created at 2010-02-15 11:59:02

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-02-17 00:15:02

I'm attaching a Mercurial patch too


---

Comment by drkirkby created at 2010-02-17 00:15:54

Mercurial patch


---

Attachment

I called the Mercurial patch "R.patch", which was probably not a very sensible name. It is for the iconv package.


---

Comment by mvngu created at 2010-02-21 21:15:53

The new iconv package builds on sage.math, bsd.math, rosemary.math, t2.math, Skynet machines (cleo and iras), and Cygwin (winxp1 on boxen.math). 




*Note to release manager:* Replace the current file `spkg/install` with [install](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/install). Also replace the current file `spkg/standard/deps` with [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/deps). Both `install` and `deps` are not under revision control, so one has to replace them with updated versions. Make sure to turn on the executable bits of `install`.


---

Comment by mvngu created at 2010-02-21 21:15:53

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-27 07:21:34

At #8306, I've added iconv to gd's dependencies to keep make from building gd too early.  Should we do that here?


---

Comment by drkirkby created at 2010-02-27 14:15:47

Yes, well spotted. You were right to add it to #8036. 

In practice however it will make no difference on Linux, Solaris or OS X as they all come with a version of iconv suitable for gd. It is only R on Solaris which needs this iconv package built, as the iconv shipped with Solaris is not suitable for building the latest versions of R. 

Since Minh has already tested this on multiple machines and given it positive review, I'm reluctant to change anything now, which might delay the package getting into Sage, as it would then need reviewing again. 

Delaying this getting into Sage will stop Sage working on Solaris. Whether iconv gets built before or after gd will make no difference on any supported platform. 

Since #8306 will have a dependancy on this, you have already taken care of the gd dependancy, so again I think that points to the fact there is no need to change this. 

Dave


---

Comment by drkirkby created at 2010-02-27 14:17:26

Replying to [comment:11 drkirkby]:
> Yes, well spotted. You were right to add it to #8036. 

Oops, you were right to add it to #8306 was what I meant to write.


---

Comment by drkirkby created at 2010-03-01 16:24:06

Changing priority from major to blocker.


---

Comment by mvngu created at 2010-03-02 19:23:32

apply to script repository; depends on #8307


---

Attachment

The iconv spkg installs a binary called "iconv" to `SAGE_LOCAL/bin`, a directory which is under revision control. Usually, we don't put executable binaries under revision control. After installing the iconv spkg, I get this:

```
[mvngu@sage bin]$ hg st
? iconv
```

The file `.hgignore` needs to be configured to ignore this file. I have attached [trac_8191-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/trac_8191-reviewer.patch) which does this. Apply that patch to the script repository. It depends on the patch at #8307. Only my patch needs review by anyone but me.


---

Comment by mvngu created at 2010-03-02 19:27:57

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-03-02 19:28:07

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-03-02 20:29:39

Thanks Minh. Yes, that makes perfect sense. Positive review from me.


---

Comment by drkirkby created at 2010-03-02 20:29:39

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 22:38:46

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 22:38:46

Merged in this order:

 1. Replace current "install" under `SAGE_ROOT/spkg` with [install](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/install).
 1. Replace current "deps" under `SAGE_ROOT/spkg/standard` with [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/deps).
 1. Merged [iconv-1.13.1.spkg](http://boxen.math.washington.edu/home/kirkby/new-packages/iconv/iconv-1.13.1.spkg) in the standard spkg repository.
 1. Merged [trac_8191-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8191/trac_8191-reviewer.patch) in the script repository.


---

Comment by mvngu created at 2010-03-04 03:58:29

Replying to [comment:11 drkirkby]:
> In practice however it will make no difference on Linux, Solaris or OS X as they all come with a version of iconv suitable for gd.

Sage 4.3.4.alpha0 fails to build on a Fedora Linux system because iconv is not yet part of the dependency rule for building gd. This issue is now tracked at #8432.
