# Issue 2091: List of Of Objects for a command

Issue created by migration from Trac.

Original creator: gmoose05

Original creation time: 2008-02-07 23:43:50

Assignee: was

I would like a command so that I can get a list of objects that a particular function acts on


```
sage: Objects(.factor) 

[PolynomialRing, MultivariatePolynomialRing, IntegerRing, etc.]
```


but it wouldn't return FractionFieldofPolynomialRing  (for example)

This might be accomplished by pruning class_graph(sage) for the highest level that includes such a command 
