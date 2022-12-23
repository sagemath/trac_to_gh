# Issue 2451: plotting -- contour_plot and plot_vector_field are REALLY SLOW but it's easy to get a million times speedup

Issue created by migration from https://trac.sagemath.org/ticket/2451

Original creator: was

Original creation time: 2008-03-10 01:06:45

Assignee: was

There are two problems:

1. neither use _fast_float

2. Even worse, they don't coerce their endpoints to floats.  This is a killer.

To illustrate:

```
var('x,y')
sage: time contour_plot(x^2+y^2, (-pi,pi),(-pi,pi))
takes forever
sage: time contour_plot(x^2+y^2, (-float(pi),float(pi)),(-float(pi),float(pi)))
takes forever
sage: f = (x^2+y^2)._fast_float_('x','y')
sage: time contour_plot(f, (-float(pi),float(pi)),(-float(pi),float(pi)))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
```



---

Comment by was created at 2008-03-10 05:13:13

Changing status from new to assigned.


---

Comment by was created at 2008-03-10 06:02:40

part 1.  there may be a part 2...


---

Attachment


---

Comment by gfurnish created at 2008-03-10 06:40:01

Positive review pending patch of redundant line 4239.


---

Comment by mabshoff created at 2008-03-10 07:13:08

I did remove the offending line after merging the patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-10 07:13:25

Merged in Sage 2.10.3.rc4


---

Comment by mabshoff created at 2008-03-10 07:13:25

Resolution: fixed


---

Comment by edrex created at 2008-03-10 07:50:00

works as advertised in my limited testing. 

gfurnish indicates that line 4239 is redundant


---

Comment by edrex created at 2008-03-10 07:50:54

oops, missed previous comments
