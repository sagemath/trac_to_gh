# Issue 5851: [with patch, needs review] Convert 3 more elliptic curves files to ReST and add to reference manual

Issue created by migration from https://trac.sagemath.org/ticket/5851

Original creator: cremona

Original creation time: 2009-04-22 10:41:17

Assignee: was

Keywords: elliptic curve documentation

The patch fully ReST-ifies the files
    * ell_field.py
    * ec_database.py
    * kodaira_symbol.py
in sage/schemes/elliptic_curves, and adds them to the reference manual.

These are all quite short and simple.  The patch is based on 3.4.1.rc4.



---

Attachment


---

Comment by wuthrich created at 2009-04-23 12:08:19

John, at home I manage to produce the correct html output and all tests passed. I am quite certain the patch is ok, but a 50% success rate is maybe too low. So I am going back to see what went wrong in my office.


---

Comment by wuthrich created at 2009-04-23 12:33:31

OK. Now it works on my office installation of sage, too. I can not reproduce the earlier error and hence I can give a positive review.

This issues of this trac, namely to improve the documentation of elliptic curves, continues in trac #5853.


---

Comment by cremona created at 2009-04-23 12:43:33

Good, I'm glad the problems went away!


---

Comment by mabshoff created at 2009-04-24 02:00:59

Resolution: fixed


---

Comment by mabshoff created at 2009-04-24 02:00:59

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael
