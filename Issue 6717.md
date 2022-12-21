# Issue 6717: Sage 4.1.1.rc2: doctest failures in sage/symbolic/expression.pyx

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-08-09 18:06:33

Assignee: tbd

Georg S. Weber reported the following doctest failures at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/5f23ec4032f5e91b) thread:

```
on Mac(Intel) OS X 10.4.11 (XCode 2.5 / gcc 4.0.1 build "5370"), Sage
4.1.1.rc2 builds fine.
However, there are two (reproducible) doctest failures, one known one
and one I never saw before. The known one is:

sage -t -long "devel/sage/sage/symbolic/expression.pyx"
**********************************************************************
File "/Users/Shared/sage/sage-4.1.1.rc2/devel/sage/sage/symbolic/
expression.pyx", line 2515:
    sage: ((x+y)^a).match(w0^w1)
Expected:
    {$1: a, $0: x + y}
Got:
    {$0: x + y, $1: a}
**********************************************************************
File "/Users/Shared/sage/sage-4.1.1.rc2/devel/sage/sage/symbolic/
expression.pyx", line 2521:
    sage: ((a+b)*(a+c)).match((a+w0)*(a+w1))
Expected:
    {$1: c, $0: b}
Got:
    {$0: b, $1: c}
**********************************************************************
File "/Users/Shared/sage/sage-4.1.1.rc2/devel/sage/sage/symbolic/
expression.pyx", line 2527:
    sage: (a*(x+y)+a*z+b).match(a*w0+w1)
Expected:
    {$1: a*z + b, $0: x + y}
Got:
    {$0: x + y, $1: a*z + b}
**********************************************************************
1 items had failures:
   3 of  24 in __main__.example_62
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/Shared/sage/sage-4.1.1.rc2/
tmp/.doctest_expression.py
         [73.6 s] 
```

Here is William Stein's suggestion for fixing the above doctest failures:

```
The above doctest should be changed so they don't depend on random hashing,
e.g., change the dicts to lists of sorted tuples. 
```



---

Attachment

fix random printing problems in doctests


---

Comment by burcin created at 2009-08-09 19:47:08

Changing assignee from tbd to burcin.


---

Comment by burcin created at 2009-08-09 19:47:08

attachment:trac_6717.patch fixes the reported problems, and one more. :)


---

Comment by burcin created at 2009-08-09 19:47:08

Changing status from new to assigned.


---

Comment by GeorgSWeber created at 2009-08-09 21:16:53

Yep, this patch does the job, now the doctest does not fail anymore for me.
Although I didn't test on a system, where the test already went fine before the patch, from the nature of the changes, I'm confident, that it will still work.


---

Comment by mvngu created at 2009-08-12 00:03:20

Resolution: fixed
