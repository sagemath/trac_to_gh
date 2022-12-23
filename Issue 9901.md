# Issue 9901: base_extend() not implemented in MPolynomialRing

Issue created by migration from https://trac.sagemath.org/ticket/9902

Original creator: vbraun

Original creation time: 2010-09-12 11:15:06

Assignee: malb

CC:  novoselt niles

The base `class Ring` defines `base_extend()`, but the implementation needs to be overridden in the derived class `MPolynomialRing`:

```
sage: sage: P.<x,y,z> = PolynomialRing(QQ,'x, y, z'); P
Multivariate Polynomial Ring in x, y, z over Rational Field
sage: P.base_extend(CC)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/vbraun/opt/sage-4.5.3/devel/sage-main/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.base_extend (sage/rings/ring.c:3190)()

TypeError: no base extension defined
```

The patch implements the override and adds documentation.


---

Attachment

Initial patch


---

Comment by vbraun created at 2010-09-17 14:05:39

Changing status from new to needs_review.


---

Comment by vbraun created at 2010-12-20 19:16:27

Andrey, I wrote this patch a while a go to be able to extend the base field of the toric coordinate ring. It might be useful...


---

Comment by novoselt created at 2010-12-20 19:53:16

Changing status from needs_review to needs_info.


---

Comment by novoselt created at 2010-12-20 19:53:16

I am not quite sure it is the right approach. It seems to me that we have two methods: `change_ring` that constructs "the same object but over different ring" and `base_extend` which does the same, but only if there is a natural coercion. Given this description, it seems to me that there should be only one implementation of `base_extend` in the base class:

```
def base_extend(self, R):
    if R.has_coerce_map(self.base_ring()):
        return self.change_ring(R)
    else:
        raise TypeError("%s cannot be extened to %s!" % (self.base_ring(), R))
```

and then each derived class should implement `change_ring` only. (If the detailed error message breaks a lot of doctests I am fine with keeping the current one.) Thoughts?

There is also discrepancy between actual argument names and their description in documentation (`base_ring` vs. `R`).
