# Issue 7060: notebook -- templating patch introduces numerous bugs

archive/issues_007060.json:
```json
{
    "body": "Assignee: boothby\n\nI realized that sage-4.1.2.alpha4 contains Tim Dumol's notebook patch, and many patches on top of that... but in separating the notebook off we found that that patch contains many errors which causes at least 6 serious bugs.  \n\nOur options:\n\n* revert that patch and everything on top of it.\n\n* switch to the new separated notebook for sage-4.1.2.\n\nThis is unfortunate and is entirely my fault since I refereed this notebook templating code, and though I did try everything in the notebook, I clearly wasn't sufficiently careful.   Sorry people.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7060\n\n",
    "created_at": "2009-09-29T03:13:33Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "notebook -- templating patch introduces numerous bugs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7060",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

I realized that sage-4.1.2.alpha4 contains Tim Dumol's notebook patch, and many patches on top of that... but in separating the notebook off we found that that patch contains many errors which causes at least 6 serious bugs.  

Our options:

* revert that patch and everything on top of it.

* switch to the new separated notebook for sage-4.1.2.

This is unfortunate and is entirely my fault since I refereed this notebook templating code, and though I did try everything in the notebook, I clearly wasn't sufficiently careful.   Sorry people.

Issue created by migration from https://trac.sagemath.org/ticket/7060





---

archive/issue_comments_058306.json:
```json
{
    "body": "so what patch was this (i.e., ticket number)?",
    "created_at": "2009-09-29T07:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7060#issuecomment-58306",
    "user": "https://github.com/jasongrout"
}
```

so what patch was this (i.e., ticket number)?



---

archive/issue_comments_058307.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> so what patch was this (i.e., ticket number)?\n\n\n#6568. The template problems are being found, and hopefully we can backport the fixes to the old notebook, if we are not to switch to the new separated notebook.",
    "created_at": "2009-09-29T15:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7060#issuecomment-58307",
    "user": "https://github.com/TimDumol"
}
```

Replying to [comment:1 jason]:
> so what patch was this (i.e., ticket number)?


#6568. The template problems are being found, and hopefully we can backport the fixes to the old notebook, if we are not to switch to the new separated notebook.



---

archive/issue_events_016656.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-02T17:45:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7060#event-16656"
}
```



---

archive/issue_comments_058308.json:
```json
{
    "body": "This is fixed by switching to the new notebook.",
    "created_at": "2009-10-14T16:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7060#issuecomment-58308",
    "user": "https://github.com/williamstein"
}
```

This is fixed by switching to the new notebook.



---

archive/issue_events_016657.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-14T16:08:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7060#event-16657"
}
```



---

archive/issue_comments_058309.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-14T16:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7060#issuecomment-58309",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_016658.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-14T16:12:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7060#event-16658"
}
```



---

archive/issue_events_016659.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-14T16:12:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7060#event-16659"
}
```
