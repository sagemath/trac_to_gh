# Issue 3515: Finance builds incorrectly with pbuild

Issue created by migration from Trac.

Original creator: ghtdak

Original creation time: 2008-06-26 15:48:43

Assignee: gfurnish

Finance needs to be set up or pbuild configured to properly compile.


---

Comment by mabshoff created at 2008-06-26 19:01:45

Glenn,

could you post some actual output from the failure?

Cheers,

Michael


---

Comment by ghtdak created at 2008-06-27 02:37:54

We don't have output per se.  It just didn't work and william suggested trying it without pbuild and it was fine.  I've discussed with Gary and we didn't implement at the time as he was refactoring the pbuild code but is aware of the problem.

My understanding is that its a straightforward entry somewhere but I don't have any information as to how to configure pbuild.


---

Comment by gfurnish created at 2008-07-01 17:15:07

This should be easy to fix after #3399 is applied.  I included some documentation on how to correctly modify pbuild.


---

Comment by mabshoff created at 2008-07-12 14:05:06

Resolution: invalid


---

Comment by mabshoff created at 2008-07-12 14:05:06

This is a duplicate of #3614.

Gary, please check for existing tickets before opening new ones. This is a pbuild ticket owned by you, so you should know about this.

Cheers,

Michael
