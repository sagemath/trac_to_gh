# Issue 5590: coercion between polynomial rings over extension fields and polynomial rings over the prime subfield

archive/issues_005590.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @williamstein\n\nKeywords: coercion, polynomial ring\n\nAt #5569 William wrote: \n> As a challenge to Martin -- can you improve Sage so this decimal \n> string conversion (which could be a killer show stopper if the \n> ideal had huge elements) isn't needed, and instead one can use a \n> homomorphism?\n\nThe situation William is talking about is this:\n\n\n```\nsage: K.<a> = GF(2^3)\nsage: P.<x,y> = PolynomialRing(K)\nsage: R = PolynomialRing(GF(2),3,'a,x,y')\n```\n\n\nand we are looking for a way to convert elements in `P` to elements in `R`.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5590\n\n",
    "created_at": "2009-03-23T12:14:48Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "coercion between polynomial rings over extension fields and polynomial rings over the prime subfield",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5590",
    "user": "@malb"
}
```
Assignee: @malb

CC:  @williamstein

Keywords: coercion, polynomial ring

At #5569 William wrote: 
> As a challenge to Martin -- can you improve Sage so this decimal 
> string conversion (which could be a killer show stopper if the 
> ideal had huge elements) isn't needed, and instead one can use a 
> homomorphism?

The situation William is talking about is this:


```
sage: K.<a> = GF(2^3)
sage: P.<x,y> = PolynomialRing(K)
sage: R = PolynomialRing(GF(2),3,'a,x,y')
```


and we are looking for a way to convert elements in `P` to elements in `R`.



Issue created by migration from https://trac.sagemath.org/ticket/5590


