# Issue 6313: optional doctest failure -- caused by maxima --> pynac switch ?

Issue created by migration from https://trac.sagemath.org/ticket/6313

Original creator: was

Original creation time: 2009-06-16 14:42:04

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/symbolic/expression.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/expression.pyx", line 482:
    sage: magma(f)                         # optional - magma
Expected:
    sin(cos(x^2) + log(x))
Got:
    sin(log(x) + cos(x^2))
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/expression.pyx", line 2803:
    sage: maple.eval('subs(x^2 + y^2 = t, cos(x) + sin(y) + x^2 + y^2 + t)')          # optional requires maple
Expected:
    'cos(x)+sin(y)+x^2+y^2+t'
Got:
    'read "/scratch/wstein/sage//temp/sage.math.washington.edu/560//interface//'
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_14
   1 of  18 in __main__.example_67
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_expression.py
	 [26.8 s]
```



---

Comment by mkoeppe created at 2022-08-06 19:56:06

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2022-08-06 19:56:06

outdated, should close


---

Comment by @DaveWitteMorris created at 2022-08-09 05:51:26

Changing status from needs_review to positive_review.


---

Comment by @DaveWitteMorris created at 2022-08-09 05:51:26

I agree.


---

Comment by mkoeppe created at 2022-09-01 02:30:35

Resolution: invalid
