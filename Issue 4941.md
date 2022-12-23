# Issue 4941: pari list slicing is extremely slow -- make it much faster

Issue created by migration from https://trac.sagemath.org/ticket/4941

Original creator: was

Original creation time: 2009-01-05 17:10:35

Assignee: was

The following illustrates that list slicing in Pari is ridiculously slow.


```
sage: time p=pari.prime_list(10^6)
CPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s
Wall time: 0.09 s
sage: len(p)
1000000
sage: time c=p[0:]
CPU times: user 45.05 s, sys: 0.54 s, total: 45.59 s
Wall time: 46.20 s
```


The code responsible for this is in pari/gen.pyx (line 825 in sage-3.2.3) in __getitem__:

```
        elif PyObject_TypeCheck(n, slice):
            l = glength(self.g)
            inds = _normalize_slice(n, l)
            k = len(inds)
            v = P.vector(k)
            for i in range(k):
                v[i] = self[inds[i]]
            return v
```


There must be dramatically faster ways to do a list slice in pari than the above.




---

Comment by ylchapuy created at 2009-01-19 20:51:35

in GP I would do something like

```
u=start-step; v=vector(k,unused,p[u+=step])
```


but I don't know how to translate this...

otherwise for big blocks,

```
p.vecextract('"150..10000"')
```

might be faster


---

Comment by ylchapuy created at 2009-01-20 18:46:10

This patch solves only the easy part of the problem, for slices of type [::1] or [::-1], still better than nothing.


---

Comment by ylchapuy created at 2009-01-20 18:47:47

oh, and it needs to be applied after patching #4974


---

Comment by ylchapuy created at 2009-01-20 20:40:12

I removed my broken patch


---

Comment by ylchapuy created at 2009-01-21 08:50:47

corrected patch, sorry for the spam...

it uses vecextract when possible.

all tests pass


---

Attachment

for polynomials, slicing for generic polynomials returns a polynomial, whereas with pari it returns a vector. I think we should change this behavior.


---

Comment by mhansen created at 2009-10-05 18:46:34

Looks good to me. If we want to change the behavior, then I would make that a seperate ticket.


---

Comment by mhansen created at 2009-10-15 05:25:28

Resolution: fixed
