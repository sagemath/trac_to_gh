# Issue 4030: Vectors of callable things should be callable

Issue created by migration from https://trac.sagemath.org/ticket/4030

Original creator: jwmerrill

Original creation time: 2008-09-01 05:13:17

Assignee: tbd

The motivation here is being able to evaluate the gradient of a function at a point.


```
The desired behavior is
    sage: x, y = var('x, y')
    sage: f = x^2 + y^2
    sage: g = f.gradient()
    sage: g(x=3,y=2)
    (6,4)

Currently, however
    sage: g(x=3,y=2)
    Traceback (most recent call last):
    ...
    TypeError:
    'sage.modules.free_module_element.FreeModuleElement_generic_dense'
    object is not callable

Calls should also work for a vector of callable symbolic expressions.
Note that the gradient part will only work once #2547 is applied.
    sage: f(x,y) = x^2 + y^2
    sage: g = f.gradient()
    sage: g(3,2)
    (6,4)
    sage: g(y=2,x=3)
    (6,4)
}}


---

Comment by jwmerrill created at 2008-09-01 05:23:47

Changing component from algebra to calculus.


---

Attachment

The attached patch solves all the cases above except the last, which returns


```
sage: g(y=2,x=3)
Traceback (most recent call last):
...
TypeError: __call__() got an unexpected keyword argument 'y'
```


Not sure what the deal is with that.

This patch should only be applied after #2547.


---

Comment by jwmerrill created at 2008-09-01 05:23:47

Changing assignee from tbd to jwmerrill.


---

Comment by jwmerrill created at 2008-09-01 06:30:14

Changing type from defect to enhancement.


---

Comment by jwmerrill created at 2008-09-01 06:30:14

After applying #4031, the patch here gives the desired behavior.


---

Comment by mabshoff created at 2008-09-01 12:25:00

Jason,

please assign a milestone to new tickets. The next release is usually the right choice.

Cheers,

Michael


---

Comment by mhansen created at 2008-09-01 22:50:14

Looks good to me. Apply only after #4031.


---

Comment by jwmerrill created at 2008-09-01 23:19:03

Just to be clear, both #2547 and #4031 should be applied before this patch.  The functionality doesn't depend on #2547, but the doctests do.


---

Comment by mabshoff created at 2008-09-02 10:14:56

Merged in Sage 3.1.2.alpha4


---

Comment by mabshoff created at 2008-09-02 10:14:56

Resolution: fixed
