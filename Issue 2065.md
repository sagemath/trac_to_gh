# Issue 2065: tidying up documentation for dsage

Issue created by migration from https://trac.sagemath.org/ticket/2065

Original creator: ljpk

Original creation time: 2008-02-05 22:22:46

Assignee: tba

In the Reference Manual, section 16.2, the phrase "DOTSAGE/dsage/server.log" is wmis-formatted thrice.

It would also be helpful in my opinion if the title of this section included the phrase "dsage" (or "DSage"), as this is the name of the package and it would make it easier to search for in the page.

Also, in

`f = DistributedFactor(P, number, name='my_factor')`

the P should be a D, as D is the label used for DSage here.


---

Comment by jhpalmieri created at 2010-01-19 22:18:36

Resolution: wontfix


---

Comment by jhpalmieri created at 2010-01-19 22:18:36

Because we've removed dsage (#7975), I think we can close this.
