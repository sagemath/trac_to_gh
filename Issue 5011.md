# Issue 5011: [with patch, needs review] Solaris: fix get_memory_usage() to use top

Issue created by migration from https://trac.sagemath.org/ticket/5011

Original creator: mabshoff

Original creation time: 2009-01-18 06:45:58

Assignee: mabshoff

get_memory_usage() falls back to using top when not on Linux. The OSX case is hard coded, but on Solaris we need this patch to make it work.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-18 06:46:04

Changing status from new to assigned.


---

Attachment

I don't have a Sun to test this on, so I'm taking for granted that the actual command being run is correct. However, I can verify that it will only be run on a Sun, which is the goal. So positive review with Michael's assurance that it's the correct usage. :)


---

Comment by mabshoff created at 2009-01-18 13:57:52

Resolution: fixed


---

Comment by mabshoff created at 2009-01-18 13:57:52

Merged in Sage 3.3.alpha0
