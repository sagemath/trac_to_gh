# Issue 5583: coercion bug in perm groups

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-03-22 11:36:05

Assignee: joyner

CC:  tscrim


```
sage: PermutationGroup([(), (1,3)]).has_coerce_map_from( PermutationGroup([(), (1,2)]) )
True
```



---

Comment by chapoton created at 2019-05-17 17:40:16

works in 8.8.b5:

```
sage: PermutationGroup([(), (1,3)]).has_coerce_map_from( PermutationGroup([(), (
....: 1,2)]) )

False
```



---

Comment by chapoton created at 2019-05-17 17:40:16

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2019-05-17 17:58:02

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2019-05-17 17:58:02

I agree. It works going back to Sage 8.3 (that's the oldest version I have installed), in both Python 2 and Python 3.


---

Comment by chapoton created at 2019-06-01 07:20:35

Changing status from positive_review to needs_work.


---

Comment by chapoton created at 2019-06-01 07:20:35

I have decided to add a doctest, just to be safe.
----
New commits:


---

Comment by chapoton created at 2019-06-01 07:20:45

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2019-06-01 10:25:49

green bot, please review this easy ticket


---

Comment by tscrim created at 2019-06-01 23:37:20

LGTM.


---

Comment by tscrim created at 2019-06-01 23:37:20

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2019-06-05 18:31:09

Resolution: fixed
