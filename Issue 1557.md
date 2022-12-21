# Issue 1557: notebook -- usability improvement after uploading file

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-18 03:27:01

Assignee: boothby


```
> Just out of curiosity should "Use" be replaced by a different name,
> or should their be a big "Back to Worksheet" button on the page
> after you upload the file?

I like the idea of replacing "Use" with something like "GUI" and also
placing a "Back to Worksheet" button on the page after a file has been
uploaded.
```


I don't like "GUI" since the whole thing is a GUI.  However, "Worksheet"
might be much better.   

William


---

Comment by tkosan created at 2007-12-20 06:33:58

Worksheet instead of GUI would be fine.

Another suggestion is to move the jsMath button from the bottom left corner of the window to the bottom right corner.  In its current position, it covers the part of the lowest cell that typing begins at.

Ted


---

Comment by was created at 2008-05-10 21:11:24

I moved Ted's comment to a new ticket: #3151.  Since it has nothing to do with this ticket.


---

Attachment


---

Comment by rlm created at 2008-05-10 21:15:45

I've watched this confuse so many people. +1


---

Comment by was created at 2008-05-10 22:20:26

This patch may depend on #1230, which might depend on the patch at #2636 and its dependency (#336).


---

Comment by mabshoff created at 2008-05-11 08:42:52

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-11 08:42:52

Resolution: fixed
