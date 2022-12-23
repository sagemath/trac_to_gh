# Issue 8135: prime_pi approximation involving zeta zeros

Issue created by migration from https://trac.sagemath.org/ticket/8135

Original creator: kevin.stueve

Original creation time: 2010-01-31 06:20:29

Assignee: Kevin Stueve

CC:  leif

Keywords: prime counting function Riemann zeta zeros

Get an analytic approximation to prime_pi, the prime counting function that uses the nontrivial zeros of the Riemann zeta function.


---

Comment by kevin.stueve created at 2010-01-31 06:43:42

Below is a conversation between myself and Tomas Oliviera e Silva (Universidade de Aveiro, Portugal).  I have included only the content relevant to this ticket in particular (more of the conversation is at [http://trac.sagemath.org/sage_trac/ticket/7013#comment:42](http://trac.sagemath.org/sage_trac/ticket/7013#comment:42)).

Kevin Stueve:

I am currently researching the error of Riemann's exact formula for
pi(x) in the form of equation 13 at
http://mathworld.wolfram.com/RiemannPrimeCountingFunction.html.  I am
contemplating various ways of compressing a table of values of the
prime counting function.  Because storage cost is a major bottleneck,
even a savings of 10% or less would be worth the effort.

Are you willing to release the code you used for your estimates of the
prime counting function at http://www.ieeta.pt/~tos/primes.html#e
under a GPL compatible license?

Tomas Oliviera e Silva (TOS):

The equation 13 you mentioned is PROBABLY wrong: check Andrey V. Kulsha'
post of 11/18/2008 entitled "On the explicit formula for the Prime-counting
function pi(x)" on the NMBRTHRY`@`LISTSERV.NODAK.EDU list. To me, it seems
far better to compress the pi(x) data using simply pi(x)=li(x)-e(x). Instead
of storing pi(x) you would store the (positive) value of e(x) rounded to the
nearest integer. Note that li(x) can be computed easily and that e(x) should
be of the order of sqrt(x). Replacing li(x) by R(x) would not help much,
because the error term could be either positive or negative (one more bit).
Using a few zeros of the zeta function could reduce the error term, but my
experience is that it would take much more time to compute the approximation
(it would be necessary to evaluate $li(x^rho)$ accurately, and also
pi(sqrt(x)), pi(cbrt(x)), etc.).

Kevin Stueve:

I am very interested in what is possible with the Riemann correction
terms.  Even if they are not reasonable for use in a production prime
counting function, I would love to find a fast implementation I can
use for research (and for Sage) without implementing it myself.
Implementing it myself would be very educational (I suppose I might
start with the Gram series), but it could consume a great deal of my
time that could be spent elsewhere.  Because I started out as a
computer science major, I see the problem of how much a table of
values of the prime counting function can be compressed and quickly
retrieved in theory as a problem worthy in its own right.

TOS:

Would you consider using the gmp and mprf packages to do the floating
point computations? I can adapt my code to compute Riemman's formula for
pi(x) using them --- it would contain calls to pi(x) itself, which I would
not implement, to compute pi(sqrt(x)), pi(cbrt(x)), etc.

Kevin Stueve:

Yes.  I would consider using gmp and mprf.  I could compute the
recursive pi(sqrt(x)) calls etc.

Tomas Oliviera e Silva:
Here goes a simple implementation of Riemann's formula in pari-gp.

Thanks Tomas!  

Kevin Stueve


---

Comment by kevin.stueve created at 2010-01-31 06:54:56

Sorry about the formatting error: 

$li(x<sup>rho</sup>)$ accurately, and also pi(sqrt(x)), pi(cbrt(x)), etc.

This formatting error is my fault.


---

Comment by kevin.stueve created at 2010-01-31 07:07:09

Sincere apologies for misspelling Tomás Oliveira e Silva's name in the above comment.

Editing recent comments on Sagetrac is a REALLY missing feature.

Also, it looks like a mailing list name beginning with NMBRTHRY, followed by an at sign, and ending in LISTSERV.NODAK.EDU was stripped by the trac server for anti-spam purposes.


---

Comment by kevin.stueve created at 2010-01-31 07:19:07

pari-gp code from Tomás Oliveira e Silva


---

Attachment


---

Attachment

rewrote TOS's riemann_pi.gp in python (paste into cell)


---

Comment by kevin.stueve created at 2010-02-04 07:02:21

Attached TOS's riemann_pi.gp converted to Python.  It would be AWESOME to see this code written in optimized multithreaded C (or assembly), or at least Cython.  Thanks again to Tomás Oliveira e Silva for releasing this code!

Kevin Stueve


---

Attachment

Rewrote periodic terms in C with real and imaginary components calculated individually
