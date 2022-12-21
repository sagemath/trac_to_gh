# Issue 2535: Problem with cuspidal_subspace and new_subspace for modular symbols

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-03-15 23:40:33

Assignee: craigcitro

CC:  alexghitza cremona

There's some error with `plus_submodule` and `cuspidal_submodule` not being "commutative." Here's an example:


```
sage: M = ModularSymbols(11,2)
sage: Mpc = M.plus_submodule().cuspidal_submodule()
sage: Mcp = M.cuspidal_submodule().plus_submodule()

sage: Mcp.q_expansion_basis(10) 
[
q - 2*q^2 - q^3 + 2*q^4 + q^5 + 2*q^6 - 2*q^7 - 2*q^9 + O(q^10)
]

sage: Mpc.q_expansion_basis(10)
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Users/craigcitro/<ipython console> in <module>()

/sage/local/lib/python2.5/site-packages/sage/modular/modsym/space.py in q_expansion_basis(self, prec, algorithm)
    458             algorithm = 'hecke'
    459         if algorithm == 'hecke':
--> 460             return Sequence(self._q_expansion_basis_hecke_dual(prec), cr=True)
    461         elif algorithm == 'eigen':
    462             return Sequence(self._q_expansion_basis_eigen(prec), cr=True)


/sage/local/lib/python2.5/site-packages/sage/modular/modsym/space.py in _q_expansion_basis_hecke_dual(self, prec)
    913         t = misc.verbose('computing basis to precision %s'%prec)
    914         while V.dimension() < d and i >= 0:
--> 915             v = [self.dual_hecke_matrix(n).column(i) for n in range(1,prec)]
    916             t = misc.verbose('iteration: %s'%j,t)
    917             X = M(v).transpose()

/sage/local/lib/python2.5/site-packages/sage/modular/hecke/module.py in dual_hecke_matrix(self, n)
    725             self._dual_hecke_matrices = {}
    726         if not self._dual_hecke_matrices.has_key(n):
--> 727             T = self._compute_dual_hecke_matrix(n)
    728             self._dual_hecke_matrices[n] = T
    729         return self._dual_hecke_matrices[n]

/sage/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py in _compute_dual_hecke_matrix(self, n)
    108         A = self.ambient_hecke_module().dual_hecke_matrix(n)
    109         check =  arith.gcd(self.level(), n) != 1
--> 110         return A.restrict(self.dual_free_module(), check=check)
    111 
    112     def _compute_hecke_matrix(self, n):

/sage/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py in dual_free_module(self, bound, anemic)
    295                 # failed
    296                 raise RuntimeError, "Computation of embedded dual vector space failed " + \
--> 297                       "(cut down to rank %s, but should have cut down to rank %s)."%(V.rank(), self.rank())
    298 
    299 

<type 'exceptions.RuntimeError'>: Computation of embedded dual vector space failed (cut down to rank 2, but should have cut down to rank 1).
```


I'll look at this soon.


---

Comment by craigcitro created at 2008-04-06 10:16:07

The underlying bug was that we didn't use the star operator in addition to the Hecke operators when trying to determine the dual space to a space of modular symbols. I added this in, though there are several choices as to how to best do that. I added in at least two of these, and added a flag that chooses between them. I tested a handful of small examples, and picked the clear winner on these examples as a default. We should revisit this at some point and decide if that's really the best choice, or if there are tradeoffs with weight vs. level, etc.

I also added a few doctests here and there, since I was at it.


---

Comment by craigcitro created at 2008-04-06 10:16:07

Changing status from new to assigned.


---

Comment by ncalexan created at 2008-04-11 05:08:35

Patch looks good -- code is clean, doctests are good.

I cannot be the only judge on this patch because I am not expert in the functionality.

One change I would advocate is documenting the choices for `use_sign`.  See the source is not the best documentation :)


---

Comment by was created at 2008-04-12 00:51:40

Negative review, since the code doesn't work on the example given below:

```
17:47 < wstein-2535> craigcitro -- what happens with this new code when the submodule we're trying to get the
17:47 < wstein-2535> dual of has both * eigenvalues?
17:48 < wstein-2535> I think this new code might just break then.
17:48 -!- roed_ [n=roed`@`c-98-216-48-4.hsd1.ma.comcast.net] has quit []
17:48 < craigcitro> ah, you're saying i want an 'else' clause in the 'star' case.
17:48 < wstein-2535>  At a minimum.
17:49 < wstein-2535> And also you *have* to use star in that case.
17:49 < wstein-2535> Or something.
17:49 < wstein-2535> You've only treated one cases, namely * = constant on subspace.
17:49 < wstein-2535> But this "use the *" trick should work more generaly for any *-equivariant module.
17:49 < craigcitro> oh, you're saying in that case, take the + and - submodules and then just take the sum
17:50 < craigcitro> (i.e. do the same thing i'd do in the case of one eigenvalue with each of them)
17:50 < wstein-2535> sage: M = ModularSymbols(43).cuspidal_submodule()
17:50 < wstein-2535> sage: S = M[0].plus_submodule() + M[1].minus_submodule()
17:50 < wstein-2535> sage: S.dual_free_module()
17:50 < wstein-2535> boom!
17:50 < wstein-2535> Yes, exactly.
```



---

Comment by mabshoff created at 2008-09-20 22:36:45

Reclassify so this ticket is picked up properly by the various reports.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 16:27:36

Could #1127 be related?

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-22 08:33:49

The attached patch addresses William's counterexample, and should be applied after Craig's patch.


---

Attachment

Final version of patch attached, with one or two small improvements over previous.


---

Comment by mabshoff created at 2009-01-24 19:30:38

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 19:30:38

Merged in Sage 3.3.alpha2

Cheers,

Michael
