# Issue 6769: Documentation for vector() does not match behavior

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-08-17 06:54:19

Assignee: was

CC:  knsam

Keywords: vector documentation

The documentation for the vector constructor (vector() in sage/modules/free_module_element.pyx) could use some improvement, since the "call formats" do not include all the possibilities and the description is a bit confusing.  For example:

1. `elts` is listed as an input, but nowhere is it stated just where this could be provided as an input.

2. `vector(QQ, 3, [1,2,3])` is a legitimate construction but the documentation does not describe it anywhere.
