# Issue 9257: remove misc/darcs.py in Sage 5.0

Issue created by migration from https://trac.sagemath.org/ticket/9257

Original creator: mvngu

Original creation time: 2010-06-18 05:58:15

Assignee: mvngu

From [sage-devel](https://groups.google.com/group/sage-devel/browse_thread/thread/971ea3ce256eed20):

```
The file misc/darcs.py was meant to serve as an interface to the Darcs
source code version control system, back in the old days before Sage
switched to using Mercurial. With the upcoming Sage 5.0 milestone, I
think that module can be removed from the Sage library. I believe its
removal would result in very minimal (next to zero?) hassle regarding
issues of backward compatibility. If I understand the Mercurial log of
the Sage library correctly, Sage hasn't been using Darcs for over 2
years now, or even since February 2006. 
```



---

Attachment


---

Comment by robertwb created at 2010-06-21 21:36:15

Changing status from new to needs_review.


---

Comment by rlm created at 2010-06-22 17:39:37

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-22 17:39:37

Looks good to me.


---

Comment by mpatel created at 2010-07-21 10:10:38

Resolution: fixed


---

Comment by kcrisman created at 2012-06-16 03:20:00

Followup; apparently we _still_ have remnants of darcs.  See #13122.


---

Comment by kcrisman created at 2012-06-16 03:21:39

As a historical note, the original thread referenced here was off by about a year and a half on when Sage 5.0 would be released... ah, expectations.
