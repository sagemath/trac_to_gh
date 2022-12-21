# Issue 8443: Active cell jumps to end of worksheet when evaluating a cell

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-03-05 12:02:34

Assignee: was

CC:  ddrake mhampton

The problem seems to be duplicate cell IDs.  The function `Worksheet.edit_save` parses a worksheet's text into a list of cells.  If the worksheet ends with a text cell, the function appends a compute cell.  But the existing code does not update the cell counter, which is the ID of the next new cell, *before* it appends the cell.  The appended cell's ID could match an existing ID.  If two cells have the same ID, the browser can jump to the second one, at the end of the worksheet, after you evaluate the predecessor of the first.

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/f28cd98f3623316c).


---

Attachment

Avoid possible duplicate cell IDs during an `edit_save` operation.  sagenb repo.


---

Comment by mpatel created at 2010-03-05 12:11:10

Note: Evaluating the last compute cell in a worksheet whose last cell is a _text cell_ does not result in a new compute cell appended to the end of the sheet.  This is a separate problem that I fixed at #7908, which I'm planning to rebase soon.


---

Comment by mpatel created at 2010-03-05 12:11:10

Changing status from new to needs_review.


---

Comment by ddrake created at 2010-03-06 08:27:48

Changing status from needs_review to needs_work.


---

Comment by ddrake created at 2010-03-06 08:27:48

This patch looks good. It fixes the problem for me with the worksheet I attached in that sage-notebook thread. I think it could use a doctest, though. Here's my idea:


```
sage: nb = sagenb.notebook.notebook.Notebook(tmp_dir()+'.sagenb')
sage: nb.add_user('sage','sage','sage`@`sagemath.org',force=True)
sage: W = nb.create_new_worksheet('Test trac #8443', 'sage')
sage: W.edit_save("`\n1+1\n///\n`\n\n<p>a text cell</p>")
sage: len(set(W.cell_id_list())) == 3
True
```


The idea is that if a duplicate cell id gets added, making a set out of the id list will be shorter than the plain id list. Does this seem like a reasonable test that will prevent a regression on this issue?


---

Comment by mpatel created at 2010-03-06 13:28:57

Yes, definitely.  I should have written a test.  I've tweaked your example a bit, since it also passes without the patch.  Please see V2.

*Without* the patch, I get

```python
sage: nb = sagenb.notebook.notebook.Notebook(tmp_dir() + '.sagenb')
sage: nb.add_user('sage', 'sage', 'sage`@`sagemath.org', force=True)
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

Comment by mpatel created at 2010-03-06 13:28:57

Changing status from needs_work to needs_review.


---

Attachment

Added doctest.  Apply only this patch.


---

Comment by ddrake created at 2010-03-07 05:31:40

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-03-07 05:31:40

Your doctest fails without the patch, and succeeds with it. It has some nice ReST formatting. The patch fixes the problem. Positive review here!


---

Comment by ddrake created at 2010-03-07 07:27:09

Release manager: apply only attachment:trac_8443-cell_focus_jump.2.patch to sagenb repo.


---

Comment by mpatel created at 2010-03-09 04:59:10

Resolution: fixed
