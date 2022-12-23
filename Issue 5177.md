# Issue 5177: Notebook keeps directories for deleted cells

Issue created by migration from https://trac.sagemath.org/ticket/5177

Original creator: kcrisman

Original creation time: 2009-02-04 18:05:26

Assignee: boothby

CC:  ddrake

If you delete a cell, it doesn't delete the directory for the cell, at least not very soon (it does seem that they eventually get deleted).  Should it maybe when you log off the worksheet?  Or maybe immediately.  This is particularly bad when there are large computations or graphics involved, and may contribute to making .sws files rather large even if there are few cells.


---

Comment by mabshoff created at 2009-02-06 23:02:39

3.4 is for ReST tickets only.

Cheers,

Michael


---

Attachment

Uses twisted.internet.threads.deferToThread to delete cell directory on cell delete. Should apply cleanly on sagenb-0.5.0.


---

Comment by timdumol created at 2010-01-17 09:49:49

This hopefully won't cause any performance problems. Anyone mind giving their opinion on this?


---

Comment by timdumol created at 2010-01-17 09:49:49

Changing status from new to needs_review.


---

Attachment

Trivial rebase on new patch queue. (Deletion of one empty line)


---

Comment by timdumol created at 2010-01-17 22:06:13

This is then new patch queue:


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
trac_7962-link-worksheets-zip-file.patch
trac_5177-delete-cell-dirs.patch
```


Sorry for the immense queue.


---

Comment by kcrisman created at 2010-01-18 01:49:30

I can't review this, but thank you so much for doing it - it really annoyed me and it's the sort of background thing that in the long run will make Sage so much better even if no one ever sees it.


---

Comment by mpatel created at 2010-01-19 15:26:45

Changing status from needs_review to needs_info.


---

Comment by mpatel created at 2010-01-19 15:26:45

If I evaluate 

```python
print 'Hello!'
plot(sin(x))
```

then "Delete All Output," "Save & quit" and reopen the worksheet, the plot (not the text) reappears.

We could also delete the cells' files in `Worksheet.delete_all_output`.  But we may wish to do this synchronously; otherwise, a long-running or simply delayed (e.g., on a busy server) thread might remove newly-written files.

(For deleting just one cell, there might be a similar but less likely race condition.  For example, if after deleting a cell (with ID <id>) in the browser, a user pastes and saves ``id=<id>|\n<updated code>///\n\n`` in the "Edit" window, and re-evaluates the cell, a delayed `Deferred` could delete new files.)

What do most users expect/prefer?

I'm adding `schilly` to the Cc: list, since he's almost certainly better qualified than I on this (and many other) topics.


---

Attachment

Also delete files when deleting all output.  Synchronous only.  Replaces previous.


---

Comment by mpatel created at 2010-01-25 07:33:05

Changing status from needs_info to needs_review.


---

Comment by mpatel created at 2010-01-25 07:33:05

V3 deletes the output synchronously (on the server), whether it's for one cell or for the whole worksheet.

I think this is much safer, since it avoids race conditions.  Although deferred deletions could help performance, we already copy a cell's output synchronously.  But with the appropriate locks or other synchronization constructs (e.g., "marking" cells for deletion), we could offload some tasks to other threads or to worksheet processes.


---

Comment by mpatel created at 2010-03-07 23:48:18

We should be able to doctest both "hunks" on V3.


---

Comment by mpatel created at 2010-03-07 23:48:18

Changing status from needs_review to needs_work.


---

Attachment

Add doctects to V3.  Apply only this patch.  sagenb repo.


---

Comment by mpatel created at 2010-03-09 10:22:28

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-04-18 07:45:10

Since a major problem with the notebook right now is its performance, and this may slow it down even further, I'm putting this to "Needs work; requires optimization".


---

Comment by timdumol created at 2010-04-18 07:45:10

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-11-30 08:34:40

Changing priority from major to critical.


---

Comment by jdemeyer created at 2011-11-30 08:34:40

Replying to [comment:9 timdumol]:
> Since a major problem with the notebook right now is its performance, and this may slow it down even further
How should this patch slow things down?  The new code is only called when deleting a cell.  In fact, it could even speed up the notebook as there will be fewer files around.


---

Comment by jdemeyer created at 2011-11-30 08:34:40

Changing status from needs_work to needs_review.


---

Comment by jason created at 2011-11-30 09:28:49

Resolution: fixed


---

Comment by jason created at 2011-11-30 09:28:49

Looks good to me.  I applied a modified version to the flask notebook in this commit: http://code.google.com/r/jasongrout-flask-sagenb/source/detail?r=01b77dc4c1934eb0b54a16e19037f3d89f312482


---

Comment by jason created at 2011-11-30 09:29:04

Resolution changed from fixed to 


---

Comment by jason created at 2011-11-30 09:29:04

Changing status from closed to new.


---

Comment by jason created at 2011-11-30 09:29:13

Changing status from new to needs_review.


---

Comment by jason created at 2011-11-30 09:29:19

Changing status from needs_review to positive_review.


---

Comment by jason created at 2011-11-30 09:30:16

I'm not sure if I should have closed this.  I'll leave it as positive review for now, since I suppose it could also be applied to the current notebook.  The code looks fine to apply to the current notebook, but I don't know if it will apply cleanly, etc.


---

Comment by jdemeyer created at 2011-11-30 09:35:04

Replying to [comment:15 jason]:
> I'm not sure if I should have closed this.
Only the release manager should ever close tickets (with the exception of spam tickets or tickets which have no interesting content at all).

> I'll leave it as positive review for now, since I suppose it could also be applied to the current notebook.
Yes, I will merge it.

This reminds me of the fact that we should really discuss how to merge the new notebook, and coordination between the current notebook and the new notebook.  It's a topic which I started several times, but still I don't have a good answer.


---

Comment by novoselt created at 2011-11-30 18:52:11

Is this issue somehow related to #10234 by any chance?


---

Comment by jason created at 2011-11-30 19:06:10

I fixed #10234 a while ago in the flask notebook.  This patch is related; I rebased this patch around the (small) changes I made to fix #10234.


---

Comment by jdemeyer created at 2011-11-30 20:38:24

Replying to [comment:19 jason]:
> I fixed #10234 a while ago in the flask notebook.  This patch is related
In which sense "related".  Does this ticket also fix #10234?  If you fixed #10234 already, it would be good also to merge #10234 in the current sagenb.


---

Comment by jdemeyer created at 2011-11-30 20:55:08

Resolution: fixed
