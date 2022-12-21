# Issue 3864: [with patch, needs review] Bug exposed by p-adic matrices

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-08-15 02:35:06

Assignee: craigcitro

David Loeffler ran into the following bug, and reported it on sage-support:


```
sage: M = MatrixSpace(pAdicField(3,100), 2)
sage: m1 = M([1,0,0,90]) - (1+O(3^100)) * M(1) 
sage: m1.left_kernel()
---------------------------------------------------------------------------
PrecisionError                            Traceback (most recent call last)

/Users/craigcitro/<ipython console> in <module>()

/Users/craigcitro/matrix2.pyx in sage.matrix.matrix2.Matrix.left_kernel (sage/matrix/matrix2.c:8531)()

/Users/craigcitro/matrix2.pyx in sage.matrix.matrix2.Matrix.echelon_form (sage/matrix/matrix2.c:15904)()

/Users/craigcitro/matrix2.pyx in sage.matrix.matrix2.Matrix.echelonize (sage/matrix/matrix2.c:15596)()

/Users/craigcitro/matrix2.pyx in sage.matrix.matrix2.Matrix._echelon_in_place_classical (sage/matrix/matrix2.c:16358)()

/Users/craigcitro/padic_capped_relative_element.pyx in sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement.__invert__ (sage/rings/padics/padic_capped_relative_element.c:9168)()

PrecisionError: cannot divide by something indistinguishable from zero.
```


One fix is attached -- namely, add another call to the `__nonzero__` method for `pAdicCappedRelativeElement`s that will fix this. I could be convinced that there is another problem here, i.e. that another function should have called `self._normalize()` before and hasn't.

I'm tagging this for 3.1, since it's small, but I'm happy to see it move into 3.1.1 if it really causes any trouble. It seems like it should only cause slowdowns, never bugs. Also, given that it's in p-adics code, it's unlikely to cause doctest failures ... since there are so few doctests! :)


---

Attachment


---

Comment by mabshoff created at 2008-08-15 07:29:15

Merged in Sage 3.1.rc0


---

Comment by mabshoff created at 2008-08-15 07:29:15

Resolution: fixed
