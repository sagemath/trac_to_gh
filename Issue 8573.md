# Issue 8573: prod(primes(190)).divisors() crashes

Issue created by migration from https://trac.sagemath.org/ticket/8573

Original creator: asdjughewou9474388

Original creation time: 2010-03-21 21:31:02

Assignee: tbd

Keywords: product primes 190

Exactly what the title says...The divisors of the product of all primes under 190 crashes sage.

The number has about 74 digits I believe, and finding the divisors of a similar 74 digit prime works.

I believe the crash is due to the fact that the number that comes out of prod(primes(190)) has over 4 million divisors.

The I probably selected the wrong component, by the way, I chose factorization, but really I'm talking about divisors.


---

Comment by asdjughewou9474388 created at 2010-03-21 21:31:38

Changing keywords from "product primes 190" to "product primes 190 divisors".


---

Comment by mmezzarobba created at 2014-02-02 11:15:40

It now (6.1) fails with a `MemoryError`, which looks reasonable to me.


---

Comment by mmezzarobba created at 2014-02-02 11:15:40

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-02-03 10:17:33

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2014-02-03 10:30:28

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2014-02-03 10:32:35

Changing keywords from "product primes 190 divisors" to "integer divisors".


---

Comment by jdemeyer created at 2014-02-03 10:32:35

Changing component from factorization to basic arithmetic.


---

Comment by jdemeyer created at 2014-02-03 14:25:00

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2014-02-05 09:33:59

New commits:


---

Comment by rws created at 2014-03-10 10:12:55

Rebased on 6.2.beta3. Tests OK --long in rings/. Seems to be an uncomplicated change.
----
New commits:


---

Comment by rws created at 2014-03-10 10:12:55

Changing status from needs_review to positive_review.


---

Comment by git created at 2014-03-12 08:01:36

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by git created at 2014-03-12 08:01:36

Changing status from positive_review to needs_review.


---

Comment by jdemeyer created at 2014-03-12 10:31:55

Why change the branch all the time?
----
New commits:


---

Comment by jdemeyer created at 2014-03-12 10:31:55

Changing status from needs_review to positive_review.


---

Comment by rws created at 2014-03-12 10:56:53

Replying to [comment:13 jdemeyer]:
> Why change the branch all the time?

https://groups.google.com/forum/#!topic/sage-devel/sTLT83d1g14


---

Comment by jdemeyer created at 2014-03-12 12:33:40

In this ticket, you made no changes, so there is no reason at all to commit/push anything. I'm not complaining about changing the branch, I am complaining about changing the branch _without making any changes_.


---

Comment by vbraun created at 2014-03-13 02:38:45

Resolution: fixed
