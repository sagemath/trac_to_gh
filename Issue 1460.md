# Issue 1460: bug in float( ... ) conversion in calculus

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-11 16:55:44

Assignee: was


```
On Dec 11, 2007 8:39 AM, Joel B. Mohler <joel`@`kiwistrawberry.us> wrote:
>
> Hi,
>
> I've noticed a very recent regression -- it worked 2 months ago.
>
> sage: t=var('t')
> sage: f=t*cos(0)
> sage: float(f(1))
> 1.0
> sage: f=t*sin(0)
> sage: float(f(1))
> Traceback...
> <type 'exceptions.TypeError'>: float() argument must be a string or a number
>
> --

It is actually hard to decide how to fix this.   This is a result of
several significant fixes
and optimizations recently.  What is happening is that for t*sin(0)
the simplified
form is 0, so (t*sin(0)).variables() is [].

sage: t=var('t')
sage: f = t*cos(0)
sage: f.variables()
(t,)
sage: g = t*sin(0)
sage: g.variables()
()
sage: float(f(1))
1.0
sage: float(g(t=1))
0.0

Both f(1) and g(1) are formal products.  However:

sage: g(1)._operands
[t, 0]
sage: f(1)._operands
[1, 1]

Notice the [t, 0].

One possible solution would be to call simplify before
doing float(...) -- but that could greatly slow symbolic calculus
down in some cases.   Another possibility would be to change
the definition of variables() to return all variables, even the ones
that are simplified away:

sage: (x - x).variables()   # fake
(x,)

That would be very confusing.

A third possibility would be to make implicit calling use variables
in the unsimplified expression if the simplified expression has
no variables.  This would cleanly deal with your case above.

Thoughts?
```



---

Attachment


---

Comment by was created at 2007-12-12 00:44:25

The attached patch also greatly improves doctests for the relevant functions.


---

Attachment

Looks good to me.  One of the doctests failed on my machine due to numerical noise; I attached a trivial doctest patch to fix it.  After my patch, all doctests pass in sage/calculus/ and sage/rings/.


---

Comment by mabshoff created at 2007-12-15 04:45:54

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 04:45:54

Resolution: fixed
