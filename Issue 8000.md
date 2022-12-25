# Issue 8000: Add # -*- coding: utf-8 -*- to the top of all SageNB .py files

archive/issues_008000.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @TimDumol mvngu\n\nAdding the pragma now to all Python files in SageNB should prevent the increasingly common docbuild errors \n\n```\nreading sources... [ 99%] sagenb/notebook/worksheet\nSphinx error:\n'utf8' codec can't decode bytes in position 420-422: invalid data\n```\nraised when we build the reference manual.\n\nThis is partly a followup to #7249, I think.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8000\n\n",
    "created_at": "2010-01-19T16:26:52Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Add # -*- coding: utf-8 -*- to the top of all SageNB .py files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8000",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @TimDumol mvngu

Adding the pragma now to all Python files in SageNB should prevent the increasingly common docbuild errors 

```
reading sources... [ 99%] sagenb/notebook/worksheet
Sphinx error:
'utf8' codec can't decode bytes in position 420-422: invalid data
```
raised when we build the reference manual.

This is partly a followup to #7249, I think.

Issue created by migration from https://trac.sagemath.org/ticket/8000





---

archive/issue_comments_069783.json:
```json
{
    "body": "Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?",
    "created_at": "2010-01-19T16:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69783",
    "user": "https://github.com/qed777"
}
```

Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?



---

archive/issue_comments_069784.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?\n\nIn particular, post-#7249, we've got non-ASCII Unicode characters in *doctests.*",
    "created_at": "2010-01-19T16:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69784",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:1 mpatel]:
> Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?

In particular, post-#7249, we've got non-ASCII Unicode characters in *doctests.*



---

archive/issue_comments_069785.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?\n\nI'm not sure about this, although I can clearly see the benefit of it. On the one hand, this could be further discouragement to people who want to start with Sage development. Could you send an email to sage-devel polling people about this issue? I mean something along the line of, \"Should each source file have the character encoding preamble # -*- coding: utf-8 -*- ?\". Also see #7999 relating to one file in the Sage library.",
    "created_at": "2010-01-19T16:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69785",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:1 mpatel]:
> Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?

I'm not sure about this, although I can clearly see the benefit of it. On the one hand, this could be further discouragement to people who want to start with Sage development. Could you send an email to sage-devel polling people about this issue? I mean something along the line of, "Should each source file have the character encoding preamble # -*- coding: utf-8 -*- ?". Also see #7999 relating to one file in the Sage library.



---

archive/issue_comments_069786.json:
```json
{
    "body": "Actually, it seems that `# -*- coding: utf-8 -*-` was already at the top of `worksheet.py`.",
    "created_at": "2010-01-19T16:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69786",
    "user": "https://github.com/qed777"
}
```

Actually, it seems that `# -*- coding: utf-8 -*-` was already at the top of `worksheet.py`.



---

archive/issue_comments_069787.json:
```json
{
    "body": "Perhaps a different coding slipped in?",
    "created_at": "2010-01-19T17:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69787",
    "user": "https://github.com/qed777"
}
```

Perhaps a different coding slipped in?



---

archive/issue_comments_069788.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> Perhaps a different coding slipped in?\n\nIt turns out that we could fix this problem (cf. #7249) by making the docstring a unicode or raw string (e.g., `\"\"\"` --> u`\"\"\"` or r`\"\"\"`).",
    "created_at": "2010-01-19T19:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69788",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:5 mpatel]:
> Perhaps a different coding slipped in?

It turns out that we could fix this problem (cf. #7249) by making the docstring a unicode or raw string (e.g., `"""` --> u`"""` or r`"""`).



---

archive/issue_comments_069789.json:
```json
{
    "body": "This adds the coding directive",
    "created_at": "2010-01-19T21:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69789",
    "user": "https://github.com/TimDumol"
}
```

This adds the coding directive



---

archive/issue_comments_069790.json:
```json
{
    "body": "Attachment [trac_8000-utf-8-coding-directive.patch](tarball://root/attachments/some-uuid/ticket8000/trac_8000-utf-8-coding-directive.patch) by @TimDumol created at 2010-01-19 21:05:33\n\nThis patch should do the trick.",
    "created_at": "2010-01-19T21:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69790",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_8000-utf-8-coding-directive.patch](tarball://root/attachments/some-uuid/ticket8000/trac_8000-utf-8-coding-directive.patch) by @TimDumol created at 2010-01-19 21:05:33

This patch should do the trick.



---

archive/issue_comments_069791.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T21:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69791",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069792.json:
```json
{
    "body": "Replying to [comment:7 timdumol]:\n> This patch should do the trick.\n\nIt does, indeed.  V2 also fixes a failed doctest in `sagenb.misc.sageinspect.`",
    "created_at": "2010-01-20T03:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69792",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:7 timdumol]:
> This patch should do the trick.

It does, indeed.  V2 also fixes a failed doctest in `sagenb.misc.sageinspect.`



---

archive/issue_comments_069793.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T03:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69793",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069794.json:
```json
{
    "body": "Fix failed doctest.  Replaces previous.  sagenb repo.",
    "created_at": "2010-01-20T03:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69794",
    "user": "https://github.com/qed777"
}
```

Fix failed doctest.  Replaces previous.  sagenb repo.



---

archive/issue_comments_069795.json:
```json
{
    "body": "Attachment [trac_8000-utf-8-coding-directive.3.patch](tarball://root/attachments/some-uuid/ticket8000/trac_8000-utf-8-coding-directive.3.patch) by @qed777 created at 2010-01-25 00:44:54\n\nRebased for SageNB 0.6 + queue in comment.  Replaces previous.",
    "created_at": "2010-01-25T00:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69795",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8000-utf-8-coding-directive.3.patch](tarball://root/attachments/some-uuid/ticket8000/trac_8000-utf-8-coding-directive.3.patch) by @qed777 created at 2010-01-25 00:44:54

Rebased for SageNB 0.6 + queue in comment.  Replaces previous.



---

archive/issue_comments_069796.json:
```json
{
    "body": "V3 is rebased for this queue (patch version numbers may be off by one):\n\n```\nsagenb-0.6\ntrac_7249-jinja2_v9.5.patch\ntrac_7962-link-worksheets-zip-file.patch\ntrac_7969-escaped-backslash.patch\ntrac_4217-html-system-formatting.3.patch\ntrac_3083-print-documentation.5.patch\ntrac_6182-double-quotes-ws.2.patch\ntrac_5263-publish-url.patch\ntrac_7631-republish-name.patch\ntrac_6353-cookies-diff-ports.patch\ntrac_7207-sagenb-future-import.3.patch\ntrac_8000-utf-8-coding-directive.2.patch\n```",
    "created_at": "2010-01-25T00:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69796",
    "user": "https://github.com/qed777"
}
```

V3 is rebased for this queue (patch version numbers may be off by one):

```
sagenb-0.6
trac_7249-jinja2_v9.5.patch
trac_7962-link-worksheets-zip-file.patch
trac_7969-escaped-backslash.patch
trac_4217-html-system-formatting.3.patch
trac_3083-print-documentation.5.patch
trac_6182-double-quotes-ws.2.patch
trac_5263-publish-url.patch
trac_7631-republish-name.patch
trac_6353-cookies-diff-ports.patch
trac_7207-sagenb-future-import.3.patch
trac_8000-utf-8-coding-directive.2.patch
```



---

archive/issue_comments_069797.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69797",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019173.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-25T00:53:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8000#event-19173"
}
```
