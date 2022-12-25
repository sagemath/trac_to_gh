# Issue 7811: Worksheet list CSS: Account for special characters in login names

archive/issues_007811.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robert-marik @TimDumol @williamstein\n\nWe need to account for this difference\n\n```\n$ grep compile twist.py template.py\ntwist.py:re_valid_username = re.compile('[a-z|A-Z|0-9|_|.|@]*')\ntemplate.py:css_illegal_re = re.compile(r'[^-A-Za-z_0-9]')\n```\nwhen processing the checkboxes in a worksheet listing.  Otherwise, the Archive, Stop, and Delete buttons will not work for users whose login names contain dots (`.`) or [at signs](http://en.wikipedia.org/wiki/At_sign) (``@``).\n\nThis is a follow-up to #7332.  See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/9da7dd211fe5570b) for the bug report.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7811\n\n",
    "closed_at": "2010-01-04T06:57:53Z",
    "created_at": "2010-01-01T22:47:15Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Worksheet list CSS: Account for special characters in login names",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7811",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @robert-marik @TimDumol @williamstein

We need to account for this difference

```
$ grep compile twist.py template.py
twist.py:re_valid_username = re.compile('[a-z|A-Z|0-9|_|.|@]*')
template.py:css_illegal_re = re.compile(r'[^-A-Za-z_0-9]')
```
when processing the checkboxes in a worksheet listing.  Otherwise, the Archive, Stop, and Delete buttons will not work for users whose login names contain dots (`.`) or [at signs](http://en.wikipedia.org/wiki/At_sign) (``@``).

This is a follow-up to #7332.  See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/9da7dd211fe5570b) for the bug report.

Issue created by migration from https://trac.sagemath.org/ticket/7811





---

archive/issue_comments_067467.json:
```json
{
    "body": "Escape /, `@`, and . in worksheet list CSS IDs.  sagenb repo.",
    "created_at": "2010-01-01T23:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67467",
    "user": "https://github.com/qed777"
}
```

Escape /, `@`, and . in worksheet list CSS IDs.  sagenb repo.



---

archive/issue_comments_067468.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-01T23:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67468",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067469.json:
```json
{
    "body": "Attachment [trac_7811-escape_ws_list_ids.patch](tarball://root/attachments/some-uuid/ticket7811/trac_7811-escape_ws_list_ids.patch) by @qed777 created at 2010-01-01 23:05:52\n\nPlease let me know if I've missed any other characters.",
    "created_at": "2010-01-01T23:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67469",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7811-escape_ws_list_ids.patch](tarball://root/attachments/some-uuid/ticket7811/trac_7811-escape_ws_list_ids.patch) by @qed777 created at 2010-01-01 23:05:52

Please let me know if I've missed any other characters.



---

archive/issue_comments_067470.json:
```json
{
    "body": "Why not use /[^-A-Za-z_0-9]/g ? If the regexp for usernames is updated for all valid emails, then '+' will be allowed for usernames, which is illegal as a CSS id.",
    "created_at": "2010-01-02T07:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67470",
    "user": "https://github.com/TimDumol"
}
```

Why not use /[^-A-Za-z_0-9]/g ? If the regexp for usernames is updated for all valid emails, then '+' will be allowed for usernames, which is illegal as a CSS id.



---

archive/issue_comments_067471.json:
```json
{
    "body": "Excellent point.  I'll update the patch.",
    "created_at": "2010-01-02T08:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67471",
    "user": "https://github.com/qed777"
}
```

Excellent point.  I'll update the patch.



---

archive/issue_comments_067472.json:
```json
{
    "body": "Attachment [trac_7811-escape_ws_list_ids_v2.patch](tarball://root/attachments/some-uuid/ticket7811/trac_7811-escape_ws_list_ids_v2.patch) by @qed777 created at 2010-01-02 08:55:41\n\nMore general RegExp.  Replaces previous.",
    "created_at": "2010-01-02T08:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67472",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7811-escape_ws_list_ids_v2.patch](tarball://root/attachments/some-uuid/ticket7811/trac_7811-escape_ws_list_ids_v2.patch) by @qed777 created at 2010-01-02 08:55:41

More general RegExp.  Replaces previous.



---

archive/issue_comments_067473.json:
```json
{
    "body": "Works for me. Is it neceassary to run ./sage -t even when upgrading spkg package?",
    "created_at": "2010-01-02T09:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67473",
    "user": "https://github.com/robert-marik"
}
```

Works for me. Is it neceassary to run ./sage -t even when upgrading spkg package?



---

archive/issue_comments_067474.json:
```json
{
    "body": "If you mean `sage -b` --- it's necessary only for changes to the main Sage library, under `SAGE_ROOT/devel/sage`, but not if you're just installing a spkg.",
    "created_at": "2010-01-02T10:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67474",
    "user": "https://github.com/qed777"
}
```

If you mean `sage -b` --- it's necessary only for changes to the main Sage library, under `SAGE_ROOT/devel/sage`, but not if you're just installing a spkg.



---

archive/issue_comments_067475.json:
```json
{
    "body": "Ideally this should be tested with `sage -t -sagenb` when #7650 comes in, or with a Selenium test (sagenb.testing), specifically in `sagenb.testing.tests.test_accounts`.",
    "created_at": "2010-01-02T10:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67475",
    "user": "https://github.com/TimDumol"
}
```

Ideally this should be tested with `sage -t -sagenb` when #7650 comes in, or with a Selenium test (sagenb.testing), specifically in `sagenb.testing.tests.test_accounts`.



---

archive/issue_comments_067476.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> If you mean `sage -b` --- it's necessary only for changes to the main Sage library, under `SAGE_ROOT/devel/sage`, but not if you're just installing a spkg.\n\n\nNo, I meant actually sage -t. I wondered, if I can give positive review without doctesting.",
    "created_at": "2010-01-02T11:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67476",
    "user": "https://github.com/robert-marik"
}
```

Replying to [comment:5 mpatel]:
> If you mean `sage -b` --- it's necessary only for changes to the main Sage library, under `SAGE_ROOT/devel/sage`, but not if you're just installing a spkg.


No, I meant actually sage -t. I wondered, if I can give positive review without doctesting.



---

archive/issue_comments_067477.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-03T13:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67477",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067478.json:
```json
{
    "body": "Wors fine. Tests passed. Doctests are not meaningful for this patch. Positive review.",
    "created_at": "2010-01-03T13:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67478",
    "user": "https://github.com/robert-marik"
}
```

Wors fine. Tests passed. Doctests are not meaningful for this patch. Positive review.



---

archive/issue_comments_067479.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T06:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67479",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_018703.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-01-04T06:57:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7811#event-18703"
}
```



---

archive/issue_comments_067480.json:
```json
{
    "body": "merged into sagenb-0.4.8",
    "created_at": "2010-01-04T06:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67480",
    "user": "https://github.com/williamstein"
}
```

merged into sagenb-0.4.8
