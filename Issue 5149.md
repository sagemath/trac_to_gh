# Issue 5149: [with patch; needs review] Cremona database -- fix a bug in handling of 990h

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-02-01 08:34:22

Assignee: was

John mentioned that 990h3 is a special case in ticket #5138 -- I looked at the Cremona database code and found that there was one function where this special case isn't treated correctly.  I fixed that and added some doctests.  


---

Attachment

Patch applies cleanly to 3.33.alpha2 and all tests pass.  Code looks good, so pass!


---

Comment by mabshoff created at 2009-02-02 02:56:56

Merged in Sage 3.3.alpha4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 02:56:56

Resolution: fixed
