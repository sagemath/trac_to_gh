# Issue 7454: Make comparison of character tables sensible

archive/issues_007454.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @rbeezer @wdjoyner\n\nThis seems annoying:\n\n```\nsage: S = SymmetricGroup(3).direct_product(CyclicPermutationGroup(2))[0]\nsage: S\nPermutation Group with generators [(1,2,3), (1,2), (4,5)]\nsage: S.character_table()\n\n[ 1  1  1  1  1  1]\n[ 1 -1 -1  1  1 -1]\n[ 1 -1  1 -1  1 -1]\n[ 1  1 -1 -1  1  1]\n[ 2 -2  0  0 -1  1]\n[ 2  2  0  0 -1 -1]\nsage: D = DihedralGroup(6)\nsage: D.character_table()\n\n[ 1  1  1  1  1  1]\n[ 1 -1 -1  1  1  1]\n[ 1 -1  1 -1  1 -1]\n[ 1  1 -1 -1  1 -1]\n[ 2  0  0  1 -1 -2]\n[ 2  0  0 -1 -1  2]\nsage: S.character_table()==D.character_table()\nFalse\n```\n\nThis is despite the fact that these groups are isomorphic (a fun exercise!).  The reason is\n\n```\nsage: type(S.character_table())\n<type 'sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense'>\n```\n\nand the matrices above are obviously not identical.  Which shouldn't necessarily be changed, but nonetheless this is annoying.  Maybe at least a .has_same_character_table_as() method?  At least for pedagogical purposes.  Better might be to have a separate class for character tables, with a .matrix() method, but that would be perhaps backwards-incompatible.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7454\n\n",
    "created_at": "2009-11-13T19:28:22Z",
    "labels": [
        "group theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Make comparison of character tables sensible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7454",
    "user": "@kcrisman"
}
```
Assignee: joyner

CC:  @rbeezer @wdjoyner

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

Issue created by migration from https://trac.sagemath.org/ticket/7454


