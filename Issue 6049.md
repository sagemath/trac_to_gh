# Issue 6049: [with patch, needs review] bitset complement zeroes out last word if the bitset is a multiple of the word size

Issue created by migration from https://trac.sagemath.org/ticket/6049

Original creator: jason

Original creation time: 2009-05-16 18:27:46

Assignee: cwitty

CC:  rlm robertwb

I introduced a serious error in bitset complements when the bitsets are multiples of the word size.  This patch corrects this and doctests the correct behavior.


---

Attachment


---

Comment by cwitty created at 2009-05-16 22:26:00

Code looks good, doctests pass.  Positive review.


---

Comment by mabshoff created at 2009-05-18 23:09:30

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-18 23:09:30

Resolution: fixed
