# Issue 5635: plot method on lattice polytopes gives something ridiculous

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-29 20:25:02

Assignee: mhansen

CC:  sage-combinat

The plot method on an object should return either a 2d plot or raise NotImplementedError (or not be defined).  On LatticePolytope's it returns a 3d Tachyon object.


```
sage: p = LatticePolytope(random_matrix(ZZ, 3,6, x=7)).plot()
sage: type(p)
<class 'sage.plot.tachyon.Tachyon'>
```



---

Attachment

The patch removes plot() method and fixes the documentation. I also changed show() to show3d(), which shows the plot without axes.


---

Comment by mabshoff created at 2009-04-01 01:02:10

Resolution: fixed


---

Comment by mabshoff created at 2009-04-01 01:02:10

Merged in Sage 3.4.1.rc0.

Cheers,

Michael
