# Issue 7060: notebook -- templating patch introduces numerous bugs

archive/issues_007060.json:
```json
{
    "body": "Assignee: boothby\n\nI realized that sage-4.1.2.alpha4 contains Tim Dumol's notebook patch, and many patches on top of that... but in separating the notebook off we found that that patch contains many errors which causes at least 6 serious bugs.  \n\nOur options:\n\n* revert that patch and everything on top of it.\n\n* switch to the new separated notebook for sage-4.1.2.\n\nThis is unfortunate and is entirely my fault since I refereed this notebook templating code, and though I did try everything in the notebook, I clearly wasn't sufficiently careful.   Sorry people.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7060\n\n",
    "created_at": "2009-09-29T03:13:33Z",
    "labels": [
        "notebook",
        "blocker",
        "bug"
    ],
    "title": "notebook -- templating patch introduces numerous bugs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7060",
    "user": "was"
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

archive/issue_comments_058416.json:
```json
{
    "body": "so what patch was this (i.e., ticket number)?",
    "created_at": "2009-09-29T07:44:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7060#issuecomment-58416",
    "user": "jason"
}
```

so what patch was this (i.e., ticket number)?



---

archive/issue_comments_058417.json:
```json
{
    "body": "Replying to [comment:1 jason]:\n> so what patch was this (i.e., ticket number)?\n\n#6568. The template problems are being found, and hopefully we can backport the fixes to the old notebook, if we are not to switch to the new separated notebook.",
    "created_at": "2009-09-29T15:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7060#issuecomment-58417",
    "user": "timdumol"
}
```

Replying to [comment:1 jason]:
> so what patch was this (i.e., ticket number)?

#6568. The template problems are being found, and hopefully we can backport the fixes to the old notebook, if we are not to switch to the new separated notebook.



---

archive/issue_comments_058418.json:
```json
{
    "body": "This is fixed by switching to the new notebook.",
    "created_at": "2009-10-14T16:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7060#issuecomment-58418",
    "user": "was"
}
```

This is fixed by switching to the new notebook.



---

archive/issue_comments_058419.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-14T16:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7060#issuecomment-58419",
    "user": "was"
}
```

Resolution: fixed
