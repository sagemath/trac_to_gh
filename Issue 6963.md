# Issue 6963: follow up to #3133: fix ReST formatting

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-19 20:01:53

Assignee: tba

CC:  jason kcrisman

This is a follow up to #3133 to fix some ReST formatting issues.


---

Comment by mvngu created at 2009-09-19 20:05:05

depends on #3133


---

Attachment


---

Comment by jason created at 2009-09-20 05:58:26

I didn't apply this, but I think it's probably simple enough that I can give it positive review just by looking at it.

Minh---I would have thought that this was a change small enough that you could have just added this as a "reviewer" patch on the original ticket.


---

Comment by mvngu created at 2009-09-20 20:04:25

Replying to [comment:2 jason]:
> Minh---I would have thought that this was a change small enough that you could have just added this as a "reviewer" patch on the original ticket.
Yes and no. 





Why "yes"? --- The patch is about reviewing ticket #3133.





Why "no"? --- I wanted to merge #3133, or any ticket with a positive review, as soon as possible without any unnecessary delay. It was only after merging #3133 that I created this follow up ticket. In cases where a ticket has positive review and is ready to be merged seamlessly, I think it can be a waste of time to upload another reviewer patch and get someone to review that patch. It's better to get stuff in as soon as possible where merging it results in no doctest or hunk failures. And indeed some people would find it a waste of time and unnecessary work if I had uploaded another reviewer patch that addresses a micro-bug. Better off to isolate the micro-bug to another ticket, while first merging the ticket with positive review.


---

Comment by mvngu created at 2009-09-22 22:07:55

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:35:29

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
