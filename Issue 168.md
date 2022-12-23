# Issue 168: Plot bounds ignored when frame=True

Issue created by migration from https://trac.sagemath.org/ticket/168

Original creator: nbruin

Original creation time: 2006-11-08 21:55:30

Assignee: boothby

When I do:


```
  show(plot(lambda x: 1/x,-1,1),frame=True,ymin=-3,ymax=3)
```


the ymin and ymax bounds get ignored. Without frame=True, the plot works properly


---

Comment by was created at 2007-01-17 21:05:05

Alex C sent me a patch that fixes this problem.


---

Comment by was created at 2007-01-17 21:05:05

Resolution: fixed
