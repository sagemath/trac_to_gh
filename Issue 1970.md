# Issue 1970: [with tiny patch; needs easy review] notebook -- gnutls should not be needed if you're running the notebook insecurely, so don't require it

Issue created by migration from https://trac.sagemath.org/ticket/1970

Original creator: was

Original creation time: 2008-01-29 11:56:32

Assignee: boothby




---

Attachment


---

Comment by malb created at 2008-01-29 16:08:10

updated patch use this instead


---

Attachment

I've uploaded a new patch which replaces the old patch. This version checks for an OSError rather than any exception. It is better to check for a specific error only because this way we can spot errors and fix them. I've applied this patch against rc2 but the insecure notebook worked for me before and after the patch (I have GnuTLS installed system wide)


---

Comment by mabshoff created at 2008-01-29 16:19:33

Resolution: fixed


---

Comment by mabshoff created at 2008-01-29 16:19:33

Merged trac-1970-notebook-gnutls.2.patch in Sage 2.10.1.rc3
