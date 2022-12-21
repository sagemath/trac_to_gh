# Issue 6871: temporary passwords aren't temporary

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2009-09-03 03:19:25

Assignee: boothby

As described in comment:27:ticket:4135, when #4135 is applied, the "temporary" password you get when resetting a user's password isn't temporary -- you can log in, log out, and then log in again with it.

Also, the page that tells you the new password has a title of "Error" even though no error has occurred.


---

Comment by startakovsky created at 2012-10-19 07:25:10

This comment may be gratuitous, but the issue I'm having with the notebook running on Sage 5.3 is:

1) I create a new user.

2) I let the user know their temporary password.

3) They log in successfully with their temporary password.

4) They change their password.

5) After automatic logout, neither password works, not the temporary nor the newly created password.  Screen reads "wrong password".

The weird thing is, when I do this with a longer than 4 letter name I don't get this problem...


---

Comment by kcrisman created at 2014-12-10 19:30:53

The 'error' message is long since gone.

I cannot replicate the issue in comment:1, though it is certainly not gratuitous.  Partly that is because we now say
> The username must start with a letter and be between 4 and 32 characters long.

So the only remaining issue is, of course, the one actually mentioned.  The question is whether this is a problem...


---

Comment by kcrisman created at 2014-12-10 19:31:59

https://github.com/sagemath/sagenb/issues/294


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets
