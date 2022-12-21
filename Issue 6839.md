# Issue 6839: Implementation of crystal of letters for type E7

Issue created by migration from Trac.

Original creator: aschilling

Original creation time: 2009-08-29 06:34:56

Assignee: mhansen

CC:  sage-combinat

Keywords: combinat, crystals

- Implemented crystal of letters for type E7
- Added the method that goes to the highest weight element from any crystal element
  (living in a highest weight crystal)


---

Attachment


---

Comment by aschilling created at 2009-08-29 06:49:52

Changing assignee from mhansen to aschilling.


---

Comment by bump created at 2009-09-04 18:04:42

This patch creates the E7 crystal with highest weight
vector the last fundamental weight. This is the 56-dimensional
one. As usual, once the crystal of letters is implemented,
others follow using CrystalOfTableaux, though for such a
large group this will be computationally intensive.

The patch applies without change to sage 4.1.1.

It passes `sage --testall`.

I convinced myself that the crystal created is correct. For
example, it branches correctly to E6, A6 and D6.

The new method to_highest_weight() is very useful. You
can specify a subset of the index set and partition the
crystal into subcrystals for any Levi subgroup.


---

Comment by mvngu created at 2009-09-07 17:25:36

The following docstring causes warnings when building the reference manual:

```
1287	    TESTS:: 
1288	 
1289	    sage: C = CrystalOfLetters(['E',7]) 
1290	    sage: C.module_generators 
1291	    [This is the Trac macro *7* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#7-macro) 
1292	    sage: C.list() 
1293	    [[7], [-7, 6], [-6, 5], [-5, 4], [-4, 2, 3], [-2, 3], [-3, 1, 2], [-1, 
1294	    2], [-3, -2, 1, 4], [-1, -2, 4], [-4, 1, 5], [-4, -1, 3, 5], [-3, 5], 
1295	    [-5, 6, 1], [-5, -1, 3, 6], [-5, -3, 4, 6], [-4, 2, 6], [-2, 6], [-6, 7, 
1296	    1], [-1, -6, 3, 7], [-6, -3, 7, 4], [-6, -4, 2, 7, 5], [-6, -2, 7, 5], 
1297	    [-5, 7, 2], [-5, -2, 4, 7], [-4, 7, 3], [-3, 1, 7], [-1, 7], [-7, 1], 
1298	    [-1, -7, 3], [-7, -3, 4], [-4, -7, 2, 5], [-7, -2, 5], [-5, -7, 6, 2], 
1299	    [-5, -2, -7, 4, 6], [-7, -4, 6, 3], [-3, -7, 1, 6], [-7, -1, 6], [-6, 
1300	    2], [-2, -6, 4], [-6, -4, 5, 3], [-3, -6, 1, 5], [-6, -1, 5], [-5, 3], 
1301	    [-3, -5, 4, 1], [-5, -1, 4], [-4, 1, 2], [-1, -4, 3, 2], [-3, 2], [-2, 
1302	    -3, 4], [-4, 5], [-5, 6], [-6, 7], [-7], [-2, 1], [-2, -1, 3]] 
1303	    sage: C.check() 
1304	    True 
1305	    sage: all(b.f(i).e(i) == b for i in C.index_set() for b in C if b.f(i) is not None) 
1306	    True 
1307	    sage: all(b.e(i).f(i) == b for i in C.index_set() for b in C if b.e(i) is not None) 
1308	    True 
1309	    sage: G = C.digraph() 
1310	    sage: G.show(edge_labels=true, figsize=12, vertex_size=1) 
```

See #6901 for a follow-up to this ticket.


---

Comment by mvngu created at 2009-09-07 17:25:36

Resolution: fixed
