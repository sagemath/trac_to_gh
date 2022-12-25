# Issue 4230: implement arbitrary precision Bessel Y function

archive/issues_004230.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman @benjaminfjones\n\nAt the moment, Sage uses Maxima to compute the Bessel Y function.  This is slow and works only with the default 53 bits of precision.  It would be fairly easy to implement this:\n\n* for integer values of the order nu, use the mpfr yn function\n* for non-integer values of nu, use the formula $Y_nu(z) = (J_nu(z)*cos(nu*pi) - J_{-nu}(z))/sin(nu*pi)$, where J is the Bessel J function.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4230\n\n",
    "created_at": "2008-10-01T10:09:21Z",
    "labels": [
        "component: calculus",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "implement arbitrary precision Bessel Y function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4230",
    "user": "https://github.com/aghitza"
}
```
Assignee: @burcin

CC:  @kcrisman @benjaminfjones

At the moment, Sage uses Maxima to compute the Bessel Y function.  This is slow and works only with the default 53 bits of precision.  It would be fairly easy to implement this:

* for integer values of the order nu, use the mpfr yn function
* for non-integer values of nu, use the formula $Y_nu(z) = (J_nu(z)*cos(nu*pi) - J_{-nu}(z))/sin(nu*pi)$, where J is the Bessel J function.


Issue created by migration from https://trac.sagemath.org/ticket/4230





---

archive/issue_comments_030680.json:
```json
{
    "body": "It would also be nice to be able to evaluate Bessel functions with complex, or at least purely imaginary, arguments.",
    "created_at": "2008-10-07T06:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4230#issuecomment-30680",
    "user": "https://github.com/dandrake"
}
```

It would also be nice to be able to evaluate Bessel functions with complex, or at least purely imaginary, arguments.



---

archive/issue_comments_030681.json:
```json
{
    "body": "See #3426 (and review it!) for the Bessel functions other than Y.  The code computes values at arbitrary complex coefficients.",
    "created_at": "2008-10-07T11:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4230#issuecomment-30681",
    "user": "https://github.com/aghitza"
}
```

See #3426 (and review it!) for the Bessel functions other than Y.  The code computes values at arbitrary complex coefficients.



---

archive/issue_comments_030682.json:
```json
{
    "body": "Now that mpmath is included in Sage, why not just use mpmath's Bessel functions? http://mpmath.googlecode.com/svn/trunk/doc/build/functions/bessel.html\n\nThey seem to be very well-implemented, work to arbitrary precision, take complex arguments, and so on. Is this a good idea?",
    "created_at": "2009-10-09T04:06:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4230#issuecomment-30682",
    "user": "https://github.com/dandrake"
}
```

Now that mpmath is included in Sage, why not just use mpmath's Bessel functions? http://mpmath.googlecode.com/svn/trunk/doc/build/functions/bessel.html

They seem to be very well-implemented, work to arbitrary precision, take complex arguments, and so on. Is this a good idea?



---

archive/issue_comments_030683.json:
```json
{
    "body": "This would most likely be fixed by #4102.",
    "created_at": "2013-01-03T15:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4230#issuecomment-30683",
    "user": "https://github.com/kcrisman"
}
```

This would most likely be fixed by #4102.



---

archive/issue_comments_030684.json:
```json
{
    "body": "Yep, I'll add a related doctest in #4102 to address arbitrary precision numerical evaluation for bessel_Y.",
    "created_at": "2013-01-03T23:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4230#issuecomment-30684",
    "user": "https://github.com/benjaminfjones"
}
```

Yep, I'll add a related doctest in #4102 to address arbitrary precision numerical evaluation for bessel_Y.



---

archive/issue_comments_030685.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-08T17:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4230#issuecomment-30685",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_030686.json:
```json
{
    "body": "Confirmed that this is doctested there.",
    "created_at": "2013-02-08T17:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4230#issuecomment-30686",
    "user": "https://github.com/kcrisman"
}
```

Confirmed that this is doctested there.



---

archive/issue_comments_030687.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-08T17:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4230#issuecomment-30687",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_030688.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-02-17T20:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4230#issuecomment-30688",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_004467.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-02-17T20:10:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4230",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4230#event-4467"
}
```
