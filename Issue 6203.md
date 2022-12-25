# Issue 6203: numerical noise on sparc solaris (trivial to fix)

archive/issues_006203.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t  devel/sage/sage/symbolic/expression.pyx\n**********************************************************************\nFile \"/home/wstein/build-4.4.0/mark/sage-4.0.1.alpha0/devel/sage-main/sage/symbolic/expression.pyx\", line 5486:\n    sage: f.find_minimum_on_interval(1, 5, tol=1e-3)\nExpected:\n    (-3.288371361890984, 3.42575079030572)\nGot:\n    (-3.2883713618909844, 3.42575079030572)\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_141\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6203\n\n",
    "created_at": "2009-06-03T23:11:19Z",
    "labels": [
        "component: porting: solaris",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "numerical noise on sparc solaris (trivial to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6203",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
sage -t  devel/sage/sage/symbolic/expression.pyx
**********************************************************************
File "/home/wstein/build-4.4.0/mark/sage-4.0.1.alpha0/devel/sage-main/sage/symbolic/expression.pyx", line 5486:
    sage: f.find_minimum_on_interval(1, 5, tol=1e-3)
Expected:
    (-3.288371361890984, 3.42575079030572)
Got:
    (-3.2883713618909844, 3.42575079030572)
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_141
***Test Failed*** 1 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/6203





---

archive/issue_comments_049467.json:
```json
{
    "body": "Changing assignee from tbd to @mwhansen.",
    "created_at": "2009-06-04T06:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6203#issuecomment-49467",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tbd to @mwhansen.



---

archive/issue_comments_049468.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-04T06:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6203#issuecomment-49468",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049469.json:
```json
{
    "body": "Attachment [trac_6203.patch](tarball://root/attachments/some-uuid/ticket6203/trac_6203.patch) by @williamstein created at 2009-06-04 08:24:42",
    "created_at": "2009-06-04T08:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6203#issuecomment-49469",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_6203.patch](tarball://root/attachments/some-uuid/ticket6203/trac_6203.patch) by @williamstein created at 2009-06-04 08:24:42



---

archive/issue_events_006453.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T09:05:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6203#event-6453"
}
```



---

archive/issue_comments_049470.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T09:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6203#issuecomment-49470",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049471.json:
```json
{
    "body": "Merged in 4.0.1.rc0.",
    "created_at": "2009-06-04T09:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6203#issuecomment-49471",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.rc0.
