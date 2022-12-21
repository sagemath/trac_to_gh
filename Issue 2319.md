# Issue 2319: change dsage docstrings to match rest of sage

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-02-26 17:45:06

Assignee: yi

Currently much of the dsage docstrings are written using reST syntax which apparently Sage does not use. It should be rewritten to be more like the other Sage docstrings. An alternative is for new Sage documentation to be written in something like reST which would allow much easier API doc generation through something like epydoc.


---

Comment by was created at 2008-02-27 12:44:34

> Currently much of the dsage docstrings are written using reST syntax 
> which apparently Sage does not use. It should be rewritten to be more 
> like the other Sage docstrings. 
> An alternative is for new Sage
> documentation to be written in something like reST which would 
> allow much easier API doc generation through something like epydoc.

Some comments:

 * Sage is MATH SOFTWARE, and as such reST is not what we want -- Latex very much is what we want.  For math, Latex is by far the best choice.  We're definitely not changing the docstring format in the rest of Sage (not an option). 

 * DSage -- except for the examples -- is not specifically math software.  For dsage, latex is potentially just a nuisance.  

Just keep those points in mind when thinking about this issue.


---

Comment by was created at 2010-01-19 07:39:21

Resolution: wontfix


---

Comment by was created at 2010-01-19 07:39:21

Dsage has been deprecated.
