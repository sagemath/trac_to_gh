# Issue 8824: Make it so that numpy datatypes are integrated into the coercion model

Issue created by migration from https://trac.sagemath.org/ticket/8824

Original creator: jason

Original creation time: 2010-04-29 15:36:37

Assignee: robertwb

From sage-devel: http://groups.google.com/group/sage-devel/browse_frm/thread/221f569eaba874de

>   Hello:
> >   Tracking a weird bug I've discovered the following:
> >   For a symbolic variable x and a numpy.float64 y, the code 'x<y' evals
> > to a Symbolic expression, while 'y<x' evals to a numpy.bool.
> >   I'm afraid I'm stacked, as it is the responsability of the method
> > numpy.float64.__lt__, and I can't assign it to a custom method, for example.
> >   Any idea what can I try so that 'y<x' evals to a Symbolic Expression
> > too (if you agree this should be the result)?
Sage should set the __array_priority__ attribute to something very
high in its base class(es), then let the coercion model decide how
NumPy objects should be handled (in this case, coerce to RDF or CDF).

NumPy uses the custom convention that __array_priority__ decides which
operand gets to handle the operation.

Example:

```
import numpy as np

class MagicOne:
    __array_priority__ = 1000
    def __cmp__(self, other):
        print 'MagicOne has control'
        return cmp(1, other)

one = MagicOne()

print one < np.float64(63.3)
print np.float64(63.3) < one
```

This prints

```
MagicOne has control
True
MagicOne has control
False
```



---

Comment by dagss created at 2010-04-29 18:51:53

This might be a fitting place to record a wish: If Sage decides to do something with NumPy arrays (not just scalars), I think the behaviour should be something like:


```
sage: M = random_matrix(RDF, 4, 3)
sage: A = np.random.normal(size=(12, 10, 4)).astype(np.float32)
sage: type(A * M)
<type np.ndarray...>
sage: (A * M).shape
(12, 10, 3)
sage: (A * M).dtype
float64
```

I.e. let matrices be operators acting on data, operating along the vectors along the rightmost dimension (matrix on right) or leftmost dimension (matrix on left).

In particular, I think it would be very bad to coerce NumPy arrays to Sage matrices!
