# Issue 3148: improved orthogonal functions

Issue created by migration from Trac.

Original creator: fwclarke

Original creation time: 2008-05-10 12:08:12

Assignee: was

Keywords: orthogonal polynomials Maxima


The defects in the code for the hermite function in
sage/functions/orthogonal_polys.py which were noted and corrected in 
#2336 apply equally to the other functions in that file.

The attached patch applies the same fix that worked for hermite to the 
following functions:

chebyshev_T,
chebyshev_U,
gen_laguerre,
gen_legendre_P,
gen_legendre_Q,
jacobi_P,
laguerre,
legendre_P,
legendre_Q,
ultraspherical

This allows these polynomials to take much more general 
arguments; see the examples given for legendre_P.

The functions:

gen_legendre_P,
gen_legendre_Q,
legendre_Q

no longer yield a string representing a Maxima expression when the 
argument is a variable.   

For m > n the function gen_legendre_Q(n, m, x)
has to be computed independently of Maxima.  This part of the code may 
need improving.

The introductory documentation has not been changed.




---

Attachment


---

Comment by mhansen created at 2008-05-23 07:27:03

Looks good to me.  All the tests pass, and the patch definitely simplifies the code.


---

Comment by mabshoff created at 2008-05-23 07:29:07

Merged in Sage 3.0.2.rc0


---

Comment by mabshoff created at 2008-05-23 07:29:07

Resolution: fixed
