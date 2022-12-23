# Issue 8187: improve equality tests for words

Issue created by migration from https://trac.sagemath.org/ticket/8187

Original creator: slabbe

Original creation time: 2010-02-05 03:16:45

Assignee: sage-combinat

CC:  abmasse vdelecroix saliola

More often, when we compare two words, we test their equality and not that one is less than the other. So why not implement the equatlity test!? This ticket does this for datatypes and for math objects. It also improve the comparison function (by removing it!).

1. This patch adds equality test for `WordDatatype_str`, `WordDatatype_list` and `WordDatatype_tuple`  (via `__richcmp__`) usefull when comparing two words represented by the same kind of data. It is now as fast as the python object :


```
BEFORE:

    sage: w = Word(range(10000))
    sage: z = Word(range(10000))
    sage: %timeit w == z
    125 loops, best of 3: 4.08 ms per loop

AFTER:

    sage: w = Word(range(10000))
    sage: z = Word(range(10000))
    sage: %timeit w == z
    625 loops, best of 3: 422 µs per loop

PYTHON OBJECT:

    sage: w = range(10000)
    sage: z = range(10000)
    sage: %timeit w == z
    625 loops, best of 3: 442 µs per loop
```



```
BEFORE:

    sage: w = Word(tuple(range(10000)))
    sage: z = Word(tuple(range(10000)))
    sage: %timeit w == z
    125 loops, best of 3: 3.97 ms per loop

AFTER:

    sage: w = Word(tuple(range(10000)))
    sage: z = Word(tuple(range(10000)))
    sage: %timeit w == z
    625 loops, best of 3: 419 µs per loop

PYTHON OBJECT:

    sage: w = tuple(range(10000))
    sage: z = tuple(range(10000))
    sage: %timeit w == z
    625 loops, best of 3: 420 µs per loop
```



```
BEFORE:

    sage: w = Word('a'*10000)
    sage: z = Word('a'*10000)
    sage: %timeit w == z
    125 loops, best of 3: 3.9 ms per loop

AFTER:

    sage: w = Word('a'*10000)
    sage: z = Word('a'*10000)
    sage: %timeit w == z
    625 loops, best of 3: 2.36 µs per loop

PYTHON OBJECT:

    sage: w = 'a'*10000
    sage: z = 'a'*10000
    sage: %timeit w == z
    625 loops, best of 3: 2.03 µs per loop

```


2. Remove the `__cmp__` from `FiniteWord_class` since the same function in `Word_class` does the job anyway and in a cleaner way : it doesn't use the (useless?) coerce function. Surprinsingly, removing it makes it faster :


```
BEFORE:

    sage: w = Word([0]*10000)
    sage: z = Word([0]*10000, alphabet=[0,1])
    sage: type(w)
    <class 'sage.combinat.words.word.FiniteWord_list'>
    sage: type(z)
    <class 'sage.combinat.words.word.FiniteWord_list'>
    sage: %timeit w.__cmp__(w)
    125 loops, best of 3: 3.79 ms per loop
    sage: %timeit w.__cmp__(z)
    25 loops, best of 3: 13.3 ms per loop
    sage: %timeit z.__cmp__(w)
    5 loops, best of 3: 50.1 ms per loop
    sage: %timeit z.__cmp__(z)
    25 loops, best of 3: 35.7 ms per loop


AFTER:

    sage: w = Word([0]*10000)
    sage: z = Word([0]*10000, alphabet=[0,1])
    sage: type(w)
    <class 'sage.combinat.words.word.FiniteWord_list'>
    sage: type(z)
    <class 'sage.combinat.words.word.FiniteWord_list'>
    sage: %timeit w.__cmp__(w)
    125 loops, best of 3: 3.89 ms per loop
    sage: %timeit w.__cmp__(z)
    125 loops, best of 3: 5.4 ms per loop
    sage: %timeit z.__cmp__(w)
    25 loops, best of 3: 35.9 ms per loop
    sage: %timeit z.__cmp__(z)
    25 loops, best of 3: 35.7 ms per loop
```


NOTE : The difference between w and z above is that the parent of w is the alphabet of all python objects which uses the cmp of python to compare the letters whereas z compares its letters relatively to the order of the letters defined by the parent (here 0 < 1 but one could also say 1 < 0) which is slower.


3. Add the `__eq__` and `__ne__` for `Word_class` because it is faster than using `__cmp__` (especially when parent alphabet are defined):

no parents :


```
BEFORE:

    sage: L = range(10000)
    sage: t = tuple(L)
    sage: w = Word(L)
    sage: z = Word(t)
    sage: type(w)
    <class 'sage.combinat.words.word.FiniteWord_list'>
    sage: type(z)
    <class 'sage.combinat.words.word.FiniteWord_tuple'>
    sage: %timeit w == z
    125 loops, best of 3: 3.69 ms per loop


AFTER:

    sage: L = range(10000)
    sage: t = tuple(L)
    sage: w = Word(L)
    sage: z = Word(t)
    sage: type(w)
    <class 'sage.combinat.words.word.FiniteWord_list'>
    sage: type(z)
    <class 'sage.combinat.words.word.FiniteWord_tuple'>
    sage: %timeit w == z
    625 loops, best of 3: 1.44 ms per loop
```


with parents (!!):


```
BEFORE:

    sage: W = Words([0,1,2])
    sage: w = W([0, 1, 1, 2]*4000)
    sage: z = W([0, 1, 1, 2]*4000)
    sage: %timeit w == z
    5 loops, best of 3: 63 ms per loop

AFTER:

    sage: W = Words([0,1,2])
    sage: w = W([0, 1, 1, 2]*4000)
    sage: z = W([0, 1, 1, 2]*4000)
    sage: %timeit w == z
    125 loops, best of 3: 2.57 ms per loop
```



---

Comment by slabbe created at 2010-02-05 03:40:55

Changing keywords from "" to "words".


---

Comment by slabbe created at 2010-02-05 03:40:55

Changing status from new to needs_review.


---

Comment by slabbe created at 2010-02-10 15:55:48

This patch seems to introduce some problems. See

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/9e90bbeb0328034c

Needs work...


---

Comment by slabbe created at 2010-02-10 15:55:48

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by slabbe created at 2010-02-10 18:24:58

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-02-10 18:24:58

> This patch seems to introduce some problems.

Finally, the problem were already present. This ticket was simply making them appear! The problem is being tracked at #8232.

I just uploaded a new patch.

Needs review again!


---

Comment by abmasse created at 2010-02-24 00:59:17

I tested the patch and everything seems fine. Although it modifies several basic functions, it doesn't seem to have any side effect. I couldn't check all documentation since some part of the code is written in Cython, but the functions I did check built correctly.

I've made minor changes in the doc: just formatting some part of the code or correcting typos. If Sébastien agrees with my change, I allow him to set the path to `positive review`.


---

Comment by abmasse created at 2010-02-24 01:00:20

Doc, formatting and typos changes -- apply on top of the main patch


---

Attachment

I forgot to mention that equality tests are indeed improved in some cases, and I haven't encountered any worse case, which is good !


---

Comment by slabbe created at 2010-02-24 01:55:54

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 21:19:47

Merged in this order:

 1. [trac_8187_equality_words-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8187/trac_8187_equality_words-sl.patch)
 1. [trac_8187_review-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8187/trac_8187_review-abm.patch)


---

Comment by mvngu created at 2010-03-02 21:19:47

Resolution: fixed
