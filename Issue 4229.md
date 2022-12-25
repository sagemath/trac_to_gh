# Issue 4229: special functions should use mpfr when available

archive/issues_004229.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jdemeyer\n\nMPFR has fast implementations for restricted types of arguments in some special functions, e.g. Bessel J and Y with integer order and positive real argument.  We should be using these instead of Pari or Maxima or Scipy whenever that is feasible.\n\nExample:\n\n```\nsage: a = RR(2)\nsage: timeit(\"bessel_J(1, a)\")\n625 loops, best of 3: 370 \u00b5s per loop\nsage: timeit(\"a.j1()\")\n625 loops, best of 3: 13.9 \u00b5s per loop\n```\n\nThat's 26 times faster than Pari.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4229\n\n",
    "created_at": "2008-10-01T09:55:56Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "special functions should use mpfr when available",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4229",
    "user": "https://github.com/aghitza"
}
```
Assignee: @burcin

CC:  @jdemeyer

MPFR has fast implementations for restricted types of arguments in some special functions, e.g. Bessel J and Y with integer order and positive real argument.  We should be using these instead of Pari or Maxima or Scipy whenever that is feasible.

Example:

```
sage: a = RR(2)
sage: timeit("bessel_J(1, a)")
625 loops, best of 3: 370 µs per loop
sage: timeit("a.j1()")
625 loops, best of 3: 13.9 µs per loop
```

That's 26 times faster than Pari.

Issue created by migration from https://trac.sagemath.org/ticket/4229





---

archive/issue_comments_030672.json:
```json
{
    "body": "Or maybe we should use mpmath - there are a number of tickets about that.  Such as Alex's own comment in #3426 :)",
    "created_at": "2011-03-16T15:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4229#issuecomment-30672",
    "user": "https://github.com/kcrisman"
}
```

Or maybe we should use mpmath - there are a number of tickets about that.  Such as Alex's own comment in #3426 :)



---

archive/issue_comments_030673.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2011-03-16T15:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4229#issuecomment-30673",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_030674.json:
```json
{
    "body": "This ticket is too broad, I suggest we close it as invalid.\n\nAt the time it was created, there was no general framework to handle these functions. The (not so) new pynac-based symbolics provide this framework. It is true that a lot of work is still needed to sort these numerical evaluation issues out, but we need a separate specific ticket for each issue.\n\nSee [symbolics/functions](symbolics-functions) for an overview on the progress of symbolic functions.",
    "created_at": "2011-06-14T18:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4229#issuecomment-30674",
    "user": "https://github.com/burcin"
}
```

This ticket is too broad, I suggest we close it as invalid.

At the time it was created, there was no general framework to handle these functions. The (not so) new pynac-based symbolics provide this framework. It is true that a lot of work is still needed to sort these numerical evaluation issues out, but we need a separate specific ticket for each issue.

See [symbolics/functions](symbolics-functions) for an overview on the progress of symbolic functions.



---

archive/issue_comments_030675.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd31\".",
    "created_at": "2011-06-14T18:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4229#issuecomment-30675",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "sd31".



---

archive/issue_comments_030676.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-06-14T18:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4229#issuecomment-30676",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_030677.json:
```json
{
    "body": "Agreed.  This wiki page solves the problem.",
    "created_at": "2011-06-14T18:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4229#issuecomment-30677",
    "user": "https://github.com/kcrisman"
}
```

Agreed.  This wiki page solves the problem.



---

archive/issue_comments_030678.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-14T18:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4229#issuecomment-30678",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009569.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-06-14T19:11:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4229",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4229#event-9569"
}
```



---

archive/issue_comments_030679.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-06-14T20:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4229",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4229#issuecomment-30679",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_009570.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-06-14T20:39:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4229",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4229#event-9570"
}
```
