# Issue 2498: PARI's is_irreducible being used inappropriately

Issue created by migration from https://trac.sagemath.org/ticket/2498

Original creator: dmharvey

Original creation time: 2008-03-12 16:24:48

Assignee: somebody

CC:  malb@informatik.uni-bremen.de

PARI's polynomial irreducibility and factoring routines are being used incorrectly for certain base rings. Here is an example:


```
sage: R.<x> = PolynomialRing(Integers(35))
sage: f = (x^2+2*x+2)*(x^2+3*x+9)
sage: f
x^4 + 5*x^3 + 17*x^2 + 24*x + 18
sage: factor(f)
x^4 + 5*x^3 + 17*x^2 + 24*x + 18
sage: f.is_irreducible()
True
```


The PARI documentation for `polisirreducible` says: "Irreducibility is checked over the smallest base field over which pol seems to be defined", whatever that means.

We should put in some checking to make sure this crazy behaviour doesn't happen, or at the very least put in big fat warnings in the documentation.



---

Comment by was created at 2008-03-12 16:33:58

> We should put in some checking to make sure this crazy behaviour 
> doesn't happen, 

+1 -- definitely. 

> or at the very least put in big fat warnings 
> in the documentation.

-1 -- let's just not allow this crap.

> "Irreducibility is checked over the smallest base field over which pol seems to be defined"

That's the sort of ick that I don't like about PARI.


---

Comment by AlexGhitza created at 2008-03-21 23:17:09

Just checking that I understand what we want to see here: suppose we are dealing with a polynomial over Z/nZ with composite n.  Then we want that both factor() and is_irreducible() throw a NotImplementedError instead of calling pari and getting an incorrect answer.

I wanted to make sure before I went and changed this.


---

Comment by cremona created at 2008-03-22 18:07:16

When n is composite in the sense that it has more than one prime factor, I agree with throwing NotImplementedErrror.  When n is a prime power we could try to be more clever (if f mod p has a factorization into coprime factors then this would lift uniquely to a factorization over Z/nZ, for example) but for now I suggest again making this NotImplemented.


---

Attachment

Yes, it should be possible to do something smart here.  For now, I'm just making factor() and is_irreducible() throw NotImplementedError so we don't get wrong answers.

See the attached patch.


---

Comment by cremona created at 2008-03-22 20:45:41

Instead of explicitly mentioning Z/nZ (for composite n) as not implemented, would it not be more useful to list which rings this _is_ implemented for?  (Fields, Z, anything else?)


---

Comment by was created at 2008-03-22 20:50:34

> Instead of explicitly mentioning Z/nZ (for composite n) as 
> not implemented, would it not be more useful to list which 
> rings this _is_ implemented for? (Fields, Z, anything else?)

It might be more useful now, but it's bound to become out of
date, in which case such a list would be wrong, and could turn
out to be way *less* useful than nothing.

William


---

Comment by cremona created at 2008-03-22 22:07:47

Replying to [comment:8 was]:
> > Instead of explicitly mentioning Z/nZ (for composite n) as 
> > not implemented, would it not be more useful to list which 
> > rings this _is_ implemented for? (Fields, Z, anything else?)
> 
> It might be more useful now, but it's bound to become out of
> date, in which case such a list would be wrong, and could turn
> out to be way *less* useful than nothing.
> 
> William

OK then -- the patch gets a thumbs up from me!


---

Comment by mabshoff created at 2008-03-23 20:37:23

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-23 20:37:23

Resolution: fixed
