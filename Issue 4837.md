# Issue 4837: implement random_element for number fields

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-12-20 15:37:20

Assignee: AlexGhitza

Keywords: random element number field

At the moment, if K is a number field then K.random_element() uses a generic implementation that simply returns a random *integer* coerced into K.  It would be useful to have a real implementation that returns an actual random element of K.

A simple idea would be to find a primitive element j that generates K as a field extension over QQ, and to return a random polynomial of degree at most [K:QQ].  This should be easy since random polynomials in one variable are already implemented.



---

Comment by AlexGhitza created at 2008-12-20 16:40:40

OK, the attached patch implements the simple idea given above.  More precisely: let a be a primitive element of K, then every element of K can be written as a polynomial of degree (at most) [K:QQ]-1 in the variable a, with rational coefficients.  Therefore the function returns a random polynomial of this type.


---

Comment by cremona created at 2008-12-21 17:49:03

There are two obvious ways to implement this:  the one in the patch (random polynomial), or a random QQ_vector applied to the QQ_basis for the field.  I think I prefer the latter, though I am not sure why.  It would almost certainly be useful to have a random_integer() function too, implemented via a random ZZ-linear combination of the ZZ-basis.  The current patch could also be adapted, but with more difficulty (especially if the ring of integers is not of the form ZZ[a]).

I don't know how easy the alternative approach would be to apply to relative extensions.  The current patch does fine, as long as computing a primitive element is not too time-consuming.

This patch applies cleanly to 3.2.2 and all tests in sage/rings/number_field pass, so I am happy to give it a positive review, while inviting comments on my comments!


---

Comment by AlexGhitza created at 2008-12-22 06:35:01

Hi John,

Here's a third possibility: any field extension L/K is really a quotient K[x]/(f(x)), so we can start with a random element of K[x] and reduce it mod f(x).  Getting a random element of K[x] is easy if we can get random elements of K itself.  If L is an absolute number field, then K=QQ and we're in business; if L/K is a relative number field, then this will "descend" to K and so on until it hits QQ.

The advantage of this approach is that it is very transparent and easy to code.  Also in the relative situation there is no need to compute a primitive element, all we need are the splitting polynomials for each step in the tower, and those are just part of the given data.

I agree with the suggestion that we should be able to produce random algebraic integers as well.  But I think this should be implemented as a method random_element() of an order in a number field, rather than as a method of the number field itself.  And then your idea of using the ZZ-basis is really the only option I can think of.


---

Comment by cremona created at 2008-12-22 09:20:32

I fully agree:  use the existing method for absolute fields (where there's essentially no need to find a primitive element), use the recursive method for relative extensions, and make a new ticket for random elements of orders (and fractional ideals while we're at it) which will use Z-bases.

Will you be adapting the current patch accordingly?


---

Comment by AlexGhitza created at 2008-12-22 10:28:53

Good.  I will modify the patch to use this strategy and resubmit it.


---

Comment by cremona created at 2008-12-22 16:37:49

Alex, I just noticed that you can do this in one line with 

K(K.polynomial_ring().random_element(degree=K.degree()-1))

since K.polynomial_ring is *not* K[x] but is the polynomial ring over K's base field, whatever that is.  So this will automatically work ok recursively, given that the random_element() method for polynomial rings uses the random_element() method for the coefficient ring.

John


---

Attachment

depends on the patch at #4218


---

Comment by AlexGhitza created at 2008-12-23 11:17:28

Following the discussion at
http://groups.google.com/group/sage-devel/browse_thread/thread/67b40b64970bbf19
I implemented coercion of elements from the isomorphic polynomial quotient ring to the number field.  As a consequence of this and the code for random elements of quotient rings at #4218, random_element() for number fields became a fairly trivial one-liner.

See the attached patch.  It is advisable to first merge the patch at #4218.


---

Comment by cremona created at 2008-12-23 12:44:18

The patch applies fine (over 3.2.2 + #4218).  Just one thing:  for an absolute extension we can create an element from a polynomial over the base field, but not for a relative extension:

```
sage: K.<z>=CyclotomicField(7)
sage: Ky.<y>=PolynomialRing(K)
sage: L.<a>=K.extension(y^2+1)
sage: K(K.polynomial_ring().random_element())
z + 1
sage: L(L.polynomial_ring().random_element())
---------------------------------------------------------------------------
TypeError           
...
TypeError: Unable to coerce 7/2*z^5 + 1/2*z^4 + z^3 - 37/2*z to a rational
```

I'm sure this will cause complaints before long, so can we make the new constructor slightly more flexible?  Of course if your replace `polynomial_ring()` with `polynomial_quotient_ring()` it works fine thanks to the new code.


---

Comment by AlexGhitza created at 2008-12-24 12:42:49

I was hoping to be able to take care of this quickly, but I keep running into brick walls.  I agree that it should be fixed though, and I've opened a new ticket for it, see #4869.


---

Comment by cremona created at 2008-12-24 14:33:31

OK, given the new ticket I'm happy to give this the positive review it has been waiting for.  Sorry to be fussy, Alex!


---

Comment by AlexGhitza created at 2008-12-25 08:13:33

Replying to [comment:11 cremona]:
> Sorry to be fussy, Alex!

No need to apologise, I quite appreciate a careful reviewing; in this instance, I had noticed the problem with polynomial rings earlier in the process, but since it wasn't the main point I put it aside, then forgot about it.  This way we have it properly reported.


---

Comment by mabshoff created at 2009-01-12 01:20:53

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-12 01:20:53

Resolution: fixed
