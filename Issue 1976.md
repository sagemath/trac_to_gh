# Issue 1976: [with 1-line patch; needs review] disable the use of openssl on linux as a hack to generate security certificates quickly

Issue created by migration from https://trac.sagemath.org/ticket/1976

Original creator: was

Original creation time: 2008-01-30 04:17:23

Assignee: boothby

This needs review and testing on linux with brand new GNUtls package.


---

Attachment


---

Comment by AlexGhitza created at 2008-03-13 12:55:18

I tested this on a Gentoo machine with gnutls-2.0.4 installed.  It works, and it's really fast.


---

Comment by mabshoff created at 2008-03-14 13:46:27

Merged in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-14 13:46:27

Resolution: fixed
