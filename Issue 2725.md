# Issue 2725: [with patch, needs review] MPolynomial_polydict doc-tests and some refactoring

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-03-29 19:54:16

Assignee: malb

The attached patch adds a number of features and refactorings:

 1. A new degrees method which returns the degrees of all the variables in one swoop (and has other useful purposes)

 2. More doc-tests

 3. ETuple helper function to eliminate fragile duplicate code

 4. Fix some latex/repr bugs with -1 (continuation of #291)



---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-03-29 20:09:04

Looks good to me. I attached a new version of the patch which plays well with the changes in #2702.  Apply that first, and then apply 2725.patch.


---

Comment by mabshoff created at 2008-03-29 22:15:05

Doctests pass with my current 2.11.rc0 merged tree, so I will merge this.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-29 22:15:30

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 22:15:30

Merged in Sage 2.11.rc0
