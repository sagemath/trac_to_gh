# Issue 3124: bug in solve_mod

Issue created by migration from https://trac.sagemath.org/ticket/3124

Original creator: was

Original creation time: 2008-05-07 15:43:25

Assignee: somebody

CC:  alexghitza


```
Hi,

I think this is a bug. Solving x == y mod 3 works fine:

sage: var('x,y')
(x, y)
sage: solve_mod([x == y], 3)
[(0, 0), (1, 1), (2, 2)]

But solving mod 2 blows up:


sage: solve_mod([x == y], 2)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/carlo/work/sagestuff/<ipython console> in <module>()

/home/carlo/sage/local/lib/python2.5/site-packages/sage/calculus/equations.py
in solve_mod(eqns, modulus)
  1339     S = MPolynomialRing(R, len(vars), vars)
  1340     eqns_mod = [S(eq) if is_SymbolicExpression(eq) else \
-> 1341                   S(eq.lhs() - eq.rhs()) for eq in eqns]
  1342
  1343     ans = []

/home/carlo/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring.py
in __call__(self, x, check)
   380
   381         elif hasattr(x, '_polynomial_'):
--> 382             return x._polynomial_(self)
   383
   384         elif isinstance(x, str) and x in self.variable_names():

/home/carlo/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py
in _polynomial_(self, R)
  1809         if len(sub) == 0:
  1810             try:
-> 1811                 return R(B(self))
  1812             except TypeError:
  1813                 if len(vars) == 1:

/home/carlo/sage/local/lib/python2.5/site-packages/sage/rings/integer_mod_ring.py
in __call__(self, x)
   574     def __call__(self, x):
   575         try:
--> 576             return integer_mod.IntegerMod(self, x)
   577         except (NotImplementedError, PariError):
   578             return TypeError, "error coercing to finite field"

/home/carlo/work/sagestuff/integer_mod.pyx in
sage.rings.integer_mod.IntegerMod (sage/rings/integer_mod.c:1731)()

/home/carlo/work/sagestuff/integer_mod.pyx in
sage.rings.integer_mod.IntegerMod_int.__init__
(sage/rings/integer_mod.c:10153)()

/home/carlo/work/sagestuff/integer_ring.pyx in
sage.rings.integer_ring.IntegerRing_class.__call__
(sage/rings/integer_ring.c:4473)()

<type 'exceptions.TypeError'>: unable to convert x (=x - y) to an integer



Any ideas?

--
Carlo Hamalainen
```



---

Comment by mhansen created at 2008-05-08 04:56:23

The underlying issue is that the reprs of the generators of polynomial rings over Z/2Z have minus signs and SymbolicArithmetic._polynomial_ expects them to not have the signs.  I think the appropriate fix would be to fix the printing for the generators of polynomial rings over Z/2Z


```
sage: Integers(3)['x,y'].gens()
(x, y)
sage: Integers(2)['x,y'].gens()
(-x, -y)
```




```
        for v in vars:
            r = repr(v)
            for g in G:
                if repr(g) == r:
                    sub.append((v,g))
```



---

Comment by mhansen created at 2009-01-21 21:02:38

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-21 21:02:38

This patch also fixes #3125.


---

Comment by mhansen created at 2009-01-21 21:02:38

Changing assignee from somebody to mhansen.


---

Attachment

And by #3125, I mean #3135.


---

Comment by AlexGhitza created at 2009-01-21 23:57:08

Looks good to me.


---

Comment by mabshoff created at 2009-01-23 08:35:32

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 08:35:32

Merged in Sage 3.3.alpha1
