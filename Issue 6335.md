# Issue 6335: optional doctest failure -- kash interface (trivial to fix)

Issue created by migration from https://trac.sagemath.org/ticket/6335

Original creator: was

Original creation time: 2009-06-16 15:18:16

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/interfaces/kash.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/kash.py", line 68:
    sage: a = kash('(9 - 7) * (5 + 6)'); a              # optional -- kash
Expected nothing
Got:
    22
**********************************************************************
1 items had failures:
   1 of 103 in __main__.example_0
***Test Failed*** 1 failures.

```



---

Comment by knsam created at 2013-02-18 21:43:52

On my Sage 5.7.beta4, all tests pass. 


```
sage -t  "devel/sage-main/sage/interfaces/kash.py"          
	 [17.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 17.4 seconds
```


So, I am marking this invalid.


---

Comment by knsam created at 2013-02-18 21:43:52

Changing status from new to needs_review.


---

Comment by knsam created at 2013-02-18 21:45:35

Oops!! There are two optional tests failing now!! So, not invalid.


---

Comment by knsam created at 2013-02-18 21:45:35

Changing status from needs_review to needs_work.
