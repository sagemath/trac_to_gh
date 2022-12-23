# Issue 5540: search_doc produces incorrect URLs

Issue created by migration from https://trac.sagemath.org/ticket/5540

Original creator: ddrake

Original creation time: 2009-03-17 02:26:54

Assignee: tba

Keywords: sphinx, documentation, search_doc

From [sage-devel](http://groups.google.com/group/sage-devel/t/2da54338e1dda0fe):

```
If I do search_doc("orbit") in sage 3.4 (in the notebook), I get
(amongst others) a link:

https://localhost:8000/doc/live/html/en/reference/genindex-F.html

which leads to a "resource cannot be found". The appropriate link
seems to be

https://localhost:8000/doc/live/reference/genindex-F.html

It could be that my sage is just screwed up, but if someone else can
confirm this error, a ticket should be opened. I bet it's easy to fix.}}}


---

Comment by jhpalmieri created at 2009-03-17 03:22:04

Changing assignee from tba to jhpalmieri.


---

Comment by jhpalmieri created at 2009-03-17 03:22:04

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-03-17 03:22:04

Changing component from documentation to misc.


---

Comment by jhpalmieri created at 2009-03-17 03:22:04

The attached patch fixes the problem for me.  I fixed the URLs by getting rid of the first two components of the path (replacing 'F', the filename, with `F.split('/', 2)[2]`).  I found another issue: for some reason, probably to get rid of the Sage banner which used to be part of the search output, the raw results 'r' of the search were processed using `r.splitlines()[4:]`.  Since the Sage banner is no longer part of the search output, this now discards the first four results.  (Therefore it's probably my fault: see #4832.) I fixed that, too.


---

Attachment

Patch solves the problem for me. The patch is also tiny, so while I'm not familiar with the code, I wouldn't expect it to cause any regressions.


---

Comment by ddrake created at 2009-03-17 04:09:59

Positive review here.


---

Comment by mabshoff created at 2009-03-25 07:34:19

Resolution: fixed


---

Comment by mabshoff created at 2009-03-25 07:34:19

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
