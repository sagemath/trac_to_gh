# Issue 3560: optimize import of gnutls_socket_ssl.py

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-06 08:28:29

Assignee: cwitty

make it import gnutls.connection	and gnutls.errors only when needed.



---

Attachment


---

Attachment


---

Attachment

Works for me.

Apply only trac_3560.patch.


---

Comment by mabshoff created at 2008-07-06 09:47:28

Resolution: fixed


---

Comment by mabshoff created at 2008-07-06 09:47:28

Merged in Sage 3.0.4.alpha2
