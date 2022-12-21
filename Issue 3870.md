# Issue 3870: bug in find_root

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-15 09:30:54

Assignee: gfurnish

CC:  jason


```
It appears that find_root give the wrong result in the following
example:

----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
sage: var('av')
av
sage: f=2.00000000000000*av - (10*sqrt(36.0000000000000*(av^4 - 2*av^3
+ av^2) + 207.360000000000*(-4*av^4 + 8*av^3 - 4*av^2) +
365*(51.8400000000000*(4*av^3 - 4*av) + 9.00000000000000*(2*av -
2*av^2)) + 133225*(2.25000000000000 - 51.8400000000000*av)) +
60.0000000000000*(av - av^2) + 5475.00000000000)/(720.000000000000*(2
- 2*av) + 131400.000000000)
sage: find_root(f,0,0.1)
0.0
sage: plot(f,0,0.1)

The last command will plot f and reveal that the root is somewhere
near to 0.05, but certainly not 0.0. No matter what I use for xtol or
rtol, I always get 0.0 as a result. Can anyone help?

Thanks!

Stan
```


I don't what is going on yet.  It may be a bug in scipy.


---

Comment by was created at 2008-08-26 09:02:11

Stan Schymanski points out that:


```

I just found out that the problem can be solved using maxima's
find_root:

sage: maxima.find_root(f,0,0.1)
.03134446907530818

It's great that sage offers multiple ways of doing the same thing. :)

Stan
```



---

Comment by anakha created at 2008-09-08 20:54:42

I don't know if that is the cause, but I don't think find_root is prepared to deal with complex numbers:


```
sage: var('av')
av
sage: f=2.00000000000000*av - (10*sqrt(36.0000000000000*(av^4 - 2*av^3
+ av^2) + 207.360000000000*(-4*av^4 + 8*av^3 - 4*av^2) +
365*(51.8400000000000*(4*av^3 - 4*av) + 9.00000000000000*(2*av -
2*av^2)) + 133225*(2.25000000000000 - 51.8400000000000*av)) +
60.0000000000000*(av - av^2) + 5475.00000000000)/(720.000000000000*(2
- 2*av) + 131400.000000000)
sage: f(0.1).n()
0.158699584011575 - 0.0475301543661689*I
```



---

Comment by anakha created at 2008-09-08 21:01:36

Continuing from the previous block:

```
sage: ff = sage.ext.fast_eval.fast_float(f, av)
sage: ff
<sage.ext.fast_eval.FastDoubleFunc object at 0x8a7a8f0>
sage: ff(0)
-0.082429990966576328
sage: ff(0.1)
nan
sage: ff(0.05)
nan
sage: ff(0.04)
0.02790669038508465
sage: find_root(f, 0, 0.04)
0.031344469075307836
```


Yeah, it is clearly not prepared.  I don't know why maxima works.


---

Comment by jason created at 2008-11-14 06:26:30

Changing keywords from "" to "scipy".


---

Comment by jason created at 2010-01-20 06:31:19

Resolution: invalid


---

Comment by jason created at 2010-01-20 06:31:19

Yep.  In the scipy documentation, it assumes the function is continuous (from context, it seems over the reals).  So this function fails, as allowed by the documentation.
