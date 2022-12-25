# Issue 5091: find_root should call fast_float

archive/issues_005091.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jasongrout\n\n\n```\nsage: f(x) = sin(x)-cos(x)\nsage: g = f._fast_float_()\n\nsage: timeit(\"find_root(f, 0, pi)\")\n625 loops, best of 3: 154 \u00b5s per loop\n\nsage: timeit(\"find_root(g, 0, pi)\")\n625 loops, best of 3: 24 \u00b5s per loop\n```\n\n\nSee also http://groups.google.com/group/sage-devel/browse_thread/thread/927319a4fa61ae3b/9fc80aa9c114e041\n\nIssue created by migration from https://trac.sagemath.org/ticket/5091\n\n",
    "created_at": "2009-01-24T22:05:03Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "find_root should call fast_float",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5091",
    "user": "https://github.com/robertwb"
}
```
Assignee: @burcin

CC:  @jasongrout


```
sage: f(x) = sin(x)-cos(x)
sage: g = f._fast_float_()

sage: timeit("find_root(f, 0, pi)")
625 loops, best of 3: 154 µs per loop

sage: timeit("find_root(g, 0, pi)")
625 loops, best of 3: 24 µs per loop
```


See also http://groups.google.com/group/sage-devel/browse_thread/thread/927319a4fa61ae3b/9fc80aa9c114e041

Issue created by migration from https://trac.sagemath.org/ticket/5091





---

archive/issue_comments_038719.json:
```json
{
    "body": "3.4 is for ReST tickets only.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T23:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5091#issuecomment-38719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

3.4 is for ReST tickets only.

Cheers,

Michael



---

archive/issue_comments_038720.json:
```json
{
    "body": "Incorporating the time it takes to call fast_float, the speedup is not that radical:\n\n```\nsage: var('x')\nx\nsage: from sage.ext.fast_eval import fast_float\nsage: timeit(\"find_root(sin(x)-cos(x), 0, pi)\")\n625 loops, best of 3: 441 \u00b5s per loop\nsage: timeit(\"find_root(fast_float(sin(x)-cos(x), x), 0, pi)\")\n625 loops, best of 3: 393 \u00b5s per loop\n```\n\nIts better for clients to call fast_float themselves, if they're using find_root inside a loop.",
    "created_at": "2009-07-29T16:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5091#issuecomment-38720",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Incorporating the time it takes to call fast_float, the speedup is not that radical:

```
sage: var('x')
x
sage: from sage.ext.fast_eval import fast_float
sage: timeit("find_root(sin(x)-cos(x), 0, pi)")
625 loops, best of 3: 441 µs per loop
sage: timeit("find_root(fast_float(sin(x)-cos(x), x), 0, pi)")
625 loops, best of 3: 393 µs per loop
```

Its better for clients to call fast_float themselves, if they're using find_root inside a loop.



---

archive/issue_comments_038721.json:
```json
{
    "body": "There is a small speedup here, so why not call it?",
    "created_at": "2010-01-17T09:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5091#issuecomment-38721",
    "user": "https://github.com/jasongrout"
}
```

There is a small speedup here, so why not call it?



---

archive/issue_comments_038722.json:
```json
{
    "body": "The point is that there should be a big speedup--I'm going to try and track down why construction is so expensive.",
    "created_at": "2010-01-17T10:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5091#issuecomment-38722",
    "user": "https://github.com/robertwb"
}
```

The point is that there should be a big speedup--I'm going to try and track down why construction is so expensive.



---

archive/issue_comments_038723.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-12-07T08:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5091#issuecomment-38723",
    "user": "https://github.com/rwst"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_038724.json:
```json
{
    "body": "Actually the speedup is 13x here (Sage 7.5beta5) only if the fast float already exists.\n\n```\nsage: timeit(\"find_root(f, 0, pi)\")\n625 loops, best of 3: 131 \u00b5s per loop\nsage: timeit(\"find_root(g, 0, pi)\")\n625 loops, best of 3: 10.2 \u00b5s per loop\nsage: timeit(\"find_root(sin(x)-cos(x), 0, pi)\")\n625 loops, best of 3: 170 \u00b5s per loop\nsage: timeit(\"find_root(fast_float(sin(x)-cos(x), x), 0, pi)\")\n625 loops, best of 3: 161 \u00b5s per loop\n\nsage: timeit('_ = sin(x)-cos(x)')\n625 loops, best of 3: 9.3 \u00b5s per loop\nsage: timeit(\"_ = fast_float(sin(x)-cos(x), x)\")\n625 loops, best of 3: 140 \u00b5s per loop\n```\n\nThe creation of `sin(x)-cos(x)` takes 10\u00b5s, `find_root` of a fast float takes also 10\u00b5s. What is slow is creation of the fast float (130\u00b5s) and `find_root` of the normal expression (120\u00b5s). So there is no gain converting to fast float because conversion eats it all.\n\nTherefore I propose to close this ticket.",
    "created_at": "2016-12-07T08:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5091#issuecomment-38724",
    "user": "https://github.com/rwst"
}
```

Actually the speedup is 13x here (Sage 7.5beta5) only if the fast float already exists.

```
sage: timeit("find_root(f, 0, pi)")
625 loops, best of 3: 131 µs per loop
sage: timeit("find_root(g, 0, pi)")
625 loops, best of 3: 10.2 µs per loop
sage: timeit("find_root(sin(x)-cos(x), 0, pi)")
625 loops, best of 3: 170 µs per loop
sage: timeit("find_root(fast_float(sin(x)-cos(x), x), 0, pi)")
625 loops, best of 3: 161 µs per loop

sage: timeit('_ = sin(x)-cos(x)')
625 loops, best of 3: 9.3 µs per loop
sage: timeit("_ = fast_float(sin(x)-cos(x), x)")
625 loops, best of 3: 140 µs per loop
```

The creation of `sin(x)-cos(x)` takes 10µs, `find_root` of a fast float takes also 10µs. What is slow is creation of the fast float (130µs) and `find_root` of the normal expression (120µs). So there is no gain converting to fast float because conversion eats it all.

Therefore I propose to close this ticket.



---

archive/issue_comments_038725.json:
```json
{
    "body": "Sounds reasonable to me.  Nice hunting.",
    "created_at": "2017-07-11T14:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5091#issuecomment-38725",
    "user": "https://github.com/kcrisman"
}
```

Sounds reasonable to me.  Nice hunting.



---

archive/issue_comments_038726.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-12-05T14:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5091#issuecomment-38726",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_038727.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-12-12T08:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5091",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5091#issuecomment-38727",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix



---

archive/issue_events_005337.json:
```json
{
    "actor": "@embray",
    "created_at": "2017-12-12T08:23:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5091",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5091#event-5337"
}
```
