# Issue 7093: fast_eval -- numerical noise on OS X 10.6

archive/issues_007093.json:
```json
{
    "body": "Assignee: tbd\n\n```\nsage -t -long \"devel/sage/sage/ext/fast_eval.pyx\"\n**********************************************************************\nFile \"/Users/was/build/sage-4.1.2.rc0/devel/sage/sage/ext/fast_eval.pyx\", line 1080:\n    sage: f(0.5)\nExpected:\n    0.5235987755982989...\nGot:\n    0.52359877559829882\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_32\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/was/.sage//tmp/.doctest_fast_eval.py\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7093\n\n",
    "created_at": "2009-10-01T19:43:40Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "fast_eval -- numerical noise on OS X 10.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7093",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

```
sage -t -long "devel/sage/sage/ext/fast_eval.pyx"
**********************************************************************
File "/Users/was/build/sage-4.1.2.rc0/devel/sage/sage/ext/fast_eval.pyx", line 1080:
    sage: f(0.5)
Expected:
    0.5235987755982989...
Got:
    0.52359877559829882
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_32
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/was/.sage//tmp/.doctest_fast_eval.py
```

Issue created by migration from https://trac.sagemath.org/ticket/7093





---

archive/issue_comments_058506.json:
```json
{
    "body": "Attachment [trac_7093.patch](tarball://root/attachments/some-uuid/ticket7093/trac_7093.patch) by @williamstein created at 2009-10-01 19:45:12",
    "created_at": "2009-10-01T19:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7093#issuecomment-58506",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7093.patch](tarball://root/attachments/some-uuid/ticket7093/trac_7093.patch) by @williamstein created at 2009-10-01 19:45:12



---

archive/issue_comments_058507.json:
```json
{
    "body": "Doesn't seem it can do any harm. Applies and passes on *Linux*. Release manager may want to see if this works on OS X as advertised.",
    "created_at": "2009-10-01T19:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7093#issuecomment-58507",
    "user": "https://github.com/TimDumol"
}
```

Doesn't seem it can do any harm. Applies and passes on *Linux*. Release manager may want to see if this works on OS X as advertised.



---

archive/issue_events_016773.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-01T20:01:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7093",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7093#event-16773"
}
```



---

archive/issue_comments_058508.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-01T20:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7093#issuecomment-58508",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_058509.json:
```json
{
    "body": "for uniqueness of author names",
    "created_at": "2017-07-19T09:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7093#issuecomment-58509",
    "user": "https://github.com/fchapoton"
}
```

for uniqueness of author names
