# Issue 3883: Streamline elliptic curve division (torsion) polynomials

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-08-17 17:33:03

Assignee: was

#3109 introduced a new bivariate division polynomial for elliptic curves, only implemented for curves in short Weierstrass form, and also very useful functions for dividing points (for arbitrary curves).

In reviewing #3377 I wanted to use the division_points() function for curvesw defined over number fields and ran into problems.  This led me to reconsider the existing division polynomial code, and this is the result.  I removed the commenting-out # signs from a perfectly good set of three functions pseudo_division_polynomial(), multiple_x_numerator() and multiple_x_denominator().  I rewrote full_division_polynomial() to use these, making it very much simpler and apply to all curves, not just those in short W. form.  I also rewrote division_points(), simplifying it.

I'll shortly post a patch for all this.  In the patch you will find some rather long-winded comments which explain very precisely what the relation is between these functions.  If approved, I'll make use of this and get back to working on #3377.



---

Attachment


---

Comment by cremona created at 2008-08-17 17:35:18

Patch sage-trac3883.patch is based on 3.1.rc0


---

Comment by cremona created at 2008-08-26 11:40:08

Chris W. has reviewed this in an email to John C., which I will copy here when he tells me I can, and there will be a new patch appearing after that.


---

Comment by cremona created at 2008-08-26 15:36:30

Apply after the previous patch


---

Attachment

Review by Chris Wuthrich:

So, I had a closer look at your division polynomials.

I don't get any errors with 3.1.1. (without the changes in 3927).
I will make some small changes, like the spelling of my name :), and
some bigger ones, depending on your views on these :

    * Personally I would have chosen one name, say division_polynomial,
and then an option in it to get the full_ version or the pseudo
version. There are already very many (218) function on the elliptic
curve class and it would be less confusing for the average user. That
is a matter of taste, I guess.

    * multiply_x_* should maybe be a _multiply_x_* as I don't think
someone will ever use that directly and it will certainly be confusing
for the newbie. Where was this function before ? Has it something to
do with the _multiply_point in padics.py ?
 There is another implementation of the division_polynomials that
could be rewritten. But there the curve has coefficients in a ring and
one computes integrally. So that does not make sense in ell_generic.

    * By the way and completely unrelated, I saw the example
  E = EllipticCurve(GF(3),[1,2])
  E.short_weierstrass_model()
which gives "no short model for Elliptic Curve defined by y^2  = x^3 +
x + 2 over Finite Field of size 3". Do you agree that we should not
raise an error when the model is already in short form ?

    * Also, completely unrelated again. E.integral_weierstrass_model
should be E.integral_short_weierstrass_model..


---

Comment by cremona created at 2008-08-26 15:48:57

Replying to [comment:3 cremona]:
> Review by Chris Wuthrich:
> 
> So, I had a closer look at your division polynomials.

Thanks!

> 
> I don't get any errors with 3.1.1. (without the changes in 3927).
> I will make some small changes, like the spelling of my name :), and
> some bigger ones, depending on your views on these :

The only appearance of your name I found has it spelled "Wuthrich" (and not by me).  Is it an umlaut you want?

I have made some changes based on your comments, and there is a second patch.

> 
>     * Personally I would have chosen one name, say division_polynomial,
> and then an option in it to get the full_ version or the pseudo
> version. There are already very many (218) function on the elliptic
> curve class and it would be less confusing for the average user. That
> is a matter of taste, I guess.

I do agree, so I have refactored the code accordingly.  The only function the user needs is `division_polynomial()`.    Using the value of a flag one can access all the existing functionality.  I have commented out code which is now redundant:  the function `full_division_polynomial()`, originally written by William Stein and rewritten by me, is now accessible by calling division_polynomial with parameter two_torsion_multiplicity=2.  The alternative old `torsion_polynomial()` code by David Kohel has been commented out since it duplicates what is there.  The old function `pseudo_torsion_polynomial()` by David Harvey is now the basis of everything, but is renamed `division_polynomial_0()`.

> 
>     * multiply_x_* should maybe be a _multiply_x_* as I don't think
> someone will ever use that directly and it will certainly be confusing
> for the newbie. Where was this function before ? Has it something to
> do with the _multiply_point in padics.py ?

These functions were implemented by David Harvey along with `pseudo_torsion_polynomial()`.  I left the names as they were since we need to access them from ell_point.py which would be awkward if they had leading underscores.  (But I am open to other suggestions for the names of these).

>  There is another implementation of the division_polynomials that
> could be rewritten. But there the curve has coefficients in a ring and
> one computes integrally. So that does not make sense in ell_generic.

I'm not sure where you are referring to here.

> 
>     * By the way and completely unrelated, I saw the example
>   E = EllipticCurve(GF(3),[1,2])
>   E.short_weierstrass_model()
> which gives "no short model for Elliptic Curve defined by y^2  = x^3 +
> x + 2 over Finite Field of size 3". Do you agree that we should not
> raise an error when the model is already in short form ?
> 

Fair enough, but that belongs in another ticket.

>     * Also, completely unrelated again. E.integral_weierstrass_model
> should be E.integral_short_weierstrass_model..
> 

Ditto.


---

Comment by wuthrich created at 2008-08-27 17:16:34

small changes to be applied after the previous two patches.


---

Attachment

I have added a small patch, which changes all multiply_x_numerator to _multiply_x_numerator. Personally I don't see why it should harm that there is a _function in ell_points.py. I don't believe this function would be used by users directly, so it makes sense to me to hide. Also I changed the documentation referring to my thesis.

As it is only a matter of taste, it is up to John to decide, I think, if he would like the third patch to be applied or not.

Other than that all is fine. Test pass, the functions are very well documented and very well coded.

POSITIVE REVIEW (both with only the first two or will all three patches).


---

Comment by wuthrich created at 2008-08-27 17:35:16

> The only appearance of your name I found has it spelled "Wuthrich" (and not by me). Is it an umlaut you want?

No there was a Christopher before. :)

> I do agree, so I have refactored the code accordingly. [..] but is renamed division_polynomial_0().

I agree with you and the new version.


>>   There is another implementation of the division_polynomials that could be rewritten. 
>> But there the curve has coefficients in a ring and one computes integrally. So that does
>>  not make sense in ell_generic.
>
> I'm not sure where you are referring to here.

The function _multiply_point on line 303 in padics.py is just another version of an implementation of the division polynomials. In fact this builds the polynomials that you called multiply_x_numerator and denominator, but as homogeneous polynomials. To clear up denominators so that integers can be plugged in to get integers. The p-adic height computation needs the computation of the square root of numerator of 
x(m*P) for a large m. Using this function is much faster than computing m*P. 

But I think it is better to leave that as it is by now.

Chris.


---

Comment by cremona created at 2008-08-27 18:54:18

I am quite happy with the extra changes Chris has made.  (I had already corrected his first name, but he gives a better reference anyway).

Thanks for the review!


---

Comment by mabshoff created at 2008-08-28 02:01:43

Merged in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-28 02:01:43

Resolution: fixed
