# Issue 6463: Residue fields broken for relative extensions

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-07-04 15:42:22

Assignee: was

Keywords: ideals

The code for residue fields of ideals in number fields is broken for ideals of relative extensions, as it tries to call "norm" on an ideal, which we have chosen to deliberately break for relative ideals.


---

Comment by davidloeffler created at 2009-07-04 15:52:08

patch against 4.1.alpha2


---

Attachment


---

Comment by ncalexan created at 2009-07-14 21:09:13

Fine by me.


---

Comment by mvngu created at 2009-07-16 21:01:12

David, the patch `trac_6463-relative_residue_field.patch` doesn't have your username, so I'm committing it in your name.


---

Comment by mvngu created at 2009-07-16 21:01:12

Resolution: fixed
