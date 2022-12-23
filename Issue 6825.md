# Issue 6825: intermittent failure in vector_real_double_dense.pyx

Issue created by migration from https://trac.sagemath.org/ticket/6825

Original creator: mvngu

Original creation time: 2009-08-25 17:18:55

Assignee: tbd

CC:  jason

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


---

Comment by jason created at 2009-08-30 05:31:36

I think this is probably an error in scipy or numpy.


---

Comment by was created at 2009-09-02 15:07:01


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

Comment by was created at 2009-10-13 20:28:34

Changing priority from major to blocker.


---

Comment by mvngu created at 2009-10-21 22:06:23

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

Comment by jason created at 2009-10-21 22:17:53

Replying to [comment:4 mvngu]:
> Now I get a mysterious error in Sage 4.2.alpha0:

This seems like a totally different error.  Should a new ticket be opened?


---

Comment by jason created at 2009-10-21 22:18:40

* Is your memory error reproducible?

 * Can you use hg bisect to narrow it down to a patch?


---

Comment by mhansen created at 2009-11-12 05:50:57

I've made an spkg which fixes the assert statement by switching it to the correct syntax.

It can be found a http://sage.math.washington.edu/home/mhansen/scipy-0.7.p3.spkg


---

Comment by mhansen created at 2009-11-12 05:50:57

Changing status from new to needs_review.


---

Comment by was created at 2009-11-12 06:00:26

Positive review.  I slightly modified the spkg and put the modified version here:

   http://wstein.org/home/wstein/patches/scipy-0.7.p3.spkg


---

Comment by was created at 2009-11-12 06:00:50

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-12 06:01:20

Oh, and the thing mike patched has already been fixed upstream.


---

Comment by jason created at 2009-11-12 06:32:44

Replying to [comment:12 was]:
> Oh, and the thing mike patched has already been fixed upstream.

We're already a version behind (we're at 0.7, but upstream is 0.7.1).  Would upgrading to 0.7.1 get us this fix?


---

Comment by jason created at 2009-11-12 06:35:23

Is this the bug: http://projects.scipy.org/scipy/ticket/944

If so, it is fixed in 0.7.1, so we should probably just upgrade.


---

Comment by mhansen created at 2009-11-12 06:39:25

Yes, that's the bug.  I think at this point, it makes more sense to apply the small fix for 4.2.1 which should be out in the next day or so.

In 4.3, we can upgrade to 0.7.1 when we can get more rounds of testing on various platforms.


---

Comment by mhansen created at 2009-11-12 07:04:35

Resolution: fixed


---

Comment by mhansen created at 2009-11-12 07:04:35

I'll open a new ticket to update to 0.7.1.
