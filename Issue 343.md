# Issue 343: inserting tab messes scrolls to top of cell input

Issue created by migration from https://trac.sagemath.org/ticket/343

Original creator: boothby

Original creation time: 2007-04-02 22:38:08

Assignee: boothby

In Firefox, if you make a long (~50 line) input cell, with your cursor towards the bottom, and hit the tab key, focus (in the input cell) bounces to the top -- though the cursor stays where it was. In many cases, it actually scrolls the cursor out of view.


---

Comment by aginiewicz created at 2008-09-02 00:04:17

hmm... just curious, is this still issue? I cannot reproduce it any more (window stays where it was, no jump to top), don't know if due to changes in notebook or in firefox (I use FF3)...


---

Comment by mhansen created at 2009-01-22 13:53:51

Resolution: invalid


---

Comment by mhansen created at 2009-01-22 13:53:51

I can't reproduce this either.  It's been quite awhile ago and the notebook has been reworked since then.  I'm going to mark this as invalid.
