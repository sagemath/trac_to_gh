# Issue 2913: [with patch; needs review] notebook -- deleting a running cell results in a bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-14 03:27:27

Assignee: boothby


```
Today when I was using the notebook I got this:

http://skitch.com/yqiang/jqwb/notebook-bug

Is this a known bug? It happened when I deleted a cell while it was
still running and trying to produce output.

Cheers,
Yi
```



---

Attachment


---

Comment by yi created at 2008-04-14 04:51:25

Patch applied cleanly against alpha3 and fixes my original issue, good job!


---

Comment by mabshoff created at 2008-04-14 04:58:26

Resolution: fixed


---

Comment by mabshoff created at 2008-04-14 04:58:26

Merged in Sage 3.0.alpha5
