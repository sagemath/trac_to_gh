# Issue 7641: symbolic expression plots

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-12-09 17:34:16

Assignee: was

CC:  burcin

Right now, plots for symbolic expressions do not go through the generic codepath, but through the expression.plot() function in symbolic/expression.pyx.  This specialized codepath changes how the arguments are handled, etc.  I think any functionality in the special codepath ought to go in the generic codepath, or we should reduce the generic codepath quite a bit and just pass things off to symbolic expressions.  Too much code duplication here has led to lots of little inconsistencies.

As an example, this works `plot(x^2,0,x,5)`, but this doesn't: `parametric_plot((x,x^2), 0,x,5)`, since the first uses the expression.pyx codepath, but the parametric plot uses the generic codepath.
