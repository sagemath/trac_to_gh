# Issue 2040: 2d graphics -- problems with axes_labels options

Issue created by migration from https://trac.sagemath.org/ticket/2040

Original creator: was

Original creation time: 2008-02-03 22:37:57

Assignee: was

1. 2d graphics -- the show method of a 2d graphics option *must* document e.g., the axes_labels option, but doesn't, making it useless


```
sage: P = point((0,0))
sage: P.show?
```


nothing about axes labels.

2. The axes labels appear in the notebook but not from the command line.  Try
this in the notebook (good), and command line (bad):

```
sage: plot(sin,0,1).show(axes_labels=['x','Pr(x)'])
```





---

Comment by jhpalmieri created at 2008-05-13 21:52:40

add axes_labels to documentation to show


---

Attachment

I've attached a patch for point 1.  I don't know anything about point 2.


---

Attachment

show axes_labels when called from command line


---

Comment by jhpalmieri created at 2008-05-13 21:58:44

Actually, I have a patch for point 2, also.


---

Comment by mhampton created at 2008-05-24 20:40:34

Changing keywords from "" to "show, axes_labels".


---

Comment by mhampton created at 2008-05-24 20:40:34

This is a simple patch that seems to work as it should.  I tested it on 3.0.2.rc3, both the show and save changes; saving to png and pdf.  plot.py passes all tests.   

I think it would be nice to add this to the plot command as well, but that can be another ticket if others agree.

-Marshall Hampton


---

Comment by mabshoff created at 2008-05-25 04:10:38

Merged in Sage 3.0.3.alpha0. Please post Mercurial patches and not diff the next time. The patches have been check in with credit to John.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-25 04:10:38

Resolution: fixed
