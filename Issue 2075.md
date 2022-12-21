# Issue 2075: very serious bug in modules over QQ[x] -- they shouldn't "work" (solution fix defn of echelon form over QQ[x] to raise NotImplementedError)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-06 09:58:01

Assignee: was

E.g., this is DEFINITELY WRONG -- it directly contradicts how things work over ZZ, and leads to major bugs in the free module code.   This must be changed ASAP.    There can be a method that returns the echelon form over the fraction field, but it must have a different name. 

```
sage: R.<x> = QQ[]
sage: a = matrix(R, 2, 3, [x,x^2,1,1+x, 1,x])
sage: a.echelon_form()
[                             1                              0    (-x^3 + 1)/(-x^3 - x^2 + x)]
[                             0                              1 (x^2 - x - 1)/(-x^3 - x^2 + x)]
```



---

Comment by malb created at 2008-02-06 10:27:13

It is the default behaviour of Sage to return the echelon form over fraction fields 


```
#matrix2.pyx
if not (R == ZZ or R.is_field()):
    try:
        E = self.matrix_over_field()
    except TypeError:
        raise NotImplementedError, "Echelon form not implemented over '%s'."%R
```


so this is much more general.

Note, that there is a specialised implementation for multivariate polynomials though:


```
sage: R.<x> = MPolynomialRing(QQ,1)
sage: a = matrix(R, 2, 3, [x,x^2,1,1+x, 1,x])
sage: a.echelon_form() # default as above
[                             1                              0    (-x^3 + 1)/(-x^3 - x^2 + x)]
[                             0                              1 (x^2 - x - 1)/(-x^3 - x^2 + x)]

sage: a.echelon_form('row_reduction')
[         x + 1              1              x]
[-x^3 - x^2 + x              0       -x^3 + 1]

sage: a.echelon_form('bareiss')
[          x       x + 1           1]
[          0 x^2 - x - 1     x^3 - 1]
```



---

Comment by was created at 2008-02-06 20:05:37

> It is the default behaviour of Sage to return the echelon form over fraction fields

Well that's TERRIBLE, and needs to be changed ASAP.  It is completely wrong / inconsistent.


---

Comment by mabshoff created at 2008-02-14 23:49:54

We ought to sort this out before 2.10.2 is released.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-14 23:49:54

Changing priority from major to blocker.


---

Comment by cremona created at 2008-02-17 22:29:39

There is a nice notion of normal form for matrices over F[x] for any field F which plays a similar role in the theory of modules over such rings to that played by Hermite normal form over Z.  Reduction to that form can be as useful as LLL reduction for Z-lattices.  It has various names including "weak Popov form".  It is very easy to implement, atleast naively.  I have used it successfully where F is a finte field (in an application to find rational points on curves defined over F(x)).  However when F is (for example) Q the naive implementation would be about as useful as the Euclidean algorithm for two polynomials in Q[x] -- in fact the algorithm directly generalises this too.  I mean: it is not useful since intermediate expression swell kills it performance-wise.

 What's the conclusion?   That there is no simple answer to what is the best form of normal form for matrices over rings.

 Can William explain where this is used in the free module code and what the resulting problems are?  If so I might be able to help.  But is this really a blocker for 2.20.2?


---

Comment by was created at 2008-02-17 22:58:35

YES, this is a blocker.  If you create a free module over QQ[x] with given generators, it replaces the generators by a basis coming from the rows of the "echelon form" of the matrix.  It is terrible if the elements in this echelon form aren't even in the QQ[x] span of the original matrix.


---

Attachment

Some minor issues:

 * in docstring of `_echelonize_ring` `NotImplemenetedError` should get `\code{`}
 * does `self.dense_matrix()` return `self` if it is already dense? If not the extra copy should be avoided by checking if the matrix is dense or sparse first
 * What is the status of "`#not very useful?`" is that a note to self to fix this or for the user?
 * "#This code is by Me" that should be William Stein
 * Erocal Burcin -> Burcin Erocal

Except those minor things the code looks good. Note, I didn't attempt to apply the patch yet.


---

Comment by was created at 2008-02-21 20:35:02

* in docstring of _echelonize_ring NotImplemenetedError should get \code{}

Yes.

    * does self.dense_matrix() return self if it is already dense? If not the extra copy should be avoided by checking if the matrix is dense or sparse first

Yes, it returns self. 

    * What is the status of "#not very useful?" is that a note to self to fix this or for the user?

It looks WRONG to me.  Shouldn't the second row be removed?!

    * "#This code is by Me" that should be William Stein

OK.

    * Erocal Burcin -> Burcin Erocal 

OK. 

Any chance you could make the changes you suggest above?  I have to a bunch
of other stuff today, and don't want to hold up rc1.


---

Comment by malb created at 2008-02-21 20:46:55

fixes most minor issues


---

Attachment

`sage-2075.2.patch` fixes:
 * in docstring of _echelonize_ring NotImplemenetedError should get \code{} 
 * "#This code is by Me" that should be William Stein 
 * Erocal Burcin -> Burcin Erocal

Left over:
 * "does self.dense_matrix() return self if it is already dense? If not the extra copy should be avoided by checking if the matrix is dense or sparse first  -> Yes, it returns self." So it needs no fix
 * "What is the status of "#not very useful?" is that a note to self to fix this or for the user?  ->  It looks WRONG to me. Shouldn't the second row be removed?!"
  rowred only considers constants for reduction, not very useful for most applications indeed.

I say apply. If we don't like rowred the way it is, we should (a) rename it and/or (b) fix it in another ticket.


---

Comment by mabshoff created at 2008-02-21 21:09:23

William, if you redo the patch you should also remove the last hunk since it has already been merged via some other patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-22 01:15:21

Merged sage-2075.2.patch in Sage 2.10.2.rc0.


---

Comment by mabshoff created at 2008-02-22 01:15:21

Resolution: fixed
