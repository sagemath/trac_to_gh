# Issue 1443: cannot define function variables?

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-12-09 21:49:26

Assignee: was

It seems not possible to create a functional variable in SAGE. This gives strange things:

```
sage: var('f');
sage: f(x)
x
```

Ideally one should be able to do the following, to compute the formal derivative of f(g(x)):

```
sage: var('f,g');
sage: diff(f(g(x)), x)
```

(Currently this gives 1 due to the above strange simplification f(x) -> x.)


---

Comment by mhansen created at 2007-12-10 07:45:03


```
sage: f = function('f')
sage: f(x)
f(x)
sage: g = function('g')
sage: f(g(x))
f(g(x))
sage: diff(f(g(x)),x)
diff(f(g(x)), x, 1)
```



---

Comment by mhansen created at 2007-12-10 07:45:03

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-12-10 07:45:03

Changing status from new to assigned.


---

Comment by was created at 2007-12-15 23:39:33

Use function, as mentioned above:


```
sage: function('f, g')
(f, g)
sage: diff(f(g(x)), x)
diff(f(g(x)), x, 1)
```



---

Comment by was created at 2007-12-15 23:40:36

Resolution: invalid
