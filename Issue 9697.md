# Issue 9697: DS_Store garbage in flint spkg

Issue created by migration from https://trac.sagemath.org/ticket/9697

Original creator: rlm

Original creation time: 2010-08-06 17:33:52

Assignee: tbd


```
[rlm-book standard]$ tar xf flint-1.5.0.p5.spkg 
tar: copyfile unpack (flint-1.5.0.p5/src/zn_poly/demo/bernoulli/.svn/prop-base/.DS_Store.svn-base) failed: No such file or directory
```



---

Comment by pdehaye created at 2012-10-15 21:46:31

I have reported a similar error about flint-1.5.2.p1.spkg at https://groups.google.com/d/topic/sage-release/52Hz8-G3TWA/discussion


---

Comment by pdehaye created at 2012-10-15 21:47:46

Changing assignee from tbd to pdehaye.


---

Comment by pdehaye created at 2012-10-15 21:50:40

Suggested fix: http://boxen.math.washington.edu/home/pdehaye/spkg/flint-1.5.2.p2.spkg

Beware, this is my first spkg. I removed the offending file, modified SPKG.txt, and the mercurial log. I then made the spkg using sage _5.0_ as this is the last version I have running on my system. It looks like sage-spkg has not been changed since, so that should not be a problem.


---

Comment by pdehaye created at 2012-10-15 21:51:01

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-10-16 00:36:19

The spkg was created correctly, as far as I can tell.  You even added the tag!

This just needs formal testing on a couple machines to make sure something weird didn't accidentally happen, but looks good.


---

Comment by kcrisman created at 2012-10-16 01:17:26

Seems fine on sage.math, passes relevant tests.


---

Comment by kcrisman created at 2012-10-16 01:54:32

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-10-16 01:54:32

Same on Mac OS X.  I think this is ok...


---

Comment by leif created at 2012-10-16 10:29:41

FWIW, the `.svn/` folders should get removed from the source tree anyway.  [Haven't looked at the new spkg.]


---

Comment by pdehaye created at 2012-10-16 12:01:30

`@`leif: There are actually two issues: some .DS_Store are in the spkg, all having to do with bernoulli. One of those files sits inside a .svn folder, and was originally reported in this ticket. The others are in regular src/ folders, and might have been introduced when preparing the spkg.


---

Comment by jdemeyer created at 2012-10-17 20:52:18

Resolution: fixed
