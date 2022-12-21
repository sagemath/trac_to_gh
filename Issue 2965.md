# Issue 2965: extcode spkg build failure on Debian

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-04-20 04:02:32

Assignee: tabbott

Now that there's a dist/debian directory in the extcode spkg, my Debian scripts try to build extcode as a separate package.  This doesn't work; I've attached a trivial patch to make this not happen.


---

Attachment


---

Comment by mabshoff created at 2008-04-20 04:17:09

Patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 04:17:21

Merged in Sage 3.0.rc0


---

Comment by mabshoff created at 2008-04-20 04:17:21

Resolution: fixed
