# Issue 2306: Tab completion in the command-line mode

Issue created by migration from https://trac.sagemath.org/ticket/2306

Original creator: ljpk

Original creation time: 2008-02-25 23:33:46

Assignee: was

When I use tab-complete in the command-line interface when typing an object name, the cursor moves to one space after the end of the name. This is unwanted behaviour, because this means that one cannot then type "." and tab-complete again to get the list of functions associated to the object.


---

Comment by jason created at 2008-02-25 23:44:52

tab completion works correctly for me (Ubuntu 7.10, 32-bit), i.e., no space after pressing tab.


---

Comment by ljpk created at 2008-02-25 23:49:15

OK, so I should clarify that this is for the Windows-via-VMware version 2.10.1 (as just downloaded this evening).


---

Comment by was created at 2008-02-26 00:00:28

Are you typing directly into the vmware machine, or did you ssh into it via putty or something?


---

Comment by was created at 2008-02-26 00:01:35

It works fine for me on the vmware image (run from OS X) directly typing into vmware.


---

Comment by ljpk created at 2008-02-26 09:11:51

This is directly typing in to the vmware machine.


---

Comment by jason created at 2008-03-08 20:27:41

In 2.9.3, tab completion did not put a space after the command (Ubuntu 7.10, 32-bit).

However I am seeing this problem in 2.10.2, which, as the original poster mentioned, is annoying and slightly frustrating.


---

Comment by gfurnish created at 2008-07-14 10:23:30

Is this still an issue?


---

Comment by jason created at 2008-07-14 14:27:48

Yes.  I am seeing this on a home-compiled Sage 3.0.4 on Ubuntu 8.04.


---

Comment by jason created at 2008-07-14 14:31:59

For background and how to make a solution, see:

http://groups.google.com/group/sage-support/browse_thread/thread/b96905d2a648ad7b/e8586abd04da4cc5?lnk=gst&q=tab+completion+space#e8586abd04da4cc5


---

Comment by jason created at 2008-08-21 23:10:15

#2469 is another ticket for this issue.


---

Comment by mabshoff created at 2008-09-28 00:09:51

Resolution: duplicate


---

Comment by mabshoff created at 2008-09-28 00:09:51

Closed as a dupe of #2469 since that ticket has the better explanation.

Cheers,

Michael
