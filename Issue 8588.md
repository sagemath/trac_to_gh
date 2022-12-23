# Issue 8588: list(SL(2,2)) is inconsistent with SL(2,2).list()

Issue created by migration from https://trac.sagemath.org/ticket/8588

Original creator: nthiery

Original creation time: 2010-03-23 16:29:31

Assignee: AlexGhitza

CC:  sage-combinat

Keywords: Special linear group, TestSuite


```
sage: G = SL(2,2)
sage: TestSuite(G).run()
Failure in _test_enumerated_set_iter_list:
Traceback (most recent call last):
...
AssertionError: [1 1]
[0 1] != [1 0]
[0 1]
------------------------------------------------------------
The following tests failed: _test_enumerated_set_iter_list

sage: list(G)[2]
[1 1]
[0 1]
sage: G.list()[2]
[1 0]
[0 1]
```



---

Attachment


---

Comment by itaibn created at 2012-05-30 00:40:22

Just attached a fix.


---

Attachment

Fixed a typo and improved the formatting.


---

Comment by nbruin created at 2012-06-04 23:35:16

Are you sure this is a wise fix? This way, even starting to iterate on the elements of a matrix group involves constructing all its elements. The iterator method on matrix groups previously was the one inherited from `sage.combinat.backtrack.TransitiveIdeal.__iter__`, which seems a little more conservative.

In principle, people can write `iter(SL(next_prime(10^5),2)).next()` to get an example of a determinant 1 matrix. This doesn't need to be expensive (with the current code it is, though. It seems the `semigroup_generators` method is horribly inefficient). With the present patch it's guaranteed to be very expensive.

Iterators and lists have different use cases, so why should G.list() and list(G) give the same result? I think structures should be allowed to choose different enumeration methods depending on the application. G.list() knows it returns a list of all elements, so it can concentrate on speed and not worry about storage. list(G), which is just [g for g in G] asks G to produce an iterator over its elements, which can choose an enumeration method that saves memory and/or ensures that it's fast even when only a couple of elements are consumed.

It seems to me the correct fix is to amend `TestSuite` to not enforce that iter(G.list()) and iter(G) produce the elements in the same order.


---

Comment by itaibn created at 2012-06-05 00:40:12

The reason I this fix is that I assumed that whoever made that test knew what they were doing and had a good reason. I guess I should have checked if such a reason existed. I actually checked and found out that the test was made in #5891, a large patch where such a mistake could've slipped through.


---

Attachment

I got

```
sage: G = SL(2,2)
sage: TestSuite(G).run()
sage: list(G)[2]
[0 1]
[1 1]
sage: G.list()[2]
[0 1]
[1 1]

```



---

Comment by aapitzsch created at 2014-08-18 21:50:01

Changing status from new to needs_review.


---

Comment by vbraun created at 2014-10-25 21:45:07

Resolution: fixed
