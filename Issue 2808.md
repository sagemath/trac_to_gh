# Issue 2808: G2 fundamental weights were the negative of what they should be.

Issue created by migration from https://trac.sagemath.org/ticket/2808

Original creator: bump

Original creation time: 2008-04-05 16:18:50

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

patch correcting the G2 fundamental weights


---

Comment by bump created at 2008-04-05 16:29:07

Changing status from new to assigned.


---

Comment by bump created at 2008-04-05 16:29:07

Changing assignee from mhansen to bump.


---

Comment by cremona created at 2008-04-05 17:22:08

Quoting from the email to sage-devel:


```
I should have added some justification for this conclusion
in the trac report. Instead I'm giving it here. You can
look the weights up in Bourbaki, Lie Groups and Lie
Algebras Ch 4-6 (Appendix) and you can also check
the inner products of the weights with the simple
roots (which are correct). The inner product of
the i-th fundamental weight with the j-th simple
root should be positive if i=j and zero otherwise.
I checked that all the other root systems are right
by examining the output following program on the ambient
lattices. This change had no effect on the output of
the Weyl dimension formula.

def test_lattice(L):
   rank = L.ct[1]
   roots = L.simple_roots()
   weights = L.fundamental_weights()
      return [[i,j, roots[i].inner_product(weights[j])] for i in range(rank) for j in range(rank)]
```


I am happy with this (small!) change.


---

Comment by mabshoff created at 2008-04-05 17:31:52

Resolution: fixed


---

Comment by mabshoff created at 2008-04-05 17:31:52

Merged in Sage 3.0.alpha2.
