# Issue 4430: optimize new worksheet startup

archive/issues_004430.json:
```json
{
    "body": "Assignee: tbd\n\nWhen one creates a new worksheet, it would be nice if the sage process started up in the background right then, rather than wait till one types the first command. Currently there is an annoying lag...\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4430\n\n",
    "created_at": "2008-11-03T17:53:13Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optimize new worksheet startup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4430",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd

When one creates a new worksheet, it would be nice if the sage process started up in the background right then, rather than wait till one types the first command. Currently there is an annoying lag...


Issue created by migration from https://trac.sagemath.org/ticket/4430





---

archive/issue_comments_032489.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2008-11-03T20:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4430#issuecomment-32489",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing component from algebra to notebook.



---

archive/issue_comments_032490.json:
```json
{
    "body": "Changing assignee from tbd to boothby.",
    "created_at": "2008-11-03T20:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4430#issuecomment-32490",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing assignee from tbd to boothby.



---

archive/issue_comments_032491.json:
```json
{
    "body": "Attachment [trac_4330.patch](tarball://root/attachments/some-uuid/ticket4430/trac_4330.patch) by @mwhansen created at 2008-11-21 21:39:20",
    "created_at": "2008-11-21T21:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4430#issuecomment-32491",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4330.patch](tarball://root/attachments/some-uuid/ticket4430/trac_4330.patch) by @mwhansen created at 2008-11-21 21:39:20



---

archive/issue_comments_032492.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-25T16:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4430#issuecomment-32492",
    "user": "https://github.com/qed777"
}
```

Resolution: invalid



---

archive/issue_comments_032493.json:
```json
{
    "body": "I'm closing this, since we now start a worksheet when it's first served.  From `twist.py`, around line #1514:\n\n```python\nclass Worksheet(WorksheetResource, resource.Resource):\n    addSlash = True\n\n    def render(self, ctx):\n        self.worksheet.sage()\n        s = notebook.html(worksheet_filename = self.name,  username=self.username)\n        return HTMLResponse(stream=s)\n```\n\nI've also confirmed this with a print statement in `Worksheet.sage`.\n\nBy the way, the patch here appears to be for a different ticket.",
    "created_at": "2010-01-25T16:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4430#issuecomment-32493",
    "user": "https://github.com/qed777"
}
```

I'm closing this, since we now start a worksheet when it's first served.  From `twist.py`, around line #1514:

```python
class Worksheet(WorksheetResource, resource.Resource):
    addSlash = True

    def render(self, ctx):
        self.worksheet.sage()
        s = notebook.html(worksheet_filename = self.name,  username=self.username)
        return HTMLResponse(stream=s)
```

I've also confirmed this with a print statement in `Worksheet.sage`.

By the way, the patch here appears to be for a different ticket.



---

archive/issue_events_004674.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-25T16:05:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4430",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4430#event-4674"
}
```
