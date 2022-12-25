# Issue 4217: notebook -- formatting of cells  beginning with "%hide %html" is not saved

archive/issues_004217.json:
```json
{
    "body": "Assignee: @mwhansen\n\nIn http://groups.google.com/group/sage-support/browse_thread/thread/642313d7270e789f it was reported:\n\n```\nAs of version 3.1.2, plots are saved correctly in notebooks. Thanks to \nthose that fixed it. However, I noticed that the formatting of cells \nbeginning with \"%hide %html\" is not saved. I need to re-evaluate all \nof those cells to get the formatting back. Is this a bug in SAGE or \ndoes it have something to do with the web browser (Firefox 3.0.3 on \nMac OS X 10.4)? \nThanks again for the great effort! \n\nStan\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4217\n\n",
    "closed_at": "2010-01-25T00:51:44Z",
    "created_at": "2008-09-29T18:17:11Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "notebook -- formatting of cells  beginning with \"%hide %html\" is not saved",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4217",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @mwhansen

In http://groups.google.com/group/sage-support/browse_thread/thread/642313d7270e789f it was reported:

```
As of version 3.1.2, plots are saved correctly in notebooks. Thanks to 
those that fixed it. However, I noticed that the formatting of cells 
beginning with "%hide %html" is not saved. I need to re-evaluate all 
of those cells to get the formatting back. Is this a bug in SAGE or 
does it have something to do with the web browser (Firefox 3.0.3 on 
Mac OS X 10.4)? 
Thanks again for the great effort! 

Stan
```

Issue created by migration from https://trac.sagemath.org/ticket/4217





---

archive/issue_comments_030577.json:
```json
{
    "body": "Notice that now there is a concrete example in the above thread. It cannot be copy and pasted here since the wiki interprets part of the syntax.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T08:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30577",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Notice that now there is a concrete example in the above thread. It cannot be copy and pasted here since the wiki interprets part of the syntax.

Cheers,

Michael



---

archive/issue_comments_030578.json:
```json
{
    "body": "I can reproduce this on sagenb.org, but I can't after some of my notebook patches.  I think we might be able to resolve this as fixed in 3.3.  I'll check in 3.3.alpha1 when I get ahold of it.",
    "created_at": "2009-01-24T05:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30578",
    "user": "https://github.com/mwhansen"
}
```

I can reproduce this on sagenb.org, but I can't after some of my notebook patches.  I think we might be able to resolve this as fixed in 3.3.  I'll check in 3.3.alpha1 when I get ahold of it.



---

archive/issue_comments_030579.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T05:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30579",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030580.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2009-01-24T05:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30580",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_030581.json:
```json
{
    "body": "Attachment [trac_4217-html-system-formatting.patch](tarball://root/attachments/some-uuid/ticket4217/trac_4217-html-system-formatting.patch) by @TimDumol created at 2010-01-17 01:22:36\n\nRemoves Cell.__is_html and instead depends on the Cell.system() call for html cell detection",
    "created_at": "2010-01-17T01:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30581",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_4217-html-system-formatting.patch](tarball://root/attachments/some-uuid/ticket4217/trac_4217-html-system-formatting.patch) by @TimDumol created at 2010-01-17 01:22:36

Removes Cell.__is_html and instead depends on the Cell.system() call for html cell detection



---

archive/issue_comments_030582.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T01:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30582",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_030583.json:
```json
{
    "body": "The line breaks should not have been visible in the output in the first place as linebreaks are ignored in html. The line breaks were visible because the output was mistakenly surrounded by <pre> tags, which preformat the whitespace. This is because Cell.__is_html is not properly set on evaluation. This patch removes Cell.__is_html to prevent any future problems, and instead uses the previously included check using Cell.system().",
    "created_at": "2010-01-17T01:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30583",
    "user": "https://github.com/TimDumol"
}
```

The line breaks should not have been visible in the output in the first place as linebreaks are ignored in html. The line breaks were visible because the output was mistakenly surrounded by <pre> tags, which preformat the whitespace. This is because Cell.__is_html is not properly set on evaluation. This patch removes Cell.__is_html to prevent any future problems, and instead uses the previously included check using Cell.system().



---

archive/issue_comments_030584.json:
```json
{
    "body": "Attachment [trac_4217-html-system-formatting.2.patch](tarball://root/attachments/some-uuid/ticket4217/trac_4217-html-system-formatting.2.patch) by @TimDumol created at 2010-01-17 21:57:15\n\nRebase on new",
    "created_at": "2010-01-17T21:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30584",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_4217-html-system-formatting.2.patch](tarball://root/attachments/some-uuid/ticket4217/trac_4217-html-system-formatting.2.patch) by @TimDumol created at 2010-01-17 21:57:15

Rebase on new



---

archive/issue_comments_030585.json:
```json
{
    "body": "That comment was suppoesd to be \"Rebase on new patch sent\"\n\n```\ntrac_7650-sagenb_doctesting_v6.patch\ntrac_7650-reviewer.patch\ntrac_7648-missing_indent.patch\ntrac_7663-rstrip_prompt.patch\ntrac_7847-empty-trash-no-referer.patch\ntrac_7786-template-jinja-idiomatic.patch\ntrac_7863-declare_vars_aux_js_v2.patch\ntrac_7874-typeset_interact_labels.patch\ntrac_7858-key_binding_vars_v2.patch\ntrac_7666-alphanumeric_cell_ids_B5.patch\ntrac_7666-reviewer.patch\ntrac_7835-preparsing-unicode_v2.patch\ntrac_7249_jinja2_v5.patch\ntrac_2779-sagenb-error-message.patch\n2779_2_banner.patch\ntrac_3154-spurious-u0027-output.patch\ntrac_7969-escaped-backslash.patch\ntrac_7937-sass_manifest.patch\ntrac_4217-html-system-formatting.patch\n```\n\nSorry for the immense patch queue.",
    "created_at": "2010-01-17T21:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30585",
    "user": "https://github.com/TimDumol"
}
```

That comment was suppoesd to be "Rebase on new patch sent"

```
trac_7650-sagenb_doctesting_v6.patch
trac_7650-reviewer.patch
trac_7648-missing_indent.patch
trac_7663-rstrip_prompt.patch
trac_7847-empty-trash-no-referer.patch
trac_7786-template-jinja-idiomatic.patch
trac_7863-declare_vars_aux_js_v2.patch
trac_7874-typeset_interact_labels.patch
trac_7858-key_binding_vars_v2.patch
trac_7666-alphanumeric_cell_ids_B5.patch
trac_7666-reviewer.patch
trac_7835-preparsing-unicode_v2.patch
trac_7249_jinja2_v5.patch
trac_2779-sagenb-error-message.patch
2779_2_banner.patch
trac_3154-spurious-u0027-output.patch
trac_7969-escaped-backslash.patch
trac_7937-sass_manifest.patch
trac_4217-html-system-formatting.patch
```

Sorry for the immense patch queue.



---

archive/issue_comments_030586.json:
```json
{
    "body": "A related problem: The input cells with the `%hide` directive are not hidden upon page load.  I think we just need to use `input_cls` in `cell.html`.",
    "created_at": "2010-01-18T11:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30586",
    "user": "https://github.com/qed777"
}
```

A related problem: The input cells with the `%hide` directive are not hidden upon page load.  I think we just need to use `input_cls` in `cell.html`.



---

archive/issue_comments_030587.json:
```json
{
    "body": "Uses `input_cell` in `cell.html`.  Replaces previous.",
    "created_at": "2010-01-19T11:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30587",
    "user": "https://github.com/qed777"
}
```

Uses `input_cell` in `cell.html`.  Replaces previous.



---

archive/issue_comments_030588.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T13:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30588",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_030589.json:
```json
{
    "body": "Attachment [trac_4217-html-system-formatting.3.patch](tarball://root/attachments/some-uuid/ticket4217/trac_4217-html-system-formatting.3.patch) by @qed777 created at 2010-01-19 13:18:01\n\nI've attached V3, which just uses `cell.html`'s `input_cls`.\n\nSometimes, evaluating a cell with `%hide` at its top doesn't hide it.  This is a separate problem, apparently\n\nPositive review on this ticket.  Feel free to ignore V3.",
    "created_at": "2010-01-19T13:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30589",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_4217-html-system-formatting.3.patch](tarball://root/attachments/some-uuid/ticket4217/trac_4217-html-system-formatting.3.patch) by @qed777 created at 2010-01-19 13:18:01

I've attached V3, which just uses `cell.html`'s `input_cls`.

Sometimes, evaluating a cell with `%hide` at its top doesn't hide it.  This is a separate problem, apparently

Positive review on this ticket.  Feel free to ignore V3.



---

archive/issue_comments_030590.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T00:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30590",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009550.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-25T00:51:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4217#event-9550"
}
```



---

archive/issue_comments_030591.json:
```json
{
    "body": "Note: The commit strings for all of the patches above are actually for #3154.  I merged version 3 into SageNB 0.7 at #8051.",
    "created_at": "2010-02-06T19:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4217#issuecomment-30591",
    "user": "https://github.com/qed777"
}
```

Note: The commit strings for all of the patches above are actually for #3154.  I merged version 3 into SageNB 0.7 at #8051.
