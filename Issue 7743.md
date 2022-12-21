# Issue 7743: Piecewise integration fixes [with patch; needs review]

Issue created by migration from Trac.

Original creator: pbutler

Original creation time: 2009-12-19 22:52:08

Assignee: AlexGhitza

Keywords: integration

This patch fixes two issues with the piecewise class, brought up in this sage-support thread:

http://groups.google.com/group/sage-support/browse_thread/thread/18d830ece7826898/86c401e4d6b8f3dd

The first issue is that when a piece of the function belongs to the Integer ring, integration doesn't work. This is fixed by coercing each piece to the symbolic expression ring.

The second issue is that there are cases where maxima needs to be given assumptions about the domain of x for the piece being integrated. This is fixed with the assume and forget functions.

Additional unit tests have been added (or existing tests modified) for each issue.


---

Attachment


---

Comment by AlexGhitza created at 2009-12-19 23:36:02

Changing component from algebra to calculus.


---

Comment by AlexGhitza created at 2009-12-19 23:36:02

Changing assignee from AlexGhitza to burcin.


---

Comment by wdj created at 2009-12-20 13:33:51

Changing status from new to needs_work.


---

Comment by wdj created at 2009-12-20 13:33:51

This patch failed to apply to sage-4.3.a1 and 4.3.rc0. Maybe it needs rebasing?


---

Attachment


---

Comment by pbutler created at 2009-12-20 17:10:58

My mistake; I was using a much older version of sage. I've attached another patch that should apply to sage-4.2, but I'm not sure to actually obtain the latest development version of sage-4.3 for testing. Is there documentation on this somewhere?


---

Comment by wdj created at 2009-12-21 02:10:04

Replying to [comment:3 pbutler]:
> My mistake; I was using a much older version of sage. I've attached another 
> patch that should apply to sage-4.2, but I'm not sure to actually obtain 


This doesn't work either.

> the latest development version of sage-4.3 for testing. Is there documentation 
> on this somewhere?

I sent you the link by separate email to your gmail address.


---

Comment by was created at 2009-12-24 07:06:42

I'm declaring a total feature freeze on sage-4.3.


---

Attachment


---

Comment by pbutler created at 2010-01-06 06:03:43

I've attached 13535.patch and tested that it can be applied on sage 4.3, but it doesn't look much different from the previous one (aside from a try/except that I had to add because of a change to the behaviour of `assume`). If it still doesn't apply, could you paste the shell transcript?


---

Comment by wdj created at 2010-01-06 23:56:24

Thanks, I'll review it.


---

Comment by wdj created at 2010-01-06 23:56:24

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2010-01-07 00:00:00

Applies to 4.3.1.a0 (the hacked version) and 4.3. Passes all tests but sagedoc on 64bit ubuntu 9.10 with 4.3.1.a0
and only with seemingly unrelated failures on imac 10.6.2 with 4.3.

Thanks for fixing this bug!

Positive review.


---

Comment by wdj created at 2010-01-07 00:00:00

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 09:12:43

merged just 13535.patch


---

Comment by rlm created at 2010-01-13 09:12:43

Resolution: fixed
