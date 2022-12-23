# Issue 8170: character_table() missing for matrix groups

Issue created by migration from https://trac.sagemath.org/ticket/8170

Original creator: dimpase

Original creation time: 2010-02-03 12:53:15

Assignee: joyner

There is an inconsistency in matrix groups
(sage/groups/matrix_gps/matrix_group()):
The method character_table() is missing, whereas it is present
for permutation groups
(sage/groups/perm_gps/permgroup.py)

