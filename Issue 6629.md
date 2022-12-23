# Issue 6629: Implement the abstract ring of multivariate polynomials, with several bases (Schur schubert, ...)

Issue created by migration from https://trac.sagemath.org/ticket/6629

Original creator: nthiery

Original creation time: 2009-07-26 19:55:34

Assignee: mhansen

CC:  sage-combinat vivianepons tscrim opechenik

Keywords: multivariate polynomials, schubert polynomials, non symmetric polynomials

See: http://wiki.sagemath.org/combinat/MultivariatePolynomials


---

Comment by VivianePons created at 2013-02-13 16:09:51

Changing assignee from mhansen to VivianePons.


---

Comment by VivianePons created at 2013-02-13 16:14:29

the patch apply on 5.6 and is mostly working. It is not yet ready for review though, it needs more tests and docs and possibly a few fixes.


---

Comment by jferreira created at 2013-05-15 22:16:32

What is the status of this ticket? Is it still in development?


---

Comment by VivianePons created at 2013-05-16 07:51:19

Yes, sorry for taking such a long time but this is a big implementation and I work on it only when I have time (which is not so often). 
My plan is to finish a first version of it on the upcoming Sage days in Paris and find someone to work on the review.
In the meantime, the patch is working already and some people use it.


---

Attachment

Just attached the last version of the patch to apply on Sage 5.9


---

Comment by VivianePons created at 2013-11-07 00:32:22

New commits:


---

Comment by tscrim created at 2013-11-13 22:41:37

Changing keywords from "multivariate polynomials, schubert polynomials, non symmetric polynomials" to "multivariate polynomials, schubert polynomials, non symmetric polynomials, days54".


---

Comment by git created at 2014-01-16 15:08:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-05-02 21:43:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-05-05 15:18:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-06-16 20:14:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2016-07-12 14:23:05

Viviane, when you get a chance, could you push the code that you currently have or are you still working on this?


---

Comment by VivianePons created at 2016-07-14 20:59:15

Just pushed my latest code. 
Mostly everything is working but the tests and examples are all messed up (and, for some reason, I still cannot run any tests). 

I have simplified many things, removing useless classes and so on. Now, I consider the monomial basis to be a "generator", I call it x and write:

 

```
sage: A.<x> = MultivariatePolynomialAlgebra(QQ)
sage: x[1,2,3] + x[2,3]
x[2, 3, 0] + x[1, 2, 3]
```


I think it makes more sense and it is more natural to use. The goal is to hide the inner mechanics as much as possible. "New example" are written in this manner, old ones still use the m notation.

All basis are combinatorial free module using a common "key wrapper" class that handles lists and ambient space basis elements.

In terms of mathematical meaning, remember that all bases are indexed by **vectors**, for Grothendieck and Schubert, they correspond to the Lehmer code of the permutation.

The only part that is not working is the "Double polynomial" one, but it's quite independent from the rest. 

I let you have a look at it, it's not finished yet. Feel free to change it if you feel like it. I will be on holidays for the next 2 weeks.
----
New commits:


---

Comment by tscrim created at 2016-07-14 22:28:14

Thank you Viviane, I appreciate it. I will take a look at it soon and pass it along to the REU students. Enjoy your holidays!


---

Comment by git created at 2019-07-09 08:46:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2019-07-09 11:56:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2019-07-09 14:15:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2019-07-10 06:48:41

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by opechenik created at 2019-07-12 14:55:23

Changing keywords from "multivariate polynomials, schubert polynomials, non symmetric polynomials, days54" to "multivariate polynomials, schubert polynomials, non symmetric polynomials, days54, fpsac2019".


---

Comment by tscrim created at 2021-02-28 21:37:08

A version that works on Python3.
----
New commits:
