# Issue 3670: symbolic equation should be merged into symbolic opeartors

Issue created by migration from https://trac.sagemath.org/ticket/3670

Original creator: gfurnish

Original creation time: 2008-07-17 11:14:45

Assignee: gfurnish

As detailed in emails with cwitty, SymbolicEquation should be absorbed into a ==, <, etc, SymbolicOperator that is of sym_parent boolean parent (which is not yet implemented), to be based off of BooleanLattice.  Notzero should remain as is, but raise an exception of sym_parent is not boolean.  


---

Comment by was created at 2008-07-18 14:30:44

I changed it to an enhancement -- this isn't a bug in Sage.


---

Comment by was created at 2008-07-18 14:30:44

Changing type from defect to enhancement.


---

Comment by was created at 2008-08-23 08:14:07

Resolution: invalid


---

Comment by was created at 2008-08-23 08:14:14

Milestone sage-symbolics deleted
