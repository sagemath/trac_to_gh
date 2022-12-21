# Issue 9517: PolynomialRing() returns Multivariate polynomial rings when you would expect univariate ones

Issue created by migration from Trac.

Original creator: mderickx

Original creation time: 2010-07-16 10:20:32

Assignee: malb

Below is an example of the strange behavior in sage 4.4.4.


```
sage: PR1=PolynomialRing(QQ,'x');PR2=PolynomialRing(QQ,1,'x')
sage: PR1;PR2
Univariate Polynomial Ring in x over Rational Field
Multivariate Polynomial Ring in x over Rational Field
```


I've searched for similar problems but only #9220 seems vagely related but is a real different problem.


---

Comment by malb created at 2010-07-16 10:30:12

It's not a bug it's a feature :)

From the documentation of PolynomialRing:


```
``PolynomialRing(base_ring, name, sparse=False)`` returns a univariate polynomial ring; also, PolynomialRing(base_ring, names, sparse=False) yields a univariate polynomial ring, if names is a list or tuple providing exactly one name. All other input formats return a multivariate polynomial ring.
```



---

Comment by malb created at 2010-07-16 10:30:12

Resolution: wontfix
