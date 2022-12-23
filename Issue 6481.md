# Issue 6481: g.subs({x:1,y:2}) should walk through x,y sorted

Issue created by migration from https://trac.sagemath.org/ticket/6481

Original creator: malb

Original creation time: 2009-07-08 12:58:14

Assignee: malb

reported by Kwankyu on [sage-support]:


```
I mean the substitution y:x*y is applied first in the following

sage: R.<x,y>=QQ[]
sage: g=x+y
sage: g.subs({x:x+1,y:x*y})
x*y + x + y + 1

where I think applying x:x+1 first seems intuitive if order ever
should be significant.
```




---

Comment by was created at 2009-07-08 13:11:28

For the record, I think the entire design of subs for multivariate polynomial rings is wrong.  I've thus opened #6482 and explained my reasoning for this.

Note that in any case, if the current subs behavior is super fast or useful to people (is it?) then we can keep it as a nondefault option, in which case this ticket #6481 also makes sense to keep, since at least we should do the order of substitution in an easy-to-understand way.


---

Comment by malb created at 2009-09-09 20:13:29

Resolution: duplicate


---

Comment by malb created at 2009-09-09 20:13:29

Dupe of #6482
