# Issue 5163: jsmath extensions for published webpages

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-02-03 04:55:31

Assignee: boothby

The extensions enabled in #5021 don't work for published web pages, I think because js.py isn't loaded.

We could move the extensions to be invoked right after jsmath is loaded.


---

Attachment


---

Comment by jason created at 2009-02-03 09:24:40

Changing assignee from boothby to jason.


---

Comment by jason created at 2009-02-03 09:24:40

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-02-04 21:39:41

Looks good to me.  I was wondering if there was a better place to put these extensions when I wrote the patch for #5021...


---

Comment by mabshoff created at 2009-02-05 10:49:17

Merged in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-05 10:49:17

Resolution: fixed
