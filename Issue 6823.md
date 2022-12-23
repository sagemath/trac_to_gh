# Issue 6823: [with patch, needs review] Kneser Graph in graph_generators

Issue created by migration from https://trac.sagemath.org/ticket/6823

Original creator: ncohen

Original creation time: 2009-08-25 08:20:10

Assignee: rlm

Kneser graphs for graph_generators ( http://en.wikipedia.org/wiki/Kneser_graph )

I just define the new function graphs.KneserGraph()


---

Attachment


---

Comment by rbeezer created at 2009-09-21 02:13:04

Changing keywords from "" to "graph generators kneser".


---

Comment by rbeezer created at 2009-09-21 02:13:04

Hi Nathann,

This will be a nice addition to the graph generators.  Some suggestions:

1.  How about giving the graph a name with the parameters in the string, like "Kneser graph with parameters 5 and 2"?

2.  The patch just seems to be a diff file, so it really should be a Mercurial patch with your name/email and a one-line comment.  Patch files now seem to uniformly have filenames that begin with "trac_xxxx_" and you should put the trac number in the one-line summary of the Mercurial patch.

3.  I'd really like to see more robust handling of the inputs (and doctests to see that they work).  For example, a negative n will bomb in the subset code.  How about checking that `n >= 0` and then that  `0 <= k <= n`?

4.  English is very good, but I'd suggest "adjacent" or "joined" instead of "linked" and "with parameters" instead of "of parameters" (three places).

With this completed, it'll be easy to add the Odd graphs - just Kneser graphs with n=2k+1.

This passes all tests in sage/graphs and the documentation builds fine.

Rob


---

Comment by ncohen created at 2009-09-26 09:07:01

New patch. Odds graphs are added, and with some luck each one of your remarks will find an answer in this new version. Hope you'll like it ! :-)

Nathann


---

Attachment


---

Comment by ncohen created at 2009-09-29 11:07:56

New patch taking into account the comments from #6828


---

Attachment

Reviewer patch to set odd graph name


---

Comment by rbeezer created at 2009-09-30 05:40:19

Nathann,

Looks very good, builds on 4.1.2.alpha2, passes all tests, etc.

Right now the name of an odd graph reports the Kneser graph parameters, etc.  I'd expect this to confuse someone who builds an odd graph, yet does not know the connection to the Kneser graphs.  I've attached a small patch that just sets the name on the odd graph routine.  If you agree with the change, then you can mark the ticket as positive review.  In other words, you can review my additional patch, and we'll be done.

Thanks,
Rob


---

Comment by ncohen created at 2009-09-30 07:21:03

Good thinking ! ;-)

Nathann


---

Comment by mhansen created at 2009-10-15 16:25:00

Resolution: fixed
