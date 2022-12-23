# Issue 7812: Compute Bell numbers using mpmath by default (instead of GAP)

Issue created by migration from https://trac.sagemath.org/ticket/7812

Original creator: jbandlow

Original creation time: 2010-01-02 02:41:55

Assignee: sage-combinat

CC:  jbandlow ncohen

Keywords: bell numbers

Fredrick Johansson discusses [here](http://fredrik-j.blogspot.com/2009/03/computing-generalized-bell-numbers.html) his implementation of generalized Bell numbers in mpmath. I've verified that this function is present in the version of mpmath shipped with sage 4.3. Benchmarks show it is faster than GAP (currently used by sage) and even mathematica.  This should be very easy to wrap.


---

Comment by tscrim created at 2013-03-28 21:39:17

I've exposed (wrapped) mpmath's `bell()` in #10170.


---

Comment by tscrim created at 2013-03-28 21:39:17

Changing status from new to needs_review.


---

Comment by bsalisbury1 created at 2013-05-01 19:39:14

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-03 08:03:01

Resolution: duplicate
