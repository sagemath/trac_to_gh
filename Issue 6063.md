# Issue 6063: x^2 for x over QQ is really frickin' slow compared to over ZZ (nearly factor of 100!!)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-05-18 05:28:40

Assignee: somebody


```
wstein`@`sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x> = ZZ[]
sage: timeit('x^2')
625 loops, best of 3: 1.4 µs per loop
sage: R.<x> = QQ[]
sage: timeit('x^2')
625 loops, best of 3: 118 µs per loop
sage: %prun x**2
         34 function calls in 0.001 CPU seconds
| Sage Version 3.4.1, Release Date: 2009-04-21                       |
| Type notebook() for the GUI, and license() for information.        |
   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 polynomial_element_generic.py:590(__init__)
        4    0.000    0.000    0.000    0.000 polynomial_element_generic.py:656(__getitem__)
        3    0.000    0.000    0.000    0.000 {method 'poldegree' of 'sage.libs.pari.gen.gen' objects}
        3    0.000    0.000    0.000    0.000 polynomial_element_generic.py:874(degree)
        2    0.000    0.000    0.000    0.000 {method 'Polrev' of 'sage.libs.pari.gen.gen' objects}
        1    0.000    0.000    0.000    0.000 polynomial_ring.py:211(_element_constructor_)
        1    0.000    0.000    0.000    0.000 polynomial_ring.py:741(gen)
        9    0.000    0.000    0.000    0.000 {isinstance}
        3    0.000    0.000    0.000    0.000 {max}
        1    0.000    0.000    0.000    0.000 {hasattr}
        1    0.000    0.000    0.000    0.000 polynomial_ring.py:810(is_sparse)
        1    0.000    0.000    0.000    0.000 {method 'type' of 'sage.libs.pari.gen.gen' objects}
        1    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {sage.rings.fraction_field_element.is_FractionFieldElement}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

sage: R.<x> = ZZ[]
sage: %prun x**2
         3 function calls in 0.000 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 polynomial_ring.py:741(gen)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

```



---

Comment by AlexGhitza created at 2009-07-13 13:54:00

See also #4000, which might be the best way to fix this.


---

Comment by was created at 2010-01-18 01:31:02

This is because polynomials over QQ are still pure Python.   This is an enhancement, not a bug.


---

Comment by was created at 2010-01-18 01:31:02

Changing type from defect to enhancement.


---

Comment by jrp created at 2011-01-21 22:20:06

This appears to be fixed now - the QQ one is even slightly faster.


---

Comment by davidloeffler created at 2011-01-22 15:50:53

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2011-01-22 15:50:53

Yes, this is fixed. Release manager: please close this ticket.


---

Comment by davidloeffler created at 2011-01-22 15:50:59

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-22 19:44:29

Resolution: duplicate
