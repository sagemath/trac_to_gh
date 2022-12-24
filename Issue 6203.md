# Issue 6203: numerical noise on sparc solaris (trivial to fix)

archive/issues_006203.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t  devel/sage/sage/symbolic/expression.pyx\n**********************************************************************\nFile \"/home/wstein/build-4.4.0/mark/sage-4.0.1.alpha0/devel/sage-main/sage/symbolic/expression.pyx\", line 5486:\n    sage: f.find_minimum_on_interval(1, 5, tol=1e-3)\nExpected:\n    (-3.288371361890984, 3.42575079030572)\nGot:\n    (-3.2883713618909844, 3.42575079030572)\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_141\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6203\n\n",
    "created_at": "2009-06-03T23:11:19Z",
    "labels": [
        "porting: Solaris",
        "blocker",
        "bug"
    ],
    "title": "numerical noise on sparc solaris (trivial to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6203",
    "user": "was"
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

archive/issue_comments_049562.json:
```json
{
    "body": "Changing assignee from tbd to mhansen.",
    "created_at": "2009-06-04T06:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6203#issuecomment-49562",
    "user": "mhansen"
}
```

Changing assignee from tbd to mhansen.



---

archive/issue_comments_049563.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-04T06:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6203#issuecomment-49563",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049564.json:
```json
{
    "body": "Attachment [trac_6203.patch](tarball://root/attachments/some-uuid/ticket6203/trac_6203.patch) by was created at 2009-06-04 08:24:42",
    "created_at": "2009-06-04T08:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6203#issuecomment-49564",
    "user": "was"
}
```

Attachment [trac_6203.patch](tarball://root/attachments/some-uuid/ticket6203/trac_6203.patch) by was created at 2009-06-04 08:24:42



---

archive/issue_comments_049565.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T09:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6203#issuecomment-49565",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049566.json:
```json
{
    "body": "Merged in 4.0.1.rc0.",
    "created_at": "2009-06-04T09:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6203#issuecomment-49566",
    "user": "mhansen"
}
```

Merged in 4.0.1.rc0.
