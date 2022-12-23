# Issue 4960: issue with user account creation in the notebook

Issue created by migration from https://trac.sagemath.org/ticket/4960

Original creator: was

Original creation time: 2009-01-09 22:50:11

Assignee: boothby

CC:  was mhansen


```
Hello,

I'm running my server with account creation disabled and when I want
to add a user I restart it briefly with notebook(...,accounts=true)

Stage 1:
I through the "create a new account" procedure without trying the
newly created user then immediately restarts the server with accounts
disabled (as I don't want to run too much with account creation open)
I try to log in -> the user "doesn't exist".

Stage 2:
I restart the server accounts=true, create the user and log in a first
time with the newly created account, then logout and restart the
server with accounts creation disabled.
Same error, user doesn't exist anymore.

Stage 3:
- Create account
- Log in with it
- Create a new (first) worksheet
- Logout
- Restart the server
- Alleluia the user finally exists and can log in.

Apparently existence of the user seems to be linked to the existence
of a first sheet or at least the user directory under .sage/
sage_notebook/worksheets/

I would rather expect stage1 to be enough to create a new account,
maybe creating the user directory during what is supposed to be the
initial user creation would be enough?

Phil
```



---

Comment by timdumol created at 2010-01-17 09:05:58

I cannot replicate this issue anymore. Can someone confirm and close?


---

Comment by was created at 2010-01-17 11:26:47

Resolution: fixed


---

Comment by was created at 2010-01-17 11:26:47

Probably our rewrite fixed this...
