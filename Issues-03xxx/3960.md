# Issue 3960: [with patch, positive review] "edit this" on published worksheets doesn't work anymore in 3.1.1

archive/issues_003960.json:
```json
{
    "body": "Assignee: @mwhansen\n\nWay to reproduce:\n\n- start notebook\n- create worksheet\n- publish worksheet\n- go to \"published worksheets\"\n- click published worksheet\n\nresult:\n\n\"edit this\" or \"edit a copy\" link lead to another \"published\" version, not a normal worksheet\n\nexpected result:\n\nan editable worksheet\n\nNOTE: This worked properly in 3.0.6\n\nIssue created by migration from https://trac.sagemath.org/ticket/3960\n\n",
    "closed_at": "2008-09-04T02:02:46Z",
    "created_at": "2008-08-26T18:27:26Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, positive review] \"edit this\" on published worksheets doesn't work anymore in 3.1.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3960",
    "user": "https://github.com/nbruin"
}
```
Assignee: @mwhansen

Way to reproduce:

- start notebook
- create worksheet
- publish worksheet
- go to "published worksheets"
- click published worksheet

result:

"edit this" or "edit a copy" link lead to another "published" version, not a normal worksheet

expected result:

an editable worksheet

NOTE: This worked properly in 3.0.6

Issue created by migration from https://trac.sagemath.org/ticket/3960





---

archive/issue_comments_028384.json:
```json
{
    "body": "This is definitely a blocker for 3.1.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T07:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28384",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is definitely a blocker for 3.1.2.

Cheers,

Michael



---

archive/issue_comments_028385.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2008-08-27T07:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28385",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_028386.json:
```json
{
    "body": "I believe that this is because somewhere the wrong username is taken into account. Here is an example: publish a worksheet, and navigate to it. The link should say \"edit this\", not \"edit a copy\".\n\nAlternatively, I found that the username passed to worksheet_html() in notebook.py is \"pub\", but was unable to find the source of the problem.",
    "created_at": "2008-08-27T16:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28386",
    "user": "https://github.com/itolkov"
}
```

I believe that this is because somewhere the wrong username is taken into account. Here is an example: publish a worksheet, and navigate to it. The link should say "edit this", not "edit a copy".

Alternatively, I found that the username passed to worksheet_html() in notebook.py is "pub", but was unable to find the source of the problem.



---

archive/issue_comments_028387.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-03T00:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28387",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028388.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2008-09-03T00:53:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28388",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_028389.json:
```json
{
    "body": "Attachment [trac_3960.patch](tarball://root/attachments/some-uuid/ticket3960/trac_3960.patch) by @mwhansen created at 2008-09-04 01:35:54",
    "created_at": "2008-09-04T01:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28389",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3960.patch](tarball://root/attachments/some-uuid/ticket3960/trac_3960.patch) by @mwhansen created at 2008-09-04 01:35:54



---

archive/issue_comments_028390.json:
```json
{
    "body": "This patch fixes the issue and Mike walked through the code with me. Positive review. Mike is also writing a Selenium doctest for this bug, so we will catch it in the future.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T01:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28390",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch fixes the issue and Mike walked through the code with me. Positive review. Mike is also writing a Selenium doctest for this bug, so we will catch it in the future.

Cheers,

Michael



---

archive/issue_events_009089.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-04T02:02:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3960#event-9089"
}
```



---

archive/issue_comments_028391.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T02:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28391",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028392.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-04T02:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3960#issuecomment-28392",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0
