# Issue 4781: creation of relative number fields when defining polynomial not integral is broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-13 03:16:45

Assignee: was


```
sage: K.<a> = NumberField(x^2 + 1)
sage: L.<b> = NumberField(K['y'].0^2 + 1/2)
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

PariError: impossible inverse modulo:  (36)
> /Users/wstein/sage/build/sage-3.2.2.alpha0/gen.pyx(8050)sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38578)()

```



---

Comment by fwclarke created at 2009-03-13 09:04:39

Seems to be fine now (3.4):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: K.<a> = NumberField(x^2 + 1)
sage: L.<b> = NumberField(K['y'].0^2 + 1/2)
sage: L
Number Field in b with defining polynomial y^2 + 1/2 over its base field
```



---

Comment by fwclarke created at 2009-03-13 09:04:39

Changing priority from major to minor.


---

Comment by davidloeffler created at 2009-07-21 08:17:38

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:17:38

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-21 08:31:12

In the above example, you can create the field L but you can't do much with it (for instance, `L.absolute_discriminant()` fails). But I would argue that this is covered by ticket #252. I propose closing this ticket as "duplicate".


---

Comment by mvngu created at 2009-07-22 18:20:55

Resolution: duplicate


---

Comment by mvngu created at 2009-07-22 18:20:55

Closing this as a duplicate of #252.
