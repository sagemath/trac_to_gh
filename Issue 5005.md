# Issue 5005: polynomial_template __init__ from list horribly innefficient

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-01-17 23:58:30

Assignee: tbd


```
            for e in x:
                # r += parent(e)*power
                celement_pow(&monomial, &gen, deg, NULL, parent)
                coeff = (<Polynomial_template>parent(e)).x
                celement_mul(&monomial, &coeff, &monomial, parent)
                celement_add(&self.x, &self.x, &monomial, parent)
                deg += 1
```


There should be a celement_set(self, x, i). 


---

Comment by robertwb created at 2010-01-17 09:45:30

The polynomial template framework has no c-level concept of elements of the basering, so there's not much that can be done here. Both ZZ[x] and Z/nZ[x] override `__init__` to be more efficient, so it's not really an issue, and so I'm closing this as won't fix.


---

Comment by robertwb created at 2010-01-17 09:45:30

Resolution: wontfix
