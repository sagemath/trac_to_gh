# Issue 9429: Undesirable behaviour when deriving from QuotientRingElement

Issue created by migration from https://trac.sagemath.org/ticket/9429

Original creator: vbraun

Original creation time: 2010-07-05 10:44:05

Assignee: AlexGhitza

CC:  novoselt robertwb

All arithmetic operations on `QuotientRingElement` return a new `QuotientRingElement`, which is not the desired result for derived classes. Instead one should use `self.__class__` to return an instance of the actual type:

```
sage: from sage.rings.quotient_ring_element import QuotientRingElement
sage: class Q(QuotientRingElement):
...    pass
...
sage: P.<x,y> = PolynomialRing(QQ, 'x, y')
sage: Pquo = P.quo(x^3)
sage: q = Q(Pquo, x)
sage: type(q)
<class '__main__.Q'>
sage: type(q^2)
<class 'sage.rings.quotient_ring_element.QuotientRingElement'>
```


Expected behaviour: `q^2` should have the same (derived) type as `q`.

I am running into this issue because I want to express cohomology classes on toric varieties as derived classes of `QuotientRingElement`, see #9326. I'll write the obvious patch and attach it later today.


---

Attachment

missed one occurrence


---

Comment by vbraun created at 2010-07-05 12:06:02

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-07-05 13:38:44

I think

```
P = self.parent()
return P._element_constructor_(...)
```

is the way to go here according to http://wiki.sagemath.org/coercion (if it does not work, that this is a bug that should be fixed ;-))


---

Comment by novoselt created at 2010-07-06 15:56:07

Actually, I should have probably written

```
P = self.parent()
return P(...)
```

to eliminate the use of private methods completely.


---

Comment by novoselt created at 2010-07-06 16:02:23

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-07-06 16:02:23

I have added a couple of printing lines into the quotient ring and got the following:

```
sage: FF = FiniteField(7)
sage: P.<x> = PolynomialRing(FF)
_coerce_map_from_(Finite Field of size 7, <type 'int'>)
_coerce_map_from_(Finite Field of size 7, Integer Ring)
_element_constructor_(Finite Field of size 7, 0)
sage: x + 1
_element_constructor_(Finite Field of size 7, 1)
...
TypeError: unsupported operand parent(s) for '+':
'Univariate Polynomial Ring in x over Finite Field of size 7'
and 'Integer Ring'
sage: isinstance(FF, sage.rings.quotient_ring.QuotientRing_generic)
True
```



---

Attachment

Volker Braun's patch (with two print statements)


---

Comment by novoselt created at 2010-07-07 06:31:52

Hi Volker,

I think I need to clarify my position a bit. I think that the coercion system is great and we should try to use it and comply with it as much as possible, especially in new classes. However it is not yet implemented everywhere and "fixing" existing files sometimes leads to a lot of problems, which may have a simple solution, but it is not necessarily obvious. I have tried today to switch divisor groups to the new framework and discovered that all modules in Sage are still inherited from old-style parents and trying to change it gives tons of errors. So if you are up to determine the exact cause of the problems above and fix them - it would be great (looks like the issue here is with `int` type, which should be treated like `ZZ`), but at the same time I don't think it should be mandatory.

Meanwhile, I am attaching a version of your first patch with `return self.parent()(...)` statements. Naturally, `q^2` in your example will be of type `QuotientRingElement` since this is what the parent of `q` constructs as its elements. However, if you derive a class from `QuotientRing` which will construct its elements as some other type, these operations should return that other type. Please check if it actually works for your patches (I checked that at least it does not break anything so far). If it works, then perhaps we can add an example in the module docstring with derived classes for both ring and element and then mark it as ready for inclusion.

Thank you,
Andrey


---

Comment by novoselt created at 2010-07-07 06:32:35

`return self.parent()(...)` version


---

Attachment

I agree that your self.parent() version, of course. If we can't improve `QuotientRing` then we should go with the current version. I asked on sage-devel for help, maybe somebody can tell us more about the issue:

http://groups.google.com/group/sage-devel/browse_thread/thread/efe93107ce004d3b


---

Comment by vbraun created at 2010-07-15 17:11:38

The reason why `first_attempt.patch` breaks so many things is because the classes `QuotientRing_generic` -> `IntegerModRing_generic` -> `FiniteField_prime_modn` do not work within the new coercion model. 

Robert wrote on sage-devel:
> What should have happened is that QuotientRing should be an abstract class, and with subclasses QuotientRingGeneric and FiniteField/IntegerModRing/etc. as the latter end up 
 ignoring/subverting the implementation of the former. This would make things like this much easier to change

We should eventually port this to the new coercion model, but it seems to be a bigger effort. I don't want to wait with the current toric varieties code until this is done. So I'd like to go ahead with the "wrong" coercion in #9326, and leave this ticket for later.


---

Comment by novoselt created at 2010-07-15 17:22:00

What about merging only `trac_9429_fix_derived_classes.2.patch` for now? Forgetting coercion, it still would be nice if cohomology classes were represented by a new class rather than just an element of a quotient polynomial ring, since it will allow us to add methods to these classes.


---

Comment by vbraun created at 2010-07-15 17:30:58

I am right now moving your 'trac_9429_fix_derived_classes.patch' to #9326. Then you will hopefully review that ticket positively, allowing it to get merged :-)


---

Comment by vbraun created at 2010-07-15 17:32:45

I meant to write: I'm moving your `trac_9429_fix_derived_classes.2.patch`...


---

Comment by tscrim created at 2014-06-22 06:55:32

Changing keywords from "" to "sd59".


---

Comment by tscrim created at 2014-06-22 06:55:32

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2014-06-22 06:55:32

I've "reverted" back to using the `self.__class__(self.parent(), x)` since this (as I remember) is the "correct" way to do things as it does not go through the coercion model. So can someone double-check to make sure doctests pass?
----
New commits:


---

Comment by mmezzarobba created at 2015-02-05 10:30:31

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-02-17 19:28:25

Resolution: fixed
