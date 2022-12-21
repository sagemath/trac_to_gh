# Issue 5856: elliptic curves over Z/pZ are treated totally differently than elliptic curves over GF(p)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-22 15:47:38

Assignee: was

CC:  cremona

We have

```
sage: type(EllipticCurve(Zmod(11), [1,2]))
<class 'sage.schemes.elliptic_curves.ell_generic.EllipticCurve_generic'>
sage: type(EllipticCurve(GF(11), [1,2]))
<class 'sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field'>
```


This means that if you make a curve over Z/pZ then basically nothing works, but if you make the same curve over GF(p), there is tons of functionality.


---

Comment by AlexGhitza created at 2009-04-29 08:39:51

I see two options:

 1. Change the `EllipticCurve` constructor so that if it is given `Zmod(p)` for a prime number `p`, it actually returns the corresponding elliptic curve over `GF(p)`.  This would probably only take a couple of minutes to do.  However, this means that creating a curve over `Zmod(5)` would return a different type than creating a curve over `Zmod(4)`.

 2. We keep creating the curve over `Zmod(p)` as before but we attach to it the corresponding curve over `GF(p)` (cached).  We put in the headers of all the methods from `GF(p)` and have them call the corresponding methods from `GF(p)` to do all the work.  This is a somewhat ugly.

Right now I like the first option better than the second.  But maybe there are better ideas out there, or convincing arguments in favour of one thing or the other.


---

Comment by cremona created at 2009-04-29 08:45:58

I vote with Alex for 1.  This is in fact similar to the following:


```
Loading Sage library. Current Mercurial branch is: test2
sage: E = EllipticCurve(ZZ, [1,2,3,4,5])
sage: E.base_ring()
Integer Ring
sage: E.conductor()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/24208/_home_masgaj__sage_init_sage_0.py in <module>()

AttributeError: 'EllipticCurve_generic' object has no attribute 'conductor'
```

as compared to 

```
sage: E = EllipticCurve([1,2,3,4,5])
sage: E.base_ring()
Rational Field
sage: E.conductor()
10351
```

i.e. we already choose to use the field of fractions as base ring when the entries are integers, and if we try to insist otherwise we get an ell_generic on which we can do rather little.

Of course a purist would say that there is no such thing as an elliptic curve over ZZ (it would have to have everywhere good reduction), and we do not allow singular models.


---

Comment by AlexGhitza created at 2009-04-29 13:26:56

The attached patch implements option 1 above in the cleanest way I could think of, and adds some doctests and explanations.


---

Comment by AlexGhitza created at 2009-04-29 13:26:56

Changing keywords from "" to "elliptic curve integers mod prime".


---

Comment by AlexGhitza created at 2009-04-29 13:26:56

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-04-29 13:26:56

Changing status from new to assigned.


---

Comment by cremona created at 2009-04-29 15:29:53

I was expecting that here,

```
sage: F = Zmod(101) 
 	92	        sage: EllipticCurve(F, [2, 3]) 
 	93	        Elliptic Curve defined by y^2 = x^3 + 2*x + 3 over Ring of integers modulo 101 
 	94	        sage: E = EllipticCurve([F(2), F(3)]) 
 	95	        sage: type(E) 
 	96	        <class 'sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field'> 
```

both would end up as EllipticCurve_finite_field objects, but I guess that we have to have a way of constructing the other things, so that is ok.
But would it not be better to change the base_ring (and base_field) of E in the second case to GF(101)?

Next (but not this patch's fault at all):


```
sage: R = Zmod(101)
sage: is_Field(R)
True
sage: is_FiniteField(R)
False
```


Now the second is justified since the is_*() functions are supposed to do a type test, not prove a theorem, but then why should the first not also return False?  Should this be a new ticket?


Here:

```
227	 	        raise ValueError, "sequence of coefficients must have length at 2 or 5" 
 	246	        raise ValueError, "sequence of coefficients must have length between 2 and 5" 
```

It is [2,5] and not [2..5], and the only valid lengths are 2 and 5, so can we put that back to how it was?  

Sorry to be such a pain with my reviews...I'll give it a positive review if the very last point is seen to.


---

Attachment

Replying to [comment:5 cremona]:
> I was expecting that here,
> {{{
> sage: F = Zmod(101) 
>  	92	        sage: EllipticCurve(F, [2, 3]) 
>  	93	        Elliptic Curve defined by y^2 = x^3 + 2*x + 3 over Ring of integers modulo 101 
>  	94	        sage: E = EllipticCurve([F(2), F(3)]) 
>  	95	        sage: type(E) 
>  	96	        <class 'sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field'> 
> }}}
> both would end up as EllipticCurve_finite_field objects, but I guess that we have to have a way of constructing the other things, so that is ok.
> But would it not be better to change the base_ring (and base_field) of E in the second case to GF(101)?

Both of these do end up as `EllipticCurve_finite_field` objects, which is fine because (mathematically) `Zmod(101)` is a finite field.  However, I did not want to just change the base ring to `GF(101)` because I don't think it is necessary, and after all the user specified that she wanted the base ring to be `Zmod(101)`.  It's a bit pedantic, but we should give the user the object she asks for (if possible), not something that's isomorphic to it.  I think the point becomes more clear in another situation, which I ran into while testing this code: say you have an elliptic curve over a number field, and you take its reduction at some good prime.  You end up with an elliptic curve over what is mathematically a finite field, so should we just force this curve to be over `GF(q)` rather than `Residue field of...`?  We would be throwing away some information here, and I think we shouldn't.

So my philosophy in this patch was that we keep the base ring that the user asked for, but we're smart enough to recognise that it's (mathematically) a finite field so we create an elliptic curve of the appropriate type.

> Next (but not this patch's fault at all):
> 
> {{{
> sage: R = Zmod(101)
> sage: is_Field(R)
> True
> sage: is_FiniteField(R)
> False
> }}}
> 
> Now the second is justified since the is_*() functions are supposed to do a type test, not prove a theorem, but then why should the first not also return False?  Should this be a new ticket?

I noticed this as well when writing the code because I was getting inconsistent behaviour from these two functions.  It's a bit annoying for the developer (since we somehow assume that `is_*()` just checks types), but I guess it is documented...

> 
> Here:
> {{{
> 227	 	        raise ValueError, "sequence of coefficients must have length at 2 or 5" 
>  	246	        raise ValueError, "sequence of coefficients must have length between 2 and 5" 
> }}}
> It is [2,5] and not [2..5], and the only valid lengths are 2 and 5, so can we put that back to how it was?  

Sorry about this one, I saw it from the corner of my eye and my hands did the typing before the brain had time to process it properly.  Also the "at" in "length at 2 or 5" confused me.  I've changed it now, and replaced the patch.

> Sorry to be such a pain with my reviews...I'll give it a positive review if the very last point is seen to.

I'm happy you are so careful with the reviews.  It's hard to think of everything that could go wrong (thank god for doctests), or that could be confusing, or that could be bad design, especially when you fix a particular bug without necessarily having the big picture in mind.  So it's great to have a fresh pair of eyes look over this stuff.

I'm marking this as "needs review" again, but the only new change is reverting the "2 to 5" mistake.


---

Comment by cremona created at 2009-04-30 08:07:52

Thanks for the well-argued response.  The example you gave (reduction of an elliptic curve over a number field) is an excellent one.

I just diff'd this patch with the earlier one to give the Positive Review.


---

Comment by mabshoff created at 2009-04-30 09:07:10

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 09:07:10

Resolution: fixed
