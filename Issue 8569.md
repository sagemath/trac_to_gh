# Issue 8569: Standardize the title in the categories

Issue created by migration from https://trac.sagemath.org/ticket/8569

Original creator: hivert

Original creation time: 2010-03-21 11:11:55

Assignee: nthiery

CC:  documentation

Right now there are various choices of title format in the categories files: for examples you have "FiniteSemigroups" but
"Finite Weyl Groups". Even worse, files `finite_monoids.py` and `monoids.py` have the same title, namely "Monoids". As a results, in the front page http://www.sagemath.org/doc/reference/categories.html the link "Monoids" points to `finite_monoids.html` and `monoids.html` is compiled but not linked there. 

I think we should all standardize so that the title of the file is the same as the name of the category with space in it. For example,
file `finite_monoids.py` which defines category `FiniteMonoids()` should have title "Finite Monoids"

Florent




---

Comment by nthiery created at 2010-03-21 20:58:21

Replying to [ticket:8569 hivert]:
> Right now there are various choices of title format in the categories files: for examples you have "FiniteSemigroups" but
> "Finite Weyl Groups". Even worse, files `finite_monoids.py` and `monoids.py` have the same title, namely "Monoids". As a results, in the front page http://www.sagemath.org/doc/reference/categories.html the link "Monoids" points to `finite_monoids.html` and `monoids.html` is compiled but not linked there. 
> 
> I think we should all standardize so that the title of the file is the same as the name of the category with space in it. For example,
> file `finite_monoids.py` which defines category `FiniteMonoids()` should have title "Finite Monoids"

+1.

The only issue is for how to do handle it while minimizing the conflicts with other patches.
