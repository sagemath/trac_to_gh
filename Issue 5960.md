# Issue 5960: fix bug in documentation of find_minimum_on_interval

Issue created by migration from https://trac.sagemath.org/ticket/5960

Original creator: was

Original creation time: 2009-05-02 06:31:23

Assignee: burcin

CC:  kcrisman


```
From Thomas Savitsky (on sage-devel):
> > I've noticed that the function find_minimum_on_interval makes no attempt to
> > find "the" minimum on the interval as the documentation implies, but rather
> > "a local" minimum.  I imagine this may be a source of confusion for other
> > new users as well.  Rather than treating this as a bug, may I suggest
> > changing the documentation for this function to reflect that it only finds a
> > local minimum and adding an additional function which searches for a global
> > minimum?
>
> +1  Can you provide a few examples for the docstring that illustrate this?

Do these work?

sage: h(x) =  -sin(x) - 2*sin(2*x)
sage: h.find_minimum_on_interval(0, 2*pi)
(-1.3271810224585345, 3.8298351449342838)
But there is another local minimum at h(0.8666760871050464) = -2.73581510406


sage: find_minimum_on_interval(x*(x-1)*(x+1), -2, 2)
(-0.38490017945975047, 0.57735026913115706)
The minimum on this interval is the endpoint h(-2) = 6.


sage: find_minimum_on_interval((x-2)*(x-1)*x*(x+1) - x, -2, 2)
(-0.43749999999999994, -0.49999999973911674)

but
sage: find_minimum_on_interval((x-2)*(x-1)*x*(x+1) - x, 0, 2)
(-2.6642135623730949, 1.7071067879138031)

```





---

Comment by burcin created at 2009-05-05 09:45:46

The real problem is described in #2607. I suggest we fix that instead of changing the documentation to justify this behavior.

If people think it necessary, we can create another function called .find_local_minimum() with the current behavior.

Note that I haven't looked at the code at all, and it's possible that I'm missing the point entirely.


---

Comment by kcrisman created at 2011-06-15 21:56:16

Changing keywords from "" to "sd31".


---

Comment by kcrisman created at 2011-06-15 21:56:16

This [Scipy tutorial page](http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html) should be relevant.  I will try to resolve this soon.


---

Comment by kcrisman created at 2011-06-16 00:07:08


```
sage: from scipy import optimize
sage: optimize.fminbound(h._fast_float_(x),0,6,full_output=True)
(3.8298366870225147, -1.327181022449951, 0, 10)
sage: optimize.fminbound(h._fast_float_(x),0,3,full_output=True)
(0.86667541098916612, -2.7358151040622416, 0, 9)
```


From the tutorial referenced above:

```
Finds a local minimizer 
```

so I agree this should be closed as a dup. 

Moving examples there.


---

Comment by kcrisman created at 2011-06-16 00:07:08

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-06-16 00:08:18

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-06-16 00:08:18

To release manager - please close as a duplicate of #2607.


---

Comment by jdemeyer created at 2011-06-24 14:59:30

Resolution: duplicate
