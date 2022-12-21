# Issue 5135: Alternative basis for kernel of a matrix

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-01-30 03:34:07

Assignee: rbeezer

Keywords: kernel, basis

The left_kernel() method in matrix2.pyx computes basis vectors from the reduced echelon form of the transposed matrix.  For each non-pivot column, the corresponding entry of a basis vector is set to 1, the other non-pivot columns are set to zero, and the remaining entries are set to negatives of other specific entries of the matrix.

This basis is then used in a constructor of a subspace, and the basis is "echelonized" in the process.  Add a new keyword argument, echelonize, to left_kernel, that defaults to true.  With echelonize=false, the subspace will be constructed with the "pivot" basis and it will not be further massaged.

Sage-devel discussion [here](http://groups.google.com/group/sage-devel/browse_thread/thread/3d934669e00978e1/).
