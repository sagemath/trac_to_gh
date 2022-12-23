# Issue 5658: Efficiency improvement in generic order_from_multiple()

Issue created by migration from https://trac.sagemath.org/ticket/5658

Original creator: cremona

Original creation time: 2009-04-01 15:04:57

Assignee: tbd

CC:  rhinton

Keywords: generic group order

Ryan Hinton pointed out that for groups of prime order n every non-identity element has order n.  The current implementation of order_from_multiple() computes `g^n` twice when g is not the identity and n is prime.

The attached patch avoids this: for each prime p dividing the given multiple M of the order, we avoid the last multiplication/powering by p, so there is a saving whenever the p-exponent of the order is maximal.

In an example where the order is `2^1279-1` (a Mersenne prime) the times was reduced from 100ms to 70ms.


---

Attachment

based on 3.4.1.alpha0


---

Comment by rhinton created at 2009-04-01 15:41:13

Patch applies cleanly and passes doctests.  I don't understand what `val_unit` does, so I am unsure whether I'm qualified to give a positive review.


---

Comment by cremona created at 2009-04-01 15:49:50

Thanks for the fast review.

Here is what val_unit does.  Given a nonzero integer or rational n and a prime p, you can write n uniquely as `n = m*p^e` where m is not divisible by p (if rational, neither the numerator nor the denominator of m is divisible by p).   We call e the valuation of m at p  (which can be obtained on its own by n.valuation(p)) and m the "unit" part of n at p (which can be obtained on its own by n.prime_to_m_part(p)).  Using val_unit() gives these together which is more efficient as they are computed together.

It's an operation frequently needed in number theory!

I added "needs review" which I forgot to do earlier.  If you are happy with val_unit() you can change that, or I can hit someone else to take a look.


---

Comment by rhinton created at 2009-04-01 16:19:42

Sounds good to me!


---

Comment by mabshoff created at 2009-04-02 00:06:19

Merged in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-02 00:06:19

Resolution: fixed
