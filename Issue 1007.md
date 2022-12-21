# Issue 1007: Cyclotomic polynomial broken

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-10-27 01:52:01

Assignee: was


```
sage: QQ['x'].cyclotomic_polynomial(12)
x^4 - x^2 + 1
sage: ZZ['x'].cyclotomic_polynomial(12)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/robert/<ipython console> in <module>()

/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in cyclotomic_polynomial(self, n)
    559         coeffs = str(f.Vec())
    560         if C == polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl:
--> 561             return self(coeffs, construct=True)
    562 
    563         coeffs = eval(coeffs)

/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)
    239         C = self.__polynomial_class
    240         if absprec is None:
--> 241             return C(self, x, check, is_gen, construct=construct)
    242         else:
    243             return C(self, x, check, is_gen, construct=construct, absprec = absprec)

/Users/robert/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.__init__()

/Users/robert/integer.pyx in sage.rings.integer.Integer.__init__()

<type 'exceptions.TypeError'>: unable to convert x (=[1, 0, -1, 0, 1]) to an integer
```


I am sure we can do much better than just calling Pari, maybe even using Andrew Arnold's code. 


---

Attachment


---

Comment by robertwb created at 2007-10-27 10:56:12

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2007-10-27 10:56:12

As well as fixing broken ZZ[x], we have before

```
sage: time f = pari.polcyclo(5*7*13*100)
CPU time: 0.18 s,  Wall time: 0.19 s
sage: time f = pari.polcyclo(5*7*13*1000)
CPU time: 14.68 s,  Wall time: 14.75 s
```

after

```
sage: time f = ZZ['x'].cyclotomic_polynomial(5*7*13*100)
CPU time: 0.02 s,  Wall time: 0.02 s
sage: time f = ZZ['x'].cyclotomic_polynomial(5*7*13*1000)
CPU time: 1.01 s,  Wall time: 1.02 s
```

Note that 99% of the time is spent in polynomial construction overhead

```
sage: from sage.rings.polynomial.cyclotomic import cyclotomic_coeffs
sage: time v = cyclotomic_coeffs(5*7*13*1000)
CPU time: 0.01 s,  Wall time: 0.01 s
```



---

Comment by cwitty created at 2007-10-27 19:02:03

Resolution: fixed
