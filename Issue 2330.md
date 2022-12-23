# Issue 2330: modforms -- implement computation of weight 1 forms in Sage

Issue created by migration from https://trac.sagemath.org/ticket/2330

Original creator: was

Original creation time: 2008-02-27 11:02:54

Assignee: was

Kevin Buzzard and I intend to do this ASAP based on algorithms he designed in 2002.

If you see this and are interested in helping, send me an email (wstein`@`gmail.com).


---

Comment by was created at 2008-02-27 11:03:03

Changing type from defect to enhancement.


---

Comment by AlexGhitza created at 2008-04-13 01:56:16

Changing assignee from was to craigcitro.


---

Comment by AlexGhitza created at 2008-04-13 01:56:16

Changing component from number theory to modular forms.


---

Comment by roed created at 2017-02-06 18:20:49

Presumably this would be based on http://wwwf.imperial.ac.uk/~buzzard/maths/research/papers/wt1.pdf


---

Comment by davidloeffler created at 2017-11-08 02:52:34

New commits:


---

Comment by davidloeffler created at 2017-11-08 02:52:34

Changing status from new to needs_review.


---

Comment by roed created at 2017-11-08 07:59:37

It's awesome to have weight 1 forms!

Overall, the code looks good.  A few issues to be addressed:

* There's a plugin failure complaining about two lines with non-ASCII characters
* The definition of `R` in the docstring of `modular_ratio_space` is off by one compared to the usage of `R` in the code.


---

Comment by roed created at 2017-11-08 07:59:37

Changing status from needs_review to needs_work.


---

Comment by git created at 2017-11-08 12:00:35

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by davidloeffler created at 2017-11-08 12:01:18

This should address those two issues.
----
New commits:


---

Comment by davidloeffler created at 2017-11-08 12:01:18

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2017-11-08 12:29:05

I'm a bit puzzled that four out of the five patchbot reports for the first version of the code are reporting test failures, all of which are nothing to do with the ticket as far as I can see -- is there something wrong with the patchbot? Most of them seem to be timeout errors.


---

Comment by roed created at 2017-11-08 18:23:00

I'm not sure what's wrong with the other patchbots, but I've seen some of these errors in other places.  It's certainly not a problem with your code.

Looks good!


---

Comment by roed created at 2017-11-08 18:23:00

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-12-11 01:04:08

Resolution: fixed
