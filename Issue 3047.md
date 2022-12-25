# Issue 3047: version option returning clone branch name

archive/issues_003047.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe attached patch adds to version an option which returns the version and the branch clone name.\nNew behavior:\nsage: version()\nreturns exactly the same thing it did before no change.\nsage: version(True) # or replace \"True\" by anything except \"0\" or \"False\"\nreturns \n(Version, Branch name)\nFor example,\n\n```\nsage: version(1)\n\n('SAGE Version 3.0, Release Date: 2008-04-22',\n 'Mercurial clone branch: version')\n```\n\nin a Mercurial clone branch created using \"sage -clone version\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/3047\n\n",
    "created_at": "2008-04-27T20:20:33Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "version option returning clone branch name",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3047",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @williamstein

The attached patch adds to version an option which returns the version and the branch clone name.
New behavior:
sage: version()
returns exactly the same thing it did before no change.
sage: version(True) # or replace "True" by anything except "0" or "False"
returns 
(Version, Branch name)
For example,

```
sage: version(1)

('SAGE Version 3.0, Release Date: 2008-04-22',
 'Mercurial clone branch: version')
```

in a Mercurial clone branch created using "sage -clone version".

Issue created by migration from https://trac.sagemath.org/ticket/3047





---

archive/issue_comments_020940.json:
```json
{
    "body": "This ticket should be deleted. I meant only to create trac 3046.",
    "created_at": "2008-04-27T20:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3047#issuecomment-20940",
    "user": "https://github.com/wdjoyner"
}
```

This ticket should be deleted. I meant only to create trac 3046.



---

archive/issue_events_003256.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-04-27T21:52:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3047",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3047#event-3256"
}
```



---

archive/issue_comments_020941.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-04-27T21:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3047#issuecomment-20941",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate
