# Issue 5017: graph.automorphism_group(translation=True) gives error in 3.2.3

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2009-01-18 18:29:03

Assignee: rlm



```
Nikos Apostolakis wrote:
> > The "translation=True" flag does not work after upgrading to sage 3.2.3
> > I am not sure when this behaviour was introduced.  In version 2.10.2 it
> > works fine, unfortunately I don't have a more recent old sage to check.
> > 
> >   sage: foo = Graph()
> >   sage: foo.add_edges([(0,1,1),(1,2,2), (2,3,3)])
> >   sage: foo.automorphism_group(translation=True)


This worked in sage-3.1.2 and before, giving
  (Permutation Group with generators [(1,2)(3,4)], {0: 4, 1: 1, 2: 2, 3: 3})

In sage-3.2.1 and later this fails.

Jaap
```




---

Attachment


---

Comment by jsp created at 2009-01-18 21:24:47

After the patch:



```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.3, Release Date: 2009-01-05                       |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: foo = Graph()

sage:  sage: foo.add_edges([(0,1,1),(1,2,2), (2,3,3)])

sage:  sage: foo.automorphism_group(translation=True)
 (Permutation Group with generators [(1,2)(3,4)], {0: 4, 1: 1, 2: 2, 3: 3})

sage: 

```



looking at the code, patch seems ok.

Jaap


---

Comment by jsp created at 2009-01-18 23:07:58

I can reproduce the error in sage-3.1.4 FWIW

Jaap


---

Comment by mabshoff created at 2009-01-19 04:15:43

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 04:15:43

Merged in Sage 3.3.alpha0
