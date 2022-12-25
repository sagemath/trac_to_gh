# Issue 6150: numerical noise issues in 4.0.rc1

archive/issues_006150.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\n\n       sage -t  \"devel/sage/sage/matrix/matrix2.pyx\"\n       sage -t  \"devel/sage/sage/symbolic/expression.pyx\"\n\nsage -t  \"devel/sage/sage/matrix/matrix2.pyx\"\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/matrix/matrix2.pyx\", line 4964:\n    sage: m.change_ring(CDF).eigenvalues() # again for display purposes\nExpected:\n    [10.463115298 - 4.98835989975e-16*I, 7.42365754809 - 5.05298436852e-16*I, 3.36964641458 + 5.59670199836e-17*I, 1.25904669699 + 4.34508443713e-17*I,\n0.00689184179485 - 5.75358699674e-17*I, 0.330700789655 + 5.1816322259e-16*I]\nGot:\n    [10.463115298 - 4.46500755169e-16*I, 7.42365754809 + 1.02246204259e-16*I, 3.36964641458 - 2.25910315504e-16*I, 1.25904669699 + 7.13217318887e-17*I,\n0.00689184179485 - 3.00110164897e-16*I, 0.330700789655 + 1.23712186398e-16*I]\n**********************************************************************\n1 items had failures:\n   1 of  36 in __main__.example_81\n\nsage -t  \"devel/sage/sage/symbolic/expression.pyx\"\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/symbolic/expression.pyx\", line 4395:\n    sage: maxima('atanh(0.5)')\nExpected:\n    .5493061443340548\nGot:\n    .5493061443340549\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/symbolic/expression.pyx\", line 946:\n    sage: hash(x^y)\nExpected:\n    4043309056\nGot:\n    -251658240\n**********************************************************************\n2 items had failures:\n   1 of   9 in __main__.example_115\n   1 of  14 in __main__.example_33\n***Test Failed*** 2 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6150\n\n",
    "created_at": "2009-05-28T15:30:24Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "numerical noise issues in 4.0.rc1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6150",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd


```

       sage -t  "devel/sage/sage/matrix/matrix2.pyx"
       sage -t  "devel/sage/sage/symbolic/expression.pyx"

sage -t  "devel/sage/sage/matrix/matrix2.pyx"
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/matrix/matrix2.pyx", line 4964:
    sage: m.change_ring(CDF).eigenvalues() # again for display purposes
Expected:
    [10.463115298 - 4.98835989975e-16*I, 7.42365754809 - 5.05298436852e-16*I, 3.36964641458 + 5.59670199836e-17*I, 1.25904669699 + 4.34508443713e-17*I,
0.00689184179485 - 5.75358699674e-17*I, 0.330700789655 + 5.1816322259e-16*I]
Got:
    [10.463115298 - 4.46500755169e-16*I, 7.42365754809 + 1.02246204259e-16*I, 3.36964641458 - 2.25910315504e-16*I, 1.25904669699 + 7.13217318887e-17*I,
0.00689184179485 - 3.00110164897e-16*I, 0.330700789655 + 1.23712186398e-16*I]
**********************************************************************
1 items had failures:
   1 of  36 in __main__.example_81

sage -t  "devel/sage/sage/symbolic/expression.pyx"
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/symbolic/expression.pyx", line 4395:
    sage: maxima('atanh(0.5)')
Expected:
    .5493061443340548
Got:
    .5493061443340549
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/symbolic/expression.pyx", line 946:
    sage: hash(x^y)
Expected:
    4043309056
Got:
    -251658240
**********************************************************************
2 items had failures:
   1 of   9 in __main__.example_115
   1 of  14 in __main__.example_33
***Test Failed*** 2 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/6150





---

archive/issue_comments_048994.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-28T16:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6150#issuecomment-48994",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048995.json:
```json
{
    "body": "Changing assignee from tbd to @mwhansen.",
    "created_at": "2009-05-28T16:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6150#issuecomment-48995",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tbd to @mwhansen.



---

archive/issue_comments_048996.json:
```json
{
    "body": "I've attached a patch which fixes the above issues.",
    "created_at": "2009-05-28T16:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6150#issuecomment-48996",
    "user": "https://github.com/mwhansen"
}
```

I've attached a patch which fixes the above issues.



---

archive/issue_comments_048997.json:
```json
{
    "body": "Attachment [trac_6150.patch](tarball://root/attachments/some-uuid/ticket6150/trac_6150.patch) by @mwhansen created at 2009-05-28 16:54:09",
    "created_at": "2009-05-28T16:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6150#issuecomment-48997",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6150.patch](tarball://root/attachments/some-uuid/ticket6150/trac_6150.patch) by @mwhansen created at 2009-05-28 16:54:09



---

archive/issue_events_006399.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-05-28T19:12:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6150",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6150#event-6399"
}
```



---

archive/issue_comments_048998.json:
```json
{
    "body": "Merged in 4.0.rc2.",
    "created_at": "2009-05-28T19:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6150#issuecomment-48998",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.rc2.



---

archive/issue_comments_048999.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T19:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6150#issuecomment-48999",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
