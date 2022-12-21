# Issue 9932: BooleanPolynomialRing not recognizing leading term of elements

Issue created by migration from Trac.

Original creator: mariah

Original creation time: 2010-09-17 13:57:20

Assignee: malb


```
R = BooleanPolynomialRing(5,'x')
e = R.random_element()
print e
print e.lt()
print e.lt() in R  ## says false???
```



---

Comment by malb created at 2010-10-12 16:41:44

Changing status from new to needs_review.


---

Attachment

The attached patch fixes the reported issue. In the process I also fixed a very annoying performance issue


```python
# Old
sage: B = BooleanPolynomialRing(200,'x')
sage: %timeit B("x0")
25 loops, best of 3: 17.1 ms per loop

# New
sage: B = BooleanPolynomialRing(200,'x')
sage: %timeit B("x0")
625 loops, best of 3: 11.6 µs per loop

# "optimal"
sage: gd = B.gens_dict()
sage: %timeit gd['x0']
625 loops, best of 3: 94.2 ns per loop
```



---

Comment by malb created at 2010-11-23 19:58:50

Patch applies to 4.6.1.alpha2 and passes `make ptestlong` on sage.math.


---

Comment by mariah created at 2010-11-24 19:12:54

Changing status from needs_review to positive_review.


---

Comment by mariah created at 2010-11-24 19:12:54


```
Applied patch to sage-4.6 on skynet/lena.  Patch fixes
reported problem.  Ran 'make testlong'. All tests passed.  Positive review!
```



---

Comment by sbulygin created at 2010-11-30 08:48:44

The patch fixes the problem. All tests passed with "make ptestlong", although certain tests had to be repeated due to "time out".


---

Comment by jdemeyer created at 2010-12-02 16:09:35

Resolution: fixed
