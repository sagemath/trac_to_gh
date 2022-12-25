# Issue 2106: Implement univariate polynomials over GF(2) via ntl.GF2X

archive/issues_002106.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @malb\n\nMarshall Buck on [sage-support] writes:\n\nIt is a shame that normal arithmetic for polys over GF(2) still seems\nto be implemented by the ntl ZZ_pX library, which is usually at least\n10 times slower than GF2X,  up to degree 2<sup>17</sup> anyway. In that range\nGF2X matches the speed of magma.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2106\n\n",
    "created_at": "2008-02-08T09:44:08Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Implement univariate polynomials over GF(2) via ntl.GF2X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2106",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

CC:  @malb

Marshall Buck on [sage-support] writes:

It is a shame that normal arithmetic for polys over GF(2) still seems
to be implemented by the ntl ZZ_pX library, which is usually at least
10 times slower than GF2X,  up to degree 2<sup>17</sup> anyway. In that range
GF2X matches the speed of magma.

Issue created by migration from https://trac.sagemath.org/ticket/2106





---

archive/issue_comments_013702.json:
```json
{
    "body": "This is related to #4302, and will probably be fixed with #4302, thus might be marked as\nduplicate of #4302.",
    "created_at": "2008-10-18T11:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2106#issuecomment-13702",
    "user": "https://github.com/zimmermann6"
}
```

This is related to #4302, and will probably be fixed with #4302, thus might be marked as
duplicate of #4302.



---

archive/issue_events_005052.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2008-11-01T22:18:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2106",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2106#event-5052"
}
```



---

archive/issue_events_005053.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2008-11-01T22:18:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2106",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2106#event-5053"
}
```



---

archive/issue_comments_013703.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-11-01T22:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2106#issuecomment-13703",
    "user": "https://github.com/malb"
}
```

Resolution: duplicate



---

archive/issue_comments_013704.json:
```json
{
    "body": "This is a duplicate #4302",
    "created_at": "2008-11-01T22:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2106#issuecomment-13704",
    "user": "https://github.com/malb"
}
```

This is a duplicate #4302
