# Issue 9818: Add a default gcd and lcm methods for fields

Issue created by migration from https://trac.sagemath.org/ticket/9819

Original creator: lftabera

Original creation time: 2010-08-27 10:55:25

Assignee: AlexGhitza

Keywords: lcm, gcd, fields

For the case of field elements gcd and lcm methods are not of great interest. However, they can be addecuated for some reasons.

- Some algorithms may accept as input either polynomials or rational functions. In these algorithms we may reduce a list of polynomials and rational functions to a common denominator. If all the inputs are polynomials, the denominators are the one element of the base field. In this case, lcm would fail.

See #9063 for a case of this problem.

- Rational numbers already have custom gcd and lcm methods.

-It would erase the following problem. Currently, if we are dealing with elements in a finite field, the gcd of the elements can be computed sometimes coercing to the integers and doing computations. This lead to inconsistencies.


```
sage: a=F(2)
sage: gcd(a,a)
2
sage: gcd(a,p)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/luisfe/Varios/Comprobantes-gastos/<ipython console> in <module>()

/opt/SAGE/sage-4.5.2/local/lib/python2.6/site-packages/sage/rings/arith.pyc in gcd(a, b, **kwargs)
   1423                 return ZZ(a).gcd(ZZ(b))
   1424             except TypeError:
-> 1425                 raise TypeError, "unable to find gcd of %s and %s"%(a,b)
   1426     
   1427     from sage.structure.sequence import Sequence

TypeError: unable to find gcd of 2 and p
```


I propose the following:

- For gcd, follow the convention of the rational cesa. If both elements are 0, return 0 (on the appropriate field). Otherwise return 1

- For lcm, if one of the elements is zero, return zero. Otherwise return 1.

#9063 depends on this bug to be merged.


---

Comment by lftabera created at 2010-09-01 14:27:11

To make thing worse, currently (sage 4.5.3.alpha2) GF(5)(4) is an IntegerMod_int that does not derive from FieldElement but CommutativeRingElement


---

Comment by mstreng created at 2011-02-14 14:59:04

related ticket with different proposal: #10771


---

Comment by SimonKing created at 2011-02-14 15:31:17

Replying to [comment:3 mstreng]:
> related ticket with different proposal: #10771

I wouldn't say that it is a different proposal. #10771 treats the case of fields that happen to be the fraction field of a unique factorization domain. In this case, one can do better than to return either 0 or 1.

However, #10771 does not consider the case of fields that are no fraction fields, or are fraction fields of rings that do not provide lcm and gcd. I suggest that for that purpose, one should implement gcd and lcd as element methods of the category of `Fields()`. That would also solve the problem that `IntegerMod_int` does not derive from `FieldElement`.


---

Comment by mstreng created at 2012-01-12 12:05:07

Is everything on this ticket fixed already? It seems that #10771 did implement `Fields.ElementMethods.gcd()` after all and its behaviour is as requested in this ticket.


---

Comment by mstreng created at 2012-01-12 12:05:16

Changing status from new to needs_info.


---

Comment by lftabera created at 2012-01-12 17:32:36

Yes, this ticket should be resolved as duplicated.


---

Comment by lftabera created at 2012-01-12 17:32:36

Changing status from needs_info to needs_review.


---

Comment by mstreng created at 2012-01-16 15:00:29

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-31 09:39:34

Resolution: duplicate
