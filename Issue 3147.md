# Issue 3147: "Quit Worksheet" in notebook doesn't seem to work anymore

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2008-05-09 22:32:49

Assignee: anybody

Action: Click on "Quit worksheet" when you have a worksheet open

Expected result:
 * Sage process behind worksheet exits/gets killed (happed prior to 3.0)
 * Browser goes back to worksheet list (this would be an enhancement over previous behaviour)

Actual result:
 * drop down list keeps "quit worksheet" selection and no other result
 * if you return to worksheet list manually, the worksheet is still listed as "(active)"

Reproducible:
 * every time for me: vanilla RHEL Server 5.1 box (amd64) running sage notebook as "nobody".
Connection made with Firefox 2.0.0.14 from a Fedora 7 machine.

Problem:
 * machine fills up with sage processes. Restarting the sage server solves the problem, obviously, but is a bit draconian.


---

Comment by boothby created at 2008-05-10 17:20:09

Note:  the "save & quit" and "discard & quit" buttons work for me, while using the pulldown does not.


---

Comment by nbruin created at 2008-05-10 23:21:05

The patch for #1230 resolves the issue for me, so once that ticket is closed, I would not mind if this one gets closed too.


---

Comment by was created at 2008-05-10 23:23:40

I agree with Nils, this is a dup of #1230.


---

Comment by was created at 2008-05-10 23:23:40

Resolution: duplicate
