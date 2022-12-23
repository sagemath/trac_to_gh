# Issue 8585: PermutationGroup and SymmetricGroup on the empty set

Issue created by migration from https://trac.sagemath.org/ticket/8585

Original creator: hivert

Original creation time: 2010-03-23 09:01:45

Assignee: hivert

CC:  sage-combinat nborie

Keywords: Empty Set, PermutationGroup

Sage can't properly work with SymmetricGroup(0) or PermutationsGroup on the
empty set.

```
sage: SymmetricGroup(0)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
[...]
ValueError: min() arg is an empty sequence
```




---

Comment by hivert created at 2010-03-23 09:14:43

Should be ready for review.


---

Comment by hivert created at 2010-03-23 09:14:43

Changing status from new to needs_review.


---

Comment by hivert created at 2010-03-31 10:16:46

A comment by e-mail from Nicolas Borie:

> 1. Est-ce qu'on change ce comportement ?

Trans: Should we change this behavior

```
> sage: SymmetricGroup(-12)
> Symmetric group of order 0! as a permutation group
```


> 2. Ce serait bien de changer ce message d'erreur :

Trans: This error message is wrong:

```
> sage: SymmetricGroup('bla')
>[...]
> ValueError: n (=bla) must be an integer >= 1 or a list (but n has type
> <type 'str'>)
```


> --> n must be an integer >= 0 now !!!


---

Comment by nborie created at 2010-04-16 09:32:54

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-04-16 10:20:09

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:4 nborie]:
Oups ! I forgot to reupload the patch after sending my e-mail... Sorry.


---

Comment by nborie created at 2010-04-16 11:00:23

Changing status from needs_review to positive_review.


---

Comment by nborie created at 2010-04-16 11:00:23

The patch apply, all tests passed, good behavior with the user. And step by step, the TestSuite design give a nice coherence of "mathematical tests" in the sage code... Perfect from me.

I give this patch a positive review.


---

Comment by jhpalmieri created at 2010-04-19 05:14:41

Merged "trac_8585-permutation_group_on_empty_set-fh.patch" into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-19 05:14:41

Resolution: fixed
