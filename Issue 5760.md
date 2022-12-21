# Issue 5760: bring doctest coverage of plot3d/shapes.pyx to 100%

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-04-11 19:04:00

Assignee: mabshoff


```
plot/plot3d/shapes.pyx: 16% (5 of 31)
```



---

Attachment


---

Comment by was created at 2009-04-13 14:30:56

Wow, not only does this greatly improve the coverage, it appears that several subtle bugs were fixed in 3d plotting along the way!

This example looks awesome, by the way.  It's a spotted icosahedron:

show(sphere(opacity=.8,size=1.31) + icosahedron(size=2,opacity=.5,color='red'), frame=False)


---

Comment by mabshoff created at 2009-04-13 19:56:21

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 19:56:21

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
