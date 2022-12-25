# Issue 2892: notebook -- traceback shrinking/expanding in the notebook is broken in an obscure case

archive/issues_002892.json:
```json
{
    "body": "Assignee: boothby\n\nI discovered this but when teaching my class.  It's best explained\nwith a screen shot. \n\nhttp://sage.math.washington.edu/home/was/patches/traceback_shrinking.png\n\nIssue created by migration from https://trac.sagemath.org/ticket/2892\n\n",
    "created_at": "2008-04-12T03:17:30Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "notebook -- traceback shrinking/expanding in the notebook is broken in an obscure case",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2892",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

I discovered this but when teaching my class.  It's best explained
with a screen shot. 

http://sage.math.washington.edu/home/was/patches/traceback_shrinking.png

Issue created by migration from https://trac.sagemath.org/ticket/2892





---

archive/issue_comments_019854.json:
```json
{
    "body": "This patch:\n* fixes the stated bug.  To observe this try this input: \n\n```\ntry:\n    1/0\nfinally:\n    print \"<html><b>hello</b></html>\"\n```\n\nNote that the output has html properly formated at the top, etc.\n\n* also fixes a bug when the traceback output is too long.  To \nverify this, try this input and wait a few seconds.  NOte that a link\nappears as it should:\n\n```\ndef f(n):\n    f(n)\n\nf(5)\n```\n\n\n* I'm sorry but providing doctests for this is just too hard at present, given that we don't have a good notebook testing framework just yet.  These bugs are pretty high priority imho.",
    "created_at": "2008-04-12T03:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2892#issuecomment-19854",
    "user": "https://github.com/williamstein"
}
```

This patch:
* fixes the stated bug.  To observe this try this input: 

```
try:
    1/0
finally:
    print "<html><b>hello</b></html>"
```

Note that the output has html properly formated at the top, etc.

* also fixes a bug when the traceback output is too long.  To 
verify this, try this input and wait a few seconds.  NOte that a link
appears as it should:

```
def f(n):
    f(n)

f(5)
```


* I'm sorry but providing doctests for this is just too hard at present, given that we don't have a good notebook testing framework just yet.  These bugs are pretty high priority imho.



---

archive/issue_comments_019855.json:
```json
{
    "body": "Attachment [sage-2892.patch](tarball://root/attachments/some-uuid/ticket2892/sage-2892.patch) by @williamstein created at 2008-04-12 03:56:25",
    "created_at": "2008-04-12T03:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2892#issuecomment-19855",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2892.patch](tarball://root/attachments/some-uuid/ticket2892/sage-2892.patch) by @williamstein created at 2008-04-12 03:56:25



---

archive/issue_comments_019856.json:
```json
{
    "body": "works for me",
    "created_at": "2008-04-12T07:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2892#issuecomment-19856",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

works for me



---

archive/issue_comments_019857.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-12T11:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2892#issuecomment-19857",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_comments_019858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T11:27:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2892",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2892#issuecomment-19858",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003090.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-12T11:27:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2892",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2892#event-3090"
}
```
