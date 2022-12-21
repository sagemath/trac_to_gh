# Issue 1215: Sage misparses maxima integration result

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-20 13:45:56

Assignee: was

LordRuslanNightmare reported:

```
> As far as i know, length of curve, defined as
> f(x)
> from a to b (a <= x <= b) is
> L = integral from a to b of sqrt(1 + df(x)^2)dx
> where df(x) is diff(f,x)
> 
> for f(x) = y = x^2 , a=0, b=2 it should be
> df(x)=2x
> sqrt(17) + ln|4 + sqrt(17)|/4
> 
> which is 4.647
> 
> however, SAGE thinks differently. For this code:
> 
> y = x^2
> dy = diff(y,x)
> z = integral(sqrt(1 + dy^2), x, 0, 2)
> print(z)
> print(RR(z))
> 
> output is
> 
>                                  4 sqrt(17) + 4
>                                  --------------
>                                        4
> 5.12310562561766
> 
> Am i doing something wrong?

No. Maxima gives

(%i2) integrate (sqrt(1+4*x^2), x, 0, 2);
                             asinh(4) + 4 sqrt(17)
(%o2)                        ---------------------
                                       4

so possibly SAGE is not parsing that properly? That's the only thing I can think
of. The following just confirms your computation:

sage: sqrt(1 + (2*x)^2).nintegrate(x, 0, 2)
(4.6467837624329427, 1.5663635326179329e-09, 21, 0)
sage: integral(sqrt(1 + (2*x)^2), x, 0, 2)
(4 + 4*sqrt(17))/4
sage: RR(integral(sqrt(1 + (2*x)^2), x, 0, 2))
5.12310562561766
```


Cheers,

Michael


---

Comment by was created at 2007-11-20 15:16:54

Changing priority from major to blocker.


---

Attachment


---

Comment by mabshoff created at 2007-11-20 15:57:47

fixed: Merged in 2.8.13.rc1.


---

Comment by mabshoff created at 2007-11-20 15:57:47

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-20 15:57:47

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-11-20 16:18:42

Resolution: fixed
