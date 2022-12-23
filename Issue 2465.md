# Issue 2465: 2.10.3 doctest failure in groebner_fan.py

Issue created by migration from https://trac.sagemath.org/ticket/2465

Original creator: mabshoff

Original creation time: 2008-03-11 01:43:15

Assignee: failure

The failure is

```
File "groebner_fan.py", line 42:
    sage: g.reduced_groebner_bases()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        g.reduced_groebner_bases()###line 42:
    sage: g.reduced_groebner_bases()
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 272, in reduced_groebner_bases
        G0 = self._gfan_reduced_groebner_bases()
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 230, in _gfan_reduced_groebner_bases
        B = self.gfan()
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 310, in gfan
        I = self._gfan_ideal()
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 214, in _gfan_ideal
        J = to_gfan(self.__ideal)
      File "morphism.pyx", line 116, in sage.categories.morphism.Morphism.__call__
      File "multi_polynomial_libsingular.pyx", line 618, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
        return self(str(element))
      File "multi_polynomial_libsingular.pyx", line 525, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
        element = eval(element, d, {})
      File "<string>", line 1
         Ideal (x**2 - y**2 + 1) of Multivariate Polynomial Ring in x, y over Rational Field
                                  ^
     SyntaxError: invalid syntax
**********************************************************************
```



---

Comment by was created at 2008-03-11 01:44:44

Changing assignee from failure to was.


---

Attachment


---

Comment by was created at 2008-03-11 02:13:30

Resolution: fixed


---

Comment by mabshoff created at 2008-03-11 02:31:21

The patch fixes the doctest failure. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-11 02:37:58

Merged in Sage 2.10.3.rc5
