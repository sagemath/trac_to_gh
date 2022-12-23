# Issue 5627: Trivial typo in quadratic_nonresidue

Issue created by migration from https://trac.sagemath.org/ticket/5627

Original creator: kcrisman

Original creation time: 2009-03-29 02:58:53

Assignee: justin

CC:  jonhanke

An "l" was missing.  


---

Attachment

Based on 3.4


---

Comment by kcrisman created at 2009-03-29 03:01:47

While fixing this, I also changed the TypeErrors to more appropriate ValueErrors, added a catch for non-primeness that is just slightly more informative (since no longer from legendre_symbol, but from the function itself), and added a doctest of one of these ValueErrors.


---

Comment by mvngu created at 2009-03-31 06:25:13

Here's a trivial observation on performance. Look at the line

```
247	        for r in range(2,p):
```

With the patch as is, on sage.math I get the following timings:

```
# BEFORE
sage: p = 179424673
sage: time quadratic_nonresidue(p)
CPU times: user 9.07 s, sys: 4.37 s, total: 13.44 s
Wall time: 13.44 s
5
sage: timeit("quadratic_nonresidue(p)")
5 loops, best of 3: 19.3 s per loop
```

Now if I change the said line to

```
247	        for r in xrange(2,p):
```

I get some performance improvement:

```
# AFTER
sage: p = 179424673
sage: time quadratic_nonresidue(p)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
5
sage: timeit("quadratic_nonresidue(p)")
625 loops, best of 3: 36.6 µs per loop
```

However, in both cases whether we use `range()` or `xrange()`, if p is say 88462514817229869523, then I get the following error for `range()`:

```
sage: p = 88462514817229869523
sage: quadratic_nonresidue(p)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/14179/_home_mvngu__sage_init_sage_0.py in <module>()

/scratch/mvngu/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/quadratic_forms/extras.pyc in quadratic_nonresidue(p)
    245     ## Find the smallest non-residue mod p
    246     try:
--> 247         for r in range(2,p):
    248             if legendre_symbol(r, p) == -1:
    249                 return r

TypeError: range() integer end argument expected, got sage.rings.integer.Integer.
```

And for `xrange()`, I get a similar error, but this time it's an `OverflowError`:

```
sage: p = 88462514817229869523
sage: quadratic_nonresidue(p)
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/14262/_home_mvngu__sage_init_sage_0.py in <module>()

/scratch/mvngu/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/quadratic_forms/extras.pyc in quadratic_nonresidue(p)
    245     ## Find the smallest non-residue mod p
    246     try:
--> 247         for r in xrange(2,p):
    248             if legendre_symbol(r, p) == -1:
    249                 return r

OverflowError: long int too large to convert to int
```



---

Comment by kcrisman created at 2009-03-31 17:09:39

Those are very interesting remarks!  Unfortunately, I didn't write it, I just used it, as they say.  

What I would say is that you should definitely review this, based of course on whether it fixes the typo and whether the new error checks and doctest are wrong (and of course whether it makes performance WORSE, which is possible since IANAP [I am not a programmer!]).  

Then you should open a different ticket for the performance issue and implement whatever you think is best.  (Maybe srange would allow your other example to work?)  I feel like this is what mabshoff would say, anyway :)  I'm not really sure whether this function has non-pedagogical uses in real life, but it's always worth looking at improvements that dramatic!


---

Attachment

referee patch


---

Comment by mvngu created at 2009-04-02 05:46:28

REFEREE REPORT



The patch `quad-nonres.patch` applies OK against Sage 3.4.1.alpha0; all doctests passed with the options

```
-t -long
```

I'm also adding the patch `trac_5627-referee.patch` which adds another test case in addition to kcrisman's test case. This patch should be applied on top of kcrisman's patch. So positive review for kcrisman's patch. Only my patch needs to be reviewed.



As for my observation on performance improvement, I agree with kcrisman that the issue should definitely be addressed in another ticket. That issue should not prevent kcrisman's patch from being applied, since kcrisman's patch only deals with exception handling, adding a test case, and fixing a typo.


---

Comment by cremona created at 2009-04-08 11:26:33

I have added another patch after looking carefully at this, which does the following:

    1. I removed hilbert_symbol_rational(), making a trivial change to hilbert_symbol() so that it already works on rationals.  I think this will useful outside the quadratic forms module.
    2. I moved IsPadicSquare() to a member function for rationals, so you now say r.is_padic_square(p) instead of IsPadicSquare(r,p), while at the same time making the function simpler and cleaner.  I think this will also be useful outside the quadratic forms module.
    3. I removed random_int_upto(n) since it does the same as ZZ.random_element(n).
    4. I simplified quadratic_nonresidue() (and changed its name to least_quadratic_nonresidue()) -- by putting in three simple tests for when the answer is 2, 3 or 5 the loop is avoided in 7/8 of the cases.   I also changed the loop to "for r in xsrange(7,p)", in response to the discussion earlier on this ticket:  adding the x gives an iterator instead of making the whole list and iterating through it (bad for large p!), and adding the s makes the iterator yield Sage integers (so it works for p too large to fit into a python int).  I also added an is_prime() test on p, since otherwise if you give it a huge composite number there seemed to be a danger that it would run through a loop of length p before realising that the input was invalid.

All tests in sage/quadratic_forms pass, as do those in arith.py and rational.py which were also touched.

If one of the origianl posters can ok my patch then the whole lot can be merged, I hope.


---

Comment by kcrisman created at 2009-04-08 14:02:30

I hate to be a wet blanket, but probably two things should be done:

1) Change the summary - this is no longer about a trivial typo

2) (possibly) leave in the no-longer-useful or moved functions with standard 6-month deprecation warning, including of course leaving in the import statements in other files like all.py.  Of course these would now just call the "better" functions instead of leaving in their old code.  Unless deprecation does not apply to these sort of functions?  That policy is still not completely clear to me.


---

Comment by cremona created at 2009-04-08 14:22:22

You are probably right, I got a bit carried away when I saw functions I knew I would like to use but rather hidden away.

I think that for functions which are only used in this module (i.e. quadratic_forms/*) we do not need to go through the deprecation procedure, especially as this stuff has not been in Sage long anyway.

A suitable new Summary would be something like "Tidy up utility functions for quadratic forms", but I'll leave that to you as it is your patch.

By the way, the extend_to_primitive() function will be extremely useful too, and I would like to see it mvoed to somewhere like matrix/matrix_integer_dense.pyx (where smith_form is) but I thought I had wreaked enough havoc as it was.

Any comment from mvngu who did the original refereeing?


---

Comment by mvngu created at 2009-04-17 02:34:20

Replying to [comment:7 cremona]: 
> Any comment from mvngu who did the original refereeing?


It looks like this ticket has reached a stage where it's more difficult to merge, as is the case with #545, although not as difficult. The original idea was to fix a typo and add some test cases. Since cremona now adds more quadratic forms stuff, I don't feel confident to review the technical maths content of his patch. Further enhancements should have been addressed in another ticket, where it would be easier to review and merge. Some quadratic forms experts to the rescue? :-)


---

Comment by cremona created at 2009-04-17 08:09:55

OK, this is all my fault.  the original patches which fix the typo should be allowed to go ahead.  I will open a different ticket to do the thinks which my patch does, called something like "Move useful algebraic utilities out of the quadratic forms module".

Upshot: merge the first two patches ONLY.  On that basis I have retagged this "positive review".


---

Comment by mabshoff created at 2009-04-19 02:13:27

John,

can you please open another patch for the issues you observed and attach the patch at the new ticket? I will then delete the patch here.

Cheers,

Michael


---

Comment by cremona created at 2009-04-20 10:08:03

Replying to [comment:10 mabshoff]:
> John,
> 
> can you please open another patch for the issues you observed and attach the patch at the new ticket? I will then delete the patch here.

Done at #5834.  The patch there is the same as the 3rd one here (rebased and checked), and it relies on the first two patches here being applied first.  The third patch here can now be deleted.

Next time I feel inspired to do something similar I'll do so in a new ticket in the first place.

> 
> Cheers,
> 
> Michael


---

Comment by mabshoff created at 2009-04-24 09:54:12

Merged both patches in Sage 3.4.2.alpha0.

John: This is touching quadratic forms code, so I am CCing you. You really ought to get rid of the "Oops!" bit when throwing exceptions :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 09:54:12

Resolution: fixed


---

Comment by cremona created at 2009-04-24 10:37:04

Replying to [comment:12 mabshoff]:
> Merged both patches in Sage 3.4.2.alpha0.
> 
> John: This is touching quadratic forms code, so I am CCing you. You really ought to get rid of the "Oops!" bit when throwing exceptions :)
> 
> Cheers,
> 
> Michael

They were not my "oops"s, and I agree with you.  I just did not remove them.  If we do this now with a new ticket/ patch then it will interfere with #5834 but I think I could live with that.


---

Comment by mabshoff created at 2009-04-24 10:49:41

Replying to [comment:13 cremona]:

> They were not my "oops"s, and I agree with you.  I just did not remove them.  If we do this now with a new ticket/ patch then it will interfere with #5834 but I think I could live with that.

Sorry John, I meant to alert Jon Hanke (But I misspelled his name :(). Jon Hanke is supposed to get coverage up to 100% for the quadratic forms code by the end of the month, so I wanted him to be aware of all patches that touch quadratic forms. We might still get #5834 in before that happens, so we will see. So far there is no patch from Jon to merge AFAIK :(

Cheers,

Michael
