# Issue 6571: Improve iterator of word morphisms

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2009-07-20 19:27:05

Assignee: slabbe

CC:  sage-combinat saliola

Keywords: words morphisms

Right now, we can iterate over word morphisms with specific image lengths :


```
    Iterator over morphisms with specific image lengths::

	sage: map(str, W.iter_morphisms([2, 1]))
	['WordMorphism: a->aa, b->a',
	 'WordMorphism: a->aa, b->b',
	 'WordMorphism: a->ab, b->a',
	 'WordMorphism: a->ab, b->b',
	 'WordMorphism: a->ba, b->a',
	 'WordMorphism: a->ba, b->b',
	 'WordMorphism: a->bb, b->a',
	 'WordMorphism: a->bb, b->b']
	sage: map(str, W.iter_morphisms([2, 2]))
	['WordMorphism: a->aa, b->aa',
	 'WordMorphism: a->aa, b->ab',
	 'WordMorphism: a->aa, b->ba',
	 'WordMorphism: a->aa, b->bb',
	 'WordMorphism: a->ab, b->aa',
	 'WordMorphism: a->ab, b->ab',
	 'WordMorphism: a->ab, b->ba',
	 'WordMorphism: a->ab, b->bb',
	 'WordMorphism: a->ba, b->aa',
	 'WordMorphism: a->ba, b->ab',
	 'WordMorphism: a->ba, b->ba',
	 'WordMorphism: a->ba, b->bb',
	 'WordMorphism: a->bb, b->aa',
	 'WordMorphism: a->bb, b->ab',
	 'WordMorphism: a->bb, b->ba',
	 'WordMorphism: a->bb, b->bb']
	sage: map(str, W.iter_morphisms([0, 0]))
	['WordMorphism: a->, b->']
	sage: map(str, W.iter_morphisms([0, 1]))
	['WordMorphism: a->, b->a', 'WordMorphism: a->, b->b']
```


I want to iterate over all (non erasing) morphisms! In particuliar, I want the following to work :


```
    sage: W = Words('ab')                 
    sage: it = W.iter_morphisms()
    sage: for _ in range(10): print it.next()
    WordMorphism: a->a, b->a
    WordMorphism: a->a, b->b
    WordMorphism: a->b, b->a
    WordMorphism: a->b, b->b
    WordMorphism: a->aa, b->a
    WordMorphism: a->aa, b->b
    WordMorphism: a->ab, b->a
    WordMorphism: a->ab, b->b
    WordMorphism: a->ba, b->a
    WordMorphism: a->ba, b->b
```



---

Comment by slabbe created at 2009-07-20 19:57:15

Changing status from new to assigned.


---

Comment by slabbe created at 2009-07-20 20:14:57

There is a bug in my patch. Some tests are apparently failing....


---

Comment by slabbe created at 2009-07-20 20:45:22

Failing tests were related to #5600 because the patch I first posted here was depending on `compositions-cleanup-5600-nt.patch`. The patch `word_iter_morphism_6571-sl.patch` should now apply cleanly (including doctests) on sage-4.1.1.alpha0.


---

Comment by AlexGhitza created at 2009-08-16 05:49:56

Changing component from algebra to combinatorics.


---

Attachment

This file depends on #6519 as well as on #5600


---

Comment by slabbe created at 2009-08-19 18:00:34

Since #5600 should be merge soon (it has a positive review), I just uploaded a new patch that uses the benefits of #5600.


---

Comment by saliola created at 2009-08-24 20:46:46

I made a few changes:

 1. As written, the iter_morphisms method is recursive if it is iterating through all morphisms (it calls `self.iter_morphisms(composition)` for all compositions). This is not necessary and it is inefficient. I changed the code to avoid doing this.

 2. Switched from `Compositions` to `IntegerListsLex` instead: the patch converted compositions spit out by `Compositions` to lists; so I changed it because compositions are created from the lists output by `IntegerListsLex`.

 3. `IntegerListsLex` allows one to specify `min_part`, so I added a `min_length` keyword option (so erasing morphisms can be obtained by taking `min_length=0`). The default is 1 (the current behaviour).


---

Comment by saliola created at 2009-08-24 20:47:32

Apply on top of word_iter_morphism_6571-sl.patch


---

Attachment

In case it matters: I applied the patches from #5600 before word_iter_morphism_6571-sl.patch.


---

Comment by slabbe created at 2009-08-25 18:40:00

This patch applies over the precedent two.


---

Attachment

Thanks Franco for your good review. I didn't know about `IntegerListsLex`. Allowing erasing morphism is great as well. I just added a small patch to correct a word in a one-line comment. I am currently building the documentation...


---

Attachment

Applies over the precedent three patches.


---

Comment by slabbe created at 2009-08-25 19:54:17

There was a bug in the ReST documentation. I just added `trac_6571-ReST-bug.patch` which corrects it. Documentation now builds without warnings. Doctests passed on words.py. I am giving a positive review to Franco's changes.


---

Comment by saliola created at 2009-08-25 19:56:44

Sébastien's documentation changes are good.


---

Comment by mvngu created at 2009-08-26 21:46:24

Resolution: fixed
