# Issue 5177: Notebook keeps directories for deleted cells

archive/issues_005177.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @dandrake\n\nIf you delete a cell, it doesn't delete the directory for the cell, at least not very soon (it does seem that they eventually get deleted).  Should it maybe when you log off the worksheet?  Or maybe immediately.  This is particularly bad when there are large computations or graphics involved, and may contribute to making .sws files rather large even if there are few cells.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5177\n\n",
    "created_at": "2009-02-04T18:05:26Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "Notebook keeps directories for deleted cells",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5177",
    "user": "@kcrisman"
}
```
Assignee: boothby

CC:  @dandrake

If you delete a cell, it doesn't delete the directory for the cell, at least not very soon (it does seem that they eventually get deleted).  Should it maybe when you log off the worksheet?  Or maybe immediately.  This is particularly bad when there are large computations or graphics involved, and may contribute to making .sws files rather large even if there are few cells.

Issue created by migration from https://trac.sagemath.org/ticket/5177





---

archive/issue_comments_039655.json:
```json
{
    "body": "3.4 is for ReST tickets only.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T23:02:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39655",
    "user": "mabshoff"
}
```

3.4 is for ReST tickets only.

Cheers,

Michael



---

archive/issue_comments_039656.json:
```json
{
    "body": "Attachment [trac_5177-delete-cell-dirs.patch](tarball://root/attachments/some-uuid/ticket5177/trac_5177-delete-cell-dirs.patch) by @TimDumol created at 2010-01-17 09:48:43\n\nUses twisted.internet.threads.deferToThread to delete cell directory on cell delete. Should apply cleanly on sagenb-0.5.0.",
    "created_at": "2010-01-17T09:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39656",
    "user": "@TimDumol"
}
```

Attachment [trac_5177-delete-cell-dirs.patch](tarball://root/attachments/some-uuid/ticket5177/trac_5177-delete-cell-dirs.patch) by @TimDumol created at 2010-01-17 09:48:43

Uses twisted.internet.threads.deferToThread to delete cell directory on cell delete. Should apply cleanly on sagenb-0.5.0.



---

archive/issue_comments_039657.json:
```json
{
    "body": "This hopefully won't cause any performance problems. Anyone mind giving their opinion on this?",
    "created_at": "2010-01-17T09:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39657",
    "user": "@TimDumol"
}
```

This hopefully won't cause any performance problems. Anyone mind giving their opinion on this?



---

archive/issue_comments_039658.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T09:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39658",
    "user": "@TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039659.json:
```json
{
    "body": "Attachment [trac_5177-delete-cell-dirs.2.patch](tarball://root/attachments/some-uuid/ticket5177/trac_5177-delete-cell-dirs.2.patch) by @TimDumol created at 2010-01-17 22:05:28\n\nTrivial rebase on new patch queue. (Deletion of one empty line)",
    "created_at": "2010-01-17T22:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39659",
    "user": "@TimDumol"
}
```

Attachment [trac_5177-delete-cell-dirs.2.patch](tarball://root/attachments/some-uuid/ticket5177/trac_5177-delete-cell-dirs.2.patch) by @TimDumol created at 2010-01-17 22:05:28

Trivial rebase on new patch queue. (Deletion of one empty line)



---

archive/issue_comments_039660.json:
```json
{
    "body": "This is then new patch queue:\n\n\n```\ntrac_7650-sagenb_doctesting_v6.patch\ntrac_7650-reviewer.patch\ntrac_7648-missing_indent.patch\ntrac_7663-rstrip_prompt.patch\ntrac_7847-empty-trash-no-referer.patch\ntrac_7786-template-jinja-idiomatic.patch\ntrac_7863-declare_vars_aux_js_v2.patch\ntrac_7874-typeset_interact_labels.patch\ntrac_7858-key_binding_vars_v2.patch\ntrac_7666-alphanumeric_cell_ids_B5.patch\ntrac_7666-reviewer.patch\ntrac_7835-preparsing-unicode_v2.patch\ntrac_7249_jinja2_v5.patch\ntrac_2779-sagenb-error-message.patch\n2779_2_banner.patch\ntrac_3154-spurious-u0027-output.patch\ntrac_7969-escaped-backslash.patch\ntrac_7937-sass_manifest.patch\ntrac_4217-html-system-formatting.patch\ntrac_3083-print-documentation.patch\ntrac_7962-link-worksheets-zip-file.patch\ntrac_5177-delete-cell-dirs.patch\n```\n\n\nSorry for the immense queue.",
    "created_at": "2010-01-17T22:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39660",
    "user": "@TimDumol"
}
```

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

archive/issue_comments_039661.json:
```json
{
    "body": "I can't review this, but thank you so much for doing it - it really annoyed me and it's the sort of background thing that in the long run will make Sage so much better even if no one ever sees it.",
    "created_at": "2010-01-18T01:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39661",
    "user": "@kcrisman"
}
```

I can't review this, but thank you so much for doing it - it really annoyed me and it's the sort of background thing that in the long run will make Sage so much better even if no one ever sees it.



---

archive/issue_comments_039662.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-01-19T15:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39662",
    "user": "@qed777"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_039663.json:
```json
{
    "body": "If I evaluate \n\n```python\nprint 'Hello!'\nplot(sin(x))\n```\n\nthen \"Delete All Output,\" \"Save & quit\" and reopen the worksheet, the plot (not the text) reappears.\n\nWe could also delete the cells' files in `Worksheet.delete_all_output`.  But we may wish to do this synchronously; otherwise, a long-running or simply delayed (e.g., on a busy server) thread might remove newly-written files.\n\n(For deleting just one cell, there might be a similar but less likely race condition.  For example, if after deleting a cell (with ID <id>) in the browser, a user pastes and saves ``id=<id>|\\n<updated code>///\\n\\n`` in the \"Edit\" window, and re-evaluates the cell, a delayed `Deferred` could delete new files.)\n\nWhat do most users expect/prefer?\n\nI'm adding `schilly` to the Cc: list, since he's almost certainly better qualified than I on this (and many other) topics.",
    "created_at": "2010-01-19T15:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39663",
    "user": "@qed777"
}
```

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

archive/issue_comments_039664.json:
```json
{
    "body": "Attachment [trac_5177-delete-cell-dirs.3.patch](tarball://root/attachments/some-uuid/ticket5177/trac_5177-delete-cell-dirs.3.patch) by @qed777 created at 2010-01-25 06:58:32\n\nAlso delete files when deleting all output.  Synchronous only.  Replaces previous.",
    "created_at": "2010-01-25T06:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39664",
    "user": "@qed777"
}
```

Attachment [trac_5177-delete-cell-dirs.3.patch](tarball://root/attachments/some-uuid/ticket5177/trac_5177-delete-cell-dirs.3.patch) by @qed777 created at 2010-01-25 06:58:32

Also delete files when deleting all output.  Synchronous only.  Replaces previous.



---

archive/issue_comments_039665.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-01-25T07:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39665",
    "user": "@qed777"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_039666.json:
```json
{
    "body": "V3 deletes the output synchronously (on the server), whether it's for one cell or for the whole worksheet.\n\nI think this is much safer, since it avoids race conditions.  Although deferred deletions could help performance, we already copy a cell's output synchronously.  But with the appropriate locks or other synchronization constructs (e.g., \"marking\" cells for deletion), we could offload some tasks to other threads or to worksheet processes.",
    "created_at": "2010-01-25T07:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39666",
    "user": "@qed777"
}
```

V3 deletes the output synchronously (on the server), whether it's for one cell or for the whole worksheet.

I think this is much safer, since it avoids race conditions.  Although deferred deletions could help performance, we already copy a cell's output synchronously.  But with the appropriate locks or other synchronization constructs (e.g., "marking" cells for deletion), we could offload some tasks to other threads or to worksheet processes.



---

archive/issue_comments_039667.json:
```json
{
    "body": "We should be able to doctest both \"hunks\" on V3.",
    "created_at": "2010-03-07T23:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39667",
    "user": "@qed777"
}
```

We should be able to doctest both "hunks" on V3.



---

archive/issue_comments_039668.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-07T23:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39668",
    "user": "@qed777"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_039669.json:
```json
{
    "body": "Attachment [trac_5177-delete-cell-dirs.4.patch](tarball://root/attachments/some-uuid/ticket5177/trac_5177-delete-cell-dirs.4.patch) by @qed777 created at 2010-03-09 10:21:33\n\nAdd doctects to V3.  Apply only this patch.  sagenb repo.",
    "created_at": "2010-03-09T10:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39669",
    "user": "@qed777"
}
```

Attachment [trac_5177-delete-cell-dirs.4.patch](tarball://root/attachments/some-uuid/ticket5177/trac_5177-delete-cell-dirs.4.patch) by @qed777 created at 2010-03-09 10:21:33

Add doctects to V3.  Apply only this patch.  sagenb repo.



---

archive/issue_comments_039670.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-09T10:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39670",
    "user": "@qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_039671.json:
```json
{
    "body": "Since a major problem with the notebook right now is its performance, and this may slow it down even further, I'm putting this to \"Needs work; requires optimization\".",
    "created_at": "2010-04-18T07:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39671",
    "user": "@TimDumol"
}
```

Since a major problem with the notebook right now is its performance, and this may slow it down even further, I'm putting this to "Needs work; requires optimization".



---

archive/issue_comments_039672.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-18T07:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39672",
    "user": "@TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_039673.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2011-11-30T08:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39673",
    "user": "@jdemeyer"
}
```

Changing priority from major to critical.



---

archive/issue_comments_039674.json:
```json
{
    "body": "Replying to [comment:9 timdumol]:\n> Since a major problem with the notebook right now is its performance, and this may slow it down even further\nHow should this patch slow things down?  The new code is only called when deleting a cell.  In fact, it could even speed up the notebook as there will be fewer files around.",
    "created_at": "2011-11-30T08:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39674",
    "user": "@jdemeyer"
}
```

Replying to [comment:9 timdumol]:
> Since a major problem with the notebook right now is its performance, and this may slow it down even further
How should this patch slow things down?  The new code is only called when deleting a cell.  In fact, it could even speed up the notebook as there will be fewer files around.



---

archive/issue_comments_039675.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-11-30T08:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39675",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_039676.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-11-30T09:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39676",
    "user": "@jasongrout"
}
```

Resolution: fixed



---

archive/issue_comments_039677.json:
```json
{
    "body": "Looks good to me.  I applied a modified version to the flask notebook in this commit: http://code.google.com/r/jasongrout-flask-sagenb/source/detail?r=01b77dc4c1934eb0b54a16e19037f3d89f312482",
    "created_at": "2011-11-30T09:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39677",
    "user": "@jasongrout"
}
```

Looks good to me.  I applied a modified version to the flask notebook in this commit: http://code.google.com/r/jasongrout-flask-sagenb/source/detail?r=01b77dc4c1934eb0b54a16e19037f3d89f312482



---

archive/issue_comments_039678.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-11-30T09:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39678",
    "user": "@jasongrout"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_039679.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-11-30T09:29:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39679",
    "user": "@jasongrout"
}
```

Changing status from closed to new.



---

archive/issue_comments_039680.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-30T09:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39680",
    "user": "@jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_039681.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-30T09:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39681",
    "user": "@jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_039682.json:
```json
{
    "body": "I'm not sure if I should have closed this.  I'll leave it as positive review for now, since I suppose it could also be applied to the current notebook.  The code looks fine to apply to the current notebook, but I don't know if it will apply cleanly, etc.",
    "created_at": "2011-11-30T09:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39682",
    "user": "@jasongrout"
}
```

I'm not sure if I should have closed this.  I'll leave it as positive review for now, since I suppose it could also be applied to the current notebook.  The code looks fine to apply to the current notebook, but I don't know if it will apply cleanly, etc.



---

archive/issue_comments_039683.json:
```json
{
    "body": "Replying to [comment:15 jason]:\n> I'm not sure if I should have closed this.\nOnly the release manager should ever close tickets (with the exception of spam tickets or tickets which have no interesting content at all).\n\n> I'll leave it as positive review for now, since I suppose it could also be applied to the current notebook.\nYes, I will merge it.\n\nThis reminds me of the fact that we should really discuss how to merge the new notebook, and coordination between the current notebook and the new notebook.  It's a topic which I started several times, but still I don't have a good answer.",
    "created_at": "2011-11-30T09:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39683",
    "user": "@jdemeyer"
}
```

Replying to [comment:15 jason]:
> I'm not sure if I should have closed this.
Only the release manager should ever close tickets (with the exception of spam tickets or tickets which have no interesting content at all).

> I'll leave it as positive review for now, since I suppose it could also be applied to the current notebook.
Yes, I will merge it.

This reminds me of the fact that we should really discuss how to merge the new notebook, and coordination between the current notebook and the new notebook.  It's a topic which I started several times, but still I don't have a good answer.



---

archive/issue_comments_039684.json:
```json
{
    "body": "Is this issue somehow related to #10234 by any chance?",
    "created_at": "2011-11-30T18:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39684",
    "user": "@novoselt"
}
```

Is this issue somehow related to #10234 by any chance?



---

archive/issue_comments_039685.json:
```json
{
    "body": "I fixed #10234 a while ago in the flask notebook.  This patch is related; I rebased this patch around the (small) changes I made to fix #10234.",
    "created_at": "2011-11-30T19:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39685",
    "user": "@jasongrout"
}
```

I fixed #10234 a while ago in the flask notebook.  This patch is related; I rebased this patch around the (small) changes I made to fix #10234.



---

archive/issue_comments_039686.json:
```json
{
    "body": "Replying to [comment:19 jason]:\n> I fixed #10234 a while ago in the flask notebook.  This patch is related\nIn which sense \"related\".  Does this ticket also fix #10234?  If you fixed #10234 already, it would be good also to merge #10234 in the current sagenb.",
    "created_at": "2011-11-30T20:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39686",
    "user": "@jdemeyer"
}
```

Replying to [comment:19 jason]:
> I fixed #10234 a while ago in the flask notebook.  This patch is related
In which sense "related".  Does this ticket also fix #10234?  If you fixed #10234 already, it would be good also to merge #10234 in the current sagenb.



---

archive/issue_comments_039687.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-11-30T20:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5177",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5177#issuecomment-39687",
    "user": "@jdemeyer"
}
```

Resolution: fixed
