# Issue 1232: bug in modular symbols over GF(2)

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2007-11-21 03:49:42

Assignee: was

Running


```
ModularSymbols(1,6,0,GF(2)).simple_factors()
```


results in


```
---------------------------------------------------------------------------
<type 'exceptions.AssertionError'>        Traceback (most recent call last)

/home/ghitza/sage/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/modular/modsym/space.py in simple_factors(self)
    996         ASSUMPTION: self is a module over the anemic Hecke algebra.
    997         """
--> 998         return [S for S,_ in self.factorization()]
    999 
   1000     def star_eigenvalues(self):

/opt/sage/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py in factorization(self)
   1064         D = sage.structure.all.Factorization(D, cr=True)
   1065         assert r == s, "bug in factorization --  self has dimension %s, but sum of dimensions of factors is %s\n%s"%(
-> 1066             r, s, D)
   1067         self._factorization = D
   1068         return self._factorization

<type 'exceptions.AssertionError'>: bug in factorization --  self has dimension 2, but sum of dimensions of factors is 3
(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2) * 
(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2) * 
(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 2 for Gamma_0(1) of weight 6 with sign 0 over Finite Field of size 2)
```


Outcome is similar for higher weights, e.g. for weight 100 I get "self has dimension 33, but sum of dimensions of factors is 65".



---

Comment by craigcitro created at 2007-12-02 11:38:33

So the problem here is straightforward to find -- M.factorization() breaks up the cuspidal parts into +1 and -1 eigenspaces; since 1 == -1 mod 2, they all get counted twice (so that the dimension will always be 2*cuspidal part + eisenstein part). The fix is also easy -- if 2 == 0, don't add the minus part in. However, the question is whether the space is still simple in this case, because otherwise we're now producing wrong answers.


---

Attachment


---

Comment by craigcitro created at 2007-12-12 04:34:28

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2007-12-12 04:34:28

Added a fix for this. The issue was what I mentioned above, namely the fact that +1 == -1 in characteristic 2. Alex Ghitza offered the following explanation of why this is a mathematically valid fix:

Here's my line of thought:
-- in Sage, "simple" means "simple as a module over the anemic Hecke
algebra adjoined the star involution *"
-- in characteristic 2, the star involution is actually not an
involution, but rather the identity map, and so "simple" should just
mean "simple as a module over the anemic Hecke algebra", so synonymous
to "splittable_anemic" in Sage terminology
-- the factorization() aka simple_factors() function for modular
symbols uses the HeckeModule_free_module.decomposition() function,
which implements an algorithm that breaks up the module as much as
possible using the anemic Hecke algebra; therefore the resulting
factors are "splittable_anemic", and so "simple" (for char 2).

The attached patch fixes the problem, and adds a doctest or two.


---

Comment by craigcitro created at 2007-12-12 04:34:28

Changing status from new to assigned.


---

Comment by was created at 2007-12-15 06:30:24

This is good (ok and better than before).  Note however that in a lot of cases simple_factors still won't work (due to the algorithm not really being meant for GF(p) -- instead one should use decomposition):


```
sage: n = ModularSymbols(54,weight=2,base_ring=GF(2)); n
Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2
sage: m =n.new_subspace()
sage: n.simple_factors()
Traceback (most recent call last):
...
AssertionError: bug in factorization --  self has dimension 19, but sum of dimensions of factors is 11
(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 1 for Gamma_0(2) of weight 2 with sign 0 over Finite Field of size 2)^7 * 
(Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 for Gamma_0(27) of weight 2 with sign 0 over Finite Field of size 2)^2 * 
(Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2)
sage: m.simple_factors()
[Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2, Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2]
sage: f = n.decomposition(5)
sage: f
[
Modular Symbols subspace of dimension 4 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2,
Modular Symbols subspace of dimension 15 of Modular Symbols space of dimension 19 for Gamma_0(54) of weight 2 with sign 0 over Finite Field of size 2
]
```



---

Comment by mabshoff created at 2007-12-15 06:49:14

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 06:49:14

Merged in 2.9.rc0.
