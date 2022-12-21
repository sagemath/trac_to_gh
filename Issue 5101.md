# Issue 5101: [with patch, needs review] more types for sage_input: vectors, matrices, etc.

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-01-25 20:32:52

Assignee: cwitty

CC:  jason

I'm attaching a patch to increase sage_input support.  Newly supported are floats, elements of RDF and CC, vectors, and matrices (sparse and dense).  I also added some new features to sage_input for handling these new types, and fixed a bug in matrix_modn_sparse that was exposed in the process (sorry, the bug fix really should have been a separate patch).

This patch depends on #2898 (and hence indirectly on #3938).


---

Attachment

I've looked over the patch and it looks reasonable.  Doctests pass on 3.3alpha3 for all (nontrivially) touched files.  Positive review.

This does depend on someone reviewing 2898, though.


---

Comment by mabshoff created at 2009-02-08 02:29:09

This fix depends on #2898 getting a positive review and getting merged.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 09:05:19

Merged in Sage 3.3.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 09:05:19

Resolution: fixed
