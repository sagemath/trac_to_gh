# Issue 2605: Notebook tab-backspace-(shift enter) gives bug

Issue created by migration from https://trac.sagemath.org/ticket/2605

Original creator: jvoight

Original creation time: 2008-03-19 20:39:28

Assignee: boothby

In an empty cell, type
  tab, backspace, and shift-enter
and it gives a strange bug: Missing output for cell ...  

Reported by Andrew Guertin, an undergraduate in my Math 252 class.

JV


---

Comment by was created at 2008-03-19 20:45:36

I cannot replicate this.  If I do the above the cell is deleted and loses focus, which is exactly the desired behavior. 

SO -- took keep this from being marked invalid, please list the exact operating system, browser, sage version, etc., and that *you* can replicate the problem (not just your student).


---

Comment by jvoight created at 2008-03-19 20:53:31

I also replicated the bug.  I'm running Sage version 2.10.3 (on a separate Linux machine); the notebook is running under Windows XP with Firefox version:

Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11

JV


---

Comment by was created at 2008-05-10 21:22:53

Resolution: fixed


---

Comment by was created at 2008-05-10 21:22:53

I cannot replicate this on any system.  I believe it is no longer a bug.
