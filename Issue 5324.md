# Issue 5324: notebook -- %time block bug

archive/issues_005324.json:
```json
{
    "body": "Assignee: boothby\n\nIf you create a block like this:\n\n```\n%time \n2+2\n```\n\nin the notebook, then you get the following output:\n\n```\nTraceback (click to the left for traceback)\n...\nNameError: name 'time' is not defined\n```\n\n\nIMPORTANT: There is a single space right immediately after %time in the input!  Without the space things are fine. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5324\n\n",
    "created_at": "2009-02-20T20:00:08Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "notebook -- %time block bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5324",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

If you create a block like this:

```
%time 
2+2
```

in the notebook, then you get the following output:

```
Traceback (click to the left for traceback)
...
NameError: name 'time' is not defined
```


IMPORTANT: There is a single space right immediately after %time in the input!  Without the space things are fine. 

Issue created by migration from https://trac.sagemath.org/ticket/5324





---

archive/issue_comments_040904.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-20T21:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40904",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040905.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-02-20T21:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40905",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_040906.json:
```json
{
    "body": "mhansen says this is fixed at #5564.",
    "created_at": "2009-05-30T07:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40906",
    "user": "https://github.com/jasongrout"
}
```

mhansen says this is fixed at #5564.



---

archive/issue_comments_040907.json:
```json
{
    "body": "Ticket #5564 has been closed because it addresses many issues. The issues it addresses are also considered by other tickets. If anyone is working on this ticket, please refer to #5564 for code and inspiration.",
    "created_at": "2009-08-26T19:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40907",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #5564 has been closed because it addresses many issues. The issues it addresses are also considered by other tickets. If anyone is working on this ticket, please refer to #5564 for code and inspiration.



---

archive/issue_comments_040908.json:
```json
{
    "body": "Note that the problem isn't just with %time, but with any % modes.",
    "created_at": "2009-11-09T02:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40908",
    "user": "https://github.com/williamstein"
}
```

Note that the problem isn't just with %time, but with any % modes.



---

archive/issue_comments_040909.json:
```json
{
    "body": "Attachment [sagenb_5324.patch](tarball://root/attachments/some-uuid/ticket5324/sagenb_5324.patch) by @williamstein created at 2009-11-09 02:13:16",
    "created_at": "2009-11-09T02:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40909",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagenb_5324.patch](tarball://root/attachments/some-uuid/ticket5324/sagenb_5324.patch) by @williamstein created at 2009-11-09 02:13:16



---

archive/issue_comments_040910.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-09T02:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40910",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_040911.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-09T03:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40911",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040912.json:
```json
{
    "body": "Looks good and seems to fix the problem.  What's the point of setting i=-1 in the patch?  Is that just so i is defined as an integer if text has no elements when reaching the line: return \"\\n\".join(text[i:]).strip()?  Setting i = 0 would seem to make slightly more sense, if so.  I'm just curious, that doesn't seem like enough of an issue to block a positive review.",
    "created_at": "2009-11-09T03:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40912",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Looks good and seems to fix the problem.  What's the point of setting i=-1 in the patch?  Is that just so i is defined as an integer if text has no elements when reaching the line: return "\n".join(text[i:]).strip()?  Setting i = 0 would seem to make slightly more sense, if so.  I'm just curious, that doesn't seem like enough of an issue to block a positive review.



---

archive/issue_comments_040913.json:
```json
{
    "body": "> Is that just so i is defined as an integer if text has no elements when \n> reaching the line: return\n\nYes.    splitlines and split('\\n') have different semantics.  I changed to splitlines in anticipation of windows. \n\nYou're right, using i=0 makes more sense, though of course won't make any difference since in this special case the list we're slicing is empty.",
    "created_at": "2009-11-09T17:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40913",
    "user": "https://github.com/williamstein"
}
```

> Is that just so i is defined as an integer if text has no elements when 
> reaching the line: return

Yes.    splitlines and split('\n') have different semantics.  I changed to splitlines in anticipation of windows. 

You're right, using i=0 makes more sense, though of course won't make any difference since in this special case the list we're slicing is empty.



---

archive/issue_comments_040914.json:
```json
{
    "body": "Attachment [sagenb_5324-part2.patch](tarball://root/attachments/some-uuid/ticket5324/sagenb_5324-part2.patch) by @williamstein created at 2009-11-09 17:12:17",
    "created_at": "2009-11-09T17:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40914",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagenb_5324-part2.patch](tarball://root/attachments/some-uuid/ticket5324/sagenb_5324-part2.patch) by @williamstein created at 2009-11-09 17:12:17



---

archive/issue_events_012404.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-11-09T17:19:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5324#event-12404"
}
```



---

archive/issue_comments_040915.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-09T17:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40915",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
