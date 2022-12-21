# Issue 7419: implicit_plot ignores the z-range

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-11-09 17:44:29

Assignee: was

CC:  wcauchois

This does not produce half of a sphere:


```
implicit_plot3d((x^2)/2+(y^2)/2+(z^2)/2,(x,-5,5),(y,-5,5),(z,
0,5),contour=2)
```


The problem and solution were found in http://groups.google.com/group/sage-support/browse_thread/thread/69efe89a6aa97473

Reported by Micah (I don't see a last name on the email post reporting this)


---

Attachment


---

Comment by jason created at 2009-11-09 17:47:58

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-11-10 15:03:21

This looks good.  I added a little extra explanation because the aspect_ratio needed to be set for the hemispheres to not look too weird.  I can't believe that little 1 was sitting there the whole time, wanting to be a 2!  Positive review, apply only reviewer patch.


---

Comment by kcrisman created at 2009-11-10 15:03:21

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-11-10 15:03:47

Based on 4.2.1.alpha0, apply only this patch.


---

Attachment


---

Comment by wcauchois created at 2009-11-10 19:42:16

This must have been a simple copy-pasting error on my part. I'm glad we caught it!


---

Comment by jason created at 2009-11-10 20:03:20

I'm pretty sure it's my fault from when I did the setup_eval_from_grid patch.


---

Comment by mhansen created at 2009-11-12 06:46:05

Resolution: fixed
