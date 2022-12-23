# Issue 8483: Multiplication faster than squaring?

Issue created by migration from https://trac.sagemath.org/ticket/8483

Original creator: malb

Original creation time: 2010-03-09 15:37:58

Assignee: AlexGhitza

This is odd:


```python
sage: R=GF(2^283,'a')
sage: x=R.random_element()
sage: y=R.random_element()
```


First, note that squaring is slower than multiplication:


```python
sage: %timeit z=x^2
625 loops, best of 3: 3.79 µs per loop
```



```python
sage: %timeit z=x*y
625 loops, best of 3: 3.17 µs per loop
```


Now observe that squaring done differently is indeed faster:


```python
sage: %timeit z=x*x
625 loops, best of 3: 1.91 µs per loop
```



---

Comment by jdemeyer created at 2010-10-10 21:47:37

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-10-10 21:47:37

This is mainly because of the Sage Integer in the exponent:

```
sage: R=GF(2^283,'a')
sage: x=R.random_element()
```



```
sage: two=2
sage: %timeit z=x^two
625 loops, best of 3: 4.07 µs per loop
```



```
sage: two=int(2)
sage: %timeit z=x^two
625 loops, best of 3: 1.01 µs per loop
```


This is still slightly slower than normal multiplication, probably because of overhead in the `^` operator:

```
sage: %timeit z=x*x
625 loops, best of 3: 834 ns per loop
```


I suggest to close this ticket as "invalid" because this is essentially impossible to fix...


---

Comment by malb created at 2010-11-23 17:35:14

Resolution: wontfix


---

Comment by malb created at 2010-11-23 17:35:14

I think "needs_review" as not intended.
