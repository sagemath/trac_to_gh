# Issue 5720: [with patch, needs review] notebook -- new worksheets open in new page/tab

Issue created by migration from https://trac.sagemath.org/ticket/5720

Original creator: jhpalmieri

Original creation time: 2009-04-08 22:51:51

Assignee: jhpalmieri

Along the lines of #5681: this patch makes the "new worksheet" button open up in a new tab.

Note that the new system with this patch (or even just with #5681) is not perfect: if you open up a worksheet, work for a while, then hit "Save & Quit" or "Discard & Quit", you now have two tabs open listing your active worksheets.



---

Attachment


---

Comment by mabshoff created at 2009-04-09 21:22:33

Merged in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 21:22:33

Resolution: fixed
