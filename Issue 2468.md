# Issue 2468: inverting a non-invertible matrix over RDF returns weird results

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-03-11 02:46:35

Assignee: was

Check this out:


```
sage: A = Matrix(RDF, [[1, 0], [0, 0]])
sage: A.inverse()

[nan nan]
[nan inf]
```


This is, to say the least, weird.  This should throw a ZeroDivisionError instead.



---

Comment by dfdeshom created at 2008-03-13 03:19:03

I don't see why a ZeroDivisionError should be thrown. Note that Matlab doesn't complain either:

```
>> a = [1 0; 0 0];
>> inv(a)
Warning: Matrix is singular to working precision.

ans =

   Inf   Inf
   Inf   Inf
```



---

Comment by was created at 2008-03-13 03:33:20

I agree with dfdeshom.  The relevant code that does the inverse is


```
result_invert = gsl_linalg_LU_invert(self._LU,self._p,M._matrix)
```


Note that 1/RDF(0) also doesn't give ZeroDivisionError:

```
sage: 1/RDF(0)
inf
```


So I think that (1) this ticket should be resolved with a patch
that simply adds a doctest with this nan/inf behavior and says
what the deal is in the docs.


---

Comment by dfdeshom created at 2008-03-14 05:28:36

I've added a patch that, in addition:

 * adds some doctests to this file
 * corrects a bug where subtraction of RDF matrices would always throw an error


---

Attachment

correct a small typo in patch


---

Comment by mabshoff created at 2008-03-18 02:52:50

Replying to [comment:4 dfdeshom]:
> I've added a patch that, in addition:
> 
>  * adds some doctests to this file
>  * corrects a bug where subtraction of RDF matrices would always throw an error

Very nice! Before the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.4, Release Date: 2008-03-16                      |
| Type notebook() for the GUI, and license() for information.        |
sage: m = Matrix(RDF, [[1,2],[3,4]])
sage: n=m^2
sage: n+m

[ 8.0 12.0]
[18.0 26.0]
sage: n-m
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-2.11.alpha0/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-2.11.alpha0/element.pyx in sage.structure.element.ModuleElement.__sub__()

/scratch/mabshoff/release-cycle/sage-2.11.alpha0/coerce.pxi in sage.structure.element._sub_c()

/scratch/mabshoff/release-cycle/sage-2.11.alpha0/matrix_real_double_dense.pyx in sage.matrix.matrix_real_double_dense.Matrix_real_double_dense._sub_c_impl()

<type 'exceptions.ValueError'>: GSL routine had an error
sage:
```

I will add a doctest patch for this bug since it is currently missing.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-18 03:22:21

Ok, I now figured out that you also added a doctest for the bug you fixed. So disregard my comment about adding a doctest.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-18 03:22:49

Merged in Sage 2.11.alpha0


---

Comment by mabshoff created at 2008-03-18 03:22:49

Resolution: fixed
