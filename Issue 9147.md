# Issue 9147: [with patch, needs review] Make sage able to compile/link with --as-needed

Issue created by migration from Trac.

Original creator: cschwan

Original creation time: 2010-06-05 10:15:43

Assignee: tba

With sage-on-gentoo it is possible to compile Sage with custom CFLAGS/LDFLAGS. One common LDFLAG on gentoo is "-Wl,--as-needed" which has some advantages when it comes to upgrading a program's dependencies (see http://www.gentoo.org/proj/en/qa/asneeded.xml for a good explanation).

The following patch is needed to enable Sage to be compiled with --as-needed; even if one does not do so the patch should not hurt.



---

Comment by mhansen created at 2010-06-05 17:37:27

Resolution: invalid


---

Attachment

This is already handled by #8844.
