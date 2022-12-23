# Issue 4193: Coercion between relative and absolute number fields

Issue created by migration from https://trac.sagemath.org/ticket/4193

Original creator: davidloeffler

Original creation time: 2008-09-25 10:15:29

Assignee: was

CC:  fwclarke

Is there supposed to be a canonical coercion map between a relative number field and its associated absolute field?

At the moment (in 3.1.2) there apparently isn't, and trying to force one raises a TypeError:

```
sage: K1.<a> = NumberField(x^3 - 2)
sage: R.<y> = PolynomialRing(K1).gen()
sage: K2.<b> = K1.extension(y^2 - a)
sage: K2abs = K2.absolute_field('w')
sage: K2abs(b)
TypeError: Cannot coerce element into this number field
```


I suppose it's sort of fair enough as there exist multiple K1-linear embeddings from K2 into K2abs, but shouldn't the definition of K2abs give a distinguished element of this set, sending the generator b of K2 to the generator w of K2abs?

This causes problems elsewhere, as the code for relative orders in number fields relies on having such a coercion to do basic element-creation and membership-testing routines, and these are all broken as a result:

```
sage: R = K2.order(b)
sage: b in R
False
sage: bb = R.gens()[1] # b by any other name
sage: bb == b
True
sage: bb.parent() is R
True
sage: bb in R
False
sage: R(bb) # trying to coerce something into its own parent!
TypeError: Cannot coerce element into this number field
```


I uncovered this last problem first while trying to fix #4190, or more precisely while trying to write a doctest for a fix that I'd already written. (I have a fix which works for absolute orders and should work for relative orders too, but there's no way it can work given the above general brokenness.)

David


---

Comment by davidloeffler created at 2009-03-17 10:06:13

I'm pleased to report that this seems to be fixed by fwclarke's patch for #5508. There isn't  automatic coercion between relative + absolute fields but it's debatable whether there should be; the more severe issue was the problems with orders assuming that there was in their coercion code, which is now fixed. Well done that man.


---

Comment by mabshoff created at 2009-03-25 08:54:58

To close this we would need a doctest.

Cheers,

Michael


---

Comment by davidloeffler created at 2009-03-27 10:39:14

I have added a doctest that checks this is corrected to my latest patch at #5159. This also includes another patch to catch a doctest failure arising from #5508 on 32-bit machines.


---

Comment by davidloeffler created at 2009-04-24 08:39:03

Michael: can we close this ticket now, as with 5508 and 5159 merged, the code contains both a fix and a doctest to prove the fix works?

Regards,

David


---

Comment by mabshoff created at 2009-04-24 08:44:29

Fixed in Sage 3.4.2.alpha0 by #5508.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 08:44:29

Resolution: fixed
