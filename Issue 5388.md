# Issue 5388: Remove hg_doc* in Sage 3.4 since it no longer works once the doc repo is gone

archive/issues_005388.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @mwhansen @jhpalmieri\n\nThis come up via other tickets. Removing the functionality completely might be not the best solution, but having it print a warning and apply the patch to devel might be an alternative. Just printing the warning might be more prudent since any patch against the doc repo will likely be broken anyway.\n\nI am sure the manual needs to be updated about hg_doc.* going away, but that can be another ticket in case it isn't implemented yet.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5388\n\n",
    "created_at": "2009-02-26T22:53:03Z",
    "labels": [
        "component: documentation",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Remove hg_doc* in Sage 3.4 since it no longer works once the doc repo is gone",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: tba

CC:  @mwhansen @jhpalmieri

This come up via other tickets. Removing the functionality completely might be not the best solution, but having it print a warning and apply the patch to devel might be an alternative. Just printing the warning might be more prudent since any patch against the doc repo will likely be broken anyway.

I am sure the manual needs to be updated about hg_doc.* going away, but that can be another ticket in case it isn't implemented yet.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5388





---

archive/issue_comments_041423.json:
```json
{
    "body": "I'm pretty sure I already removed this in the patches in alpha0.",
    "created_at": "2009-02-26T22:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5388#issuecomment-41423",
    "user": "https://github.com/mwhansen"
}
```

I'm pretty sure I already removed this in the patches in alpha0.



---

archive/issue_comments_041424.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-02-26T23:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5388#issuecomment-41424",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_041425.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> I'm pretty sure I already removed this in the patches in alpha0.\n\nYes, I should have checked first that it is gone instead of opening a ticket :(\n\n```\nsage: hg_ [TAB]\nhg_extcode  hg_sage     hg_scripts  \nsage:\n```\n\n\nI just someone (I believe it was John) mention an issue with hg_doc not working, but that might have been for a pre-3.4 sage build or one that did not have all patches applied. \n\nSo: invalid.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-26T23:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5388#issuecomment-41425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:1 mhansen]:
> I'm pretty sure I already removed this in the patches in alpha0.

Yes, I should have checked first that it is gone instead of opening a ticket :(

```
sage: hg_ [TAB]
hg_extcode  hg_sage     hg_scripts  
sage:
```


I just someone (I believe it was John) mention an issue with hg_doc not working, but that might have been for a pre-3.4 sage build or one that did not have all patches applied. 

So: invalid.

Cheers,

Michael



---

archive/issue_events_005645.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-26T23:26:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5388",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5388#event-5645"
}
```
