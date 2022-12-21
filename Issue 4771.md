# Issue 4771: notebook -- get rid of these debug log messages I put in: "Dumping ..."

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-12 19:04:12

Assignee: boothby

The messages:

```
2008-12-12 10:56:37-0800 [HTTPChannel,53,24.143.70.101] Dumping admin history to 'sage_notebook/worksheets/admin/history.sobj'
```

that the notebook prints out for no good reason should be deleted by commenting out the line in the notebook server code that prints them.


---

Attachment


---

Comment by mabshoff created at 2008-12-13 06:30:10

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-13 09:36:11

Resolution: fixed


---

Comment by mabshoff created at 2008-12-13 09:36:11

Merged in Sage 3.2.2.alpha2
