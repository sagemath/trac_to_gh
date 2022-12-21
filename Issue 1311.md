# Issue 1311: [graphs] calculate chromatic number

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-28 20:01:15

Assignee: mhansen

Keywords: graphs




---

Comment by rlm created at 2007-12-17 15:14:51

Changing keywords from "graphs" to "".


---

Comment by rlm created at 2007-12-17 15:14:51

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2007-12-17 15:14:51

Changing component from combinatorics to graph theory.


---

Comment by boothby created at 2008-02-23 21:03:42

Patch resolves this and #1313, depends on patch to #2271.


---

Attachment


---

Attachment


---

Comment by boothby created at 2008-02-25 20:19:22

1311_updated.patch implements 1311_ref.patch, and uses the improved DLXMatrix interface found in #2271.


---

Comment by mabshoff created at 2008-02-25 20:49:51

Resolution: fixed


---

Comment by mabshoff created at 2008-02-25 20:49:51

Merged 1311_and_1313_chromatic_functions.patch and 1311_updated.patch in Sage 2.10.3.alpha0
