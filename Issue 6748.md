# Issue 6748: [with patch, needs review] Adds Graph.Cliquer to the reference

Issue created by migration from https://trac.sagemath.org/ticket/6748

Original creator: ncohen

Original creation time: 2009-08-14 19:11:16

Assignee: tba

All the cliquer-related functions in the Graph class are documented, but they do not appear in SAGE's reference as they all use functions defined in graphs/cliquer, which is not included in the .rst file.

This patch fixes this, plus adds a few lines to the docstrings in cliquer.pyx


---

Attachment

apply on top of previous patch


---

Comment by jason created at 2009-09-22 16:03:32

looks good!


---

Comment by mvngu created at 2009-09-22 21:34:08

Merged both patches.


---

Comment by mvngu created at 2009-09-22 21:34:08

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:32:14

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on the making the notebook a standalone package.
