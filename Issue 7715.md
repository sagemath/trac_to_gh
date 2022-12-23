# Issue 7715: implement vectors mod 2 as M4RI matrices with one row

Issue created by migration from https://trac.sagemath.org/ticket/7715

Original creator: malb

Original creation time: 2009-12-16 17:18:14

Assignee: was

CC:  simonking

Keywords: vector, M4RI, matrix, GF(2)

In order to resolve the embarrassing situation at #3684, we need faster vectors mod 2.


---

Comment by malb created at 2009-12-16 17:29:18

The speed-up provided by this patch is considerable (but not as much as one would hope for). Here's the example from #3684:

*Before*


```python
sage: A = random_matrix(GF(2),1000,2000)
sage: %time K = A.right_kernel()
CPU times: user 11.24 s, sys: 0.02 s, total: 11.25 s
Wall time: 11.42 s
```



*After*


```python
sage: A = random_matrix(GF(2),1000,2000)
sage: %time K = A.right_kernel()
CPU times: user 0.15 s, sys: 0.00 s, total: 0.15 s
Wall time: 0.16 s
```


Speed-up: 11.25/0.15 = 75


----

Another example

*Before*


```python
sage: VS = VectorSpace(GF(2),10^4)
sage: e = VS.random_element()
sage: f = VS.random_element()
sage: %timeit e+f
10000 loops, best of 3: 89.8 µs per loop
sage: %timeit e*f
10000 loops, best of 3: 146 µs per loop
```


*After*


```python
sage: VS = VectorSpace(GF(2),10^4)
sage: e = VS.random_element()
sage: f = VS.random_element()
sage: %timeit e+f
1000000 loops, best of 3: 1.08 µs per loop
sage: %timeit e*f
100000 loops, best of 3: 2.47 µs per loop
```


Speed-ups: 83 and 59.

----
The attached patch might indeed depend on #3684.


---

Attachment


---

Comment by malb created at 2009-12-16 18:20:04

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-19 22:48:24

Looks good to me.


---

Comment by mhansen created at 2009-12-19 22:48:24

Resolution: fixed
