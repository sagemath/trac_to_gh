# Issue 8483: Multiplication faster than squaring?

archive/issues_008483.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis is odd:\n\n\n```python\nsage: R=GF(2^283,'a')\nsage: x=R.random_element()\nsage: y=R.random_element()\n```\n\n\nFirst, note that squaring is slower than multiplication:\n\n\n```python\nsage: %timeit z=x^2\n625 loops, best of 3: 3.79 \u00b5s per loop\n```\n\n\n\n```python\nsage: %timeit z=x*y\n625 loops, best of 3: 3.17 \u00b5s per loop\n```\n\n\nNow observe that squaring done differently is indeed faster:\n\n\n```python\nsage: %timeit z=x*x\n625 loops, best of 3: 1.91 \u00b5s per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8483\n\n",
    "created_at": "2010-03-09T15:37:58Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Multiplication faster than squaring?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8483",
    "user": "https://github.com/malb"
}
```
Assignee: @aghitza

This is odd:


```python
sage: R=GF(2^283,'a')
sage: x=R.random_element()
sage: y=R.random_element()
```


First, note that squaring is slower than multiplication:


```python
sage: %timeit z=x^2
625 loops, best of 3: 3.79 µs per loop
```



```python
sage: %timeit z=x*y
625 loops, best of 3: 3.17 µs per loop
```


Now observe that squaring done differently is indeed faster:


```python
sage: %timeit z=x*x
625 loops, best of 3: 1.91 µs per loop
```


Issue created by migration from https://trac.sagemath.org/ticket/8483





---

archive/issue_comments_076327.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-10T21:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8483#issuecomment-76327",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076328.json:
```json
{
    "body": "This is mainly because of the Sage Integer in the exponent:\n\n```\nsage: R=GF(2^283,'a')\nsage: x=R.random_element()\n```\n\n\n\n```\nsage: two=2\nsage: %timeit z=x^two\n625 loops, best of 3: 4.07 \u00b5s per loop\n```\n\n\n\n```\nsage: two=int(2)\nsage: %timeit z=x^two\n625 loops, best of 3: 1.01 \u00b5s per loop\n```\n\n\nThis is still slightly slower than normal multiplication, probably because of overhead in the `^` operator:\n\n```\nsage: %timeit z=x*x\n625 loops, best of 3: 834 ns per loop\n```\n\n\nI suggest to close this ticket as \"invalid\" because this is essentially impossible to fix...",
    "created_at": "2010-10-10T21:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8483#issuecomment-76328",
    "user": "https://github.com/jdemeyer"
}
```

This is mainly because of the Sage Integer in the exponent:

```
sage: R=GF(2^283,'a')
sage: x=R.random_element()
```



```
sage: two=2
sage: %timeit z=x^two
625 loops, best of 3: 4.07 µs per loop
```



```
sage: two=int(2)
sage: %timeit z=x^two
625 loops, best of 3: 1.01 µs per loop
```


This is still slightly slower than normal multiplication, probably because of overhead in the `^` operator:

```
sage: %timeit z=x*x
625 loops, best of 3: 834 ns per loop
```


I suggest to close this ticket as "invalid" because this is essentially impossible to fix...



---

archive/issue_events_008665.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2010-11-23T17:35:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8483",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8483#event-8665"
}
```



---

archive/issue_comments_076329.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-11-23T17:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8483#issuecomment-76329",
    "user": "https://github.com/malb"
}
```

Resolution: wontfix



---

archive/issue_comments_076330.json:
```json
{
    "body": "I think \"needs_review\" as not intended.",
    "created_at": "2010-11-23T17:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8483#issuecomment-76330",
    "user": "https://github.com/malb"
}
```

I think "needs_review" as not intended.
