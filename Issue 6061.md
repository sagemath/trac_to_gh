# Issue 6061: [with patch; needs review] refresh the pickle jar

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-05-18 04:00:25

Assignee: mabshoff

Sage-4.0 has tons  (nearly 100) of objects with doctests that create pickles, which aren't in the pickle jar right now (in sage-3.4.2).  
The attached new pickle *adds* all these 100 pickles to the existing pickle jar, and deletes a few from calculus that are no longer supported.  This depends on the pynac switch for the new symbolic pickles to work.


---

Comment by mabshoff created at 2009-05-20 23:38:04

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-20 23:38:04

Resolution: fixed


---

Comment by mabshoff created at 2009-05-20 23:40:59

Oh, positive review obviously.

Cheers,

Michael
