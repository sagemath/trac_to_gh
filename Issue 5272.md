# Issue 5272: [with patch, needs review] extend sage_input to work with RIF, CIF, AA, and QQbar

archive/issues_005272.json:
```json
{
    "body": "Assignee: cwitty\n\nThe attached patch adds support for intervals and for algebraic numbers to the sage_input system.  I'm going to mark it as Milestone 3.3, but I'm feeling no urgency about it... I'm happy to rebase against 3.4.whatever if it doesn't make it into 3.3.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5272\n\n",
    "created_at": "2009-02-14T15:20:25Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] extend sage_input to work with RIF, CIF, AA, and QQbar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5272",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

The attached patch adds support for intervals and for algebraic numbers to the sage_input system.  I'm going to mark it as Milestone 3.3, but I'm feeling no urgency about it... I'm happy to rebase against 3.4.whatever if it doesn't make it into 3.3.

Issue created by migration from https://trac.sagemath.org/ticket/5272





---

archive/issue_comments_040393.json:
```json
{
    "body": "Attachment [sage-input-qqbar.patch](tarball://root/attachments/some-uuid/ticket5272/sage-input-qqbar.patch) by cwitty created at 2009-02-14 15:20:54",
    "created_at": "2009-02-14T15:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5272#issuecomment-40393",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [sage-input-qqbar.patch](tarball://root/attachments/some-uuid/ticket5272/sage-input-qqbar.patch) by cwitty created at 2009-02-14 15:20:54



---

archive/issue_comments_040394.json:
```json
{
    "body": "This appears to work as intended, and passes doctests for me.\n\nIn examining the coverage of these files, the additions are well documented and tested, but the remaining coverage of some of them are quite low.  I will file some tickets about that once I check that they don't already exist.\n\nI am giving this a positive review but it wouldn't hurt if someone who uses this code looked at it - I have not used sage_input before.  I don't think that's a reason not to put it in a release candidate though.",
    "created_at": "2009-02-14T17:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5272#issuecomment-40394",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This appears to work as intended, and passes doctests for me.

In examining the coverage of these files, the additions are well documented and tested, but the remaining coverage of some of them are quite low.  I will file some tickets about that once I check that they don't already exist.

I am giving this a positive review but it wouldn't hurt if someone who uses this code looked at it - I have not used sage_input before.  I don't think that's a reason not to put it in a release candidate though.



---

archive/issue_comments_040395.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T07:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5272#issuecomment-40395",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_events_012248.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-15T07:56:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5272",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5272#event-12248"
}
```



---

archive/issue_comments_040396.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-15T07:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5272#issuecomment-40396",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
