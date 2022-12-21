# Issue 3128: PolynomialRing's behaviour does not match docstring

Issue created by migration from Trac.

Original creator: broune

Original creation time: 2008-05-07 22:31:00

Assignee: tbd

The docstring for the function PolynomialRing states

```
    OUTPUT:
        PolynomialRing(base_ring, name, sparse=False) returns a univariate
        polynomial ring; all other input formats return a multivariate
        polynomial ring.
```

which is not what PolynomialRing actually does, since

```
sage: PolynomialRing(QQ, names=['x'])
Univariate Polynomial Ring in x over Rational Field
```

Either PolynomialRing has a bug or the docstring should be corrected.


---

Comment by broune created at 2008-05-12 10:14:57

To be more precise, the problem is that the docstring of PolynomialRing says there is only one way to get a univariate polynomial ring, but in fact PolynomialRing tries to be clever and returns univariate rings in other cases too.


---

Attachment

Fixing wrong docstring statement and adding more doctests


---

Comment by SimonKing created at 2009-01-22 06:23:32

I think the new doc string covers all use cases. It also provides the corner cases (zero or one variables) as doc tests.


---

Comment by malb created at 2009-01-24 09:09:13


```
Note that a multivariate polynomial ring is returned even if the 
given number of variables is zero or one. 
```


should be replaced with


```
Note that a multivariate polynomial ring is returned when an explicit number is given.
```



---

Comment by mhansen created at 2009-10-19 19:12:02

Changing status from needs_work to needs_review.


---

Attachment

I rebased the patch and changed the docstring as per malb's suggestion.


---

Comment by mhansen created at 2009-11-05 02:28:01

I think that this can go in.


---

Comment by mhansen created at 2009-11-05 02:28:01

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-05 02:29:02

Resolution: fixed
