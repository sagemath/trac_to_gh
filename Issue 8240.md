# Issue 8240: cannot coerce p-adic field into residue field

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2010-02-11 19:51:59

Assignee: roed

CC:  roed robertwb saraedum caruso kedlaya


```
sage: K.<a> = Qq(25)
sage: F = K.residue_field()
sage: F(a)
Traceback (click to the left of this block for traceback)
...
TypeError: unable to coerce
```


Perhaps this is a "feature request", but it seems like a pretty basic feature...

(It works fine for prime fields)



---

Attachment

padic base coercion


---

Attachment

coercion for extensions, part 1


---

Attachment

coercion for extensions, part 2


---

Comment by roed created at 2012-02-21 12:51:16

I've updated the dependencies.  If you care about this ticket, review them!

Note that the 8240.patch is a duplicate of #12077 and should be removed.  8240_ext1.patch and 8240_ext2.patch are in progress: I basically didn't finish writing them.  Feel free to add to these patches in the same vein as #12077.


---

Comment by git created at 2017-07-23 09:10:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by roed created at 2017-07-23 09:11:25

Last 10 new commits:


---

Comment by roed created at 2017-07-23 09:17:41


```
sage -t --warn-long 53.3 src/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py  # 27 doctests failed
sage -t --warn-long 53.3 src/sage/modular/btquotients/pautomorphicform.py  # 24 doctests failed
sage -t --warn-long 53.3 src/sage/schemes/elliptic_curves/padics.py  # 1 doctest failed
sage -t --warn-long 53.3 src/sage/modular/btquotients/btquotient.py  # 4 doctests failed
sage -t --warn-long 53.3 src/sage/schemes/hyperelliptic_curves/monsky_washnitzer.py  # 4 doctests failed
```



---

Comment by git created at 2017-08-03 22:14:20

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by roed created at 2017-08-04 07:21:44

So, there are a number of failures coming from following change

```
sage: R = Zp(5); S = Zmod(5^5)
sage: a = R(1, 3); a
1 + O(5^3)
sage: S(a)
Traceback (most recent call last):
...
PrecisionError: Not enough precision to determine reduction.
```

Previously, Sage performed this reduction without complaint.  Some questions:
* Do we want a coercion from `R` to `S`?  Mathematically, this coercion is very similar to the one from `ZZ` to `Zmod(N)`, so I think the answer is yes.
* If there is a coercion, what should its behavior be on elements without enough precision, as in the example above?  A `PrecisionError` seems reasonable, but normally coercions don't raise errors....
* The coercion model demands that if there is a coercion between two parents, then that morphism should be used as the conversion as well (this is implemented in `discover_convert_map`, which calls `_internal_coerce_map_from` as the first step).  So we can't have different behavior for the coercion and the conversion from `R` to `S`.
* It's pretty annoying to have these kind of `PrecisionError`s in conversions.  For example, conversions are used in `change_ring` on polynomials, and there are plenty of examples in the Sage library where `change_ring` that trigger this kind of `PrecisionError`.

Any suggestions?


---

Comment by robharron created at 2017-08-04 07:54:10

I just checked the following:

```
sage: R1 = RealIntervalField(10)
sage: C1 = ComplexIntervalField(10)
sage: C1.coerce_map_from(R1)

Call morphism:
  From: Real Interval Field with 10 bits of precision
  To:   Complex Interval Field with 10 bits of precision
sage: C1 = ComplexIntervalField(11)
sage: C1.coerce_map_from(R1)
sage: C1.convert_map_from(R1)

Call morphism:
  From: Real Interval Field with 10 bits of precision
  To:   Complex Interval Field with 11 bits of precision
```

So, there's a precedent in the archimedean code to only have a convert map, not a coerce map, when mapping from a lower precision to a higher precision. For Zp(5) to Zmod(5<sup>5</sup>), you're mapping an inexact ring to an exact ring, so this would suggest that there should be no coercion, only a conversion.


---

Comment by roed created at 2017-08-05 02:37:48

Yeah, just having a conversion seems like the simplest solution.  I think it may be reasonable to have a coercion to the residue field though?


---

Comment by robharron created at 2017-08-05 02:43:47

Replying to [comment:10 roed]:
> Yeah, just having a conversion seems like the simplest solution.  I think it may be reasonable to have a coercion to the residue field though?

Yeah, I think coercion to the residue field makes sense, though a PrecisionError will still need to be raised for O(5<sup>0</sup>); I think that's reasonable since O(5<sup>0</sup>) basically means you have no idea what element of Zp you have!


---

Comment by git created at 2017-08-05 07:31:28

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by roed created at 2017-08-05 07:42:45

Changing status from new to needs_review.


---

Comment by caruso created at 2017-08-05 12:30:00

IMO, It's a kinda weird to promote reduction modulo p to a coercion map but not reduction modulo p^n.


---

Comment by roed created at 2017-08-06 05:46:42

Replying to [comment:14 caruso]:
> IMO, It's a kinda weird to promote reduction modulo p to a coercion map but not reduction modulo p^n.

I agree that it's kind of weird.  I'd really like for them both to be coercions, but I explain above why that doesn't seem to be possible.

I think it's probably okay to also delete the coercion to the residue field.  For integers, you really want to be able to ask for `a+1` if `a` is an element of `Zmod(N)`, but I think that this is a lot less important for p-adics.

If nobody else has input, I can go ahead and make this change.


---

Comment by roed created at 2017-08-06 05:49:19

Replying to [comment:14 caruso]:
> IMO, It's a kinda weird to promote reduction modulo p to a coercion map but not reduction modulo p^n.

I agree that it's kind of weird.  I'd really like for them both to be coercions, but I explain above why that doesn't seem to be possible.

I think it's probably okay to also delete the coercion to the residue field.  For integers, you really want to be able to ask for `a+1` if `a` is an element of `Zmod(N)`, but I think that this is a lot less important for p-adics.


---

Comment by jpflori created at 2017-08-21 16:44:57

Can we try to live with a conversion? if that raise problems we cna try to make all maps coercions.
But as David said, there is a precendent with other constructions in sagE.


---

Comment by git created at 2017-09-20 17:12:51

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-09-20 18:52:33

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:


---

Comment by git created at 2017-09-20 20:31:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-09-20 20:36:11

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-09-20 20:48:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-09-20 21:57:43

Branch pushed to git repo; I updated commit sha1. New commits:


---

Attachment

Diff against #14825 for ease of review


---

Comment by git created at 2017-09-22 19:40:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by roed created at 2017-09-23 18:32:40

I'm getting an error from the docbuild plugin:

```
OSError: [padics   ] ...docstring of sage.rings.padics.padic_generic.pAdicGeneric.residue_ring:1: WARNING: Inline interpreted text or phrase reference start-string without end-string.
```

The relevant docstring is

```
    """
    Return the quotient of the ring of integers by the nth power of its maximal ideal.

    EXAMPLES::

        sage: S.<x> = ZZ[]
 	sage: W.<w> = Zp(5).extension(x^2 - 5)
 	sage: W.residue_ring(1)
 	Ring of integers modulo 5

    The following requires implementing more general Artinian rings::

 	sage: W.residue_ring(2)
 	Traceback (most recent call last):
 	...
 	NotImplementedError
    """
```


Any ideas what might be going on?


---

Comment by chapoton created at 2017-09-23 18:40:22

in
`Returns the quotient of the ring of integers by the `n`th power of the maximal ideal.`
add a space after ``n``


---

Comment by chapoton created at 2017-09-23 18:44:01

in

```
richcmp((type(self), self.domain(), self.codomain()), (type(other), other.domain(), other.codomain()), op)
```

you compare types, which is not allowed in python3.

**EDIT**
Instead you can do something like

```
if type(self) != type(other):
    return NotImplemented
return richcmp(...)
```



---

Comment by git created at 2017-09-23 19:08:15

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by roed created at 2017-09-24 02:33:56

Thanks; I've fixed the richcmp error you pointed out.


---

Comment by git created at 2017-09-24 02:45:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-09-25 06:50:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by roed created at 2017-09-25 19:29:04

Tests pass.


---

Comment by kedlaya created at 2017-09-26 02:26:07

I confess to not having inspected all of this code line-by-line. But I did go through the main blocks, and I tried a few tests of my own without finding any issues. Positive review.


---

Comment by kedlaya created at 2017-09-26 02:26:45

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-10-09 20:04:11

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2017-10-09 20:04:11

Merge conflict


---

Comment by saraedum created at 2017-10-13 05:54:10

No conflicts for me.
----
New commits:


---

Comment by saraedum created at 2017-10-13 05:54:10

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2017-10-15 15:29:17

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2017-10-15 15:29:17

wait for next beta


---

Comment by roed created at 2017-10-18 20:16:04

Changing status from needs_work to positive_review.


---

Comment by roed created at 2017-10-18 20:16:04

Fixed the merge conflict and ran all tests.
----
New commits:


---

Comment by vbraun created at 2017-10-20 09:15:34

Resolution: fixed
