# Issue 7811: Worksheet list CSS: Account for special characters in login names

archive/issues_007811.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robert-marik @TimDumol @williamstein\n\nWe need to account for this difference\n\n```\n$ grep compile twist.py template.py\ntwist.py:re_valid_username = re.compile('[a-z|A-Z|0-9|_|.|@]*')\ntemplate.py:css_illegal_re = re.compile(r'[^-A-Za-z_0-9]')\n```\n\nwhen processing the checkboxes in a worksheet listing.  Otherwise, the Archive, Stop, and Delete buttons will not work for users whose login names contain dots (`.`) or [at signs](http://en.wikipedia.org/wiki/At_sign) (``@``).\n\nThis is a follow-up to #7332.  See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/9da7dd211fe5570b) for the bug report.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7811\n\n",
    "created_at": "2010-01-01T22:47:15Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Worksheet list CSS: Account for special characters in login names",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7811",
    "user": "@qed777"
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

archive/issue_comments_067584.json:
```json
{
    "body": "Escape /, `@`, and . in worksheet list CSS IDs.  sagenb repo.",
    "created_at": "2010-01-01T23:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67584",
    "user": "@qed777"
}
```

Escape /, `@`, and . in worksheet list CSS IDs.  sagenb repo.



---

archive/issue_comments_067585.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-01T23:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67585",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067586.json:
```json
{
    "body": "Attachment [trac_7811-escape_ws_list_ids.patch](tarball://root/attachments/some-uuid/ticket7811/trac_7811-escape_ws_list_ids.patch) by @qed777 created at 2010-01-01 23:05:52\n\nPlease let me know if I've missed any other characters.",
    "created_at": "2010-01-01T23:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67586",
    "user": "@qed777"
}
```

Attachment [trac_7811-escape_ws_list_ids.patch](tarball://root/attachments/some-uuid/ticket7811/trac_7811-escape_ws_list_ids.patch) by @qed777 created at 2010-01-01 23:05:52

Please let me know if I've missed any other characters.



---

archive/issue_comments_067587.json:
```json
{
    "body": "Why not use /[^-A-Za-z_0-9]/g ? If the regexp for usernames is updated for all valid emails, then '+' will be allowed for usernames, which is illegal as a CSS id.",
    "created_at": "2010-01-02T07:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67587",
    "user": "@TimDumol"
}
```

Why not use /[^-A-Za-z_0-9]/g ? If the regexp for usernames is updated for all valid emails, then '+' will be allowed for usernames, which is illegal as a CSS id.



---

archive/issue_comments_067588.json:
```json
{
    "body": "Excellent point.  I'll update the patch.",
    "created_at": "2010-01-02T08:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67588",
    "user": "@qed777"
}
```

Excellent point.  I'll update the patch.



---

archive/issue_comments_067589.json:
```json
{
    "body": "Attachment [trac_7811-escape_ws_list_ids_v2.patch](tarball://root/attachments/some-uuid/ticket7811/trac_7811-escape_ws_list_ids_v2.patch) by @qed777 created at 2010-01-02 08:55:41\n\nMore general RegExp.  Replaces previous.",
    "created_at": "2010-01-02T08:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67589",
    "user": "@qed777"
}
```

Attachment [trac_7811-escape_ws_list_ids_v2.patch](tarball://root/attachments/some-uuid/ticket7811/trac_7811-escape_ws_list_ids_v2.patch) by @qed777 created at 2010-01-02 08:55:41

More general RegExp.  Replaces previous.



---

archive/issue_comments_067590.json:
```json
{
    "body": "Works for me. Is it neceassary to run ./sage -t even when upgrading spkg package?",
    "created_at": "2010-01-02T09:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67590",
    "user": "@robert-marik"
}
```

Works for me. Is it neceassary to run ./sage -t even when upgrading spkg package?



---

archive/issue_comments_067591.json:
```json
{
    "body": "If you mean `sage -b` --- it's necessary only for changes to the main Sage library, under `SAGE_ROOT/devel/sage`, but not if you're just installing a spkg.",
    "created_at": "2010-01-02T10:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67591",
    "user": "@qed777"
}
```

If you mean `sage -b` --- it's necessary only for changes to the main Sage library, under `SAGE_ROOT/devel/sage`, but not if you're just installing a spkg.



---

archive/issue_comments_067592.json:
```json
{
    "body": "Ideally this should be tested with `sage -t -sagenb` when #7650 comes in, or with a Selenium test (sagenb.testing), specifically in `sagenb.testing.tests.test_accounts`.",
    "created_at": "2010-01-02T10:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67592",
    "user": "@TimDumol"
}
```

Ideally this should be tested with `sage -t -sagenb` when #7650 comes in, or with a Selenium test (sagenb.testing), specifically in `sagenb.testing.tests.test_accounts`.



---

archive/issue_comments_067593.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> If you mean `sage -b` --- it's necessary only for changes to the main Sage library, under `SAGE_ROOT/devel/sage`, but not if you're just installing a spkg.\n\nNo, I meant actually sage -t. I wondered, if I can give positive review without doctesting.",
    "created_at": "2010-01-02T11:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67593",
    "user": "@robert-marik"
}
```

Replying to [comment:5 mpatel]:
> If you mean `sage -b` --- it's necessary only for changes to the main Sage library, under `SAGE_ROOT/devel/sage`, but not if you're just installing a spkg.

No, I meant actually sage -t. I wondered, if I can give positive review without doctesting.



---

archive/issue_comments_067594.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-03T13:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67594",
    "user": "@robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067595.json:
```json
{
    "body": "Wors fine. Tests passed. Doctests are not meaningful for this patch. Positive review.",
    "created_at": "2010-01-03T13:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67595",
    "user": "@robert-marik"
}
```

Wors fine. Tests passed. Doctests are not meaningful for this patch. Positive review.



---

archive/issue_comments_067596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T06:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67596",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_067597.json:
```json
{
    "body": "merged into sagenb-0.4.8",
    "created_at": "2010-01-04T06:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7811#issuecomment-67597",
    "user": "@williamstein"
}
```

merged into sagenb-0.4.8
