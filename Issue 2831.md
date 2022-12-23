# Issue 2831: plot taking a very, very long time

Issue created by migration from https://trac.sagemath.org/ticket/2831

Original creator: jsp

Original creation time: 2008-04-06 16:40:19

Assignee: was

In the notebook of sage-2.11:

time plot(1.0 - x * floor(1/x), (x,0.00001,1.0)

CPU time: 143.77 s,  Wall time: 1660.39 s

with a correct image.

Maple is almost immediate.


Even worse:

time plot(1.0 - x * floor(1/x), (x, 0.0, 1.0), plot_points=1000)

        	
CPU time: 244.71 s,  Wall time: 5155.23 s

Jaap


---

Comment by mabshoff created at 2008-04-06 16:57:29

The problem is that "floor(1/x)" calls maxima. If you drop it the
whole thing takes about a second. 

Cheers,

Michael


---

Comment by was created at 2008-04-06 19:08:11

The problem is that there is a bug when deciding to use fast float, since the above
plot takes 0.04 seconds to draw when one calls fast_float explicitly:

```
sage: time plot((1.0 - x * floor(1/x))._fast_float_(x), (x,0.00001,1.0))
CPU times: user 0.03 s, sys: 0.01 s, total: 0.04 s
```



 -- William


---

Attachment


---

Comment by jsp created at 2008-04-06 19:57:14

This is an *absurdly* good speedup!

          	

CPU time: 1.01 s,  Wall time: 3.75 s

compared with:

CPU time: 244.71 s, Wall time: 5155.23 s


---

Comment by mabshoff created at 2008-04-06 20:01:38

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-06 20:01:38

Resolution: fixed


---

Comment by mabshoff created at 2008-04-06 21:14:10

Ok, somebody didn't doctest properly:

```
sage -t -long devel/sage/sage/functions/special.py          
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/tmp/special.py", line 905:
    sage: P = plot(inverse_jacobi('sn', x, 0.5), 0, 1, plot_points=20)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[5]>", line 1, in <module>
        P = plot(inverse_jacobi('sn', x, RealNumber('0.5')), Integer(0), Integer(1), plot_points=Integer(20))###line 905:
    sage: P = plot(inverse_jacobi('sn', x, 0.5), 0, 1, plot_points=20)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 3553, in __call__
        G = funcs.plot(*args, **kwds)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 915, in plot
        f = F._fast_float_(param)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 3814, in _fast_float_
        raise NotImplementedError # return lambda x: float(self(x))
    NotImplementedError
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_13
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.alpha2/tmp/.doctest_special.py
         [4.7 s]
```


Cheers,

Michael


---

Attachment

Replying to [comment:6 mabshoff]:
> Ok, somebody didn't doctest properly:

You may call me names is you like :-)!

Jaap


---

Comment by mabshoff created at 2008-04-06 21:41:19

sage-2831_part2.patch add a fallback to lambda in case _fast_float fails. It also fixes the doctest issue. Positive review and merged in Sage 3.0.alpha2

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-06 21:42:52

Replying to [comment:7 jsp]:
> Replying to [comment:6 mabshoff]:
> > Ok, somebody didn't doctest properly:
> 
> You may call me names is you like :-)!

Sure :)

I would prefer if people stated what they actually doctested [i.e. which version of Sage with what patches applied on what platforms] so I would check myself in case somebody didn't do as much coverage as I would prefer. So you can always blame me too.

> Jaap
> 

Cheers,

Michael
