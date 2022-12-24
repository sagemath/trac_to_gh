# Issue 8569: Standardize the title in the categories

archive/issues_008569.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  documentation\n\nRight now there are various choices of title format in the categories files: for examples you have \"FiniteSemigroups\" but\n\"Finite Weyl Groups\". Even worse, files `finite_monoids.py` and `monoids.py` have the same title, namely \"Monoids\". As a results, in the front page http://www.sagemath.org/doc/reference/categories.html the link \"Monoids\" points to `finite_monoids.html` and `monoids.html` is compiled but not linked there. \n\nI think we should all standardize so that the title of the file is the same as the name of the category with space in it. For example,\nfile `finite_monoids.py` which defines category `FiniteMonoids()` should have title \"Finite Monoids\"\n\nFlorent\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8569\n\n",
    "created_at": "2010-03-21T11:11:55Z",
    "labels": [
        "categories",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Standardize the title in the categories",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8569",
    "user": "hivert"
}
```
Assignee: nthiery

CC:  documentation

Right now there are various choices of title format in the categories files: for examples you have "FiniteSemigroups" but
"Finite Weyl Groups". Even worse, files `finite_monoids.py` and `monoids.py` have the same title, namely "Monoids". As a results, in the front page http://www.sagemath.org/doc/reference/categories.html the link "Monoids" points to `finite_monoids.html` and `monoids.html` is compiled but not linked there. 

I think we should all standardize so that the title of the file is the same as the name of the category with space in it. For example,
file `finite_monoids.py` which defines category `FiniteMonoids()` should have title "Finite Monoids"

Florent



Issue created by migration from https://trac.sagemath.org/ticket/8569





---

archive/issue_comments_077622.json:
```json
{
    "body": "Replying to [ticket:8569 hivert]:\n> Right now there are various choices of title format in the categories files: for examples you have \"FiniteSemigroups\" but\n> \"Finite Weyl Groups\". Even worse, files `finite_monoids.py` and `monoids.py` have the same title, namely \"Monoids\". As a results, in the front page http://www.sagemath.org/doc/reference/categories.html the link \"Monoids\" points to `finite_monoids.html` and `monoids.html` is compiled but not linked there. \n> \n> I think we should all standardize so that the title of the file is the same as the name of the category with space in it. For example,\n> file `finite_monoids.py` which defines category `FiniteMonoids()` should have title \"Finite Monoids\"\n\n+1.\n\nThe only issue is for how to do handle it while minimizing the conflicts with other patches.",
    "created_at": "2010-03-21T20:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8569#issuecomment-77622",
    "user": "nthiery"
}
```

Replying to [ticket:8569 hivert]:
> Right now there are various choices of title format in the categories files: for examples you have "FiniteSemigroups" but
> "Finite Weyl Groups". Even worse, files `finite_monoids.py` and `monoids.py` have the same title, namely "Monoids". As a results, in the front page http://www.sagemath.org/doc/reference/categories.html the link "Monoids" points to `finite_monoids.html` and `monoids.html` is compiled but not linked there. 
> 
> I think we should all standardize so that the title of the file is the same as the name of the category with space in it. For example,
> file `finite_monoids.py` which defines category `FiniteMonoids()` should have title "Finite Monoids"

+1.

The only issue is for how to do handle it while minimizing the conflicts with other patches.
