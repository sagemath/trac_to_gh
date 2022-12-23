# Issue 9280: implement an example of a graded algebra with basis

Issue created by migration from https://trac.sagemath.org/ticket/9280

Original creator: jhpalmieri

Original creation time: 2010-06-20 03:39:29

Assignee: nthiery

The summary says it all.  Also see the patch.


---

Comment by jhpalmieri created at 2010-06-20 03:40:21

Changing status from new to needs_review.


---

Attachment

Hi John,

For the record: we went through your patches with Franco and Jason, and discussed quite a bit around it. We will post here shortly an updated patch with some little suggestions.


---

Comment by jhpalmieri created at 2010-10-01 22:17:48

Replying to [comment:2 nthiery]:
> Hi John,
> 
> For the record: we went through your patches with Franco and Jason, and discussed quite a bit around it. We will post here shortly an updated patch with some little suggestions.

Is it "shortly" yet?  :)


---

Comment by jhpalmieri created at 2010-11-08 23:27:34

In the sage-combinat patch, there are a few typos and some other issues:

 - in sage/categories/graded_algebras_with_basis.py, the docstring for "degree" says "The degree of this element in the graded polynomial algebra."  Delete "polynomial".

 - in sage/categories/examples/graded_algebras_with_basis.py, the docstring for "one_basis" contains `'(0,...,0`)`, and I think this should be changed to ```(0,...,0)```.

 - in sage/categories/examples/graded_algebras_with_basis.py, the docstring for the main class is now outdated: it still refers to "basis_function" and "_basis_fcn", which don't exist any more, and also to "homogeneous_component", which is now part of the default implementation, not something specific to this example.

I'm attaching a referee patch which fixes these. 

There are also some doctests for "basis" in sage/categories/graded_algebras_with_basis.py which are marked as "todo: not implemented".  Do we need to wait for these to be fixed, or should we consider this ready for review?  It may not be ideal, but we could also change

```
sage: A.basis(6) # todo: not implemented (output)
Family (y^{2}, x^{3}
```

to

```
sage: A.basis(6) # todo: not implemented (output)
Family (y^{2}, x^{3}
sage: list(A.basis(6))
[y^{2}, x^{3}]
```

By the way, all tests pass with this patch and with the one from #10193.  So perhaps we could also delete the commented-out part at the beginning of the example, where it says

```
# TODO: double check that we can now discard this function
```



---

Attachment

apply on top of sage-combinat patch


---

Comment by saliola created at 2012-07-13 14:53:29

There are a couple of patches on the sage-combinat queue experimenting with moving some of the generic methods into the category `GradedAlgebraWithBasis`:

- trac_9280-graded-algebras-example-review-fs.patch
- trac_9280-graded-algebras-example.patch


---

Comment by vdelecroix created at 2013-02-13 22:46:26

Sorry for the long delay for the ticket but #10193 is now ready !!


---

Comment by chapoton created at 2013-08-21 13:11:07

Changing keywords from "" to "graded algebra".


---

Comment by chapoton created at 2013-08-23 08:29:28

Franco, Nicolas, what can we do with this ticket ? Should we use the patch from the combinat queue or the patch here ?


---

Attachment


---

Comment by chapoton created at 2013-08-30 16:02:31

let me take the patch of sage-combinat as a starting point.

for the bot: apply only trac_9280-graded-algebras-example-fs.patch


---

Comment by jhpalmieri created at 2013-08-30 17:57:08

I don't know why I'm listed as an author in the file "sage/categories/examples/graded_modules_with_basis.py"; I don't think I had anything to do with that.


---

Comment by chapoton created at 2013-08-30 18:37:31

The part of this patch concerning modules has been separated into ticket #11688 : the ticket #11688 should go first, then this one will need to be rebased on it. 

I upload here the "algebra only patch" that will be the new starting point.


---

Attachment


---

Comment by chapoton created at 2013-09-15 16:38:12

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2013-09-15 16:38:12

this needs to be rebased


---

Comment by tscrim created at 2013-12-20 03:15:41

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2013-12-20 03:15:41

Since the graded algebras with basis example is using (weighted) integer vectors, we need #12453. I'd like to attach the branch "public/categories/graded_examples-9280", but trac is giving me an error when I try...


---

Comment by tscrim created at 2013-12-21 15:41:23

New commits:


---

Comment by git created at 2014-01-25 19:01:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-02-08 17:58:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-08-10 11:36:17

needs rebase


---

Comment by chapoton created at 2014-08-10 11:36:17

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2016-08-25 16:48:34

Yet another instance of someone asking a question related to this. Six (!) years ago, when I opened this ticket, I thought it would be good to have an example in the Sage library and in the documentation, and I really can't understand why this hasn't been taken care of yet. I am not interested in working on it myself any more, but I find it incredibly frustrating that this ticket has languished for so long.

http://ask.sagemath.org/question/34577/can-sage-compute-a-basis-for-the-graded-parts-of-a-graded-ring/


---

Comment by tscrim created at 2016-08-25 19:27:51

It is because of the dependency on integer vectors, which led to #12453. We can either give a new example based on another object or we review #12453 (which I just did a [non-trivial] rebase to the latest beta).
