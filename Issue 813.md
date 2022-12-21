# Issue 813: forced coercion vs. automatic coercion

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-10-03 18:52:27

Assignee: was

This should give similar results, but it is inconsistent:

```
P1.<x>=QQ[]
L=P1.fraction_field()
x=L(x)
P2.<y>=P1[]

f=x+y

P3.<x,y>=QQ[]

P3(f)

0*P3.0+f
```



---

Comment by nbruin created at 2007-10-03 20:58:07

Changing component from algebraic geometry to basic arithmetic.


---

Comment by nbruin created at 2007-10-03 20:58:07

Changing assignee from was to roed.


---

Comment by roed created at 2007-10-13 00:33:50

I will work on this once Robert has added rdef'd functions to Sage (that way I don't have to redo the changes once this occurs)


---

Comment by mhansen created at 2008-11-14 09:02:50

This now gives a TypeError when doing the last arithmetic:


```
TypeError: unsupported operand parent(s) for '+': 'Multivariate Polynomial Ring in x, y over Rational Field' and 'Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field'
```



---

Comment by SimonKing created at 2011-07-31 14:38:33

I accidentally came accross this stone age ticket.

For the record: Current behaviour as of sage-4.7.rc2 is

```
sage: P1.<x>=QQ[]
sage: L=P1.fraction_field()
sage: x=L(x)
sage: P2.<y>=P1[]
sage:
sage: f=x+y
sage:
sage: P3.<x,y>=QQ[]
sage:
sage: P3(f)
x + y
sage:
sage: 0*P3.0+f
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/<ipython console> in <module>()

/mnt/local/king/SAGE/sage-4.7.rc2/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11959)()

/mnt/local/king/SAGE/sage-4.7.rc2/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7382)()

TypeError: unsupported operand parent(s) for '+': 'Multivariate Polynomial Ring in x, y over Rational Field' and 'Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field'
sage: f.parent()
Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field
sage: P3
Multivariate Polynomial Ring in x, y over Rational Field
```


The question thus is: Should there be a coercion from P3 to the parent of f? Then one should implement it. Otherwise, the ticket should be closed as invalid.

Let fP be the parent of f, hence, the polynomial ring in y over the fraction field of the polynomial ring in x over the rationals.

There _is_ a coercion to fP from the polyomial ring in y over the polynomial ring in x over the rationals:

```
sage: from sage.structure.element import get_coercion_model
sage: cm = get_coercion_model()
sage: fP = f.parent()
sage: cm.explain(fP, QQ[x][y])
Coercion on right operand via
    Conversion map:
      From: Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
      To:   Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field
Arithmetic performed after coercions.
Result lives in Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field
Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field
```


However, there is no such coercion from the bivariate polynomial ring in x and y over the rationals:

```
sage: cm.explain(fP, QQ[x,y])
Will try _r_action and _l_action
Unknown result parent.
```


I think there should be such coercion! What do you think? I guess I'll also ask sage-devel.


---

Comment by SimonKing created at 2011-07-31 20:09:42

For the record: I did post on [sage-algebra](http://groups.google.com/group/sage-algebra/browse_thread/thread/7f884449de17bb31), not sage-devel.

There, I argued that there should be no coercion/pushout between `QQ[x][y]` and `QQ[y][x]`, even though there is a coercion between `QQ[x,y]` and `QQ[y,x]`. I wonder whether my argument is convincing, though.

However, even in that case, I could imagine that with a little more effort one could modify the algorithm behind `sage.categories.pushout.pushout` so that the pushout of `Frac(QQ['x'])['y']` and `QQ['x','y']` is `Frac(QQ['x'])['y']`. Do we want that behaviour of the pushout?


---

Comment by SimonKing created at 2011-08-02 13:23:19

Changing component from basic arithmetic to coercion.


---

Comment by SimonKing created at 2011-08-02 13:23:19

Meanwhile I believe that this is _not_ invalid. Namely, we have the following:

```
sage: from sage.categories.pushout import pushout
sage: pushout(QQ['x','y'],Frac(QQ['x'])['y'])
Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field
```


Hence, arithmetic between `QQ['x','y']` and `Frac(QQ['x'])['y']` should work! But it doesn't:

```
sage: QQ['x','y'](1) + Frac(QQ['x'])['y'](1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/Projekte/MeatAxe/meataxe-2.2.4/<ipython console> in <module>()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11997)()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7382)()

TypeError: unsupported operand parent(s) for '+': 'Multivariate Polynomial Ring in x, y over Rational Field' and 'Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field'
```


What is the problem? The conversion is fine:

```
sage: Frac(QQ['x'])['y'](QQ['x','y'](1))
1
```


But in fact there is no coercion into the pushout:

```
sage: pushout(QQ['x','y'],Frac(QQ['x'])['y']).has_coerce_map_from(QQ['x','y'])
False
```


That's a bug, I think.


---

Comment by SimonKing created at 2011-08-02 13:25:16

PS: In addition, since there is a coercion from `QQ['y','x']` to `QQ['x','y']`, it is conceivable that the pushout of `QQ['y','x']` with `Frac(QQ['x'])['y']` should be `Frac(QQ['x'])['y']` as well. But it isn't:

```
sage: pushout(QQ['y','x'],Frac(QQ['x'])['y'])
---------------------------------------------------------------------------
CoercionException                         Traceback (most recent call last)

/home/king/Projekte/MeatAxe/meataxe-2.2.4/<ipython console> in <module>()

/mnt/local/king/SAGE/sage-4.7.1.rc1/local/lib/python2.6/site-packages/sage/categories/pushout.pyc in pushout(R, S)
   3072                     if Rc[-1] in Sc:
   3073                         if Sc[-1] in Rc:
-> 3074                             raise CoercionException, ("Ambiguous Base Extension", R, S)
   3075                         else:
   3076                             all = Sc.pop() * all

CoercionException: ('Ambiguous Base Extension', Multivariate Polynomial Ring in y, x over Rational Field, Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field)
```



---

Comment by SimonKing created at 2011-08-02 14:24:54

Here is my plan for implementing a coercion of `P = QQ['x','y']` into `Q = Frac(QQ['x'])['y']`.

Since conversion of P into Q works, we only need to make `Q._coerce_map_from_(P)` return True.

Let p be an element of P. When converting p into Q, the multivariate polynomial p is transformed into a univeriate polynomial via p. This is done using `p._polynomial_(Q)`, which ultimately boils down to `Q(p.polynomial(P('y')))`:

```
sage: P = QQ['x','y']
sage: p = P.gen(0)
sage: Q = Frac(QQ['x'])['y']
sage: Q(p.polynomial(P('y')))
x
```


`p.polynomial(P('y')).parent()` lives in a stacked polynomial ring:

```
sage: p.polynomial(P('y')).parent()
Univariate Polynomial Ring in y over Univariate Polynomial Ring in x over Rational Field
```

That stacked ring coerces into Q:

```
sage: Q.has_coerce_map_from(p.polynomial(P('y')).parent())
True
```


Conclusion: If we want to test whether a multivariate polynomial ring P coerces into a univariate polynomial ring Q in variable y, then we need to try and transform P into a _univariate_ polynomial ring P' in variable y; here, we have `P'=QQ['x']['y']`. There is a coercion from P into Q if and only if there is a coercion from P' into Q.

I already have a patch, but "surprisingly" the additional coercion yields some doctest errors in other places.


---

Comment by SimonKing created at 2011-08-02 15:38:56

The problem with my approach is that it would create a bidirectional coercion, namely a coercion from `QQ['x','y']` to `QQ['x']['y']` in addition to the coercion from `QQ['x']['y']` to `QQ['x','y']` that already exists.

But I think I have an idea that would solve the problem.

My original idea was to have a coercion from P to Q if there is a coercion from `P.remove_var(Q.variable_name())` to `Q.base_ring()`. That created the bidirectional coercion.

My modified idea is to have the coercion from P to Q _only_ if `P.remove_var(Q.variable_name())` is different from `Q.base_ring()`, but coerces into it. Hence, a coercion only takes place if the rings become more complicated, thus avoiding circles.

The tests in sage/rings/polynomial pass. I am now running all doc tests, and then I can hopefully submit my patch...


---

Comment by SimonKing created at 2011-08-02 17:04:00

Coercion from multivariate to univariate polynomial rings


---

Comment by SimonKing created at 2011-08-02 17:11:41

Changing status from new to needs_review.


---

Attachment

I think I was able to solve the problem. With my patch applied on top of sage-4.7.1.rc1, all tests seem to pass, and one can do

```
            sage: P = QQ['x','y']
            sage: Q = Frac(QQ['x'])['y']
            sage: Q.has_coerce_map_from(P)
            True
            sage: P.0+Q.0
            y + x
```


In order to avoid bidirectional coercions (that would break a lot of tests), I have

```
            sage: Q = QQ['x']['y']
            sage: Q.has_coerce_map_from(P)
            False
            sage: Q.base_ring() is P.remove_var(Q.variable_name())
            True
```


The rule is: If `Q.base_ring() is P.remove_var(Q.variable_name())` then there can not be a coercion from the multivariate ring P to the univariate ring Q; in fact, there is a coercion in the opposite direction. But otherwise, there is a coercion if `Q.base_ring()` has a coercion from `P.remove_var(Q.variable_name())`.


---

Comment by SimonKing created at 2011-08-30 10:28:13

Any reviewer for a time-honoured ticket?


---

Comment by saraedum created at 2011-09-21 10:59:59

Looking at your patch, was `def univariate_ring(self, x):` added by purpose? Apart from that it seems to be a perfectly good solution as long as we can not have cyclic coercions.


---

Comment by saraedum created at 2011-09-21 12:17:26

btw., doctests pass when applied to 4.7.2.alpha2.


---

Comment by saraedum created at 2011-09-21 12:17:44

Changing status from needs_review to needs_info.


---

Comment by SimonKing created at 2011-09-21 13:00:44

Changing status from needs_info to needs_review.


---

Comment by SimonKing created at 2011-09-21 13:00:44

Replying to [comment:14 saraedum]:
> Looking at your patch, was `def univariate_ring(self, x):` added by purpose? 

Good question. I think it was meant as analogy to the method `univariate_polynomial` of multivariate polynomials. But really, it seems unneeded to have that method. Could probably be dropped, if you prefer (needs to be tested, though).


---

Comment by saraedum created at 2011-09-21 13:29:28

Ok. In this case it makes sense to have this method. I made some minor changes to the docstrings.

Sorry, I created an extra attachment. Apply trac813_univariate_coerce_from_multivariate.patch, trac_813_review.2.patch.


---

Comment by saraedum created at 2011-09-21 13:29:28

Changing status from needs_review to positive_review.


---

Comment by saraedum created at 2011-09-21 13:30:39

Apply trac813_univariate_coerce_from_multivariate.patch, trac_813_review.2.patch.


---

Comment by saraedum created at 2011-09-21 13:34:15

Apply trac813_univariate_coerce_from_multivariate.patch, trac_813_review.patch

Sorry, struggling with the patchbot.


---

Comment by leif created at 2011-09-23 10:26:04

Changing status from positive_review to needs_info.


---

Comment by leif created at 2011-09-23 10:26:04

Replying to [ticket:813 nbruin]:
> Apply 

> 

>  1. [attachment:trac813_univariate_coerce_from_multivariate.patch] 

>  1. [attachment:trac_813_review.2.patch] 

> 

> to the sage repository.

? The attachment comment of the second file says _"ignore this file"_, and the "patch" is only 17 bytes in total...

So I guess the description should be updated, to apply the [attachment:trac_813_review.patch "old" reviewer patch].


---

Comment by saraedum created at 2011-09-23 10:48:35

sure. sorry, only updated the patchbot instructions but not the ticket description.


---

Comment by saraedum created at 2011-09-23 10:48:35

Changing status from needs_info to needs_review.


---

Comment by saraedum created at 2011-09-23 10:48:43

Changing status from needs_review to positive_review.


---

Comment by leif created at 2011-09-23 11:04:30

Ok, I've deleted the 17 bytes...


---

Comment by leif created at 2011-09-27 17:42:14

Resolution: fixed


---

Attachment

small changes to docstrings
