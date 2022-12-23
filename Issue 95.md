# Issue 95: _gap_init_ bug

Issue created by migration from https://trac.sagemath.org/ticket/95

Original creator: wdj

Original creation time: 2006-09-28 23:57:56

Assignee: wdj

Keywords: GAP

This was reported by David Loeffler on 9-28-2006:

I'm running SAGE 1.3.7.3.3 on one of Imperial College's public RedHat Linux boxes.

If I load the interpreter and type:

M=MatrixSpace(QQ,3)
G=MatrixGroup([M([0,1,0,0,0,1,1,0,0]), M([0,1,0,1,0,0,0,0,1])])
G.order()

it works fine, and returns the obvious answer 6.

If I say instead

G=MatrixGroup([M([0,1,0,0,0,1,1,0,0]), M([0,1,0,1,0,0,0,0,1]), M([-1,0,0,0,1,0,0,0,1])])

then whenever I call any methods on G, it dies:

sage: G.order()
---------------------------------------------------------------------------
exceptions.TypeError                                 Traceback (most recent call last)


---

Comment by wdj created at 2006-09-29 00:00:13

Resolution: fixed


---

Comment by wdj created at 2006-09-29 00:00:13

This is bad. However, I get a bug even on your working example:

sage: M = MatrixSpace(GF(3),3,3)

sage: G = MatrixGroup([M([[0,1,0],[0,0,1],[1,0,0]]), M([[0,1,0],[1,0,0],[0,0,1]])])

sage: G._gap_init_()

''

The bug is in the _gap_init_ method in the MatrixGroup class. If you use

   def _gap_init_(self):
       """
       Returns the string representation of the corresponding GAP command.

       EXAMPLES:
           sage: F = GF(5); MS = MatrixSpace(F,2,2)

           sage: gens = [MS([[1,2],[-1,1]]),MS([[1,1],[0,1]])]

           sage: G = MatrixGroup(gens)

           sage: G._gap_init_()

           'Group([ [ [ Z(5)0, Z(5) ], [ Z(5)2, Z(5)0 ] ],        
              [ [ Z(5)0, Z(5)0 ], [ 0*Z(5), Z(5)0 ] ] ])'
       """
       gens_gap = [gap(x) for x in self.gens()]

       cmd = "Group("+str(gens_gap)+")"

       cmd = cmd.replace("\n","")

       return gap(cmd)

instead it will work (I'm sure the wiki will destroy the indenting, but you get the idea).


---

Comment by wdj created at 2006-09-29 00:02:21

Resolution changed from fixed to 


---

Comment by wdj created at 2006-09-29 00:02:21

Changing status from closed to reopened.


---

Comment by was created at 2007-01-12 22:39:48

Resolution: fixed


---

Comment by was created at 2007-01-12 22:39:48

This was already fixed.  But another bug appeared (and got fixed)
when I tested the example:

```

# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168641553 28800
# Node ID e7e66d37ff7a6bc0c31efa693c0dcd5be1c6d048
# Parent  85b96a510e10e13d5e71aa12afb2a3f1a3564fb8
Fix bug in matrix hessenberg form.

diff -r 85b96a510e10 -r e7e66d37ff7a sage/matrix/matrix_modn_dense.pyx
--- a/sage/matrix/matrix_modn_dense.pyx Fri Jan 12 14:26:44 2007 -0800
+++ b/sage/matrix/matrix_modn_dense.pyx Fri Jan 12 14:39:13 2007 -0800
@@ -48,6 +48,19 @@ EXAMPLES:
     sage: b.echelonize(); b
     [ 1  0 36]
     [ 0  1  2]
+
+We create a matrix group and coerce it to GAP:
+    sage: M = MatrixSpace(GF(3),3,3)
+    sage: G = MatrixGroup([M([[0,1,0],[0,0,1],[1,0,0]]), M([[0,1,0],[1,0,0],[0,0,1]])])
+    sage: G
+    Matrix group over Finite Field of size 3 with 2 generators: 
+     [[[0, 1, 0], [0, 0, 1], [1, 0, 0]], [[0, 1, 0], [1, 0, 0], [0, 0, 1]]]
+    sage: gap(G)
+    Group(
+    [ [ [ 0*Z(3), Z(3)^0, 0*Z(3) ], [ 0*Z(3), 0*Z(3), Z(3)^0 ], [ Z(3)^0, 0*Z(3),
+               0*Z(3) ] ], 
+      [ [ 0*Z(3), Z(3)^0, 0*Z(3) ], [ Z(3)^0, 0*Z(3), 0*Z(3) ], 
+          [ 0*Z(3), 0*Z(3), Z(3)^0 ] ] ])
 """
 
 include "../ext/interrupt.pxi"
@@ -419,8 +432,8 @@ cdef class Matrix_modn_dense(matrix_dens
                  t = h[i][m-1]
                  t_inv = ai.c_inverse_mod_int(t,p)
                  if i > m:
-                     self._swap_rows_c(i,m)
-                     self._swap_columns_c(i,m)
+                     self.swap_rows_c(i,m)
+                     self.swap_columns_c(i,m)
 
                  # Now the nonzero entry in position (m,m-1) is t.
                  # Use t to clear the entries in column m-1 below m.
```

