# Issue 3911: come up with a good framework for citing stuff in docstrings

Issue created by migration from https://trac.sagemath.org/ticket/3911

Original creator: malb

Original creation time: 2008-08-20 14:29:10

Assignee: tba

the framework should allow to generate a bibliography etc. while not reinventing the wheel: BibTeX? By citing in docstrings I mean stuff like this:

```
INPUT:
   foo -- bar (as described in [BCDT]

REFERENCES:
[BCDT] Breuil, Conrad, Diamond, Taylor, "Modularity ...."
```



---

Comment by malb created at 2009-04-27 13:01:54

This is fixed thanks to Sphinx and ReST which has native support for this.


---

Comment by malb created at 2009-04-27 13:01:54

Resolution: fixed


---

Comment by mabshoff created at 2009-04-27 15:39:41

Well, it should be documented in some way how we do things things. If such documentation exists a link from the ticket would be nice.

Cheers,

Michael


---

Comment by malb created at 2009-04-27 15:56:35

It is a standard feature of ReST, see: http://sphinx.pocoo.org/rest.html#citations


---

Comment by mabshoff created at 2009-04-27 15:58:12

Replying to [comment:3 malb]:
> It is a standard feature of ReST, see: http://sphinx.pocoo.org/rest.html#citations

I now that. I meant in Sage's documentation so that documentation writes in Sage will use it :).

Cheers,

Michael
