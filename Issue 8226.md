# Issue 8226: Elementary divisors for non PIDs

Issue created by migration from Trac.

Original creator: mraum

Original creation time: 2010-02-10 08:48:32

Assignee: davidloeffler

Keywords: elementary divisors

Over maximal orders O in number fields K the elementary divisors provide a complete system of invariants for in matrices GL_n(K). Here the elementary divisors are the ideals e_i = d_i / d_{i-1} where d_i are the determinantal divisors. This patch provides the possibility to compute these elementary divisors.


---

Attachment


---

Comment by mraum created at 2010-02-10 08:50:39

Changing status from new to needs_review.


---

Comment by cremona created at 2010-02-21 14:05:59

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-02-21 14:05:59

There looks like a typo on line 6293.


---

Comment by mraum created at 2010-02-21 14:19:47

Replying to [comment:2 cremona]:
> There looks like a typo on line 6293.

Acutally no. The statement "raise" raises the last exception one has cached and this is exactly what I want. If the SMNF can't be obtainted by means of the algorithm implemented at the moment - and this is indicated by an ArithmeticError - I check whether I can do it diffently. If not the original ArithmeticError with its trac back is the most useful error message.
Do you think diffently about this?

The best would be to check whether a ring is a PID or not. Then decide on the algorithm to use. But this isn't even implemented for ZZ, so no chance to do it.


---

Comment by davidloeffler created at 2010-06-29 11:34:22

I think mraum's point is a fair one: re-raising the original error will generally be more helpful than raising a new one (e.g. it might give an explicit example of a non-principal ideal in the base ring). 

But I don't like the idea that `smith_form` will sometimes return elements and sometimes ideals. I totally agree that we should have the functionality to compute these elementary divisor ideals, but it should be a separate function, with `smith_form` raising an error when the elementary divisors aren't principal. Also, Pari has a fast algorithm for this problem, so we should use that rather than devising our own; see #4742.
