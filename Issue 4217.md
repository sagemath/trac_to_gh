# Issue 4217: notebook -- formatting of cells  beginning with "%hide %html" is not saved

Issue created by migration from https://trac.sagemath.org/ticket/4217

Original creator: mabshoff

Original creation time: 2008-09-29 18:17:11

Assignee: boothby

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



---

Comment by mabshoff created at 2008-09-30 08:56:00

Notice that now there is a concrete example in the above thread. It cannot be copy and pasted here since the wiki interprets part of the syntax.

Cheers,

Michael


---

Comment by mhansen created at 2009-01-24 05:54:48

I can reproduce this on sagenb.org, but I can't after some of my notebook patches.  I think we might be able to resolve this as fixed in 3.3.  I'll check in 3.3.alpha1 when I get ahold of it.


---

Comment by mhansen created at 2009-01-24 05:54:48

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-24 05:54:48

Changing assignee from boothby to mhansen.


---

Attachment

Removes Cell.__is_html and instead depends on the Cell.system() call for html cell detection


---

Comment by timdumol created at 2010-01-17 01:26:55

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-17 01:26:55

The line breaks should not have been visible in the output in the first place as linebreaks are ignored in html. The line breaks were visible because the output was mistakenly surrounded by <pre> tags, which preformat the whitespace. This is because Cell.__is_html is not properly set on evaluation. This patch removes Cell.__is_html to prevent any future problems, and instead uses the previously included check using Cell.system().


---

Attachment

Rebase on new


---

Comment by timdumol created at 2010-01-17 21:59:25

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

Comment by mpatel created at 2010-01-18 11:03:01

A related problem: The input cells with the `%hide` directive are not hidden upon page load.  I think we just need to use `input_cls` in `cell.html`.


---

Comment by mpatel created at 2010-01-19 11:55:57

Uses `input_cell` in `cell.html`.  Replaces previous.


---

Comment by mpatel created at 2010-01-19 13:18:01

Changing status from needs_review to positive_review.


---

Attachment

I've attached V3, which just uses `cell.html`'s `input_cls`.

Sometimes, evaluating a cell with `%hide` at its top doesn't hide it.  This is a separate problem, apparently

Positive review on this ticket.  Feel free to ignore V3.


---

Comment by mpatel created at 2010-01-25 00:51:44

Resolution: fixed


---

Comment by mpatel created at 2010-02-06 19:37:31

Note: The commit strings for all of the patches above are actually for #3154.  I merged version 3 into SageNB 0.7 at #8051.
