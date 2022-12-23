# Issue 9558: Make `is_symmetric` method for polynomials or where else useful

Issue created by migration from https://trac.sagemath.org/ticket/9558

Original creator: kcrisman

Original creation time: 2010-07-21 01:22:52

Assignee: AlexGhitza

CC:  sage-combinat

This is a little vague - should it also be for SR, not just polynomial rings?  But it seems like a reasonable request on sage-support:

```
Hi, 
I would like to know if there are any function that says if a 
polynomial is or not symmetric (like: 'is_symmetric'), so Mathematica 
have this kind of function. 
http://en.wikipedia.org/wiki/Symmetric_polynomial 
Thanks! 
```



---

Comment by jbandlow created at 2010-07-30 15:31:45

Changing assignee from AlexGhitza to sage-combinat.


---

Comment by jbandlow created at 2010-07-30 15:31:45

The following works (at least in sage-4.4.4):

```
sage: R.<x,y,z> = QQ[]
sage: SF = SymmetricFunctions(QQ)
sage: SF.from_polynomial(x^2 + y^2 + z^2)
m[2]
sage: SF.from_polynomial(x^2 + y^2)
...
ValueError: x^2 + y^2 is not a symmetric polynomial
```


If someone wants to make a top level function like that suggested in the initial post, a design discussion should probably happen on sage.devel or sage.combinat.devel first.  

I'm changing the component to combinatorics since that's where tickets related to symmetric functions usually live.


---

Comment by jbandlow created at 2010-07-30 15:31:45

Changing component from algebra to combinatorics.
