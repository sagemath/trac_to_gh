# Issue 2809: G2 fundamental weights were the negative of what they should be.

Issue created by migration from https://trac.sagemath.org/ticket/2809

Original creator: bump

Original creation time: 2008-04-05 16:23:26

Assignee: mhansen

CC:  sage-combinat

In combinat/root_system.py, the fundamental weights for the various root systems are entered by hand. For G2, the fundamental weights were the negatives of what they should be.

```

diff -r 80b506b8e07c sage/combinat/root_system.py
--- a/sage/combinat/root_system.py	Tue Apr 01 19:18:55 2008 -0700
+++ b/sage/combinat/root_system.py	Sat Apr 05 08:40:46 2008 -0700
@@ -788,11 +788,11 @@ class AmbientLattice_g(AmbientLattice_ge
         """
         EXAMPLES:
             sage: CartanType(['G',2]).root_system().ambient_lattice().fundamental_weights()
-            [(-1, 0, 1), (-2, 1, 1)]
+            [(1, 0, -1), (2, -1, -1)]
         """
         return [ c0*self._term(0)+c1*self._term(1)+c2*self._term(2) \
                  for [c0,c1,c2] in
-                 [[-1,0,1],[-2,1,1]]]
+                 [[1,0,-1],[2,-1,-1]]]
 
 
 def WeylDim(type, coeffs):

```



---

Attachment

This is a dupe of #2808, so I am closing it. Dan: once you open a ticket and you hit "submit" you should remove the "preview" bit from the url before going on. This is a buglet in trac and you aren't the first one who has been bitten by it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-05 16:30:34

Resolution: duplicate
