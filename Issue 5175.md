# Issue 5175: [bug] Bug computing Bessel function J0(0)

Issue created by migration from Trac.

Original creator: pdenapo

Original creation time: 2009-02-04 17:19:04

Assignee: tbd

A bug under sage 3.2.3 computing J_0(0)
(which should be just "1")

sage: g=Bessel(0)
sage: g          
J_{0}            
sage: g(1)
0.765197686557967
sage: g(0)      
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/home/pablo/sage/sage-3.1/<ipython console> in <module>()

/home/pablo/sage/sage-3.1/local/lib/python2.5/site-packages/sage/functions/special.pyc in __call__(self, z)
    689             return bessel_I(nu,z,algorithm=s,prec=p)
    690         if t == "J":
--> 691             return bessel_J(nu,z,algorithm=s,prec=p)
    692         if t == "K":
    693             return bessel_K(nu,z,algorithm=s,prec=p)

/home/pablo/sage/sage-3.1/local/lib/python2.5/site-packages/sage/functions/special.pyc in bessel_J(nu, z, algorithm, prec)
    522             K = C
    523         K = z.parent()
--> 524         return K(pari(nu).besselj(z, precision=prec))
    525     elif algorithm=="scipy":
    526         if prec != 53:

/home/pablo/sage/sage-3.1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38645)()

PariError:  (8)


---

Comment by AlexGhitza created at 2009-07-11 11:18:52

Changing component from algebra to interfaces.


---

Comment by AlexGhitza created at 2009-07-11 11:18:52

This works in sage-4.1:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: g = Bessel(0)
sage: g(0)
1.00000000000000
```



---

Comment by AlexGhitza created at 2009-07-11 11:18:52

Changing assignee from tbd to was.


---

Comment by mvngu created at 2009-08-12 16:04:53

Resolution: fixed
