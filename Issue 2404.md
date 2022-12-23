# Issue 2404: subs_expr claims to take a dictionary, but doesn't

Issue created by migration from https://trac.sagemath.org/ticket/2404

Original creator: ddrake

Original creation time: 2008-03-06 09:49:43

Assignee: was

Keywords: calculus, substitution, subs_expr

The docstring for subs_expr (in calculus.py) says:

> Given a dictionary of key:value pairs, substitute all occurences of key for value in self.

...but the function does not accept a dictionary:


```
def subs_expr(self, *equations):
```


It'll take an arbitrary number of regular parameters (which must be SymbolicEquations), but not a dictionary.

I tried to modify the function to something like the following, but couldn't get it to work. Someone familiar with this code should have no problem implementing it correctly:


```
def subs_expr(self, *equations, **equationsdict):
  for x in equations:
    if not isinstance(x, SymbolicEquation):
      raise TypeError, "each expression must be an equation"

  R = self.parent()
  v = ','.join(['%s=%s'%(x.lhs()._maxima_init_(), x.rhs()._maxima_init_()) \
                    for x in equations])
  v = v + ','.join(['%s=%s' % (key._maxima_init_(), \
    equationsdict[key]._maxima_init_()) for key in equationsdict.keys()]
  return R(self._maxima_().subst(v))
```





---

Attachment

The attached patch fixes subs_expr to take a dictionary, adds an appropriate doctest, and clarifies the docstring a bit.


---

Comment by mhansen created at 2009-01-24 03:07:00

Looks good to me.


---

Comment by mabshoff created at 2009-01-28 14:41:44

Note that the following in the patch needs to be changed

```
The following test shows that \#4364 is indeed fixed.
```

I did so in the patch I applied.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 15:17:27

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 15:17:27

Merged in Sage 3.3.alpha3.

Cheers,

Michael
