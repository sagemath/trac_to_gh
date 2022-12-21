# Issue 2422: Update Programming Guide

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-07 17:29:17

Assignee: tba

The programming guide should be updated:

1. Instructions about working with trac (posting a patch, the "[with patch, needs review]", the review process, etc.)

2. Expectations for patches (doctests and documentation, clean code, can be slow as an initial version, but if it's a naive way to do things when it could be faster, it should probably be mentioned, references for algorithms if it is an algorithm from a paper, etc.)

3. Instructions on creating patches instead of bundles, maybe a short introduction to queues.

4. Say that you really should go ask people to review your patch and then follow up and make sure the patch doesn't fall through the cracks.

5. Instructions for running the doctests to check for failures.

6. Expectations and instructions for creating spkgs



---

Comment by jason created at 2008-03-07 17:37:14

Also, we probably ought to reorganize the guide so that it's very, very easy for a person to pick it up and start doing at least small fixes.  Maybe put the short mercurial tutorial in the very front with a small documentation-fixing example or an example of adding a simple function.


---

Comment by mabshoff created at 2008-03-07 20:04:09

This ticket is a collection of various things to do. It would be better if each of the listed tasks would be its own ticket (some already are) since it seems unlikely that all of the above issues will be solved in on patch and during one merge cycle. We should wait past Doc Day 2 how much happens there, but it is likely that once a patch has been merged this ticket will be closed and the left overs will be moved to new ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-07 20:37:57

Replying to [ticket:2422 jason]:
> The programming guide should be updated:
> 
> 1. Instructions about working with trac (posting a patch, the "[with patch, needs review]", the review process, etc.)

This is #1648.

> 2. Expectations for patches (doctests and documentation, clean code, can be slow as an initial version, but if it's a naive way to do things when it could be faster, it should probably be mentioned, references for algorithms if it is an algorithm from a paper, etc.)

Also partly covered by #1648.

> 3. Instructions on creating patches instead of bundles, maybe a short introduction to queues.

The way to create patches is already in the manual. What is needed is to tell people to use bundles only in special situations and to change the default example in that section away from bundles.

> 4. Say that you really should go ask people to review your patch and then follow up and make sure the patch doesn't fall through the cracks.

This is also covered by #1648.

> 5. Instructions for running the doctests to check for failures.

I am not sure, but it seems obvious to do. I also mention it in the material I have written for #1648.

> 6. Expectations and instructions for creating spkgs

#1647 - so there isn't much meat left for this ticket :)

I will be working on #1647 and #1648 once 2.10.3 is out and most likely during Doc Day 2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-25 21:32:16

This ticket can be closed once #3905 has been merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-31 07:59:04

Resolution: fixed


---

Comment by mabshoff created at 2008-08-31 07:59:04

Since #3905 has been merged this can be closed. In case you want improvements please open a specific followup ticket.

Cheers,

Michael
