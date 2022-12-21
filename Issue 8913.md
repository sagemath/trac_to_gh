# Issue 8913: S.cayley_graph(side = "twosided") returns broken labels

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-05-07 15:10:43

Assignee: nthiery

CC:  sage-combinat rbeezer

This patch reinstates appropriate labeling of the edges for two sided cayley graphs::

```
   sage: S = FiniteSemigroups().example(alphabet=('a','b'))
   sage: g = S.cayley_graph(side="twosided")
   sage: g.edges()
   [('a', 'a', (0, 'left')), ('a', 'a', (0, 'right')), ('a', 'ab', (1, 'right')), ('a', 'ba', (1, 'left')), ('ab', 'ab', (0, 'left')), ('ab', 'ab', (0, 'right')), ('ab', 'ab', (1, 'right')), ('ab', 'ba', (1, 'left')), ('b', 'ab', (0, 'left')), ('b', 'b', (1, 'left')), ('b', 'b', (1, 'right')), ('b', 'ba', (0, 'right')), ('ba', 'ab', (0, 'left')), ('ba', 'ba', (0, 'right')), ('ba', 'ba', (1, 'left')), ('ba', 'ba', (1, 'right'))]
```


This was inadvertently broken by #8044 which discarded the `left` / `right` info.


---

Comment by nthiery created at 2010-05-18 21:18:11

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-05-18 21:18:11

Changing keywords from "" to "cayley graph".


---

Attachment


---

Comment by rbeezer created at 2010-05-19 03:33:34

Looks good.  Running tests now.


---

Comment by rbeezer created at 2010-05-19 05:41:29

Looks good (including the addition of a new doctest for this situation).

Applies, builds, whole library passes tests, docs are fine, all on 4.4.2.rc0.

Positive review.


---

Comment by rbeezer created at 2010-05-19 05:41:29

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-05-19 06:26:20

Replying to [comment:4 rbeezer]:
> Looks good (including the addition of a new doctest for this situation).
> 
> Applies, builds, whole library passes tests, docs are fine, all on 4.4.2.rc0.
> 
> Positive review.

Thanks Rob, that was quick!


---

Comment by mhansen created at 2010-06-06 01:12:36

Resolution: fixed
