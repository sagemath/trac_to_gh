# Issue 6589: bring doctest coverage for ring/laurent_series_ring.py to 100%

Issue created by migration from https://trac.sagemath.org/ticket/6589

Original creator: mhampton

Original creation time: 2009-07-22 13:07:51

Assignee: tbd

Keywords: Laurent series, doctest, coverage

I (Marshall Hampton) am hoping to work on this in late July or August 2009.  If it hasn't been done by September, assume that I didn't get around to it.


---

Comment by knsam created at 2013-02-03 19:49:29

As of Sage 5.7.beta2, the file in question does have 100% coverage. So, I think this has been done. See the related #12259 (which itself is a part of the bigger meta ticket: #12024). So, I'll set this to sage-invalid...


---

Comment by knsam created at 2013-02-03 19:50:03

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-02-05 18:02:55

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2013-02-05 18:02:55

Also in `5.5.rc0`:

```
travis@travis-virtualbox:~/sage-5.5.rc0/devel/sage/sage$ sage -coverage rings/laurent_series_ring.py 
----------------------------------------------------------------------
rings/laurent_series_ring.py
SCORE rings/laurent_series_ring.py: 100% (25 of 25)
----------------------------------------------------------------------
```



---

Comment by jdemeyer created at 2013-02-08 13:24:35

Resolution: worksforme
