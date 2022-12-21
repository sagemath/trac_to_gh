# Issue 6368: shift-tab in the notebook should go back 4 spaces instead of going to the previous input cell

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-20 15:27:19

Assignee: boothby

CC:  timdumol

Right now, in the notebook, usually shift-tab goes back to the previous input cell.  Since tab goes forward 4 spaces (or if text is highlighted, indents it), and shift-tab unindents highlighted text, it would by far make the most sense if shift-tab when no text is highlighted just goes back 4 spaces.


---

Comment by acleone created at 2010-01-20 02:52:15

Changing status from new to needs_review.


---

Attachment

Should I add any Selenium tests?


---

Comment by mpatel created at 2010-01-20 05:29:13

Nice work!

 * This works as expected in Cr4, FF3.5.7, & S4 on Windows XP and Cr4 & FF3.5.6 on Linux.
 * In O10 on XP and Linux, shift-tab for non-empty selections was already broken and is still broken.
 * In IE8 on XP, auto-indentation and tab/shift-tab were already broken and they still are.

We can make new tickets for the latter two.  It seems that a given browser behaves more consistently across platforms than different browsers on a given platform, but it would be great to get feedback on various browsers on Mac OS.  Usually, we test what we can, e.g., the locally available combinations, ourselves and receive more varied data from the field (alphas, rcs, and releases).

On the Se tests:  Please feel free to try!  In my experience, Se does not handle at least some keys (e.g., TAB) consistently across browsers.  So far, we've tested mostly in Firefox.  It's relatively easy to set up Se Grid to test other browsers.  But I've found getting the Se tests to pass in more than one browser is a tedious affair.  Moreover, the results are very sensitive to seemingly innocuous changes in HTML, etc.  Nevertheless, we should refine and extend our suite to cover more notebook functions.


---

Comment by mpatel created at 2010-01-20 05:29:13

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-25 01:17:47

Resolution: fixed
