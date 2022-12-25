# Issue 204: bug in real number comparison or coercion

archive/issues_000204.json:
```json
{
    "body": "Assignee: somebody\n\nfrom Yi\n\n```\nOk, here is a weird bug:\non sage.math.washington.edu\n \nsage: sys.maxint\n9223372036854775807\nsage: sys.maxint >= 0.01\nFalse\n \nsage: sys.maxint >= int(0.01)\nTrue\n \nLooks to be a problem with <type 'sage.rings.real_mpfr.RealNumber'>\n \nAny ideas on how to fix this?\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/204\n\n",
    "created_at": "2007-01-21T03:45:11Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.9",
    "title": "bug in real number comparison or coercion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/204",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

from Yi

```
Ok, here is a weird bug:
on sage.math.washington.edu
 
sage: sys.maxint
9223372036854775807
sage: sys.maxint >= 0.01
False
 
sage: sys.maxint >= int(0.01)
True
 
Looks to be a problem with <type 'sage.rings.real_mpfr.RealNumber'>
 
Any ideas on how to fix this?
```

Issue created by migration from https://trac.sagemath.org/ticket/204





---

archive/issue_comments_000915.json:
```json
{
    "body": "```\nIt's a coercion issue:\n\nimport sys\nsage: sys.maxint\n9223372036854775807\nsage: type(sys.maxint)\n<type 'int'>\nsage: RR(sys.maxint)\n-1.00000000000000\nsage: RDF(sys.maxint)\n9.22337203685e+18\nsage: RealField(100)(sys.maxint)\n-1.0000000000000000000000000000\n```",
    "created_at": "2007-01-21T03:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/204#issuecomment-915",
    "user": "https://github.com/williamstein"
}
```

```
It's a coercion issue:

import sys
sage: sys.maxint
9223372036854775807
sage: type(sys.maxint)
<type 'int'>
sage: RR(sys.maxint)
-1.00000000000000
sage: RDF(sys.maxint)
9.22337203685e+18
sage: RealField(100)(sys.maxint)
-1.0000000000000000000000000000
```



---

archive/issue_comments_000916.json:
```json
{
    "body": "This is now fixed for sage > 1.8.  The problem in involved the \nreal number constructor.   While I was at it, I optimized that a lot.",
    "created_at": "2007-01-23T21:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/204#issuecomment-916",
    "user": "https://github.com/williamstein"
}
```

This is now fixed for sage > 1.8.  The problem in involved the 
real number constructor.   While I was at it, I optimized that a lot.



---

archive/issue_events_000407.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-23T21:50:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/204",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/204#event-407"
}
```



---

archive/issue_comments_000917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-23T21:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/204#issuecomment-917",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
