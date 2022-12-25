# Issue 2798: [with patch, positive review] probably easy-to-fix ptest issue

archive/issues_002798.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n```\n09:56 < wstein> I just got this from ptest:\n09:56 -!- Irssi: Pasting 5 lines to #sage-devel. Press Ctrl-K if you wish to do this or Ctrl-C to cancel.\n09:56 < wstein>   File \"/Users/was/build/sage-2.10.4/local/bin/sage-ptest\", line 74, in run\n09:56 < wstein>     if e==-2:\n09:56 < wstein> UnboundLocalError: local variable 'e' referenced before assignment\n09:56 < wstein>  \n09:56 < wstein> but then it worked...\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2798\n\n",
    "closed_at": "2008-04-04T19:54:59Z",
    "created_at": "2008-04-04T16:57:05Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, positive review] probably easy-to-fix ptest issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2798",
    "user": "https://github.com/williamstein"
}
```
Assignee: @garyfurnish

```
09:56 < wstein> I just got this from ptest:
09:56 -!- Irssi: Pasting 5 lines to #sage-devel. Press Ctrl-K if you wish to do this or Ctrl-C to cancel.
09:56 < wstein>   File "/Users/was/build/sage-2.10.4/local/bin/sage-ptest", line 74, in run
09:56 < wstein>     if e==-2:
09:56 < wstein> UnboundLocalError: local variable 'e' referenced before assignment
09:56 < wstein>  
09:56 < wstein> but then it worked...
```

Issue created by migration from https://trac.sagemath.org/ticket/2798





---

archive/issue_comments_019172.json:
```json
{
    "body": "Attachment [trac_2798.patch](tarball://root/attachments/some-uuid/ticket2798/trac_2798.patch) by @garyfurnish created at 2008-04-04 18:47:09",
    "created_at": "2008-04-04T18:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2798#issuecomment-19172",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_2798.patch](tarball://root/attachments/some-uuid/ticket2798/trac_2798.patch) by @garyfurnish created at 2008-04-04 18:47:09



---

archive/issue_comments_019173.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-04T18:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2798#issuecomment-19173",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019174.json:
```json
{
    "body": "Patch looks good to me. It doesn't really address the issue wstein encountered, but it will print a proper error message the next time somebody hits the bug that caused the problem in the first place. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-04T19:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2798#issuecomment-19174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. It doesn't really address the issue wstein encountered, but it will print a proper error message the next time somebody hits the bug that caused the problem in the first place. Positive review.

Cheers,

Michael



---

archive/issue_events_006454.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-04T19:54:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2798#event-6454"
}
```



---

archive/issue_comments_019175.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T19:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2798#issuecomment-19175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019176.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T19:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2798",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2798#issuecomment-19176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha1
