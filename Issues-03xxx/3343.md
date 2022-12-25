# Issue 3343: [with patch, with positive review] arguments, documentation to ln function

archive/issues_003343.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: ln, calculus\n\nFirst, ln should only take 1 argument.  As it is, it accepts more than one, and just ignores all of the extra ones:\n\n```\nsage: ln(6,2)\nlog(6)\nsage: ln(12,-2,0,0,3,4,5)\nlog(12)\n```\n\nSecond, the documentation for ln (hitting 'ln?') gives the documentation for the class Function_log, and hence includes things like this:\n\n```\nsage: log(1024, 2) # the following is ugly (for now)\nlog(1024)/log(2)\nsage: log(10, 4)\nlog(10)/log(4)\n```\n\nThe attached patch defines ln as a function accepting only one argument, and with its own documentation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3343\n\n",
    "closed_at": "2008-06-10T05:51:51Z",
    "created_at": "2008-05-31T21:46:29Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, with positive review] arguments, documentation to ln function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3343",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: somebody

Keywords: ln, calculus

First, ln should only take 1 argument.  As it is, it accepts more than one, and just ignores all of the extra ones:

```
sage: ln(6,2)
log(6)
sage: ln(12,-2,0,0,3,4,5)
log(12)
```

Second, the documentation for ln (hitting 'ln?') gives the documentation for the class Function_log, and hence includes things like this:

```
sage: log(1024, 2) # the following is ugly (for now)
log(1024)/log(2)
sage: log(10, 4)
log(10)/log(4)
```

The attached patch defines ln as a function accepting only one argument, and with its own documentation.


Issue created by migration from https://trac.sagemath.org/ticket/3343





---

archive/issue_comments_023172.json:
```json
{
    "body": "Attachment [3343.patch](tarball://root/attachments/some-uuid/ticket3343/3343.patch) by @jhpalmieri created at 2008-05-31 21:49:10",
    "created_at": "2008-05-31T21:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3343#issuecomment-23172",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [3343.patch](tarball://root/attachments/some-uuid/ticket3343/3343.patch) by @jhpalmieri created at 2008-05-31 21:49:10



---

archive/issue_comments_023173.json:
```json
{
    "body": "This is a good idea.",
    "created_at": "2008-06-10T05:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3343#issuecomment-23173",
    "user": "https://github.com/garyfurnish"
}
```

This is a good idea.



---

archive/issue_comments_023174.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-10T05:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3343#issuecomment-23174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023175.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha2",
    "created_at": "2008-06-10T05:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3343#issuecomment-23175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.alpha2



---

archive/issue_events_007490.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-10T05:51:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3343",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3343#event-7490"
}
```
