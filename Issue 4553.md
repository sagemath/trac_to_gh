# Issue 4553: [with patch, needs review] a few new methods for FiniteFieldElement

Issue created by migration from https://trac.sagemath.org/ticket/4553

Original creator: jhpalmieri

Original creation time: 2008-11-19 18:05:02

Assignee: somebody

Keywords: finite field element

The attached patch adds a few methods for finite field elements.  It seems as though `.additive_order()` (and therefore `.order()`) was not implemented before (!), so I've implemented that.  I've also implemented pth powers and pth roots, where p is the characteristic of the field.

These are written pretty naively, so they may not be that fast. If anyone has suggestions for improvements, I'm happy to hear them (or to have you implement them).


---

Attachment


---

Comment by cremona created at 2008-11-22 17:33:44

That's funny -- in 3.2 I get

```
sage: a = GF(13^5,'a').gen()
sage: a.order()
13
```

where the function order() is implemented just as in your patch.  But additive_order is not implemented.

I definitely think that this functionality should go in.  But surely a.frobenius() should give `a^q` where q = a.parent().order() and not `a^p` where p = a.parent().characteristic()?  Secondly, you can use a.parent().degree(), there is no need to factor q to get the degree.

Lastly, I think it would be more efficient to compute (and cache) the matrix of frobenius as a linear map, viewing F_q as an F_p-vector space of dimension d where `q=p^d`.  I know an efficient way to do this (similar to tricks used in Berlekamp factorization).  Then taking q'th roots would be easy (invert the matrix).

I'm not sure when I'll have time to try doing this!


---

Comment by jhpalmieri created at 2008-11-24 03:25:07

Replying to [comment:2 cremona]:
> That's funny -- in 3.2 I get

```
sage: a = GF(13^5,'a').gen()
sage: a.order()
13
```

> where the function order() is implemented just as in your patch.  But additive_order is not implemented.

I'm not sure why I was thinking that order() wasn't implemented.  Anyway, in sage/structure/element.pyx, it says something like "don't override order, override additive_order instead" -- this is for instances of the class ModuleElement, from which FiniteFieldElement inherits.  So I'll produce a new patch that removes order() from finite_field_element.py and has  the definition of additive_order() in element.pyx.

>  I definitely think that this functionality should go in.  But surely
>  a.frobenius() should give `a^q` where q = a.parent().order() and not
>  `a^p` where p = a.parent().characteristic()?  

But then the Frobenius map would always be the identity! Also, for what it's worth, both wikipedia and mathworld describe the Frobenius as being the `p`th power map, not the `p^k`th power map.

>Secondly, you can use
>  a.parent().degree(), there is no need to factor q to get the degree.

Good point. I was looking for this sort of thing and hadn't found it. Thanks.

>  Lastly, I think it would be more efficient to compute (and cache) the
>  matrix of frobenius as a linear map, viewing F_q as an F_p-vector space of
>  dimension d where `q=p^d`.  I know an efficient way to do this
>  (similar to tricks used in Berlekamp factorization).  Then taking q'th
>  roots would be easy (invert the matrix).
>
>  I'm not sure when I'll have time to try doing this!

Is it worth accepting a patch without this efficiency change, and then adding this in later (as a separate ticket)?


---

Comment by jhpalmieri created at 2008-11-24 03:25:50

this replaces the other patch


---

Attachment

Sorry about my silly comment about q'th power against p'th power, I was not thinking.

The linear algebra approach will have to wait until we have a common interface for all finite fields -- currently the functions available depend on q since they differ according to whether we use givaro or NTL or pari.  (e.g. an element a in GF(q) sometimes has a._coordinates() but not always.  So it's fine to go ahead with this one for now, perhaps with a note that a better implementation might be possible in future.

I hope to review this properly, but Monday morning calls...


---

Comment by cremona created at 2008-11-25 12:52:12

The new patch looks good, applies cleanly to 3.2 and the doctests in both the changed files pass.

All tests in sage/structure and sage/rings pass.

I say: go for it!


---

Comment by mabshoff created at 2008-11-25 13:14:03

Hmm, should we deprecate "order" in sage/rings/finite_field_element.py ?

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-25 13:41:46

Resolution: fixed


---

Comment by mabshoff created at 2008-11-25 13:41:46

Merged finitefieldelement_new.patch in Sage 3.2.1.alpha1
