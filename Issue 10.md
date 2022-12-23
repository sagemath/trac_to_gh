# Issue 10: Cython fixes in Tate algebras

CC:  roed jdemeyer

I address Jeroen's comments in ticket #26195

Issue created by migration from https://trac.sagemath.org/ticket/26807




---

Changing status from new to needs_review.


---

Branch pushed to git repo; I updated commit sha1. New commits:


---

You misinterpreted Jeroen's comment about `cpdef _mul_`: it shouldn't be changed to `cdef` but instead you need to add `cpdef _mul_` to `tate_algebra_element.pxd`.


---

Why is it better to have `cpdef _mul_` than `cdef _mul_`?

I noticed that `_mul_` is `cdef` in `MonoidElement` but `cpdef` in `RingElement` but didn't understand why.


---

It's better because it allows Python subclasses to override `_mul_` and have it picked up by the coercion system.  Moreover, if you use `cdef` in a superclass but override it with `cpdef` (and possibly also `def`), there was a nasty bug in Cython that caused segfaults because Cython tried to call a non-existent function.  That's the source of the warning that Jeroen referred to.

I haven't looked at `MonoidElement`, but I would guess that the `cdef` `_mul_` there should be changed to `cpdef`.


---

Branch pushed to git repo; I updated commit sha1. New commits:


---

Changing status from needs_review to needs_work.


---

This should be `cpdef _floordiv_` (which should then also be declared the `.pxd` file):

```
cdef _floordiv_(self, other):
```


Also, fill in your name as Author.


---

In `_cmp_c`, shouldn't we be worried about potential overflow here?

```
cdef int c = other._valuation_c() - self._valuation_c()
```

The result of `_valuation_c` is a `long` and you are downcasting that to `int`.

The easiest solution is returning a `long` in `_cmp_c`.


---

Branch pushed to git repo; I updated commit sha1. New commits:


---

Changing status from needs_work to needs_review.


---

Done.


---

Branch pushed to git repo; I updated commit sha1. New commits:


---

Jeroen, David, any other comments here? If not, I will flip this to positive.


---

Changing status from needs_review to positive_review.


---

Thanks; I'm happy with the changes.


---

Resolution: fixed


---

This tickets were closed as fixed after the Sage 8.5 release.
