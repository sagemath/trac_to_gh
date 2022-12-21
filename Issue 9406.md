# Issue 9406: Multi-dimensional polynomial fit

Issue created by migration from Trac.

Original creator: olazo

Original creation time: 2010-07-02 03:06:24

Assignee: olazo

CC:  ncohen

Keywords: polynomial,fit

At this point, the only way (to my knowledge) to use the least-squares algorithm within sage is trough numpy.polyfit, which is limited to 1-dimensional polynomials. It takes a list of 2-tuples which are interpreted as points of the form (x,P). And returns an array of coefficients of the polynomial with the specified degree.

I've written a sage script that works for arbitrary dimensions, taking a list of N-tuples, and returns a polynomial (as a sage-expression) with the specified degree for each dimension.

I'll post this as soon as I gain access to off-line sage (at this point I am stuck without it).

This would bring us closer to Mathematica's mighty Fit:

[http://reference.wolfram.com/mathematica/ref/Fit.html](http://reference.wolfram.com/mathematica/ref/Fit.html)


---

Comment by olazo created at 2010-07-15 19:58:40

It seems that a much more powerful tool than the one I was about to submit is already included in sage: find_fit. Since find_fit already does everything I proposed, I advice this ticket to be closed.


---

Comment by rlm created at 2010-07-18 19:12:46

Resolution: worksforme
