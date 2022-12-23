# Issue 8000: Add # -*- coding: utf-8 -*- to the top of all SageNB .py files

archive/issues_008000.json:
```json
{
    "body": "Assignee: was\n\nCC:  timdumol mvngu\n\nAdding the pragma now to all Python files in SageNB should prevent the increasingly common docbuild errors \n\n```\nreading sources... [ 99%] sagenb/notebook/worksheet\nSphinx error:\n'utf8' codec can't decode bytes in position 420-422: invalid data\n```\n\nraised when we build the reference manual.\n\nThis is partly a followup to #7249, I think.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8000\n\n",
    "created_at": "2010-01-19T16:26:52Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Add # -*- coding: utf-8 -*- to the top of all SageNB .py files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8000",
    "user": "mpatel"
}
```
Assignee: was

CC:  timdumol mvngu

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

archive/issue_comments_069903.json:
```json
{
    "body": "Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?",
    "created_at": "2010-01-19T16:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69903",
    "user": "mpatel"
}
```

Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?



---

archive/issue_comments_069904.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?\nIn particular, post-#7249, we've got non-ASCII Unicode characters in *doctests.*",
    "created_at": "2010-01-19T16:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69904",
    "user": "mpatel"
}
```

Replying to [comment:1 mpatel]:
> Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?
In particular, post-#7249, we've got non-ASCII Unicode characters in *doctests.*



---

archive/issue_comments_069905.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?\nI'm not sure about this, although I can clearly see the benefit of it. On the one hand, this could be further discouragement to people who want to start with Sage development. Could you send an email to sage-devel polling people about this issue? I mean something along the line of, \"Should each source file have the character encoding preamble # -*- coding: utf-8 -*- ?\". Also see #7999 relating to one file in the Sage library.",
    "created_at": "2010-01-19T16:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69905",
    "user": "mvngu"
}
```

Replying to [comment:1 mpatel]:
> Minh -- Is this OK?  Shall we make another ticket to update the whole Sage library?
I'm not sure about this, although I can clearly see the benefit of it. On the one hand, this could be further discouragement to people who want to start with Sage development. Could you send an email to sage-devel polling people about this issue? I mean something along the line of, "Should each source file have the character encoding preamble # -*- coding: utf-8 -*- ?". Also see #7999 relating to one file in the Sage library.



---

archive/issue_comments_069906.json:
```json
{
    "body": "Actually, it seems that `# -*- coding: utf-8 -*-` was already at the top of `worksheet.py`.",
    "created_at": "2010-01-19T16:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69906",
    "user": "mpatel"
}
```

Actually, it seems that `# -*- coding: utf-8 -*-` was already at the top of `worksheet.py`.



---

archive/issue_comments_069907.json:
```json
{
    "body": "Perhaps a different coding slipped in?",
    "created_at": "2010-01-19T17:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69907",
    "user": "mpatel"
}
```

Perhaps a different coding slipped in?



---

archive/issue_comments_069908.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> Perhaps a different coding slipped in?\nIt turns out that we could fix this problem (cf. #7249) by making the docstring a unicode or raw string (e.g., `\"\"\"` --> u`\"\"\"` or r`\"\"\"`).",
    "created_at": "2010-01-19T19:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69908",
    "user": "mpatel"
}
```

Replying to [comment:5 mpatel]:
> Perhaps a different coding slipped in?
It turns out that we could fix this problem (cf. #7249) by making the docstring a unicode or raw string (e.g., `"""` --> u`"""` or r`"""`).



---

archive/issue_comments_069909.json:
```json
{
    "body": "This adds the coding directive",
    "created_at": "2010-01-19T21:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69909",
    "user": "timdumol"
}
```

This adds the coding directive



---

archive/issue_comments_069910.json:
```json
{
    "body": "Attachment\n\nThis patch should do the trick.",
    "created_at": "2010-01-19T21:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69910",
    "user": "timdumol"
}
```

Attachment

This patch should do the trick.



---

archive/issue_comments_069911.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T21:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69911",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069912.json:
```json
{
    "body": "Replying to [comment:7 timdumol]:\n> This patch should do the trick.\nIt does, indeed.  V2 also fixes a failed doctest in `sagenb.misc.sageinspect.`",
    "created_at": "2010-01-20T03:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69912",
    "user": "mpatel"
}
```

Replying to [comment:7 timdumol]:
> This patch should do the trick.
It does, indeed.  V2 also fixes a failed doctest in `sagenb.misc.sageinspect.`



---

archive/issue_comments_069913.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T03:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69913",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069914.json:
```json
{
    "body": "Fix failed doctest.  Replaces previous.  sagenb repo.",
    "created_at": "2010-01-20T03:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69914",
    "user": "mpatel"
}
```

Fix failed doctest.  Replaces previous.  sagenb repo.



---

archive/issue_comments_069915.json:
```json
{
    "body": "Attachment\n\nRebased for SageNB 0.6 + queue in comment.  Replaces previous.",
    "created_at": "2010-01-25T00:44:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69915",
    "user": "mpatel"
}
```

Attachment

Rebased for SageNB 0.6 + queue in comment.  Replaces previous.



---

archive/issue_comments_069916.json:
```json
{
    "body": "V3 is rebased for this queue (patch version numbers may be off by one):\n\n```\nsagenb-0.6\ntrac_7249-jinja2_v9.5.patch\ntrac_7962-link-worksheets-zip-file.patch\ntrac_7969-escaped-backslash.patch\ntrac_4217-html-system-formatting.3.patch\ntrac_3083-print-documentation.5.patch\ntrac_6182-double-quotes-ws.2.patch\ntrac_5263-publish-url.patch\ntrac_7631-republish-name.patch\ntrac_6353-cookies-diff-ports.patch\ntrac_7207-sagenb-future-import.3.patch\ntrac_8000-utf-8-coding-directive.2.patch\n```\n",
    "created_at": "2010-01-25T00:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69916",
    "user": "mpatel"
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

archive/issue_comments_069917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8000#issuecomment-69917",
    "user": "mpatel"
}
```

Resolution: fixed
