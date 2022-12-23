# Issue 9629: sage -merge should look for sensible-editor before pico

Issue created by migration from https://trac.sagemath.org/ticket/9629

Original creator: ddrake

Original creation time: 2010-07-29 00:32:23

Assignee: jason

I don't have pico installed, and hadn't set $EDITOR, so "sage -merge" bombed out; but on Debian-like systems, there's always sensible-editor, which is pretty much what you'd expect. The sage -merge script should look for that before looking for pico.

(Also, uppity free software types would argue that you should look for nano, not pico...)


---

Comment by aapitzsch created at 2014-06-22 16:01:47

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2014-06-22 16:01:47

`-merge` option is gone.


---

Comment by vdelecroix created at 2014-06-22 16:16:28

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2014-06-22 16:16:28

Replying to [comment:4 aapitzsch]:
> `-merge` option is gone.
Great, one ticket less!


---

Comment by vbraun created at 2014-06-23 19:15:58

Resolution: invalid
