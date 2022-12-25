# Issue 7831: numpy-1.3.0.p2 fixes for FreeBSD

archive/issues_007831.json:
```json
{
    "body": "Assignee: @peterjeremy\n\n* !__init!__.py needs a sage-specific patch to prefer sage_fortran on FreeBSD.  Without this, numpy reports:\n\n```\nRunning from numpy source directory.\nF2PY Version 2\nblas_opt_info:\nblas_mkl_info:\n  libraries mkl,vml,guide not found in /home/peter/sage/sage-4.3/local/lib\n  NOT AVAILABLE\n\natlas_blas_threads_info:\nSetting PTATLAS=ATLAS\n  libraries ptf77blas,ptcblas,atlas_r not found in /home/peter/sage/sage-4.3/local/lib\n  NOT AVAILABLE\n\natlas_blas_info:\n  libraries f77blas,cblas,atlas_r not found in /home/peter/sage/sage-4.3/local/lib\n  NOT AVAILABLE\n\n/home/peter/sage/sage-4.3/spkg/build/numpy-1.3.0.p2/src/numpy/distutils/system_info.py:1383: UserWarning: \n    Atlas (http://math-atlas.sourceforge.net/) libraries not found.\n    Directories to search for the libraries can be specified in the\n    numpy/distutils/site.cfg file (section [atlas]) or by setting\n    the ATLAS environment variable.\n  warnings.warn(AtlasNotFoundError.__doc__)\nblas_info:\n  FOUND:\n    libraries = ['blas']\n    library_dirs = ['/home/peter/sage/sage-4.3/local/lib']\n    language = f77\n\n  FOUND:\n```\n\n\nThis also causes matplotlib to die with\n\n```\nREQUIRED DEPENDENCIES\n                 numpy: no\n                        * You must install numpy 1.1 or later to build\n                        * matplotlib.\n```\n\n\n* By default, numpy references threaded atlas libraries, as well as a custom variant on the lapack library, on FreeBSD. The reasoning behind this is unclear - there is nothing in the numpy documentation to indicate whether a threaded or non-threaded atlas is needed and the publicly available SVN logs do not mention this code. A query to the numpy mailing list elicited a response that either threaded or non-threaded atlas can be used and suggesting that the special-casing for FreeBSD may be obsolete. By default, atlas is built non-threaded and r-2.6.1.p23 assumes a non-threaded atlas and fails when only the threaded libraries are installed. Based on this, the special casing for FreeBSD was removed from numpy - it now uses the same libraries irrespective of the host OS.  This part of the patch could potentially be integrated upstream but this has not been done yet.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7831\n\n",
    "created_at": "2010-01-03T09:14:11Z",
    "labels": [
        "component: porting: bsd",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "numpy-1.3.0.p2 fixes for FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7831",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: @peterjeremy

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

Issue created by migration from https://trac.sagemath.org/ticket/7831





---

archive/issue_comments_067704.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T09:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67704",
    "user": "https://github.com/peterjeremy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067705.json:
```json
{
    "body": "These changes look good to me.  Could you look over the ones at #7321?  I'll handle making an spkg with all of these rolled together.\n\nThanks!",
    "created_at": "2010-01-03T16:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67705",
    "user": "https://github.com/mwhansen"
}
```

These changes look good to me.  Could you look over the ones at #7321?  I'll handle making an spkg with all of these rolled together.

Thanks!



---

archive/issue_comments_067706.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-03T16:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67706",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067707.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-13T07:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_067708.json:
```json
{
    "body": "Updated spkg at\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/numpy/numpy-1.3.0.p3.spkg\n\nwhich incorporates the patch [7831.numpy.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7831/7831.numpy.patch). This spkg needs review by anyone other than me.",
    "created_at": "2010-02-13T07:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67708",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Updated spkg at

http://sage.math.washington.edu/home/mvngu/spkg/standard/numpy/numpy-1.3.0.p3.spkg

which incorporates the patch [7831.numpy.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7831/7831.numpy.patch). This spkg needs review by anyone other than me.



---

archive/issue_comments_067709.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-13T07:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67709",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067710.json:
```json
{
    "body": "Looks fine.  The the changes based on the newest spkg are at \n\nhttp://sage.math.washington.edu/home/mhansen/numpy-1.3.0.p4.spkg",
    "created_at": "2010-06-22T23:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67710",
    "user": "https://github.com/mwhansen"
}
```

Looks fine.  The the changes based on the newest spkg are at 

http://sage.math.washington.edu/home/mhansen/numpy-1.3.0.p4.spkg



---

archive/issue_comments_067711.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-22T23:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67711",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067712.json:
```json
{
    "body": "There is another ticket updating numpy as well: #8010. These two conflicting spkg's need to be resolved.",
    "created_at": "2010-06-25T05:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67712",
    "user": "https://github.com/rlmill"
}
```

There is another ticket updating numpy as well: #8010. These two conflicting spkg's need to be resolved.



---

archive/issue_comments_067713.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-28T17:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67713",
    "user": "https://github.com/rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_067714.json:
```json
{
    "body": "Since #8010 has been closed, it would be helpful to know whether the changes here are still needed (which I can't test, unfortunately).",
    "created_at": "2010-11-03T12:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67714",
    "user": "https://github.com/kcrisman"
}
```

Since #8010 has been closed, it would be helpful to know whether the changes here are still needed (which I can't test, unfortunately).



---

archive/issue_comments_067715.json:
```json
{
    "body": "Can someone verify whether this is fixed by other changes to the numpy package in 4.6.1alpha0?",
    "created_at": "2010-11-05T06:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67715",
    "user": "https://trac.sagemath.org/admin/accounts/users/flawrence"
}
```

Can someone verify whether this is fixed by other changes to the numpy package in 4.6.1alpha0?



---

archive/issue_comments_067716.json:
```json
{
    "body": "The __init__.py changes don't appear to be needed any longer but the remaining fixes are still required.",
    "created_at": "2010-11-18T19:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67716",
    "user": "https://github.com/peterjeremy"
}
```

The __init__.py changes don't appear to be needed any longer but the remaining fixes are still required.



---

archive/issue_comments_067717.json:
```json
{
    "body": "Attachment [7831.numpy.patch](tarball://root/attachments/some-uuid/ticket7831/7831.numpy.patch) by @kcrisman created at 2011-03-12 04:11:32\n\nNote that numpy 1.5.1 is on the way to Sage - #10792.   It would be great to get this incorporated with that.",
    "created_at": "2011-03-12T04:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67717",
    "user": "https://github.com/kcrisman"
}
```

Attachment [7831.numpy.patch](tarball://root/attachments/some-uuid/ticket7831/7831.numpy.patch) by @kcrisman created at 2011-03-12 04:11:32

Note that numpy 1.5.1 is on the way to Sage - #10792.   It would be great to get this incorporated with that.



---

archive/issue_comments_067718.json:
```json
{
    "body": "Apparently [Stephen Montgomery-Smith](http://groups.google.com/group/sage-devel/browse_thread/thread/2feec7c5511c4ae5/857a00a9aa271f17) has had some success with this recently as a \"port\".",
    "created_at": "2012-01-31T02:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67718",
    "user": "https://github.com/kcrisman"
}
```

Apparently [Stephen Montgomery-Smith](http://groups.google.com/group/sage-devel/browse_thread/thread/2feec7c5511c4ae5/857a00a9aa271f17) has had some success with this recently as a "port".



---

archive/issue_comments_067719.json:
```json
{
    "body": "More success at [this thread](https://groups.google.com/forum/?fromgroups#!topic/sage-devel/yPGIKHRSANs).  Checking whether it was with a system version or Sage version.",
    "created_at": "2012-06-20T15:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67719",
    "user": "https://github.com/kcrisman"
}
```

More success at [this thread](https://groups.google.com/forum/?fromgroups#!topic/sage-devel/yPGIKHRSANs).  Checking whether it was with a system version or Sage version.



---

archive/issue_comments_067720.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2012-06-20T15:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67720",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_067721.json:
```json
{
    "body": "Just noting here that although this was the Sage version, Numpy upstream still has the special FreeBSD code, [here as of June 2012](https://github.com/numpy/numpy/blob/master/numpy/distutils/system_info.py#L972), so the patch definitely hasn't been applied.  My sense is that probably the R upgrades over the years is what made this obsolete.\n\nSo I'm putting this to positive review as it builds (and so does R) and passes the overwhelming majority of tests on FreeBSD 8 and 9, but leaving this info here in case in certain unusual cases this ends up being a problem after all.",
    "created_at": "2012-06-20T18:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67721",
    "user": "https://github.com/kcrisman"
}
```

Just noting here that although this was the Sage version, Numpy upstream still has the special FreeBSD code, [here as of June 2012](https://github.com/numpy/numpy/blob/master/numpy/distutils/system_info.py#L972), so the patch definitely hasn't been applied.  My sense is that probably the R upgrades over the years is what made this obsolete.

So I'm putting this to positive review as it builds (and so does R) and passes the overwhelming majority of tests on FreeBSD 8 and 9, but leaving this info here in case in certain unusual cases this ends up being a problem after all.



---

archive/issue_comments_067722.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-06-20T18:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67722",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_067723.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-20T18:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67723",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008046.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-07-04T07:11:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7831#event-8046"
}
```



---

archive/issue_comments_067724.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-07-04T07:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7831#issuecomment-67724",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
