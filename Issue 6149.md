# Issue 6149: Fix ReST glitches

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-05-28 13:05:02

Assignee: tba

CC:  cremona

Building the documentation currently raises something like 50 errors because of incorrect ReST formatting in docstrings (mostly "unexpected indent" or similar). We should probably have a policy of not merging patches that cause documentation building errors, just as we don't merge patches that cause doctest failures.

I have found and fixed most of the errors in 4.0.rc1 (some with great difficulty, because the ReST parser is very unreliable at telling you where the error is arising in a given file).

I know this is a bit last-minute, but the patch below doesn't actually change any code at all, so it might not be too late to include it in the final 4.0 release.


---

Attachment

patch against 4.0.rc1


---

Comment by davidloeffler created at 2009-05-28 13:17:04

With the above patch applied, the documentation should build fine.

John: I've cced you here, since you say you have suffered from this too :-) Any chance you could review this one quickly, since it would be good to get it into 4.0?


---

Attachment


---

Comment by mhansen created at 2009-05-28 16:32:18

David's patch looks good to me.

Could someone take a quick look at my patch?


---

Comment by mhansen created at 2009-05-28 16:32:18

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-28 16:32:18

Changing assignee from tba to mhansen.


---

Comment by davidloeffler created at 2009-05-28 17:36:28

Looks fine to me - docs build OK, and the dsage page looks good.

David


---

Comment by mhansen created at 2009-05-28 17:51:44

Resolution: fixed


---

Comment by mhansen created at 2009-05-28 17:51:44

Merged both patches in 4.0.rc2.


---

Comment by jhpalmieri created at 2009-05-28 18:27:16

This got refereed too quickly for me!  See #6152 for a few more fixes -- should be quick to referee.
