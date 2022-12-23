# Issue 6: Error message in szeged_index()

`Graph({0: [1], 2: []}).szeged_index()` gives `KeyError: 2`. No idea about what is Szeged index, but anyways at least the error message should be better.

Issue created by migration from https://trac.sagemath.org/ticket/26803




---

According to https://en.wikipedia.org/wiki/Szeged_index, this index is defined for connected graphs only.

I added a test and a doctest, a link to the wikipedia page for easier access to definition,  and took the opportunity to do PEP8 cleaning of this method.
----
New commits:


---

Changing status from new to needs_review.


---

Seems good, but test for a ticket should go to `TESTS::` section instead of `EXAMPLES::`.


---

Changing status from needs_review to needs_work.


---

Branch pushed to git repo; I updated commit sha1. New commits:


---

Right, done.


---

Changing status from needs_work to needs_review.


---

Changing status from needs_review to positive_review.


---

Good to go.


---

Resolution: fixed
