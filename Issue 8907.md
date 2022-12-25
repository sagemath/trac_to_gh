# Issue 8907: build Python as a shared library

archive/issues_008907.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis is needed by #8542 .  There is an spkg at http://sage.math.washington.edu/home/mhansen/python-2.6.4.p8.spkg but it requires lots of testing.  Also, the changes are not committed to the repository.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8907\n\n",
    "created_at": "2010-05-06T17:10:55Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "build Python as a shared library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8907",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @aghitza

This is needed by #8542 .  There is an spkg at http://sage.math.washington.edu/home/mhansen/python-2.6.4.p8.spkg but it requires lots of testing.  Also, the changes are not committed to the repository.

Issue created by migration from https://trac.sagemath.org/ticket/8907





---

archive/issue_events_021761.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-05-06T17:11:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "milestone": "sage-4.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8907#event-21761"
}
```



---

archive/issue_comments_081895.json:
```json
{
    "body": "Changing component from algebra to cygwin.",
    "created_at": "2010-05-06T17:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8907#issuecomment-81895",
    "user": "https://github.com/mwhansen"
}
```

Changing component from algebra to cygwin.



---

archive/issue_comments_081896.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-06T17:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8907#issuecomment-81896",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081897.json:
```json
{
    "body": "Check on OS X, we don't need --enable-shared.  I'm check on t2 now.  The spkg will have to be updated accordingly.",
    "created_at": "2010-05-06T17:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8907#issuecomment-81897",
    "user": "https://github.com/mwhansen"
}
```

Check on OS X, we don't need --enable-shared.  I'm check on t2 now.  The spkg will have to be updated accordingly.



---

archive/issue_comments_081898.json:
```json
{
    "body": "--enabled-shared fails on t2 because of http://bugs.python.org/issue1628484 .  We need to apply the patch there.",
    "created_at": "2010-05-25T05:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8907#issuecomment-81898",
    "user": "https://github.com/mwhansen"
}
```

--enabled-shared fails on t2 because of http://bugs.python.org/issue1628484 .  We need to apply the patch there.



---

archive/issue_events_021762.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-05-26T00:44:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8907#event-21762"
}
```



---

archive/issue_comments_081899.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T00:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8907#issuecomment-81899",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
