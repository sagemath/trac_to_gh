# Issue 9858: Doctest failures due to hard-coded line numbers in (doctests of) sage/rings/*.pyx

Issue created by migration from https://trac.sagemath.org/ticket/9859

Original creator: leif

Original creation time: 2010-09-06 04:32:10

Assignee: mvngu

Keywords: DeprecationWarning failure integer.pyx rational.pyx beginner


```
$ ./sage -t  -long devel/sage/sage/rings/integer.pyx
sage -t -long "devel/sage/sage/rings/integer.pyx"           
**********************************************************************
File "devel/sage/sage/rings/integer.pyx", line 4618:
    sage: 5.sqrt_approx(prec=200)
Expected:
    doctest:1172: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.
    2.2360679774997896964091736687312762354406183596115257242709
Got:
    doctest:1176: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.
    2.2360679774997896964091736687312762354406183596115257242709
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_118
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_integer.py
	 [16.4 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/rings/integer.pyx"
Total time for all tests: 16.4 seconds
$ ./sage -t  -long devel/sage/sage/rings/rational.pyx 
sage -t -long "devel/sage/sage/rings/rational.pyx"          
**********************************************************************
File "devel/sage/sage/rings/rational.pyx", line 1339:
    sage: (5/3).sqrt_approx()
Expected:
    doctest:1172: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.
    1.29099444873581
Got:
    doctest:1176: DeprecationWarning: This function is deprecated.  Use sqrt with a given number of bits of precision instead.
    1.29099444873581
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_31
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_rational.py
	 [4.5 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/rings/rational.pyx"
Total time for all tests: 4.6 seconds
```


These failures occurred just because some line numbers in `$SAGE_LOCAL/bin/ncadoctest.py` changed (when I added some flush statements).


---

Comment by leif created at 2010-09-06 04:36:55

Minh, please excuse and change the component in case it's the wrong one. (I'm not sure if "doctest" refers to the framework or doctest failures in general.)


---

Comment by leif created at 2010-09-06 05:04:08

Based on Sage 4.5.3.rc0. Apply to Sage library.


---

Attachment

Ok, I'm a beginner. ;-)

(I've uploaded a patch.)


---

Comment by leif created at 2010-09-06 05:06:53

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-09-07 18:45:38

Those hard-coded line numbers that leif fixed shouldn't have been there in the first place. The patch applied OK against Sage 4.5.3.rc0, all doctests (including long) passed, and the standard documentation built fine. And I'm OK with the changes in the patch.


---

Comment by mvngu created at 2010-09-07 18:45:38

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-07 19:22:52

Replying to [comment:3 mvngu]:
> Those hard-coded line numbers that leif fixed shouldn't have been there in the first place.

Yes. According to Mercurial, Michael Abshoff introduced that in Jan 2009(!)... :-)
(There's no ticket number in the commit message. I'm not sure when it really got merged, but obviously long time ago.)

I wonder why I never ran into this before, since I frequently doctest with modified versions of `ncadoctest` (but perhaps incidentally not the whole Sage library, or `sage/rings`).

Thanks for reviewing this.


---

Comment by mpatel created at 2010-09-15 10:40:58

Resolution: fixed
