# Issue 9455: Dimensions of eigenspaces for the Atkin-Lehner operator acting on modular forms

Issue created by migration from https://trac.sagemath.org/ticket/9455

Original creator: ljpk

Original creation time: 2010-07-08 15:10:40

Assignee: craigcitro

CC:  was

This is a port of David Kohel's MAGMA code to compute dimensions of the eigenspaces for the Atkin-Lehner operators acting on spaces of cusp forms of weight 2 (see here for the original):

http://echidna.maths.usyd.edu.au/echidna/dbs/atkin-lehner/index.html

These methods do not rely on computing explicit bases of newforms, instead using formulae about the ramification points of the Atkin-Lehner operator. 

These functions use the class number method qfbclassno() from Pari/GP.


---

Attachment

Code to implement dimensions of Atkin-Lehner eigenspaces for the ModularForms class


---

Comment by ljpk created at 2010-08-11 15:18:00

Changing assignee from craigcitro to ljpk.


---

Comment by ljpk created at 2010-08-11 15:18:37

Changing assignee from ljpk to craigcitro.


---

Attachment


---

Comment by chapoton created at 2013-08-08 19:57:48

I have tried to maker a clean patch starting with the given file

Some doctests are still failing.

for the bot: apply only trac_9455_atkin_lehner_dim.patch​


---

Comment by chapoton created at 2013-08-08 19:57:48

Changing keywords from "" to "atkin lehner".


---

Comment by chapoton created at 2014-01-09 19:53:40

New commits:


---

Comment by git created at 2014-11-14 16:09:01

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-02-18 10:33:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-02-18 10:34:20

Changing status from new to needs_review.


---

Comment by chapoton created at 2015-02-18 10:34:20

Now all tests pass. But maybe this is too slow.


---

Comment by git created at 2015-02-19 11:00:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-22 11:09:58

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2015-03-22 14:05:03

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-22 15:09:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by davidloeffler created at 2015-12-04 16:37:44

This needs some serious work.

- Most of this new code is added via methods of Gamma0 modular forms space objects. However, these objects can have any weight, but the implementations here only work for weight 2, so you can type something like

```
 sage: ModularForms(1000003, 4).atkin_lehner_eigenspace_dimensions()
```

 and it will silently return wrong output. More importantly, lots of these methods (e.g. `atkin_lehner_ramification`) are computing geometric properties of the underlying modular curves, so they belong in `sage.modular.arithgroup.congroup_gamma0`. Similarly, "primitive_ideal_number" should probably be a method of order objects, not a standalone function.

- Many function names are mysterious or downright misleading, e.g. the method `modular_genus_X0` is not actually computing the genus of anything in most cases. 

- The documentation is poor. What on earth is the "(M, R)-old subspace"? What are "cyclic ideals"?  Docstrings for each method should explain what the arguments mean. The docstring for `old_subspace_dimension(self, M, R, w)` does not even mention Atkin--Lehner involutions!

- Why is a line of code in the number fields module (in `absolute_order_from_module_generators`) deleted without explanation?


---

Comment by davidloeffler created at 2015-12-04 16:37:44

Changing status from needs_review to needs_work.


---

Comment by git created at 2016-03-01 11:26:11

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-04-13 19:03:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-07-29 18:52:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-03-01 15:05:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-03-11 19:59:27

Branch pushed to git repo; I updated commit sha1. New commits:
