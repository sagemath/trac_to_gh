# Issue 9559: *generalized* canonical generation in Cython

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-07-21 08:27:52

Assignee: joyner

CC:  boothby ncohen kini dimpase

Right now this ticket is for organization, so I'm leaving it as "new".


---

Comment by rlm created at 2010-07-21 08:28:12

Changing assignee from joyner to rlm.


---

Comment by rlm created at 2011-05-18 04:53:23

Changing status from new to needs_review.


---

Comment by boothby created at 2012-01-22 00:54:44

Changing status from needs_review to positive_review.


---

Comment by boothby created at 2012-01-22 01:06:26


```
477c477,478
< groups/perm_gps/partn_ref/refinement_graphs.pyx: 100% (8 of 8)
---
> groups/perm_gps/partn_ref/refinement_graphs.pyx: 100% (10 of 10)
> groups/perm_gps/partn_ref/refinement_sets.pyx: 100% (3 of 3)
1299,1300c1300,1301
< Total number of functions:  28567
< We need 1110 more function to get to 90% coverage.
---
> Total number of functions:  28572
> We need 1109 more function to get to 90% coverage.
```



---

Comment by jdemeyer created at 2012-01-23 22:12:45

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-01-23 22:12:45

The commit message needs to be fixed, it certainly should not contain "[mq]".

Newly added files should conform to the template at [http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files](http://sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files).

New documentation strings should conform to [http://sagemath.org/doc/developer/conventions.html#documentation-strings](http://sagemath.org/doc/developer/conventions.html#documentation-strings).


---

Attachment


---

Comment by rlm created at 2013-01-17 04:39:52

Changing status from needs_work to needs_review.


---

Comment by boothby created at 2013-01-17 04:42:36

Changing status from needs_review to positive_review.


---

Comment by boothby created at 2013-01-17 04:42:36

Tests pass, formatting updated as requested by jdemeyer.


---

Comment by jdemeyer created at 2013-01-21 21:07:39

Resolution: fixed
