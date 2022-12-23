# Issue 1302: bug in laurent_series integration

Issue created by migration from https://trac.sagemath.org/ticket/1302

Original creator: was

Original creation time: 2007-11-28 19:05:46

Assignee: somebody


```
On Nov 28, 2007 10:43 AM, Jennifer S. Balakrishnan <> wrote:
> I'm trying to integrate a list of Laurent series, and it seems that
> once the list has more than 4 elements, Sage gets upset:

The problem is:

sage: A.<t> = LaurentSeriesRing(QQ)
sage: (-2*t^(-4) + O(t^8)).integral()
Traceback (most recent call last):
...
IndexError: list index out of range

This is because of  this code in rings/laurent_series_ring_element.pyx not
being coded correctly around line 880:
        if n < 0:
            v = [a[i]/(n+i+1) for i in range(-1-n)] + [0]
        else:
            v = []
        v += [a[i]/(n+i+1) for i in range(max(-n,0), len(a))]
	try:

So you should fix that and submit a patch :-).

William



> 
> sage: A.<t> = LaurentSeriesRing(QQ)
> sage: B = [-2*t^4 + O(t^16), -2*t^2 + O(t^14), -2 + O(t^12), -2*t^-2 +
> O(t^10), -2*t^-4 + O(t^8), -2*t^-6 + O(t^6)]
> sage: for i in range(6):
> ....:     B[i] = integral(B[i])
> ....:
> ---------------------------------------------------------------------------
> <type 'exceptions.IndexError'>            Traceback (most recent call last)
> 
> /home/jen/<ipython console> in <module>()
> 
> /home/jen/sage-2.8.13-use_this_on_sage_dot_math-x86_64-Linux/local/lib/python2.5/site-packages/sage/misc/functional.py
> in integral(x, *args, **kwds)
>     449     """
>     450     if hasattr(x, 'integral'):
> --> 451         return x.integral(*args, **kwds)
>     452     else:
>     453         from sage.calculus.calculus import SR
> 
> /home/jen/laurent_series_ring_element.pyx in
> sage.rings.laurent_series_ring_element.LaurentSeries.integral()
> 
> <type 'exceptions.IndexError'>: list index out of range
> sage: B
> 
> [-2/5*t^5 + O(t^17),
>  -2/3*t^3 + O(t^15),
>  -2*t + O(t^13),
>  2*t^-1 + O(t^11),
>  -2*t^-4 + O(t^8),        <================== stopped integrating here
>  -2*t^-6 + O(t^6)]
> 
> What's going on?
> 
> Jen
> 
```



---

Comment by mabshoff created at 2007-12-26 03:14:15

Certainly Bug Day material.


---

Comment by rishi created at 2008-01-02 22:38:19

Changing assignee from somebody to rishi.


---

Comment by rishi created at 2008-01-02 22:38:19

Changing status from new to assigned.


---

Comment by rishi created at 2008-01-03 01:30:43

IndexError occurs when the highest power in the Laurent series is less than -2. The two lines in the patch add appropriate number of zero coefficients so that this does not happen. I consider this a bandaid solution, but at least it works.


---

Attachment


---

Comment by rishi created at 2008-01-04 08:39:27

I changed the patch. This is much better than previous solution.


---

Comment by robertwb created at 2008-01-04 22:14:43

Yep, works great.


---

Comment by mabshoff created at 2008-01-04 22:26:26

We should add doctests to verify that the patch works. I am still willing to merge this patch for 2.9.2, but then I would open a new ticket to add doctests to test this.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-01-05 02:32:16

Merged in 2.9.2.rc1.


---

Comment by mabshoff created at 2008-01-05 02:32:16

Resolution: fixed
