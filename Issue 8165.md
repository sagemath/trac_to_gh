# Issue 8165: title cuts off on worksheet upload

archive/issues_008165.json:
```json
{
    "body": "Assignee: @williamstein\n\nI just tried uploading the following worksheet:\n\nhttp://sagenb.org/home/pub/1139/\n\nby pasting the URL into the middle box of the upload page on a (fairly fresh) 4.3.1 install.  When I opened up the worksheet on the local server, the title was cut off to be about 14 characters long.  This is a bug.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8165\n\n",
    "created_at": "2010-02-03T05:39:24Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "title cuts off on worksheet upload",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8165",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

I just tried uploading the following worksheet:

http://sagenb.org/home/pub/1139/

by pasting the URL into the middle box of the upload page on a (fairly fresh) 4.3.1 install.  When I opened up the worksheet on the local server, the title was cut off to be about 14 characters long.  This is a bug.


Issue created by migration from https://trac.sagemath.org/ticket/8165





---

archive/issue_comments_071720.json:
```json
{
    "body": "Attachment [trac_8165-download_ws_name.patch](tarball://root/attachments/some-uuid/ticket8165/trac_8165-download_ws_name.patch) by @qed777 created at 2010-02-03 06:17:36\n\nDon't use `rstrip` to chop `'.sws'`.  sagenb repo.",
    "created_at": "2010-02-03T06:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8165#issuecomment-71720",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8165-download_ws_name.patch](tarball://root/attachments/some-uuid/ticket8165/trac_8165-download_ws_name.patch) by @qed777 created at 2010-02-03 06:17:36

Don't use `rstrip` to chop `'.sws'`.  sagenb repo.



---

archive/issue_comments_071721.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T06:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8165#issuecomment-71721",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071722.json:
```json
{
    "body": "The problem is the use of [str.rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip) in `twist.Worksheet_download`:\n\n```python\nsage: '112 - 01 - Review.sws'.rstrip('.sws')\n'112 - 01 - Revie'\n```\n\nThe patch uses `str.endswith` and a slice, instead.",
    "created_at": "2010-02-03T06:20:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8165#issuecomment-71722",
    "user": "https://github.com/qed777"
}
```

The problem is the use of [str.rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip) in `twist.Worksheet_download`:

```python
sage: '112 - 01 - Review.sws'.rstrip('.sws')
'112 - 01 - Revie'
```

The patch uses `str.endswith` and a slice, instead.



---

archive/issue_comments_071723.json:
```json
{
    "body": "Related: #7663, #7924.\n\nTo review this, if you have the time, I suggest using the latest spkg at #8051.",
    "created_at": "2010-02-03T06:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8165#issuecomment-71723",
    "user": "https://github.com/qed777"
}
```

Related: #7663, #7924.

To review this, if you have the time, I suggest using the latest spkg at #8051.



---

archive/issue_comments_071724.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-07T06:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8165#issuecomment-71724",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071725.json:
```json
{
    "body": "I've reproduced the problem on 4.3.1, then applied the patch on top of sagenb-0.7.4.spkg and the title survives properly when saved to an sws file and subsequently loaded into a notebook.\n\nPositive review.",
    "created_at": "2010-02-07T06:49:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8165#issuecomment-71725",
    "user": "https://github.com/rbeezer"
}
```

I've reproduced the problem on 4.3.1, then applied the patch on top of sagenb-0.7.4.spkg and the title survives properly when saved to an sws file and subsequently loaded into a notebook.

Positive review.



---

archive/issue_events_008369.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-10T18:32:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8165",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8165#event-8369"
}
```



---

archive/issue_comments_071726.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-10T18:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8165#issuecomment-71726",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
