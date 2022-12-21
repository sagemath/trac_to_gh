# Issue 79: Create a framework for numerical computation in SAGE

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-23 00:37:23

Assignee: somebody

Good support in SAGE for numerical computation is crucial to our success.  Ignoring serious numerical computation has crippled numerous other systems (e.g., GAP).  
The primary audience of SAGE is not engineers or big-lab researchers.  
The target audience of SAGE is mainly undergraduate mathematics majors,
mathematics graduate students, and researchers in mathematics and cryptography.


SAGE's unique approach to numerics will be to focus from the ground up on connections between algrebraic and numerical computation.  This means:

   * The numerical objects in SAGE will be very algebraically structured, just like objects are in Magma and the rest of SAGE.  Matrices, vectors, etc., will be mathematical objects, with all the accomanying structure. 

   * There will be substantial support for transforming objects from numerical to algebraic and from algebraic to numerical.  For example, there should be very fast transformations of matrices (vectors, polynomials, etc.) over the rationals to matrices with floating point entries, implemented at the compiled level.  And the supported transformations should make sense mathematically.  Also, there should be transformations like "give me the best rational coefficient approximation to this polynomial", etc.   There are likely interesting problems here that could lead to a paper. 


    * The numerical libraries should be build-able 100% with no dependencies, so that users can understand all numerical code in SAGE with just knowledge of C and Python.   We are not targeting engineers who are happy with black boxes -- we are targeting curious talented mathematicians, who we can reasonably expect might want to crack open the box and look inside.  Of course, for speed one should also be able to build against standard optimized (sometimes closed source) BLAS implementations.  GSL nicely satisfies this requirement. 

    * When possible, available functions, their layout, conventions, and function names should be similar to what is in MATLAB, since that's what many people use for numerical computation and know well, and MATLAB is well designed.  This will make it easier for people to use both SAGE and MATLAB. 

    * Plotting is very important.   We should put huge effort in to make plotting of numerical objects integrate nicely with what SAGE offers via the notebook, i.e., via matplotlib, tachyon, etc.   For local-GUI plotting, vtk already does an excellent job and SAGE has little to add.  But for plotting in a notebook, there are still many interesting difficult problems. 


---

Comment by mabshoff created at 2007-09-10 03:08:24

This should be broken up into smaller tickets. Some of this has already happened/is covered by other tickets.

Cheers,

Michael


---

Comment by was created at 2007-09-20 13:48:35

Josh did this with integrating in scipy, etc.


---

Comment by was created at 2007-09-20 13:48:35

Resolution: fixed
