# Issue 8187: improve equality tests for words

archive/issues_008187.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  abmasse vdelecroix saliola\n\nMore often, when we compare two words, we test their equality and not that one is less than the other. So why not implement the equatlity test!? This ticket does this for datatypes and for math objects. It also improve the comparison function (by removing it!).\n\n1. This patch adds equality test for `WordDatatype_str`, `WordDatatype_list` and `WordDatatype_tuple`  (via `__richcmp__`) usefull when comparing two words represented by the same kind of data. It is now as fast as the python object :\n\n\n```\nBEFORE:\n\n    sage: w = Word(range(10000))\n    sage: z = Word(range(10000))\n    sage: %timeit w == z\n    125 loops, best of 3: 4.08 ms per loop\n\nAFTER:\n\n    sage: w = Word(range(10000))\n    sage: z = Word(range(10000))\n    sage: %timeit w == z\n    625 loops, best of 3: 422 \u00b5s per loop\n\nPYTHON OBJECT:\n\n    sage: w = range(10000)\n    sage: z = range(10000)\n    sage: %timeit w == z\n    625 loops, best of 3: 442 \u00b5s per loop\n```\n\n\n\n```\nBEFORE:\n\n    sage: w = Word(tuple(range(10000)))\n    sage: z = Word(tuple(range(10000)))\n    sage: %timeit w == z\n    125 loops, best of 3: 3.97 ms per loop\n\nAFTER:\n\n    sage: w = Word(tuple(range(10000)))\n    sage: z = Word(tuple(range(10000)))\n    sage: %timeit w == z\n    625 loops, best of 3: 419 \u00b5s per loop\n\nPYTHON OBJECT:\n\n    sage: w = tuple(range(10000))\n    sage: z = tuple(range(10000))\n    sage: %timeit w == z\n    625 loops, best of 3: 420 \u00b5s per loop\n```\n\n\n\n```\nBEFORE:\n\n    sage: w = Word('a'*10000)\n    sage: z = Word('a'*10000)\n    sage: %timeit w == z\n    125 loops, best of 3: 3.9 ms per loop\n\nAFTER:\n\n    sage: w = Word('a'*10000)\n    sage: z = Word('a'*10000)\n    sage: %timeit w == z\n    625 loops, best of 3: 2.36 \u00b5s per loop\n\nPYTHON OBJECT:\n\n    sage: w = 'a'*10000\n    sage: z = 'a'*10000\n    sage: %timeit w == z\n    625 loops, best of 3: 2.03 \u00b5s per loop\n\n```\n\n\n2. Remove the `__cmp__` from `FiniteWord_class` since the same function in `Word_class` does the job anyway and in a cleaner way : it doesn't use the (useless?) coerce function. Surprinsingly, removing it makes it faster :\n\n\n```\nBEFORE:\n\n    sage: w = Word([0]*10000)\n    sage: z = Word([0]*10000, alphabet=[0,1])\n    sage: type(w)\n    <class 'sage.combinat.words.word.FiniteWord_list'>\n    sage: type(z)\n    <class 'sage.combinat.words.word.FiniteWord_list'>\n    sage: %timeit w.__cmp__(w)\n    125 loops, best of 3: 3.79 ms per loop\n    sage: %timeit w.__cmp__(z)\n    25 loops, best of 3: 13.3 ms per loop\n    sage: %timeit z.__cmp__(w)\n    5 loops, best of 3: 50.1 ms per loop\n    sage: %timeit z.__cmp__(z)\n    25 loops, best of 3: 35.7 ms per loop\n\n\nAFTER:\n\n    sage: w = Word([0]*10000)\n    sage: z = Word([0]*10000, alphabet=[0,1])\n    sage: type(w)\n    <class 'sage.combinat.words.word.FiniteWord_list'>\n    sage: type(z)\n    <class 'sage.combinat.words.word.FiniteWord_list'>\n    sage: %timeit w.__cmp__(w)\n    125 loops, best of 3: 3.89 ms per loop\n    sage: %timeit w.__cmp__(z)\n    125 loops, best of 3: 5.4 ms per loop\n    sage: %timeit z.__cmp__(w)\n    25 loops, best of 3: 35.9 ms per loop\n    sage: %timeit z.__cmp__(z)\n    25 loops, best of 3: 35.7 ms per loop\n```\n\n\nNOTE : The difference between w and z above is that the parent of w is the alphabet of all python objects which uses the cmp of python to compare the letters whereas z compares its letters relatively to the order of the letters defined by the parent (here 0 < 1 but one could also say 1 < 0) which is slower.\n\n\n3. Add the `__eq__` and `__ne__` for `Word_class` because it is faster than using `__cmp__` (especially when parent alphabet are defined):\n\nno parents :\n\n\n```\nBEFORE:\n\n    sage: L = range(10000)\n    sage: t = tuple(L)\n    sage: w = Word(L)\n    sage: z = Word(t)\n    sage: type(w)\n    <class 'sage.combinat.words.word.FiniteWord_list'>\n    sage: type(z)\n    <class 'sage.combinat.words.word.FiniteWord_tuple'>\n    sage: %timeit w == z\n    125 loops, best of 3: 3.69 ms per loop\n\n\nAFTER:\n\n    sage: L = range(10000)\n    sage: t = tuple(L)\n    sage: w = Word(L)\n    sage: z = Word(t)\n    sage: type(w)\n    <class 'sage.combinat.words.word.FiniteWord_list'>\n    sage: type(z)\n    <class 'sage.combinat.words.word.FiniteWord_tuple'>\n    sage: %timeit w == z\n    625 loops, best of 3: 1.44 ms per loop\n```\n\n\nwith parents (!!):\n\n\n```\nBEFORE:\n\n    sage: W = Words([0,1,2])\n    sage: w = W([0, 1, 1, 2]*4000)\n    sage: z = W([0, 1, 1, 2]*4000)\n    sage: %timeit w == z\n    5 loops, best of 3: 63 ms per loop\n\nAFTER:\n\n    sage: W = Words([0,1,2])\n    sage: w = W([0, 1, 1, 2]*4000)\n    sage: z = W([0, 1, 1, 2]*4000)\n    sage: %timeit w == z\n    125 loops, best of 3: 2.57 ms per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8187\n\n",
    "created_at": "2010-02-05T03:16:45Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "improve equality tests for words",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8187",
    "user": "slabbe"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/8187





---

archive/issue_comments_072156.json:
```json
{
    "body": "Changing keywords from \"\" to \"words\".",
    "created_at": "2010-02-05T03:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72156",
    "user": "slabbe"
}
```

Changing keywords from "" to "words".



---

archive/issue_comments_072157.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-05T03:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72157",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072158.json:
```json
{
    "body": "This patch seems to introduce some problems. See\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/9e90bbeb0328034c\n\nNeeds work...",
    "created_at": "2010-02-10T15:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72158",
    "user": "slabbe"
}
```

This patch seems to introduce some problems. See

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/9e90bbeb0328034c

Needs work...



---

archive/issue_comments_072159.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-10T15:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72159",
    "user": "slabbe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072160.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-02-10T18:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72160",
    "user": "slabbe"
}
```

Attachment



---

archive/issue_comments_072161.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-10T18:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72161",
    "user": "slabbe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072162.json:
```json
{
    "body": "> This patch seems to introduce some problems.\n\nFinally, the problem were already present. This ticket was simply making them appear! The problem is being tracked at #8232.\n\nI just uploaded a new patch.\n\nNeeds review again!",
    "created_at": "2010-02-10T18:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72162",
    "user": "slabbe"
}
```

> This patch seems to introduce some problems.

Finally, the problem were already present. This ticket was simply making them appear! The problem is being tracked at #8232.

I just uploaded a new patch.

Needs review again!



---

archive/issue_comments_072163.json:
```json
{
    "body": "I tested the patch and everything seems fine. Although it modifies several basic functions, it doesn't seem to have any side effect. I couldn't check all documentation since some part of the code is written in Cython, but the functions I did check built correctly.\n\nI've made minor changes in the doc: just formatting some part of the code or correcting typos. If S\u00e9bastien agrees with my change, I allow him to set the path to `positive review`.",
    "created_at": "2010-02-24T00:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72163",
    "user": "abmasse"
}
```

I tested the patch and everything seems fine. Although it modifies several basic functions, it doesn't seem to have any side effect. I couldn't check all documentation since some part of the code is written in Cython, but the functions I did check built correctly.

I've made minor changes in the doc: just formatting some part of the code or correcting typos. If Sébastien agrees with my change, I allow him to set the path to `positive review`.



---

archive/issue_comments_072164.json:
```json
{
    "body": "Doc, formatting and typos changes -- apply on top of the main patch",
    "created_at": "2010-02-24T01:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72164",
    "user": "abmasse"
}
```

Doc, formatting and typos changes -- apply on top of the main patch



---

archive/issue_comments_072165.json:
```json
{
    "body": "Attachment\n\nI forgot to mention that equality tests are indeed improved in some cases, and I haven't encountered any worse case, which is good !",
    "created_at": "2010-02-24T01:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72165",
    "user": "abmasse"
}
```

Attachment

I forgot to mention that equality tests are indeed improved in some cases, and I haven't encountered any worse case, which is good !



---

archive/issue_comments_072166.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-24T01:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72166",
    "user": "slabbe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072167.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8187_equality_words-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8187/trac_8187_equality_words-sl.patch)\n2. [trac_8187_review-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8187/trac_8187_review-abm.patch)",
    "created_at": "2010-03-02T21:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72167",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8187_equality_words-sl.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8187/trac_8187_equality_words-sl.patch)
2. [trac_8187_review-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8187/trac_8187_review-abm.patch)



---

archive/issue_comments_072168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8187#issuecomment-72168",
    "user": "mvngu"
}
```

Resolution: fixed
