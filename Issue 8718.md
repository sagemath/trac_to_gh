# Issue 8718: Polynomial.apply_map()

Issue created by migration from Trac.

Original creator: mmezzarobba

Original creation time: 2010-04-19 20:15:46

Assignee: AlexGhitza

CC:  dkrenn

Keywords: polynomial, map

Computing, for instance, the complex conjugate of a polynomial currently requires going through its list or dictionary representation. Polynomials could provide a method similar to Matrix.apply_map() to make this kind of computations easier.


---

Attachment


---

Comment by mmezzarobba created at 2010-05-17 19:57:05

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2010-05-17 19:57:05

The attached patch adds naive implementations of apply_map() and of a second similar method, map_coefficients(), modeled after that of multivariate polynomials.

Note that I have as good as no experience with Python or Sage development—so sorry for any newbie errors... and please review carefully! :-)


---

Comment by jason created at 2010-05-18 02:07:39

One suggestion---the names of the new functions do not seem to indicate to me that they only operate on the nonzero coefficients, so it would be hard for me to remember what the difference between map_coefficients and apply_map is.

How about just adding an argument to apply_map:

p.apply_map(nonzero_only=True)

or something like that?


---

Comment by mmezzarobba created at 2010-05-18 07:05:57

The idea was to stay compatible with ``MPolynomial.map_coefficients()``, which operates on nonzero coefficients.  Perhaps we could remove ``apply_map()`` rather that ``map_coefficients()``, and add an option to make ``map_coefficients()`` map over zero coefficients too. (Ignoring them by default seems sensible, since (i) there is really no mathematical difference between zeros below and above the leading coefficient, and (ii) the functions one will typically pass to ``map_coefficients()`` are ring homomorphisms.)

What do you think?


---

Comment by jason created at 2010-05-18 15:28:57

That sounds cleaner to me.  I'm likely not to use this function very much, so I shouldn't be the last authority on it, though.


---

Comment by davidloeffler created at 2010-09-27 17:58:33

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-09-27 17:58:33

Any progress here? I agree with Jason's contention that having both `apply_map` and `map_coefficients` is less than ideal, so I suggest that we put this back to "needs work" pending a patch that implements this.


---

Comment by dkrenn created at 2011-11-02 16:38:16

I would suggest to map only non-zero coefficients because of the following reason: When mapping all (really all) zeros to a non-zero, the result is not a polynomial any more, so one would have to restrict that. But how should this restriction look like? A good restriction strategy (strategy which coefficients to choose and apply the map on) should be generalizable to the multivariate case. E.g. restriction by degree (i.e. only change the coefficients with indizes 0 to degree) could work in the univariate case, but does not work for multivariate polynomials.

If one really wants to map 0 to a non-zero, then this should be done somewhere else, i.e., not in `map_coefficients`


---

Comment by saraedum created at 2012-02-06 20:51:03

Changing status from needs_work to needs_review.


---

Comment by saraedum created at 2012-02-06 20:51:03

I agree that mapping 0 to non-zero should not be a part of map_coefficients().

I rewrote the patch to only contain map_coefficients() for polynomial elements.

Was there any reason for distinguishing between polynomial_element and polynomial_element_generic? I removed the distinction and it turned out that this implementation is even faster for the example polynomials.


---

Comment by saraedum created at 2012-02-06 20:51:30

adds map_coefficients()


---

Attachment

apply trac_8718.patch


---

Comment by mmezzarobba created at 2012-02-07 08:04:03

Thanks for taking care of that! (And shame on me that I didn't!)

As for the distinction  between polynomial_element and polynomial_element_generic, it may indeed have been a speed issue, but I can't remember the details. Anyway, if the current version does the job, I'm fine with it.

[I'm not sure what the rules are here: am I allowed to review the new version of the patch though being its initial author?]


---

Comment by saraedum created at 2012-02-08 18:16:49

> [I'm not sure what the rules are here: am I allowed to review the new version of the patch though being its initial author?]

Yes, in my experience this is ok and actually happens frequently.


---

Comment by dkrenn created at 2012-02-09 11:05:18

Changing status from needs_review to needs_work.


---

Comment by dkrenn created at 2012-02-09 11:05:18

In #11981 the map_coefficients of a multivariate polynomial was adapted to change the base ring of the coefficients. I think we should also do this here for this function, since the two should have the same behavior.


---

Comment by saraedum created at 2012-02-09 11:12:33

True. I wanted to push this to a later ticket but we can also talk about this here.

I wonder if this "new base ring" should default to the codomain of f (if the function is actually a sage 'Map'). For me this has always been what I wanted. Any opinions on that?


---

Comment by saraedum created at 2012-02-09 11:12:33

Changing status from needs_work to needs_info.


---

Comment by dkrenn created at 2012-02-10 12:49:49

Replying to [comment:12 saraedum]:
> I wonder if this "new base ring" should default to the codomain of f (if the function is actually a sage 'Map'). For me this has always been what I wanted. Any opinions on that?

That is a good idea, we should implement that. So the strategy would be the following: If a new base ring is given, then we use it, otherwise, we check if the function knowns its codomain and if yes use it, otherwise we do not change the base ring.


---

Comment by saraedum created at 2012-02-10 14:27:48

Ok. I already have that implemented. Just need to add some more doctests and upload it.


---

Comment by saraedum created at 2012-02-19 17:43:36

consider the codomain in map_coefficients for univariate polynomials


---

Attachment

consider the codomain in map_coefficients for multivariate polynomials


---

Comment by saraedum created at 2012-02-19 17:45:43

Changing status from needs_info to needs_review.


---

Comment by dkrenn created at 2012-02-20 18:51:09

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-02-27 11:19:40

Resolution: fixed
