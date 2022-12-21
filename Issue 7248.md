# Issue 7248: include jinja2 / upgrade jinja spkg

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2009-10-19 08:42:29

Assignee: boothby

CC:  jhpalmieri

I'm not sure whether this is an upgrade or a new spkg, but the plan is to switch the notebook to Jinja2, which will require updating/replacing the current Jinja spkg.

John Palmieri has a proposed spkg at #6586.


---

Comment by jhpalmieri created at 2009-10-19 19:13:03

> John Palmieri has a proposed spkg at #6586.

"Proposed"?  It's in Sage 4.2.alpha0.

Some work needs to be done if you want to get rid of Jinja -- last time I checked, some parts of the Sage library use things from Jinja that it wasn't immediately obvious how to replace using Jinja2: see [this comment from #6586](http://trac.sagemath.org/sage_trac/ticket/6586#comment:49).


---

Comment by ddrake created at 2009-10-19 23:22:16

Replying to [comment:1 jhpalmieri]:
> > John Palmieri has a proposed spkg at #6586.
> 
> "Proposed"?  It's in Sage 4.2.alpha0.

Oops. I didn't know.
 
> Some work needs to be done if you want to get rid of Jinja

For this ticket, I was thinking of just getting jinja2 in. We can do another ticket later for removing jinja. I'll close this since it's already done.


---

Comment by ddrake created at 2009-10-19 23:22:16

Resolution: fixed


---

Comment by mhansen created at 2009-10-20 03:32:06

Actually, the notebook hasn't switched over.  The only thing in Sage 4.2 that uses Jinja2 is Sphinx.


---

Comment by mhansen created at 2009-10-20 03:32:06

Changing status from closed to new.


---

Comment by mhansen created at 2009-10-20 03:32:06

Resolution changed from fixed to 


---

Comment by ddrake created at 2009-10-20 05:22:48

Replying to [comment:3 mhansen]:
> Actually, the notebook hasn't switched over.  The only thing in Sage 4.2 that uses Jinja2 is Sphinx.

This ticket isn't about switching anything to Jinja2. The title is "include jinja2 / upgrade jinja spkg", and I closed it because you had already done exactly that in 4.2.alpha0.

#7249 is about switching, and it has a patch and awaits review.


---

Comment by mhansen created at 2009-10-20 05:32:51

Duplicate of #6586.


---

Comment by mhansen created at 2009-10-20 05:32:51

Resolution: duplicate
