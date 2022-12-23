# Issue 7233: [with patch, positive review] adapted SymmetricGroupAlgebra to the category framework

Issue created by migration from https://trac.sagemath.org/ticket/7233

Original creator: hivert

Original creation time: 2009-10-16 11:03:04

Assignee: nthiery

CC:  combinat

Keywords: Symmetric Group Algebra, Categories

The goal of the patch is to adapt SymmetricGroupAlgebra to categories and to add some improvements. The patch improve SymmetricGroupAlgebra in two ways:
 
 - SymmetricGroupAlgebra is now in the category FiniteDimensionalAlgebraWithBasis. Note: A forthcomming patch from Valentin Feray will put it in the correct GroupAlgebras category;

 - When creating SGA(n) a coercion from SGA(n-1) is declared.

I'm submitting the patch on behalf on Nicolas after reviewing it.

Depends on the categories framework #5891.

Cheers,

Florent



---

Attachment


---

Comment by hivert created at 2009-10-16 11:12:38

Resolution: duplicate


---

Comment by hivert created at 2009-10-16 11:12:38

Oops !!! This is a duplicate of 6138... I should have gessed it from the name of the patch. Sorry for the mess,

Florent
