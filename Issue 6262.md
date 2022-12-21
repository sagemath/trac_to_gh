# Issue 6262: notebook takes 5-10 minutes to quit

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-06-11 19:34:49

Assignee: boothby

CC:  was

Even with no worksheets active, with sage-4.0.1 the server takes a long time to quit after pressing ctrl-C.  This did not use to be the case, and is extremely annoying.  It consistently happens to me on an OS 10.5 intel mac.  


---

Comment by boothby created at 2009-06-11 21:20:56

You're definitely what I'd consider a "power user".  How many worksheets do you have?  Can you move your .sage directory temporarily, and then see if you get the same behavior?


---

Comment by mhampton created at 2009-06-12 02:26:36

That directory had 250 worksheets for admin, the only user account.  I used a new directory, and everything was very snappy.   So you are right, it must be related to the number of worksheets.  I still think its a bug - if there are no active worksheets it shouldn't take 10 minutes to save the notebook.


---

Comment by boothby created at 2009-06-16 20:00:42

Agreed, that is a ridiculous amount of time for the notebook to quit -- but this pinpoints the problem.  (also, I can easily reproduce it now)


---

Comment by mpatel created at 2010-01-25 16:46:16

How bad is the problem in Sage 4.3.1?


---

Comment by mhampton created at 2010-01-25 19:03:15

I can't say exactly because after having this problem I changed the way I set up my servers to avoid having tons of worksheets and users.  Since then, I have not had a problem but I'm not sure that means the problem went away.  I am guessing that things have gotten better though since I have not had a hint of a problem recently.  I am OK with closing this ticket as invalid/fixed.


---

Comment by mpatel created at 2010-01-25 19:33:51

William -- Is this a problem with `sagenb.org`?


---

Comment by mpatel created at 2010-01-27 01:57:18

Resolution: invalid


---

Comment by mpatel created at 2010-01-27 01:57:18

For now, at least, I'm closing this ticket as invalid.  Feel free to reopen it!
