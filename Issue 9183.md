# Issue 9183: creating an expect element can modify a previously created expect element

Issue created by migration from https://trac.sagemath.org/ticket/9183

Original creator: saliola

Original creation time: 2010-06-08 03:16:19

Assignee: was

Keywords: gap

The `_next_variable_name` method in the expect interface sometimes spits out a variable name that is in use. This means that a previously created element might be modified inadvertently:

```
sage: z = gap(3); z
3
sage: gap.clear(z.name())
sage: gap.clear(z.name())
sage: x = gap(3); x
3
sage: y = gap(4); y
4
sage: x
4 
```

Of course, x should be 3 above, and not 4.

(This issue was found in #8380, but it didn't get resolved there. See the ticket for more details.)
