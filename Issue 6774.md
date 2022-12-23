# Issue 6774: [with patch, needs review] tour Graph Theory

Issue created by migration from https://trac.sagemath.org/ticket/6774

Original creator: ncohen

Original creation time: 2009-08-18 17:08:45

Assignee: tba

Hello !

I thought it was a pity Sage contained nothing yet about Graph theory. This is what I have written to fix it... Merge any of your ideas in it, it can not hope to be complete !

And.... If I forgot your country when coloring the map of Western Europe, or if you do not stand to watch Western Europe being colored while your country is not, just add the data to the document ;-)

Nathann


---

Attachment


---

Attachment

apply on top of previous patch


---

Comment by jason created at 2009-09-17 09:32:45

I added stylistic/punctuation corrections.  Positive review pending the examples actually working (I believe they need ncohen's patches to be merged in).


---

Comment by jason created at 2009-09-17 19:17:51

I guess I should change this to "positive review", and just say it depends on whatever tickets implement the functionality in the examples.


---

Comment by mvngu created at 2009-09-17 23:06:32

Merged patches in this order:

 1. `graph_tour.patch`
 1. `trac-6774-graph-tour-review.patch`

See #6952 for a follow-up to this ticket.


---

Comment by mvngu created at 2009-09-17 23:06:32

Resolution: fixed


---

Comment by jason created at 2009-09-19 02:58:07

I assume that you merged the tickets that define the functions listed here (i.e., you were able to run doctests on this file and everything was okay).  The functions in this file did not work for me with 4.1.1.alpha1, presumably because they hadn't been merged at that point.


---

Comment by mvngu created at 2009-09-19 19:27:16

Replying to [comment:4 jason]:
> I assume that you merged the tickets that define the functions listed here
Yes, I have done so.





> (i.e., you were able to run doctests on this file and everything was okay).
Yes, with the two patches on this ticket all doctests in the tutorial pass.


---

Comment by jhpalmieri created at 2009-10-08 02:01:22

Replying to [comment:5 mvngu]:
> Replying to [comment:4 jason]:
> > I assume that you merged the tickets that define the functions listed here
> Yes, I have done so.

No, you haven't.  These functions are defined in #6679 and #6680, which haven't been reviewed, let alone merged.  This ticket should have been marked as "depends on #6679 and #6680": we can't have functions mentioned in the tutorial which are not yet part of Sage.  For now, the graph theory tour has been removed from the tutorial -- see #7149.

When the tickets #6679 and #6680 have been merged, then open up a new ticket to reinstate the graph theory tour (the corrected version, as of #6952).  Before running doctests, apply the script patches from #6572 to make sure that everything is getting tested -- the current doctesting system is broken, so many doctests in .rst files are inadvertently skipped.


---

Comment by ncohen created at 2009-10-08 06:15:32

I would have prefered the fixing to be "let's review these two patches now to have a good Graph Theory Tour", but removing it for the moment is a good solution too..
Perhaps Minh just meant that he had applied the corresponding patches to test the tutorial..

The thing is that patches #6679 and #6680 define for Sage some of the most important functions in Graph Theory ( Flows, matching, graph coloring, connectivity, etc .. )

The first version is two month old, and since then I have had to update them each time class MIP is modified. I do not even know myself how many things I have yet to write based on these functions.. What could we do about it ? If the code is not commented enough, if the only things you need are references, tell me and they'll be there in a few seconds :-)


---

Comment by ncohen created at 2009-11-24 23:32:14

Resolution changed from fixed to 


---

Comment by ncohen created at 2009-11-24 23:32:14

Changing status from closed to new.


---

Comment by ncohen created at 2009-11-24 23:32:20

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-29 10:15:39

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-29 10:19:11

I thought that we didn't want things in the tutorial that depended on optional packages.


---

Comment by mvngu created at 2009-11-29 10:25:14

Replying to [comment:11 mhansen]:
> I thought that we didn't want things in the tutorial that depended on optional packages.
That is correct. Anything in the attached patches that uses optional packages should be removed. A new patch should be attached that still gives a tour of graph theory in Sage, but without using any optional packages.


---

Comment by ncohen created at 2009-11-29 10:41:52

Is it just because it would be a legal problem for Sage to claim as "available" functions that we cannot provide without the addition of a software we are not allowed to embed ?

In this case I understand this decision, but you have to consider the fact that it is very likely 99% of Sage's graph theoretical functions will depend on Linear Programming by the time people REWRITE the functions I defined using Linear Programming through other means.

I'll just try again to find a free LP solver or an old version of GLPK. And in the meantine I'll just update my personnal tutorial on Graphs (available pretty soon).. :-)


---

Comment by ncohen created at 2009-11-29 10:44:30

Besides, this can be updated because of ticket #6813 which just got merged... We have much more that eastern europe in Sage now :-)


---

Comment by jhpalmieri created at 2009-11-29 16:06:12

Replying to [comment:13 ncohen]:
> Is it just because it would be a legal problem for Sage to claim as "available" functions that we cannot provide without the addition of a software we are not allowed to embed ?

It's because everything in the tutorial should "just work".  You shouldn't have to install anything extra, it should work right out of the box.


---

Comment by jhpalmieri created at 2009-12-22 00:12:47

Can we close this as "won't fix"?


---

Comment by mvngu created at 2009-12-22 03:58:16

The graph theory tour as is cannot be added to the tutorial since it depends on an optional package. However, you can open a ticket to add that tour to the Constructions document.


---

Comment by mvngu created at 2009-12-22 03:58:16

Resolution: wontfix
