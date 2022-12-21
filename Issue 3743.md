# Issue 3743: notebook -- allow admin user to view any worksheet

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-07-29 18:09:08

Assignee: boothby

User "admin" will be able to go to hostname/users and click on any listed user and have complete access to that user's worksheets.


---

Attachment


---

Comment by was created at 2008-07-29 21:49:01

REFEREE REPORT:

You determine whether a user is an admin with

```
           if self.username == 'admin' 
```

It would be better to determine whether a user is an admin by using the account_type() method of users.  This is because a user with a username other than 'admin' can still be an admin; with the code you've written you would introduce a bug since suddenly certain admin-like things wouldn't work for such a user, but they should.


---

Comment by TimothyClemans created at 2008-07-30 03:57:58

I started out using user_type but for whatever reason for user admin it was returning 'user' so to get the functionality working at all I used the current work around.


---

Attachment


---

Comment by was created at 2008-08-05 05:44:43

Positive review


---

Comment by mabshoff created at 2008-08-06 01:29:40

Merged both patches in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-06 01:29:40

Resolution: fixed
