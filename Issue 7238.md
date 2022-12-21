# Issue 7238: sagenb notebook: insert new cell *above* text cell

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-18 06:31:05

Assignee: boothby

This is a longstanding annoying GUI issue with the notebook.


---

Attachment

part 1


---

Comment by was created at 2009-10-18 09:22:42

first patch works but there is an issue: 
NOTE: there is still one issue, namely that if you insert a new cell above a text cell,
then delete it, the cursor jumps to the end of the worksheet.  If you refresh before
deleting then everything is fine.


---

Attachment

this fixes moving between cells


---

Comment by was created at 2009-10-19 17:35:49

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-10-19 18:40:46

Patch works as advertised. Positive review.


---

Comment by timdumol created at 2009-10-19 18:40:46

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2009-10-20 01:36:35

I think there are a few problems with the patch set:

 * [Expected] doctest failures in `cell.py`.
 * Adding a new text cell at the end of a worksheet does not update the `cell_id_list`.
 * In Firebug's console, there are two errors:
   * `get_cell(id) is null` in `resize_all_cells()` for text cells.
   * `cell_prev is null` in `join_cell()` when the top cell is a text cell.

I'm working on part 3.


---

Comment by mpatel created at 2009-10-20 06:45:50

Also:  Evaluating all cells, deleting all output, slide mode.

A potential annoyance:  Reopening (or editing) a worksheet fuses consecutive text cells.
Should we have "special" delimiters for text cells?


---

Comment by mpatel created at 2009-10-20 06:48:25

Part 3.  Various small fixes.  Apply on top of other patches.


---

Attachment

> A potential annoyance: Reopening (or editing) a worksheet fuses consecutive 
> text cells. Should we have "special" delimiters for text cells? 

This has been the case since there first were text cells.  Some people consider it good (a feature), and others find it confusing.


---

Comment by was created at 2009-10-20 23:18:37

Tim Dumol gave this a positive review, then Mitesh Patel found some issues and I read his code and was happy with all those fixes and verified that they fixed the new issues.  So I think it is reasonable to give this a positive review.  It is also now merged in sagenb.


---

Comment by was created at 2009-10-20 23:18:37

Resolution: fixed
