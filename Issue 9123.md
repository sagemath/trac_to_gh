# Issue 9123: implement Schur algebras using AlgebrasWithBasis

Issue created by migration from https://trac.sagemath.org/ticket/9123

Original creator: hthomas

Original creation time: 2010-06-03 04:08:56

Assignee: AlexGhitza

CC:  quantumking

Schur algebras are algebras with basis used in the description of the representation theory of GL_n.  I'd like to implement them.  

A nice reference is Chapter 2 of Green's book "Polynomial representations of GL_n".


---

Comment by hthomas created at 2010-06-03 04:09:51

Changing assignee from AlexGhitza to hthomas.


---

Comment by hthomas created at 2011-05-05 14:43:10

Changing assignee from hthomas to AlexGhitza.


---

Comment by hthomas created at 2011-05-05 14:43:10

Changing keywords from "" to "days30".


---

Comment by hthomas created at 2011-06-17 18:03:55

A patch which does more or less what I want is on the sage-combinat queue, but it needs more work on the documentation.  I was told I shouldn't post it here until I had that done, but if anyone wants to look at it other than by installing the combinat queue, I would be happy to post it.


---

Attachment


---

Comment by hthomas created at 2013-03-25 12:23:34

Someone expressed interest in seeing the current state of the code, so I have attached it.


---

Comment by chapoton created at 2015-04-24 08:53:23

Changing status from new to needs_review.


---

Comment by chapoton created at 2015-04-24 08:53:23

Changing keywords from "days30" to "days30, schur".


---

Comment by chapoton created at 2015-04-24 08:53:23

Here is a git branch. Tests do pass, but the doc may not build.
----
New commits:


---

Comment by git created at 2015-04-24 09:27:31

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-04-25 15:46:39

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2015-05-01 01:41:40

I made a bunch of major revisions:

- I changed the indexing set for `SchurAlgebra` be tuples rather than words since it was not using any properties of words and was incurring for it.
- I changed `TensorSpace` to `SchurTensorModule` (although I'm quite open to better names).
- `SchurTensorModule` inherits from `CombinatorialFreeModule_Tensor`. This makes it behave like a tensor product with respect to things like `tensor()`.
- I implemented the actions of the symmetric group (well...permutations), the symmetric group algebra, and the Schur algebra as actual actions using `_acted_upon_`. I also cached the Schur action morphism and implemented the permutation actions directly.
- Renamed `GL_n_irred_character` to `GL_irreducible_character`.
- Added documentation and doctests for full coverage.

The net result of my changes is over a 30x speedup to `GL_irreducible_character`, which allowed me to remove the `# long time` from those tests. If someone (Hugh, Frederic, ?) could review my changes, then I think we can set a positive review.
----
New commits:


---

Comment by git created at 2015-05-01 08:15:15

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-05-01 08:17:22

Thanks a lot Travis.

I have made a review patch.

There is still something missing : the doc for SchurTensorModule is almost void. Nowhere
one can see anything about the commuting actions. I think one should at least illustrate
both actions.


---

Comment by tscrim created at 2015-05-01 15:11:33

Thanks for those changes. I will add the examples later today.


---

Comment by git created at 2015-05-02 14:04:20

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2015-05-02 14:05:52

Done. I also tweaked the output of the elements of the Schur algebra.


---

Comment by chapoton created at 2015-05-02 17:12:40

Ok, looks good to me. If you see nothing else to do, set to positive review.


---

Comment by tscrim created at 2015-05-02 20:39:07

Thanks Frédéric.


---

Comment by tscrim created at 2015-05-02 20:39:07

Changing status from needs_review to needs_work.


---

Comment by tscrim created at 2015-05-02 20:39:25

Helps if I select the right thing...


---

Comment by tscrim created at 2015-05-02 20:39:25

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2015-05-03 12:06:44

Resolution: fixed
