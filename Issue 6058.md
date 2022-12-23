# Issue 6058: Add basic statistics functionality at the top level

Issue created by migration from https://trac.sagemath.org/ticket/6058

Original creator: mhampton

Original creation time: 2009-05-17 21:02:12

Assignee: jkantor

Sage should provide basic statistics functionality at the top level.  These functions might use scipy.stats or R or a new native implementation.  For graphics in particular we should probably bypass R.  

This ticket will merely start this process with one patch, but will not completely address the needed functionality.


---

Comment by mhampton created at 2009-05-17 21:18:47

A baby step towards top-level statistics


---

Attachment

Comments are welcome on this very initial effort.


---

Comment by mhampton created at 2009-05-17 21:30:47

Changing assignee from jkantor to mhampton.


---

Comment by mhampton created at 2009-05-17 21:30:47

Changing component from numerical to statistics.


---

Comment by craigcitro created at 2009-05-17 22:05:20

Two quick comments:

 * With the mean function, dividing by `len(a_list)` is *really* dangerous -- for instance, if you give the function a collection of Python `int`s, then it will do Python `int` division -- so `3/2 = 1`, etc. Bad news.

 * Do we want to use the name `std` for standard deviation? Since the other systems (e.g. R) use that, we should have it available, but I would also like to have the full `standard_deviation` available (especially since we have `variance` as opposed to just `var`, for obvious reasons).


---

Comment by kcrisman created at 2012-06-01 18:42:48

This apparently was done at around the same time as this was posted by #7197, and no one noticed.  Sorry, Marshall :( but on the plus side we have had this since Sage 4.3 :)

To release manager - this is invalid/dup.


---

Comment by kcrisman created at 2012-06-01 18:42:48

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-06-02 12:34:28

Resolution: duplicate
