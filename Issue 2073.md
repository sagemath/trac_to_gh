# Issue 2073: calculus -- get doctest coverage up to 100%

Issue created by migration from https://trac.sagemath.org/ticket/2073

Original creator: was

Original creation time: 2008-02-06 09:00:28

Assignee: was




---

Attachment


---

Attachment


---

Attachment


---

Attachment

As of patch four, these are the only remaining public (not underscored) functions without proper documentation in the entire calculus directory:


```

Missing documentation:
         * subs(self, *args, **kwds)
         * substitute_over_ring(self, in_dict=None, ring=None, **kwds)
         * str(self, bits=None)
         * maxima_init(x)
         * sys_init(x, system)
         * var_cmp(x,y)
         * CallableSymbolicExpressionRing(args, check=True)
         * foo(n)
         * args(self)
         * plot(self, *args, **kwds)
         * tex_needs_braces(self)
         * simplify(self)


Missing doctests:
         * obj(self)
         * variables(self, vars=tuple([]))
         * integral(self, x=None, a=None, b=None)
         * expression(self)
```



---

Comment by was created at 2008-02-06 18:46:59

this is done and ready to be reviewed


---

Attachment

Positive review after applying the last patch as well.


---

Comment by mabshoff created at 2008-02-07 10:05:53

Resolution: fixed


---

Comment by mabshoff created at 2008-02-07 10:05:53

Applied all five patches to Sage 2.10.2.alpha0
