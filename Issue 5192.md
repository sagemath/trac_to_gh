# Issue 5192: Improve factor documentation

Issue created by migration from https://trac.sagemath.org/ticket/5192

Original creator: kcrisman

Original creation time: 2009-02-06 01:17:59

Assignee: tbd

Integers which result from symbolic expressions live in the symbolic ring, so they are not factored by factor().  E.g.

```
sage: f(n)=n^2+n+41
sage: a=f(40)
sage: factor(a),is_prime(a),a
(1681, False, 1681)
sage: factor(1681)
41^2
```

But this is not obvious from the documentation of factor(), which only refers to e.g. a.factor? as the source of this.  Some example like this should be added to the documentation of the global factor().


---

Attachment

Based on 3.3.alpha5


---

Comment by mabshoff created at 2009-02-07 00:55:57

Resolution: fixed


---

Comment by mabshoff created at 2009-02-07 00:55:57

Merged in Sage 3.3.alpha6.

Cheers,

Michael
