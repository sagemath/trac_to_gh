# Issue 9776: include more rings in random testing

Issue created by migration from Trac.

Original creator: niles

Original creation time: 2010-08-21 19:47:56

Assignee: AlexGhitza

CC:  tscrim slelievre @kliem

Keywords: random testing, rings

p-adics should be included, perhaps at "level 0"?

The following "level 1" rings are not included in `sage.rings.tests`:

 * power series rings

 * Laurent series rings

 * multivariate power series rings (implemented in #1956)

 * infinite polynomial rings

Also, it's not clear that "level n" testing occurs for `n > 1`; e.g. multivariate polynomial ring in 3 variables over Laurent series ring over finite field of size 29, etc.

Quotient rings are also not included, but should be.  There are probably more to be included than this list indicates.


---

Comment by chapoton created at 2021-08-11 14:34:05

Here is a branch.

But is this still pertinent ?
----
New commits:


---

Comment by chapoton created at 2021-08-11 14:34:05

Changing status from new to needs_review.


---

Comment by chapoton created at 2021-08-19 16:06:49

any opinion on the pertinence ?


---

Comment by mjo created at 2021-08-19 23:34:09

Is this doctest checking the right function?


```patch
+
+def padic_field():
+    """
+    Return a random p-adic field modulo n with p at most 10000
+    and precision between 10 and 100.
+
+    EXAMPLES::
+
+        sage: import sage.rings.tests
+        sage: sage.rings.tests.integer_mod_ring()
+        Ring of integers modulo 30029
+    """
+    from sage.all import ZZ, Qp
+    prec = ZZ.random_element(x=10, y=100)
+    p = ZZ.random_element(x=2, y=10**4 - 30).next_prime()
+    return Qp(p, prec)
+
+
```


In any case, it would be nice to avoid adding _new_ tests that require a specific random seed. We're pretty close to making all testing random testing.


---

Comment by tscrim created at 2021-08-20 00:03:05

I am not sure how useful this is for catching bugs as we do (or at least should do) good test coverage within the individual files/rings themselves. However, I would follow `@`mjo's recommendation as I don't have a strong opinion on this.


---

Comment by git created at 2021-08-20 12:20:41

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2021-08-20 12:21:06

ok, should be better now


---

Comment by mjo created at 2021-08-23 00:18:44

Thanks! Many of these tests can probably be removed later on, but it's nice to have this old ticket fixed in the meantime, especially in the likely event that we all forget about it for another decade.


---

Comment by mjo created at 2021-08-23 00:18:44

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2021-08-29 09:39:31

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2021-08-29 09:39:31

Merge conflict


---

Comment by git created at 2021-09-01 06:12:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2021-09-01 06:13:08

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2021-09-01 06:13:08

indeed a serious merge conflict. Needs another round of review, please


---

Comment by mjo created at 2021-09-02 15:18:30

Changing status from needs_review to positive_review.


---

Comment by mjo created at 2021-09-02 15:18:30

Still OK.


---

Comment by vbraun created at 2021-09-07 20:52:28

Resolution: fixed
