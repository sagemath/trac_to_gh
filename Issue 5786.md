# Issue 5786: interrupt makes truncated output --> /dev/null

Issue created by migration from https://trac.sagemath.org/ticket/5786

Original creator: rlm

Original creation time: 2009-04-14 18:47:45

Assignee: boothby

CC:  was mhansen boothby

If you print a large amount, but interrupt while the cell is evaluating, then you can't see the middle, because the output is truncated but the link to see it isn't there yet.


---

Comment by timdumol created at 2010-01-18 19:37:14

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

Comment by timdumol created at 2010-01-19 03:11:19

Works with sagenb-0.6


---

Comment by timdumol created at 2010-01-19 03:11:19

Resolution: duplicate


---

Comment by timdumol created at 2010-01-19 03:37:25

Resolution changed from duplicate to fixed
