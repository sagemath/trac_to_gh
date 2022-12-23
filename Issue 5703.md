# Issue 5703: [with patch; needs review] notebook -- fix major bug introduced by #5687

Issue created by migration from https://trac.sagemath.org/ticket/5703

Original creator: was

Original creation time: 2009-04-07 04:54:54

Assignee: boothby




---

Comment by was created at 2009-04-07 04:56:29

I was looking in the logs and found a serious bug introduced by me in the patch for #5687.  The attached 1-line patch fixes this bug.


---

Attachment

Looking at the code this patch looks ok.

It applies cleanly.

Tested this on my Fedora installs. Don't know whether this qualifies as a positive review :)

Jaap


---

Comment by mabshoff created at 2009-04-08 01:27:12

After talking to William about why this fix I am giving this a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 01:48:47

Merged in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 01:48:47

Resolution: fixed
