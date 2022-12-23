# Issue 4536: Various number field order and ideal utilities

Issue created by migration from https://trac.sagemath.org/ticket/4536

Original creator: cremona

Original creation time: 2008-11-16 20:47:31

Assignee: was

CC:  m.t.aranes@warwick.ac.uk dl267@cam.ac.uk

Keywords: number fields, orders, ideals

Additional methods for (fractional) ideals:

    1. Ideals cache their norms
    2. Integral ideals now have a residues() iterator
    3. numerator() and denominator() defined for fractional ideals
    4. is_coprime() defined for a fractional ideal & another (or a field element)
    5. euler_phi() defined for integral ideals

Additional method for orders:

    1. coordinates(x) for x in the field gives a vector of rationals expressing x as a linear combination of the order's Z-basis.
    


---

Comment by cremona created at 2008-11-16 20:48:33

Based on 3.2.rc1


---

Attachment

Hi John,

Just one quick comment. Is there a reason you are manually doing the caching instead of using the cached_method decorator in sage/misc/cachefunc.py?  I think the result is a bit cleaner.

Also, you don't need to use backslashes to continue lines if it occurs with in parens or brackets because Python knows that they need to be closed.

--Mike


---

Comment by cremona created at 2008-11-17 09:43:02

Replying to [comment:1 mhansen]:
> Hi John,
> 
> Just one quick comment. Is there a reason you are manually doing the caching instead of using the cached_method decorator in sage/misc/cachefunc.py?  I think the result is a bit cleaner.

Quick answer: it never occurred to me to do it any other way!  But isn't it completely standard in Sage that when an object has a property (such as the norm for an ideal) then one computes it the first time and caches it so that further requests for the property used the cached value?  This is surely different from caching values of a function.

> 
> Also, you don't need to use backslashes to continue lines if it occurs with in parens or brackets because Python knows that they need to be closed.

OK -- I'll remember that for next time (and if I get to revising this patch I'll remove them).

Thanks

> 
> --Mike


---

Comment by mhansen created at 2008-11-17 11:08:33

Replying to [comment:2 cremona]:
> Quick answer: it never occurred to me to do it any other way!  But isn't it completely standard in Sage that when an object has a property (such as the norm for an ideal) then one computes it the first time and caches it so that further requests for the property used the cached value?  This is surely different from caching values of a function.

The cached_method decorator is relatively new which is why it isn't in use throughout Sage.  For an example, see the groebner_basis method in sage/rings/polynomial/multi_polynomial_ideal.py

That's exactly what the cached_method decorator does except that it also handles the case where arguments are passed into the method.  The values are cached in a dictionary attribute on the object itself so it gets garbage collected correctly.  It also supports things such as clearing the cache, etc.


---

Comment by cremona created at 2008-11-17 12:28:33

Replying to [comment:3 mhansen]:
> Replying to [comment:2 cremona]:
> > Quick answer: it never occurred to me to do it any other way!  But isn't it completely standard in Sage that when an object has a property (such as the norm for an ideal) then one computes it the first time and caches it so that further requests for the property used the cached value?  This is surely different from caching values of a function.
> 
> The cached_method decorator is relatively new which is why it isn't in use throughout Sage.  For an example, see the groebner_basis method in sage/rings/polynomial/multi_polynomial_ideal.py
> 
> That's exactly what the cached_method decorator does except that it also handles the case where arguments are passed into the method.  The values are cached in a dictionary attribute on the object itself so it gets garbage collected correctly.  It also supports things such as clearing the cache, etc.

That looks brilliant, and had completely passed me by.  I'll start using it right away!  It would also be a good idea to start to systematically use it all over (wouldn't it) -- then people would see it and use it themselves.


---

Attachment

The second patch trac-4536-2.patch fixes a bug in the first implementation of residues(): I forgot to take the Smith Normal Form of the matrix.  The first of the two new doctests is an example which failed with the old version.


---

Comment by davidloeffler created at 2008-11-25 06:45:47

Patches install and compile fine under 3.2, and all doctests in sage/rings/number_field pass.

But I'm not happy with the is_coprime() method for fractional ideals. I thought the outcome of the discussion on the sage-nt list was that coprime for fractional ideals means disjoint supports, but I got this:


```
sage: E.<a> = NumberField(x^5 + 7*x^4 + 18*x^2 + x - 3)
sage: OE = E.ring_of_integers()
sage: i,j,k = [u[0] for u in factor(3*OE)] # three distinct prime ideals of degrees 3,1,1
sage: (i/j).is_coprime(j/k)
True
sage: (j/k).is_coprime(j/k)
True
```


The problem here is that the fractional ideal j/k has norm 1, and the code falsely assumes that if norm(i) and norm(j) are coprime, then i and j must be coprime. Thus the code will say that j/k is coprime to everything (including itself).


---

Comment by cremona created at 2008-11-25 09:26:11

David, you are quite right.  We could just delete that coprimality of norms pre-test except when the ideals are integral.  I'll correct it and put up a new patch.

Thanks for spotting this mistake!


---

Attachment


---

Comment by cremona created at 2008-11-25 11:47:34

The new patch trac-4536-fix.patch address the reviewer's just criticism, and adds a relevant doctest.


---

Comment by davidloeffler created at 2008-11-26 08:11:54

I've found no other problems, and the third patch certainly fixes the issue I reported, so I'll happily give this a positive review.


---

Comment by mabshoff created at 2008-11-26 10:30:08

Merged all three patches in Sage 3.2.1.alpha1


---

Comment by mabshoff created at 2008-11-26 10:30:08

Resolution: fixed
