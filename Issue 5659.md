# Issue 5659: [with patch, needs review] Use CRT to speed up solve_mod

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-04-01 15:41:31

Assignee: whuss

The attached patch uses the Chinese Remainder Theorem to speed up 
solve_mod if the modulus can be factorized into small numbers.

It also adds the option solution_dict for consistency with solve.


---

Attachment


---

Comment by mabshoff created at 2009-04-13 02:16:31

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 02:16:31

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
