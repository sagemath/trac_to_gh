# Issue 5590: coercion between polynomial rings over extension fields and polynomial rings over the prime subfield

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-03-23 12:14:48

Assignee: malb

CC:  was

Keywords: coercion, polynomial ring

At #5569 William wrote: 
> As a challenge to Martin -- can you improve Sage so this decimal 
> string conversion (which could be a killer show stopper if the 
> ideal had huge elements) isn't needed, and instead one can use a 
> homomorphism?

The situation William is talking about is this:


```
sage: K.<a> = GF(2^3)
sage: P.<x,y> = PolynomialRing(K)
sage: R = PolynomialRing(GF(2),3,'a,x,y')
```


and we are looking for a way to convert elements in `P` to elements in `R`.


