# Issue 3735: Interact - header Javascript code executes on update

archive/issues_003735.json:
```json
{
    "body": "Assignee: boothby\n\nHere is an illustration (requires #3636):\n\n\n```\n@interact\ndef _(t=text_control(\"n = <span id='n'>0</span>\\\n        <script>n=parseInt($('#n').text()); $('#n').text(1+n);</script>\"),\n    l=[\"Increment\"]\n): pass\n```\n\n\nPressing \"Increment\" increments n, which implies that the line of Javascript code *in the header* is executed. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3735\n\n",
    "created_at": "2008-07-28T18:53:48Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "Interact - header Javascript code executes on update",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3735",
    "user": "https://github.com/itolkov"
}
```
Assignee: boothby

Here is an illustration (requires #3636):


```
@interact
def _(t=text_control("n = <span id='n'>0</span>\
        <script>n=parseInt($('#n').text()); $('#n').text(1+n);</script>"),
    l=["Increment"]
): pass
```


Pressing "Increment" increments n, which implies that the line of Javascript code *in the header* is executed. 

Issue created by migration from https://trac.sagemath.org/ticket/3735





---

archive/issue_comments_026457.json:
```json
{
    "body": "Attachment [sage-3735.patch](tarball://root/attachments/some-uuid/ticket3735/sage-3735.patch) by @williamstein created at 2008-08-05 21:31:37",
    "created_at": "2008-08-05T21:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3735#issuecomment-26457",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3735.patch](tarball://root/attachments/some-uuid/ticket3735/sage-3735.patch) by @williamstein created at 2008-08-05 21:31:37



---

archive/issue_comments_026458.json:
```json
{
    "body": "And, as an added bonus we also fix another bug!  Namely, if you put e.g., \n\n\n```\nhtml(\"alert('hi')\")\n```\n\n\nin a cell and hit shift-enter, then hi pops up in an alert ONCE, but if you\nthen refresh the page, \"hi\" pops up in an alert twice.   Now it only happens once\nin both cases.\n\nCode written by William Stein and Igor Tolkov",
    "created_at": "2008-08-05T21:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3735#issuecomment-26458",
    "user": "https://github.com/williamstein"
}
```

And, as an added bonus we also fix another bug!  Namely, if you put e.g., 


```
html("alert('hi')")
```


in a cell and hit shift-enter, then hi pops up in an alert ONCE, but if you
then refresh the page, "hi" pops up in an alert twice.   Now it only happens once
in both cases.

Code written by William Stein and Igor Tolkov



---

archive/issue_comments_026459.json:
```json
{
    "body": "Positive review.\n\nThere is still a bug, namely, if one tries\n\n```\nhtml(\"<script>alert('</script>');</script>\")\n```\n\nand the same for html tags. However, this defect existed before.",
    "created_at": "2008-08-07T05:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3735#issuecomment-26459",
    "user": "https://github.com/itolkov"
}
```

Positive review.

There is still a bug, namely, if one tries

```
html("<script>alert('</script>');</script>")
```

and the same for html tags. However, this defect existed before.



---

archive/issue_comments_026460.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-09T23:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3735#issuecomment-26460",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_026461.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-09T23:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3735#issuecomment-26461",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003958.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-09T23:23:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3735",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3735#event-3958"
}
```
