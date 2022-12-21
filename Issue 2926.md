# Issue 2926: Minilistic change password page for notebook user

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-04-15 03:46:38

Assignee: TimothyClemans

** Write resource "passwd" with inspiration from RegistrationPage
 * Add resource "passwd" to UserTopLevel
 * Add link to "change password" in the list entries in the function _html_body in notebook.py


---

Attachment


---

Comment by mabshoff created at 2008-04-16 01:16:57

This might be superseded by #2936, but if the functionality is not in there it can probably ported to the new codebase.

Cheers,

Michael


---

Comment by was created at 2008-05-11 08:49:12

This just works.  There's no way for a user to actually use it short of explicitly typing
/passwd in the URL.  But it does work correctly and the underlying code looks good.

I wish it were somehow tested, but I don't know how to test it (yet).

So it's a preliminary and solid step to this functionality, so it should go in.  

I don't think it overlaps with #2936 which is more backend stuff, whereas this is more UI oriented.


---

Comment by mabshoff created at 2008-05-11 10:47:42

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-11 10:47:42

Resolution: fixed
