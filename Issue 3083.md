# Issue 3083: Print does not include documentation

Issue created by migration from https://trac.sagemath.org/ticket/3083

Original creator: rlm

Original creation time: 2008-05-02 19:43:37

Assignee: boothby

CC:  was

If I type `sage.graphs.chrompoly??` for example in a cell, and evaluate, I get a nice chunk of code. But when I hit "print", all I get is the input. Docs should be included in the printed worksheets.


---

Comment by timdumol created at 2010-01-16 21:10:24

This bug is caused by the fact that introspection output is not saved with the worksheet. Should this be the case?


---

Comment by timdumol created at 2010-01-17 08:26:51

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-17 08:26:51

This should do the job.


---

Comment by timdumol created at 2010-01-17 08:34:15

Makes evaluated (S-Enter, eval link, etc.) introspection show up in print while clearly marking that TAB introspected output is unprinted (also makes it draggable).


---

Attachment

Big +1 to this design approach.


---

Comment by timdumol created at 2010-01-17 22:03:50

Rebase on a new patch set.


---

Attachment

The new patch set is:


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
trac_3083-print-documentation.patch
```


Sorry for the immense patch queue.


---

Comment by mpatel created at 2010-01-20 01:41:48

Well done!

 * "Closing" a dialog does not remove it from the DOM.  It's just hidden.  I suggest mapping the close button to, e.g., `$('.dialog').dialog('destroy').remove();`.

 * For `'eval'`-method docstrings, the sans-serif font becomes monospaced.

 * I suggest changing "Click on the box..." to, e.g., "Click here..." and binding the click event to just that `div`.  Otherwise, users who click on the docstring as they read it and/or copy examples might get an unwanted dialog.

 * It might be worth it to mention on the "Help" page or in the tutorial which docstrings are printable.

 * If I evaluate `factor?` in a cell, I can print the docstring with the worksheet, as desired.  People might also find it useful for evaluated docstrings to survive reopening the worksheet or to appear in published worksheets (e.g., as part of an annotated tutorial).  But I suggest waiting for feedback on the mailing lists and, if it's necessary, creating new tickets.


---

Comment by mpatel created at 2010-01-20 03:35:14

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2010-01-20 08:34:59

Has all the requested changes by Patel.


---

Comment by timdumol created at 2010-01-20 08:36:44

Changing status from needs_work to needs_review.


---

Attachment

Thanks for catching all of that, especially the last point. That was what I intended, and William and others here agreed with it, so it seems to be ok to implement. This patch should implement everything. I have opened a new patch to include sagenb.notebook.tutorial into the ReST documentation too: #8011.


---

Comment by mpatel created at 2010-01-21 12:53:17

Various fixes, small enhancements.  See comment.  Replaces previous.


---

Attachment


---

Attachment

V4.2

 * Implements the "last point" above in a different way.  With V3, the output formatting didn't persist --- docstrings in restarted/reopened and published worksheets were escaped.  Docstrings also appeared twice in each output cell.

 * Popping now
   * Resets the cell's introspection state.
   * Puts the object's name in the dialog title, with a bit of color.
   * Destroys just that dialog on close.  The previous query was broad enough that it could close multiple dialogs.

 * Moves `"""nodoctest\n"""` back to the top of `notebook_object.py`.

Again, great work!  My review is positive, but someone should review my changes.


---

Comment by mpatel created at 2010-01-21 13:15:43

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-22 22:54:13

Moves the module docstring to the top as well.


---

Attachment

Positive review for your changes, but I've added a new patch that moves the module docstring of `notebook_object.py` to the top of the file, otherwise documentation won't build (the notebook must be `setup.py instal`ed for the updated documentation to build).


---

Comment by mpatel created at 2010-01-25 00:57:52

Resolution: fixed


---

Comment by mpatel created at 2010-01-30 05:52:40

Don't truncate long docstrings.  Apply on top of previous patch, e.g., #8051's sagenb-0.7.1.


---

Attachment

I've added a "notruncate" patch that blocks #8051.


---

Comment by was created at 2010-01-30 23:52:18

Positive review about the idea of adding notruncate.  That makes perfect sense to me.
