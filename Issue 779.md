# Issue 779: Matrix from Matrix_integer_dense() blows up

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2007-10-02 01:58:14

Assignee: was

If I create a matrix with Matrix_integer_dense(), and try to display it, sage blows chunks.  It appears to happen inside the gmp library.  This is with 2.8.5.1 on a Core 2 Duo (Mac OS X, 10.4.10).

sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense
sage: a = Matrix_integer_dense.__new__(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)
sage: a.ncols()
3
sage: a.nrows()
3
sage: a

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_INVALID_ADDRESS at address: 0x013af000
0x00777991 in __gmpn_copyi ()
(gdb) bt
#0  0x00777991 in __gmpn_copyi ()
#1  0x0075c4a0 in __gmpz_set ()
Previous frame inner to this frame (corrupt stack?)


Then, there is

sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense
sage: a = Matrix_integer_dense.__new__(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)
sage: for i in range(a.nrows()):
   ...:     for j in range(a.ncols()):
   ...:         print a[i,j]
   ...:         
0
python(16613) malloc: *** vm_allocate(size=1680302080) failed (error code=3)
python(16613) malloc: *** error: can't allocate region
python(16613) malloc: *** set a breakpoint in szone_error to debug

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_PROTECTION_FAILURE at address: 0x00000000
0x0076a0b7 in __gmpn_sqr_basecase ()
(gdb) 


---

Comment by justin created at 2007-10-02 02:41:39

Resolution: invalid


---

Comment by justin created at 2007-10-02 02:41:39

I closed this because the formatting really sucks.  The new
Trac# is 781.


---

Comment by mabshoff created at 2007-10-04 19:48:45

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-10-04 19:48:45

Resolution changed from invalid to 


---

Comment by mabshoff created at 2007-10-04 19:48:52

Resolution: duplicate
