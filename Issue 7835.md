# Issue 7835: Preparsing on server does not account for unicode text

archive/issues_007835.json:
```json
{
    "body": "Assignee: was\n\nCC:  was mpatel ddrake\n\n#7483 moves preparsing to the server but does not account for unicode text, i.e., does not have a `# -*- coding: utf-8 -*-` header.\n\nThis patch depends on #7514 and everything it depends on.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7835\n\n",
    "created_at": "2010-01-03T19:15:54Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Preparsing on server does not account for unicode text",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7835",
    "user": "timdumol"
}
```
Assignee: was

CC:  was mpatel ddrake

#7483 moves preparsing to the server but does not account for unicode text, i.e., does not have a `# -*- coding: utf-8 -*-` header.

This patch depends on #7514 and everything it depends on.

Issue created by migration from https://trac.sagemath.org/ticket/7835





---

archive/issue_comments_067871.json:
```json
{
    "body": "This should do the trick.",
    "created_at": "2010-01-03T19:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67871",
    "user": "timdumol"
}
```

This should do the trick.



---

archive/issue_comments_067872.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T19:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67872",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067873.json:
```json
{
    "body": "Adds '# -*- coding: utf-8 -*-' to the preparsing code.",
    "created_at": "2010-01-03T19:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67873",
    "user": "timdumol"
}
```

Adds '# -*- coding: utf-8 -*-' to the preparsing code.



---

archive/issue_comments_067874.json:
```json
{
    "body": "Attachment [trac_7835-preparsing-unicode.patch](tarball://root/attachments/some-uuid/ticket7835/trac_7835-preparsing-unicode.patch) by mpatel created at 2010-01-06 20:26:42\n\nThis looks good to me.  Is there a simple example that breaks the existing code?",
    "created_at": "2010-01-06T20:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67874",
    "user": "mpatel"
}
```

Attachment [trac_7835-preparsing-unicode.patch](tarball://root/attachments/some-uuid/ticket7835/trac_7835-preparsing-unicode.patch) by mpatel created at 2010-01-06 20:26:42

This looks good to me.  Is there a simple example that breaks the existing code?



---

archive/issue_comments_067875.json:
```json
{
    "body": "You mean without this patch? Just use any non-ASCII character and attempt to evalaute it.\n\n\n```\nprint '\u00e9'\n```\n",
    "created_at": "2010-01-06T20:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67875",
    "user": "timdumol"
}
```

You mean without this patch? Just use any non-ASCII character and attempt to evalaute it.


```
print 'é'
```




---

archive/issue_comments_067876.json:
```json
{
    "body": "Just to check: I should apply #7249, too.  Otherwise, even with this patch, `print '\u00e9'` raises\n\n```python\n          File \"/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py\", line 1205, in render\n            max_out=HISTORY_MAX_OUTPUT)\n        exceptions.UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 17: ordinal not in range(128)\n```\n\nat least for me.",
    "created_at": "2010-01-06T20:45:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67876",
    "user": "mpatel"
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

archive/issue_comments_067877.json:
```json
{
    "body": "Now reviewing #7249...",
    "created_at": "2010-01-06T20:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67877",
    "user": "mpatel"
}
```

Now reviewing #7249...



---

archive/issue_comments_067878.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-06T23:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67878",
    "user": "mpatel"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067879.json:
```json
{
    "body": "Add short-term workaround for History/Log.  Replaces previous.",
    "created_at": "2010-01-07T01:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67879",
    "user": "mpatel"
}
```

Add short-term workaround for History/Log.  Replaces previous.



---

archive/issue_comments_067880.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-07T01:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67880",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067881.json:
```json
{
    "body": "Attachment [trac_7835-preparsing-unicode_v2.patch](tarball://root/attachments/some-uuid/ticket7835/trac_7835-preparsing-unicode_v2.patch) by mpatel created at 2010-01-07 01:31:28\n\nV2 wraps the [comment:4 problem above] in a `try-except` block, for now, i.e., until #7249 takes hold.  My review is positive, but someone should review my change.",
    "created_at": "2010-01-07T01:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67881",
    "user": "mpatel"
}
```

Attachment [trac_7835-preparsing-unicode_v2.patch](tarball://root/attachments/some-uuid/ticket7835/trac_7835-preparsing-unicode_v2.patch) by mpatel created at 2010-01-07 01:31:28

V2 wraps the [comment:4 problem above] in a `try-except` block, for now, i.e., until #7249 takes hold.  My review is positive, but someone should review my change.



---

archive/issue_comments_067882.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T06:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67882",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067883.json:
```json
{
    "body": "I'm assuming my change is OK, given its [comment:9:ticket:7908 position], but feel free to revert the status.",
    "created_at": "2010-01-18T06:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67883",
    "user": "mpatel"
}
```

I'm assuming my change is OK, given its [comment:9:ticket:7908 position], but feel free to revert the status.



---

archive/issue_comments_067884.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7835#issuecomment-67884",
    "user": "timdumol"
}
```

Resolution: fixed
