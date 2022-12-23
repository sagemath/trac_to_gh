# Issue 6218: small changes to jacobian_morphism to make hyperelliptic curve arithmetic faster

Issue created by migration from https://trac.sagemath.org/ticket/6218

Original creator: ncalexan

Original creation time: 2009-06-05 00:36:10

Assignee: was

CC:  craigcitro

Keywords: jacobian morphism hyperelliptic curve speed profile time

The attached patch uses % instead of the generic mod and avoids creating polynomial rings.  The savings are significant:


```
sage: F = GF(next_prime(10^30))
sage: x = F['x'].gen()
sage: f = x^7 + x^2 + 1
sage: H = HyperellipticCurve(f, 2*x); H
Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1
sage: J = H.jacobian()(F); J
verbose 0 (902: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057
sage: Q = J(H.lift_x(F(1))); Q
(x + 1000000000000000000000000000056, y + 1000000000000000000000000000056)
```


Before:

```
sage: %time ZZ.random_element(10**10) * Q
CPU times: user 0.91 s, sys: 0.02 s, total: 0.93 s
Wall time: 0.93 s
(x^3 + 402198643461859040647192719684*x^2 + 601836335767969290835741174254*x + 16518729356967251698882316239, y + 473734498489001855322294293716*x^2 + 971294794490578173226993121181*x + 205331062061696832607472618253)

sage: %timeit ZZ.random_element(10**10) * Q
10 loops, best of 3: 980 ms per loop
```


After:

```
sage: %time ZZ.random_element(10^10) * Q
CPU times: user 0.22 s, sys: 0.01 s, total: 0.23 s
Wall time: 0.25 s
(x^3 + 275125861943108889646384133572*x^2 + 753495481691507497462095614898*x + 60041420316935318537784907957, y + 904016250260250717251913633712*x^2 + 297807486916138001851276656278*x + 514899226321704405985204664612)

sage: %timeit ZZ.random_element(10**10) * Q
10 loops, best of 3: 207 ms per loop
```



---

Attachment


---

Comment by kedlaya created at 2009-06-08 22:09:58

Looks fine aside from one minor doctest failure:

```
sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/jacobian_morphism.py"
**********************************************************************
File "/home/kedlaya/sage-4.0.1/devel/sage/sage/schemes/hyperelliptic_curves/jacobian_morphism.py", line 297:
    sage: J = H.jacobian()(F); J
Expected:
    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057
Got:
    verbose 0 (902: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057
**********************************************************************
```



---

Comment by ncalexan created at 2009-06-08 22:25:18

Is that even a doctest failure?  Am I supposed to include the (spurious) warning in the output?


---

Comment by ncalexan created at 2009-06-08 22:30:01

Okay, after discussion on IRC, the warning just needs to be copied in (maybe with ... instead of 902).  So this is good to go with the doctest fixed.


---

Comment by ncalexan created at 2009-06-13 22:19:39

Resolution: fixed
