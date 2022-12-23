# Issue 1905: elliptic curves -- both E.Lseries and E.L_series are defined.  Just define one of them, say E.Lseries. (trivial to fix)

Issue created by migration from https://trac.sagemath.org/ticket/1905

Original creator: was

Original creation time: 2008-01-24 03:09:02

Assignee: was

There is no good reason to have both.  That would be like having KroneckerSymbol and kronecker_symbol. 


---

Attachment


---

Comment by AlexGhitza created at 2008-01-24 09:24:01

See the attached patch for the trivial fix.  The duplicate L_series() appeared only in two files: ell_rational_field.py and padics.py.  Removed it from the first file, and replaced all occurrences in the second file by Lseries().  Also ran sage -t * in schemes/elliptic_curves to make sure nothing got screwed in the process.


---

Comment by was created at 2008-01-24 16:19:01

Looks good to me.  Thanks Alex!


---

Comment by mabshoff created at 2008-01-24 20:45:28

Merged in Sage 2.10.1.alpha2


---

Comment by mabshoff created at 2008-01-24 20:45:28

Resolution: fixed
