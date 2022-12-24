# Issue 2091: List of Of Objects for a command

archive/issues_002091.json:
```json
{
    "body": "Assignee: @williamstein\n\nI would like a command so that I can get a list of objects that a particular function acts on\n\n\n```\nsage: Objects(.factor) \n\n[PolynomialRing, MultivariatePolynomialRing, IntegerRing, etc.]\n```\n\n\nbut it wouldn't return FractionFieldofPolynomialRing  (for example)\n\nThis might be accomplished by pruning class_graph(sage) for the highest level that includes such a command \n\nIssue created by migration from https://trac.sagemath.org/ticket/2091\n\n",
    "created_at": "2008-02-07T23:43:50Z",
    "labels": [
        "user interface",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "List of Of Objects for a command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2091",
    "user": "gmoose05"
}
```
Assignee: @williamstein

I would like a command so that I can get a list of objects that a particular function acts on


```
sage: Objects(.factor) 

[PolynomialRing, MultivariatePolynomialRing, IntegerRing, etc.]
```


but it wouldn't return FractionFieldofPolynomialRing  (for example)

This might be accomplished by pruning class_graph(sage) for the highest level that includes such a command 

Issue created by migration from https://trac.sagemath.org/ticket/2091


