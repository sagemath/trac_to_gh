# Issue 3709: QuaternionAlgebraElement.sqrt()

archive/issues_003709.json:
```json
{
    "body": "Assignee: tbd\n\nThis method currently does not exist, but it should.  For an outline of an algorithm see: http://www.mathreference.com/ring-q,sqr.html\n\nThe only issue is that, as far as I know, there is no standard for which square root to take like there is over C or R.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3709\n\n",
    "created_at": "2008-07-23T00:00:33Z",
    "labels": [
        "algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "QuaternionAlgebraElement.sqrt()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3709",
    "user": "epotash"
}
```
Assignee: tbd

This method currently does not exist, but it should.  For an outline of an algorithm see: http://www.mathreference.com/ring-q,sqr.html

The only issue is that, as far as I know, there is no standard for which square root to take like there is over C or R.

Issue created by migration from https://trac.sagemath.org/ticket/3709





---

archive/issue_comments_026329.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-12-18T17:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3709#issuecomment-26329",
    "user": "fwclarke"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_026330.json:
```json
{
    "body": "In the quaternions there are infinitely many square-roots of -1: (xi + yj + zk)<sup>2</sup> = -1 for any real numbers x, y, z such that x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup> = 1. \u00a0I don't know how to prefer one of these.",
    "created_at": "2011-12-18T17:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3709#issuecomment-26330",
    "user": "fwclarke"
}
```

In the quaternions there are infinitely many square-roots of -1: (xi + yj + zk)<sup>2</sup> = -1 for any real numbers x, y, z such that x<sup>2</sup> + y<sup>2</sup> + z<sup>2</sup> = 1.  I don't know how to prefer one of these.
