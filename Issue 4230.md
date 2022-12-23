# Issue 4230: implement arbitrary precision Bessel Y function

Issue created by migration from https://trac.sagemath.org/ticket/4230

Original creator: AlexGhitza

Original creation time: 2008-10-01 10:09:21

Assignee: burcin

CC:  kcrisman benjaminfjones

At the moment, Sage uses Maxima to compute the Bessel Y function.  This is slow and works only with the default 53 bits of precision.  It would be fairly easy to implement this:

 * for integer values of the order nu, use the mpfr yn function
 * for non-integer values of nu, use the formula $Y_nu(z) = (J_nu(z)*cos(nu*pi) - J_{-nu}(z))/sin(nu*pi)$, where J is the Bessel J function.



---

Comment by ddrake created at 2008-10-07 06:21:37

It would also be nice to be able to evaluate Bessel functions with complex, or at least purely imaginary, arguments.


---

Comment by AlexGhitza created at 2008-10-07 11:42:25

See #3426 (and review it!) for the Bessel functions other than Y.  The code computes values at arbitrary complex coefficients.


---

Comment by ddrake created at 2009-10-09 04:06:32

Now that mpmath is included in Sage, why not just use mpmath's Bessel functions? http://mpmath.googlecode.com/svn/trunk/doc/build/functions/bessel.html

They seem to be very well-implemented, work to arbitrary precision, take complex arguments, and so on. Is this a good idea?


---

Comment by kcrisman created at 2013-01-03 15:32:50

This would most likely be fixed by #4102.


---

Comment by benjaminfjones created at 2013-01-03 23:09:14

Yep, I'll add a related doctest in #4102 to address arbitrary precision numerical evaluation for bessel_Y.


---

Comment by kcrisman created at 2013-02-08 17:36:01

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-02-08 17:36:01

Confirmed that this is doctested there.


---

Comment by kcrisman created at 2013-02-08 17:37:59

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-17 20:10:19

Resolution: duplicate
