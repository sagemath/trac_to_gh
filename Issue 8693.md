# Issue 8693: QuadraticForm::basis_of_short_vectors may not return an actual basis.

Issue created by migration from Trac.

Original creator: afiori

Original creation time: 2010-04-15 18:51:18

Assignee: justin

CC:  lorenz

Keywords: quadratic forms, basis, automorphisms

QuadraticForm::basis_of_short_vectors does not actually ensure the list of vectors it returns is a basis, it only assures that it spans a full rank sub-lattice.

In particular in the following example (E8):



```
Q = QuadraticForm( matrix( [[2,0,0,0,0,0,0,1],
                            [0,2,1,1,1,1,1,1],
                            [0,1,2,1,1,1,1,1],
                            [0,1,1,2,1,1,1,1],
                            [0,1,1,1,2,1,1,1],
                            [0,1,1,1,1,2,1,1],
                            [0,1,1,1,1,1,2,0],
                            [1,1,1,1,1,1,0,2]] ))
B = Q.basis_of_short_vectors()
matrix(B).det()
```



The result is -2, which indicates we did not get a basis.
Note that the above means that sage likely returns incorrect results about the automorphism groups of a number of interesting lattices.
I am attaching some sample code which (once properly merged {and tested}) could be used to correct the issue.


---

Attachment

Sample code to correct a non-basis from basis_of_short_vectors


---

Comment by jdemeyer created at 2015-08-30 10:50:11

Isn't this just a matter of defining what "basis" means?


---

Comment by afiori created at 2015-09-25 17:47:23

I suppose someone might want a rational basis for the associated rational vector space which consists only of integral vectors... but that seems unlikely to be a common use case.
In any case, if I recall correctly... the code which computes automorphism groups of lattices uses this function, and consequently computes the automorphism group of E8 incorrectly.
The simplest stopgap would be to check if you are returning a basis, and if not just return the original basis. 
The code I had posted before (before I had learned to build patches under the old system) probably works, though as I don't currently have a working sage install to test it in (and still haven't done anything with current system for building patches) I am not really in a position to do much testing.


---

Comment by nbruin created at 2021-08-26 16:18:00

It looks to me the well-defined notion here would be the "successive minima" of a lattice: a sequence of vectors in the lattice where each vector is of minimal length while being linearly independent from the previous ones. Such a set is indeed not necessarily a basis. So we should check that the routine actually computes this and then rename it.

I think for most applications, the lengths themselves are usually more important than the vectors that attain them.

Naturally, this notion needs a (positive) definite quadratic form.
