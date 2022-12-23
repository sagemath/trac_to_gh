# Issue 6193: [with patch, needs review] implement elliptic logarithm

Issue created by migration from https://trac.sagemath.org/ticket/6193

Original creator: robertwb

Original creation time: 2009-06-03 06:58:06

Assignee: was

CC:  cremona

Depends on #6021.


---

Attachment


---

Comment by robertwb created at 2009-06-03 07:00:53

Comment from previous ticket: 

Yet another patch, to be applied after the previous ones.

   1. Better handling of precision. The algebraic quantities needed for both periods and elliptic logs are now cached. Then period and log computations just have to coerce into the appropriate Real/ComplexField, and do the transcendental part via agm.
   2. Elliptic log implementation now moved into period lattice class (except for the algorithm="pari" case which is unchanged). Also available via call i.e. as L.elliptic_logarithm(P) or just L(P). Uses an extended agm function which has been separated off.
   3. Earlier precision issues with a difficult example are fixed; we get all the same digits as pari, and faster. To do this we compute the extended AGM in double the required precision and then revert to desired precision at the end. (I tried adding 10 or 20 bits of precision, but that nasty example (18074g1) needs more). 

The only remaining thing is to implement elliptic logs for non-real lattices. This is not hard to do but harder to justify! Before I do that, to test it I need to implement the reverse of the elliptic log -- using Weierstrass P-functions and derivative to go from z mod L back to P(x,y) with complex coords in general.


---

Comment by robertwb created at 2009-06-03 07:13:55

The code looks good after my first reading. 

 * I assume by `on_egg` you're implying the non-identity component of an elliptic curve over R? 

 * Where does the terminology `ei` come from for the x-coordinates of the 2-torsion? (I may just not be familiar with the notation, if so, just let me know.) 

 * What assurance is there that `extended_agm_iteration` will terminate in the presence of numerical noise? (I suppose if delta is around machine epsilon, then (1+delta).sqrt() should be identically 1. Is that enough? 

 * It would be good to have an example demonstrating that the elliptic log is actually the inverse of the standard Weierstrass isomorphism (at least using Pari's version so far)

I am still building a 4.0 so I haven't actually applied/tested it, but will when that's done building.


---

Comment by cremona created at 2009-06-03 08:30:39

Replying to [comment:2 robertwb]:
> The code looks good after my first reading. 
> 
>  * I assume by `on_egg` you're implying the non-identity component of an elliptic curve over R? 

That is right.  Some people call this (the compact component in `R^2`) the "egg".  Perhaps a comment should be included to explain this, but the name has the advantage of being short.

> 
>  * Where does the terminology `ei` come from for the x-coordinates of the 2-torsion? (I may just not be familiar with the notation, if so, just let me know.) 
> 

I thought it was standard to call the real roots e1, e2, e3 (i.e. these are the x-coords of the points of order 2).  Less standard is the ordering (for curves over R):  when they are all real then either e1<e2<e3 or the other way round;  and when only one is real, it is e1 for some people and e3 for others.  Hence I do make this explicit.

>  * What assurance is there that `extended_agm_iteration` will terminate in the presence of numerical noise? (I suppose if delta is around machine epsilon, then (1+delta).sqrt() should be identically 1. Is that enough? 
> 

That does worry me.  I am hopeless at numerical analysis;  I put this simple test in while testing and it seemed to work fine;  otherwise we should be testing that delta is small enough that 1+delta is exactly 1 within the current precision.  (Note that the way this is coded it is already using relative rather than absolute precision, which is good).

>  * It would be good to have an example demonstrating that the elliptic log is actually the inverse of the standard Weierstrass isomorphism (at least using Pari's version so far)

Of course;  and that is listed in the things I have not done yet.

> 
> I am still building a 4.0 so I haven't actually applied/tested it, but will when that's done building. 
>


---

Comment by robertwb created at 2009-06-03 08:46:06

Replying to [comment:3 cremona]:
> Replying to [comment:2 robertwb]:
> > The code looks good after my first reading. 
> > 
> >  * I assume by `on_egg` you're implying the non-identity component of an elliptic curve over R? 
> 
> That is right.  Some people call this (the compact component in `R^2`) the "egg".  Perhaps a comment should be included to explain this, but the name has the advantage of being short.

I think it's fine, the terminology is very evocative of what it is :)

> >  * Where does the terminology `ei` come from for the x-coordinates of the 2-torsion? (I may just not be familiar with the notation, if so, just let me know.) 
> 
> I thought it was standard to call the real roots e1, e2, e3 (i.e. these are the x-coords of the points of order 2).  Less standard is the ordering (for curves over R):  when they are all real then either e1<e2<e3 or the other way round;  and when only one is real, it is e1 for some people and e3 for others.  Hence I do make this explicit.

Oh, of course. I wasn't thinking of the i as an index, now ei makes total sense with the e1, e2, and e3 conventions.


---

Comment by robertwb created at 2009-06-05 11:11:36

There was some numerical noise, I fixed it with this patch. Also, I added a test to see that it does actually invert the Weierstrass P function (though this should be done more cleanly when we have a native and/or better wrapped Weierstrass P.) 

Thinking about the agm termination condition, the convergence of agm is quadratic, so delta will be ~1upl < 3upl, so it should not be an issue.


---

Attachment


---

Comment by cremona created at 2009-06-05 13:58:33

Thanks.  Pity about the ..., but it's the only one.  I'm working on getting the ellztopoint (via pari's ellwp) but will put that on another ticket.  John


---

Comment by ncalexan created at 2009-06-13 20:41:52

Resolution: fixed
