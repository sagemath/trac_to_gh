# Issue 2034: {{{__floordiv__}}} should be part of coercion modell

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-02 13:52:56

Assignee: somebody

but it isn't


---

Comment by AlexGhitza created at 2009-07-11 13:19:42

Changing assignee from somebody to robertwb.


---

Comment by AlexGhitza created at 2009-07-11 13:19:42

Changing component from basic arithmetic to coercion.


---

Comment by jdemeyer created at 2016-01-19 16:41:10

New commits:


---

Comment by jdemeyer created at 2016-01-19 16:41:10

Changing status from new to needs_review.


---

Comment by git created at 2016-01-20 12:47:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-01-20 13:18:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2016-01-20 14:22:23

According to the "principle of least surprise", supporting floordiv for finite fields looks suspicious

```
sage: ZZ(5) // ZZ(3)
1
sage: GF(7)(5) // GF(7)(3)
4
```

If this is just an alias of division, why do we need it?


---

Comment by jdemeyer created at 2016-01-20 14:35:30

Replying to [comment:16 vdelecroix]:
> According to the "principle of least surprise", supporting floordiv for finite fields looks suspicious

That's outside the scope of this ticket. This ticket only implements coercion for `__floordiv__`, it doesn't otherwise change the semantics of floor division. There shouldn't be anything controversial in this ticket.


---

Comment by vdelecroix created at 2016-01-20 15:01:49

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2016-01-20 15:01:49

All right. Hope this will be fixed with #15260.


---

Comment by vbraun created at 2016-01-23 20:42:41

Resolution: fixed
