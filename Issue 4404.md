# Issue 4404: notebook -- split "Download to a file" into two menu options, one without revision history

Issue created by migration from https://trac.sagemath.org/ticket/4404

Original creator: was

Original creation time: 2008-10-30 18:36:03

Assignee: boothby

CC:  burcin kcrisman was mhansen

As requested by Stan Flavia on sage-support, replace the single "Download to a file" menu option in the notebook by two options:
   * Download to a file
   * Download to a file w/ history

The first would download a version of the file without the revision history.  The second would do what the current "Download to a file" command does.


---

Comment by kcrisman created at 2009-02-24 18:00:52

One should also discuss the possibility of an option to download _just_ the worksheet.txt, for those accessing Sage only via their browser.


---

Comment by timdumol created at 2009-12-06 13:49:27

SageNB no longer exports revision data, so I think this should be closed.


---

Comment by kcrisman created at 2009-12-07 11:55:48

Okay, so maybe the ticket should be reversed in order.  Are you saying that it is impossible to have Sage export revision data at all now, or that it isn't implemented?  I can't find it quickly, but there have been discussions on cases where this could be useful.  And exporting just the txt or whatever file would also still be good, though in the meantime that may be a different ticket.


---

Comment by was created at 2009-12-09 15:45:30

I'm changing the summary to better reflect the issue.


---

Comment by boothby created at 2020-03-29 02:05:01

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:05:01

Resolution: invalid
