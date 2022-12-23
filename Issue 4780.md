# Issue 4780: relative number field constructor -- error message when given poly of degree < 1 is bad

Issue created by migration from https://trac.sagemath.org/ticket/4780

Original creator: was

Original creation time: 2008-12-13 03:14:59

Assignee: was


```
sage: K.<a> = NumberField(x^2 + 1)
sage: L.<b> = NumberField(K['y'](1))
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/Users/wstein/sage/build/sage-3.2.2.alpha0/<ipython console> in <module>()

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in NumberField(polynomial, name, check, names, cache, embedding)
    374 
    375     if isinstance(R, NumberField_generic):
--> 376         S = R.extension(polynomial, name, check=check)
    377         if cache:
    378             _nf_cache[key] = weakref.ref(S)

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in extension(self, poly, name, names, check, embedding)
   2570         if name is None:
   2571             raise TypeError, "the variable name must be specified."
-> 2572         return NumberField_relative(self, poly, str(name), check=check, embedding=embedding)
   2573 
   2574     def factor(self, n):

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in __init__(self, base, polynomial, name, latex_name, names, check, embedding)
   4567 
   4568         self.__pari_relative_polynomial = pari(str(polynomial_y))
-> 4569         self.__rnf = self.__base_nf.rnfinit(self.__pari_relative_polynomial)
   4570         
   4571         self.__base_field = base

/Users/wstein/sage/build/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38578)()

PariError: not a polynomial (38)
> /Users/wstein/sage/build/sage-3.2.2.alpha0/gen.pyx(8050)sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38578)()

```



---

Comment by mhansen created at 2009-06-04 23:41:46

This seems to be better now:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: K.<a> = NumberField(x^2 + 1)
sage: sage: L.<b> = NumberField(K['y'](1))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
| Sage Version 4.0.1.rc1, Release Date: 2009-06-04                   |
| Type notebook() for the GUI, and license() for information.        |
/home/mhansen/.sage/temp/sage.math.washington.edu/25032/_home_mhansen__sage_init_sage_0.py in <module>()

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in NumberField(polynomial, name, check, names, cache, embedding)
    415 
    416     if isinstance(R, NumberField_generic):
--> 417         S = R.extension(polynomial, name, check=check)
    418         if cache:
    419             _nf_cache[key] = weakref.ref(S)

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.pyc in extension(self, poly, name, names, check, embedding)
   2920             raise TypeError, "the variable name must be specified."
   2921         from sage.rings.number_field.number_field_rel import NumberField_relative
-> 2922         return NumberField_relative(self, poly, str(name), check=check, embedding=embedding)
   2923 
   2924     def factor(self, n):

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_rel.pyc in __init__(self, base, polynomial, name, latex_name, names, check, embedding)
    274                 # future, is_irreducible should be made faster for
    275                 # polynomials over number fields -- see ticket #4724
--> 276                 raise ValueError, "defining polynomial (%s) must be irreducible"%polynomial
    277 
    278         self.__gens = [None]

ValueError: defining polynomial (1) must be irreducible
```


Comments?


---

Comment by davidloeffler created at 2009-07-20 20:30:52

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 20:30:52

Changing component from number theory to number fields.


---

Comment by mhansen created at 2012-03-29 07:36:21

Can this be closed now?


---

Comment by davidloeffler created at 2012-03-29 07:47:47

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2012-03-29 07:47:47

Yes, I think so.


---

Comment by davidloeffler created at 2012-03-29 07:48:00

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-04-04 13:27:01

Resolution: worksforme
