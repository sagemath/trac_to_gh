# Issue 6374: [with patch, needs review] Fix race condition in sage build process

Issue created by migration from https://trac.sagemath.org/ticket/6374

Original creator: craigcitro

Original creation time: 2009-06-20 20:41:41

Assignee: tbd

CC:  ncalexan georgsweber

So on #6234, there was a second patch to fix a race condition that Nick saw during the 4.0.2 release cycle. Someone else just ran into this, and I noticed that the second patch from that ticket somehow didn't make it into Sage. (Oops.)

I'm attaching the patch here, with the same filename -- see #6234 (at the bottom) for an example of the bad behavior and an explanation for the fix. It's already been reviewed at least once, but a second review wouldn't hurt. ;)


---

Attachment

At least twice, I ran into the failure (hopefully) fixed by this ticket. I already volunteered to review it (in a note on sage-release), but if somebody else is faster, OK.


---

Comment by GeorgSWeber created at 2009-07-22 19:59:49

Works fine for/with Sage-4.1.1.alpha0. It's hard to "prove" that a certain sporadic failures has been fixed, but the patch at least doesn't hurt. And it is plausible that it does help indeed.


---

Comment by mvngu created at 2009-07-23 01:43:50

Resolution: fixed
