# Issue 6833: use hg for worksheet history

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-08-27 23:21:32

Assignee: boothby

CC:  kini

Keywords: notebook, mercurial, hg

Sage ships an excellent revision control software but uses a rather simple approach to worksheet version-ing. It would be nice if a hg repository was used behind the scenes. This would enable diffs, cool sharing (just pull my worksheet) and collaboration.


---

Comment by malb created at 2014-06-25 00:56:38

Let's just close this ticket.


---

Comment by aapitzsch created at 2014-08-18 21:59:43

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-08-27 15:37:51

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2014-08-27 15:37:51

https://github.com/sagemath/sagenb/issues/216


---

Comment by kcrisman created at 2014-11-20 14:02:41

Some other ideas from #301:

 * Show history without code lines.
 * Show history without SAGE command line markup
 * Show history by time
 * Show activity graphs by time
 * Show history for worksheets
 * Show history for cell in worksheet
   * Show differences between two edits in a cell

Naturally not all of these would be implemented here, but any that aren't could be moved to another ticket.  Should sagenb, or the universe, last that long.


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets
