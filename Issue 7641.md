# Issue 7641: symbolic expression plots

archive/issues_007641.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @burcin\n\nRight now, plots for symbolic expressions do not go through the generic codepath, but through the expression.plot() function in symbolic/expression.pyx.  This specialized codepath changes how the arguments are handled, etc.  I think any functionality in the special codepath ought to go in the generic codepath, or we should reduce the generic codepath quite a bit and just pass things off to symbolic expressions.  Too much code duplication here has led to lots of little inconsistencies.\n\nAs an example, this works `plot(x^2,0,x,5)`, but this doesn't: `parametric_plot((x,x^2), 0,x,5)`, since the first uses the expression.pyx codepath, but the parametric plot uses the generic codepath.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7641\n\n",
    "created_at": "2009-12-09T17:34:16Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "symbolic expression plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7641",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

CC:  @burcin

Right now, plots for symbolic expressions do not go through the generic codepath, but through the expression.plot() function in symbolic/expression.pyx.  This specialized codepath changes how the arguments are handled, etc.  I think any functionality in the special codepath ought to go in the generic codepath, or we should reduce the generic codepath quite a bit and just pass things off to symbolic expressions.  Too much code duplication here has led to lots of little inconsistencies.

As an example, this works `plot(x^2,0,x,5)`, but this doesn't: `parametric_plot((x,x^2), 0,x,5)`, since the first uses the expression.pyx codepath, but the parametric plot uses the generic codepath.

Issue created by migration from https://trac.sagemath.org/ticket/7641


