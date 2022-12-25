# Issue 3368: bug in CartesianProduct

archive/issues_003368.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nHi,\n\nThe following is a bug that Bill Page found in Sage.  It is in the combinatorial\nclasses code  (mostly) by Mike Hansen, so maybe he'll fix it. \n\n```\nIn: http://modular.math.washington.edu/msri06/work/kohel/msri_magma.pdf\n\n \"A Brief Magma Tutorial\" by David R. Kohel gives this example:\n\n----------\n\nThe parent structure of a tuple is more important than in the case\nof sequences or sets.\n> C := CartesianProduct(Integers(),RationalField());\n> t := C!<1,1>;\n> Parent(t[2]);\nRational Field\n\n----------\n\nThe analogous computation in Sage 3.0.2 yields:\n\nsage: C = CartesianProduct(Integers(),RationalField())\n\n# case 1\nsage: t=C([1,1/2])\nsage: parent(t[0])\nInteger Ring\nsage: parent(t[1])\nRational Field\n\n# case 2\nsage: t=C([1,1])\nsage: parent(t[0])\nInteger Ring\nsage: parent(t[1])\nInteger Ring\n\n---------\n\nNotice that the parent of t[1] is incorrect in the 2nd case.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3368\n\n",
    "closed_at": "2017-01-21T18:03:11Z",
    "created_at": "2008-06-04T22:07:22Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in CartesianProduct",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3368",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Hi,

The following is a bug that Bill Page found in Sage.  It is in the combinatorial
classes code  (mostly) by Mike Hansen, so maybe he'll fix it. 

```
In: http://modular.math.washington.edu/msri06/work/kohel/msri_magma.pdf

 "A Brief Magma Tutorial" by David R. Kohel gives this example:

----------

The parent structure of a tuple is more important than in the case
of sequences or sets.
> C := CartesianProduct(Integers(),RationalField());
> t := C!<1,1>;
> Parent(t[2]);
Rational Field

----------

The analogous computation in Sage 3.0.2 yields:

sage: C = CartesianProduct(Integers(),RationalField())

# case 1
sage: t=C([1,1/2])
sage: parent(t[0])
Integer Ring
sage: parent(t[1])
Rational Field

# case 2
sage: t=C([1,1])
sage: parent(t[0])
Integer Ring
sage: parent(t[1])
Integer Ring

---------

Notice that the parent of t[1] is incorrect in the 2nd case.
```

Issue created by migration from https://trac.sagemath.org/ticket/3368





---

archive/issue_comments_023519.json:
```json
{
    "body": "This was never the intended functionality of CartesianProduct -- it is different than the CartesianProduct of Magma.  It was mainly intended to iterator over the cartesian product of a bunch of iterables in Python.  Maybe the name should be changed.",
    "created_at": "2008-06-04T22:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3368#issuecomment-23519",
    "user": "https://github.com/mwhansen"
}
```

This was never the intended functionality of CartesianProduct -- it is different than the CartesianProduct of Magma.  It was mainly intended to iterator over the cartesian product of a bunch of iterables in Python.  Maybe the name should be changed.



---

archive/issue_events_007586.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3368#event-7586"
}
```



---

archive/issue_events_007587.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3368#event-7587"
}
```



---

archive/issue_events_007588.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3368#event-7588"
}
```



---

archive/issue_events_007589.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3368#event-7589"
}
```



---

archive/issue_events_007590.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3368#event-7590"
}
```



---

archive/issue_events_007591.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3368#event-7591"
}
```



---

archive/issue_events_007592.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3368#event-7592"
}
```



---

archive/issue_events_007593.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2016-08-31T15:37:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3368#event-7593"
}
```



---

archive/issue_events_007594.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2016-08-31T15:37:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3368#event-7594"
}
```



---

archive/issue_comments_023520.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-08-31T15:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3368#issuecomment-23520",
    "user": "https://github.com/videlec"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023521.json:
```json
{
    "body": "This is now fixed (and moreover `CartesianProduct` is now deprecated)!",
    "created_at": "2016-08-31T15:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3368#issuecomment-23521",
    "user": "https://github.com/videlec"
}
```

This is now fixed (and moreover `CartesianProduct` is now deprecated)!



---

archive/issue_comments_023522.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-08-31T16:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3368#issuecomment-23522",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023523.json:
```json
{
    "body": "Confirmed:\n\n```\nsage: C = cartesian_product([Integers(),RationalField()])\nsage: c = C([1,1])\nsage: c\n(1, 1)\nsage: c[0].parent()\nInteger Ring\nsage: c[1].parent()\nRational Field\n\nsage: C = CartesianProduct(Integers(),RationalField())\n/opt/sage-git/src/bin/sage-ipython:1: DeprecationWarning: CartesianProduct is deprecated. Use cartesian_product instead\nSee http://trac.sagemath.org/18411 for details.\n  #!/usr/bin/env python\nsage: c = C([1,1])\nsage: c[0].parent()\nInteger Ring\nsage: c[1].parent()\nRational Field\n```\n\nYeah, let's close a 4 digits eight years old combinat ticket for cheap :-)",
    "created_at": "2016-08-31T16:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3368#issuecomment-23523",
    "user": "https://github.com/nthiery"
}
```

Confirmed:

```
sage: C = cartesian_product([Integers(),RationalField()])
sage: c = C([1,1])
sage: c
(1, 1)
sage: c[0].parent()
Integer Ring
sage: c[1].parent()
Rational Field

sage: C = CartesianProduct(Integers(),RationalField())
/opt/sage-git/src/bin/sage-ipython:1: DeprecationWarning: CartesianProduct is deprecated. Use cartesian_product instead
See http://trac.sagemath.org/18411 for details.
  #!/usr/bin/env python
sage: c = C([1,1])
sage: c[0].parent()
Integer Ring
sage: c[1].parent()
Rational Field
```

Yeah, let's close a 4 digits eight years old combinat ticket for cheap :-)



---

archive/issue_events_007595.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2017-01-21T18:03:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3368#event-7595"
}
```



---

archive/issue_comments_023524.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-01-21T18:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3368#issuecomment-23524",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid
