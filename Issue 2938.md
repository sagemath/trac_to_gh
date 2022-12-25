# Issue 2938: ModularSymbols(GammaH(81, [10])).decomposition(); ModularSymbols(GammaH(8, [3])).decomposition()

archive/issues_002938.json:
```json
{
    "body": "Assignee: @craigcitro\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version sage-2.11, Release Date: 2008-03-30                   |\n| Type notebook() for the GUI, and license() for information.        |\n\nsage: G = GammaH(81, [10])\n\nsage: M = ModularSymbols(G)\n\nsage: D = M.decomposition()\n---------------------------------------------------------------------------\n<type 'exceptions.KeyError'>              Traceback (most recent call \nlast)\n\n/home/burhanud/<ipython console> in <module>()\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/hecke/module.py \nin decomposition(self, bound, anemic, compute_dual, height_guess, proof)\n    605             self.__is_splittable_anemic = len(D) > 1\n    606 \n--> 607         D.sort()\n    608         D.set_immutable()\n    609         self.__decomposition[key] = D\n\n/home/was/s/local/lib/python2.5/site-packages/sage/structure/sequence.py \nin sort(self, cmp, key, reverse)\n    392         \"\"\"\n    393         self._require_mutable()\n--> 394         list.sort(self, cmp=cmp, key=key, reverse=reverse)\n    395 \n    396     def __hash__(self):\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/space.py \nin __cmp__(self, other)\n    103         # distinguish using Hecke operators, if possible.\n    104         try:\n--> 105             for p in arith.prime_range(self.hecke_bound()):\n    106                 ap = self.hecke_matrix(p).trace()\n    107                 bp = other.hecke_matrix(p).trace()\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/subspace.py \nin hecke_bound(self)\n\n    298             53\n    299         \"\"\"\n--> 300         if self.is_cuspidal():\n    301             return self.sturm_bound()\n    302         else:\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/subspace.py \nin is_cuspidal(self)\n    316             return self.__is_cuspidal\n    317         except AttributeError:\n--> 318             C = self.ambient_hecke_module().cuspidal_submodule()\n    319             self.__is_cuspidal = self.is_submodule(C)\n    320             return self.__is_cuspidal\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py \nin cuspidal_submodule(self)\n    809             return self.__cuspidal_submodule\n    810         except AttributeError:\n--> 811             S = self.boundary_map().kernel()\n    812             S._is_full_hecke_module = True\n    813             ## We know the cuspidal subspace is stable, so\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py \nin boundary_map(self)\n    765             # compute boundary map\n    766             B = self.boundary_space()\n--> 767             I = [B(b) for b in self.basis()]\n    768             W = matrix_space.MatrixSpace(self.base_ring(), len(I), \nB.rank(), sparse=True)\n    769 \n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin __call__(self, x)\n    260             if len(S) == 0:\n    261                 return self(0)\n--> 262             return sum([c*self._coerce_in_manin_symbol(v) for c, v \nin S])\n    263 \n    264         elif is_FreeModuleElement(x):\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _coerce_in_manin_symbol(self, x)\n    225         alpha, beta = x.endpoints(self.level())\n    226         if self.weight() == 2:\n--> 227             return self(alpha) - self(beta)\n    228         if i == 0:\n    229             return self(alpha)\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin __call__(self, x)\n    245 \n    246         elif isinstance(x, cusps.Cusp):\n--> 247             return self._coerce_cusp(x)\n    248 \n    249         elif manin_symbols.is_ManinSymbol(x):\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _coerce_cusp(self, c)\n    550         k    = self.weight()\n    551         sign = self.sign()\n--> 552         i, eps = self._cusp_index(c)\n    553         if i != -1:\n    554             if i in self._is_zero:\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _cusp_index(self, cusp)\n    538         N = self.level()\n    539         for i in xrange(len(g)):\n--> 540             t, eps = self._is_equiv(cusp, g[i])\n    541             if t:\n    542                 return i, eps\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _is_equiv(self, c1, c2)\n    532 \n    533     def _is_equiv(self, c1, c2):\n--> 534         return c1.is_gamma_h_equiv(c2, self.group())\n    535 \n    536     def _cusp_index(self, cusp):\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/cusps.py in \nis_gamma_h_equiv(self, other, G)\n    591 \n    592         # Coset reduction data\n--> 593         c1, t1 = G._reduce_cusp(self)\n    594         c2, t2 = G._reduce_cusp(other)\n    595         return c1 == c2, t1*t2\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.py in \n_reduce_cusp(self, c)\n    937             return u,v, h\n    938 \n--> 939         u, v, h = f(u,v)\n    940         N_over_2 = N//2\n    941         if u > N_over_2:\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.py in \nf(u, v)\n    927                 return 0, 1, h\n    928             u = (hinv * u) % d\n--> 929             H_cong1_mod_N_over_d = second[d]\n    930             if len(H_cong1_mod_N_over_d) > 1:\n    931                 umin = u\n\n<type 'exceptions.KeyError'>: 27\n\n\n\n\n\nsage: G = GammaH(8, [3])\n\nsage: M = ModularSymbols(G)\n\nsage: D = M.decomposition()\n\nsage: D\n \n[\nModular Symbols subspace of dimension 3 of Modular Symbols space of \ndimension 3 for Congruence Subgroup Gamma_H(8) with H generated by [3] of \nweight 2 with sign 0 and over Rational Field\n]\n\nsage: D[0].is_cuspidal()\n---------------------------------------------------------------------------\n<type 'exceptions.KeyError'>              Traceback (most recent call \nlast)\n\n/home/burhanud/<ipython console> in <module>()\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/subspace.py \nin is_cuspidal(self)\n    316             return self.__is_cuspidal\n    317         except AttributeError:\n--> 318             C = self.ambient_hecke_module().cuspidal_submodule()\n    319             self.__is_cuspidal = self.is_submodule(C)\n    320             return self.__is_cuspidal\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py \nin cuspidal_submodule(self)\n    809             return self.__cuspidal_submodule\n    810         except AttributeError:\n--> 811             S = self.boundary_map().kernel()\n    812             S._is_full_hecke_module = True\n    813             ## We know the cuspidal subspace is stable, so\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py \nin boundary_map(self)\n    765             # compute boundary map\n    766             B = self.boundary_space()\n--> 767             I = [B(b) for b in self.basis()]\n    768             W = matrix_space.MatrixSpace(self.base_ring(), len(I), \nB.rank(), sparse=True)\n    769 \n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin __call__(self, x)\n    260             if len(S) == 0:\n    261                 return self(0)\n--> 262             return sum([c*self._coerce_in_manin_symbol(v) for c, v \nin S])\n    263 \n    264         elif is_FreeModuleElement(x):\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _coerce_in_manin_symbol(self, x)\n    225         alpha, beta = x.endpoints(self.level())\n    226         if self.weight() == 2:\n--> 227             return self(alpha) - self(beta)\n    228         if i == 0:\n    229             return self(alpha)\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin __call__(self, x)\n    245 \n    246         elif isinstance(x, cusps.Cusp):\n--> 247             return self._coerce_cusp(x)\n    248 \n    249         elif manin_symbols.is_ManinSymbol(x):\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _coerce_cusp(self, c)\n    550         k    = self.weight()\n    551         sign = self.sign()\n--> 552         i, eps = self._cusp_index(c)\n    553         if i != -1:\n    554             if i in self._is_zero:\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _cusp_index(self, cusp)\n    538         N = self.level()\n    539         for i in xrange(len(g)):\n--> 540             t, eps = self._is_equiv(cusp, g[i])\n    541             if t:\n    542                 return i, eps\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _is_equiv(self, c1, c2)\n    532 \n    533     def _is_equiv(self, c1, c2):\n--> 534         return c1.is_gamma_h_equiv(c2, self.group())\n    535 \n    536     def _cusp_index(self, cusp):\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/cusps.py in \nis_gamma_h_equiv(self, other, G)\n    591 \n    592         # Coset reduction data\n--> 593         c1, t1 = G._reduce_cusp(self)\n    594         c2, t2 = G._reduce_cusp(other)\n    595         return c1 == c2, t1*t2\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.py in \n_reduce_cusp(self, c)\n    937             return u,v, h\n    938 \n--> 939         u, v, h = f(u,v)\n    940         N_over_2 = N//2\n    941         if u > N_over_2:\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _coerce_in_manin_symbol(self, x)\n    225         alpha, beta = x.endpoints(self.level())\n    226         if self.weight() == 2:\n--> 227             return self(alpha) - self(beta)\n    228         if i == 0:\n    229             return self(alpha)\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin __call__(self, x)\n    245 \n    246         elif isinstance(x, cusps.Cusp):\n--> 247             return self._coerce_cusp(x)\n    248 \n    249         elif manin_symbols.is_ManinSymbol(x):\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _coerce_cusp(self, c)\n    550         k    = self.weight()\n    551         sign = self.sign()\n--> 552         i, eps = self._cusp_index(c)\n    553         if i != -1:\n    554             if i in self._is_zero:\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _cusp_index(self, cusp)\n    538         N = self.level()\n    539         for i in xrange(len(g)):\n--> 540             t, eps = self._is_equiv(cusp, g[i])\n    541             if t:\n    542                 return i, eps\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.py \nin _is_equiv(self, c1, c2)\n    532 \n    533     def _is_equiv(self, c1, c2):\n--> 534         return c1.is_gamma_h_equiv(c2, self.group())\n    535 \n    536     def _cusp_index(self, cusp):\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/cusps.py in \nis_gamma_h_equiv(self, other, G)\n    591 \n    592         # Coset reduction data\n--> 593         c1, t1 = G._reduce_cusp(self)\n    594         c2, t2 = G._reduce_cusp(other)\n    595         return c1 == c2, t1*t2\n\n/home/was/s/local/lib/python2.5/site-packages/sage/modular/congroup.py in \n_reduce_cusp(self, c)\n    937             return u,v, h\n    938 \n--> 939         u, v, h = f(u,v)\n    940         N_over_2 = N//2\n    941         if u > N_over_2:\n\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2938\n\n",
    "created_at": "2008-04-16T00:23:12Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "ModularSymbols(GammaH(81, [10])).decomposition(); ModularSymbols(GammaH(8, [3])).decomposition()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2938",
    "user": "https://trac.sagemath.org/admin/accounts/users/burhanud"
}
```
Assignee: @craigcitro


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


Issue created by migration from https://trac.sagemath.org/ticket/2938





---

archive/issue_comments_020195.json:
```json
{
    "body": "The patch at #2523 fixes this, too. (It was the same problem with data generated to determine GammaH-equivalence.)",
    "created_at": "2008-04-26T18:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20195",
    "user": "https://github.com/craigcitro"
}
```

The patch at #2523 fixes this, too. (It was the same problem with data generated to determine GammaH-equivalence.)



---

archive/issue_comments_020196.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T18:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20196",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed



---

archive/issue_comments_020197.json:
```json
{
    "body": "Replying to [comment:2 craigcitro]:\n> The patch at #2523 fixes this, too. (It was the same problem with data generated to determine GammaH-equivalence.)\n\nCraig,\n\nsince you asked about this in IRC: The procedure you did, i.e. mentioning which ticket fixed the issue is fine. You are certainly an expert in the area, so that closing the ticket is also fine by me. The only thing you didn't do correctly is wait for the fixing patch to be applied since we only close tickets that have been fixed in the official release. But since #2523 will be merged in seconds that is a moot point. So overall I am perfectly fine with you closing this ticket, thanks for staying on top of this ;)\n\nRe Credit for tickets closed by other patches: It depends, i.e. if it is discovered a release or two later I usually do not list it in the release notes. If it is the same release and clearly not a dupe tickets I will list both tickets like in this case.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T20:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20197",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 craigcitro]:
> The patch at #2523 fixes this, too. (It was the same problem with data generated to determine GammaH-equivalence.)

Craig,

since you asked about this in IRC: The procedure you did, i.e. mentioning which ticket fixed the issue is fine. You are certainly an expert in the area, so that closing the ticket is also fine by me. The only thing you didn't do correctly is wait for the fixing patch to be applied since we only close tickets that have been fixed in the official release. But since #2523 will be merged in seconds that is a moot point. So overall I am perfectly fine with you closing this ticket, thanks for staying on top of this ;)

Re Credit for tickets closed by other patches: It depends, i.e. if it is discovered a release or two later I usually do not list it in the release notes. If it is the same release and clearly not a dupe tickets I will list both tickets like in this case.

Cheers,

Michael



---

archive/issue_comments_020198.json:
```json
{
    "body": "I am wondering now if it would be useful to add a doctest for this failure just to verify that the bug is *actually* fixed. Not that I don't trust Craig, but it is policy after all ;)\n\nIf you post a doctest patch no point in reopening the ticket. Just comment that a patch is available and I will merge it.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T21:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20198",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am wondering now if it would be useful to add a doctest for this failure just to verify that the bug is *actually* fixed. Not that I don't trust Craig, but it is policy after all ;)

If you post a doctest patch no point in reopening the ticket. Just comment that a patch is available and I will merge it.

Cheers,

Michael



---

archive/issue_comments_020199.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-04-26T23:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20199",
    "user": "https://github.com/craigcitro"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_020200.json:
```json
{
    "body": "Good point, mabshoff. Adding patch with doctests.",
    "created_at": "2008-04-26T23:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20200",
    "user": "https://github.com/craigcitro"
}
```

Good point, mabshoff. Adding patch with doctests.



---

archive/issue_comments_020201.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-04-26T23:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20201",
    "user": "https://github.com/craigcitro"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_020202.json:
```json
{
    "body": "Attachment [trac-2938-doc.patch](tarball://root/attachments/some-uuid/ticket2938/trac-2938-doc.patch) by @craigcitro created at 2008-04-26 23:05:12",
    "created_at": "2008-04-26T23:05:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20202",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2938-doc.patch](tarball://root/attachments/some-uuid/ticket2938/trac-2938-doc.patch) by @craigcitro created at 2008-04-26 23:05:12



---

archive/issue_comments_020203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T23:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20203",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020204.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-04-26T23:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20204",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha1



---

archive/issue_comments_020205.json:
```json
{
    "body": "Patch looks good and passes the doctest it adds ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T23:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2938#issuecomment-20205",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good and passes the doctest it adds ;)

Cheers,

Michael
