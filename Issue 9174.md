# Issue 9174: cygwin: robert miller's 2-descent is completely broken on cygwin

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-07 04:57:52

Assignee: tbd

CC:  jpflori dimpase kcrisman


```

sage -t  "devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx"
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1093:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    1
Got:
    0
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1098:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    2
Got:
    0
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1102:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    3
Got:
    2*log(3)/log(2) - 2
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1195:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    1
Got:
    0
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1198:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    2
Got:
    0
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx", line 1201:
    sage: log(n1,2) + log(n1_prime,2) - 2 # the rank
Expected:
    3
Got:
    log(3)/log(2) - 1
**********************************************************************
2 items had failures:
   3 of  30 in __main__.example_18
   3 of  11 in __main__.example_19
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_descent_two_isogeny.py
	 [29.1 s]
```



---

Comment by kcrisman created at 2011-08-02 02:25:15

This file passed doctests in a build of mine on XP.


---

Comment by kcrisman created at 2011-08-19 14:27:18

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-08-19 14:27:18

And checking by hand works. 

Since this was undoubtedly an XP machine on which the original failure was reported, I will move this to sage-invalid.


---

Comment by kcrisman created at 2011-08-19 14:27:25

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-08-19 14:40:56

But doing anything other than the *first* one by hand doesn't work.  In fact, nasty things happen.


---

Comment by kcrisman created at 2011-08-19 14:40:56

Changing status from positive_review to needs_work.


---

Comment by kcrisman created at 2013-01-15 16:00:29

I attempted this, but got forking errors; that doesn't mean it doesn't actually work.  JP, want to give it a whirl?


---

Comment by jpflori created at 2013-01-15 18:07:05

And the test passes for me (64bits W7 + 5.6.rc0).


---

Comment by kcrisman created at 2013-01-15 18:11:35

> And the test passes for me (64bits W7 + 5.6.rc0).
Don't forget to try these by hand as well.  In the past I've had failures only in the terminal.


---

Comment by jpflori created at 2013-01-30 10:48:18

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2013-02-08 12:46:18

No problems on another 32 bits W7, let's close this one.


---

Comment by jpflori created at 2013-02-08 12:46:18

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-08 13:18:48

Resolution: worksforme
