# Issue 8232: cmp function for words is broken

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-02-10 16:03:32

Assignee: sage-combinat

CC:  abmasse

As discussed on [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/9e90bbeb0328034c), cmp is broken for words. 



```
Amusant: this boils down to:

sage: W = Words(['a','b','c'])
sage: W('a') == W([])
True
sage: W([]) == W('a')
False
```


it causes problem else where :


```
sage: A = AlgebrasWithBasis(QQ).example(); A
An example of an algebra with basis: the free algebra on the
generators ('a', 'b', 'c') over Rational Field
sage: [a,b,c] = A.algebra_generators()
sage: a.is_one()
True
sage: b.is_one()
True
sage: c.is_one()
True
sage: A.one().is_one()
True
sage: (a+b).is_one()
False
sage: (a+A.one()).is_one()
False
```




---

Comment by slabbe created at 2010-02-10 17:42:00

I just applied a patch which does the following things.

1. Fixed `__cmp__` for `Word_class` which was broken.

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


NOTE : The difference between w and z above is that the parent of w is the alphabet of all python objects which uses the cmp of python to compare the letters whereas z compares its letters relatively to the order of the letters defined by its parent (here 0 < 1 but one could also say 1 < 0) which is slower.

3. The broken `__cmp__` was hidding one bug in `longest_common_prefix`. Indeed a doctest was passing while it wasn't supposed to:


```
BEFORE:

    sage: w = Word('12345')
    sage: w.longest_common_prefix(Word())
    word: 1

AFTER:

    sage: w = Word('12345')
    sage: w.longest_common_prefix(Word())
    word: 

```



---

Comment by slabbe created at 2010-02-10 17:55:07

Depends on #8186


---

Comment by slabbe created at 2010-02-10 17:55:29

Changing status from new to needs_review.


---

Attachment


---

Comment by abmasse created at 2010-02-16 11:01:35

Hi, Sébastien !

I finally got some time to look at your patch and everything seems fine, code makes sense, documentation builds without warning and the bugs mentionned in the description are fixed.

The only observation I would make is that it seems costly to use all those `try` and `catch` blocks in the `__cmp__(...)` function. Don't you think it may be better to use the `izip_longest` function of the `itertools` library, which fills the shortest iterator with a special character ? This way, you would only have to check if that character appear in `self_it or in `other_it` to choose which one is the smallest w.r.t the lexicographic order.


---

Comment by abmasse created at 2010-02-16 23:35:16

Never mind my last observation, it seems more complicated to use `izip_longest` since you have to choose a different character from the one occurring in the compared words... and there is no clean way that comes up to me since the letters of word can be any object.

Anyway, the goal of the patch is reached, the documentation builds correctly, all tests pass, the bugs are fixed.

Positive review !


---

Comment by abmasse created at 2010-02-16 23:35:16

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-17 20:38:19

Resolution: fixed
