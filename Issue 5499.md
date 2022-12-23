# Issue 5499: Wrong precision when creating p-adic field element

Issue created by migration from https://trac.sagemath.org/ticket/5499

Original creator: kedlaya

Original creation time: 2009-03-12 05:18:12

Assignee: was

This was originally reported on ticket #5076 but seems to be a separate issue.

```
sage: K = Qp(11,8)
sage: a = 11^-2 + O(11^5)
sage: a
11^-2 + O(11^3)
```

By contrast:

```
sage: K = Qp(11,8)
sage: 11^(-2) + K(O(11^5))
11^-2 + O(11^5)
```

Note that

```
sage: O(11^5).parent()
11-adic Ring with capped relative precision 5
sage: O(11^5).parent() == K
False
```




---

Attachment


---

Comment by robertwb created at 2009-03-18 05:01:52

The explanation looks good, I'm not sure how one would get around this without doing something lazily. Also, +1 to only allowing `O(x^n)` not `O((x+1)^n)`

However, what's up with the change of comparison direction in the last three files of the patch? Is this fixing an separate bug?


---

Comment by mabshoff created at 2009-03-25 06:58:00

David: Any chance you could answer Robert's question since this patch is holding up the merge of #4637?

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 07:15:43

This patch causes many doctest failures:

```
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 1 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py # 1 doctests failed
	sage -t -long devel/sage/doc/fr/tutorial/tour_polynomial.rst # 1 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/formal_group.py # 8 doctests failed
	sage -t -long devel/sage/doc/en/tutorial/tour_polynomial.rst # 1 doctests failed
	sage -t -long devel/sage/sage/rings/laurent_series_ring_element.pyx # 48 doctests failed
	sage -t -long devel/sage/sage/rings/laurent_series_ring.py # 3 doctests failed
	sage -t -long devel/sage/sage/rings/big_oh.py # 2 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # Segfault
```

The last seems to get very slow, i.e. only the last step in the following computation

```
Trying:
    E = EllipticCurve('37a')###line 585:_sage_    >>> E = EllipticCurve('37a')
Expecting nothing
ok
Trying:
    E.is_supersingular(Integer(3))###line 586:_sage_    >>> E.is_supersingular(3)
Expecting:
    True
ok
Trying:
    h = E.padic_height(Integer(3), Integer(5))###line 588:_sage_    >>> h = E.padic_height(3, 5)
Expecting nothing
ok
Trying:
    h(E.gens()[Integer(0)])###line 589:_sage_    >>> h(E.gens()[0])
Expecting:
    (2*3 + 2*3^2 + 3^3 + 2*3^4 + 2*3^5 + O(3^6), 3^2 + 3^3 + 3^4 + 3^5 + O(3^7))
```

takes more than 3 minutes CPU time on sage.math.

Cheers,

Michael


---

Comment by kedlaya created at 2009-04-12 12:59:47

I was originally unsure whether this was simply because those doctests depended on the old behavior. But in fact there is a real problem with the patch, as I extracted from the second file on Michael's list.

```
sage: E=EllipticCurve('389a1')
sage: X,Y=E.modular_parametrization()
sage: q = X.parent().gen()
sage: E.defining_polynomial()(X,Y,1)
869*q^11 + 2151*q^12 - 2768*q^13 + O(q^14)
sage: E.defining_polynomial()(X,Y,1) + O(q^11)
870*q^11 + 2151*q^12 - 2768*q^13 + O(q^14)
```



---

Comment by kedlaya created at 2009-04-12 14:06:20

To clarify my previous comment: before the patch, we have correctly:

```
sage: R.<q> = LaurentSeriesRing(Rationals())
sage: O(q^14)
O(q^14)
```

but afterwards we have:

```
sage: R.<q> = LaurentSeriesRing(Rationals())
sage: O(q^14)
q^14
```



---

Comment by roed created at 2009-04-12 16:47:19

I fixed the problem with the laurent series ring, which was also causing the doctest failures.

The change in direction of the coercion maps is one that I discussed with Kiran at AWS.  I think it's a good idea, though it is a somewhat different issue.


---

Comment by roed created at 2009-04-12 16:49:35

Fixes laurents series, as well as p-adic l-series code affected by change in direction of coercion


---

Attachment

Cool, trac_5499_2.patch only passes doctests for my 3.4.1.rc3 merge tree.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 08:47:29

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 08:47:29

Merged trac_5499_2.patch in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by robertwb created at 2009-04-14 02:15:02

Regarding "change in direction of the coercion maps", this should at least be accompanied by some doctests to illistrate what's going on...


---

Comment by mabshoff created at 2009-04-15 03:26:22

This is the patch I imported which gives credit to David
