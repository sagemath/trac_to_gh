# Issue 9918: Wrap wraps-decorator working around bug when used with non-function callables

archive/issues_009918.json:
```json
{
    "body": "Assignee: jason\n\nKeywords: decorators\n\nThe `@`wraps decorator from the Python standard library does not work for non-function callables (e.g. methods) in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, we should have a small work-around.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9919\n\n",
    "created_at": "2010-09-16T14:07:12Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Wrap wraps-decorator working around bug when used with non-function callables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9918",
    "user": "jsrn"
}
```
Assignee: jason

Keywords: decorators

The `@`wraps decorator from the Python standard library does not work for non-function callables (e.g. methods) in Python versions older than 3.2. It was fixed as Python bug issue 3445. Until Sage upgrades to such a new version of Python, we should have a small work-around.

Issue created by migration from https://trac.sagemath.org/ticket/9919





---

archive/issue_comments_098700.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-23T12:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9918#issuecomment-98700",
    "user": "jsrn"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098701.json:
```json
{
    "body": "I hope I'm not being too picky here, but could also note in the source that this was fixed in Python 3.2 and the Python bug number?  That way, when I'm reading the source (much more often than this ticket!), it's easy to determine when we can remove the work around?\n\nThis might be easier to change over on #9089, which I plan to review in conjunction with this ticket.",
    "created_at": "2010-09-23T12:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9918#issuecomment-98701",
    "user": "jason"
}
```

I hope I'm not being too picky here, but could also note in the source that this was fixed in Python 3.2 and the Python bug number?  That way, when I'm reading the source (much more often than this ticket!), it's easy to determine when we can remove the work around?

This might be easier to change over on #9089, which I plan to review in conjunction with this ticket.



---

archive/issue_comments_098702.json:
```json
{
    "body": "No problem. I have fixed #9907 (which was probably the one you meant) to include such a reference.",
    "created_at": "2010-09-24T06:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9918#issuecomment-98702",
    "user": "jsrn"
}
```

No problem. I have fixed #9907 (which was probably the one you meant) to include such a reference.



---

archive/issue_comments_098703.json:
```json
{
    "body": "If I apply #6094, #9907, #9919, and #10107 together on top of sage-4.6, all long tests pass. The code looks good.",
    "created_at": "2010-11-09T20:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9918#issuecomment-98703",
    "user": "rlm"
}
```

If I apply #6094, #9907, #9919, and #10107 together on top of sage-4.6, all long tests pass. The code looks good.



---

archive/issue_comments_098704.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-09T20:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9918#issuecomment-98704",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098705.json:
```json
{
    "body": "Please change the commit message to include the ticket number (use `hg qrefresh -e` for that)",
    "created_at": "2010-11-10T18:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9918#issuecomment-98705",
    "user": "jdemeyer"
}
```

Please change the commit message to include the ticket number (use `hg qrefresh -e` for that)



---

archive/issue_comments_098706.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-11-10T18:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9918#issuecomment-98706",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_098707.json:
```json
{
    "body": "Attachment [trac_9919_workaround_upd_wrapper_bug.patch](tarball://root/attachments/some-uuid/ticket9919/trac_9919_workaround_upd_wrapper_bug.patch) by jsrn created at 2010-11-11 12:56:58\n\nFixed the commit message. Changed back to positive review as the code hasn't changed since Robert Miller's review.",
    "created_at": "2010-11-11T12:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9918#issuecomment-98707",
    "user": "jsrn"
}
```

Attachment [trac_9919_workaround_upd_wrapper_bug.patch](tarball://root/attachments/some-uuid/ticket9919/trac_9919_workaround_upd_wrapper_bug.patch) by jsrn created at 2010-11-11 12:56:58

Fixed the commit message. Changed back to positive review as the code hasn't changed since Robert Miller's review.



---

archive/issue_comments_098708.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-11-11T12:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9918#issuecomment-98708",
    "user": "jsrn"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_098709.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-11T19:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9918",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9918#issuecomment-98709",
    "user": "jdemeyer"
}
```

Resolution: fixed
