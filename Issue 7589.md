# Issue 7589: bug in coercion and cyclotomic fields

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-12-03 09:45:31

Assignee: robertwb

CC:  vripoll stumpc5 tscrim

This should work automagically:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = CyclotomicField(3).random_element()
sage: b = CyclotomicField(4).random_element()
sage: a + b
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
/home/ghitza/.sage/temp/artin/9098/_home_ghitza__sage_init_sage_0.py in <module>()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:6989)()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7021)()

TypeError: unsupported operand parent(s) for '+': 'Cyclotomic Field of order 3 and degree 2' and 'Cyclotomic Field of order 4 and degree 2'
sage: a * b
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ghitza/.sage/temp/artin/9098/_home_ghitza__sage_init_sage_0.py in <module>()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10248)()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7021)()

TypeError: unsupported operand parent(s) for '*': 'Cyclotomic Field of order 3 and degree 2' and 'Cyclotomic Field of order 4 and degree 2'
```


I think it's a coercion problem.  If someone knows better, please change the trac component accordingly.



---

Comment by vripoll created at 2014-04-11 00:06:12

Has anyone looked at this ticket? I ran into this today and discover that the issue has been reported 4 years ago... This bug is particularly confusing for the user, especially when you read the doc that says "Due to their default embedding into CC, cyclotomic number fields are all compatible", and goes on to show the following example:

```
      sage: cf30 = CyclotomicField(30)
      sage: cf5 = CyclotomicField(5)
      sage: cf3 = CyclotomicField(3)
      sage: cf30.gen() + cf5.gen() + cf3.gen()
      zeta30^6 + zeta30^5 + zeta30 - 1
```

It turns out Sage is able to compute that only because the first field contains the next two! Note the following test:

```
      ┌────────────────────────────────────────────────────────────────────┐
      │ Sage Version 6.2.beta7, Release Date: 2014-04-08                   │
      │ Type "notebook()" for the browser-based notebook interface.        │
      │ Type "help()" for help.                                            │
      └────────────────────────────────────────────────────────────────────┘
      sage: cf15=CyclotomicField(15)
      sage: cf5=CyclotomicField(5)
      sage: cf3=CyclotomicField(3)
      
      sage: cf15.gen()+cf5.gen()+cf3.gen()
      zeta15^5 + zeta15^3 + zeta15
      
      sage: cf5.gen()+cf3.gen()+cf15.gen()
      Traceback (most recent call last)
      ...
      TypeError: unsupported operand parent(s) for '+': 'Cyclotomic Field of order 5 and degree 4'   and 'Cyclotomic Field of order 3 and degree 2'
      
      sage: cf5.gen()+cf3.gen()
      Traceback (most recent call last)
      ...
      TypeError: unsupported operand parent(s) for '+': 'Cyclotomic Field of order 5 and degree 4' and 'Cyclotomic Field of order 3 and degree 2'
      
      sage: 0*cf15.gen()+cf5.gen()+cf3.gen()
      zeta15^5 + zeta15^3
```



---

Comment by vripoll created at 2014-04-11 00:07:09

Changing keywords from "" to "coercion, cyclotomic".


---

Comment by vdelecroix created at 2016-08-31 15:41:29

see also the somehow related #20746


---

Comment by chapoton created at 2018-04-30 16:55:19

Changing status from new to needs_review.


---

Comment by chapoton created at 2018-04-30 16:55:19

first tentative, let us see what patchbot says
----
New commits:


---

Comment by chapoton created at 2018-04-30 16:55:19

Changing keywords from "coercion, cyclotomic" to "coercion, cyclotomic, coxeter".


---

Comment by vdelecroix created at 2018-04-30 16:58:32

You should take care of embeddings. The map `add: CF(p) x CF(q) -> CF(lcm(p,q))` is not uniquely defined.


---

Comment by chapoton created at 2018-04-30 19:36:32

Well. What we just add here is the information that we need to go through CF(lcm). No responsability is taken on the existence of a canonical coercion from CF(p) to CF(lcm). I guess that this already an existing thing..


---

Comment by tscrim created at 2018-04-30 23:01:34

As Frederic said, this does not change the (canonical) coercions between cyclotomic fields but allows the analogous computation to

```
sage: R.<x,y> = ZZ[]
sage: S.<y> = QQ[]
sage: R.an_element() + S.an_element()
x + y
sage: _.parent()
Multivariate Polynomial Ring in x, y over Rational Field
```



---

Comment by tscrim created at 2018-04-30 23:01:34

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2018-05-08 17:27:45

Resolution: fixed
