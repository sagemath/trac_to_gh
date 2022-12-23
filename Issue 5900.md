# Issue 5900: [with patches, needs review] Add support for system python != Sage python

Issue created by migration from https://trac.sagemath.org/ticket/5900

Original creator: tabbott

Original creation time: 2009-04-26 05:43:42

Assignee: tabbott

On Ubuntu jaunty, the system Python is 2.6 but Sage is built with Python 2.5.  This results in problems in a few places where Sage directly invokes a python program rather than running it via python.  For example, running "trial" rather than "python $(which trial)" would result in "trial" being started with Python 2.6.

I've attached the set of patches that I applied in order to deal with this issue in Jaunty.  I believe they should be harmless for Sage, since it puts $SAGE_LOCAL at the start of PATH, ahead of any system copies of trial/twistd/etc. that might exist.



---

Attachment


---

Attachment


---

Comment by mhansen created at 2009-09-08 05:29:43

They look good to me.  I'm not sure if they are still relevant since Sage switched to Python 2.6, but they shouldn't hurt.


---

Comment by mvngu created at 2009-09-08 11:07:03

Resolution: fixed


---

Comment by mvngu created at 2009-09-08 11:07:26

Applied to the bin repository.
