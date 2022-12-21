# Issue 4226: [with patch, needs reivew] Real Lazy Field

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-30 21:10:57

Assignee: robertwb

This is needed for number field embedding. 


---

Attachment


---

Attachment

Looks good to me.  Note that the second patch should be applied as well since we got rid of the *_impl methods.


---

Comment by mabshoff created at 2008-10-01 08:34:27

The doctest "hash(RLF(sin(1)))" should probably not be #random, but should have separate #32 and #64 bit output.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-01 08:40:15

Fix a typo so the ticket is picked up by reports.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-01 10:32:17

I fixed the 32 vs. 64 bit hashing issue in a trivial patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-01 10:32:28

Resolution: fixed


---

Comment by mabshoff created at 2008-10-01 10:32:28

Merged in Sage 3.1.3.alpha3


---

Comment by robertwb created at 2008-10-01 19:19:06

Thanks for the fixes (I should have remembered that arithmetic patch got in).
