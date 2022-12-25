# Issue 9539: segfault after memory exhausted using GF(9001)((x))

archive/issues_009539.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @burcin\n\nOn a MacBook Pro with 2Go (Mac OS X 10.4.11), filling the memory terminates with a seg fault:\n\ncode used:\n\n```\nfrom sage.all import LaurentSeriesRing, GF, timeit\nR = LaurentSeriesRing(GF(9001), 'x')\nf = R([1, 1])\nfor i in range(27):\n    timeit('g = f*f', number=1, repeat=1) ; f = f*f\n```\n\noutput is:\n\n```\n1 loops, best of 1: 16.5 s per loop\n1 loops, best of 1: 28.4 s per loop\n1 loops, best of 1: 88.6 s per loop\npython(6488) malloc: *** vm_allocate(size=2147614720) failed (error code=3)\npython(6488) malloc: *** error: can't allocate region\npython(6488) malloc: *** set a breakpoint in szone_error to debug\n\n\n------------------------------------------------------------\nUnhandled SIGBUS: A bus error occured in Sage.\nThis probably occured because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9539\n\n",
    "created_at": "2010-07-18T15:55:11Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "segfault after memory exhausted using GF(9001)((x))",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9539",
    "user": "https://trac.sagemath.org/admin/accounts/users/fchyzak"
}
```
Assignee: @rlmill

CC:  @burcin

On a MacBook Pro with 2Go (Mac OS X 10.4.11), filling the memory terminates with a seg fault:

code used:

```
from sage.all import LaurentSeriesRing, GF, timeit
R = LaurentSeriesRing(GF(9001), 'x')
f = R([1, 1])
for i in range(27):
    timeit('g = f*f', number=1, repeat=1) ; f = f*f
```

output is:

```
1 loops, best of 1: 16.5 s per loop
1 loops, best of 1: 28.4 s per loop
1 loops, best of 1: 88.6 s per loop
python(6488) malloc: *** vm_allocate(size=2147614720) failed (error code=3)
python(6488) malloc: *** error: can't allocate region
python(6488) malloc: *** set a breakpoint in szone_error to debug


------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```

Issue created by migration from https://trac.sagemath.org/ticket/9539





---

archive/issue_comments_091773.json:
```json
{
    "body": "Changing assignee from @aghitza to @rlmill.",
    "created_at": "2010-09-08T11:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9539#issuecomment-91773",
    "user": "https://github.com/burcin"
}
```

Changing assignee from @aghitza to @rlmill.



---

archive/issue_comments_091774.json:
```json
{
    "body": "Changing component from basic arithmetic to memleak.",
    "created_at": "2010-09-08T11:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9539",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9539#issuecomment-91774",
    "user": "https://github.com/burcin"
}
```

Changing component from basic arithmetic to memleak.



---

archive/issue_events_023719.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9539",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9539#event-23719"
}
```



---

archive/issue_events_023720.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9539",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9539#event-23720"
}
```



---

archive/issue_events_023721.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9539",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9539#event-23721"
}
```



---

archive/issue_events_023722.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9539",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9539#event-23722"
}
```



---

archive/issue_events_023723.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9539",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9539#event-23723"
}
```



---

archive/issue_events_023724.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9539",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9539#event-23724"
}
```



---

archive/issue_events_023725.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9539",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9539#event-23725"
}
```
