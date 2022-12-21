# Issue 36: Bug in display2d for maxima interface

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:29:29

Assignee: somebody


```
   sage: maxima.de_solve('diff(w,x,2) + 2*diff(w,x)+2*w = 0', ['x','w'], [0,1,2])
w = %e^-x*(3*sin(x) + cos(x))
sage: maxima.de_solve('diff(w,x,2) + 2*diff(w,x)+2*w = 0', ['x','w'], [0,1,2]).display2d()
(output looks funny)
```





---

Comment by was created at 2007-01-13 02:08:31

Works fine now.

```
sage: print maxima.de_solve('diff(w,x,2) + 2*diff(w,x)+2*w = 0', ['x','w'], [0,1,2])
sage: print maxima.de_solve('diff(w,x,2) + 2*diff(w,x)+2*w = 0', ['x','w'], [0,1,2]).display2d()
w = %e^-x*(3*sin(x) + cos(x))
			       - x
       			 w = %e	   (3 sin(x) + cos(x))

```



---

Comment by was created at 2007-01-13 02:08:31

Resolution: fixed
