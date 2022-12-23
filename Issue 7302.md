# Issue 7302: Nowhere wero flow

Issue created by migration from https://trac.sagemath.org/ticket/7302

Original creator: ncohen

Original creation time: 2009-10-25 19:46:14

Assignee: rlm

As we will soon have a Flow function in Sage, the next step could be to write a Nowhere Zero flow function !

More informations there : http://en.wikipedia.org/wiki/Nowhere-zero_flow


---

Comment by ncohen created at 2010-06-06 10:59:17

Changing status from new to needs_work.


---

Comment by dcoudert created at 2017-10-22 12:04:13

Changing status from needs_work to needs_review.


---

Comment by dcoudert created at 2017-10-22 12:04:13

I propose a MIP formulation that answers this long standing request. I'm not aware of alternative/faster methods. It works for any bridgeless (di)graphs with loops or multiple edges.
----
New commits:


---

Comment by git created at 2017-10-22 21:05:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-12-09 18:47:00

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2017-12-11 08:08:22

Overall it looks good. I made some documentation tweaks. However, I do have a question about graphs with a single vertex. Should the nowhere zero flow correspond to an empty digraph? If so, then positive review. Otherwise a fix will be needed.
----
New commits:


---

Comment by tscrim created at 2017-12-11 08:08:22

Changing status from needs_review to needs_info.


---

Comment by git created at 2017-12-11 09:43:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2017-12-11 09:50:12

You are right, the returned digraph must be on the same vertex set.
I have pushed required changes.

However, the current solution does not pass test due to an issue in `orientations`:

```
sage: G = Graph(1)
sage: next(G.orientations())
Digraph on 0 vertices
```

I'm opening a ticket to fix that and put a dependency on ticket #24366. So we have to wait before finalizing this ticket.


---

Comment by git created at 2017-12-16 01:33:56

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2017-12-16 01:34:52

Changing status from needs_info to needs_review.


---

Comment by tscrim created at 2017-12-16 01:34:52

Replying to [comment:14 dcoudert]:
> So we have to wait before finalizing this ticket.

Why? I don't see the point of waiting for the beta with the dependency to be released. I just merge in the branch, and let us continue with the review here.

I made a few more small tweaks. If my changes look good, then positive review.


---

Comment by dcoudert created at 2017-12-16 10:02:24

Changing status from needs_review to positive_review.


---

Comment by dcoudert created at 2017-12-16 10:02:24

Thank you Travis. LGTM.


---

Comment by vbraun created at 2017-12-17 14:17:01

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2017-12-17 14:17:01

PDF docs fail (hint: − is not a minus sign)


---

Comment by git created at 2017-12-17 19:02:51

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2017-12-17 19:03:19

Sorry for that.


---

Comment by dcoudert created at 2017-12-17 19:03:19

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2017-12-17 21:11:43

Thanks to both.


---

Comment by tscrim created at 2017-12-17 21:11:43

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-12-22 23:29:43

Resolution: fixed
