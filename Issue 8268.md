# Issue 8268: Improve speed of Christoffel word construction

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-02-15 00:15:17

Assignee: slabbe

CC:  abmasse

This patch adds a new implementation for construction of Christoffel words using continued fraction :


```
sage: %timeit words.ChristoffelWord(5, 9, algorithm='linear')
625 loops, best of 3: 67.7 µs per loop
sage: %timeit words.ChristoffelWord(5, 9, algorithm='cf')
625 loops, best of 3: 309 µs per loop
```


For large words, it is much faster than the actual implementation.


```
sage: %timeit words.ChristoffelWord(500, 90001, algorithm='linear')
5 loops, best of 3: 111 ms per loop
sage: %timeit words.ChristoffelWord(500, 90001, algorithm='cf')
125 loops, best of 3: 4 ms per loop
```



---

Attachment


---

Comment by slabbe created at 2010-02-15 00:21:53

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-02-24 01:53:39

I tested the improved function. It is indeed much faster, especially when the two prime numbers are big. The code makes sense, all tests passed, and I tried also other values with very big prime numbers: no problem. The doc builds fine too.

I made very minor changes (typos, punctuation, etc.). Positive review.


---

Comment by abmasse created at 2010-02-24 01:55:26

Changing status from needs_review to positive_review.


---

Comment by abmasse created at 2010-02-24 01:55:26

Changing keywords from "" to "christoffel words".


---

Comment by abmasse created at 2010-02-24 01:59:39

Sorry, forgot two small things, uploading a new patch in a few minutes.


---

Comment by abmasse created at 2010-02-24 01:59:39

Changing status from positive_review to needs_work.


---

Comment by abmasse created at 2010-02-24 02:07:53

Changing status from needs_work to needs_review.


---

Comment by abmasse created at 2010-02-24 02:08:43

Minor change -- apply on top


---

Comment by abmasse created at 2010-02-24 02:09:36

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by mvngu created at 2010-03-02 21:30:05

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 21:30:05

Merged in this order:

 1. [trac_8268_speed_up_Christoffel-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8268/trac_8268_speed_up_Christoffel-sl.patch)
 1. [trac_8268_review-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8268/trac_8268_review-abm.patch)
