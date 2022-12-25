# Issue 2281: elliptic_curve_finite_field: order caching problem

archive/issues_002281.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe problem, caused by the patches to #1130, are that the cached field `elliptic_curve_finite_field.__order` which is python-mangled to `elliptic_curve_finite_field._elliptic_curve_finite_field_order`, was being accessed (and even set) by elements of the `EllipticCurvePoint_finite_field` class.\n\nSolution: rename the field `_order` (with a single underscore) to show that it is intended to be private but can still be accessed easily by \"friendly\" classes which know what they are doing.\n\nPatch (based on 2.10.2) to follow will address some other issues with `elliptic_curve_finite_field`\n\nIssue created by migration from https://trac.sagemath.org/ticket/2281\n\n",
    "created_at": "2008-02-23T20:57:05Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "elliptic_curve_finite_field: order caching problem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2281",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

The problem, caused by the patches to #1130, are that the cached field `elliptic_curve_finite_field.__order` which is python-mangled to `elliptic_curve_finite_field._elliptic_curve_finite_field_order`, was being accessed (and even set) by elements of the `EllipticCurvePoint_finite_field` class.

Solution: rename the field `_order` (with a single underscore) to show that it is intended to be private but can still be accessed easily by "friendly" classes which know what they are doing.

Patch (based on 2.10.2) to follow will address some other issues with `elliptic_curve_finite_field`

Issue created by migration from https://trac.sagemath.org/ticket/2281





---

archive/issue_comments_015102.json:
```json
{
    "body": "Attachment [8681.patch](tarball://root/attachments/some-uuid/ticket2281/8681.patch) by @JohnCremona created at 2008-02-23 22:02:05\n\nPatch 8681.patch fixes this.  Most of the changes are dealing with the double/single underscore problem.  In addition, less use is made of pari/gp scripts for prime fields since the native code here handles more cases (larger primes), as in a new doctest which shows that we are closer to reasonable behaviour in cases such as in #351.  [The example in the doctest is a little smaller, but the example from #351 works fine in <5s).\n\nThe referee is welcome to ask for more detailed info.",
    "created_at": "2008-02-23T22:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2281#issuecomment-15102",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [8681.patch](tarball://root/attachments/some-uuid/ticket2281/8681.patch) by @JohnCremona created at 2008-02-23 22:02:05

Patch 8681.patch fixes this.  Most of the changes are dealing with the double/single underscore problem.  In addition, less use is made of pari/gp scripts for prime fields since the native code here handles more cases (larger primes), as in a new doctest which shows that we are closer to reasonable behaviour in cases such as in #351.  [The example in the doctest is a little smaller, but the example from #351 works fine in <5s).

The referee is welcome to ask for more detailed info.



---

archive/issue_events_005400.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-24T00:31:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2281",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2281#event-5400"
}
```



---

archive/issue_comments_015103.json:
```json
{
    "body": "Applies to 2.10.3.alpha0 and passes tests for me.",
    "created_at": "2008-02-28T00:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2281#issuecomment-15103",
    "user": "https://github.com/mwhansen"
}
```

Applies to 2.10.3.alpha0 and passes tests for me.



---

archive/issue_comments_015104.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T00:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2281#issuecomment-15104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc0



---

archive/issue_comments_015105.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T00:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2281#issuecomment-15105",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005401.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-28T00:30:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2281",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2281#event-5401"
}
```
