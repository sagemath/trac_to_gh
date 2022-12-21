# Issue 269: add floordiv, mod, invert, pow to arithmetic architecture (at least in RingElement)

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-02-17 22:43:30

Assignee: somebody

CC:  vdelecroix

So far we only have add, sub, neg, various versions of mul, and div.

We also need floordiv, mod, invert, pow.

These would be very useful in p-adics, and need to happen for other reasons too.


---

Comment by was created at 2007-08-18 09:56:53

Changing type from defect to enhancement.


---

Comment by cwitty created at 2007-10-06 19:46:11

Replying to [ticket:269 dmharvey]:
> So far we only have add, sub, neg, various versions of mul, and div.
> 
> We also need floordiv, mod, invert, pow.
> 
> These would be very useful in p-adics, and need to happen for other reasons too.

Is exact division (that is, division where the caller knows that there is no remainder) common enough to belong here?  (There's an implementation for Integer already, where the method is called divide_knowing_divisible_by() and calls mpz_divexact().)


---

Comment by jbmohler created at 2008-03-19 12:08:08

Replying to [comment:3 cwitty]:
> Replying to [ticket:269 dmharvey]:
> > So far we only have add, sub, neg, various versions of mul, and div.
> > 
> > We also need floordiv, mod, invert, pow.
> > 
> > These would be very useful in p-adics, and need to happen for other reasons too.
> 
> Is exact division (that is, division where the caller knows that there is no remainder) common enough to belong here?  (There's an implementation for Integer already, where the method is called divide_knowing_divisible_by() and calls mpz_divexact().)

I definitely think that exact division should be included in the arithmetic architecture.  This is not because it's common, but because there is a bunch of daft coercion code in most !__floordiv!__ implementations.  All this needs to be fixed and the fix is a common boiler-plate prefix on these functions.  Or, a much better alternative is to include it in the arithmetic hierarchy and write that boilerplate coercion once at the head of the tree.

I think that gcd (and maybe xgcd) should also be on this list.


---

Comment by jbmohler created at 2008-03-19 12:10:13

Oh, and quo_rem should be here too -- #383


---

Comment by jdemeyer created at 2016-01-19 17:40:17

Changing component from basic arithmetic to coercion.


---

Comment by vdelecroix created at 2016-01-22 12:10:51

Jeroen, what is the rationale for

```
cpdef _mod_(self, Element other)
```

instead of

```
cpdef Element _mod_(self, Element other)
```

In a situtation like `e1._mod_(e2)._add_(e3)` Cython would be happier. No?


---

Comment by jdemeyer created at 2016-01-22 12:37:19

Replying to [comment:19 vdelecroix]:
> In a situtation like `e1._mod_(e2)._add_(e3)` Cython would be happier. No?

Sure, but I don't know how common that is.

I want to avoid unneeded checking. If you do something like

```
cpdef Element _foo_(self, other):
    x = ...
    return x
```

then Cython will add a check that `x` is actually of type `Element`. I think (but this is just a wild guess) that the slow-down of these extra checks does not justify the few cases where the check might improve performance.


---

Comment by jdemeyer created at 2016-01-22 13:24:36

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-01-22 13:24:36

New commits:


---

Comment by vdelecroix created at 2016-03-11 20:39:49

Does not apply on last beta.


---

Comment by vdelecroix created at 2016-03-11 20:39:49

Changing status from needs_review to needs_work.


---

Comment by git created at 2016-05-31 15:54:38

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by jdemeyer created at 2016-05-31 15:56:37

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2016-05-31 16:03:14

About [comment:19 comment:19] I guess that the rationale is that we should follow what was done until now. If you want to change the `cpdef` methods without declaring them as `Element` or `ModuleElement` or whatever I guess you should open a new ticket.


---

Comment by git created at 2016-06-05 09:08:51

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2016-06-14 11:35:51

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2016-06-14 11:43:13

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by vdelecroix created at 2016-07-13 15:09:26

Please, add doctests for `__mod__` in `sage.rings.finite_rings.integer_mod`.


---

Comment by vdelecroix created at 2016-07-13 15:09:26

Changing status from needs_review to needs_work.


---

Comment by git created at 2016-07-14 16:37:52

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-07-14 16:54:05

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by jdemeyer created at 2016-07-14 16:55:27

Changing status from needs_work to needs_review.


---

Comment by git created at 2016-07-15 09:00:01

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2016-07-25 01:29:28

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2016-07-25 07:38:50

Thanks!


---

Comment by vbraun created at 2016-07-27 20:24:59

Resolution: fixed
