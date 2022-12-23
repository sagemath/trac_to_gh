# Issue 6827: [with patch, needs review] probability distributions doctests + general discrete distribution

Issue created by migration from https://trac.sagemath.org/ticket/6827

Original creator: carlohamalainen

Original creation time: 2009-08-26 08:28:09

Assignee: mhampton

This patch attends to sage/gsl/probability_distribution.pyx:

- 100% doctest coverage (previously this file had nodoctest)

- fixed formatting (all indents now 4 spaces).

- ReST docstring formatting.

- One extra class: general discrete distributions (I think that #6662 should be marked as invalid since the code there fits better here).

- valgrind ok

- probability_distribution.pyx added to the reference manual under Probability.



---

Attachment


---

Attachment

Looks good to me.  I added a one character change to get the docs to build without warning.  Both patches should be applied.

It would probably be good to factor each of the RealDistributions out into their own classes so we don't have to have the massive if/elif/else statements.  It might be a good easy project if someone is working on stats stuff this fall.


---

Comment by mvngu created at 2009-09-09 10:39:00

Resolution: fixed


---

Comment by mvngu created at 2009-09-09 10:39:00

Merged patches in this order:

 1. `probability_distribution.patch`
 1. `trac_6827_review.patch`
