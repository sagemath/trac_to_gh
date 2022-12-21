# Issue 2971: One method of creating a Laurent poly ring doesn't give access to the variables

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2008-04-20 05:26:13

Assignee: mhansen

One method of creating a Laurent poly ring doesn't give access to the variables.

```
sage: R = LaurentPolynomialRing(QQ,'x',3) ; R
Multivariate Laurent Polynomial Ring in x0, x1, x2 over Rational Field
sage: x0
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/home/bump/sage/<ipython console> in <module>()

<type 'exceptions.NameError'>: name 'x0' is not defined
```



---

Comment by mhansen created at 2008-04-20 05:32:03

Hi Dan,

That is by design, and the other polynomial rings work that way as well.


```
sage: R = PolynomialRing(QQ,'x',3)
sage: x0
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/opt/sage-3.0.alpha6/devel/sage-839/<ipython console> in <module>()

<type 'exceptions.NameError'>: name 'x0' is not defined
```


You can use the .inject_variables() method to get access to the variables.


```
sage: R.inject_variables()
Defining x0, x1, x2
sage: x0
x0
```



---

Comment by mhansen created at 2008-04-20 05:32:03

Resolution: invalid
