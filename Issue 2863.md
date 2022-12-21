# Issue 2863: Integer() does not specify that numbers beginning with 0 and 0x are treated specially

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2008-04-09 08:45:49

Assignee: somebody

Keywords: integer octal hexadecimal

The Integer() function interprets numbers and strings beginning with 0 (respectively, 0x) as octal (respectively hexadecimal) numbers. The docstring does not reflect this. Attached patch fixes this.


---

Attachment


---

Comment by mabshoff created at 2008-04-09 08:52:12

Merged in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-09 08:52:12

Resolution: fixed
