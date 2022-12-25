# Issue 1144: mpfr to RQDF coercion

archive/issues_001144.json:
```json
{
    "body": "Assignee: somebody\n\nI do not understand the following in RQDF??:\n\n        The rings that canonically coerce to the real quad double field are:\n* the mpfr real field, if its precision is at least 212 bits\n                                           <sup>^</sup><sup>^</sup><sup>^</sup><sup>^</sup><sup>^</sup>^^\n\nOn the contrary, RealField(p) should coerce to RQDF **exactly** for p <= 212 (in fact this\nshould be 215 = 53 + 1 + 53 + 1 + 53 + 1 + 53 since if you round to nearest, then the remainder\nis smaller than 1/2 ulp of the most significant part).\n\nThus coercion from RealField() to RQDF should always work.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1144\n\n",
    "created_at": "2007-11-11T13:09:12Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "mpfr to RQDF coercion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1144",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: somebody

I do not understand the following in RQDF??:

        The rings that canonically coerce to the real quad double field are:
* the mpfr real field, if its precision is at least 212 bits
                                           <sup>^</sup><sup>^</sup><sup>^</sup><sup>^</sup><sup>^</sup>^^

On the contrary, RealField(p) should coerce to RQDF **exactly** for p <= 212 (in fact this
should be 215 = 53 + 1 + 53 + 1 + 53 + 1 + 53 since if you round to nearest, then the remainder
is smaller than 1/2 ulp of the most significant part).

Thus coercion from RealField() to RQDF should always work.




Issue created by migration from https://trac.sagemath.org/ticket/1144





---

archive/issue_comments_006931.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2007-11-11T14:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1144#issuecomment-6931",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_006932.json:
```json
{
    "body": "This is the \"canonical coercion\", which is a somewhat different concept than coercion (the terminology is bad, and may change).\n\nCanonical coercions are the coercions that Sage applies automatically, for instance when doing arithmetic.  If you try to add (or multiply, etc.) an element of A and an element of B, sage will look for a canonical coercion from A to B and a canonical coercion from B to A.  (Only one of these should exist.)  It will apply this coercion, and then do the arithmetic.\n\nIn general, the Sage policy is to prefer to throw away information, rather than make up information; so the product of an RR and an RQDF is an RR.\n\nExplicit coercions are more general; for instance, both RR(RQDF(1)) and RQDF(RR(1)) work.\n\nSo the fact that the canonical coercions seem \"backward\" is by design.  However, the use of 212 instead of 215 does seem to be a bug.",
    "created_at": "2007-11-15T02:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1144#issuecomment-6932",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

This is the "canonical coercion", which is a somewhat different concept than coercion (the terminology is bad, and may change).

Canonical coercions are the coercions that Sage applies automatically, for instance when doing arithmetic.  If you try to add (or multiply, etc.) an element of A and an element of B, sage will look for a canonical coercion from A to B and a canonical coercion from B to A.  (Only one of these should exist.)  It will apply this coercion, and then do the arithmetic.

In general, the Sage policy is to prefer to throw away information, rather than make up information; so the product of an RR and an RQDF is an RR.

Explicit coercions are more general; for instance, both RR(RQDF(1)) and RQDF(RR(1)) work.

So the fact that the canonical coercions seem "backward" is by design.  However, the use of 212 instead of 215 does seem to be a bug.



---

archive/issue_comments_006933.json:
```json
{
    "body": "Even if one can represent 215 bit numbers exactly with RDQF, the arithmetic it seems is only done to 212 bits of precision according to the documentation, so this would seem to be the correct bound. \n\nhttp://www.cs.berkeley.edu/~yozo/",
    "created_at": "2007-12-04T08:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1144#issuecomment-6933",
    "user": "https://github.com/robertwb"
}
```

Even if one can represent 215 bit numbers exactly with RDQF, the arithmetic it seems is only done to 212 bits of precision according to the documentation, so this would seem to be the correct bound. 

http://www.cs.berkeley.edu/~yozo/



---

archive/issue_comments_006934.json:
```json
{
    "body": "Should this be marked as invalid then?",
    "created_at": "2007-12-06T21:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1144#issuecomment-6934",
    "user": "https://github.com/mwhansen"
}
```

Should this be marked as invalid then?



---

archive/issue_comments_006935.json:
```json
{
    "body": "Since we are removing RQDF, I'm going to mark this as invalid.",
    "created_at": "2008-11-14T08:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1144#issuecomment-6935",
    "user": "https://github.com/mwhansen"
}
```

Since we are removing RQDF, I'm going to mark this as invalid.



---

archive/issue_comments_006936.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-11-14T08:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1144#issuecomment-6936",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_001271.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-11-14T08:34:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1144",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1144#event-1271"
}
```
