# Issue 6353: change cookies structure to support multiple notebook logins at different ports

archive/issues_006353.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  boothby\n\nAt present, a user cannot log into two different notebooks at the same address with different ports.  For example, if I run two notebooks at\n\nhttp://sage.math.washington.edu:8001\n\nand\n\nhttp://sage.math.washington.edu:8002\n\nthen I can only use one at a time unless I use two separate browsers.  A simple change to the cookies should fix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6353\n\n",
    "created_at": "2009-06-18T00:07:45Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "change cookies structure to support multiple notebook logins at different ports",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6353",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby

CC:  boothby

At present, a user cannot log into two different notebooks at the same address with different ports.  For example, if I run two notebooks at

http://sage.math.washington.edu:8001

and

http://sage.math.washington.edu:8002

then I can only use one at a time unless I use two separate browsers.  A simple change to the cookies should fix this.

Issue created by migration from https://trac.sagemath.org/ticket/6353





---

archive/issue_comments_050693.json:
```json
{
    "body": "Attachment [trac_6353-cookies-diff-ports.patch](tarball://root/attachments/some-uuid/ticket6353/trac_6353-cookies-diff-ports.patch) by @TimDumol created at 2010-01-19 11:06:55\n\nAppends port number to the cookie names.",
    "created_at": "2010-01-19T11:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6353#issuecomment-50693",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_6353-cookies-diff-ports.patch](tarball://root/attachments/some-uuid/ticket6353/trac_6353-cookies-diff-ports.patch) by @TimDumol created at 2010-01-19 11:06:55

Appends port number to the cookie names.



---

archive/issue_comments_050694.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T11:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6353#issuecomment-50694",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050695.json:
```json
{
    "body": "This should do the trick.",
    "created_at": "2010-01-19T11:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6353#issuecomment-50695",
    "user": "https://github.com/TimDumol"
}
```

This should do the trick.



---

archive/issue_comments_050696.json:
```json
{
    "body": "Nice excuse to try out [Firecookie](https://addons.mozilla.org/en-US/firefox/addon/6683).",
    "created_at": "2010-01-20T03:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6353#issuecomment-50696",
    "user": "https://github.com/qed777"
}
```

Nice excuse to try out [Firecookie](https://addons.mozilla.org/en-US/firefox/addon/6683).



---

archive/issue_comments_050697.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T03:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6353#issuecomment-50697",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050698.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6353#issuecomment-50698",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_014945.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-25T00:52:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6353",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6353#event-14945"
}
```
