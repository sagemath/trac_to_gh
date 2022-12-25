# Issue 7272: Upgrade to Cython 0.12

archive/issues_007272.json:
```json
{
    "body": "Assignee: mabshoff\n\nCython 0.12 isn't released yet, but should be shortly, and this ticket is about getting Sage to compile and pass all tests.\n\nSpkg at http://sage.math.washington.edu/home/robertwb/cython/cython-0.12.spkg\n\nAlso depends on patch at #7023 (to be applied before the attached patch). \n\nIssue created by migration from https://trac.sagemath.org/ticket/7272\n\n",
    "created_at": "2009-10-23T17:04:56Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Upgrade to Cython 0.12",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7272",
    "user": "https://github.com/robertwb"
}
```
Assignee: mabshoff

Cython 0.12 isn't released yet, but should be shortly, and this ticket is about getting Sage to compile and pass all tests.

Spkg at http://sage.math.washington.edu/home/robertwb/cython/cython-0.12.spkg

Also depends on patch at #7023 (to be applied before the attached patch). 

Issue created by migration from https://trac.sagemath.org/ticket/7272





---

archive/issue_comments_060382.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-10-23T17:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60382",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_060383.json:
```json
{
    "body": "I had to force cdivision=True globally as way to much stuff broke otherwise (and even if all tests passed, it's a bold move that should be taken after looking through the entire library for problems).",
    "created_at": "2009-10-23T17:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60383",
    "user": "https://github.com/robertwb"
}
```

I had to force cdivision=True globally as way to much stuff broke otherwise (and even if all tests passed, it's a bold move that should be taken after looking through the entire library for problems).



---

archive/issue_comments_060384.json:
```json
{
    "body": "I've gotten everything working but\n\n\n```\n\tsage -t  \"sage/modular/modsym/ambient.py\"\n\tsage -t  \"sage/modular/modsym/heilbronn.pyx\"\n```\n\n\nwith \n\n\n```\nsage -t  \"devel/sage-cython2/sage/modular/modsym/heilbronn.pyx\"\npython(96760) malloc: *** mmap(size=1744830464) failed (error code=12)\n*** error: can't allocate region\n*** set a breakpoint in malloc_error_break to debug\n**********************************************************************\nFile \"/Users/robertwb/sage/sage-4.0/devel/sage-cython2/sage/modular/modsym/heilbronn.pyx\", line 839:\n    sage: sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k(4,1,3,15,6,[1,11,12], R)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/robertwb/sage/sage-4.0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/robertwb/sage/sage-4.0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/robertwb/sage/sage-4.0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_17[4]>\", line 1, in <module>\n        sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k(Integer(4),Integer(1),Integer(3),Integer(15),Integer(6),[Integer(1),Integer(11),Integer(12)], R)###line 839:\n    sage: sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k(4,1,3,15,6,[1,11,12], R)\n      File \"heilbronn.pyx\", line 877, in sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k (sage/modular/modsym/heilbronn.c:7652)\n      File \"heilbronn.pyx\", line 417, in sage.modular.modsym.heilbronn.HeilbronnMerel.__init__ (sage/modular/modsym/heilbronn.c:4561)\n    SystemError: NULL result without error in PyObject_Call\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_17\n***Test Failed*** 1 failures.\n```\n",
    "created_at": "2009-10-23T17:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60384",
    "user": "https://github.com/robertwb"
}
```

I've gotten everything working but


```
	sage -t  "sage/modular/modsym/ambient.py"
	sage -t  "sage/modular/modsym/heilbronn.pyx"
```


with 


```
sage -t  "devel/sage-cython2/sage/modular/modsym/heilbronn.pyx"
python(96760) malloc: *** mmap(size=1744830464) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
**********************************************************************
File "/Users/robertwb/sage/sage-4.0/devel/sage-cython2/sage/modular/modsym/heilbronn.pyx", line 839:
    sage: sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k(4,1,3,15,6,[1,11,12], R)
Exception raised:
    Traceback (most recent call last):
      File "/Users/robertwb/sage/sage-4.0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/robertwb/sage/sage-4.0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/robertwb/sage/sage-4.0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[4]>", line 1, in <module>
        sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k(Integer(4),Integer(1),Integer(3),Integer(15),Integer(6),[Integer(1),Integer(11),Integer(12)], R)###line 839:
    sage: sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k(4,1,3,15,6,[1,11,12], R)
      File "heilbronn.pyx", line 877, in sage.modular.modsym.heilbronn.hecke_images_gamma0_weight_k (sage/modular/modsym/heilbronn.c:7652)
      File "heilbronn.pyx", line 417, in sage.modular.modsym.heilbronn.HeilbronnMerel.__init__ (sage/modular/modsym/heilbronn.c:4561)
    SystemError: NULL result without error in PyObject_Call
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_17
***Test Failed*** 1 failures.
```




---

archive/issue_comments_060385.json:
```json
{
    "body": "Above failure due to memory corruption caused by http://trac.cython.org/cython_trac/ticket/442\n\nSage builds and passes all tests (vanilla 4.2 + attached patch)",
    "created_at": "2009-10-30T06:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60385",
    "user": "https://github.com/robertwb"
}
```

Above failure due to memory corruption caused by http://trac.cython.org/cython_trac/ticket/442

Sage builds and passes all tests (vanilla 4.2 + attached patch)



---

archive/issue_comments_060386.json:
```json
{
    "body": "Attachment [7272-cython-0.12.patch](tarball://root/attachments/some-uuid/ticket7272/7272-cython-0.12.patch) by @robertwb created at 2009-10-30 06:17:29",
    "created_at": "2009-10-30T06:17:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60386",
    "user": "https://github.com/robertwb"
}
```

Attachment [7272-cython-0.12.patch](tarball://root/attachments/some-uuid/ticket7272/7272-cython-0.12.patch) by @robertwb created at 2009-10-30 06:17:29



---

archive/issue_comments_060387.json:
```json
{
    "body": "Looks good to me.\n\nI went ahead and removed the src/.hg/ repo from the Cython spkg and checked in the modification to spkg-install.  The new spkg can be found at http://sage.math.washington.edu/home/mhansen/cython-0.12.spkg",
    "created_at": "2009-11-17T11:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60387",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.

I went ahead and removed the src/.hg/ repo from the Cython spkg and checked in the modification to spkg-install.  The new spkg can be found at http://sage.math.washington.edu/home/mhansen/cython-0.12.spkg



---

archive/issue_events_017197.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-17T11:10:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7272#event-17197"
}
```



---

archive/issue_comments_060388.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T11:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60388",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_060389.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2009-11-17T20:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60389",
    "user": "https://github.com/robertwb"
}
```

Changing status from closed to needs_work.



---

archive/issue_events_017198.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2009-11-17T20:07:49Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7272#event-17198"
}
```



---

archive/issue_comments_060390.json:
```json
{
    "body": "Thanks for doing this, but 0.12 isn't officially out yet. Fortunately, I just updated the spkg to the most recent release candidate a couple of days ago. I see a release happening in the next week, so the only change (that impacts us, there's two windows fixes since then) will be the version number bump (I hope). \n\nThe linked spkg should work fine, but if we release soon (before you do) I'd be nice to actually be synced with upstream.",
    "created_at": "2009-11-17T20:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60390",
    "user": "https://github.com/robertwb"
}
```

Thanks for doing this, but 0.12 isn't officially out yet. Fortunately, I just updated the spkg to the most recent release candidate a couple of days ago. I see a release happening in the next week, so the only change (that impacts us, there's two windows fixes since then) will be the version number bump (I hope). 

The linked spkg should work fine, but if we release soon (before you do) I'd be nice to actually be synced with upstream.



---

archive/issue_comments_060391.json:
```json
{
    "body": "I think 0.12 will be out before 4.3.  I'll include the official 0.12 in the main release.",
    "created_at": "2009-11-18T03:51:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60391",
    "user": "https://github.com/mwhansen"
}
```

I think 0.12 will be out before 4.3.  I'll include the official 0.12 in the main release.



---

archive/issue_comments_060392.json:
```json
{
    "body": "It looks like 0.12 is out now.  From the Cython webpage:\n\n\n```\nThe latest release of Cython is 0.12 (released 2009-11-23).\n```\n\n\nIs the official release in the spkg above, or were there changes since the spkg above?\n\nAnd congrats on the 0.12 release!  I'm excited about the improvements in it!",
    "created_at": "2009-12-03T14:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60392",
    "user": "https://github.com/jasongrout"
}
```

It looks like 0.12 is out now.  From the Cython webpage:


```
The latest release of Cython is 0.12 (released 2009-11-23).
```


Is the official release in the spkg above, or were there changes since the spkg above?

And congrats on the 0.12 release!  I'm excited about the improvements in it!



---

archive/issue_comments_060393.json:
```json
{
    "body": "I'll upload the actual spkg.",
    "created_at": "2009-12-03T16:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60393",
    "user": "https://github.com/robertwb"
}
```

I'll upload the actual spkg.



---

archive/issue_comments_060394.json:
```json
{
    "body": "Spkg at http://sage.math.washington.edu/home/robertwb/cython/cython-0.12.spkg is the 0.12 release (minus repo).",
    "created_at": "2009-12-05T17:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60394",
    "user": "https://github.com/robertwb"
}
```

Spkg at http://sage.math.washington.edu/home/robertwb/cython/cython-0.12.spkg is the 0.12 release (minus repo).



---

archive/issue_comments_060395.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-07T19:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60395",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060396.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-07T19:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60396",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060397.json:
```json
{
    "body": "I'm changing this to positive review, as the changes between when this was merged and the official upstream are minimal.",
    "created_at": "2009-12-07T19:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60397",
    "user": "https://github.com/robertwb"
}
```

I'm changing this to positive review, as the changes between when this was merged and the official upstream are minimal.



---

archive/issue_events_017199.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-07T23:19:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7272#event-17199"
}
```



---

archive/issue_comments_060398.json:
```json
{
    "body": "I've merged this new spkg in 4.3.rc0",
    "created_at": "2009-12-07T23:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7272#issuecomment-60398",
    "user": "https://github.com/mwhansen"
}
```

I've merged this new spkg in 4.3.rc0
