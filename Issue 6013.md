# Issue 6013: rewrite number field relativize to be much faster

Issue created by migration from https://trac.sagemath.org/ticket/6013

Original creator: ncalexan

Original creation time: 2009-05-10 07:59:13

Assignee: was

CC:  was craigcitro

Keywords: number field relativize speed

Patch says it best.  Avoid an nfinit at all costs; allows to relativize over large number fields.

This also fixes longstanding degree one relativize bugs.


---

Attachment

The patch is good, but I accidentally cut it from my symbolics branch.  Not really a problem, but I mangled mq so the hg changeset info is wacky.  Maybe best to use mq to review this, so the actual hg parent, etc, is not taken into account.


---

Comment by mabshoff created at 2009-05-12 05:52:52

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 05:52:52

Resolution: fixed
