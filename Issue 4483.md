# Issue 4483: Add coefficient_field() method to ModularSymbols/ModularForms

archive/issues_004483.json:
```json
{
    "body": "Assignee: @craigcitro\n\n## Define a newform (up to conjugation)\n`time nf = ModularSymbols(100,2,1).cuspidal_subspace().new_subspace().decomposition()[0]`\n\n`nf.coefficient_field()` -- should return the field of definition of the newform.  (This appears to be accomplished with `nf.eigenvalue(1).parent()`.  It would be nice to know that this really does give the field of definition.)\n\n`nf.degree()` -- should return the degree of the coefficient field.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4483\n\n",
    "created_at": "2008-11-09T22:43:46Z",
    "labels": [
        "modular forms",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Add coefficient_field() method to ModularSymbols/ModularForms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4483",
    "user": "@jonhanke"
}
```
Assignee: @craigcitro

## Define a newform (up to conjugation)
`time nf = ModularSymbols(100,2,1).cuspidal_subspace().new_subspace().decomposition()[0]`

`nf.coefficient_field()` -- should return the field of definition of the newform.  (This appears to be accomplished with `nf.eigenvalue(1).parent()`.  It would be nice to know that this really does give the field of definition.)

`nf.degree()` -- should return the degree of the coefficient field.

Issue created by migration from https://trac.sagemath.org/ticket/4483





---

archive/issue_comments_033119.json:
```json
{
    "body": "There is something like this in Sage: look at the class `Newform` in modular/modform/element.py.  It has a method `hecke_eigenvalue_field()` which returns the field of definition of the newform.  There is no `degree()` method, although that's of course easy to get at this point as `nf.hecke_eigenvalue_field().degree()`.\n\nIt remains to add such a method to modular symbols (`nf.eigenvalue(1).parent()` is indeed correct), and maybe make `coefficient_field()` an alias for `hecke_eigenvalue_field()`.",
    "created_at": "2010-01-05T11:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4483#issuecomment-33119",
    "user": "@aghitza"
}
```

There is something like this in Sage: look at the class `Newform` in modular/modform/element.py.  It has a method `hecke_eigenvalue_field()` which returns the field of definition of the newform.  There is no `degree()` method, although that's of course easy to get at this point as `nf.hecke_eigenvalue_field().degree()`.

It remains to add such a method to modular symbols (`nf.eigenvalue(1).parent()` is indeed correct), and maybe make `coefficient_field()` an alias for `hecke_eigenvalue_field()`.
