# Issue 9152: Update extension code for mpmath-0.15

Issue created by migration from https://trac.sagemath.org/ticket/9152

Original creator: fredrik.johansson

Original creation time: 2010-06-05 17:39:17

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


---

Attachment


---

Attachment

I've released mpmath-0.15; providing spkg as attachment.


---

Comment by ddrake created at 2010-06-09 23:48:27

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

Attachment

small fix on top of mpmath15fix.patch


---

Comment by fredrik.johansson created at 2010-06-10 00:45:46

Thanks, Dan. Sorry for missing those two failures.

This second patch should fix them.


---

Comment by ddrake created at 2010-06-10 03:53:28

With your "fixfix" patch, the doctests pass. (This is on 64-bit Ubuntu.) The spkg looks good, although we should test it on some other platforms. I don't know enough Cython to say much about the patches, unfortunately.


---

Comment by ddrake created at 2010-06-10 03:53:28

Changing assignee from tbd to ddrake.


---

Comment by ddrake created at 2010-06-10 07:52:57

The spkgs and patches also work with 4.4.4.alpha0 on bsd.math (OS X 10.6, I think).


---

Comment by mhansen created at 2010-06-22 22:42:09

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-06-22 22:42:09

The changes look good to me.  I've checked in the changes in the spkg at http://sage.math.washington.edu/home/mhansen/mpmath-0.15.spkg


---

Comment by mhansen created at 2010-06-22 22:42:24

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-25 15:44:05

Resolution: fixed


---

Comment by mpatel created at 2010-06-26 03:56:50

I think applying the two sage repository patches to 4.5.alpha0 will fix all or nearly all of its [doctest failures](http://groups.google.com/group/sage-release/browse_thread/thread/28b187636fda282b).


---

Comment by leif created at 2010-06-26 16:30:33

Replying to [comment:12 mpatel]:
> I think applying the two sage repository patches to 4.5.alpha0 will fix all or nearly all of its [doctest failures](http://groups.google.com/group/sage-release/browse_thread/thread/28b187636fda282b).

At first glance (testing only the 10 files that had doctest failures), *yes*, i.e. applying these two patches to alpha0 fixes them *all* (see also sage-release).

Currently running complete tests (ptestlong) again...


---

Comment by leif created at 2010-06-26 17:25:30


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

Comment by rlm created at 2010-06-28 16:49:41

Note: I have merged the two sage library patches into sage-4.5.alpha1.
