# Issue 7831: numpy-1.3.0.p2 fixes for FreeBSD

Issue created by migration from https://trac.sagemath.org/ticket/7831

Original creator: pjeremy

Original creation time: 2010-01-03 09:14:11

Assignee: pjeremy

* !__init!__.py needs a sage-specific patch to prefer sage_fortran on FreeBSD.  Without this, numpy reports:

```
Running from numpy source directory.
F2PY Version 2
blas_opt_info:
blas_mkl_info:
  libraries mkl,vml,guide not found in /home/peter/sage/sage-4.3/local/lib
  NOT AVAILABLE

atlas_blas_threads_info:
Setting PTATLAS=ATLAS
  libraries ptf77blas,ptcblas,atlas_r not found in /home/peter/sage/sage-4.3/local/lib
  NOT AVAILABLE

atlas_blas_info:
  libraries f77blas,cblas,atlas_r not found in /home/peter/sage/sage-4.3/local/lib
  NOT AVAILABLE

/home/peter/sage/sage-4.3/spkg/build/numpy-1.3.0.p2/src/numpy/distutils/system_info.py:1383: UserWarning: 
    Atlas (http://math-atlas.sourceforge.net/) libraries not found.
    Directories to search for the libraries can be specified in the
    numpy/distutils/site.cfg file (section [atlas]) or by setting
    the ATLAS environment variable.
  warnings.warn(AtlasNotFoundError.__doc__)
blas_info:
  FOUND:
    libraries = ['blas']
    library_dirs = ['/home/peter/sage/sage-4.3/local/lib']
    language = f77

  FOUND:
```


This also causes matplotlib to die with

```
REQUIRED DEPENDENCIES
                 numpy: no
                        * You must install numpy 1.1 or later to build
                        * matplotlib.
```


   * By default, numpy references threaded atlas libraries, as well as a custom variant on the lapack library, on FreeBSD. The reasoning behind this is unclear - there is nothing in the numpy documentation to indicate whether a threaded or non-threaded atlas is needed and the publicly available SVN logs do not mention this code. A query to the numpy mailing list elicited a response that either threaded or non-threaded atlas can be used and suggesting that the special-casing for FreeBSD may be obsolete. By default, atlas is built non-threaded and r-2.6.1.p23 assumes a non-threaded atlas and fails when only the threaded libraries are installed. Based on this, the special casing for FreeBSD was removed from numpy - it now uses the same libraries irrespective of the host OS.  This part of the patch could potentially be integrated upstream but this has not been done yet.


---

Comment by pjeremy created at 2010-01-03 09:25:25

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-01-03 16:41:49

These changes look good to me.  Could you look over the ones at #7321?  I'll handle making an spkg with all of these rolled together.

Thanks!


---

Comment by mhansen created at 2010-01-03 16:41:49

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-13 07:22:12

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-02-13 07:22:12

Updated spkg at

http://sage.math.washington.edu/home/mvngu/spkg/standard/numpy/numpy-1.3.0.p3.spkg

which incorporates the patch [7831.numpy.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7831/7831.numpy.patch). This spkg needs review by anyone other than me.


---

Comment by mvngu created at 2010-02-13 07:22:24

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-06-22 23:09:30

Looks fine.  The the changes based on the newest spkg are at 

http://sage.math.washington.edu/home/mhansen/numpy-1.3.0.p4.spkg


---

Comment by mhansen created at 2010-06-22 23:09:30

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 05:34:44

There is another ticket updating numpy as well: #8010. These two conflicting spkg's need to be resolved.


---

Comment by rlm created at 2010-06-28 17:05:44

Changing status from positive_review to needs_work.


---

Comment by kcrisman created at 2010-11-03 12:58:19

Since #8010 has been closed, it would be helpful to know whether the changes here are still needed (which I can't test, unfortunately).


---

Comment by flawrence created at 2010-11-05 06:50:13

Can someone verify whether this is fixed by other changes to the numpy package in 4.6.1alpha0?


---

Comment by pjeremy created at 2010-11-18 19:01:06

The __init__.py changes don't appear to be needed any longer but the remaining fixes are still required.


---

Attachment

Note that numpy 1.5.1 is on the way to Sage - #10792.   It would be great to get this incorporated with that.


---

Comment by kcrisman created at 2012-01-31 02:05:19

Apparently [Stephen Montgomery-Smith](http://groups.google.com/group/sage-devel/browse_thread/thread/2feec7c5511c4ae5/857a00a9aa271f17) has had some success with this recently as a "port".


---

Comment by kcrisman created at 2012-06-20 15:56:31

More success at [this thread](https://groups.google.com/forum/?fromgroups#!topic/sage-devel/yPGIKHRSANs).  Checking whether it was with a system version or Sage version.


---

Comment by kcrisman created at 2012-06-20 15:56:31

Changing status from needs_work to needs_info.


---

Comment by kcrisman created at 2012-06-20 18:24:38

Just noting here that although this was the Sage version, Numpy upstream still has the special FreeBSD code, [here as of June 2012](https://github.com/numpy/numpy/blob/master/numpy/distutils/system_info.py#L972), so the patch definitely hasn't been applied.  My sense is that probably the R upgrades over the years is what made this obsolete.

So I'm putting this to positive review as it builds (and so does R) and passes the overwhelming majority of tests on FreeBSD 8 and 9, but leaving this info here in case in certain unusual cases this ends up being a problem after all.


---

Comment by kcrisman created at 2012-06-20 18:24:38

Changing status from needs_info to needs_review.


---

Comment by kcrisman created at 2012-06-20 18:25:05

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-07-04 07:11:32

Resolution: duplicate
