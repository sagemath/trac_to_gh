# Issue 1953: [with patch] fix problems found by Jason while reviewing #1945

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-01-27 22:05:53

Assignee: was

Jason found a couple of problems with calculus.py while reviewing #1945: a one-character typo and a duplicate method.  The attached patch fixes both problems.

Doctests pass in sage/calculus/.



---

Attachment

I think this patch is OK.

I want to make one comment though.  With the previous version of this patch, if you made a new class that derives from CallableSymbolicExpressionRing_class and overload args, then arguments would automatically call the overloaded method.  Now it won't -- argument will give you the old method before overloading.  This isn't a problem since that's not done in calculus.py.  

So I give this a positive review.


---

Comment by mabshoff created at 2008-01-27 22:25:45

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 22:25:45

Merged in Sage 2.10.1.rc2
