# Issue 2212: degree sequence documentation [with bundle, needs review]

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2008-02-19 20:30:40

Assignee: rlm

This corrects some errors/transpositions in the documentation of the various degree sequence functions.  It also removes the "seed" variable in DegreeSequence itself, as a main NetworkX developer confirmed what the NetworkX code suggests, that this is unnecessary (they have now removed it in their implementation).


---

Comment by kcrisman created at 2008-02-19 20:31:19

Changes degree sequence documentation and removes "seed" variable from DegreeSequence


---

Attachment

Upon looking at the .diff, I see some changes which I did NOT put in there.  I saw them while using hg_sage, but figured it was some artifact, yet here they are.  
The only changes I made were very short ones in the documentation for the various DegreeSequence functions and removing "seed".  Apologies for not catching this; I assume the other changes were already incorporated in any case.


---

Comment by mabshoff created at 2008-02-19 20:52:16

The bundle needs to be rebased against the current release, so do not apply.

Cheers,

Michael


---

Comment by kcrisman created at 2008-02-28 01:50:56

New patch correctly based against 2.10.2 release.


---

Comment by kcrisman created at 2008-02-28 01:51:26

Newer patch based on 2.10.2


---

Attachment

Based on 2.10.3.rc2


---

Comment by jason created at 2008-03-07 23:41:19

Positive review pending a couple of suggestions:

1. In DegreeSequence, in the docs, it says "connecting vertices of highest to" and should probably read "connecting vertices of highest degree to"

2. DegreeSequenceExpected never does anything with the seed parameter.  Can you modify the call to networkx so that the seed is passed?

3. The docs for DegreeSequenceExpected contain the informational, but distracting, parenthetical remark about quantum graphs.  Can you delete that remark?


---

Comment by rlm created at 2008-03-08 00:11:29

This is probably clear already, but just in case, do NOT apply 8681.patch.

+1 on the positive review


---

Comment by kcrisman created at 2008-03-08 01:02:44

Responding in reverse order:

3. Whoever wrote the original documentation put that in there, so I left it, though I also found it distracting. Was there additional functionality expected?  So I'll remove it there and in another place it occurs, and if we ever support quantum graphs we can put it back in.  (I sheepishly admit I have never heard of quantum graphs.)

2. I didn't notice that, and will add the call, since NetworkX definitely has it.

1. I also left that alone because it was in the original documentation, but with the review I gladly change it.


---

Attachment

Fixes of comments - please apply AFTER 8809 patch.  Confirming to NOT apply 8681 patch or previous bundle.


---

Comment by jason created at 2008-03-10 14:56:27

The changes look good to me.  I say apply.


---

Comment by mabshoff created at 2008-03-13 12:45:42

Merged in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-13 12:45:42

Resolution: fixed
