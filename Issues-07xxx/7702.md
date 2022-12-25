# Issue 7702: Handle interrupts better in the notebook

archive/issues_007702.json:
```json
{
    "body": "Assignee: @williamstein\n\nInterrupting the notebook is less robust than it used to be.  The attached worksheet is an example where the notebook fails to interrupt.  When this happens, the notebook acts as though it's interrupted.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7702\n\n",
    "closed_at": "2011-05-07T11:26:22Z",
    "created_at": "2009-12-16T03:17:24Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Handle interrupts better in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7702",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: @williamstein

Interrupting the notebook is less robust than it used to be.  The attached worksheet is an example where the notebook fails to interrupt.  When this happens, the notebook acts as though it's interrupted.

Issue created by migration from https://trac.sagemath.org/ticket/7702





---

archive/issue_comments_065959.json:
```json
{
    "body": "Attachment [interrupt test.sws](tarball://root/attachments/some-uuid/ticket7702/interrupt test.sws) by boothby created at 2009-12-16 03:17:42",
    "created_at": "2009-12-16T03:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-65959",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [interrupt test.sws](tarball://root/attachments/some-uuid/ticket7702/interrupt test.sws) by boothby created at 2009-12-16 03:17:42



---

archive/issue_comments_065960.json:
```json
{
    "body": "I have verified this.    It is a *very* bad bug, since it means that one thinks the notebook got interrupted, but it didn't.  This results in a seemingly totally broken worksheet, which must cause massive confusion to everybody, to say the least.",
    "created_at": "2009-12-16T03:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-65960",
    "user": "https://github.com/williamstein"
}
```

I have verified this.    It is a *very* bad bug, since it means that one thinks the notebook got interrupted, but it didn't.  This results in a seemingly totally broken worksheet, which must cause massive confusion to everybody, to say the least.



---

archive/issue_comments_065961.json:
```json
{
    "body": "(Oh, and it is surely my fault since I rewrote the interrupt code in the notebook separation.)",
    "created_at": "2009-12-16T03:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-65961",
    "user": "https://github.com/williamstein"
}
```

(Oh, and it is surely my fault since I rewrote the interrupt code in the notebook separation.)



---

archive/issue_comments_065962.json:
```json
{
    "body": "The patch at #5712 should fix the problem.",
    "created_at": "2010-01-18T06:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-65962",
    "user": "https://github.com/TimDumol"
}
```

The patch at #5712 should fix the problem.



---

archive/issue_comments_065963.json:
```json
{
    "body": "Hard to say what's going on here.  My guess would be a bare `except:` somewhere catching the `KeyboardInterrupt`.",
    "created_at": "2011-01-26T14:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-65963",
    "user": "https://github.com/jdemeyer"
}
```

Hard to say what's going on here.  My guess would be a bare `except:` somewhere catching the `KeyboardInterrupt`.



---

archive/issue_events_018399.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-07T11:26:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7702#event-18399"
}
```



---

archive/issue_comments_065964.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-05-07T11:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-65964",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_018400.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-07T11:26:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7702#event-18400"
}
```



---

archive/issue_comments_065965.json:
```json
{
    "body": "I cannot reproduce the problem anymore in recent versions of Sage, so I assume it got fixed by #9678.",
    "created_at": "2011-05-07T11:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-65965",
    "user": "https://github.com/jdemeyer"
}
```

I cannot reproduce the problem anymore in recent versions of Sage, so I assume it got fixed by #9678.
