# Issue 5786: interrupt makes truncated output --> /dev/null

archive/issues_005786.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was mhansen boothby\n\nIf you print a large amount, but interrupt while the cell is evaluating, then you can't see the middle, because the output is truncated but the link to see it isn't there yet.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5786\n\n",
    "created_at": "2009-04-14T18:47:45Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "interrupt makes truncated output --> /dev/null",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5786",
    "user": "rlm"
}
```
Assignee: boothby

CC:  was mhansen boothby

If you print a large amount, but interrupt while the cell is evaluating, then you can't see the middle, because the output is truncated but the link to see it isn't there yet.

Issue created by migration from https://trac.sagemath.org/ticket/5786





---

archive/issue_comments_045289.json:
```json
{
    "body": "This seems to be fixed after this patch queue:\n\n\n```\ntrac_7650-sagenb_doctesting_v6.patch\ntrac_7650-reviewer.patch\ntrac_7648-missing_indent.patch\ntrac_7663-rstrip_prompt.patch\ntrac_7847-empty-trash-no-referer.patch\ntrac_7786-template-jinja-idiomatic.patch\ntrac_7863-declare_vars_aux_js_v2.patch\ntrac_7874-typeset_interact_labels.patch\ntrac_7858-key_binding_vars_v2.patch\ntrac_7666-alphanumeric_cell_ids_B5.patch\ntrac_7666-reviewer.patch\ntrac_7835-preparsing-unicode_v2.patch\ntrac_7249_jinja2_v5.patch\ntrac_2779-sagenb-error-message.patch\n2779_2_banner.patch\n3154_escaping_quotes.2.patch\ntrac_7969-escaped-backslash.patch\ntrac_7937-sass_manifest.patch\ntrac_4217-html-system-formatting.patch\ntrac_3083-print-documentation.patch\ntrac_7962-link-worksheets-zip-file.patch\ntrac_5177-delete-cell-dirs.patch\ntrac_5712-interrupt-notification.patch\ntrac_6182-double-quotes-ws.patch\n```\n\n\nI'm guessing #5712 is the one that fixed it. This should probably be marked as fixed.",
    "created_at": "2010-01-18T19:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5786#issuecomment-45289",
    "user": "timdumol"
}
```

This seems to be fixed after this patch queue:


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
3154_escaping_quotes.2.patch
trac_7969-escaped-backslash.patch
trac_7937-sass_manifest.patch
trac_4217-html-system-formatting.patch
trac_3083-print-documentation.patch
trac_7962-link-worksheets-zip-file.patch
trac_5177-delete-cell-dirs.patch
trac_5712-interrupt-notification.patch
trac_6182-double-quotes-ws.patch
```


I'm guessing #5712 is the one that fixed it. This should probably be marked as fixed.



---

archive/issue_comments_045290.json:
```json
{
    "body": "Works with sagenb-0.6",
    "created_at": "2010-01-19T03:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5786#issuecomment-45290",
    "user": "timdumol"
}
```

Works with sagenb-0.6



---

archive/issue_comments_045291.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5786#issuecomment-45291",
    "user": "timdumol"
}
```

Resolution: duplicate



---

archive/issue_comments_045292.json:
```json
{
    "body": "Resolution changed from duplicate to fixed",
    "created_at": "2010-01-19T03:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5786#issuecomment-45292",
    "user": "timdumol"
}
```

Resolution changed from duplicate to fixed
