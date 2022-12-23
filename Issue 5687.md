# Issue 5687: [with patch; needs review] notebook -- only save snapshot when worksheet.txt has changed.

Issue created by migration from https://trac.sagemath.org/ticket/5687

Original creator: was

Original creation time: 2009-04-05 05:38:54

Assignee: boothby




---

Attachment


---

Comment by TimothyClemans created at 2009-04-05 06:40:11

I can't create a new worksheet

Error:

```
	    if open('%s/worksheet.txt'%self.__dir).read() == E:
	exceptions.IOError: [Errno 2] No such file or directory: 'sage_notebook/worksheets/admin/44/worksheet.txt'
```



---

Attachment

Positive review: Tested both manual save and autosave


---

Comment by mabshoff created at 2009-04-05 22:59:06

Resolution: fixed


---

Comment by mabshoff created at 2009-04-05 22:59:06

Merged both patches in Sage 3.4.1.rc1.

Cheers,

Michael
