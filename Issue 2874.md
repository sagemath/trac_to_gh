# Issue 2874: add tests for type E root system, correct some misinformation in root_system.py, add Justin Walker credit

Issue created by migration from https://trac.sagemath.org/ticket/2874

Original creator: bump

Original creation time: 2008-04-11 00:55:08

Assignee: mhansen

CC:  sage-combinat

This patch was written with Justin Walker, who originally coded the exceptional group root systems based on data from Bourbaki. The patch does 3 things.

(1) Replaces self.dim with self.rank in AmbientLattice_e and corrects some related misinformation in a comment in the file. (The a comment in the file formerly said that E6 had rank 5.)

(2) Adds tests. We checked the dimensions of the fundamental representations against what they are supposed to be (from another source), which is a convincing test that all the root data are correct.

(3) Adds a credit for Justin in the file. This was my idea since I know Justin worked hard on getting the exceptional groups coded but if it is controversial it can be taken down.




---

Attachment


---

Comment by mhansen created at 2008-04-11 01:03:41

Yep, Justin should definitely get credit for the exceptional groups.

Looks good to me.


---

Comment by mabshoff created at 2008-04-11 01:39:16

Dan, 

please post mercurial patches in the future. You need to use export instead of diff. That way you get properly credited in the log as author of the patch. Let me know if you have any more questions.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-11 01:39:27

Resolution: fixed


---

Comment by mabshoff created at 2008-04-11 01:39:27

Merged in Sage 3.0.alpha4
