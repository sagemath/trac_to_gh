# Issue 8050: fix SPKG.txt in cddlib

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-01-24 03:23:23

Assignee: tbd

CC:  vbraun alexghitza mhampton

The file SPKG.txt in the cddlib spkg does not respect the rules at

http://www.sagemath.org/doc/developer/producing_spkgs.html




---

Comment by vbraun created at 2010-01-27 17:07:18

Updated SPKG.txt


---

Attachment

I've attached my current version, and I think it conforms to the specs. Let me know if there is anything missing.


---

Comment by vbraun created at 2010-01-27 17:09:08

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-02-20 16:56:35

Could be patch be rebased against cddlib-094f.p4.spkg?


---

Comment by vbraun created at 2010-02-20 17:30:17

The SPKG.txt attached to this ticket is an older version, in particular the sections "Special Update/Build Instructions" are wrong. 

All outstanding issues are already fixed in cddlib-094f.p4.spkg, see #8115. I recommend to close this ticket.


---

Comment by mvngu created at 2010-02-20 17:31:46

Close as fixed by #8115.


---

Comment by mvngu created at 2010-02-20 17:31:46

Resolution: fixed
