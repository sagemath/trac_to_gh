# Issue 4759: add branch option to sage -upgrade

Issue created by migration from https://trac.sagemath.org/ticket/4759

Original creator: robertwb

Original creation time: 2008-12-11 10:34:45

Assignee: mabshoff

Merging the sage library with local changes can often break -upgrade. The new behavior would rename the sage-main directory if it wasn't pristine. 

See the end of http://groups.google.com/group/sage-devel/browse_thread/thread/5b566397731862d/e4b19771599e2afd?lnk=gst&q=3.2.2.alpha0#e4b19771599e2afd for the full discussion. 


```
On Dec 8, 2008, at 12:25 PM, William Stein wrote:

> On Mon, Dec 8, 2008 at 12:22 PM, Robert Bradshaw
> What about an option to the upgrade script, e.g.
>
> sage -upgrade [-b branch]
>
> which would upgrade specified branch inplace if specified?

That sounds like a reasonable compromise.


William
```



---

Comment by AlexGhitza created at 2009-01-22 18:20:18

Changing type from defect to enhancement.


---

Comment by robertwb created at 2009-02-21 15:42:48

See also #4833


---

Comment by mmezzarobba created at 2014-02-24 13:52:43

Probably no longer relevant.


---

Comment by mmezzarobba created at 2014-02-24 13:52:43

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2014-03-09 22:00:15

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-11 14:04:30

Resolution: wontfix
