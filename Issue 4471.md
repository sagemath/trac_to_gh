# Issue 4471: name worksheet when creating a new worksheet

Issue created by migration from Trac.

Original creator: mrubinst

Original creation time: 2008-11-08 21:36:12

Assignee: boothby

It would be better, I think, to have the worksheet named when it is created. Right now it is given the name 'untitled' and one needs to click on the title or select 'rename' from the menu. This ends up in a lot of worksheets being left named 'untitled'.

So please change so that the user is given a naming window when creating a new worksheet which can default to 'untitled' if the user doesn't enter a name.

William agrees that this would be a good idea.


---

Comment by mabshoff created at 2008-11-09 00:22:07

Better luck in 3.2.1+

Cheers,

Michael


---

Comment by jason created at 2008-11-09 02:34:15

+1.  It's crazy how many "Untitled" worksheets I have.


---

Comment by TimothyClemans created at 2008-12-06 05:53:17

Just found the following in notebook.Notebook.html


```
# Uncomment this to force rename when the worksheet is opened (annoying!)
#if W and W.name() == "Untitled":
#    head += '<script  type="text/javascript">setTimeout("rename_worksheet()",1)</script>'
```



---

Attachment


---

Comment by TimothyClemans created at 2008-12-08 17:23:09

With this ticket you're forced to rename any worksheet with the title "Untitled". You should only have to rename new worksheets.


---

Comment by mpatel created at 2009-11-01 01:33:59

Hasn't some other ticket (or this one) already been merged to fix this?


---

Comment by was created at 2009-11-03 21:03:14

This is now fixed.


---

Comment by was created at 2009-11-03 21:03:14

Resolution: fixed
