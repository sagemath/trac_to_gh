# Issue 8667: New version of modular group cohomology spkg

Issue created by migration from https://trac.sagemath.org/ticket/8667

Original creator: SimonKing

Original creation time: 2010-04-10 01:06:30

Assignee: SimonKing

CC:  graham.ellis@nuigalway.ie david.green@uni-jena.de jhpalmieri

Keywords: modular cohomology finite group

There is a major new version 2.0 of the p_group_cohomology spkg. It can be installed by

```
sage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.0.spkg
```

A test suite is run if `SAGE_CHECK=yes`. The results are printed on screen and saved in `install.log`. There is extensive [documentation](http://sage.math.washington.edu/home/SimonKing/Cohomology/).

*__Main New Features__*

The name "p_group_cohomology" used to mean "cohomology of p-groups". Now, it means "mod p cohomology of finite groups", i.e., the package now covers the case of non prime power groups as well. This is implemented in the new module `pGroupCohomology.modular_cohomology`.

With the new package version, we were able to compute the mod-p cohomology rings of many interesting groups and for different primes - see [here http://www.nuigalway.ie/maths/sk/Cohomology/rings/]. Most notably, we can compute the mod-2 cohomology rings of the third Conway group (it is Cohen-Macaulay) and the Higman-Sims group.

*__Minor Improvements__*

 * The documentation is now backed up by references.
 * As a safety feature, data in the Singular interface are reconstructed, should Singular crash. This is particularly important, since the new implementation _heavily_ relies on Singular.
 * More generally, I tried to make all potentially hard computations interruptible without data loss.
 * The install script should be better portable:
   * The test for the presence of the Small Groups library is improved (compare #8523)
   * The environment variables `CC`, `AR`, `MKDIR`, `RM` etc are now used.
 * In previous versions, it sometimes happened that `C-MeatAxe` wrote a multiplication table in the current directory. This is now stopped.

*__Theory__*

Both for prime power and non prime power groups, the basic approach is to approximate the cohomology ring degree by degree. A completeness criterion then asserts that the approximation is complete, so that the computation may terminate. More details and [references](http://sage.math.washington.edu/home/SimonKing/Cohomology/pGroupCohomology.html#references) can be found in the documentation.

__Prime power case__

For prime power groups, the approximation is computed using an initial segment of a minimal free resolution. We use a modification of Dave Benson's completeness criterion. In the new package version, we alternatively use a criterion of Peter Symonds.

The modified Benson criterion uses an existence result for small filter regular parameters over a finite field extension. For Symonds' criterion, the parameters don't need to be filter regular, but one can not use a field extension. For both criteria, small parameter degrees are helpful.

So, two things may happen:

 * General parameters are of smaller degree than filter regular parameters: Advantage for the Symonds criterion.
 * The degrees of filter regular parameters over an extension field are smaller than the degrees of general parameters without field extension: Advantage for the modified Benson criterion.

The program chooses between the two criteria. If _both_ may apply, the Symonds criterion is preferred, since it is easier to use.

__Non prime power case__

The computations rely on the stable element method. Namely, the mod-_p_ cohomology of a finite group _G_ can be computed as a subring of the mod-_p_ cohomology of any subgroup _P_ of _G_ whose index is coprime to _p_. This subring is characterised by so-called stability conditions given by pairs of induced maps.

So, eventually the computations rely on the computation of the cohomology ring of a prime power group. But this can be in several steps. By default, the program starts with the cohomology ring of a Sylow subgroup _S_ and then proceeds to compute the cohomology of `P=Normaliser(G,Centre(S))` as a subring of the cohomology of _S_, and computes the cohomology of _G_ as a subring of the cohomology of _P_.

The reason for choosing an intermediate subgroup between _G_ and _S_ is that the number of stability conditions usually drops drastically, compared with a direct computation with _P=S_.

Now, if the cohomology ring of _P_ is computed, the ring structure of the cohomology of _G_ can be computed in increasing degree, by solving the stability conditions. Eventually, it would be possible to use either Benson's or Symonds' criterion. 

However for non prime power groups, [another criterion](http://arxiv.org/abs/1004.0736) is available that combines the advantages of the other two criteria: It uses an existence proof for (not necessarily filter regular) parameters over a finite extension field, and it relies on the computation of the Poincare series of the ring approximation, which is relatively easy compared with a computation of the filter degree type.

*__Example__*

The example that we present here is part of the doc tests. Its purpose is to illustrate a theoretical improvement that stands behind the implementation. 

We compute the mod 2 cohomology of the symmetric group `S_8`. The reason for using the option `useFactorization=False` is that in this example the random factorization algorithm for multivariate polynomials often (not always) chokes on the paramaters of the ring.

```
sage: from pGroupCohomology import CohomologyRing
sage: G = gap('SymmetricGroup(8)')
sage: H = CohomologyRing(G, prime=2,GroupName='SymmetricGroup(8)',useFactorization=False)
```

The initialisation takes quite long, since behind the scenes other cohomology rings are computed, namely:

```
sage: H.subgroup_cohomology()
H^*(SmallGroup(384,5602); GF(2))
sage: H.sylow_cohomology()
H^*(Syl2(S8); GF(2))
```


We compute the complete ring structure by a single command:

```
sage: H.make()
sage: print H

Cohomology ring of S8 with coefficients in GF(2)

Computation complete
Minimal list of generators:
[b_2_0: 2-Cocycle in H^*(S8; GF(2)),
 c_4_0: 4-Cocycle in H^*(S8; GF(2)),
 b_6_0: 6-Cocycle in H^*(S8; GF(2)),
 b_1_0: 1-Cocycle in H^*(S8; GF(2)),
 b_3_0: 3-Cocycle in H^*(S8; GF(2)),
 b_3_1: 3-Cocycle in H^*(S8; GF(2)),
 b_5_8: 5-Cocycle in H^*(S8; GF(2)),
 b_7_17: 7-Cocycle in H^*(S8; GF(2))]
Minimal list of algebraic relations:
[b_3_0*b_3_1+b_1_0*b_5_8+b_1_0^3*b_3_0+b_2_0*b_1_0*b_3_1+c_4_0*b_1_0^2,
 b_6_0*b_1_0,
 b_1_0*b_7_17,
 b_3_1*b_5_8+b_1_0^2*b_3_0^2+b_1_0^3*b_5_8+b_1_0^5*b_3_0+b_2_0*b_1_0*b_5_8+b_2_0*b_1_0^3*b_3_1+c_4_0*b_1_0*b_3_1+c_4_0*b_1_0*b_3_0+c_4_0*b_1_0^4,
 b_2_0*b_7_17,
 b_6_0*b_3_1,
 b_3_0*b_7_17,
 b_3_1*b_7_17,
 b_5_8^2+b_1_0*b_3_0^3+b_1_0^4*b_3_0^2+b_2_0*b_3_0*b_5_8+b_2_0*b_1_0^2*b_3_0^2+b_2_0^2*b_1_0*b_5_8+b_2_0^2*b_6_0+c_4_0*b_3_0^2+b_2_0*c_4_0*b_1_0*b_3_0+c_4_0^2*b_1_0^2,
 b_5_8*b_7_17]
```


In the rest of this example, we discuss the three completeness criteria. The criteria have in common that one needs to construct parameters. By Benson, using simultaneous lifts of Dickson invariants in the cohomology of maximal elementary abelian subgroups, one obtains filter regular parameters. Here, they live in degrees 8, 12, 14, 15. But it turns out that the last parameter can be replaced by an element in degree 6. Note that replacing the last parameter does not change filter regularity.


```
sage: H.filter_regular_parameters()
['b_3_0*b_5_8+b_1_0^2*b_3_1^2+b_1_0^2*b_3_0^2+b_1_0^3*b_5_8+b_1_0^5*b_3_0+b_1_0^8+b_2_0*b_1_0^3*b_3_1+b_2_0^4+c_4_0*b_1_0*b_3_1+c_4_0*b_1_0*b_3_0+c_4_0*b_1_0^4+c_4_0^2', 'b_3_1^4+b_3_0^4+b_1_0^4*b_3_0*b_5_8+b_1_0^6*b_3_1^2+b_1_0^6*b_3_0^2+b_1_0^7*b_5_8+b_1_0^9*b_3_0+b_6_0*b_3_0^2+b_6_0^2+b_2_0*b_1_0*b_3_0^3+b_2_0*b_1_0^4*b_3_1^2+b_2_0*b_1_0^5*b_5_8+b_2_0*b_1_0^7*b_3_1+b_2_0^2*b_1_0^2*b_3_1^2+b_2_0^2*b_1_0^5*b_3_0+b_2_0^3*b_1_0*b_5_8+b_2_0^3*b_1_0^3*b_3_1+b_2_0^3*b_6_0+b_2_0^4*b_1_0^4+c_4_0*b_3_0*b_5_8+c_4_0*b_1_0^2*b_3_1^2+c_4_0*b_1_0^2*b_3_0^2+c_4_0*b_1_0^3*b_5_8+c_4_0*b_1_0^5*b_3_1+c_4_0*b_1_0^5*b_3_0+c_4_0*b_1_0^8+b_2_0*c_4_0*b_3_0^2+b_2_0*c_4_0*b_1_0^3*b_3_1+b_2_0*c_4_0*b_1_0^3*b_3_0+b_2_0^2*c_4_0*b_1_0*b_3_1+b_2_0^2*c_4_0*b_1_0^4+c_4_0^2*b_1_0*b_3_1+c_4_0^2*b_1_0*b_3_0+c_4_0^2*b_1_0^4+b_2_0*c_4_0^2*b_1_0^2+b_2_0^2*c_4_0^2', 'b_7_17^2+b_3_0^3*b_5_8+b_1_0^2*b_3_1^4+b_1_0^2*b_3_0^4+b_1_0^3*b_3_0^2*b_5_8+b_6_0*b_3_0*b_5_8+b_2_0*b_1_0^3*b_3_1^3+b_2_0*b_1_0^3*b_3_0^3+b_2_0*b_1_0^4*b_3_0*b_5_8+b_2_0*b_1_0^6*b_3_1^2+b_2_0*b_1_0^9*b_3_0+b_2_0*b_6_0*b_3_0^2+b_2_0^2*b_1_0*b_3_0^3+b_2_0^2*b_1_0^4*b_3_1^2+b_2_0^2*b_1_0^4*b_3_0^2+b_2_0^2*b_1_0^7*b_3_1+b_2_0^3*b_3_0*b_5_8+b_2_0^3*b_1_0^2*b_3_0^2+b_2_0^3*b_1_0^3*b_5_8+b_2_0^4*b_1_0*b_5_8+b_2_0^4*b_6_0+c_4_0*b_1_0*b_3_1^3+c_4_0*b_1_0^4*b_3_1^2+c_4_0*b_1_0^4*b_3_0^2+c_4_0*b_1_0^7*b_3_0+b_2_0*c_4_0*b_1_0^2*b_3_1^2+b_2_0*c_4_0*b_1_0^2*b_3_0^2+b_2_0*c_4_0*b_1_0^3*b_5_8+b_2_0*c_4_0*b_1_0^5*b_3_1+b_2_0*c_4_0*b_1_0^5*b_3_0+b_2_0*c_4_0*b_1_0^8+b_2_0^2*c_4_0*b_3_0^2+b_2_0^2*c_4_0*b_1_0*b_5_8+b_2_0^2*c_4_0*b_1_0^3*b_3_1+b_2_0^2*c_4_0*b_6_0+b_2_0^3*c_4_0*b_1_0*b_3_0+c_4_0^2*b_3_1^2+c_4_0^2*b_1_0^6+b_2_0*c_4_0^2*b_1_0*b_3_1+b_2_0*c_4_0^2*b_1_0^4+c_4_0^3*b_1_0^2', 'b_1_0^6+b_6_0']
sage: H.is_filter_regular(_,[8,12,14,6])
True
sage: H.filter_degree_type()
[-1, -2, -3, -4, -4]
```


Benson's test would yield the degree bound `(8+12+14+6)-dimension = 36`. It turns out that our existence proof for filter regular parameters over a finite extension field does not yield an improvement:


```
sage: H.potential_degree_bound(H.filter_regular_parameters(),[8,12,14,6])
36
```


The Symonds test relies on parameters that are not necessarily filter regular. The program finds some, in degrees 4,12,14,6. Actually it is guaranteed that none of these parameters can be replaced by an element of smaller degree.

```
sage: H.parameters()
['b_2_0^2+c_4_0', 'b_3_1^4+b_3_0^4+b_1_0^4*b_3_0*b_5_8+b_1_0^6*b_3_1^2+b_1_0^6*b_3_0^2+b_1_0^7*b_5_8+b_1_0^9*b_3_0+b_6_0*b_3_0^2+b_6_0^2+b_2_0*b_1_0*b_3_0^3+b_2_0*b_1_0^4*b_3_1^2+b_2_0*b_1_0^5*b_5_8+b_2_0*b_1_0^7*b_3_1+b_2_0^2*b_1_0^2*b_3_1^2+b_2_0^2*b_1_0^5*b_3_0+b_2_0^3*b_1_0*b_5_8+b_2_0^3*b_1_0^3*b_3_1+b_2_0^3*b_6_0+b_2_0^4*b_1_0^4+c_4_0*b_3_0*b_5_8+c_4_0*b_1_0^2*b_3_1^2+c_4_0*b_1_0^2*b_3_0^2+c_4_0*b_1_0^3*b_5_8+c_4_0*b_1_0^5*b_3_1+c_4_0*b_1_0^5*b_3_0+c_4_0*b_1_0^8+b_2_0*c_4_0*b_3_0^2+b_2_0*c_4_0*b_1_0^3*b_3_1+b_2_0*c_4_0*b_1_0^3*b_3_0+b_2_0^2*c_4_0*b_1_0*b_3_1+b_2_0^2*c_4_0*b_1_0^4+c_4_0^2*b_1_0*b_3_1+c_4_0^2*b_1_0*b_3_0+c_4_0^2*b_1_0^4+b_2_0*c_4_0^2*b_1_0^2+b_2_0^2*c_4_0^2', 'b_7_17^2+b_3_0^3*b_5_8+b_1_0^2*b_3_1^4+b_1_0^2*b_3_0^4+b_1_0^3*b_3_0^2*b_5_8+b_6_0*b_3_0*b_5_8+b_2_0*b_1_0^3*b_3_1^3+b_2_0*b_1_0^3*b_3_0^3+b_2_0*b_1_0^4*b_3_0*b_5_8+b_2_0*b_1_0^6*b_3_1^2+b_2_0*b_1_0^9*b_3_0+b_2_0*b_6_0*b_3_0^2+b_2_0^2*b_1_0*b_3_0^3+b_2_0^2*b_1_0^4*b_3_1^2+b_2_0^2*b_1_0^4*b_3_0^2+b_2_0^2*b_1_0^7*b_3_1+b_2_0^3*b_3_0*b_5_8+b_2_0^3*b_1_0^2*b_3_0^2+b_2_0^3*b_1_0^3*b_5_8+b_2_0^4*b_1_0*b_5_8+b_2_0^4*b_6_0+c_4_0*b_1_0*b_3_1^3+c_4_0*b_1_0^4*b_3_1^2+c_4_0*b_1_0^4*b_3_0^2+c_4_0*b_1_0^7*b_3_0+b_2_0*c_4_0*b_1_0^2*b_3_1^2+b_2_0*c_4_0*b_1_0^2*b_3_0^2+b_2_0*c_4_0*b_1_0^3*b_5_8+b_2_0*c_4_0*b_1_0^5*b_3_1+b_2_0*c_4_0*b_1_0^5*b_3_0+b_2_0*c_4_0*b_1_0^8+b_2_0^2*c_4_0*b_3_0^2+b_2_0^2*c_4_0*b_1_0*b_5_8+b_2_0^2*c_4_0*b_1_0^3*b_3_1+b_2_0^2*c_4_0*b_6_0+b_2_0^3*c_4_0*b_1_0*b_3_0+c_4_0^2*b_3_1^2+c_4_0^2*b_1_0^6+b_2_0*c_4_0^2*b_1_0*b_3_1+b_2_0*c_4_0^2*b_1_0^4+c_4_0^3*b_1_0^2', 'b_1_0^6+b_6_0']
```


It turns out that the ring approximation is generated in degree at most 32, as a module over these paramters:

```
sage: max([int(singular.eval('deg(%s)'%t)) for t in H.relation_ideal().std(singular.ideal(H.parameters())).kbase()])
32
```

The Symonds criterion thus yields the bound `(4+12+14+6)-dimension+1=33`.

However, it turns out that _over some finite extension field_, the degree 14 parameter can be replaced by an element in degree 7. Note that this is impossible without a field extension, because otherwise the exhaustive search in `H.parameters()` would have detected it. The existence of the parameter can be shown like this:

```
sage: P = H.parameters()
sage: P.pop(2)
'b_7_17^2+b_3_0^3*b_5_8+b_1_0^2*b_3_1^4+b_1_0^2*b_3_0^4+b_1_0^3*b_3_0^2*b_5_8+b_6_0*b_3_0*b_5_8+b_2_0*b_1_0^3*b_3_1^3+b_2_0*b_1_0^3*b_3_0^3+b_2_0*b_1_0^4*b_3_0*b_5_8+b_2_0*b_1_0^6*b_3_1^2+b_2_0*b_1_0^9*b_3_0+b_2_0*b_6_0*b_3_0^2+b_2_0^2*b_1_0*b_3_0^3+b_2_0^2*b_1_0^4*b_3_1^2+b_2_0^2*b_1_0^4*b_3_0^2+b_2_0^2*b_1_0^7*b_3_1+b_2_0^3*b_3_0*b_5_8+b_2_0^3*b_1_0^2*b_3_0^2+b_2_0^3*b_1_0^3*b_5_8+b_2_0^4*b_1_0*b_5_8+b_2_0^4*b_6_0+c_4_0*b_1_0*b_3_1^3+c_4_0*b_1_0^4*b_3_1^2+c_4_0*b_1_0^4*b_3_0^2+c_4_0*b_1_0^7*b_3_0+b_2_0*c_4_0*b_1_0^2*b_3_1^2+b_2_0*c_4_0*b_1_0^2*b_3_0^2+b_2_0*c_4_0*b_1_0^3*b_5_8+b_2_0*c_4_0*b_1_0^5*b_3_1+b_2_0*c_4_0*b_1_0^5*b_3_0+b_2_0*c_4_0*b_1_0^8+b_2_0^2*c_4_0*b_3_0^2+b_2_0^2*c_4_0*b_1_0*b_5_8+b_2_0^2*c_4_0*b_1_0^3*b_3_1+b_2_0^2*c_4_0*b_6_0+b_2_0^3*c_4_0*b_1_0*b_3_0+c_4_0^2*b_3_1^2+c_4_0^2*b_1_0^6+b_2_0*c_4_0^2*b_1_0*b_3_1+b_2_0*c_4_0^2*b_1_0^4+c_4_0^3*b_1_0^2'
sage: H.relation_ideal().std(singular.ideal(P+H.standard_monomials(7))).dim()==0
True
```


What can we do with this existence proof? We know that the Poincare series does not change by extending the field, and we know that we can choose its denominator as given by the degree of the parameters. Moreover, it is known that the Poincare series, as a rational function, has degree at most minus the depth of the cohomology ring. The following lines imply that the computation is complete (here is the [http://arxiv.org/abs/1004.0736 theoretical background), provided that one also shows that there are no generators in higher degree:

```
sage: H.subgroup_cohomology().depth()
3
sage: 4+12+7+6-3
26
sage: H.knownDeg>=26
True
sage: p = H.poincare_series()
sage: t = p.parent().gen()
sage: q = p*(1-t^4)*(1-t^12)*(1-t^7)*(1-t^6)
sage: q.denominator()==1
True
sage: q.numerator().degree()<=26
True
```


There remains to show that there are no generators in higher degree, and this is where we use that the group is not of prime power order. It can be shown that the cohomology ring of _P_ is a finitely generated module over the restriction of the cohomology of _G_. Moreover, if it is finitely generated as a module over the restriction of the ring approximation, generated in degree at most _n_, then the cohomology ring of _G_ can be generated in degree at most _n_. Here, we find:

```
sage: Rest=[t.as_cocycle_in_subgroup().as_polynomial() for t in H.gens()[1:]]
sage: HP = H.subgroup_cohomology()
sage: HP.set_ring()
sage: max([int(singular.eval('deg(%s)'%t)) for t in HP.relation_ideal().std(singular.ideal(Rest)).kbase()])
8
```


Hence, there are no generators above degree 8. Therefore, the computation can indeed be terminated in degree 26. I call this the _Hilbert-Poincare criterion_, and it seems to be the best method available.

*__Tests__*

I did successfully build and test on my machine (`x86_64 GNU/Linux`, Intel Core Duo), on bsd.math (both 32 and 64 bit) and on boxen.math. Any Python or Cython function is documented and has a test.



---

Comment by SimonKing created at 2010-04-10 01:08:08

Is "group theory" or "optional packages" the right component?


---

Comment by SimonKing created at 2010-04-10 01:08:08

Changing component from group_theory to optional packages.


---

Comment by SimonKing created at 2010-04-13 15:31:52

I just did a small update of the package (a small aesthetic change in the method "htmlpage"). I'm running the doc tests now and will report back if it does _not_ work.


---

Comment by SimonKing created at 2010-04-15 08:54:44

I posted another update of the package.

I tried to make the package robust enough so that after interruption of Singular all relevant data are reconstructed, so that the computation can be resumed. The update concerns a case where this failed. Here is the relevant example (which forms a new doc test), that (in the originally posted package) used to result in an error:

```
            sage: from pGroupCohomology import CohomologyRing
            sage: tmp = tmp_filename()
            sage: CohomologyRing.set_user_db(tmp)
            sage: H = CohomologyRing(48,50, prime=2)
            sage: H.make()
            sage: c = H.subgroup_cohomology()('c_1_1*c_1_2^2*c_1_3^3+c_1_1*c_1_2^4*c_1_3+c_1_1*c_1_2^5+c_1_1^2*c_1_3^4+c_1_1^2*c_1_2*c_1_3^3+c_1_1^2*c_1_2^3*c_1_3+c_1_1^3*c_1_2^2*c_1_3+c_1_1^3*c_1_2^3+c_1_1^4*c_1_3^2+c_1_1^4*c_1_2*c_1_3+c_1_1^4*c_1_2^2+c_1_1^5*c_1_2+c_1_0*c_1_3^5+c_1_0*c_1_2^2*c_1_3^3+c_1_0*c_1_2^3*c_1_3^2+c_1_0*c_1_1^2*c_1_2*c_1_3^2+c_1_0*c_1_1^2*c_1_2^2*c_1_3+c_1_0*c_1_1^2*c_1_2^3+c_1_0*c_1_1^3*c_1_3^2+c_1_0*c_1_1^3*c_1_2^2+c_1_0*c_1_1^4*c_1_3+c_1_0*c_1_1^5+c_1_0^2*c_1_3^4+c_1_0^2*c_1_2^2*c_1_3^2+c_1_0^2*c_1_2^3*c_1_3+c_1_0^2*c_1_2^4+c_1_0^2*c_1_1*c_1_3^3+c_1_0^2*c_1_1*c_1_2^2*c_1_3+c_1_0^2*c_1_1^2*c_1_2*c_1_3+c_1_0^2*c_1_1^2*c_1_2^2+c_1_0^2*c_1_1^3*c_1_2+c_1_0^3*c_1_2*c_1_3^2+c_1_0^3*c_1_1*c_1_2^2+c_1_0^3*c_1_1^2*c_1_3+c_1_0^3*c_1_1^3+c_1_0^4*c_1_3^2+c_1_0^4*c_1_2*c_1_3+c_1_0^4*c_1_2^2+c_1_0^4*c_1_1*c_1_2+c_1_0^4*c_1_1^2+c_1_0^5*c_1_3+c_1_0^5*c_1_1')
            sage: d = H.stable_to_polynomial(c); d
            c_3_6^2+c_3_2*c_3_7+c_3_2*c_3_6+c_3_0*c_3_7+c_3_0*c_3_6+c_3_0*c_3_5+c_3_0*c_3_4+c_3_0*c_3_3+c_2_3^3+c_2_2*c_2_3^2+c_2_1^2*c_2_3+c_2_1^3+c_2_0*c_2_3^2+c_2_0*c_2_1*c_2_2+c_2_0*c_2_1^2+c_2_0^2*c_2_3: 6-Cocycle in H^*(SmallGroup(48,50); GF(2))
            sage: singular.quit()
            sage: d == H.stable_to_polynomial(c)
            True
```


Explanation: In the last line (i.e., after quitting Singular), the data of `c`, the data of `d` and the underlying data used in `stable_to_polynomial` are automatically reconstructed, so that the computation can be repeated, yielding the same result.


---

Comment by SimonKing created at 2010-04-15 14:00:14

I just realised that I forgot to label this ticket as "needs review". Sorry!


---

Comment by SimonKing created at 2010-04-15 14:00:14

Changing status from new to needs_review.


---

Comment by SimonKing created at 2010-04-26 13:06:14

There have been some changes in the underlying modules concerning finite fields in sage-4.4. By consequence, some import statements broke.

This is fixed by importing ``from sage.all`` whenever possible. I just posted the updated spkg.


---

Comment by was created at 2010-07-22 09:11:30

(1) Add an .hgignore file to the hg repo:


```
$  hg status 
? src/bin/checksum
? src/bin/chop
? src/bin/chop.o
...
```


(2) In spkg-install, change

```
# building parallely is bad. Therefore, although it is probably bad style:
MAKE=make; export MAKE;
```

to 

```
unset MAKE
```


The doctest coverage is excellent:

```
wstein@sage:~/build/referee/sage-4.5/spkg/build/p_group_cohomology-2.0/src/pGroupCohomology$ sage -coverage .
__init__.py: 100% (6 of 6)
barcode.py: 100% (15 of 15)
cochain.pyx: 95% (108 of 113)
cohomology.pyx: 100% (92 of 92)
dickson.pyx: 100% (4 of 4)
modular_cohomology.pyx: 100% (30 of 30)
mtx.pyx: 100% (40 of 40)
resolution.pyx: 95% (59 of 62)

Overall weighted coverage score:  97.6%
Total number of functions:  362
We need    5 more function to get to 99% coverage.
```



This package is amazing!  It's also an amazing example of how to make an optional Sage package that involves lots of serious Cython code, but isn't part of the Sage library. 

And, all tests pass (on sage.math). 

So, positive review.  However, fix (1),(2) above at some point (this is a minor nitpick).


---

Comment by was created at 2010-07-22 09:11:30

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-07-22 09:14:45

MErged into optional package repo.


---

Comment by was created at 2010-07-22 09:14:45

Resolution: fixed


---

Comment by was created at 2010-07-22 09:27:24

WARNING: In the newest version of sage there is a "Tab detection" feature in doctesting, which makes SPKG_CHECK fail:

```

pGroupCohomology.cohomology.COHO.bar_code resulted in
sage -t -optional -long "RecDoctest.py"
**********************************************************************
Error: TAB character found.

         [9.4 s]

----------------------------------------------------------------------
The following tests failed:


        sage -t -optional -long "RecDoctest.py"
Total time for all tests: 9.4 seconds  

-------------------------------------------------------------
pGroupCohomology.mtx.MTX.lead resulted in
sage -t -optional -long "RecDoctest.py"
**********************************************************************
Error: TAB character found.

         [2.5 s]
```



---

Comment by SimonKing created at 2010-07-26 22:46:53

Replying to [comment:8 was]:
> MErged into optional package repo.

Dear William,

I tried `install_package('p_group_cohomology')` but it still tries to install 1.2, not 2.0. 

Replying to [comment:7 was]:
> (1) Add an .hgignore file to the hg repo:
> 
> {{{
> $  hg status 
> ? src/bin/checksum
> ? src/bin/chop
> ? src/bin/chop.o
> ...
> }}}

The spkg at http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.0.spkg _does_ have .hgignore, and `hg status` reports nothing. But wait: Did you perhaps install the package manually? Because, src/bin/ is an empty directory, and the files checksum, chop etc are created during build.

> The doctest coverage is excellent:
> ...
> Overall weighted coverage score:  97.6%

OUTCH! I thought this was 100%, and actually my spkg-check was supposed to complain if there was any untested method. I'll fix this in version 2.1, which should be out soon (although it is only a minor upgrade).

I posted an updated package at http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.0.spkg

It has "unset MAKE" in the spkg-install, adds one doctest, and removes the tab keys.

Cheers,
Simon


---

Comment by jhpalmieri created at 2010-07-26 23:19:22

> I tried install_package('p_group_cohomology') but it still tries to install 1.2, not 2.0.

I think that Sage first looks in SAGE_ROOT/spkg/optional/ for the spkg file, and if it finds it, it installs that one.  Maybe you have an old copy of the spkg there?


---

Comment by SimonKing created at 2010-07-27 00:04:02

Replying to [comment:11 jhpalmieri]:
> I think that Sage first looks in SAGE_ROOT/spkg/optional/ for the spkg file, and if it finds it, it installs that one.  Maybe you have an old copy of the spkg there?

No, it was a freshly built Sage, and I just tested again: Even when I removed SAGE_ROOT/spkg/optional/p_group*, still `install_package('p_group_cohomology')` lead to the old version.

Indeed, `./sage -optional` yields p_group_cohomology-1.2.p0

Cheers,
Simon


---

Comment by jhpalmieri created at 2010-07-27 00:30:11

Maybe your mirror hasn't been updated?  I see both versions when I do `sage -optional`.


---

Comment by SimonKing created at 2010-07-27 07:21:02

Replying to [comment:13 jhpalmieri]:
> Maybe your mirror hasn't been updated?  I see both versions when I do `sage -optional`.

I am referring here to sage.math.

If I do `sage -optional` with the system wide Sage, I get

```
SimonKing@sage:~$ sage -optional
Using SAGE Server http://www.sagemath.org//packages
http://www.sagemath.org//packages/optional/list --> /usr/local/sage/tmp/list
[Errno 13] Permission denied: '/usr/local/sage/tmp/list'



********************************************************************************



Error contacting http://www.sagemath.org//packages/optional/list. Try using an alternative server.
For example, from the bash prompt try typing

   export SAGE_SERVER=http://sage.scipy.org/sage/

then try again.
```


If I do it with a Sage that I built myself on sage.math:/scratch/sking/, I indeed see version 2.0 installed and 1.2 not installed. But when one does 

```
sage: install_package('package_name')
```

then v1.2 gets installed, with not taking into account v2.0.

I think `install_package('package_name')` should always try to install the latest available version of `package_name`. Instead, it installs the latest _uninstalled_ version, even though a more recent version is already installed.

So, I think there is a bug in `install_package`.


---

Comment by schilly created at 2010-07-29 09:02:59

FYI, I've just updated two osx binaries and I've seen that this spkg was not properly mirrored out to the mirrors. install_package is just fine, the problem was on the server.
