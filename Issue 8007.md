# Issue 8007: Speed up generation of random number field elements

Issue created by migration from https://trac.sagemath.org/ticket/8007

Original creator: craigcitro

Original creation time: 2010-01-20 04:50:23

Assignee: davidloeffler

CC:  was boothby spancratz

In the process of looking at #3436, I noticed that generation of random number field elements was slow. I was hoping that speeding it up would make it fast enough that we could use a "generic" algorithm for generating matrices over cyclotomic fields. I did get a *100-150X* speedup for generating random elements of number fields, but amazingly, this *still* wasn't quite fast enough to beat the more "quick and dirty" approaches for cyclotomic matrices. However, I think this code is probably still worth merging.


---

Comment by craigcitro created at 2010-01-20 04:53:00

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-01-20 04:53:00

I should comment that it's actually not too hard to understand why this still isn't fast enough to beat the code on #3436. A large part of the problem is that we still represent elements of number fields by NTL polynomials -- the lion's share of the difference comes down to the fact that we end up doing several copies of data back and forth between NTL `ZZX` objects and GMP/MPIR `mpz_t` and `mpq_t` objects, which adds up fast.


---

Comment by robertwb created at 2010-01-20 09:59:33

Looks good, just needs some fixes due to random number generation changes:


```
	sage -t  devel/sage-main/sage/rings/number_field/number_field.py # 1 doctests failed
	sage -t  devel/sage-main/sage/algebras/quatalg/quaternion_algebra.py # 4 doctests failed
```



---

Comment by robertwb created at 2010-01-20 09:59:33

Changing status from needs_review to needs_work.


---

Comment by craigcitro created at 2010-01-20 19:44:57

Cool, fixed. New patch attached. 

(Amusingly, the `number_field.py` failure was a change I made on purpose: I was putting it there for myself as a reminder to doctest everything, because I was habitually only doctesting that directory ... oops.)


---

Comment by craigcitro created at 2010-01-20 19:44:57

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-02-11 20:45:13

Changing status from needs_review to needs_work.


---

Attachment

Needs to be rebased against 4.3.2...


---

Attachment


---

Comment by craigcitro created at 2010-02-12 20:15:42

Done.


---

Comment by craigcitro created at 2010-02-12 20:15:42

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-02-15 19:54:22

Changing status from needs_review to positive_review.


---

Comment by roed created at 2010-02-15 19:54:22

All tests pass, code looks good.


---

Comment by mvngu created at 2010-02-17 20:43:14

Merged [trac_8007_rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8007/trac_8007_rebase.patch).


---

Comment by mvngu created at 2010-02-17 20:43:14

Resolution: fixed
