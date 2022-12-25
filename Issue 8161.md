# Issue 8161: use Sphinx to produce docstrings from the command line

archive/issues_008161.json:
```json
{
    "body": "Assignee: mvngu\n\nThe attached patch uses Sphinx to produce docstrings from the command line.  The docstrings are still plain text, but among other things, all double colons should be turned into single colons.  The patch also (by hand) changes ```text``` to `\"text\"`, which I think looks better and conveys the same information.\n\nIt also no longer replaces `\\\\` with `\\\\\\\\` for docstrings in the notebook, since there is a line in sphinxify that just undoes this.\n\nThis depends on #8160.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8161\n\n",
    "created_at": "2010-02-03T02:34:04Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "use Sphinx to produce docstrings from the command line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8161",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: mvngu

The attached patch uses Sphinx to produce docstrings from the command line.  The docstrings are still plain text, but among other things, all double colons should be turned into single colons.  The patch also (by hand) changes ```text``` to `"text"`, which I think looks better and conveys the same information.

It also no longer replaces `\\` with `\\\\` for docstrings in the notebook, since there is a line in sphinxify that just undoes this.

This depends on #8160.


Issue created by migration from https://trac.sagemath.org/ticket/8161





---

archive/issue_comments_071658.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T02:35:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71658",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071659.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-03T03:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71659",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071660.json:
```json
{
    "body": "I think the idea is good, but this needs work; I'm getting some doctest failures with this patch:\n\n```\nThe following tests failed:\n\n\tsage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests failed\n\tsage -t -long devel/sage/sage/structure/element.pyx # 1 doctests failed\n\tsage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 6 doctests failed\n\tsage -t -long devel/sage/sage/structure/element_wrapper.py # Segfault\n\tsage -t -long devel/sage/sage/misc/sageinspect.py # 4 doctests failed\n\tsage -t -long devel/sage/sage/structure/dynamic_class.py # 1 doctests failed\n```\n\nI'll try to work on them, and anyone else who is interested can do the same.",
    "created_at": "2010-02-03T03:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71660",
    "user": "https://github.com/jhpalmieri"
}
```

I think the idea is good, but this needs work; I'm getting some doctest failures with this patch:

```
The following tests failed:

	sage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
	sage -t -long devel/sage/sage/structure/element.pyx # 1 doctests failed
	sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 6 doctests failed
	sage -t -long devel/sage/sage/structure/element_wrapper.py # Segfault
	sage -t -long devel/sage/sage/misc/sageinspect.py # 4 doctests failed
	sage -t -long devel/sage/sage/structure/dynamic_class.py # 1 doctests failed
```

I'll try to work on them, and anyone else who is interested can do the same.



---

archive/issue_comments_071661.json:
```json
{
    "body": "Attachment [trac_8161-sphinxify.patch](tarball://root/attachments/some-uuid/ticket8161/trac_8161-sphinxify.patch) by @jhpalmieri created at 2010-02-03 04:40:52",
    "created_at": "2010-02-03T04:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71661",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8161-sphinxify.patch](tarball://root/attachments/some-uuid/ticket8161/trac_8161-sphinxify.patch) by @jhpalmieri created at 2010-02-03 04:40:52



---

archive/issue_comments_071662.json:
```json
{
    "body": "With this patch, all tests pass on boxen.",
    "created_at": "2010-02-03T04:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71662",
    "user": "https://github.com/jhpalmieri"
}
```

With this patch, all tests pass on boxen.



---

archive/issue_comments_071663.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-03T04:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71663",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071664.json:
```json
{
    "body": "This looks good.  I noticed an existing problem with Unicode docstrings.  With #8051 and with or without #8167,\n\n```python\nsage: sagenb.notebook.worksheet.Worksheet.name?\nsage: sagenb.misc.misc.unicode_str?\n```\n\nhave `'<no docstring>'`.  V2 should fix this.",
    "created_at": "2010-02-04T06:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71664",
    "user": "https://github.com/qed777"
}
```

This looks good.  I noticed an existing problem with Unicode docstrings.  With #8051 and with or without #8167,

```python
sage: sagenb.notebook.worksheet.Worksheet.name?
sage: sagenb.misc.misc.unicode_str?
```

have `'<no docstring>'`.  V2 should fix this.



---

archive/issue_comments_071665.json:
```json
{
    "body": "Attachment [trac_8161-sphinxify_cmd_line.2.patch](tarball://root/attachments/some-uuid/ticket8161/trac_8161-sphinxify_cmd_line.2.patch) by @qed777 created at 2010-02-04 06:53:13\n\nHandle Unicode docstrings.  Replaces previous.  **sage** repo.",
    "created_at": "2010-02-04T06:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71665",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8161-sphinxify_cmd_line.2.patch](tarball://root/attachments/some-uuid/ticket8161/trac_8161-sphinxify_cmd_line.2.patch) by @qed777 created at 2010-02-04 06:53:13

Handle Unicode docstrings.  Replaces previous.  **sage** repo.



---

archive/issue_comments_071666.json:
```json
{
    "body": "Update `sagenb.misc.sageinspect` doctests.  **sagenb** repo.",
    "created_at": "2010-02-04T06:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71666",
    "user": "https://github.com/qed777"
}
```

Update `sagenb.misc.sageinspect` doctests.  **sagenb** repo.



---

archive/issue_comments_071667.json:
```json
{
    "body": "Attachment [trac_8161-sagenb_sageinspect.patch](tarball://root/attachments/some-uuid/ticket8161/trac_8161-sagenb_sageinspect.patch) by @qed777 created at 2010-02-04 06:59:21\n\nV2 replaces `return str(r)` with\n\n```python\n    from sagenb.misc.misc import encoded_str\n    return encoded_str(r)\n```\n\nin `sage.misc.sageinspect._sage_getdoc_unformatted`.\n\nThe sagenb patch depends on #8051 + #8167 + #8102 + #8160.",
    "created_at": "2010-02-04T06:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71667",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8161-sagenb_sageinspect.patch](tarball://root/attachments/some-uuid/ticket8161/trac_8161-sagenb_sageinspect.patch) by @qed777 created at 2010-02-04 06:59:21

V2 replaces `return str(r)` with

```python
    from sagenb.misc.misc import encoded_str
    return encoded_str(r)
```

in `sage.misc.sageinspect._sage_getdoc_unformatted`.

The sagenb patch depends on #8051 + #8167 + #8102 + #8160.



---

archive/issue_comments_071668.json:
```json
{
    "body": "On further reflection, I've decided that replacing ```` with `\"` is a bad idea.  It's complicated, and it can make some docstrings less clear.  For example, should ```\"text\"``` be turned into `\"text\"` or `\"'text'\"`?  What about ```algorithm=\"gap\"```: turn it into `\"algorithm='gap'\"`?  What about (from sage.interfaces.sage0.Sage) the beautiful ```s('\"x\"')```?\n\nIf we eventually decide this is a good idea, we can do it in another ticket (or submit it as a possible customization for text output in Sphinx), but I'm taking it out for now.\n\nA few doctests in sage and sagenb need to be changed as a consequence; see the new patches.",
    "created_at": "2010-02-05T03:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71668",
    "user": "https://github.com/jhpalmieri"
}
```

On further reflection, I've decided that replacing ```` with `"` is a bad idea.  It's complicated, and it can make some docstrings less clear.  For example, should ```"text"``` be turned into `"text"` or `"'text'"`?  What about ```algorithm="gap"```: turn it into `"algorithm='gap'"`?  What about (from sage.interfaces.sage0.Sage) the beautiful ```s('"x"')```?

If we eventually decide this is a good idea, we can do it in another ticket (or submit it as a possible customization for text output in Sphinx), but I'm taking it out for now.

A few doctests in sage and sagenb need to be changed as a consequence; see the new patches.



---

archive/issue_comments_071669.json:
```json
{
    "body": "for sage repo",
    "created_at": "2010-02-05T03:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71669",
    "user": "https://github.com/jhpalmieri"
}
```

for sage repo



---

archive/issue_comments_071670.json:
```json
{
    "body": "Attachment [trac_8161-sagenb_sageinspect-v2.patch](tarball://root/attachments/some-uuid/ticket8161/trac_8161-sagenb_sageinspect-v2.patch) by @jhpalmieri created at 2010-02-05 03:56:33\n\nfor sagenb repo",
    "created_at": "2010-02-05T03:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71670",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8161-sagenb_sageinspect-v2.patch](tarball://root/attachments/some-uuid/ticket8161/trac_8161-sagenb_sageinspect-v2.patch) by @jhpalmieri created at 2010-02-05 03:56:33

for sagenb repo



---

archive/issue_comments_071671.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-05T07:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71671",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071672.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8161#issuecomment-71672",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_008365.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-02-11T14:53:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8161",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8161#event-8365"
}
```
