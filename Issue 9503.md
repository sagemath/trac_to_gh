# Issue 9503: FreeModule_submodule_with_basis_pid calls wrong constructor

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2010-07-15 07:15:10

Assignee: AlexGhitza

This is a piece of the current code in `FreeModule_submodule_with_basis_pid` after #9502 (before it was the same without explanations)

```
# The following is WRONG - we should call __init__ of
# FreeModule_generic_pid. However, it leads to a bunch of errors.
FreeModule_generic.__init__(self, R,
                            rank=len(basis), degree=ambient.degree(),
                            sparse=ambient.is_sparse())

```

The errors seem to be related to number fields and their rings of integers.
