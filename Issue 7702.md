# Issue 7702: Handle interrupts better in the notebook

archive/issues_007702.json:
```json
{
    "body": "Assignee: was\n\nInterrupting the notebook is less robust than it used to be.  The attached worksheet is an example where the notebook fails to interrupt.  When this happens, the notebook acts as though it's interrupted.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7702\n\n",
    "created_at": "2009-12-16T03:17:24Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Handle interrupts better in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7702",
    "user": "boothby"
}
```
Assignee: was

Interrupting the notebook is less robust than it used to be.  The attached worksheet is an example where the notebook fails to interrupt.  When this happens, the notebook acts as though it's interrupted.

Issue created by migration from https://trac.sagemath.org/ticket/7702





---

archive/issue_comments_066075.json:
```json
{
    "body": "Attachment [interrupt test.sws](tarball://root/attachments/some-uuid/ticket7702/interrupt test.sws) by boothby created at 2009-12-16 03:17:42",
    "created_at": "2009-12-16T03:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-66075",
    "user": "boothby"
}
```

Attachment [interrupt test.sws](tarball://root/attachments/some-uuid/ticket7702/interrupt test.sws) by boothby created at 2009-12-16 03:17:42



---

archive/issue_comments_066076.json:
```json
{
    "body": "I have verified this.    It is a *very* bad bug, since it means that one thinks the notebook got interrupted, but it didn't.  This results in a seemingly totally broken worksheet, which must cause massive confusion to everybody, to say the least.",
    "created_at": "2009-12-16T03:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-66076",
    "user": "was"
}
```

I have verified this.    It is a *very* bad bug, since it means that one thinks the notebook got interrupted, but it didn't.  This results in a seemingly totally broken worksheet, which must cause massive confusion to everybody, to say the least.



---

archive/issue_comments_066077.json:
```json
{
    "body": "(Oh, and it is surely my fault since I rewrote the interrupt code in the notebook separation.)",
    "created_at": "2009-12-16T03:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-66077",
    "user": "was"
}
```

(Oh, and it is surely my fault since I rewrote the interrupt code in the notebook separation.)



---

archive/issue_comments_066078.json:
```json
{
    "body": "The patch at #5712 should fix the problem.",
    "created_at": "2010-01-18T06:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-66078",
    "user": "timdumol"
}
```

The patch at #5712 should fix the problem.



---

archive/issue_comments_066079.json:
```json
{
    "body": "Hard to say what's going on here.  My guess would be a bare `except:` somewhere catching the `KeyboardInterrupt`.",
    "created_at": "2011-01-26T14:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-66079",
    "user": "jdemeyer"
}
```

Hard to say what's going on here.  My guess would be a bare `except:` somewhere catching the `KeyboardInterrupt`.



---

archive/issue_comments_066080.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-05-07T11:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-66080",
    "user": "jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_066081.json:
```json
{
    "body": "I cannot reproduce the problem anymore in recent versions of Sage, so I assume it got fixed by #9678.",
    "created_at": "2011-05-07T11:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7702",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7702#issuecomment-66081",
    "user": "jdemeyer"
}
```

I cannot reproduce the problem anymore in recent versions of Sage, so I assume it got fixed by #9678.
