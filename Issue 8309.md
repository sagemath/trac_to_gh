# Issue 8309: speedup prime range

archive/issues_008309.json:
```json
{
    "body": "Assignee: was\n\nCC:  craigcitro\n\nUses Pari's `NEXT_PRIME_VIADIFF` directly, which avoids the intermediate GEN objects. Also adds a `py_ints` option for a 5x speedup, and is much faster for ranges not starting at 0. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8309\n\n",
    "created_at": "2010-02-20T01:49:28Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "speedup prime range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8309",
    "user": "robertwb"
}
```
Assignee: was

CC:  craigcitro

Uses Pari's `NEXT_PRIME_VIADIFF` directly, which avoids the intermediate GEN objects. Also adds a `py_ints` option for a 5x speedup, and is much faster for ranges not starting at 0. 

Issue created by migration from https://trac.sagemath.org/ticket/8309





---

archive/issue_comments_073698.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-20T01:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8309#issuecomment-73698",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073699.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-02-25T22:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8309#issuecomment-73699",
    "user": "zimmerma"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_073700.json:
```json
{
    "body": "Robert, an example is missing to demonstrate the speedup.\n\nPaul",
    "created_at": "2010-02-25T22:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8309#issuecomment-73700",
    "user": "zimmerma"
}
```

Robert, an example is missing to demonstrate the speedup.

Paul



---

archive/issue_comments_073701.json:
```json
{
    "body": "Attachment [8309-fast-primerange.patch](tarball://root/attachments/some-uuid/ticket8309/8309-fast-primerange.patch) by robertwb created at 2010-02-26 08:06:49",
    "created_at": "2010-02-26T08:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8309#issuecomment-73701",
    "user": "robertwb"
}
```

Attachment [8309-fast-primerange.patch](tarball://root/attachments/some-uuid/ticket8309/8309-fast-primerange.patch) by robertwb created at 2010-02-26 08:06:49



---

archive/issue_comments_073702.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-02-26T08:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8309#issuecomment-73702",
    "user": "robertwb"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_073703.json:
```json
{
    "body": "BEFORE\n\n\n```\nsage: timeit(\"prime_range(10)\", number=10000)\n10000 loops, best of 3: 57.8 \u00b5s per loop\nsage: timeit(\"prime_range(100)\", number=10000)\n10000 loops, best of 3: 61.2 \u00b5s per loop\nsage: timeit(\"prime_range(1000)\", number=10000)\n10000 loops, best of 3: 102 \u00b5s per loop\nsage: timeit(\"prime_range(1000,2000)\", number=10000)\n10000 loops, best of 3: 123 \u00b5s per loop\nsage: timeit(\"prime_range(1e6)\")\n5 loops, best of 3: 36.9 ms per loop\nsage: timeit(\"prime_range(2e6)\")\n5 loops, best of 3: 69.7 ms per loop\nsage: timeit(\"prime_range(2e6)\")\n5 loops, best of 3: 69.7 ms per loop\nsage: timeit(\"prime_range(1e6,2e6)\")\n5 loops, best of 3: 40.6 ms per loop\nsage: timeit(\"prime_range(1e6,1e6+100)\")\n25 loops, best of 3: 8.21 ms per loop\n```\n\n\nAFTER\n\n\n```\nsage: timeit(\"prime_range(10)\", number=10000)\n10000 loops, best of 3: 969 ns per loop\nsage: timeit(\"prime_range(100)\", number=10000)\n10000 loops, best of 3: 3.24 \u00b5s per loop\nsage: timeit(\"prime_range(1000)\", number=10000)\n10000 loops, best of 3: 30.3 \u00b5s per loop\nsage: timeit(\"prime_range(1000,2000)\", number=10000)\n10000 loops, best of 3: 22.2 \u00b5s per loop\nsage: timeit(\"prime_range(1e6)\")\n25 loops, best of 3: 28.5 ms per loop\nsage: timeit(\"prime_range(2e6)\")\n5 loops, best of 3: 53.8 ms per loop\nsage: timeit(\"prime_range(2e6)\")\n5 loops, best of 3: 55 ms per loop\nsage: timeit(\"prime_range(1e6,2e6)\")\n25 loops, best of 3: 25.6 ms per loop\nsage: timeit(\"prime_range(1e6,1e6+100)\")\n625 loops, best of 3: 259 \u00b5s per loop\n```\n\n\nAFTER INTS\n\n\n```\nsage: timeit(\"prime_range(10, py_ints=True)\", number=10000)\n10000 loops, best of 3: 1.27 \u00b5s per loop\nsage: timeit(\"prime_range(100, py_ints=True)\", number=10000)\n10000 loops, best of 3: 3.11 \u00b5s per loop\nsage: timeit(\"prime_range(1000, py_ints=True)\", number=10000)\n10000 loops, best of 3: 11.5 \u00b5s per loop\nsage: timeit(\"prime_range(1000, 2000, py_ints=True)\", number=10000)\n10000 loops, best of 3: 11.7 \u00b5s per loop\nsage: timeit(\"prime_range(1e6, py_ints=True)\")\n125 loops, best of 3: 4.1 ms per loop\nsage: timeit(\"prime_range(2e6, py_ints=True)\")\n125 loops, best of 3: 7.9 ms per loop\nsage: timeit(\"prime_range(2e6, py_ints=True)\")\n125 loops, best of 3: 7.83 ms per loop\nsage: timeit(\"prime_range(1e6,2e6, py_ints=True)\")\n125 loops, best of 3: 3.88 ms per loop\nsage: timeit(\"prime_range(1e6,1e6+100, py_ints=True)\")\n625 loops, best of 3: 260 \u00b5s per loop\n```\n\n\nI also cleaned up the patch a bit (e.g. using pari.init_primes rather than resetting diffptr manually).",
    "created_at": "2010-02-26T08:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8309#issuecomment-73703",
    "user": "robertwb"
}
```

BEFORE


```
sage: timeit("prime_range(10)", number=10000)
10000 loops, best of 3: 57.8 µs per loop
sage: timeit("prime_range(100)", number=10000)
10000 loops, best of 3: 61.2 µs per loop
sage: timeit("prime_range(1000)", number=10000)
10000 loops, best of 3: 102 µs per loop
sage: timeit("prime_range(1000,2000)", number=10000)
10000 loops, best of 3: 123 µs per loop
sage: timeit("prime_range(1e6)")
5 loops, best of 3: 36.9 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 69.7 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 69.7 ms per loop
sage: timeit("prime_range(1e6,2e6)")
5 loops, best of 3: 40.6 ms per loop
sage: timeit("prime_range(1e6,1e6+100)")
25 loops, best of 3: 8.21 ms per loop
```


AFTER


```
sage: timeit("prime_range(10)", number=10000)
10000 loops, best of 3: 969 ns per loop
sage: timeit("prime_range(100)", number=10000)
10000 loops, best of 3: 3.24 µs per loop
sage: timeit("prime_range(1000)", number=10000)
10000 loops, best of 3: 30.3 µs per loop
sage: timeit("prime_range(1000,2000)", number=10000)
10000 loops, best of 3: 22.2 µs per loop
sage: timeit("prime_range(1e6)")
25 loops, best of 3: 28.5 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 53.8 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 55 ms per loop
sage: timeit("prime_range(1e6,2e6)")
25 loops, best of 3: 25.6 ms per loop
sage: timeit("prime_range(1e6,1e6+100)")
625 loops, best of 3: 259 µs per loop
```


AFTER INTS


```
sage: timeit("prime_range(10, py_ints=True)", number=10000)
10000 loops, best of 3: 1.27 µs per loop
sage: timeit("prime_range(100, py_ints=True)", number=10000)
10000 loops, best of 3: 3.11 µs per loop
sage: timeit("prime_range(1000, py_ints=True)", number=10000)
10000 loops, best of 3: 11.5 µs per loop
sage: timeit("prime_range(1000, 2000, py_ints=True)", number=10000)
10000 loops, best of 3: 11.7 µs per loop
sage: timeit("prime_range(1e6, py_ints=True)")
125 loops, best of 3: 4.1 ms per loop
sage: timeit("prime_range(2e6, py_ints=True)")
125 loops, best of 3: 7.9 ms per loop
sage: timeit("prime_range(2e6, py_ints=True)")
125 loops, best of 3: 7.83 ms per loop
sage: timeit("prime_range(1e6,2e6, py_ints=True)")
125 loops, best of 3: 3.88 ms per loop
sage: timeit("prime_range(1e6,1e6+100, py_ints=True)")
625 loops, best of 3: 260 µs per loop
```


I also cleaned up the patch a bit (e.g. using pari.init_primes rather than resetting diffptr manually).



---

archive/issue_comments_073704.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-26T10:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8309#issuecomment-73704",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073705.json:
```json
{
    "body": "Robert, I got one doctest failure in `graphs/generic_graph.py`. However after cloning again 4.3.3, and testing again with your patch, it worked. Thus it might be to an interference with the other patches I've tried.\n\nOn my side (Core 2 Duo) I get:\n\n\n```\nBEFORE:\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: timeit(\"prime_range(10)\", number=10000)\n10000 loops, best of 3: 26.5 \u00b5s per loop\nsage: timeit(\"prime_range(100)\", number=10000)\n10000 loops, best of 3: 31 \u00b5s per loop\nsage: timeit(\"prime_range(1000)\", number=10000)\n10000 loops, best of 3: 65 \u00b5s per loop\nsage: timeit(\"prime_range(1000,2000)\", number=10000)\n10000 loops, best of 3: 81.1 \u00b5s per loop\nsage: timeit(\"prime_range(1e6)\")\n25 loops, best of 3: 24.9 ms per loop\nsage: timeit(\"prime_range(2e6)\")\n5 loops, best of 3: 45.9 ms per loop\nsage: timeit(\"prime_range(2e6)\")\n5 loops, best of 3: 45.8 ms per loop\nsage: timeit(\"prime_range(1e6,2e6)\")\n25 loops, best of 3: 28.3 ms per loop\nsage: timeit(\"prime_range(1e6,1e6+100)\")\n125 loops, best of 3: 5.47 ms per loop\n| Sage Version 4.3.3, Release Date: 2010-02-21                       |\n| Type notebook() for the GUI, and license() for information.        |\nAFTER:\nLoading Sage library. Current Mercurial branch is: 8309\nsage: timeit(\"prime_range(10)\", number=10000)\n10000 loops, best of 3: 649 ns per loop\nsage: timeit(\"prime_range(100)\", number=10000)\n10000 loops, best of 3: 1.79 \u00b5s per loop\nsage: timeit(\"prime_range(1000)\", number=10000)\n10000 loops, best of 3: 14.6 \u00b5s per loop\nsage: timeit(\"prime_range(1000,2000)\", number=10000)\n10000 loops, best of 3: 10.8 \u00b5s per loop\nsage: timeit(\"prime_range(1e6)\")\n25 loops, best of 3: 14.6 ms per loop\nsage: timeit(\"prime_range(2e6)\")\n25 loops, best of 3: 30.2 ms per loop\nsage: timeit(\"prime_range(2e6)\")\n25 loops, best of 3: 30.4 ms per loop\nsage: timeit(\"prime_range(1e6,2e6)\")\n25 loops, best of 3: 12.7 ms per loop\nsage: timeit(\"prime_range(1e6,1e6+100)\")\n625 loops, best of 3: 148 \u00b5s per loop\n\nAFTER INTS:\nsage: sage: timeit(\"prime_range(10, py_ints=True)\", number=10000)\n10000 loops, best of 3: 852 ns per loop\nsage: sage: timeit(\"prime_range(100, py_ints=True)\", number=10000)\n10000 loops, best of 3: 1.73 \u00b5s per loop\nsage: sage: timeit(\"prime_range(1000, py_ints=True)\", number=10000)\n10000 loops, best of 3: 6.95 \u00b5s per loop\nsage: sage: timeit(\"prime_range(1000, 2000, py_ints=True)\", number=10000)\n10000 loops, best of 3: 6.44 \u00b5s per loop\nsage: sage: timeit(\"prime_range(1e6, py_ints=True)\")\n125 loops, best of 3: 2.79 ms per loop\nsage: sage: timeit(\"prime_range(2e6, py_ints=True)\")\n125 loops, best of 3: 7.15 ms per loop\nsage: sage: timeit(\"prime_range(2e6, py_ints=True)\")\n125 loops, best of 3: 7.16 ms per loop\nsage: sage: timeit(\"prime_range(1e6,2e6, py_ints=True)\")\n125 loops, best of 3: 2.34 ms per loop\nsage: sage: timeit(\"prime_range(1e6,1e6+100, py_ints=True)\")\n625 loops, best of 3: 149 \u00b5s per loop\n```\n\nGiven that py_ints is faster for ranges larger than 100, I wonder why you didn't make it the default. Anyway a positive review. Great work!\n\nPaul",
    "created_at": "2010-02-26T10:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8309#issuecomment-73705",
    "user": "zimmerma"
}
```

Robert, I got one doctest failure in `graphs/generic_graph.py`. However after cloning again 4.3.3, and testing again with your patch, it worked. Thus it might be to an interference with the other patches I've tried.

On my side (Core 2 Duo) I get:


```
BEFORE:
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: timeit("prime_range(10)", number=10000)
10000 loops, best of 3: 26.5 µs per loop
sage: timeit("prime_range(100)", number=10000)
10000 loops, best of 3: 31 µs per loop
sage: timeit("prime_range(1000)", number=10000)
10000 loops, best of 3: 65 µs per loop
sage: timeit("prime_range(1000,2000)", number=10000)
10000 loops, best of 3: 81.1 µs per loop
sage: timeit("prime_range(1e6)")
25 loops, best of 3: 24.9 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 45.9 ms per loop
sage: timeit("prime_range(2e6)")
5 loops, best of 3: 45.8 ms per loop
sage: timeit("prime_range(1e6,2e6)")
25 loops, best of 3: 28.3 ms per loop
sage: timeit("prime_range(1e6,1e6+100)")
125 loops, best of 3: 5.47 ms per loop
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
AFTER:
Loading Sage library. Current Mercurial branch is: 8309
sage: timeit("prime_range(10)", number=10000)
10000 loops, best of 3: 649 ns per loop
sage: timeit("prime_range(100)", number=10000)
10000 loops, best of 3: 1.79 µs per loop
sage: timeit("prime_range(1000)", number=10000)
10000 loops, best of 3: 14.6 µs per loop
sage: timeit("prime_range(1000,2000)", number=10000)
10000 loops, best of 3: 10.8 µs per loop
sage: timeit("prime_range(1e6)")
25 loops, best of 3: 14.6 ms per loop
sage: timeit("prime_range(2e6)")
25 loops, best of 3: 30.2 ms per loop
sage: timeit("prime_range(2e6)")
25 loops, best of 3: 30.4 ms per loop
sage: timeit("prime_range(1e6,2e6)")
25 loops, best of 3: 12.7 ms per loop
sage: timeit("prime_range(1e6,1e6+100)")
625 loops, best of 3: 148 µs per loop

AFTER INTS:
sage: sage: timeit("prime_range(10, py_ints=True)", number=10000)
10000 loops, best of 3: 852 ns per loop
sage: sage: timeit("prime_range(100, py_ints=True)", number=10000)
10000 loops, best of 3: 1.73 µs per loop
sage: sage: timeit("prime_range(1000, py_ints=True)", number=10000)
10000 loops, best of 3: 6.95 µs per loop
sage: sage: timeit("prime_range(1000, 2000, py_ints=True)", number=10000)
10000 loops, best of 3: 6.44 µs per loop
sage: sage: timeit("prime_range(1e6, py_ints=True)")
125 loops, best of 3: 2.79 ms per loop
sage: sage: timeit("prime_range(2e6, py_ints=True)")
125 loops, best of 3: 7.15 ms per loop
sage: sage: timeit("prime_range(2e6, py_ints=True)")
125 loops, best of 3: 7.16 ms per loop
sage: sage: timeit("prime_range(1e6,2e6, py_ints=True)")
125 loops, best of 3: 2.34 ms per loop
sage: sage: timeit("prime_range(1e6,1e6+100, py_ints=True)")
625 loops, best of 3: 149 µs per loop
```

Given that py_ints is faster for ranges larger than 100, I wonder why you didn't make it the default. Anyway a positive review. Great work!

Paul



---

archive/issue_comments_073706.json:
```json
{
    "body": "Thanks. \n\nThe reason that py_ints isn't on by default is because then one wouldn't be able to do something like\n\n\n```\nfor p in prime_range(100):\n    if p.divides(N):\n        ...\n```\n",
    "created_at": "2010-02-26T11:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8309#issuecomment-73706",
    "user": "robertwb"
}
```

Thanks. 

The reason that py_ints isn't on by default is because then one wouldn't be able to do something like


```
for p in prime_range(100):
    if p.divides(N):
        ...
```




---

archive/issue_comments_073707.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8309#issuecomment-73707",
    "user": "mvngu"
}
```

Resolution: fixed
