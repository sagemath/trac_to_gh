# Issue 461: ModularForms(*,*).new_subspace() bug

Issue created by migration from Trac.

Original creator: burhanud

Original creation time: 2007-08-19 18:38:29

Assignee: was

Invoking the new_subspace on a certain ModularForms object raises an exception (but then things seems to work fine after that). --- Ifti


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8, Release Date: 2007-08-12                         |
| Type notebook() for the GUI, and license() for information.        |

sage: M = ModularForms(17,4)

sage: N = M.new_subspace()
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/burhanud/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modform/space.py in new_subspace(self, p)
    893         Synonym for new_submodule.
    894         """
--> 895         return self.new_submodule(p)
    896 
    897     def eisenstein_subspace(self):

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modform/ambient.py in new_submodule(self, p)
    267 
    268         if p is None:
--> 269             M = self._full_new_submodule()
    270             self.__new_submodule[None] = M
    271             return M

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modform/ambient.py in _full_new_submodule(self)
    283         B = range(s) + range(d, d+e)
    284         V = self.module()
--> 285         W = V.submodule([V.gen(i) for i in B])
    286         return submodule.ModularFormsSubmodule(self, W)
    287 

/home/was/s/local/lib/python2.5/site-packages/sage/modules/free_module.py in gen(self, i)
    872     def gen(self, i=0):
    873         if i < 0 or i >= self.rank():
--> 874             raise ValueError, "Generator %s not defined."%i
    875         return self.basis()[int(i)]
    876 

<type 'exceptions.ValueError'>: Generator 6 not defined.

sage: N = M.new_subspace()

sage: N.basis()
 
[
q + 2*q^5 + O(q^6),
q^2 - 3/2*q^5 + O(q^6),
q^3 + O(q^6),
q^4 - 1/2*q^5 + O(q^6)
]
```



---

Comment by was created at 2007-09-07 04:06:12

Resolution: fixed
