# Issue 4696: coercion system doesn't expect pickled parents

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-12-04 21:08:44

Assignee: robertwb

The coercion system expects parents to be unique. This doesn't seem to hold when pickled parents are involved.


```
sage: x,y = QQ['x,y'].gens()
sage: i = ideal(x^2 - y^2 + 1)
sage: j = loads(dumps(i))
sage: i == j
True
sage: j == i
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/burcin/sage/sage-3.2.1.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:5329)()
    575 
    576 
--> 577 
    578 
    579 

/home/burcin/sage/sage-3.2.1.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:4807)()
    516 
    517 
--> 518 
    519 
    520 

/home/burcin/sage/sage-3.2.1.alpha2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:6345)()
    770 
    771 
--> 772 
    773 
    774 

/home/burcin/sage/sage-3.2.1.alpha2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps._coercion_error (sage/structure/coerce.c:11109)()
   1275 
   1276 
-> 1277 
   1278 
   1279 

RuntimeError: There is a bug in the coercion code in SAGE.
Both x (=Ideal (x^2 - y^2 + 1) of Multivariate Polynomial Ring in x, y over Rational Field) and y (=Ideal (x^2 - y^2 + 1) of Multivariate Polynomial Ring in x, y over Rational Field) are supposed to have identical parents but they don't.
In fact, x has parent 'Monoid of ideals of Multivariate Polynomial Ring in x, y over Rational Field'
whereas y has parent 'Monoid of ideals of Multivariate Polynomial Ring in x, y over Rational Field'
Original elements Ideal (x^2 - y^2 + 1) of Multivariate Polynomial Ring in x, y over Rational Field (parent Monoid of ideals of Multivariate Polynomial Ring in x, y over Rational Field) and Ideal (x^2 - y^2 + 1) of Multivariate Polynomial Ring in x, y over Rational Field (parent Monoid of ideals of Multivariate Polynomial Ring in x, y over Rational Field) and maps
<type 'NoneType'> None
<type 'sage.categories.morphism.CallMorphism'> Call morphism:
  From: Monoid of ideals of Multivariate Polynomial Ring in x, y over Rational Field
  To:   Monoid of ideals of Multivariate Polynomial Ring in x, y over Rational Field
```




---

Comment by mhansen created at 2013-07-23 00:32:14

Resolution: invalid


---

Comment by mhansen created at 2013-07-23 00:32:14

This works now:


```
sage: sage: x,y = QQ['x,y'].gens()
sage: sage: i = ideal(x^2 - y^2 + 1)
sage: sage: j = loads(dumps(i))
sage: sage: i == j
True
sage: j == i
True
```

