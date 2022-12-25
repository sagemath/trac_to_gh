# Issue 5293: [with patch; positive review] tab-completion menu creates two copies of the choice made

archive/issues_005293.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: tab completion\n\nIn sage-3.3.rc0 (presumable from some patch in an alpha release) tab-completion is somewhat broken in the notebook.  If you tab-complete and there is more than one possible completion, if you choose from the drop-down menu and press enter you get the entire command repeated, for example:\n\nQQ. [press tab, get menu, choose absolute_degree and press enter]\nQQ.absolute_degreeQQ.absolute_degree\n\nThis is currently effecting sagenb's rc0, and has been confirmed on several other installs.\n\nI am not sure where to begin to track this down, or what patch caused it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5293\n\n",
    "closed_at": "2009-02-20T07:24:02Z",
    "created_at": "2009-02-17T12:57:36Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch; positive review] tab-completion menu creates two copies of the choice made",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5293",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: boothby

Keywords: tab completion

In sage-3.3.rc0 (presumable from some patch in an alpha release) tab-completion is somewhat broken in the notebook.  If you tab-complete and there is more than one possible completion, if you choose from the drop-down menu and press enter you get the entire command repeated, for example:

QQ. [press tab, get menu, choose absolute_degree and press enter]
QQ.absolute_degreeQQ.absolute_degree

This is currently effecting sagenb's rc0, and has been confirmed on several other installs.

I am not sure where to begin to track this down, or what patch caused it.

Issue created by migration from https://trac.sagemath.org/ticket/5293





---

archive/issue_comments_040600.json:
```json
{
    "body": "Changing assignee from tbd to boothby.",
    "created_at": "2009-02-17T12:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40600",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from tbd to boothby.



---

archive/issue_comments_040601.json:
```json
{
    "body": "Changing keywords from \"\" to \"tab completion\".",
    "created_at": "2009-02-17T12:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40601",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing keywords from "" to "tab completion".



---

archive/issue_comments_040602.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2009-02-17T12:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40602",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing component from algebra to notebook.



---

archive/issue_events_012302.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-17T13:01:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5293#event-12302"
}
```



---

archive/issue_comments_040603.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-02-17T20:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40603",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing priority from major to critical.



---

archive/issue_comments_040604.json:
```json
{
    "body": "This seems to be caused by #4440. I am working on a patch now.",
    "created_at": "2009-02-17T22:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This seems to be caused by #4440. I am working on a patch now.



---

archive/issue_comments_040605.json:
```json
{
    "body": "I am just confirming that this is caused by #4440.  I found this with the (very cool) hg bisect command and then hand-tested before/after the patch was committed.",
    "created_at": "2009-02-17T23:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40605",
    "user": "https://github.com/jasongrout"
}
```

I am just confirming that this is caused by #4440.  I found this with the (very cool) hg bisect command and then hand-tested before/after the patch was committed.



---

archive/issue_comments_040606.json:
```json
{
    "body": "Fixed by reverting #4440 for now.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T23:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40606",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by reverting #4440 for now.

Cheers,

Michael



---

archive/issue_events_012303.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-17T23:08:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5293#event-12303"
}
```



---

archive/issue_comments_040607.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-17T23:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40607",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012304.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-17T23:08:28Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5293#event-12304"
}
```



---

archive/issue_events_012305.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-17T23:08:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5293#event-12305"
}
```



---

archive/issue_comments_040608.json:
```json
{
    "body": "Attachment [5293.patch](tarball://root/attachments/some-uuid/ticket5293/5293.patch) by boothby created at 2009-02-19 20:39:45",
    "created_at": "2009-02-19T20:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40608",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [5293.patch](tarball://root/attachments/some-uuid/ticket5293/5293.patch) by boothby created at 2009-02-19 20:39:45



---

archive/issue_comments_040609.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-02-19T20:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40609",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_040610.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-02-19T20:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40610",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from closed to reopened.



---

archive/issue_events_012306.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2009-02-19T20:39:45Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5293#event-12306"
}
```



---

archive/issue_comments_040611.json:
```json
{
    "body": "patch depends on #4440",
    "created_at": "2009-02-19T20:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40611",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

patch depends on #4440



---

archive/issue_comments_040612.json:
```json
{
    "body": "This appears to fix the side-effects from #4440.  Patch applies to rc0, which still had #4440 applied.",
    "created_at": "2009-02-19T21:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40612",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This appears to fix the side-effects from #4440.  Patch applies to rc0, which still had #4440 applied.



---

archive/issue_comments_040613.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T07:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40613",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_events_012307.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-20T07:24:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5293#event-12307"
}
```



---

archive/issue_comments_040614.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T07:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5293#issuecomment-40614",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
