# Issue 6825: intermittent failure in vector_real_double_dense.pyx

archive/issues_006825.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jasongrout\n\nMariah Lenox reported the following doctest failure when running the test suite:\n\n```\nsage -t  \"devel/sage/sage/modules/vector_real_double_dense.pyx\"\n**********************************************************************\nFile \"/home/mariah/sage/sage-4.1.1-x86_64-Linux-core2-fc-move/devel/sage/sage/modules/vector_real_double_dense.pyx\",\nline 72:\n   sage: v.stats_skew()\nExpected:\n   0.0\nGot:\n   doctest:106: SyntaxWarning: assertion is always true, perhaps\nremove parentheses?\n   0.0\n**********************************************************************\n1 items had failures:\n```\n\nBut if you run doctest again on `sage/modules/vector_real_double_dense.pyx`, the failure would disappear. This is an intermittent failure I came across while managing the release of Sage 4.1.1.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6825\n\n",
    "created_at": "2009-08-25T17:18:55Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "intermittent failure in vector_real_double_dense.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6825",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

CC:  @jasongrout

Mariah Lenox reported the following doctest failure when running the test suite:

```
sage -t  "devel/sage/sage/modules/vector_real_double_dense.pyx"
**********************************************************************
File "/home/mariah/sage/sage-4.1.1-x86_64-Linux-core2-fc-move/devel/sage/sage/modules/vector_real_double_dense.pyx",
line 72:
   sage: v.stats_skew()
Expected:
   0.0
Got:
   doctest:106: SyntaxWarning: assertion is always true, perhaps
remove parentheses?
   0.0
**********************************************************************
1 items had failures:
```

But if you run doctest again on `sage/modules/vector_real_double_dense.pyx`, the failure would disappear. This is an intermittent failure I came across while managing the release of Sage 4.1.1.

Issue created by migration from https://trac.sagemath.org/ticket/6825





---

archive/issue_comments_056186.json:
```json
{
    "body": "I think this is probably an error in scipy or numpy.",
    "created_at": "2009-08-30T05:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56186",
    "user": "https://github.com/jasongrout"
}
```

I think this is probably an error in scipy or numpy.



---

archive/issue_comments_056187.json:
```json
{
    "body": "\n```\nI can make the problem described in sage trac ticket #6825\nreproducible and not intermitent.\n\nIf you remove\n\n    local/lib/python/site-packages/scipy/stats/mstats_basic.pyc\n\nthen you will see the error when you run\n\n    sage -t  \"devel/sage/sage/modules/vector_real_double_dense.pyx\"\n\nThis reproduces the problem whether or not you move the build directory.\n\n\nOne possible fix for the problem is to remove line 106 of\n\n    local/lib/python/site-packages/scipy/stats/mstats_basic.py\n\nwhich is the assert line about which the output message complains.\n\n\nI do not know a lot about python, but it seems that\npython evidently has some check that the sage tree has moved and\nso rebuilds *.pyc files if they have not been regenerated recently.\nI am surprised that local/bin/sage-location does not remove all the\n*.pyc files and rebuild them when the sage tree moves.\n\nMariah\n```\n",
    "created_at": "2009-09-02T15:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56187",
    "user": "https://github.com/williamstein"
}
```


```
I can make the problem described in sage trac ticket #6825
reproducible and not intermitent.

If you remove

    local/lib/python/site-packages/scipy/stats/mstats_basic.pyc

then you will see the error when you run

    sage -t  "devel/sage/sage/modules/vector_real_double_dense.pyx"

This reproduces the problem whether or not you move the build directory.


One possible fix for the problem is to remove line 106 of

    local/lib/python/site-packages/scipy/stats/mstats_basic.py

which is the assert line about which the output message complains.


I do not know a lot about python, but it seems that
python evidently has some check that the sage tree has moved and
so rebuilds *.pyc files if they have not been regenerated recently.
I am surprised that local/bin/sage-location does not remove all the
*.pyc files and rebuild them when the sage tree moves.

Mariah
```




---

archive/issue_comments_056188.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-10-13T20:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56188",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_056189.json:
```json
{
    "body": "Now I get a mysterious error in Sage 4.2.alpha0:\n\n```\n[mvngu@sage sage-4.2.alpha0-sage.math]$ sage -t -long devel/sage-main/sage/modules/vector_real_double_dense.pyx\nsage -t -long \"devel/sage-main/sage/modules/vector_real_double_dense.pyx\"\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n         [3.1 s]\nexit code: 768\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage-main/sage/modules/vector_real_double_dense.pyx\"\nTotal time for all tests: 3.1 seconds\n```\n",
    "created_at": "2009-10-21T22:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56189",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Now I get a mysterious error in Sage 4.2.alpha0:

```
[mvngu@sage sage-4.2.alpha0-sage.math]$ sage -t -long devel/sage-main/sage/modules/vector_real_double_dense.pyx
sage -t -long "devel/sage-main/sage/modules/vector_real_double_dense.pyx"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [3.1 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-main/sage/modules/vector_real_double_dense.pyx"
Total time for all tests: 3.1 seconds
```




---

archive/issue_comments_056190.json:
```json
{
    "body": "Replying to [comment:4 mvngu]:\n> Now I get a mysterious error in Sage 4.2.alpha0:\n\nThis seems like a totally different error.  Should a new ticket be opened?",
    "created_at": "2009-10-21T22:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56190",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:4 mvngu]:
> Now I get a mysterious error in Sage 4.2.alpha0:

This seems like a totally different error.  Should a new ticket be opened?



---

archive/issue_comments_056191.json:
```json
{
    "body": "* Is your memory error reproducible?\n\n  * Can you use hg bisect to narrow it down to a patch?",
    "created_at": "2009-10-21T22:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56191",
    "user": "https://github.com/jasongrout"
}
```

* Is your memory error reproducible?

  * Can you use hg bisect to narrow it down to a patch?



---

archive/issue_comments_056192.json:
```json
{
    "body": "I've made an spkg which fixes the assert statement by switching it to the correct syntax.\n\nIt can be found a http://sage.math.washington.edu/home/mhansen/scipy-0.7.p3.spkg",
    "created_at": "2009-11-12T05:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56192",
    "user": "https://github.com/mwhansen"
}
```

I've made an spkg which fixes the assert statement by switching it to the correct syntax.

It can be found a http://sage.math.washington.edu/home/mhansen/scipy-0.7.p3.spkg



---

archive/issue_comments_056193.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-12T05:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56193",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056194.json:
```json
{
    "body": "Positive review.  I slightly modified the spkg and put the modified version here:\n\n   http://wstein.org/home/wstein/patches/scipy-0.7.p3.spkg",
    "created_at": "2009-11-12T06:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56194",
    "user": "https://github.com/williamstein"
}
```

Positive review.  I slightly modified the spkg and put the modified version here:

   http://wstein.org/home/wstein/patches/scipy-0.7.p3.spkg



---

archive/issue_comments_056195.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-12T06:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56195",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056196.json:
```json
{
    "body": "Oh, and the thing mike patched has already been fixed upstream.",
    "created_at": "2009-11-12T06:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56196",
    "user": "https://github.com/williamstein"
}
```

Oh, and the thing mike patched has already been fixed upstream.



---

archive/issue_comments_056197.json:
```json
{
    "body": "Replying to [comment:12 was]:\n> Oh, and the thing mike patched has already been fixed upstream.\n\nWe're already a version behind (we're at 0.7, but upstream is 0.7.1).  Would upgrading to 0.7.1 get us this fix?",
    "created_at": "2009-11-12T06:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56197",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:12 was]:
> Oh, and the thing mike patched has already been fixed upstream.

We're already a version behind (we're at 0.7, but upstream is 0.7.1).  Would upgrading to 0.7.1 get us this fix?



---

archive/issue_comments_056198.json:
```json
{
    "body": "Is this the bug: http://projects.scipy.org/scipy/ticket/944\n\nIf so, it is fixed in 0.7.1, so we should probably just upgrade.",
    "created_at": "2009-11-12T06:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56198",
    "user": "https://github.com/jasongrout"
}
```

Is this the bug: http://projects.scipy.org/scipy/ticket/944

If so, it is fixed in 0.7.1, so we should probably just upgrade.



---

archive/issue_comments_056199.json:
```json
{
    "body": "Yes, that's the bug.  I think at this point, it makes more sense to apply the small fix for 4.2.1 which should be out in the next day or so.\n\nIn 4.3, we can upgrade to 0.7.1 when we can get more rounds of testing on various platforms.",
    "created_at": "2009-11-12T06:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56199",
    "user": "https://github.com/mwhansen"
}
```

Yes, that's the bug.  I think at this point, it makes more sense to apply the small fix for 4.2.1 which should be out in the next day or so.

In 4.3, we can upgrade to 0.7.1 when we can get more rounds of testing on various platforms.



---

archive/issue_events_007059.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-12T07:04:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6825#event-7059"
}
```



---

archive/issue_comments_056200.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T07:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56200",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_056201.json:
```json
{
    "body": "I'll open a new ticket to update to 0.7.1.",
    "created_at": "2009-11-12T07:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6825#issuecomment-56201",
    "user": "https://github.com/mwhansen"
}
```

I'll open a new ticket to update to 0.7.1.
