# Issue 7424: inconsistency between constructors SL and PSL

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-11-10 22:51:48

Assignee: joyner

Probably because these are implemented as different classes (matrix group versus permutation group), the constructors for `SL` and `PSL` have slightly different behaviour.  In particular, `PSL` does not take a field argument, and the error message it gives is misleading.  We should just make it behave exactly like `SL`:


```
[ghitza`@`artin ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: SL(2, 7)
Special Linear Group of degree 2 over Finite Field of size 7
sage: SL(2, GF(7))
Special Linear Group of degree 2 over Finite Field of size 7
sage: PSL(2, 7)
Permutation Group with generators [(3,7,5)(4,8,6), (1,2,6)(3,4,8)]
sage: PSL(2, GF(7))
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 4.2, Release Date: 2009-10-24                         |
| Type notebook() for the GUI, and license() for information.        |
/home/ghitza/.sage/temp/artin/31630/_home_ghitza__sage_init_sage_0.py in <module>()

/home/ghitza/sage-stable/local/lib/python2.6/site-packages/sage/groups/perm_gps/permgroup_named.pyc in __init__(self, n, q, name)
    645         else:
    646             id = 'PSL(%s,%s)'%(n,q)
--> 647         PermutationGroup_generic.__init__(self, gap_group=id)
    648         self._q = q
    649         self._base_ring = GF(q, name=name)

/home/ghitza/sage-stable/local/lib/python2.6/site-packages/sage/groups/perm_gps/permgroup.pyc in __init__(self, gens, gap_group, canonicalize)
    334         if gens is None:
    335             self._gap_string = gap_group if isinstance(gap_group, str) else str(gap_group)
--> 336             self._gens = self._gens_from_gap()
    337             return
    338 

/home/ghitza/sage-stable/local/lib/python2.6/site-packages/sage/groups/perm_gps/permgroup.pyc in _gens_from_gap(self)
    363             gens = self._gap_().GeneratorsOfGroup()
    364         except TypeError, s:
--> 365             raise RuntimeError, "(It might be necessary to install the database_gap optional Sage package, if you haven't already.)\n%s"%s
    366         gens = [self._element_class()(gens[n],self, check=False)
    367                        for n in range(1, int(gens.Length())+1)]

RuntimeError: (It might be necessary to install the database_gap optional Sage package, if you haven't already.)
Gap produced error output
Variable: 'Finite' must have a value

Syntax error: ) expected
$sage3:=PSL(2,Finite Field of size 7);;
                         ^

   executing $sage3:=PSL(2,Finite Field of size 7);;
```




---

Attachment

here is a patch, that also cleans a bit the doc


---

Comment by AlexGhitza created at 2013-08-02 20:39:04

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2013-08-02 20:41:08

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-20 12:57:30

Resolution: fixed
