# Issue 6815: Restarting worksheet doesn't enable typesetting even when "Typeset" box is checked

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-08-23 22:57:41

Assignee: boothby

CC:  was mpatel

Restarting worksheet seems to disable latex typesetting even though "Typeset" box is checked. If I un-check and then re-check the "Typeset" box, it starts working again.



---

Comment by jhpalmieri created at 2009-08-23 23:32:27

Either I don't understand the problem, or I'm not having it.  What Sage version, browser, and OS?

Here's what I did (Sage 4.1.1 on a Mac (Intel, OS X 10.5) with Safari or Firefox):  I start a worksheet, click the Typeset box, then do some stuff.

Then I can (a) close the worksheet window, (b) click the "Save & quit" button then close it, or (c) quit Sage, leaving the window open.  After doing (a) or (b) and re-opening the worksheet, or doing (c) and running 'sage -notebook', then when I evaluate a cell in the worksheet, latex typesetting is still active.


---

Comment by gmhossain created at 2009-08-23 23:46:51

Replying to [comment:1 jhpalmieri]:
> Either I don't understand the problem, or I'm not having it.  What Sage version, browser, and OS?




I am having this issue with Sage-4.1.1 in Ubuntu 9.04 (Thinkpad x61-tablet) with both 
Firefox/Google Chrome. I guess, you might see this issue if you restart the worksheet 
(Action-->Restart Worksheet).


---

Comment by timdumol created at 2009-10-25 19:37:26

I cannot reproduce this issue in Sage-4.1.2 using sagenb-0.4. Can someone please confirm, and if so, close this ticket?


---

Comment by jhpalmieri created at 2009-12-22 00:10:22

I don't see this any more, either.  Can we close it?


---

Comment by was created at 2009-12-22 17:04:13

Resolution: fixed
