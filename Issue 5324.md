# Issue 5324: notebook -- %time block bug

archive/issues_005324.json:
```json
{
    "body": "Assignee: boothby\n\nIf you create a block like this:\n\n```\n%time \n2+2\n```\n\nin the notebook, then you get the following output:\n\n```\nTraceback (click to the left for traceback)\n...\nNameError: name 'time' is not defined\n```\n\n\nIMPORTANT: There is a single space right immediately after %time in the input!  Without the space things are fine. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5324\n\n",
    "created_at": "2009-02-20T20:00:08Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "notebook -- %time block bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5324",
    "user": "was"
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

archive/issue_comments_040984.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-20T21:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40984",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040985.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2009-02-20T21:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40985",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_040986.json:
```json
{
    "body": "mhansen says this is fixed at #5564.",
    "created_at": "2009-05-30T07:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40986",
    "user": "jason"
}
```

mhansen says this is fixed at #5564.



---

archive/issue_comments_040987.json:
```json
{
    "body": "Ticket #5564 has been closed because it addresses many issues. The issues it addresses are also considered by other tickets. If anyone is working on this ticket, please refer to #5564 for code and inspiration.",
    "created_at": "2009-08-26T19:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40987",
    "user": "mvngu"
}
```

Ticket #5564 has been closed because it addresses many issues. The issues it addresses are also considered by other tickets. If anyone is working on this ticket, please refer to #5564 for code and inspiration.



---

archive/issue_comments_040988.json:
```json
{
    "body": "Note that the problem isn't just with %time, but with any % modes.",
    "created_at": "2009-11-09T02:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40988",
    "user": "was"
}
```

Note that the problem isn't just with %time, but with any % modes.



---

archive/issue_comments_040989.json:
```json
{
    "body": "Attachment [sagenb_5324.patch](tarball://root/attachments/some-uuid/ticket5324/sagenb_5324.patch) by was created at 2009-11-09 02:13:16",
    "created_at": "2009-11-09T02:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40989",
    "user": "was"
}
```

Attachment [sagenb_5324.patch](tarball://root/attachments/some-uuid/ticket5324/sagenb_5324.patch) by was created at 2009-11-09 02:13:16



---

archive/issue_comments_040990.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-09T02:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40990",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_040991.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-09T03:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40991",
    "user": "mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040992.json:
```json
{
    "body": "Looks good and seems to fix the problem.  What's the point of setting i=-1 in the patch?  Is that just so i is defined as an integer if text has no elements when reaching the line: return \"\\n\".join(text[i:]).strip()?  Setting i = 0 would seem to make slightly more sense, if so.  I'm just curious, that doesn't seem like enough of an issue to block a positive review.",
    "created_at": "2009-11-09T03:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40992",
    "user": "mhampton"
}
```

Looks good and seems to fix the problem.  What's the point of setting i=-1 in the patch?  Is that just so i is defined as an integer if text has no elements when reaching the line: return "\n".join(text[i:]).strip()?  Setting i = 0 would seem to make slightly more sense, if so.  I'm just curious, that doesn't seem like enough of an issue to block a positive review.



---

archive/issue_comments_040993.json:
```json
{
    "body": "> Is that just so i is defined as an integer if text has no elements when \n> reaching the line: return\n\nYes.    splitlines and split('\\n') have different semantics.  I changed to splitlines in anticipation of windows. \n\nYou're right, using i=0 makes more sense, though of course won't make any difference since in this special case the list we're slicing is empty.",
    "created_at": "2009-11-09T17:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40993",
    "user": "was"
}
```

> Is that just so i is defined as an integer if text has no elements when 
> reaching the line: return

Yes.    splitlines and split('\n') have different semantics.  I changed to splitlines in anticipation of windows. 

You're right, using i=0 makes more sense, though of course won't make any difference since in this special case the list we're slicing is empty.



---

archive/issue_comments_040994.json:
```json
{
    "body": "Attachment [sagenb_5324-part2.patch](tarball://root/attachments/some-uuid/ticket5324/sagenb_5324-part2.patch) by was created at 2009-11-09 17:12:17",
    "created_at": "2009-11-09T17:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40994",
    "user": "was"
}
```

Attachment [sagenb_5324-part2.patch](tarball://root/attachments/some-uuid/ticket5324/sagenb_5324-part2.patch) by was created at 2009-11-09 17:12:17



---

archive/issue_comments_040995.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-09T17:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5324",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5324#issuecomment-40995",
    "user": "was"
}
```

Resolution: fixed
