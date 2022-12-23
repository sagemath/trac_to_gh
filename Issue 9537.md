# Issue 9537: trial_division in Sage is really slow

Issue created by migration from https://trac.sagemath.org/ticket/9537

Original creator: was

Original creation time: 2010-07-18 14:31:40

Assignee: AlexGhitza

See my talk:
  *  http://wiki.sagemath.org/days24/schedule?action=AttachFile&do=view&target=stein-cython.pdf
  * http://sagenb.org/home/pub/2256/

Basically, this sucks:

```
sage: n = 20110000038209
sage: timeit('trial_division(n)')
125 loops, best of 3: 2.75 ms per loop
```


Even in pure python one can easily implement this so it runs in about 650microseconds.  In C, it takes only 6 microseconds!


---

Comment by was created at 2010-07-18 19:22:32

Changing status from new to needs_review.


---

Comment by was created at 2010-07-18 19:44:39

good.


---

Attachment


---

Comment by spancratz created at 2010-07-18 20:13:31

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 09:21:50

Resolution: fixed
