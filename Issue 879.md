# Issue 879: "sage -testall" should summarize all failures at the end of the run

Issue created by migration from https://trac.sagemath.org/ticket/879

Original creator: cwitty

Original creation time: 2007-10-13 19:05:33

Assignee: failure

CC:  gfurnish mjo

"sage -testall" has at least three parts (DSage unit tests, documentation doctests, library doctests).  If some documentation doctests fail, you have to know to look in the middle of the -testall output to notice; the end of the output may well say that all tests passed (meaning all library doctests).


---

Comment by cremona created at 2008-09-04 15:21:33

The desired behaviour is what actually happens now, so this ticket can surely be closed.


---

Comment by mabshoff created at 2008-09-04 17:13:41

This is actually not solved yet in the regular sage-test, but in sage-ptest. We need to merge the two implementations or alternatively move the features to sage-test to close this ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-05 05:19:58

FYI


---

Comment by AlexGhitza created at 2009-01-22 18:23:58

Changing type from defect to enhancement.


---

Comment by mderickx created at 2011-08-23 21:14:08

I think this ticket can be closed since it works now.


---

Comment by mderickx created at 2011-08-23 21:14:08

Changing status from new to needs_review.


---

Comment by mjo created at 2011-12-01 02:56:58

Changing status from needs_review to positive_review.


---

Comment by mjo created at 2011-12-01 02:56:58

Agreed, it's working now. I broke a test in the tutorial and some others in the main library are failing because of an upgraded Maxima spkg. They all get shown in the summary at the end:


```
$ sage -testall

...

The following tests failed:


	sage -t  -force_lib "devel/sage/doc/en/tutorial/tour_functions.rst"
	sage -t  -force_lib "devel/sage/sage/symbolic/expression.pyx"
	sage -t  -force_lib "devel/sage/sage/symbolic/integration/integral.py"
	sage -t  -force_lib "devel/sage/sage/interfaces/maxima_abstract.py"
	sage -t  -force_lib "devel/sage/sage/tests/cmdline.py"
Total time for all tests: 6717.0 seconds
Please see /home/mjo/.sage//tmp/test.log for the complete log from this test.
```



---

Comment by jdemeyer created at 2011-12-09 10:25:41

Resolution: worksforme
