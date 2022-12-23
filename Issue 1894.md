# Issue 1894: toy_buchberger failures

Issue created by migration from https://trac.sagemath.org/ticket/1894

Original creator: gfurnish

Original creation time: 2008-01-23 15:01:45

Assignee: failure


```

File "toy_buchberger.py", line 60:
    sage: I = sage.rings.ideal.Katsura(P)
Exception raised:
    Traceback (most recent call last):
      File "/home/x/build/sage-2.10.1.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[12]>", line 1, in <module>
        I = sage.rings.ideal.Katsura(P)###line 60:
    sage: I = sage.rings.ideal.Katsura(P)
      File "/home/x/build/sage-2.10.1.alpha1/local/lib/python2.5/site-packages/sage/rings/ideal.py", line 520, in Katsura
        return R.ideal(I)
      File "multi_polynomial_libsingular.pyx", line 703, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.ideal
        gens = list(gens)
      File "/home/x/build/sage-2.10.1.alpha1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 1132, in __iter__
        if self.type()=='matrix':
      File "/home/x/build/sage-2.10.1.alpha1/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 1129, in type
        return m.group(int(1))
    AttributeError: 'NoneType' object has no attribute 'group'
**********************************************************************
File "toy_buchberger.py", line 62:
    sage: I
Expected:
    Ideal (a + 2*b + 2*c - 1, a^2 + 2*b^2 + 2*c^2 - a, 2*a*b + 2*b*c - b) of Multivariate Polynomial Ring in a, b, c over Finite Field of size 127
Got:
    Ideal (a + 2*b + 2*c + 2*e + 2*f + 2*g - 1, a^2 + 2*b^2 + 2*c^2 + 2*e^2 + 2*f^2 + 2*g^2 - a, 2*a*b + 2*b*c + 2*c*e + 2*e*f + 2*f*g - b, b^2 + 2*a*c + 2*b*e + 2*c*f + 2*e*g - c, 2*b*c + 2*a*e + 2*b*f + 2*c*g - e, c^2 + 2*b*e + 2*a*f + 2*b*g - f) of Multivariate Polynomial Ring in a, b, c, e, f, g, h, i, j, k over Finite Field of size 32003
**********************************************************************
File "toy_buchberger.py", line 67:
    sage: buchberger(I)
Expected:
    (a + 2*b + 2*c - 1, a^2 + 2*b^2 + 2*c^2 - a) => -2*b^2 - 6*b*c - 6*c^2 + b + 2*c
    G: set([a + 2*b + 2*c - 1, 2*a*b + 2*b*c - b, a^2 + 2*b^2 + 2*c^2 - a, -2*b^2 - 6*b*c - 6*c^2 + b + 2*c])
    <BLANKLINE>
```

More follows for hundreds of lines
Gentoo  x64 gcc 4.2.2


---

Attachment

fixes bug and adapts doctest


---

Comment by mabshoff created at 2008-01-23 22:16:38

Patch looks good to me. Doctests pass now.


---

Comment by mabshoff created at 2008-01-23 22:17:36

Merged in Sage 2.10.1.alpha2


---

Comment by mabshoff created at 2008-01-23 22:17:36

Resolution: fixed
