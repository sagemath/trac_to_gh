# Issue 825: extending % to more sage types

archive/issues_000825.json:
```json
{
    "body": "Assignee: mhampton\n\nKeywords: remainder\n\nCurrently the following gives an error:\n10.23 % 2\nThe % should be extended to handle more types.\n\nIssue created by migration from https://trac.sagemath.org/ticket/825\n\n",
    "created_at": "2007-10-04T18:42:03Z",
    "labels": [
        "numerical",
        "minor",
        "bug"
    ],
    "title": "extending % to more sage types",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/825",
    "user": "mhampton"
}
```
Assignee: mhampton

Keywords: remainder

Currently the following gives an error:
10.23 % 2
The % should be extended to handle more types.

Issue created by migration from https://trac.sagemath.org/ticket/825





---

archive/issue_comments_005114.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-04T18:42:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/825#issuecomment-5114",
    "user": "mhampton"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005115.json:
```json
{
    "body": "And probably be placed into the coercion model as well (though this will be easier once cdef overrideable is in place).",
    "created_at": "2007-10-05T02:02:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/825#issuecomment-5115",
    "user": "robertwb"
}
```

And probably be placed into the coercion model as well (though this will be easier once cdef overrideable is in place).



---

archive/issue_comments_005116.json:
```json
{
    "body": "The remainder of floating-point numbers can be given a sense: see the C99 remainder function, and\nthe corresponding mpfr_remainder in MPFR.",
    "created_at": "2007-11-16T23:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/825#issuecomment-5116",
    "user": "zimmerma"
}
```

The remainder of floating-point numbers can be given a sense: see the C99 remainder function, and
the corresponding mpfr_remainder in MPFR.



---

archive/issue_comments_005117.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/825#issuecomment-5117",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_005118.json:
```json
{
    "body": "#5132 is a duplicate of that ticket.",
    "created_at": "2009-02-01T21:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/825#issuecomment-5118",
    "user": "zimmerma"
}
```

#5132 is a duplicate of that ticket.



---

archive/issue_comments_005119.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T07:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/825#issuecomment-5119",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005120.json:
```json
{
    "body": "Fixed via #5132 in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T07:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/825#issuecomment-5120",
    "user": "mabshoff"
}
```

Fixed via #5132 in Sage 3.3.alpha4.

Cheers,

Michael
