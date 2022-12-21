# Issue 1413: added _sig_on/_sig_off to mpolynomial_libsingular

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2007-12-06 20:34:55

Assignee: was

A few of these were annoying me so I tried to do all the obvious ones.


---

Comment by malb created at 2007-12-07 11:43:14

I don't like this approach because it slows down small examples a lot. At least some heuristic when to apply `_sig_on`/`_sig_off` should be used, e.g. the number of monomials of the polynomials involved.


---

Comment by jbmohler created at 2007-12-19 02:34:37

here's a new patch to review after was' comments.  I've checked the lengths and required polys to be 10-15 monomials in length before kicking in the _sig_on


---

Comment by mabshoff created at 2007-12-22 15:36:14

I don't like this patch since I assume that libSingular offers some function that provides the length of a polynomial instantly. The patch now iterates over up to 15 monomials for each polynomial which just seems wrong. If I have some time I will check how much of a performance impact this has, but multiplying polynomials with 15 terms or so should be instant anyway, so I don't see the need for sig_on & sig_off. 

Joel: what is the motivation behind this patch? Are there actual cases where you need this? I also thing that sending signals to libSingular while it is multiplying polynomials won't be very beneficial and might leave us with some sort of potential corruption. 

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-01-24 09:01:11

Changing assignee from was to malb.


---

Comment by AlexGhitza created at 2008-01-24 09:01:11

Changing component from algebraic geometry to commutative algebra.


---

Comment by jbmohler created at 2008-01-31 18:45:53

I'm attaching another patch in response to mabshoff's review.  There is, in fact, a pLength singular API.

Note that this does the _sig_xx stuff for the code in these methods:
__pow__,__floordiv__,factor,gcd,lcm,quo_rem,resultant
Obviously, it would be trivial to make data large enough so that any of these take an eternity to compute.

As to the corruption issues with a signal.  Huh?  It's the same story with virtually every other _sig_on/_sig_off in the sage code.  One should *expect* memory leaks and tolerate corruption with any of them.


---

Comment by malb created at 2008-01-31 21:29:40

Replying to [comment:8 jbmohler]:
> I'm attaching another patch in response to mabshoff's review.  There is, in fact,
> a pLength singular API.

This function also loops through the polynomial:


```
PINLINE0 int pLength(poly a)
{
  int l = 0;
  while (a!=NULL) {
    pIter(a);
    l++;
  }
  return l;
}
```


However, I'd say we should still apply this patch and see if something gets too slow. Also, all algorithms which involve `_sig_on`/`_sig_off` should be at least quadratic in the number of monomials so this linear operation shouldn't matter anyway, right?

> Note that this does the _sig_xx stuff for the code in these methods:
> __pow__,__floordiv__,factor,gcd,lcm,quo_rem,resultant
> Obviously, it would be trivial to make data large enough so that any of these take an eternity to compute.

> As to the corruption issues with a signal.  Huh?  It's the same story with
> virtually every other _sig_on/_sig_off in the sage code.  One should *expect*
> memory leaks and tolerate corruption with any of them.

I second that.

However, the patch fails to apply to 2.10.1.rc2


```
applying /home/malb/_sig_on_libsingular.patch
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #2 succeeded at 3105 with fuzz 1 (offset 0 lines).
Hunk #3 FAILED at 3167
1 out of 7 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej
abort: patch failed to apply
```



---

Comment by malb created at 2008-02-13 13:37:24

To make my statement more precise: In case the merge conflict gets resolved I am happy to give this patch a positive review.


---

Comment by jbmohler created at 2008-02-14 18:16:58

Here's another patch against 2.10.2.  In the name of being anal, I added a polyLengthBounded cdef function which caps the monomial counting for speed.  Although, I agree with malb that this is probably irrelevant given that these algorithms are probably quadratic (certainly not linear).


---

Comment by jbmohler created at 2008-02-14 18:17:31

patch against 2.10.1


---

Attachment


---

Comment by mabshoff created at 2008-02-14 18:32:21

`_sig_on_libsingular.patch` applies cleanly against my 2.10.2.alpha0, so positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-14 18:33:01

Merged in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-14 18:33:01

Resolution: fixed
