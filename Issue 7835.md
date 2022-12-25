# Issue 7835: Preparsing on server does not account for unicode text

archive/issues_007835.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein @qed777 @dandrake\n\n#7483 moves preparsing to the server but does not account for unicode text, i.e., does not have a `# -*- coding: utf-8 -*-` header.\n\nThis patch depends on #7514 and everything it depends on.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7835\n\n",
    "created_at": "2010-01-03T19:15:54Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Preparsing on server does not account for unicode text",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7835",
    "user": "https://github.com/TimDumol"
}
```
Assignee: @williamstein

CC:  @williamstein @qed777 @dandrake

#7483 moves preparsing to the server but does not account for unicode text, i.e., does not have a `# -*- coding: utf-8 -*-` header.

This patch depends on #7514 and everything it depends on.

Issue created by migration from https://trac.sagemath.org/ticket/7835





---

archive/issue_comments_067754.json:
```json
{
    "body": "This should do the trick.",
    "created_at": "2010-01-03T19:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67754",
    "user": "https://github.com/TimDumol"
}
```

This should do the trick.



---

archive/issue_comments_067755.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T19:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67755",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067756.json:
```json
{
    "body": "Adds '# -*- coding: utf-8 -*-' to the preparsing code.",
    "created_at": "2010-01-03T19:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67756",
    "user": "https://github.com/TimDumol"
}
```

Adds '# -*- coding: utf-8 -*-' to the preparsing code.



---

archive/issue_comments_067757.json:
```json
{
    "body": "Attachment [trac_7835-preparsing-unicode.patch](tarball://root/attachments/some-uuid/ticket7835/trac_7835-preparsing-unicode.patch) by @qed777 created at 2010-01-06 20:26:42\n\nThis looks good to me.  Is there a simple example that breaks the existing code?",
    "created_at": "2010-01-06T20:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67757",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7835-preparsing-unicode.patch](tarball://root/attachments/some-uuid/ticket7835/trac_7835-preparsing-unicode.patch) by @qed777 created at 2010-01-06 20:26:42

This looks good to me.  Is there a simple example that breaks the existing code?



---

archive/issue_comments_067758.json:
```json
{
    "body": "You mean without this patch? Just use any non-ASCII character and attempt to evalaute it.\n\n```\nprint '\u00e9'\n```",
    "created_at": "2010-01-06T20:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67758",
    "user": "https://github.com/TimDumol"
}
```

You mean without this patch? Just use any non-ASCII character and attempt to evalaute it.

```
print 'é'
```



---

archive/issue_comments_067759.json:
```json
{
    "body": "Just to check: I should apply #7249, too.  Otherwise, even with this patch, `print '\u00e9'` raises\n\n```python\n          File \"/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py\", line 1205, in render\n            max_out=HISTORY_MAX_OUTPUT)\n        exceptions.UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 17: ordinal not in range(128)\n```\nat least for me.",
    "created_at": "2010-01-06T20:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67759",
    "user": "https://github.com/qed777"
}
```

Just to check: I should apply #7249, too.  Otherwise, even with this patch, `print 'é'` raises

```python
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py", line 1205, in render
            max_out=HISTORY_MAX_OUTPUT)
        exceptions.UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 17: ordinal not in range(128)
```
at least for me.



---

archive/issue_comments_067760.json:
```json
{
    "body": "Now reviewing #7249...",
    "created_at": "2010-01-06T20:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67760",
    "user": "https://github.com/qed777"
}
```

Now reviewing #7249...



---

archive/issue_comments_067761.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-06T23:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67761",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067762.json:
```json
{
    "body": "Add short-term workaround for History/Log.  Replaces previous.",
    "created_at": "2010-01-07T01:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67762",
    "user": "https://github.com/qed777"
}
```

Add short-term workaround for History/Log.  Replaces previous.



---

archive/issue_comments_067763.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-07T01:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67763",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067764.json:
```json
{
    "body": "Attachment [trac_7835-preparsing-unicode_v2.patch](tarball://root/attachments/some-uuid/ticket7835/trac_7835-preparsing-unicode_v2.patch) by @qed777 created at 2010-01-07 01:31:28\n\nV2 wraps the [comment:4 problem above] in a `try-except` block, for now, i.e., until #7249 takes hold.  My review is positive, but someone should review my change.",
    "created_at": "2010-01-07T01:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67764",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7835-preparsing-unicode_v2.patch](tarball://root/attachments/some-uuid/ticket7835/trac_7835-preparsing-unicode_v2.patch) by @qed777 created at 2010-01-07 01:31:28

V2 wraps the [comment:4 problem above] in a `try-except` block, for now, i.e., until #7249 takes hold.  My review is positive, but someone should review my change.



---

archive/issue_comments_067765.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T06:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67765",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067766.json:
```json
{
    "body": "I'm assuming my change is OK, given its [comment:9:ticket:7908 position], but feel free to revert the status.",
    "created_at": "2010-01-18T06:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67766",
    "user": "https://github.com/qed777"
}
```

I'm assuming my change is OK, given its [comment:9:ticket:7908 position], but feel free to revert the status.



---

archive/issue_comments_067767.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67767",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed



---

archive/issue_events_018736.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:31:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7835#event-18736"
}
```
