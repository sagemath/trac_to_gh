# Issue 5523: [with patch, positive review] odd primary steenrod algebra fixes

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-15 03:16:30

Assignee: jhpalmieri

I'm attaching a patch to this and also giving it a positive review.  Here's why:

Charlie Odenthal (University of Toledo) sent email to me saying that he had found a few bugs in the Steenrod algebra component of Sage, and he sent me new .py files fixing the bugs. I tested his fixes, and had they been submitted as a patch file for a ticket, I would have given them a mostly positive review.  I fixed a few bugs in his new code, added some doctests, and cleaned up one thing.  Then I sent the results back to him, and he said that he was happy with my changes.  I'm attaching a patch containing our combined work, although he should get the credit, and my work should be viewed as a reviewer's patch.

I suppose I should describe the problems: computing antipodes in the odd primary Steenrod algebra was giving the wrong answers for some elements (because I had implemented it incorrectly) and was very slow for some other elements (because of the choice of algorithm).  Also, some elements which should have been equal weren't (because of a bug in multiplication).  These have now all been fixed, with doctests demonstrating that.



---

Attachment


---

Comment by mabshoff created at 2009-03-25 08:16:54

Resolution: fixed


---

Comment by mabshoff created at 2009-03-25 08:16:54

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
