# Issue 7155: Allow solving of inequalities

Issue created by migration from https://trac.sagemath.org/ticket/7155

Original creator: kcrisman

Original creation time: 2009-10-08 14:06:10

CC:  jason jhpalmieri burcin

Keywords: solve, inequality, Maxima

From a Maxima FAQ:

```
(%i1) load(fourier_elim)$

(%i2) fourier_elim([abs(x - abs(5-x)) < 1],[x]);
(%o2)                          [2<x,x<3]

(%i3) fourier_elim([x + y < 1, x - y > 9],[x,y]);
(%o3)                     [y+9<x,x<1-y,y<-4]

(%i4) fourier_elim([max(-x,x) < 7 * x + 1],[x]);
(%o4)                           [-1/8<x]
```

From pre-release codebase:

```
 (%i79) to_poly_solve((x-1)*(x-6) < 0,x);
 (%o79) %union([1 < x,x < 6])

 (%i80) to_poly_solve(min(x,1) < max(-5,x),x);
 (%o80) %union([1 < x],[x < -5])

 (%i81) to_poly_solve(min(x,1) # max(x,4),x);
 (%o81) %union([1 < x,x < 4],[4 < x],[x = 1],[x < 1],[x = 4])

 (%i82)  to_poly_solve((x+1)/(x-1) < 4,x);
 (%o82) %union([5/3 < x],[x < 1])
```

So it should not be too hard to wrap this, checking input/output for < or > or something.   This is one of those basic things people want, but which we assume it's too hard to write from scratch (which it probably is!).


---

Comment by kcrisman created at 2009-10-28 00:54:58

This is now a duplicate of #7325, which already has a first patch, so I am closing this ticket.


---

Comment by kcrisman created at 2009-10-28 00:54:58

Resolution: duplicate


---

Comment by mvngu created at 2009-10-28 12:31:32

Replying to [comment:1 kcrisman]:
> This is now a duplicate of #7325, which already has a first patch, so I am closing this ticket.

kcrisman, please don't close tickets. That's the job of the release manager.  See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for conventions on closing tickets.
