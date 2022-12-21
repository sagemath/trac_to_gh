# Issue 3153: make finite_field_ntl_gf2e use randstate framework

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-05-10 22:41:39

Assignee: tbd

The patch from #3020 added a new call to a pseudo-random-number generator, not under the control of the Sage randstate framework.  This patch fixes that up, as well as adding some new documentation to randstate.  Applies on top of the patch from #3020.


---

Attachment


---

Comment by cremona created at 2008-05-14 21:43:13

This is a very good idea indeed.  The patch looks fine to me though it would also be agood idea if someone more familiar with Sage's random framework looked at it too.


---

Comment by mabshoff created at 2008-05-17 18:31:11

Resolution: fixed


---

Comment by mabshoff created at 2008-05-17 18:31:11

Merged in Sage 3.0.2.alpha1
