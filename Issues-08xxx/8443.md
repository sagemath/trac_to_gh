# Issue 8443: Active cell jumps to end of worksheet when evaluating a cell

archive/issues_008443.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @dandrake mhampton\n\nThe problem seems to be duplicate cell IDs.  The function `Worksheet.edit_save` parses a worksheet's text into a list of cells.  If the worksheet ends with a text cell, the function appends a compute cell.  But the existing code does not update the cell counter, which is the ID of the next new cell, **before** it appends the cell.  The appended cell's ID could match an existing ID.  If two cells have the same ID, the browser can jump to the second one, at the end of the worksheet, after you evaluate the predecessor of the first.\n\nSee [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/f28cd98f3623316c).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8443\n\n",
    "closed_at": "2010-03-09T04:59:10Z",
    "created_at": "2010-03-05T12:02:34Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Active cell jumps to end of worksheet when evaluating a cell",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8443",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @dandrake mhampton

The problem seems to be duplicate cell IDs.  The function `Worksheet.edit_save` parses a worksheet's text into a list of cells.  If the worksheet ends with a text cell, the function appends a compute cell.  But the existing code does not update the cell counter, which is the ID of the next new cell, **before** it appends the cell.  The appended cell's ID could match an existing ID.  If two cells have the same ID, the browser can jump to the second one, at the end of the worksheet, after you evaluate the predecessor of the first.

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/f28cd98f3623316c).

Issue created by migration from https://trac.sagemath.org/ticket/8443





---

archive/issue_comments_075775.json:
```json
{
    "body": "Attachment [trac_8443-cell_focus_jump.patch](tarball://root/attachments/some-uuid/ticket8443/trac_8443-cell_focus_jump.patch) by @qed777 created at 2010-03-05 12:06:51\n\nAvoid possible duplicate cell IDs during an `edit_save` operation.  sagenb repo.",
    "created_at": "2010-03-05T12:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75775",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8443-cell_focus_jump.patch](tarball://root/attachments/some-uuid/ticket8443/trac_8443-cell_focus_jump.patch) by @qed777 created at 2010-03-05 12:06:51

Avoid possible duplicate cell IDs during an `edit_save` operation.  sagenb repo.



---

archive/issue_comments_075776.json:
```json
{
    "body": "Note: Evaluating the last compute cell in a worksheet whose last cell is a *text cell* does not result in a new compute cell appended to the end of the sheet.  This is a separate problem that I fixed at #7908, which I'm planning to rebase soon.",
    "created_at": "2010-03-05T12:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75776",
    "user": "https://github.com/qed777"
}
```

Note: Evaluating the last compute cell in a worksheet whose last cell is a *text cell* does not result in a new compute cell appended to the end of the sheet.  This is a separate problem that I fixed at #7908, which I'm planning to rebase soon.



---

archive/issue_comments_075777.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-05T12:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75777",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075778.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-06T08:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75778",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075779.json:
```json
{
    "body": "This patch looks good. It fixes the problem for me with the worksheet I attached in that sage-notebook thread. I think it could use a doctest, though. Here's my idea:\n\n```\nsage: nb = sagenb.notebook.notebook.Notebook(tmp_dir()+'.sagenb')\nsage: nb.add_user('sage','sage','sage@sagemath.org',force=True)\nsage: W = nb.create_new_worksheet('Test trac #8443', 'sage')\nsage: W.edit_save(\"`\\n1+1\\n///\\n`\\n\\n<p>a text cell</p>\")\nsage: len(set(W.cell_id_list())) == 3\nTrue\n```\n\nThe idea is that if a duplicate cell id gets added, making a set out of the id list will be shorter than the plain id list. Does this seem like a reasonable test that will prevent a regression on this issue?",
    "created_at": "2010-03-06T08:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75779",
    "user": "https://github.com/dandrake"
}
```

This patch looks good. It fixes the problem for me with the worksheet I attached in that sage-notebook thread. I think it could use a doctest, though. Here's my idea:

```
sage: nb = sagenb.notebook.notebook.Notebook(tmp_dir()+'.sagenb')
sage: nb.add_user('sage','sage','sage@sagemath.org',force=True)
sage: W = nb.create_new_worksheet('Test trac #8443', 'sage')
sage: W.edit_save("`\n1+1\n///\n`\n\n<p>a text cell</p>")
sage: len(set(W.cell_id_list())) == 3
True
```

The idea is that if a duplicate cell id gets added, making a set out of the id list will be shorter than the plain id list. Does this seem like a reasonable test that will prevent a regression on this issue?



---

archive/issue_comments_075780.json:
```json
{
    "body": "Yes, definitely.  I should have written a test.  I've tweaked your example a bit, since it also passes without the patch.  Please see V2.\n\n**Without** the patch, I get\n\n```python\nsage: nb = sagenb.notebook.notebook.Notebook(tmp_dir() + '.sagenb')\nsage: nb.add_user('sage', 'sage', 'sage@sagemath.org', force=True)\nsage: W = nb.create_new_worksheet('Test trac #8443', 'sage')\nsage: W.edit_save('`\\n1+1\\n///\\n`')\nsage: W.cell_id_list()\n[0]\nsage: W.next_id()\n1\nsage: W.edit_save(\"`\\n1+1\\n///\\n`\\n\\n<p>a text cell</p>\")\nsage: len(set(W.cell_id_list())) == 3    # oops!\nFalse\nsage: W.cell_id_list()                   # oops!\n[0, 1, 1]\nsage: W.next_id()                        # oops!\n2\n```\nAs far as it goes, my review of the test is positive.",
    "created_at": "2010-03-06T13:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75780",
    "user": "https://github.com/qed777"
}
```

Yes, definitely.  I should have written a test.  I've tweaked your example a bit, since it also passes without the patch.  Please see V2.

**Without** the patch, I get

```python
sage: nb = sagenb.notebook.notebook.Notebook(tmp_dir() + '.sagenb')
sage: nb.add_user('sage', 'sage', 'sage@sagemath.org', force=True)
sage: W = nb.create_new_worksheet('Test trac #8443', 'sage')
sage: W.edit_save('`\n1+1\n///\n`')
sage: W.cell_id_list()
[0]
sage: W.next_id()
1
sage: W.edit_save("`\n1+1\n///\n`\n\n<p>a text cell</p>")
sage: len(set(W.cell_id_list())) == 3    # oops!
False
sage: W.cell_id_list()                   # oops!
[0, 1, 1]
sage: W.next_id()                        # oops!
2
```
As far as it goes, my review of the test is positive.



---

archive/issue_comments_075781.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-06T13:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75781",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075782.json:
```json
{
    "body": "Attachment [trac_8443-cell_focus_jump.2.patch](tarball://root/attachments/some-uuid/ticket8443/trac_8443-cell_focus_jump.2.patch) by @qed777 created at 2010-03-06 13:37:51\n\nAdded doctest.  Apply only this patch.",
    "created_at": "2010-03-06T13:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75782",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8443-cell_focus_jump.2.patch](tarball://root/attachments/some-uuid/ticket8443/trac_8443-cell_focus_jump.2.patch) by @qed777 created at 2010-03-06 13:37:51

Added doctest.  Apply only this patch.



---

archive/issue_comments_075783.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-07T05:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75783",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075784.json:
```json
{
    "body": "Your doctest fails without the patch, and succeeds with it. It has some nice ReST formatting. The patch fixes the problem. Positive review here!",
    "created_at": "2010-03-07T05:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75784",
    "user": "https://github.com/dandrake"
}
```

Your doctest fails without the patch, and succeeds with it. It has some nice ReST formatting. The patch fixes the problem. Positive review here!



---

archive/issue_comments_075785.json:
```json
{
    "body": "Release manager: apply only attachment:trac_8443-cell_focus_jump.2.patch to sagenb repo.",
    "created_at": "2010-03-07T07:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75785",
    "user": "https://github.com/dandrake"
}
```

Release manager: apply only attachment:trac_8443-cell_focus_jump.2.patch to sagenb repo.



---

archive/issue_comments_075786.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-09T04:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8443#issuecomment-75786",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_020251.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-03-09T04:59:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8443",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8443#event-20251"
}
```
