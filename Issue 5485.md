# Issue 5485: issue with dimension of ideals in polynomial rings

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-03-11 08:25:23

Assignee: malb

Consider this:


```
sage: R.<x, y> = ZZ[]
sage: I = R.ideal(0)
sage: I.dimension()
verbose 0 (794: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
1
```


But judging from the docstring of I.dimension(),this should be the Krull dimension of R/I, which is 3 since R/I is (canonically isomorphic to) R:


```
sage: R.krull_dimension()
3
```




---

Comment by john_perry created at 2009-03-18 00:21:45

Out of curiosity, isn't the Krull dimension 2? How can the dimension of the variety be larger than the number of variables? Apparently there are two bugs at work here.


---

Comment by john_perry created at 2009-03-18 01:44:56

Looking up a little bit about Krull dimension, I think I see the problem: ZZ has Krull dimension 1, whereas fields have Krull dimenson 0. The given code assumes that the ground ring is a field. This is assumed by the source material in Cox, Little, and O'Shea, so the old code almost works as it is supposed to.

There was also an issue with the implementation so that even the zero ideal in a field would be wrong. This is now fixed, so the code works "as it is supposed to", by which I mean that it works in fields, per the source material.

However, Alex is right that this is not quite the same as what the documentation promises, since the documentation talks as if the ring is arbitrary. So, it doesn't *really* work the way it is supposed to. I have an idea for a fix for the case where the ground ring is not a field: add the Krull dimension of the ground ring to whatever is computed by the current code.

But is this correct? If so, the fix is trivial. If not, this will require a lot more work, since all my references assume fields.


---

Comment by AlexGhitza created at 2009-03-18 06:15:31

Hi John,

I've learned the hard way not to expect dimension to behave coherently when the base ring is not a field.  This being said, I have just spent some quality time with EGA IV and found something that we can use: Corollary 5.5.4 (page 95 in volume 2 of EGA IV) says that if the ring A is noetherian, then the dimension of A[x_1,...,x_n] is equal to n + dim(A).

There are examples due to Nagata of non-noetherian rings A such that dim(A)=1 but dim(A[x])=3.

So here's what we need to do for polynomial rings: check whether the base ring is noetherian; if not, raise a NotImplementedError.  If yes, return the Krull dimension of the base ring plus the number of generators.

If you want to go ahead and do this, that's great.  If not I can probably get around to it sometime before this weekend.


---

Comment by john_perry created at 2009-03-18 15:47:21

Hi Alex,

What is EGA IV? If my university's library has it, I'd be glad to take a look at it.

You wrote,

> I have just spent some quality time with EGA IV and found
> something that we can use: Corollary 5.5.4 (page 95 in
> volume 2 of EGA IV) says that if the ring A is noetherian,
> then the dimension of A[x_1,...,x_n] is equal to n + dim(A).
> ...
> 
> So here's what we need to do for polynomial rings: check
> whether the base ring is noetherian; if not, raise a
> NotImplementedError.  If yes, return the Krull dimension of
> the base ring plus the number of generators.


Hold on: `dimension()` is a method of an ideal, not of a ring. I can see that this would work with (0), but will it work with other ideals? i.e., can I assume that if R is Noetherian, then I should add the affine dimension? (I'm not sure that _affine dimension_ is the right term, probably not, but I hope you get the idea.)

For example:


```
sage: R.<x,y> = ZZ[]
sage: I = R.ideal(x+y)
sage. I.dimension()
```



Should the answer be 1 (current) or 2 (my wholly uninformed guess, dim ZZ + affine dim of ideal) or something else?


---

Comment by AlexGhitza created at 2009-03-28 02:12:53

EGA is Grothendieck's Elements de Geometrie Algebrique.  Here is a better reference: Eisenbud's "Commutative algebra with a view toward algebraic geometry", more precisely chapter 8 "Introduction to dimension theory".  I think we can get a lot of mileage even just out of the axioms that he gives for dimension (which turn out to uniquely characterise Krull dimension).


---

Comment by AlexGhitza created at 2009-03-29 02:12:27

OK, so there are several issues here.

One is that we're not sure that the naive algorithm implemented in dimension() works over base rings that are not fields.  The most interesting instance of this (in my opinion) is when the base ring is ZZ.  We are currently returning wrong answers, so even raising a `NotImplementedError` would be preferable.  Of course, it would be nice if we could get it to work -- but note that Singular 3.1.0 will have support for polynomial rings over ZZ, so in the worst case we can wait until they release.

The more pressing issue is that the naive algorithm returns wrong answers even if you run it over QQ.  To see this, try the following as it is now:


```
sage: R.<x, y> = QQ[]
sage: I = R.ideal(0)
sage: I.dimension()
2
```


This is the correct answer, and it's coming directly from Singular.  However, we can force Sage to use the naive algorithm by inserting `raise TypeError` on line 977 of `multi_polynomial_ideal.py`.  Run `sage -br` and try the same computation again:


```
sage: R.<x, y> = QQ[]
sage: I = R.ideal(0)
sage: I.dimension()
verbose 0 (932: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
1
```


This is wrong and should be our main priority.  In fact, I think it would be ok to just fix this for this ticket and open enhancement tickets for dimension() over tricky base rings.


---

Comment by john_perry created at 2009-03-29 12:57:40

The patch I uploaded 11 days ago _should_ fix the problem you identified. Unfortunately, I wrote it using an earlier version of Sage (not 3.4). I'll upload a new version tomorrow.


---

Comment by john_perry created at 2009-03-30 22:37:06

previous fix rewritten for sage 3.4, with Alex's recommendation on a NotImplementedError


---

Attachment

The current patch raises a NotImplementedError over rings that are not fields. (Tested with ZZ[x,y].) Over rings that Singular can't handle, this now works with the given problem. I added a docstring that tests it over PolynomialRing(GF(2147483659),order='lex'), and it returns the correct result.


---

Comment by AlexGhitza created at 2009-04-03 10:07:09

Looks good to me.


---

Comment by mabshoff created at 2009-04-03 23:29:31

Resolution: fixed


---

Comment by mabshoff created at 2009-04-03 23:29:31

Merged in Sage 3.4.1.rc0.

Cheers,

Michael
