# Issue 2907: polynomials lack content method

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-04-13 17:46:06

Assignee: somebody

ATM, there is no efficient way of getting the content of a polynomial in Sage.


```
gcd(p.list())
```


is a workaround, but this can be done much more efficiently.


---

Comment by AlexGhitza created at 2009-01-22 18:16:28

Changing type from defect to enhancement.


---

Comment by bruno created at 2014-12-17 11:06:58

Changing status from new to needs_review.


---

Comment by bruno created at 2014-12-17 11:06:58

That is not true anymore!


```python
sage: R.<x> = ZZ[]
sage: p = R.random_element(10)
sage: p.content()
1
sage: p *= 13
sage: p.content()
13
```


(There is a consistency problem though between different implementations of `content()`, see #16613, but this ticket can be closed now I think.)


---

Comment by bruno created at 2014-12-19 15:16:22

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2014-12-19 15:42:43

one still needs to fill in the names of the author(s) and reviewer(s), IMHO


---

Comment by tscrim created at 2014-12-20 00:22:15

Technically the one who sets the ticket to invalid should not set it to a positive review (as a "review"), but usually it's okay because things like this are non-controversial.


---

Comment by vbraun created at 2015-01-13 01:15:29

Resolution: fixed
