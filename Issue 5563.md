# Issue 5563: [with patch, needs review] Doctest failure in devel/sage/doc/en/bordeaux_2008/modular_....rst

Issue created by migration from https://trac.sagemath.org/ticket/5563

Original creator: GeorgSWeber

Original creation time: 2009-03-18 23:37:35

Assignee: mabshoff

modular_forms_and_hecke_operators.rst
contains a call to sloane_find() which requires internet access, leading to a failure if you don't


---

Attachment

patch against Sage 3.4


---

Comment by GeorgSWeber created at 2009-03-18 23:40:00

The issue had been reported originally by Minh Nguyen in the thread

http://groups.google.com/group/sage-devel/browse_thread/thread/ce81352fe52292bd/a199ed5de16c81a8#a199ed5de16c81a8


---

Comment by mvngu created at 2009-03-19 04:07:38

REFEREE REPORT



The patch *sloane_find_optional.patch* applies OK against Sage 3.4. All tests passed, both on machines with and without Internet connection. Just to be on the safe side, I rebuilt the HTML version of the whole reference manual; rebuilding went fine as expected on machines with and without Internet connection. Positive review.


---

Comment by mabshoff created at 2009-03-23 18:39:54

Resolution: fixed


---

Comment by mabshoff created at 2009-03-23 18:39:54

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
