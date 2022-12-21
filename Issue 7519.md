# Issue 7519: Allowing the choice of word datatype for images under WordMorphism

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2009-11-23 12:38:31

Assignee: slabbe

CC:  vdelecroix saliola

By default, the image of a word under a morphism is given by a iterator which is good because it is returned in constant time but which is bad because it is not directly picklable.


```
sage: m = WordMorphism({0:[0,1], 1:[1,0,0,1]})
sage: print m
WordMorphism: 0->01, 1->1001
sage: W = m.domain()
sage: w = W([0,1,1,1])
sage: type(w)
<class 'sage.combinat.words.word.FiniteWord_list'>
sage: z = m(w)
sage: type(z)
<class 'sage.combinat.words.word.FiniteWord_iter_with_caching'>
sage: loads(dumps(z))
Traceback (most recent call last):
...
PicklingError: Can't pickle <type 'generator'>: attribute lookup __builtin__.generator failed
```


This patch allows one to suggest under which datatype to represent the word :


```
sage: m = WordMorphism({0:[0,1], 1:[1,0,0,1]})
sage: z = m([0,1,1,1], datatype='list')
sage: type(z)
<class 'sage.combinat.words.word.FiniteWord_list'>
sage: loads(dumps(z))
word: 01100110011001
```


It also leaves the current default behavior :


```
sage: m = WordMorphism({0:[0,1], 1:[1,0,0,1]})
sage: m([0,1,1,1])
word: 01100110011001
sage: type(_)
<class 'sage.combinat.words.word.FiniteWord_iter_with_caching'>
```








---

Attachment


---

Comment by slabbe created at 2009-11-23 12:58:07

Changing status from new to needs_review.


---

Comment by saliola created at 2009-11-23 15:13:11

This patch seems to depend on #7405.

Patches apply cleanly on top of sage-4.3.alpha0.

The doctests in sage.combinat.words pass.

I'm running the full test suite now. Will report back soon.


---

Comment by saliola created at 2009-11-23 16:34:06

Changing status from needs_review to positive_review.


---

Comment by saliola created at 2009-11-23 16:34:06

Tests pass. Positive review.


---

Comment by slabbe created at 2009-11-23 16:55:28

Great. Thank you Franco for the quick review.


---

Comment by mhansen created at 2009-11-29 05:45:01

Resolution: fixed
