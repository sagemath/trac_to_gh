# Issue 4284: modular symbols -- applying Hecke operator on cuspidal subspace broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-14 14:38:35

Assignee: citro

Bug in sage-3.1.2:


```
sage: M = ModularSymbols(11).cuspidal_subspace(); M.hecke_operator(3)(M.0)

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/wstein/<ipython console> in <module>()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/modular/hecke/hecke_operator.py in __call__(self, x)
    127         """
    128         T = self.hecke_module_morphism()
--> 129         return T(x)
    130
    131     def __rmul__(self, left):

/home/wstein/sage/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.py in __call__(self, x)
    115             x = x.element()
    116         else:
--> 117             x = self.domain().coordinate_vector(x)
    118         v = x*self.matrix()
    119         C = self.codomain()

AttributeError: 'ModularSymbolsSubspace' object has no attribute 'coordinate_vector'
```



---

Comment by craigcitro created at 2008-10-17 09:47:11

Changing status from new to assigned.


---

Attachment

Yep, this just wasn't tested at all. Fixed it, added some doctests.


---

Comment by craigcitro created at 2008-10-17 09:47:11

Changing assignee from citro to craigcitro.


---

Comment by was created at 2008-10-17 13:10:11

Looks good!


---

Comment by mabshoff created at 2008-10-18 09:29:31

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 09:29:31

Merged in Sage 3.2.alpha0
