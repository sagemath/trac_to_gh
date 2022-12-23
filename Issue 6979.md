# Issue 6979: improve sparse matrix/vector product

Issue created by migration from https://trac.sagemath.org/ticket/6979

Original creator: ylchapuy

Original creation time: 2009-09-21 19:01:46

Assignee: was

we add ad hoc methods in matrix_sparse.pyx


---

Comment by ylchapuy created at 2009-09-21 19:13:16

for the record:

```
sage: m=random_matrix(ZZ,1000,sparse=True,density=0.01)sage: m=random_matrix(GF(17),1000,sparse=True,density=0.01)
sage: v=vector([randrange(100) for i in xrange(1000)])
```

before:

```
sage: timeit('m*v')
5 loops, best of 3: 257 ms per loop
```

after:

```
timeit('m*v')
5 loops, best of 3: 61 ms per loop
```



---

Comment by jason created at 2009-09-22 15:03:01

I added some doctests in a reviewer patch that ensure that the current return type behavior doesn't change without breaking something (i.e., notifying us that it changed).


---

Comment by mvngu created at 2009-09-25 03:33:40

I got this doctest failure:

```
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py", line 1423:
    sage: M*G
Expected:
    (0, 0)
Got:
    (0, 0, 0)
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_30
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_multi_polynomial_ideal.py
	 [15.4 s]
```



---

Comment by jason created at 2009-09-29 06:16:58

The code for both v*M and M*v has the result of type:

        s = v.parent()(0) 

However, the dimension here is clearly wrong---we don't get a result the size of the vector, but the number of rows of M if computing M*v, and the number of columns of M if computing v*M.


---

Comment by ylchapuy created at 2009-09-29 10:47:57

oups, this was of course silly...
Here is an updated patch replacing only mine.
Both patches need to be applied.


---

Comment by jason created at 2009-09-29 14:13:43

Thanks!

I still think there is a problem.  For dense things, v*M gets its base ring from M, not v.  However, the above patch gets the base ring from v.  That's what my doctest patch tests.


---

Comment by ylchapuy created at 2010-03-10 16:10:03

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-04-06 04:03:59

The doctest


```
sage:  (m*v).parent() is m.row(0).parent()
```


looks backwards to me (columns <-> rows).  A matrix-vector product should be a linear combination of the columns of the matrix, no?  I think the only reason it passes is that the matrix employed is square.  If I make the matrix rectangular, it fails.  If correct, the companion in the other method also needs fixing.

The original doctest patch has contributions to to `sage/matrix/matrix0.pyx` and `sage/matrix/matrix_sparse.pyx`, but the sparse tests are in the latest patch, but the "0" tests are not.

With some guidance, I'd look at this again for a review.


---

Comment by rbeezer created at 2010-04-06 04:03:59

Changing status from needs_review to needs_work.


---

Attachment

based on 4.5.3


---

Comment by ylchapuy created at 2010-09-26 20:32:33

The matrices in the doctest are now rectangular, and the tests corrected accordingly.

Both `matrix0.pyx` and `matrix_sparse.pyx` are modified.

Ready for review (at last).


---

Comment by ylchapuy created at 2010-09-26 20:32:33

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-09-28 20:30:15

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-09-28 20:30:15

Looks good!  I deleted my patch, since you now have those doctests.

Positive review.


---

Comment by mpatel created at 2010-09-29 04:23:31

Resolution: fixed
