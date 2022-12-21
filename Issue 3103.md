# Issue 3103: coercion errors of vectors from ZZ^2 and QQ^2 into CDF^2

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-05-05 04:12:05

Assignee: was

CC:  ncalexan rbradshaw jason

Keywords: vector CDF coerce

With

```
sage: version()
'SAGE Version 3.0.1.alpha0, Release Date: 2008-04-26'
```

I get the following coercion errors:


```
sage: vector(CDF, [2, 2]) * vector(ZZ, [1, 3])
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/<ipython console> in <module>()

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/element.pyx in sage.structure.element.Vector.__mul__ (sage/structure/element.c:10413)()

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5292)()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Vector space of dimension 2 over Complex Double Field' and 'Ambient free module of rank 2 over the principal ideal domain Integer Ring'
sage: vector(CDF, [2, 2]) * vector(QQ, [1, 3])
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/<ipython console> in <module>()

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/element.pyx in sage.structure.element.Vector.__mul__ (sage/structure/element.c:10413)()

/Users/ncalexan/sage-3.0.1.alpha0/devel/sage-nca/sage/rings/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5292)()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Vector space of dimension 2 over Complex Double Field' and 'Vector space of dimension 2 over Rational Field'
```



---

Comment by robertwb created at 2008-05-08 16:28:36

This is not due to coercion, but rather that dot product is not implemented for CDF^n. 


```
sage: (CDF^2)([1,2]) * (CDF^2)([2,3])
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "element.pyx", line 1884, in sage.structure.element.Vector.__mul__ (sage/structure/element.c:10398)
  File "element.pyx", line 1898, in sage.structure.element.Vector._dot_product_c (sage/structure/element.c:10564)
  File "element.pyx", line 1904, in sage.structure.element.Vector._dot_product_c_impl (sage/structure/element.c:10649)
<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Vector space of dimension 2 over Complex Double Field' and 'Vector space of dimension 2 over Complex Double Field'
```


Which, looking at element.pyx line 1904 shows that _dot_product_c_impl was never implemented for CDF. This should almost certainly be a NotImplementedError, or something like that, not a TypeError. In fact, there should just be a generic implementation.


---

Comment by ncalexan created at 2008-06-18 04:37:33

The attached patch fixes the errors (they were in fact dot_product errors and not coercion) and adds doctests and functionality for preserving inner product matrices.


---

Comment by robertwb created at 2008-06-18 08:56:21

The patch solves the problem and cleans up a lot of old code.


---

Comment by mabshoff created at 2008-06-23 04:32:43

This patch causes a number of doctest failures:

```
        sage -t -long devel/sage/sage/modular/modsym/space.py # 5 doctests failed
        sage -t -long devel/sage/sage/modular/modform/constructor.py # 3 doctests failed
        sage -t -long devel/sage/sage/modular/hecke/module.py # 12 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar_newform.py # 19 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar_ambient_jacobian.py # 2 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/abvar.py # 3 doctests failed
        sage -t -long devel/sage/sage/modular/abvar/homspace.py # 2 doctests failed
```


Cheers,

Michael


---

Comment by jason created at 2009-04-15 06:17:55

In Sage 3.4.1.rc2, this works:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: vector(CDF, [2, 2]) * vector(ZZ, [1, 3])
8.0
```

| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |
So this sounds like it is fixed.  However, are there nice doctests from the above patch that could be added to the current code?  Nick?


---

Comment by mabshoff created at 2009-04-15 06:36:41

Yes, I agree with Jason. Once we add a patch that adds a doctest this ticket can be merged and closed. By maybe someone ought to check out if Nick's patch contains anything else.

Cheers,

Michael


---

Comment by Bouillaguet created at 2013-01-12 12:36:05

Changing status from needs_work to needs_review.


---

Comment by Bouillaguet created at 2013-01-12 12:36:05

Since the problem has been fixed, here is a very simple doctest that enforces it won't happen again.

Patchbot !

apply trac_3103_add_doctest.patch


---

Attachment


---

Comment by Bouillaguet created at 2013-01-20 10:43:46

took care of stupid TAB in the patch


---

Comment by robertwb created at 2013-01-21 19:51:50

Apply only trac_3103_add_doctest.patch


---

Comment by robertwb created at 2013-01-22 00:34:39

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-25 13:06:07

Resolution: fixed
