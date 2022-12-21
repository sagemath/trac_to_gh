# Issue 6397: implement general Newton's method root finding for power series rings

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-24 18:13:21

Assignee: malb

CC:  robertwb was

Keywords: power series root newton method

Extracting a square root of a power series is implemented in `power_series_ring_element.pyx`.  Could we have the more general "improving a root of a polynomial" Newton's method?

My use case is calculating Puiseaux expansions around points of algebraic curves.


---

Comment by ncalexan created at 2009-06-24 20:06:16

Here's a stand-alone implementation that needs to be plugged into the hell that is `polynomial.roots()`.
