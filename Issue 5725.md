# Issue 5725: [with patch; needs review] sequences -- bring coverage to 100%; don't allow hashing of mutable sequences

Issue created by migration from https://trac.sagemath.org/ticket/5725

Original creator: was

Original creation time: 2009-04-09 08:34:53

Assignee: cwitty

Bring up the coverage of sequence.py from 59% to 100%.  Also, sequences allowed hashing even when they are mutable which *breaks* all the Python algorithms that rely on hashing!  This was because I didn't understand this fast about Python when I implemented Sequences.  

If there is any fallout as a result of eliminating hashing, then that other code must be fixed, because it would surely exhibit subtle bugs. 


---

Attachment

FYI: I ran long doctests and all of the tests pass.

Cheers,

Michael


---

Comment by robertwb created at 2009-04-09 08:59:21

Looks good to me.


---

Comment by mabshoff created at 2009-04-09 09:10:57

Merged in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 09:10:57

Resolution: fixed
