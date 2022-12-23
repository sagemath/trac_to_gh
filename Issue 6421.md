# Issue 6421: make a symbolic arctan2 function

Issue created by migration from https://trac.sagemath.org/ticket/6421

Original creator: burcin

Original creation time: 2009-06-26 12:22:36

From sage-devel:


```
> On Thu, Jun 25, 2009 at 11:31 PM, Nick
> Alexander<ncalexander@gmail.com> wrote:
> >
> > Can someone verify that this is a bug?  Any hope a fix?  (This is
> > with sage-4.0.2 on sage.math.)
> >
> > {{{
> > sage: complex_plot((x^2 + I).sqrt().real_part(), (-2, 2), (-2, 2))
> > ---------------------------------------------------------------------------
> ...
> > RuntimeError: cannot find SFunction in table
> > }}}
> 
> It seems, its not just complex_plot issue. It is happening for other
> plots. For example,  the following works fine in 3.4 but fails with
> the same error in 4.0.2
> -----
> sage: x,y=var('x,y'); plot3d( log(x+I*y).imag(), (x,-2,2), (y,-2,2))
> ...
> RuntimeError: cannot find SFunction in table
> -----

sage: %debug
> /home/burcin/sage/sage-4.0.2.rc0/expression.pyx(3115)sage.symbolic.expression.Expression.operator
> (sage/symbolic/expression.cpp:15268)()

ipdb> u
> /home/burcin/sage/sage-4.0.2.rc0/local/lib/python2.5/site-packages/sage/symbolic/expression_conversions.py(206)__call__()
    205 
--> 206         operator = ex.operator()
    207         if operator is None:

ipdb> print ex
arctan2(real_part(y) + imag_part(x), real_part(x) - imag_part(y))


Both of these fail because Sage doesn't define a symbolic arctan2
function. There is instead a simple wrapper around arctan in
sage/functions/trig.py:

sage: arctan2(x,y)
arctan(x/y)

```


It's possible that this worked on 4.0, and I broke it with #6244.





---

Attachment


---

Comment by kcrisman created at 2009-06-26 17:38:35

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-06-26 17:38:35

Set assignee to kcrisman.


---

Comment by kcrisman created at 2009-06-26 17:38:35

Okay, this seems to fix everything and passes tests on trig.py and symbolic/expression.py and /function.py.    I made the function consistent with Maxima, Pynac, and Python math.  Only issue, which I would really appreciate some insight on but should not prevent it from going in, is the following:

```
sage: latex(arctan2)
\arctan
sage: var('y')
y
sage: latex(arctan2(y,x))
\mbox{atan2}\left(y,x\right)
```

Of course, this doesn't fix the question about plotting, but now the failure on that will be clearer.


---

Attachment

minor doctest fixes in `sage.symbolic.random_tests`


---

Comment by burcin created at 2009-06-27 16:10:22

Looks good, thanks for this.

I added a small patch with doctest fixes in `sage/symbolic/random_tests.py`.


---

Comment by rlm created at 2009-07-04 01:07:11

Resolution: fixed


---

Comment by bascorp2 created at 2010-05-26 08:42:46

[mickey mouse pictures](http://like-search.info/)
