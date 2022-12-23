# Issue 9152: Update extension code for mpmath-0.15

archive/issues_009152.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  burcin\n\nI plan to release mpmath 0.15 very soon. This will require some simple modifications to the extension code in Sage.\n\nSome testing would be appreciated: apply the patch, replace the Sage mpmath install with an svn trunk checkout of mpmath, and check\n\n\n```\nsage: import mpmath\nsage: mpmath.runtests()\nsage: mpmath.doctests()\n```\n\n\nThe patch doesn't support mpmath 0.14, so it can't be applied until the spkg is upgraded.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9152\n\n",
    "created_at": "2010-06-05T17:39:17Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "Update extension code for mpmath-0.15",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9152",
    "user": "fredrik.johansson"
}
```
Assignee: tbd

CC:  burcin

I plan to release mpmath 0.15 very soon. This will require some simple modifications to the extension code in Sage.

Some testing would be appreciated: apply the patch, replace the Sage mpmath install with an svn trunk checkout of mpmath, and check


```
sage: import mpmath
sage: mpmath.runtests()
sage: mpmath.doctests()
```


The patch doesn't support mpmath 0.14, so it can't be applied until the spkg is upgraded.

Issue created by migration from https://trac.sagemath.org/ticket/9152





---

archive/issue_comments_085440.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-05T17:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85440",
    "user": "fredrik.johansson"
}
```

Attachment



---

archive/issue_comments_085441.json:
```json
{
    "body": "Attachment\n\nI've released mpmath-0.15; providing spkg as attachment.",
    "created_at": "2010-06-06T19:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85441",
    "user": "fredrik.johansson"
}
```

Attachment

I've released mpmath-0.15; providing spkg as attachment.



---

archive/issue_comments_085442.json:
```json
{
    "body": "I installed the spkg and patch into 4.4.4.alpha0. \"runtests\" worked fine (finished in 12.9 seconds, compared to 15.7 for the mpmath shipped in 4.4.3), but \"doctests\" had one failure:\n\n```\nqbarfrom**********************************************************************\nFile \"/home/drake/s/sage-4.4.4.alpha0/local/lib/python2.6/site-packages/mpmath/functions/functions.py\", line ?, in NoName\nFailed example:\n    qbarfrom(m=extraprec(20)(mfrom)(qbar=0.25))  # ill-conditioned\nException raised:\n    Traceback (most recent call last):\n      File \"/home/drake/s/sage-4.4.4.alpha0/local/lib/python/doctest.py\", line 1241, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest NoName[4]>\", line 1, in <module>\n        qbarfrom(m=extraprec(20)(mfrom)(qbar=0.25))  # ill-conditioned\n      File \"/home/drake/s/sage-4.4.4.alpha0/local/lib/python2.6/site-packages/mpmath/ctx_mp.py\", line 1228, in __call__\n        g.__name__ = f.__name__\n    AttributeError: 'mfrom' object has no attribute '__name__'\n**********************************************************************\nFile \"/home/drake/s/sage-4.4.4.alpha0/local/lib/python2.6/site-packages/mpmath/functions/functions.py\", line ?, in NoName\nFailed example:\n    qbarfrom(k=extraprec(20)(kfrom)(qbar=0.25))  # ill-conditioned\nException raised:\n    Traceback (most recent call last):\n      File \"/home/drake/s/sage-4.4.4.alpha0/local/lib/python/doctest.py\", line 1241, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest NoName[5]>\", line 1, in <module>\n        qbarfrom(k=extraprec(20)(kfrom)(qbar=0.25))  # ill-conditioned\n      File \"/home/drake/s/sage-4.4.4.alpha0/local/lib/python2.6/site-packages/mpmath/ctx_mp.py\", line 1228, in __call__\n        g.__name__ = f.__name__\n    AttributeError: 'kfrom' object has no attribute '__name__'\n0.003\n```\n\nIn 4.4.3, all the doctests pass.\n\nAlso, I think it's considered best to not post spkgs as ticket attachments -- usually you just put it somewhere on the web (your sage.math home directory is good) and post the link.",
    "created_at": "2010-06-09T23:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85442",
    "user": "ddrake"
}
```

I installed the spkg and patch into 4.4.4.alpha0. "runtests" worked fine (finished in 12.9 seconds, compared to 15.7 for the mpmath shipped in 4.4.3), but "doctests" had one failure:

```
qbarfrom**********************************************************************
File "/home/drake/s/sage-4.4.4.alpha0/local/lib/python2.6/site-packages/mpmath/functions/functions.py", line ?, in NoName
Failed example:
    qbarfrom(m=extraprec(20)(mfrom)(qbar=0.25))  # ill-conditioned
Exception raised:
    Traceback (most recent call last):
      File "/home/drake/s/sage-4.4.4.alpha0/local/lib/python/doctest.py", line 1241, in __run
        compileflags, 1) in test.globs
      File "<doctest NoName[4]>", line 1, in <module>
        qbarfrom(m=extraprec(20)(mfrom)(qbar=0.25))  # ill-conditioned
      File "/home/drake/s/sage-4.4.4.alpha0/local/lib/python2.6/site-packages/mpmath/ctx_mp.py", line 1228, in __call__
        g.__name__ = f.__name__
    AttributeError: 'mfrom' object has no attribute '__name__'
**********************************************************************
File "/home/drake/s/sage-4.4.4.alpha0/local/lib/python2.6/site-packages/mpmath/functions/functions.py", line ?, in NoName
Failed example:
    qbarfrom(k=extraprec(20)(kfrom)(qbar=0.25))  # ill-conditioned
Exception raised:
    Traceback (most recent call last):
      File "/home/drake/s/sage-4.4.4.alpha0/local/lib/python/doctest.py", line 1241, in __run
        compileflags, 1) in test.globs
      File "<doctest NoName[5]>", line 1, in <module>
        qbarfrom(k=extraprec(20)(kfrom)(qbar=0.25))  # ill-conditioned
      File "/home/drake/s/sage-4.4.4.alpha0/local/lib/python2.6/site-packages/mpmath/ctx_mp.py", line 1228, in __call__
        g.__name__ = f.__name__
    AttributeError: 'kfrom' object has no attribute '__name__'
0.003
```

In 4.4.3, all the doctests pass.

Also, I think it's considered best to not post spkgs as ticket attachments -- usually you just put it somewhere on the web (your sage.math home directory is good) and post the link.



---

archive/issue_comments_085443.json:
```json
{
    "body": "Attachment\n\nsmall fix on top of mpmath15fix.patch",
    "created_at": "2010-06-10T00:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85443",
    "user": "fredrik.johansson"
}
```

Attachment

small fix on top of mpmath15fix.patch



---

archive/issue_comments_085444.json:
```json
{
    "body": "Thanks, Dan. Sorry for missing those two failures.\n\nThis second patch should fix them.",
    "created_at": "2010-06-10T00:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85444",
    "user": "fredrik.johansson"
}
```

Thanks, Dan. Sorry for missing those two failures.

This second patch should fix them.



---

archive/issue_comments_085445.json:
```json
{
    "body": "With your \"fixfix\" patch, the doctests pass. (This is on 64-bit Ubuntu.) The spkg looks good, although we should test it on some other platforms. I don't know enough Cython to say much about the patches, unfortunately.",
    "created_at": "2010-06-10T03:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85445",
    "user": "ddrake"
}
```

With your "fixfix" patch, the doctests pass. (This is on 64-bit Ubuntu.) The spkg looks good, although we should test it on some other platforms. I don't know enough Cython to say much about the patches, unfortunately.



---

archive/issue_comments_085446.json:
```json
{
    "body": "Changing assignee from tbd to ddrake.",
    "created_at": "2010-06-10T03:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85446",
    "user": "ddrake"
}
```

Changing assignee from tbd to ddrake.



---

archive/issue_comments_085447.json:
```json
{
    "body": "The spkgs and patches also work with 4.4.4.alpha0 on bsd.math (OS X 10.6, I think).",
    "created_at": "2010-06-10T07:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85447",
    "user": "ddrake"
}
```

The spkgs and patches also work with 4.4.4.alpha0 on bsd.math (OS X 10.6, I think).



---

archive/issue_comments_085448.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-22T22:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85448",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085449.json:
```json
{
    "body": "The changes look good to me.  I've checked in the changes in the spkg at http://sage.math.washington.edu/home/mhansen/mpmath-0.15.spkg",
    "created_at": "2010-06-22T22:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85449",
    "user": "mhansen"
}
```

The changes look good to me.  I've checked in the changes in the spkg at http://sage.math.washington.edu/home/mhansen/mpmath-0.15.spkg



---

archive/issue_comments_085450.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-22T22:42:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85450",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085451.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85451",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_085452.json:
```json
{
    "body": "I think applying the two sage repository patches to 4.5.alpha0 will fix all or nearly all of its [doctest failures](http://groups.google.com/group/sage-release/browse_thread/thread/28b187636fda282b).",
    "created_at": "2010-06-26T03:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85452",
    "user": "mpatel"
}
```

I think applying the two sage repository patches to 4.5.alpha0 will fix all or nearly all of its [doctest failures](http://groups.google.com/group/sage-release/browse_thread/thread/28b187636fda282b).



---

archive/issue_comments_085453.json:
```json
{
    "body": "Replying to [comment:12 mpatel]:\n> I think applying the two sage repository patches to 4.5.alpha0 will fix all or nearly all of its [doctest failures](http://groups.google.com/group/sage-release/browse_thread/thread/28b187636fda282b).\n\nAt first glance (testing only the 10 files that had doctest failures), **yes**, i.e. applying these two patches to alpha0 fixes them **all** (see also sage-release).\n\nCurrently running complete tests (ptestlong) again...",
    "created_at": "2010-06-26T16:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85453",
    "user": "leif"
}
```

Replying to [comment:12 mpatel]:
> I think applying the two sage repository patches to 4.5.alpha0 will fix all or nearly all of its [doctest failures](http://groups.google.com/group/sage-release/browse_thread/thread/28b187636fda282b).

At first glance (testing only the 10 files that had doctest failures), **yes**, i.e. applying these two patches to alpha0 fixes them **all** (see also sage-release).

Currently running complete tests (ptestlong) again...



---

archive/issue_comments_085454.json:
```json
{
    "body": "\n```\nchangeset:   14535:97280db338bf\ntag:         tip\nuser:        Fredrik Johansson <fredrik.johansson@gmail.com>\ndate:        Thu Jun 10 02:23:59 2010 +0200\nsummary:     fix wrapped mpmath functions to retain __name__ attribute\n\nchangeset:   14534:ebf36c5d4051\nuser:        Fredrik Johansson <fredrik.johansson@gmail.com>\ndate:        Sat Jun 05 19:25:42 2010 +0200\nsummary:     update mpmath extension module for mpmath 0.15 compatibility\n\nchangeset:   14533:5c14ca9acdd3\nuser:        Robert Miller <rlm@rlmiller.org>\ndate:        Fri Jun 25 05:11:33 2010 -0700\nsummary:     4.5.alpha0\n```\n\n\n\nUbuntu 9.04 x86_64 (Core2), gcc 4.5.0, `make ptestlong`:\n\n```\nAll tests passed!\nTotal time for all tests: 2147.1 seconds\n\nreal\t36m19.732s\nuser\t80m12.569s\nsys\t6m45.373s\nleif@quadriga:~/sage-4.5.alpha0/devel/sage-9152$ \n```\n",
    "created_at": "2010-06-26T17:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85454",
    "user": "leif"
}
```


```
changeset:   14535:97280db338bf
tag:         tip
user:        Fredrik Johansson <fredrik.johansson@gmail.com>
date:        Thu Jun 10 02:23:59 2010 +0200
summary:     fix wrapped mpmath functions to retain __name__ attribute

changeset:   14534:ebf36c5d4051
user:        Fredrik Johansson <fredrik.johansson@gmail.com>
date:        Sat Jun 05 19:25:42 2010 +0200
summary:     update mpmath extension module for mpmath 0.15 compatibility

changeset:   14533:5c14ca9acdd3
user:        Robert Miller <rlm@rlmiller.org>
date:        Fri Jun 25 05:11:33 2010 -0700
summary:     4.5.alpha0
```



Ubuntu 9.04 x86_64 (Core2), gcc 4.5.0, `make ptestlong`:

```
All tests passed!
Total time for all tests: 2147.1 seconds

real	36m19.732s
user	80m12.569s
sys	6m45.373s
leif@quadriga:~/sage-4.5.alpha0/devel/sage-9152$ 
```




---

archive/issue_comments_085455.json:
```json
{
    "body": "Note: I have merged the two sage library patches into sage-4.5.alpha1.",
    "created_at": "2010-06-28T16:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9152#issuecomment-85455",
    "user": "rlm"
}
```

Note: I have merged the two sage library patches into sage-4.5.alpha1.
