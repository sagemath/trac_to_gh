# Issue 6088: LatticePolytope: Removed a try/catch which could involuntarily hide exceptions from lower code

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-05-20 01:06:58

Assignee: nthiery

CC:  sage-combinat

Keywords: lattice polytope, exceptions

This try catch made it hard to discover a trivial bug in Sequences
because it was catching the corresponding exception.

Its purpose was just to test if some data had already been
cached. This is not on a critical section, so testing on the existence
of an attribute is as good, clearer, and safer.

By the way, I would recommend not to use Sequence for this kind of
applications, as the overhead in speed and complexity is non trivial,
whereas the specific features of Sequence do not seem to be very much
used here. Plain tuples should probably work as well.



---

Attachment

Good change, positive review. I have already learned that it is a bad idea to catch exceptions from a bigger than tiny piece of code.

And thanks for the comment on Sequence! (Here it was used only for pretty output with "cr=True" but probably should not hurt performance too much since operations with nef partitions are long on their own.)


---

Comment by mabshoff created at 2009-05-21 00:33:00

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-21 00:33:00

Resolution: fixed
