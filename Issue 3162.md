# Issue 3162: Problems with echelon_form over ComplexField

Issue created by migration from https://trac.sagemath.org/ticket/3162

Original creator: dunfield

Original creation time: 2008-05-12 00:43:45

Assignee: was

CC:  jason

For certain well-conditioned floating-point matrices with entries in ComplexField, echelon_form can return matrices which are not in (approximate) echelon_form.   This breaks methods like rank(), right_solve() and inverse().  

 I've attached a sample matrix which illustrates this 



```
sage: A = load("./prob-sol.sobj")
sage: A.parent()
Full MatrixSpace of 5 by 5 dense matrices over Complex Field with 1010 bits of precision
sage: matrix(CDF, A.echelon_form())

[                              1.0                                 0                            -3.5*I                                 0                    -20.0 + 12.0*I]
[                                0                               1.0                               1.0                                 0                      -4.0 + 1.0*I]
[                                0                                 0        1.0 + 4.55695126222e-305*I                                 0 -2.33592727654 + 0.497614402099*I]
[                                0                                 0                              -4.0                               1.0                              -2.0]
[                                0                                 0                              -2.0                                 0                                 0]
sage: CC(A.det())
76.1312551138321 - 5.28799080668534*I
sage: A.rank()
4
```



This bug is probably related to #2256 and #1132 but there the problem with echelon_form is more subtle (1 entries on the diagonal which aren't quite 1), which is why I opened this new ticket.  


---

Attachment

Problem matrix


---

Comment by dunfield created at 2008-05-12 02:27:16

The problem here seems to be just basic numerical instability.  Basically, the pivots need to be chosen more carefully when working over a "floating-point" field.     In this particular matrix, echelon form is done via "_echelon_in_place_classical".  What happens is that after clearing the first column, the (1,1) entry is very nearly 0.  Despite this, it is still chosen as the pivot, and using it to clear down results in some very large entries in the rest of the matrix.   For reasons I don't fully understand, when one starts clearing from the next pivot not everything goes away.  

Presumably, the thing to do is to go look at some numerical analysis text and see what you're supposed to do here, but as a start, picking pivots which aren't close to zero would probably solve this.  

Here is printout of the various steps in this process. 



```
[-0.017 + 0.69*I   -2.1 - 0.75*I    -1.3 + 1.3*I   0.77 + 0.57*I   0.84 - 0.62*I]
[-0.017 + 0.69*I   -2.1 - 0.75*I   0.59 + 0.52*I   -1.2 + 0.94*I    0.61 + 1.5*I]
[  0.33 - 0.46*I               0   0.071 - 1.2*I    0.78 - 3.0*I    0.61 + 1.5*I]
[              0     1.0 + 1.4*I   0.071 - 1.2*I   -1.2 + 0.94*I    -2.9 - 1.8*I]
[-0.017 + 0.69*I    1.0 - 0.69*I  -0.071 + 1.2*I   -0.39 + 1.5*I   0.84 - 0.62*I] 

[          1.0  -1.0 + 3.0*I   2.0 + 1.9*I  0.80 - 1.1*I -0.93 - 1.2*I]
[            0   -9.1e-305*I  1.9 - 0.82*I -1.9 + 0.37*I -0.23 + 2.1*I]
[            0  -1.0 - 1.4*I -1.4 - 0.90*I   1.0 - 2.3*I   1.5 + 1.5*I]
[            0   1.0 + 1.4*I 0.071 - 1.2*I -1.2 + 0.94*I  -2.9 - 1.8*I]
[            0 3.1 + 0.063*I  1.3 - 0.15*I -1.2 + 0.94*I     -9.1e-305] 

[                 1.0                    0  7.2e304 - 5.4e303*I -6.7e304 - 9.4e303*I -3.1e304 + 6.7e304*I]
[                   0                  1.0  9.0e303 + 2.1e304*I -4.0e303 - 2.1e304*I -2.3e304 - 2.5e303*I]
[                   0                    0 -2.1e304 + 3.5e304*I  2.6e304 - 2.8e304*I -2.1e304 - 3.6e304*I]
[                   0                    0  2.1e304 - 3.5e304*I -2.6e304 + 2.8e304*I  2.1e304 + 3.6e304*I]
[                   0                    0 -2.6e304 - 6.5e304*I  1.1e304 + 6.5e304*I  7.2e304 + 9.2e303*I] 

[             1.0                0           -3.5*I     -8.0 - 2.0*I     -4.0 + 16.*I]
[               0              1.0              1.0                0     -4.0 + 1.0*I]
[               0                0 1.0 + 4.6e-305*I   -0.92 - 0.20*I   -0.50 + 0.90*I]
[               0                0             -2.0                0                0]
[               0                0             -4.0             -4.0              8.0] 

[             1.0                0           -3.5*I                0     -20. + 12.*I]
[               0              1.0              1.0                0     -4.0 + 1.0*I]
[               0                0 1.0 + 4.6e-305*I                0    -2.3 + 0.50*I]
[               0                0             -4.0              1.0             -2.0]
[               0                0             -2.0                0                0] 

[             1.0                0           -3.5*I                0     -20. + 12.*I]
[               0              1.0              1.0                0     -4.0 + 1.0*I]
[               0                0 1.0 + 4.6e-305*I                0    -2.3 + 0.50*I]
[               0                0             -4.0              1.0             -2.0]
[               0                0             -2.0                0                0] 
```


Note this also accounts for the non-one entries on the diagonal, which then causes an exception in __invert__ as noticed in #2256 and #1132.


---

Comment by dunfield created at 2008-05-12 02:53:38

Also, I'm pretty sure that PARI does OK with echelon forms of matrices with high-precision entries, so one could look at that code...


---

Comment by AlexGhitza created at 2009-01-23 02:44:52

Changing type from defect to enhancement.
