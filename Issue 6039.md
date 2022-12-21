# Issue 6039: [with patch, needs review] Change name of pari's sum function when imported

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2009-05-14 16:49:37

Assignee: craigcitro

When we include Pari's `sum` function via `libs/pari/decl.pxi`, it takes precedence over the default Python one. This causes some rather confusing compiler errors -- see, e.g., this thread:

http://groups.google.com/group/sage-devel/browse_thread/thread/68a7bd7e99ef22e6#

The attached patch uses string replace magic to rename it to `pari_sum`. 


---

Attachment


---

Comment by mabshoff created at 2009-05-14 17:15:45

It is never a good idea to touch sage/libs/pari/decl.pxi :). Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-14 17:33:03

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-14 17:33:03

Resolution: fixed
