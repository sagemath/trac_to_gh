# Issue 7454: Make comparison of character tables sensible

Issue created by migration from https://trac.sagemath.org/ticket/7454

Original creator: kcrisman

Original creation time: 2009-11-13 19:28:22

Assignee: joyner

CC:  rbeezer wdj

This seems annoying:

```
sage: S = SymmetricGroup(3).direct_product(CyclicPermutationGroup(2))[0]
sage: S
Permutation Group with generators [(1,2,3), (1,2), (4,5)]
sage: S.character_table()

[ 1  1  1  1  1  1]
[ 1 -1 -1  1  1 -1]
[ 1 -1  1 -1  1 -1]
[ 1  1 -1 -1  1  1]
[ 2 -2  0  0 -1  1]
[ 2  2  0  0 -1 -1]
sage: D = DihedralGroup(6)
sage: D.character_table()

[ 1  1  1  1  1  1]
[ 1 -1 -1  1  1  1]
[ 1 -1  1 -1  1 -1]
[ 1  1 -1 -1  1 -1]
[ 2  0  0  1 -1 -2]
[ 2  0  0 -1 -1  2]
sage: S.character_table()==D.character_table()
False
```

This is despite the fact that these groups are isomorphic (a fun exercise!).  The reason is

```
sage: type(S.character_table())
<type 'sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense'>
```

and the matrices above are obviously not identical.  Which shouldn't necessarily be changed, but nonetheless this is annoying.  Maybe at least a .has_same_character_table_as() method?  At least for pedagogical purposes.  Better might be to have a separate class for character tables, with a .matrix() method, but that would be perhaps backwards-incompatible.
