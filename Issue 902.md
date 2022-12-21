# Issue 902: implement computation of minpoly of symbolics

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-15 16:54:15

Assignee: robertwb

Do this by numerical approximation, algdep, checking equality.

NOTE: Robert Bradshaw has already done this!! I haven't seen any code, etc.


---

Attachment

The above patch implements this. 

I also added a bit of code to the ring __getitem__ method so constructions like ZZ[sqrt(2)] and QQ[I] work. I have not yet run "sage -testall"to make sure that it doesn't ruin any doctests elsewhere, but it should be good. It is also unclear how to handle names in this case, so the code there just names generators a, b, c, ... except for a couple of special cases.


---

Comment by was created at 2007-10-19 02:29:45

Resolution: fixed
