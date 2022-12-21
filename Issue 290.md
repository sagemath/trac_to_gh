# Issue 290: Converting Pari multivariate polynomials  to MPolynomials doesn't work

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-02-24 05:04:12

Assignee: somebody


```
QQxy.<x, y> = QQ['x', 'y']; QQxy(pari(x+y))
<type 'exceptions.TypeError'>: Unable to coerce x + y (<type 'sage.libs.pari.gen.gen'>) to Rational
```


(Reported by cwitty)


---

Comment by malb created at 2007-02-24 05:05:14

Changing status from new to assigned.


---

Comment by malb created at 2007-02-24 05:05:14

Changing assignee from somebody to malb.


---

Comment by mabshoff created at 2007-08-21 10:06:54

This is still an issue with 2.8.2pre:

```
sage: QQxy.<x, y> = QQ['x', 'y']; QQxy(pari(x+y))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/tmp/Work2/sage-2.8.1/sage-2.8.1/<ipython console> in <module>()

/tmp/Work2/sage-2.8.1/sage-2.8.1/multi_polynomial_libsingular.pyx in multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__()

/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)
    178         if isinstance(x, sage.rings.rational.Rational):
    179             return x
--> 180         return sage.rings.rational.Rational(x, base)
    181
    182     def construction(self):

/tmp/Work2/sage-2.8.1/sage-2.8.1/rational.pyx in rational.Rational.__init__()

/tmp/Work2/sage-2.8.1/sage-2.8.1/rational.pyx in rational.Rational.__set_value()

<type 'exceptions.TypeError'>: Unable to coerce x + y (<type 'sage.libs.pari.gen.gen'>) to Rational
```


I would like to tag this for 2.9 - malb do you agree or would you like to postpone this?

Cheers,

Michael


---

Comment by was created at 2007-08-31 20:43:50

This works now.


---

Comment by was created at 2007-08-31 20:43:56

Resolution: fixed
