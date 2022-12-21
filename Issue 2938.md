# Issue 2938: ModularSymbols(GammaH(81, [10])).decomposition(); ModularSymbols(GammaH(8, [3])).decomposition()

Issue created by migration from Trac.

Original creator: burhanud

Original creation time: 2008-04-16 00:23:12

Assignee: craigcitro


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version sage-2.11, Release Date: 2008-03-30                   |
| Type notebook() for the GUI, and license() for information.        |

sage: G = GammaH(81, [10])

sage: M = ModularSymbols(G)

sage: D = M.decomposition()
---------------------------------------------------------------------------
<type 'exceptions.KeyError'>              Traceback (most recent call 
last)

/home/burhanud/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/modular/hecke/module.py 
in decomposition(self, bound, anemic, compute_dual, height_guess, proof)
    605             self.__is_splittable_anemic = len(D) > 1
    606 
--> 607         D.sort()
    608         D.set_immutable()
    609         self.__decomposition[key] = D

/home/was/s/local/lib/python2.5/site-packages/sage/structure/sequence.py 
in sort(self, cmp, key, reverse)
    392         """
    393         self._require_mutable()
--> 394         list.sort(self, cmp=cmp, key=key, reverse=reverse)
    395 
    396     def __hash__(self):

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/space.py 
in __cmp__(self, other)
    103         # distinguish using Hecke operators, if possible.
    104         try:
--> 105             for p in arith.prime_range(self.hecke_bound()):
    106                 ap = self.hecke_matrix(p).trace()
    107                 bp = other.hecke_matrix(p).trace()

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/subspace.py 
in hecke_bound(self)

    298             53
    299         """
--> 300         if self.is_cuspidal():
    301             return self.sturm_bound()
    302         else:

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/subspace.py 
in is_cuspidal(self)
    316             return self.__is_cuspidal
    317         except AttributeError:
--> 318             C = self.ambient_hecke_module().cuspidal_submodule()
    319             self.__is_cuspidal = self.is_submodule(C)
    320             return self.__is_cuspidal

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py 
in cuspidal_submodule(self)
    809             return self.__cuspidal_submodule
    810         except AttributeError:
--> 811             S = self.boundary_map().kernel()
    812             S._is_full_hecke_module = True
    813             ## We know the cuspidal subspace is stable, so

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py 
in boundary_map(self)
    765             # compute boundary map
    766             B = self.boundary_space()
--> 767             I = [B(b) for b in self.basis()]
    768             W = matrix_space.MatrixSpace(self.base_ring(), len(I), 
B.rank(), sparse=True)
    769 

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in __call__(self, x)
    260             if len(S) == 0:
    261                 return self(0)
--> 262             return sum([c*self._coerce_in_manin_symbol(v) for c, v 
in S])
    263 
    264         elif is_FreeModuleElement(x):

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _coerce_in_manin_symbol(self, x)
    225         alpha, beta = x.endpoints(self.level())
    226         if self.weight() == 2:
--> 227             return self(alpha) - self(beta)
    228         if i == 0:
    229             return self(alpha)

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in __call__(self, x)
    245 
    246         elif isinstance(x, cusps.Cusp):
--> 247             return self._coerce_cusp(x)
    248 
    249         elif manin_symbols.is_ManinSymbol(x):

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _coerce_cusp(self, c)
    550         k    = self.weight()
    551         sign = self.sign()
--> 552         i, eps = self._cusp_index(c)
    553         if i != -1:
    554             if i in self._is_zero:

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _cusp_index(self, cusp)
    538         N = self.level()
    539         for i in xrange(len(g)):
--> 540             t, eps = self._is_equiv(cusp, g[i])
    541             if t:
    542                 return i, eps

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _is_equiv(self, c1, c2)
    532 
    533     def _is_equiv(self, c1, c2):
--> 534         return c1.is_gamma_h_equiv(c2, self.group())
    535 
    536     def _cusp_index(self, cusp):

/home/was/s/local/lib/python2.5/site-packages/sage/modular/cusps.py in 
is_gamma_h_equiv(self, other, G)
    591 
    592         # Coset reduction data
--> 593         c1, t1 = G._reduce_cusp(self)
    594         c2, t2 = G._reduce_cusp(other)
    595         return c1 == c2, t1*t2

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.py in 
_reduce_cusp(self, c)
    937             return u,v, h
    938 
--> 939         u, v, h = f(u,v)
    940         N_over_2 = N//2
    941         if u > N_over_2:

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.py in 
f(u, v)
    927                 return 0, 1, h
    928             u = (hinv * u) % d
--> 929             H_cong1_mod_N_over_d = second[d]
    930             if len(H_cong1_mod_N_over_d) > 1:
    931                 umin = u

<type 'exceptions.KeyError'>: 27





sage: G = GammaH(8, [3])

sage: M = ModularSymbols(G)

sage: D = M.decomposition()

sage: D
 
[
Modular Symbols subspace of dimension 3 of Modular Symbols space of 
dimension 3 for Congruence Subgroup Gamma_H(8) with H generated by [3] of 
weight 2 with sign 0 and over Rational Field
]

sage: D[0].is_cuspidal()
---------------------------------------------------------------------------
<type 'exceptions.KeyError'>              Traceback (most recent call 
last)

/home/burhanud/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/subspace.py 
in is_cuspidal(self)
    316             return self.__is_cuspidal
    317         except AttributeError:
--> 318             C = self.ambient_hecke_module().cuspidal_submodule()
    319             self.__is_cuspidal = self.is_submodule(C)
    320             return self.__is_cuspidal

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py 
in cuspidal_submodule(self)
    809             return self.__cuspidal_submodule
    810         except AttributeError:
--> 811             S = self.boundary_map().kernel()
    812             S._is_full_hecke_module = True
    813             ## We know the cuspidal subspace is stable, so

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py 
in boundary_map(self)
    765             # compute boundary map
    766             B = self.boundary_space()
--> 767             I = [B(b) for b in self.basis()]
    768             W = matrix_space.MatrixSpace(self.base_ring(), len(I), 
B.rank(), sparse=True)
    769 

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in __call__(self, x)
    260             if len(S) == 0:
    261                 return self(0)
--> 262             return sum([c*self._coerce_in_manin_symbol(v) for c, v 
in S])
    263 
    264         elif is_FreeModuleElement(x):

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _coerce_in_manin_symbol(self, x)
    225         alpha, beta = x.endpoints(self.level())
    226         if self.weight() == 2:
--> 227             return self(alpha) - self(beta)
    228         if i == 0:
    229             return self(alpha)

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in __call__(self, x)
    245 
    246         elif isinstance(x, cusps.Cusp):
--> 247             return self._coerce_cusp(x)
    248 
    249         elif manin_symbols.is_ManinSymbol(x):

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _coerce_cusp(self, c)
    550         k    = self.weight()
    551         sign = self.sign()
--> 552         i, eps = self._cusp_index(c)
    553         if i != -1:
    554             if i in self._is_zero:

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _cusp_index(self, cusp)
    538         N = self.level()
    539         for i in xrange(len(g)):
--> 540             t, eps = self._is_equiv(cusp, g[i])
    541             if t:
    542                 return i, eps

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _is_equiv(self, c1, c2)
    532 
    533     def _is_equiv(self, c1, c2):
--> 534         return c1.is_gamma_h_equiv(c2, self.group())
    535 
    536     def _cusp_index(self, cusp):

/home/was/s/local/lib/python2.5/site-packages/sage/modular/cusps.py in 
is_gamma_h_equiv(self, other, G)
    591 
    592         # Coset reduction data
--> 593         c1, t1 = G._reduce_cusp(self)
    594         c2, t2 = G._reduce_cusp(other)
    595         return c1 == c2, t1*t2

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.py in 
_reduce_cusp(self, c)
    937             return u,v, h
    938 
--> 939         u, v, h = f(u,v)
    940         N_over_2 = N//2
    941         if u > N_over_2:

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _coerce_in_manin_symbol(self, x)
    225         alpha, beta = x.endpoints(self.level())
    226         if self.weight() == 2:
--> 227             return self(alpha) - self(beta)
    228         if i == 0:
    229             return self(alpha)

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in __call__(self, x)
    245 
    246         elif isinstance(x, cusps.Cusp):
--> 247             return self._coerce_cusp(x)
    248 
    249         elif manin_symbols.is_ManinSymbol(x):

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _coerce_cusp(self, c)
    550         k    = self.weight()
    551         sign = self.sign()
--> 552         i, eps = self._cusp_index(c)
    553         if i != -1:
    554             if i in self._is_zero:

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _cusp_index(self, cusp)
    538         N = self.level()
    539         for i in xrange(len(g)):
--> 540             t, eps = self._is_equiv(cusp, g[i])
    541             if t:
    542                 return i, eps

/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py 
in _is_equiv(self, c1, c2)
    532 
    533     def _is_equiv(self, c1, c2):
--> 534         return c1.is_gamma_h_equiv(c2, self.group())
    535 
    536     def _cusp_index(self, cusp):

/home/was/s/local/lib/python2.5/site-packages/sage/modular/cusps.py in 
is_gamma_h_equiv(self, other, G)
    591 
    592         # Coset reduction data
--> 593         c1, t1 = G._reduce_cusp(self)
    594         c2, t2 = G._reduce_cusp(other)
    595         return c1 == c2, t1*t2

/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.py in 
_reduce_cusp(self, c)
    937             return u,v, h
    938 
--> 939         u, v, h = f(u,v)
    940         N_over_2 = N//2
    941         if u > N_over_2:



```



---

Comment by craigcitro created at 2008-04-26 18:27:29

The patch at #2523 fixes this, too. (It was the same problem with data generated to determine GammaH-equivalence.)


---

Comment by craigcitro created at 2008-04-26 18:27:29

Resolution: fixed


---

Comment by mabshoff created at 2008-04-26 20:45:21

Replying to [comment:2 craigcitro]:
> The patch at #2523 fixes this, too. (It was the same problem with data generated to determine GammaH-equivalence.)

Craig,

since you asked about this in IRC: The procedure you did, i.e. mentioning which ticket fixed the issue is fine. You are certainly an expert in the area, so that closing the ticket is also fine by me. The only thing you didn't do correctly is wait for the fixing patch to be applied since we only close tickets that have been fixed in the official release. But since #2523 will be merged in seconds that is a moot point. So overall I am perfectly fine with you closing this ticket, thanks for staying on top of this ;)

Re Credit for tickets closed by other patches: It depends, i.e. if it is discovered a release or two later I usually do not list it in the release notes. If it is the same release and clearly not a dupe tickets I will list both tickets like in this case.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-26 21:16:18

I am wondering now if it would be useful to add a doctest for this failure just to verify that the bug is *actually* fixed. Not that I don't trust Craig, but it is policy after all ;)

If you post a doctest patch no point in reopening the ticket. Just comment that a patch is available and I will merge it.

Cheers,

Michael


---

Comment by craigcitro created at 2008-04-26 23:04:54

Changing status from closed to reopened.


---

Comment by craigcitro created at 2008-04-26 23:04:54

Good point, mabshoff. Adding patch with doctests.


---

Comment by craigcitro created at 2008-04-26 23:04:54

Resolution changed from fixed to 


---

Attachment


---

Comment by mabshoff created at 2008-04-26 23:08:36

Resolution: fixed


---

Comment by mabshoff created at 2008-04-26 23:08:36

Merged in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-26 23:10:13

Patch looks good and passes the doctest it adds ;)

Cheers,

Michael
