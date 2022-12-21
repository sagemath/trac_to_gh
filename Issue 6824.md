# Issue 6824: cdef in timeseries.pyx follows use of variable

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-08-25 15:36:37

Assignee: was

CC:  was

> During sage -upgrade (from a mirror)
> 
> <snip>
> python `which cython` --embed-positions --incref-local-binop -I/usr/local/src/sage-4.1/devel/sage-main -o sage/finance/time_series.c sage/finance/time_series.pyx
> warning: /usr/local/src/sage-4.1/devel/sage-main/sage/finance/time_series.pyx:1722:24: cdef variable 'j' declared after it is used



Interesting.  We have in that function:

        `v = [(mn + j*step, mn + (j+1)*step) for j in range(bins)]`

and then a few lines later:

        `cdef Py_ssize_t j`


That's probably a bad idea.  The cdef line should be above that first line.



---

Attachment


---

Comment by jason created at 2009-08-25 15:39:29

Changing priority from major to minor.


---

Comment by mvngu created at 2009-08-25 16:58:03

Jason: You should change the file extension to ".patch" so the patch would display nicely within the browser.


---

Attachment

same as above, but with a ".patch" extension


---

Comment by mhansen created at 2009-09-26 04:33:55

Looks good to me.


---

Comment by mvngu created at 2009-09-26 05:55:50

Resolution: fixed


---

Comment by mvngu created at 2009-09-26 05:55:50

Merged `trac_6824-cdef-in-timeseries.patch`.


---

Comment by mvngu created at 2009-09-27 10:44:47

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
