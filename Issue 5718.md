# Issue 5718: notebook -- %hide works fine in the worksheet but shows up when printing

Issue created by migration from https://trac.sagemath.org/ticket/5718

Original creator: was

Original creation time: 2009-04-08 19:40:13

Assignee: boothby

I was able to easily reproduce the following bug in sage-3.4.


```
Hello,

%hide works fine in the worksheet but shows up when printing.  Any
advice is appreciated.

 - Sage3.4 VMWare Image
 - Dell Vostro 200 desktop

Thanks,
lmc
```



---

Comment by mabshoff created at 2009-04-09 19:34:07

Unless there is a patch for this issue it will not be considered for Sage 3.4.1, hence bumped.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2009-06-04 18:31:09

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 18:31:09

Looks good to me.  Merged in 4.0.1.rc1.
