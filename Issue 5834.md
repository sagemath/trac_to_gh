# Issue 5834: Improvements to quadratic_forms/extras/py

Issue created by migration from https://trac.sagemath.org/ticket/5834

Original creator: cremona

Original creation time: 2009-04-20 10:04:00

Assignee: justin

CC:  tornaria jonhanke

Keywords: quadratic forms

As first raised in #5627, concerning quadratic_forms/extras.py (which contains various utilities written for use in various places in thw quadratic_forms module):

I have added a patch after looking carefully at this, which does the following:

   1. I removed hilbert_symbol_rational(), making a trivial change to hilbert_symbol() so that it already works on rationals. I think this will useful outside the quadratic forms module.

   2. I moved `IsPadicSquare()` to a member function for rationals, so you now say r.is_padic_square(p) instead of `IsPadicSquare(r,p)`, while at the same time making the function simpler and cleaner. I think this will also be useful outside the quadratic forms module.

   3. I removed random_int_upto(n) since it does the same as ZZ.random_element(n).

   4. I simplified quadratic_nonresidue() (and changed its name to least_quadratic_nonresidue()) -- by putting in three simple tests for when the answer is 2, 3 or 5 the loop is avoided in 7/8 of the cases. I also changed the loop to "for r in xsrange(7,p)", in response to the discussion earlier on this ticket: adding the x gives an iterator instead of making the whole list and iterating through it (bad for large p!), and adding the s makes the iterator yield Sage integers (so it works for p too large to fit into a python int). I also added an is_prime() test on p, since otherwise if you give it a huge composite number there seemed to be a danger that it would run through a loop of length p before realising that the input was invalid. 

    5. I simplified sgn().

All tests in sage/quadratic_forms pass, as do those in arith.py and rational.py which were also touched.

The patch needs to be applied to (at least) 3.4.1.rc3 + the two patches at #5627.


---

Comment by mabshoff created at 2009-04-24 10:52:26

Gonzalo, Jon,

this is your area of expertise. Can either one of you review?

And by the way: "3. I removed random_int_upto(n) since it does the same as ZZ.random_element(n)." is #5888. As it turned out that if you wanted some random number larger than 2^53 you ended up with loads of integers that had a common divisor of 2^47 causing some trouble to Bill Hart today when he looked at the HNF code in Sage to compare some code he has written in FLINT.

Cheers,

Michael


---

Comment by cremona created at 2009-04-24 10:58:01

Replying to [comment:2 mabshoff]:
> Gonzalo, Jon,
> 
> this is your area of expertise. Can either one of you review?
> 
> And by the way: "3. I removed random_int_upto(n) since it does the same as ZZ.random_element(n)." is #5888. As it turned out that if you wanted some random number larger than 2^53 you ended up with loads of integers that had a common divisor of 2^47 causing some trouble to Bill Hart today when he looked at the HNF code in Sage to compare some code he has written in FLINT.
> 
> Cheers,
> 
> Michael

Moral: do not reinvent the wheel, especially if your version is square.  Use the wheels provided!


---

Comment by cremona created at 2009-04-27 09:28:38

Replaces earlier patch, based on 3.4.2.alpha0


---

Attachment

trac_5834-rebase.patch is rebased to 3.4.2.alpha0.  (Totally trivial, only a couple of whitespace changes).


---

Comment by jonhanke created at 2009-05-02 00:00:28

This patch looks good, and I recommend it be approved.  

A few comments:
    - There is a `quadratic_nonresidue()` routine in `integer_mod_ring.py` which might benefit from using the `least_quadratic_residue()` routine.
    - What is the procedure for adding functionality present for rationals to integers?  It might be useful for both integer and rational types to call the `is_padic_square()` method without explicit rational coercion.

Also, in an attached patch I made some very minor changes to the quadratic_form code where this replaced previous functionality.


---

Comment by jonhanke created at 2009-05-02 00:01:33

Very minor changed to the rebase patch above


---

Attachment

Thanks, Jon.  Your small extra patch looks ok to me but I did not try applying it.

I had not noticed the other quadratic_nonresidue() routine in integer_mod_ring.py!

On your other question, it seems rather random.  I'm not sure what we can do about that.  In some other languages, if there was a function which applied to rationals and you give it an integer, the compiler would insert the necessary coercion.  But cannot do that (it would involve making integer a subclass of rational, which does not seem a good idea!)


---

Comment by mabshoff created at 2009-05-04 18:15:24

Resolution: fixed


---

Comment by mabshoff created at 2009-05-04 18:15:24

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
