# Issue 790: rational reconstruction failing for p-adics

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-10-02 18:26:01

Assignee: somebody

It's not clear to me why the following rational reconstruction is failing. Either there's a bug, or the documentation for `rational_reconstruction()` needs to explain exactly what conditions the rational reconstruction should satisfy.


```
sage: R = Zp(5, 10)
sage: x = R(8969532)
sage: x.rational_reconstruction()
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/Users/david/sage-2.8.5/<ipython console> in <module>()

/Users/david/sage-2.8.5/padic_generic_element.pyx in padic_generic_element.pAdicGenericElement.rational_reconstruction()

/Users/david/sage-2.8.5/local/lib/python2.5/site-packages/sage/rings/arith.py in rational_reconstruction(a, m, algorithm)
   1338     """
   1339     if algorithm == 'fast':
-> 1340         return integer_ring.ZZ(a).rational_reconstruction(m)
   1341     elif algorithm == 'python':
   1342         return _rational_reconstruction_python(a,m)

/Users/david/sage-2.8.5/integer.pyx in integer.Integer.rational_reconstruction()

/Users/david/sage-2.8.5/rational.pyx in rational.pyrex_rational_reconstruction()

/Users/david/sage-2.8.5/gmp.pxi in rational.mpq_rational_reconstruction()

<type 'exceptions.ValueError'>: Rational reconstruction of 8969532 (mod 9765625) does not exist.
```




---

Attachment


---

Comment by was created at 2007-11-03 18:39:44

Resolution: fixed
