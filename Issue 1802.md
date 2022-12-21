# Issue 1802: unify possible finite field representations

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-17 19:15:18

Assignee: was

Keywords: usability

If Givaro implements the finite extension field then the parameter "int" or "log" changes the representation of elements. This doesn't work for larger fields and thus is ambiguous. So either the `repr="int"` parameter should be dropped for Givaro or allowed for all other implementations.
