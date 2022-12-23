# Issue 3223: notebook -- it is now broken on the iphone

Issue created by migration from https://trac.sagemath.org/ticket/3223

Original creator: was

Original creation time: 2008-05-16 18:45:37

Assignee: boothby

Now I think left or right parenthesis sends carriage return.  I think this likely has something to do with updating the keyboard support for the new safari browser.  


---

Attachment


---

Comment by was created at 2008-11-17 15:47:40

I fixed this by disabling *all* keyboard shortcut handling on the iphone.  This is a good idea, since the iphone does not have any of the keys needed to send any of the keyboard shortcuts, and it gets around the problem.  

To referee this 3-line patch, just verify that clearly I didn't break anything, since all I did was add a special case to check for the iphone string in the browser UA tag, and only then disable keyboard shortcut handling.


---

Comment by was created at 2008-11-17 15:49:22

I'm moving this back to 3.2.  It's harmless (famous last words), and I really think having iphone support working again is an extremely important bug fix.


---

Comment by boothby created at 2008-11-17 20:23:36

+1


---

Comment by was created at 2008-11-18 06:49:33

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-18 18:13:04

Merged in Sage 3.2.rc2


---

Comment by mabshoff created at 2008-11-18 18:13:04

Resolution: fixed
