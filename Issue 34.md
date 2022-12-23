# Issue 34: Bug in is_simple() for a space of ModularSymbols

Issue created by migration from https://trac.sagemath.org/ticket/34

Original creator: was

Original creation time: 2006-09-12 23:28:51

Assignee: somebody


```
   sage: M = ModularSymbols(Gamma0(22),2,sign=1)
   sage: M1 = M.decomposition()[1]
   sage: M1
   Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 5 for Gamma_0(22) of weight 2 with sign 1 over Rational Field
   sage: M1.is_simple() ## throws a TypeError
```


In fact, I can find lots of examples where this happens: levels 6, 7, 8, and 9 with weight 24 all have subspaces which crash is_simple.

I don't really know if this qualifies as "critical," but it seems more than just "annoying." Maybe the page name should be clarified (at least to me)?

-- Craig Citro




---

Comment by ncalexan created at 2007-02-19 22:06:58

Added doctest to sage/modular/modsym/subspace.py exposing related bug.  As of 2.1.5, does not pass.


---

Comment by ncalexan created at 2007-02-19 22:06:58

Changing assignee from somebody to was.


---

Comment by ncalexan created at 2007-02-19 22:06:58

Changing component from basic arithmetic to modular forms.


---

Comment by was created at 2007-08-16 09:45:34

Changing type from defect to enhancement.


---

Comment by was created at 2007-08-16 09:45:34

This throws notimplemented error now.  The problem is that actually implementing this in general efficiently is hard.  Because it's now a not implemented error, I've changed this to an enhancement.


---

Comment by mabshoff created at 2007-08-28 11:59:15

This is still a problem with Sage 2.8.2:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2, Release Date: 2007-08-22                       |
| Type notebook() for the GUI, and license() for information.        |
sage: M = ModularSymbols(Gamma0(22),2,sign=1)
sage: M1 = M.decomposition()[1]
sage: M1
Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 5 for Gamma_0(22) of weight 2 with sign 1 over Rational Field
sage: M1.is_simple()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/tmp/Work2/sage-2.8.2/<ipython console> in <module>()

/tmp/Work2/sage-2.8.2/local/lib/python2.5/site-packages/sage/modular/modsym/space.py in is_simple(self)
    234             return self._is_simple
    235         except AttributeError:
--> 236             D = self.factorization()
    237             if len(D) == 0 or len(D) == 1 and D[0][1] == 1:
    238                 self._is_simple = True

/tmp/Work2/sage-2.8.2/local/lib/python2.5/site-packages/sage/modular/modsym/subspace.py in factorization(self)
    197         if r != s:
    198             raise NotImplementedError, "modular symbols factorization not fully implemented yet --  self has dimension %s, but sum of dimensions of factors is %s"%(
--> 199             r, s)
    200         self._factorization = sage.structure.factorization.Factorization(D, cr=True)
    201         return self._factorization

<type 'exceptions.NotImplementedError'>: modular symbols factorization not fully implemented yet --  self has dimension 3, but sum of dimensions of factors is 2
sage:    
```


Maybe something worth fixing during the next bug day.

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-04-19 01:59:39

This, as well as the other cases listed in Craig's post, work for me in sage-3.0.alpha5.

I think this was fixed as a side effect of Craig's various fixes in the modular symbols code.


---

Comment by mabshoff created at 2008-04-19 21:20:01

Resolution: fixed


---

Comment by mabshoff created at 2008-04-19 21:20:01

Fixed in Sage 3.0.rc0 due to patches by Creg Citro merged earlier in the 3.0 alpha cycle.
