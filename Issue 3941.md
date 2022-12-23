# Issue 3941: threading diff over lists to give the jacobian

Issue created by migration from https://trac.sagemath.org/ticket/3941

Original creator: jason

Original creation time: 2008-08-24 05:13:27

Assignee: gfurnish

In MMA, you can thread the derivative over lists of variables and functions to compute the Jacobian.  Here's a routine that wraps the sage diff function to do it.  


```
def diff(f,*args):
    if isinstance(f, (list, tuple)):
        return [diff(component,*args) for component in f]
    else:
        if isinstance(args[0], (list, tuple)):
            return [diff(f,variable) for variable in args[0]]
        else:
            return sage.all.diff(f,*args)
```


and the results:


```
sage: var('a,b,c,d,x,y')
sage: diff((a*x+b*y,c*x+d*y),(x,y))
[[a, b], [c, d]]
```


well, so the result is not really a matrix, but rather a nested list that could be indexed like a matrix or turned into a matrix in the above case.


We could write the above even more simply if we had an outer product operator: 

outer_product(diff,f,vars), where f and vars were lists.


---

Comment by jwmerrill created at 2008-08-31 15:06:45

See also #2547, asking for a symbolic gradient and hessian.


---

Comment by jason created at 2008-11-14 06:24:25

Changing status from new to assigned.


---

Comment by jason created at 2008-11-14 06:24:25

Changing assignee from gfurnish to jason.


---

Comment by jason created at 2009-01-14 07:37:47

See http://groups.google.com/group/sage-devel/browse_thread/thread/666b18d9ea182f13 for an updated mydiff function and discussion.


---

Comment by was created at 2009-01-14 16:47:34

Why not have a function .jacobian to give the jacobian?


---

Comment by AlexGhitza created at 2009-01-22 18:22:05

Changing type from defect to enhancement.


---

Comment by jason created at 2009-02-12 22:44:16

What about functions with codomain R<sup>n</sup> where n>1?  If these are represented via a list, tuple, or vector, the code works from above (well, let's add handling of vectors with the following:


```
def diff(f, *args):
    if isinstance(f, (list, tuple)) or sage.structure.element.is_Vector(f):
        return [diff(component, *args) for component in f]
    else:
        if isinstance(args[0], (list, tuple)) or is_Vector(args[0]):
            return [diff(f, variable) for variable in args[0]]
        else:
            return sage.all.diff(f, *args)
```


This wouldn't work with a `.jacobian` method---where would we put the method?


---

Comment by jason created at 2009-02-13 05:50:22

#5253 makes this less needed, but I still think it would be nice to have good syntax for this sort of thing using the diff function.


---

Comment by kcrisman created at 2010-05-26 20:09:39

Does the new functionality that

```
f(x,y)=3*sin(x)-2*cos(y)-x*y
f.diff(2)
```

works change anything on this ticket?  Just throwing it out there, it may be irrelevant.
