# Issue 4296: univariate polynomial power ignores 2nd argument

Issue created by migration from https://trac.sagemath.org/ticket/4296

Original creator: zimmerma

Original creation time: 2008-10-15 13:47:21

Assignee: somebody


```
sage: R = PolynomialRing(GF(2), x)
sage: f = R(x^9 + x^7 + x^6 + x^5 + x^4 + x^2 + x)
sage: h = R(x^10 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + 1)
sage: (f^2) % h
x^9 + x^8 + x^7 + x^5 + x^3
sage: pow(f, 2, h)
x^18 + x^14 + x^12 + x^10 + x^8 + x^4 + x^2
```

We should expect both results to be equal to f^2 mod h.


---

Comment by AlexGhitza created at 2008-12-28 12:27:29

This works for me in sage-3.2.2.


---

Comment by mabshoff created at 2008-12-28 15:40:41

Same for me:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R = PolynomialRing(GF(2), x)
sage: f = R(x^9 + x^7 + x^6 + x^5 + x^4 + x^2 + x)
sage: h = R(x^10 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + 1)
sage: (f^2) % h
x^9 + x^8 + x^7 + x^5 + x^3
sage: pow(f, 2, h)
x^9 + x^8 + x^7 + x^5 + x^3
sage: 
```

Please add a doctest and once it has been merged we can close this ticket.
| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Comment by AlexGhitza created at 2008-12-28 15:59:10

OK, a patch with the doctest is attached.


---

Attachment

The attached patch seems to be just the doctest, no new code...


---

Comment by mabshoff created at 2008-12-29 20:25:32

Replying to [comment:5 robertwb]:
> The attached patch seems to be just the doctest, no new code...

Yes, because the bug originally reported has been fixed [or so it seems :)].

Cheers,

Michael


---

Comment by robertwb created at 2008-12-29 21:02:06

Ah, good point. 

I'm not sure how I feel about throwing the symbolic x around all around, though I guess efficiency doesn't matter too much here. 

Also, just looking at the code it can be very inefficient--it computes (a^b) in full, then divides by the modulus taking the remainder. This is fine for small exponents, but for anything large is wasteful.


---

Comment by mabshoff created at 2008-12-29 21:45:58

Replying to [comment:7 robertwb]:
> Ah, good point. 

:)

> I'm not sure how I feel about throwing the symbolic x around all around, though I guess efficiency doesn't matter too much here. 

Yeah, I would consider it a good idea to get this in as is and open another ticket to make this more efficient.

> Also, just looking at the code it can be very inefficient--it computes `(a^b)` in full, then divides by the modulus taking the remainder. This is fine for small exponents, but for anything large is wasteful. 

Cheers,

Michael


---

Comment by cremona created at 2009-01-18 17:44:34

I give this a positive review since it is just a doctest showing that something which used to fail now works.

I sympathise with robertwb's concern, but that should be a separate ticket.  I looked for, but could not find anywhere, the code which pow(f,2,h) runs.


---

Comment by mabshoff created at 2009-01-19 04:16:38

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-19 04:16:38

Resolution: fixed
