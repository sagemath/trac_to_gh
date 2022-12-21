# Issue 5083: Colormap updating?

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-01-24 02:44:59

Assignee: was

CC:  abergeron was mhansen

Referring to #4884 and the last set of comments there - loose ends for colormap info:

1. So should there be cmap_help or not?  abergeron's last statement  in #4884 implies yes.  If so...

2. For every function (e.g. matrix_plot) where cmap is an option, that function's docstring should have as a doctest a full call of cmap_help (or whatever with its output.  Also in the cmap_help doctest should have the whole output of cmap_help show up, not have ... where the actual colormaps are outputted.

If neither of these things are true, please close this ticket.  It seemed like both were true, though.


---

Comment by abergeron created at 2009-01-24 02:50:30

Tickets are not a good place for discussions, I will start a thread on sage-devel.


---

Comment by kcrisman created at 2009-01-24 02:56:18

Sorry, I was not trying to cause trouble, just trying to ask for clarification and a followup ticket seemed appropriate as opposed to spamming sage-devel.


---

Comment by mabshoff created at 2009-01-24 03:02:41

Replying to [comment:2 kcrisman]:
> Sorry, I was not trying to cause trouble, just trying to ask for clarification and a followup ticket seemed appropriate as opposed to spamming sage-devel.

Do not worry about it. The merge of the cmap patch was somewhat rushed and may be not the optimal solution, but given the time table back then it was the right decision. 

As Arnaud pointed out such discussions should be help on [sage-devel] since it is difficult for many people interested in this problem would be even aware that it is happening. Discussions on tickets also make the ticket harder to merge since I tend to read the ticket and when one has many it slows me down. One prime example of a messy ticket is the boolean logic one as well as the TinyMCE mess (sorry Jason :). It all gets resolved, but if the volume on [sage-devel] is too high people need to switch to digest mode for example.

The summary of the ticket should also be improved since the current title is meaningless to anyone not aware of the previous ticket. Fortunately you referred the ticket here, but you should also mention on the old ticket that the follow up ticket is this one.

Cheers,

Michael


---

Comment by kcrisman created at 2009-01-24 19:33:10

Changing priority from major to minor.


---

Comment by robertwb created at 2009-01-28 00:09:46

If there really are a lot of options, I would rather see a cmap object so one could do

cmap?
... lots of documentation ...

cmap.[tab]
... list of options


---

Comment by kcrisman created at 2009-12-10 14:20:04

This is taken care of in #5601 along with a lot of other color things.  Thanks, Mitesh!

To release manager: please close this once #5601 is merged, assuming it is.


---

Comment by kcrisman created at 2016-02-09 16:13:42

Changing status from new to needs_review.


---

Comment by kcrisman created at 2016-02-09 16:15:06

See comment:6


---

Comment by kcrisman created at 2016-02-09 16:15:06

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-02-23 22:59:37

Resolution: fixed
