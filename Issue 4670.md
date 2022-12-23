# Issue 4670: prime_pi for input ~ 10^10 causes PariError

Issue created by migration from https://trac.sagemath.org/ticket/4670

Original creator: roed

Original creation time: 2008-12-01 16:55:44

Assignee: was

Calling the primepi function on a large pari integer (10^10) causes an error.  The issue is that in sage/libs/pari/gen.pyx the function init_primes casts the input to an unsigned long.  If we don't want to allow initialization with input bigger than this, we should give a better error.


sage: prime_pi(10^10)
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/Users/Roed/Math/sage-3.2/<ipython console> in <module>()

/Users/Roed/Math/sage-3.2/local/lib/python2.5/site-packages/sage/functions/transcendental.pyc in __call__(self, x)
    363             from sage.rings.integer import Integer
    364             pari.init_primes(pari(x)+Integer(1))
--> 365             return ZZ(pari(x).primepi())
    366 
    367     def plot(self, xmin=0, xmax=100, *args, **kwds):

/Users/Roed/Math/sage-3.2/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:37972)()

PariError: impossible assignment I-->S (23)


---

Comment by fwclarke created at 2008-12-02 20:39:43

Note also #3658.


---

Comment by boothby created at 2009-01-15 22:13:13

ohanar is fixing this!


---

Comment by kevin.stueve created at 2010-01-18 00:25:11

Andrew Ohana's optimized Legendre prime_pi fixes this error.  The attached patch adds prime_pi(10**10) to the doctests of Andrew's code.  It may still be desired to give a better error in the PARI implementation.


Kevin Stueve


---

Comment by kevin.stueve created at 2010-01-18 00:25:11

Changing status from new to needs_review.


---

Comment by kevin.stueve created at 2010-01-18 01:42:31

added prime_pi(10**10) doctest


---

Comment by spancratz created at 2010-01-18 03:55:52

Changing status from needs_review to positive_review.


---

Attachment

The patch above includes left overs from another patch.  I'll upload a new one now.


---

Attachment

Only the relevant lines from Kevin's patch


---

Comment by rlm created at 2010-01-19 01:15:42

Resolution: fixed
