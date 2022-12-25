# Issue 8667: New version of modular group cohomology spkg

archive/issues_008667.json:
```json
{
    "body": "Assignee: @simon-king-jena\n\nCC:  graham.ellis@nuigalway.ie david.green@uni-jena.de @jhpalmieri\n\nKeywords: modular cohomology finite group\n\nThere is a major new version 2.0 of the p_group_cohomology spkg. It can be installed by\n\n```\nsage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.0.spkg\n```\n\nA test suite is run if `SAGE_CHECK=yes`. The results are printed on screen and saved in `install.log`. There is extensive [documentation](http://sage.math.washington.edu/home/SimonKing/Cohomology/).\n\n**__Main New Features__**\n\nThe name \"p_group_cohomology\" used to mean \"cohomology of p-groups\". Now, it means \"mod p cohomology of finite groups\", i.e., the package now covers the case of non prime power groups as well. This is implemented in the new module `pGroupCohomology.modular_cohomology`.\n\nWith the new package version, we were able to compute the mod-p cohomology rings of many interesting groups and for different primes - see [here http://www.nuigalway.ie/maths/sk/Cohomology/rings/]. Most notably, we can compute the mod-2 cohomology rings of the third Conway group (it is Cohen-Macaulay) and the Higman-Sims group.\n\n**__Minor Improvements__**\n\n* The documentation is now backed up by references.\n* As a safety feature, data in the Singular interface are reconstructed, should Singular crash. This is particularly important, since the new implementation *heavily* relies on Singular.\n* More generally, I tried to make all potentially hard computations interruptible without data loss.\n* The install script should be better portable:\n  * The test for the presence of the Small Groups library is improved (compare #8523)\n  * The environment variables `CC`, `AR`, `MKDIR`, `RM` etc are now used.\n* In previous versions, it sometimes happened that `C-MeatAxe` wrote a multiplication table in the current directory. This is now stopped.\n\n**__Theory__**\n\nBoth for prime power and non prime power groups, the basic approach is to approximate the cohomology ring degree by degree. A completeness criterion then asserts that the approximation is complete, so that the computation may terminate. More details and [references](http://sage.math.washington.edu/home/SimonKing/Cohomology/pGroupCohomology.html#references) can be found in the documentation.\n\n__Prime power case__\n\nFor prime power groups, the approximation is computed using an initial segment of a minimal free resolution. We use a modification of Dave Benson's completeness criterion. In the new package version, we alternatively use a criterion of Peter Symonds.\n\nThe modified Benson criterion uses an existence result for small filter regular parameters over a finite field extension. For Symonds' criterion, the parameters don't need to be filter regular, but one can not use a field extension. For both criteria, small parameter degrees are helpful.\n\nSo, two things may happen:\n\n* General parameters are of smaller degree than filter regular parameters: Advantage for the Symonds criterion.\n* The degrees of filter regular parameters over an extension field are smaller than the degrees of general parameters without field extension: Advantage for the modified Benson criterion.\n\nThe program chooses between the two criteria. If *both* may apply, the Symonds criterion is preferred, since it is easier to use.\n\n__Non prime power case__\n\nThe computations rely on the stable element method. Namely, the mod-*p* cohomology of a finite group *G* can be computed as a subring of the mod-*p* cohomology of any subgroup *P* of *G* whose index is coprime to *p*. This subring is characterised by so-called stability conditions given by pairs of induced maps.\n\nSo, eventually the computations rely on the computation of the cohomology ring of a prime power group. But this can be in several steps. By default, the program starts with the cohomology ring of a Sylow subgroup *S* and then proceeds to compute the cohomology of `P=Normaliser(G,Centre(S))` as a subring of the cohomology of *S*, and computes the cohomology of *G* as a subring of the cohomology of *P*.\n\nThe reason for choosing an intermediate subgroup between *G* and *S* is that the number of stability conditions usually drops drastically, compared with a direct computation with *P=S*.\n\nNow, if the cohomology ring of *P* is computed, the ring structure of the cohomology of *G* can be computed in increasing degree, by solving the stability conditions. Eventually, it would be possible to use either Benson's or Symonds' criterion. \n\nHowever for non prime power groups, [another criterion](http://arxiv.org/abs/1004.0736) is available that combines the advantages of the other two criteria: It uses an existence proof for (not necessarily filter regular) parameters over a finite extension field, and it relies on the computation of the Poincare series of the ring approximation, which is relatively easy compared with a computation of the filter degree type.\n\n**__Example__**\n\nThe example that we present here is part of the doc tests. Its purpose is to illustrate a theoretical improvement that stands behind the implementation. \n\nWe compute the mod 2 cohomology of the symmetric group `S_8`. The reason for using the option `useFactorization=False` is that in this example the random factorization algorithm for multivariate polynomials often (not always) chokes on the paramaters of the ring.\n\n```\nsage: from pGroupCohomology import CohomologyRing\nsage: G = gap('SymmetricGroup(8)')\nsage: H = CohomologyRing(G, prime=2,GroupName='SymmetricGroup(8)',useFactorization=False)\n```\n\nThe initialisation takes quite long, since behind the scenes other cohomology rings are computed, namely:\n\n```\nsage: H.subgroup_cohomology()\nH^*(SmallGroup(384,5602); GF(2))\nsage: H.sylow_cohomology()\nH^*(Syl2(S8); GF(2))\n```\n\n\nWe compute the complete ring structure by a single command:\n\n```\nsage: H.make()\nsage: print H\n\nCohomology ring of S8 with coefficients in GF(2)\n\nComputation complete\nMinimal list of generators:\n[b_2_0: 2-Cocycle in H^*(S8; GF(2)),\n c_4_0: 4-Cocycle in H^*(S8; GF(2)),\n b_6_0: 6-Cocycle in H^*(S8; GF(2)),\n b_1_0: 1-Cocycle in H^*(S8; GF(2)),\n b_3_0: 3-Cocycle in H^*(S8; GF(2)),\n b_3_1: 3-Cocycle in H^*(S8; GF(2)),\n b_5_8: 5-Cocycle in H^*(S8; GF(2)),\n b_7_17: 7-Cocycle in H^*(S8; GF(2))]\nMinimal list of algebraic relations:\n[b_3_0*b_3_1+b_1_0*b_5_8+b_1_0^3*b_3_0+b_2_0*b_1_0*b_3_1+c_4_0*b_1_0^2,\n b_6_0*b_1_0,\n b_1_0*b_7_17,\n b_3_1*b_5_8+b_1_0^2*b_3_0^2+b_1_0^3*b_5_8+b_1_0^5*b_3_0+b_2_0*b_1_0*b_5_8+b_2_0*b_1_0^3*b_3_1+c_4_0*b_1_0*b_3_1+c_4_0*b_1_0*b_3_0+c_4_0*b_1_0^4,\n b_2_0*b_7_17,\n b_6_0*b_3_1,\n b_3_0*b_7_17,\n b_3_1*b_7_17,\n b_5_8^2+b_1_0*b_3_0^3+b_1_0^4*b_3_0^2+b_2_0*b_3_0*b_5_8+b_2_0*b_1_0^2*b_3_0^2+b_2_0^2*b_1_0*b_5_8+b_2_0^2*b_6_0+c_4_0*b_3_0^2+b_2_0*c_4_0*b_1_0*b_3_0+c_4_0^2*b_1_0^2,\n b_5_8*b_7_17]\n```\n\n\nIn the rest of this example, we discuss the three completeness criteria. The criteria have in common that one needs to construct parameters. By Benson, using simultaneous lifts of Dickson invariants in the cohomology of maximal elementary abelian subgroups, one obtains filter regular parameters. Here, they live in degrees 8, 12, 14, 15. But it turns out that the last parameter can be replaced by an element in degree 6. Note that replacing the last parameter does not change filter regularity.\n\n\n```\nsage: H.filter_regular_parameters()\n['b_3_0*b_5_8+b_1_0^2*b_3_1^2+b_1_0^2*b_3_0^2+b_1_0^3*b_5_8+b_1_0^5*b_3_0+b_1_0^8+b_2_0*b_1_0^3*b_3_1+b_2_0^4+c_4_0*b_1_0*b_3_1+c_4_0*b_1_0*b_3_0+c_4_0*b_1_0^4+c_4_0^2', 'b_3_1^4+b_3_0^4+b_1_0^4*b_3_0*b_5_8+b_1_0^6*b_3_1^2+b_1_0^6*b_3_0^2+b_1_0^7*b_5_8+b_1_0^9*b_3_0+b_6_0*b_3_0^2+b_6_0^2+b_2_0*b_1_0*b_3_0^3+b_2_0*b_1_0^4*b_3_1^2+b_2_0*b_1_0^5*b_5_8+b_2_0*b_1_0^7*b_3_1+b_2_0^2*b_1_0^2*b_3_1^2+b_2_0^2*b_1_0^5*b_3_0+b_2_0^3*b_1_0*b_5_8+b_2_0^3*b_1_0^3*b_3_1+b_2_0^3*b_6_0+b_2_0^4*b_1_0^4+c_4_0*b_3_0*b_5_8+c_4_0*b_1_0^2*b_3_1^2+c_4_0*b_1_0^2*b_3_0^2+c_4_0*b_1_0^3*b_5_8+c_4_0*b_1_0^5*b_3_1+c_4_0*b_1_0^5*b_3_0+c_4_0*b_1_0^8+b_2_0*c_4_0*b_3_0^2+b_2_0*c_4_0*b_1_0^3*b_3_1+b_2_0*c_4_0*b_1_0^3*b_3_0+b_2_0^2*c_4_0*b_1_0*b_3_1+b_2_0^2*c_4_0*b_1_0^4+c_4_0^2*b_1_0*b_3_1+c_4_0^2*b_1_0*b_3_0+c_4_0^2*b_1_0^4+b_2_0*c_4_0^2*b_1_0^2+b_2_0^2*c_4_0^2', 'b_7_17^2+b_3_0^3*b_5_8+b_1_0^2*b_3_1^4+b_1_0^2*b_3_0^4+b_1_0^3*b_3_0^2*b_5_8+b_6_0*b_3_0*b_5_8+b_2_0*b_1_0^3*b_3_1^3+b_2_0*b_1_0^3*b_3_0^3+b_2_0*b_1_0^4*b_3_0*b_5_8+b_2_0*b_1_0^6*b_3_1^2+b_2_0*b_1_0^9*b_3_0+b_2_0*b_6_0*b_3_0^2+b_2_0^2*b_1_0*b_3_0^3+b_2_0^2*b_1_0^4*b_3_1^2+b_2_0^2*b_1_0^4*b_3_0^2+b_2_0^2*b_1_0^7*b_3_1+b_2_0^3*b_3_0*b_5_8+b_2_0^3*b_1_0^2*b_3_0^2+b_2_0^3*b_1_0^3*b_5_8+b_2_0^4*b_1_0*b_5_8+b_2_0^4*b_6_0+c_4_0*b_1_0*b_3_1^3+c_4_0*b_1_0^4*b_3_1^2+c_4_0*b_1_0^4*b_3_0^2+c_4_0*b_1_0^7*b_3_0+b_2_0*c_4_0*b_1_0^2*b_3_1^2+b_2_0*c_4_0*b_1_0^2*b_3_0^2+b_2_0*c_4_0*b_1_0^3*b_5_8+b_2_0*c_4_0*b_1_0^5*b_3_1+b_2_0*c_4_0*b_1_0^5*b_3_0+b_2_0*c_4_0*b_1_0^8+b_2_0^2*c_4_0*b_3_0^2+b_2_0^2*c_4_0*b_1_0*b_5_8+b_2_0^2*c_4_0*b_1_0^3*b_3_1+b_2_0^2*c_4_0*b_6_0+b_2_0^3*c_4_0*b_1_0*b_3_0+c_4_0^2*b_3_1^2+c_4_0^2*b_1_0^6+b_2_0*c_4_0^2*b_1_0*b_3_1+b_2_0*c_4_0^2*b_1_0^4+c_4_0^3*b_1_0^2', 'b_1_0^6+b_6_0']\nsage: H.is_filter_regular(_,[8,12,14,6])\nTrue\nsage: H.filter_degree_type()\n[-1, -2, -3, -4, -4]\n```\n\n\nBenson's test would yield the degree bound `(8+12+14+6)-dimension = 36`. It turns out that our existence proof for filter regular parameters over a finite extension field does not yield an improvement:\n\n\n```\nsage: H.potential_degree_bound(H.filter_regular_parameters(),[8,12,14,6])\n36\n```\n\n\nThe Symonds test relies on parameters that are not necessarily filter regular. The program finds some, in degrees 4,12,14,6. Actually it is guaranteed that none of these parameters can be replaced by an element of smaller degree.\n\n```\nsage: H.parameters()\n['b_2_0^2+c_4_0', 'b_3_1^4+b_3_0^4+b_1_0^4*b_3_0*b_5_8+b_1_0^6*b_3_1^2+b_1_0^6*b_3_0^2+b_1_0^7*b_5_8+b_1_0^9*b_3_0+b_6_0*b_3_0^2+b_6_0^2+b_2_0*b_1_0*b_3_0^3+b_2_0*b_1_0^4*b_3_1^2+b_2_0*b_1_0^5*b_5_8+b_2_0*b_1_0^7*b_3_1+b_2_0^2*b_1_0^2*b_3_1^2+b_2_0^2*b_1_0^5*b_3_0+b_2_0^3*b_1_0*b_5_8+b_2_0^3*b_1_0^3*b_3_1+b_2_0^3*b_6_0+b_2_0^4*b_1_0^4+c_4_0*b_3_0*b_5_8+c_4_0*b_1_0^2*b_3_1^2+c_4_0*b_1_0^2*b_3_0^2+c_4_0*b_1_0^3*b_5_8+c_4_0*b_1_0^5*b_3_1+c_4_0*b_1_0^5*b_3_0+c_4_0*b_1_0^8+b_2_0*c_4_0*b_3_0^2+b_2_0*c_4_0*b_1_0^3*b_3_1+b_2_0*c_4_0*b_1_0^3*b_3_0+b_2_0^2*c_4_0*b_1_0*b_3_1+b_2_0^2*c_4_0*b_1_0^4+c_4_0^2*b_1_0*b_3_1+c_4_0^2*b_1_0*b_3_0+c_4_0^2*b_1_0^4+b_2_0*c_4_0^2*b_1_0^2+b_2_0^2*c_4_0^2', 'b_7_17^2+b_3_0^3*b_5_8+b_1_0^2*b_3_1^4+b_1_0^2*b_3_0^4+b_1_0^3*b_3_0^2*b_5_8+b_6_0*b_3_0*b_5_8+b_2_0*b_1_0^3*b_3_1^3+b_2_0*b_1_0^3*b_3_0^3+b_2_0*b_1_0^4*b_3_0*b_5_8+b_2_0*b_1_0^6*b_3_1^2+b_2_0*b_1_0^9*b_3_0+b_2_0*b_6_0*b_3_0^2+b_2_0^2*b_1_0*b_3_0^3+b_2_0^2*b_1_0^4*b_3_1^2+b_2_0^2*b_1_0^4*b_3_0^2+b_2_0^2*b_1_0^7*b_3_1+b_2_0^3*b_3_0*b_5_8+b_2_0^3*b_1_0^2*b_3_0^2+b_2_0^3*b_1_0^3*b_5_8+b_2_0^4*b_1_0*b_5_8+b_2_0^4*b_6_0+c_4_0*b_1_0*b_3_1^3+c_4_0*b_1_0^4*b_3_1^2+c_4_0*b_1_0^4*b_3_0^2+c_4_0*b_1_0^7*b_3_0+b_2_0*c_4_0*b_1_0^2*b_3_1^2+b_2_0*c_4_0*b_1_0^2*b_3_0^2+b_2_0*c_4_0*b_1_0^3*b_5_8+b_2_0*c_4_0*b_1_0^5*b_3_1+b_2_0*c_4_0*b_1_0^5*b_3_0+b_2_0*c_4_0*b_1_0^8+b_2_0^2*c_4_0*b_3_0^2+b_2_0^2*c_4_0*b_1_0*b_5_8+b_2_0^2*c_4_0*b_1_0^3*b_3_1+b_2_0^2*c_4_0*b_6_0+b_2_0^3*c_4_0*b_1_0*b_3_0+c_4_0^2*b_3_1^2+c_4_0^2*b_1_0^6+b_2_0*c_4_0^2*b_1_0*b_3_1+b_2_0*c_4_0^2*b_1_0^4+c_4_0^3*b_1_0^2', 'b_1_0^6+b_6_0']\n```\n\n\nIt turns out that the ring approximation is generated in degree at most 32, as a module over these paramters:\n\n```\nsage: max([int(singular.eval('deg(%s)'%t)) for t in H.relation_ideal().std(singular.ideal(H.parameters())).kbase()])\n32\n```\n\nThe Symonds criterion thus yields the bound `(4+12+14+6)-dimension+1=33`.\n\nHowever, it turns out that *over some finite extension field*, the degree 14 parameter can be replaced by an element in degree 7. Note that this is impossible without a field extension, because otherwise the exhaustive search in `H.parameters()` would have detected it. The existence of the parameter can be shown like this:\n\n```\nsage: P = H.parameters()\nsage: P.pop(2)\n'b_7_17^2+b_3_0^3*b_5_8+b_1_0^2*b_3_1^4+b_1_0^2*b_3_0^4+b_1_0^3*b_3_0^2*b_5_8+b_6_0*b_3_0*b_5_8+b_2_0*b_1_0^3*b_3_1^3+b_2_0*b_1_0^3*b_3_0^3+b_2_0*b_1_0^4*b_3_0*b_5_8+b_2_0*b_1_0^6*b_3_1^2+b_2_0*b_1_0^9*b_3_0+b_2_0*b_6_0*b_3_0^2+b_2_0^2*b_1_0*b_3_0^3+b_2_0^2*b_1_0^4*b_3_1^2+b_2_0^2*b_1_0^4*b_3_0^2+b_2_0^2*b_1_0^7*b_3_1+b_2_0^3*b_3_0*b_5_8+b_2_0^3*b_1_0^2*b_3_0^2+b_2_0^3*b_1_0^3*b_5_8+b_2_0^4*b_1_0*b_5_8+b_2_0^4*b_6_0+c_4_0*b_1_0*b_3_1^3+c_4_0*b_1_0^4*b_3_1^2+c_4_0*b_1_0^4*b_3_0^2+c_4_0*b_1_0^7*b_3_0+b_2_0*c_4_0*b_1_0^2*b_3_1^2+b_2_0*c_4_0*b_1_0^2*b_3_0^2+b_2_0*c_4_0*b_1_0^3*b_5_8+b_2_0*c_4_0*b_1_0^5*b_3_1+b_2_0*c_4_0*b_1_0^5*b_3_0+b_2_0*c_4_0*b_1_0^8+b_2_0^2*c_4_0*b_3_0^2+b_2_0^2*c_4_0*b_1_0*b_5_8+b_2_0^2*c_4_0*b_1_0^3*b_3_1+b_2_0^2*c_4_0*b_6_0+b_2_0^3*c_4_0*b_1_0*b_3_0+c_4_0^2*b_3_1^2+c_4_0^2*b_1_0^6+b_2_0*c_4_0^2*b_1_0*b_3_1+b_2_0*c_4_0^2*b_1_0^4+c_4_0^3*b_1_0^2'\nsage: H.relation_ideal().std(singular.ideal(P+H.standard_monomials(7))).dim()==0\nTrue\n```\n\n\nWhat can we do with this existence proof? We know that the Poincare series does not change by extending the field, and we know that we can choose its denominator as given by the degree of the parameters. Moreover, it is known that the Poincare series, as a rational function, has degree at most minus the depth of the cohomology ring. The following lines imply that the computation is complete (here is the [http://arxiv.org/abs/1004.0736 theoretical background), provided that one also shows that there are no generators in higher degree:\n\n```\nsage: H.subgroup_cohomology().depth()\n3\nsage: 4+12+7+6-3\n26\nsage: H.knownDeg>=26\nTrue\nsage: p = H.poincare_series()\nsage: t = p.parent().gen()\nsage: q = p*(1-t^4)*(1-t^12)*(1-t^7)*(1-t^6)\nsage: q.denominator()==1\nTrue\nsage: q.numerator().degree()<=26\nTrue\n```\n\n\nThere remains to show that there are no generators in higher degree, and this is where we use that the group is not of prime power order. It can be shown that the cohomology ring of *P* is a finitely generated module over the restriction of the cohomology of *G*. Moreover, if it is finitely generated as a module over the restriction of the ring approximation, generated in degree at most *n*, then the cohomology ring of *G* can be generated in degree at most *n*. Here, we find:\n\n```\nsage: Rest=[t.as_cocycle_in_subgroup().as_polynomial() for t in H.gens()[1:]]\nsage: HP = H.subgroup_cohomology()\nsage: HP.set_ring()\nsage: max([int(singular.eval('deg(%s)'%t)) for t in HP.relation_ideal().std(singular.ideal(Rest)).kbase()])\n8\n```\n\n\nHence, there are no generators above degree 8. Therefore, the computation can indeed be terminated in degree 26. I call this the *Hilbert-Poincare criterion*, and it seems to be the best method available.\n\n**__Tests__**\n\nI did successfully build and test on my machine (`x86_64 GNU/Linux`, Intel Core Duo), on bsd.math (both 32 and 64 bit) and on boxen.math. Any Python or Cython function is documented and has a test.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8667\n\n",
    "created_at": "2010-04-10T01:06:30Z",
    "labels": [
        "component: group_theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "New version of modular group cohomology spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8667",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @simon-king-jena

CC:  graham.ellis@nuigalway.ie david.green@uni-jena.de @jhpalmieri

Keywords: modular cohomology finite group

There is a major new version 2.0 of the p_group_cohomology spkg. It can be installed by

```
sage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.0.spkg
```

A test suite is run if `SAGE_CHECK=yes`. The results are printed on screen and saved in `install.log`. There is extensive [documentation](http://sage.math.washington.edu/home/SimonKing/Cohomology/).

**__Main New Features__**

The name "p_group_cohomology" used to mean "cohomology of p-groups". Now, it means "mod p cohomology of finite groups", i.e., the package now covers the case of non prime power groups as well. This is implemented in the new module `pGroupCohomology.modular_cohomology`.

With the new package version, we were able to compute the mod-p cohomology rings of many interesting groups and for different primes - see [here http://www.nuigalway.ie/maths/sk/Cohomology/rings/]. Most notably, we can compute the mod-2 cohomology rings of the third Conway group (it is Cohen-Macaulay) and the Higman-Sims group.

**__Minor Improvements__**

* The documentation is now backed up by references.
* As a safety feature, data in the Singular interface are reconstructed, should Singular crash. This is particularly important, since the new implementation *heavily* relies on Singular.
* More generally, I tried to make all potentially hard computations interruptible without data loss.
* The install script should be better portable:
  * The test for the presence of the Small Groups library is improved (compare #8523)
  * The environment variables `CC`, `AR`, `MKDIR`, `RM` etc are now used.
* In previous versions, it sometimes happened that `C-MeatAxe` wrote a multiplication table in the current directory. This is now stopped.

**__Theory__**

Both for prime power and non prime power groups, the basic approach is to approximate the cohomology ring degree by degree. A completeness criterion then asserts that the approximation is complete, so that the computation may terminate. More details and [references](http://sage.math.washington.edu/home/SimonKing/Cohomology/pGroupCohomology.html#references) can be found in the documentation.

__Prime power case__

For prime power groups, the approximation is computed using an initial segment of a minimal free resolution. We use a modification of Dave Benson's completeness criterion. In the new package version, we alternatively use a criterion of Peter Symonds.

The modified Benson criterion uses an existence result for small filter regular parameters over a finite field extension. For Symonds' criterion, the parameters don't need to be filter regular, but one can not use a field extension. For both criteria, small parameter degrees are helpful.

So, two things may happen:

* General parameters are of smaller degree than filter regular parameters: Advantage for the Symonds criterion.
* The degrees of filter regular parameters over an extension field are smaller than the degrees of general parameters without field extension: Advantage for the modified Benson criterion.

The program chooses between the two criteria. If *both* may apply, the Symonds criterion is preferred, since it is easier to use.

__Non prime power case__

The computations rely on the stable element method. Namely, the mod-*p* cohomology of a finite group *G* can be computed as a subring of the mod-*p* cohomology of any subgroup *P* of *G* whose index is coprime to *p*. This subring is characterised by so-called stability conditions given by pairs of induced maps.

So, eventually the computations rely on the computation of the cohomology ring of a prime power group. But this can be in several steps. By default, the program starts with the cohomology ring of a Sylow subgroup *S* and then proceeds to compute the cohomology of `P=Normaliser(G,Centre(S))` as a subring of the cohomology of *S*, and computes the cohomology of *G* as a subring of the cohomology of *P*.

The reason for choosing an intermediate subgroup between *G* and *S* is that the number of stability conditions usually drops drastically, compared with a direct computation with *P=S*.

Now, if the cohomology ring of *P* is computed, the ring structure of the cohomology of *G* can be computed in increasing degree, by solving the stability conditions. Eventually, it would be possible to use either Benson's or Symonds' criterion. 

However for non prime power groups, [another criterion](http://arxiv.org/abs/1004.0736) is available that combines the advantages of the other two criteria: It uses an existence proof for (not necessarily filter regular) parameters over a finite extension field, and it relies on the computation of the Poincare series of the ring approximation, which is relatively easy compared with a computation of the filter degree type.

**__Example__**

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

However, it turns out that *over some finite extension field*, the degree 14 parameter can be replaced by an element in degree 7. Note that this is impossible without a field extension, because otherwise the exhaustive search in `H.parameters()` would have detected it. The existence of the parameter can be shown like this:

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


There remains to show that there are no generators in higher degree, and this is where we use that the group is not of prime power order. It can be shown that the cohomology ring of *P* is a finitely generated module over the restriction of the cohomology of *G*. Moreover, if it is finitely generated as a module over the restriction of the ring approximation, generated in degree at most *n*, then the cohomology ring of *G* can be generated in degree at most *n*. Here, we find:

```
sage: Rest=[t.as_cocycle_in_subgroup().as_polynomial() for t in H.gens()[1:]]
sage: HP = H.subgroup_cohomology()
sage: HP.set_ring()
sage: max([int(singular.eval('deg(%s)'%t)) for t in HP.relation_ideal().std(singular.ideal(Rest)).kbase()])
8
```


Hence, there are no generators above degree 8. Therefore, the computation can indeed be terminated in degree 26. I call this the *Hilbert-Poincare criterion*, and it seems to be the best method available.

**__Tests__**

I did successfully build and test on my machine (`x86_64 GNU/Linux`, Intel Core Duo), on bsd.math (both 32 and 64 bit) and on boxen.math. Any Python or Cython function is documented and has a test.


Issue created by migration from https://trac.sagemath.org/ticket/8667





---

archive/issue_comments_078712.json:
```json
{
    "body": "Is \"group theory\" or \"optional packages\" the right component?",
    "created_at": "2010-04-10T01:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78712",
    "user": "https://github.com/simon-king-jena"
}
```

Is "group theory" or "optional packages" the right component?



---

archive/issue_comments_078713.json:
```json
{
    "body": "Changing component from group_theory to optional packages.",
    "created_at": "2010-04-10T01:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78713",
    "user": "https://github.com/simon-king-jena"
}
```

Changing component from group_theory to optional packages.



---

archive/issue_comments_078714.json:
```json
{
    "body": "I just did a small update of the package (a small aesthetic change in the method \"htmlpage\"). I'm running the doc tests now and will report back if it does *not* work.",
    "created_at": "2010-04-13T15:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78714",
    "user": "https://github.com/simon-king-jena"
}
```

I just did a small update of the package (a small aesthetic change in the method "htmlpage"). I'm running the doc tests now and will report back if it does *not* work.



---

archive/issue_comments_078715.json:
```json
{
    "body": "I posted another update of the package.\n\nI tried to make the package robust enough so that after interruption of Singular all relevant data are reconstructed, so that the computation can be resumed. The update concerns a case where this failed. Here is the relevant example (which forms a new doc test), that (in the originally posted package) used to result in an error:\n\n```\n            sage: from pGroupCohomology import CohomologyRing\n            sage: tmp = tmp_filename()\n            sage: CohomologyRing.set_user_db(tmp)\n            sage: H = CohomologyRing(48,50, prime=2)\n            sage: H.make()\n            sage: c = H.subgroup_cohomology()('c_1_1*c_1_2^2*c_1_3^3+c_1_1*c_1_2^4*c_1_3+c_1_1*c_1_2^5+c_1_1^2*c_1_3^4+c_1_1^2*c_1_2*c_1_3^3+c_1_1^2*c_1_2^3*c_1_3+c_1_1^3*c_1_2^2*c_1_3+c_1_1^3*c_1_2^3+c_1_1^4*c_1_3^2+c_1_1^4*c_1_2*c_1_3+c_1_1^4*c_1_2^2+c_1_1^5*c_1_2+c_1_0*c_1_3^5+c_1_0*c_1_2^2*c_1_3^3+c_1_0*c_1_2^3*c_1_3^2+c_1_0*c_1_1^2*c_1_2*c_1_3^2+c_1_0*c_1_1^2*c_1_2^2*c_1_3+c_1_0*c_1_1^2*c_1_2^3+c_1_0*c_1_1^3*c_1_3^2+c_1_0*c_1_1^3*c_1_2^2+c_1_0*c_1_1^4*c_1_3+c_1_0*c_1_1^5+c_1_0^2*c_1_3^4+c_1_0^2*c_1_2^2*c_1_3^2+c_1_0^2*c_1_2^3*c_1_3+c_1_0^2*c_1_2^4+c_1_0^2*c_1_1*c_1_3^3+c_1_0^2*c_1_1*c_1_2^2*c_1_3+c_1_0^2*c_1_1^2*c_1_2*c_1_3+c_1_0^2*c_1_1^2*c_1_2^2+c_1_0^2*c_1_1^3*c_1_2+c_1_0^3*c_1_2*c_1_3^2+c_1_0^3*c_1_1*c_1_2^2+c_1_0^3*c_1_1^2*c_1_3+c_1_0^3*c_1_1^3+c_1_0^4*c_1_3^2+c_1_0^4*c_1_2*c_1_3+c_1_0^4*c_1_2^2+c_1_0^4*c_1_1*c_1_2+c_1_0^4*c_1_1^2+c_1_0^5*c_1_3+c_1_0^5*c_1_1')\n            sage: d = H.stable_to_polynomial(c); d\n            c_3_6^2+c_3_2*c_3_7+c_3_2*c_3_6+c_3_0*c_3_7+c_3_0*c_3_6+c_3_0*c_3_5+c_3_0*c_3_4+c_3_0*c_3_3+c_2_3^3+c_2_2*c_2_3^2+c_2_1^2*c_2_3+c_2_1^3+c_2_0*c_2_3^2+c_2_0*c_2_1*c_2_2+c_2_0*c_2_1^2+c_2_0^2*c_2_3: 6-Cocycle in H^*(SmallGroup(48,50); GF(2))\n            sage: singular.quit()\n            sage: d == H.stable_to_polynomial(c)\n            True\n```\n\n\nExplanation: In the last line (i.e., after quitting Singular), the data of `c`, the data of `d` and the underlying data used in `stable_to_polynomial` are automatically reconstructed, so that the computation can be repeated, yielding the same result.",
    "created_at": "2010-04-15T08:54:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78715",
    "user": "https://github.com/simon-king-jena"
}
```

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

archive/issue_comments_078716.json:
```json
{
    "body": "I just realised that I forgot to label this ticket as \"needs review\". Sorry!",
    "created_at": "2010-04-15T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78716",
    "user": "https://github.com/simon-king-jena"
}
```

I just realised that I forgot to label this ticket as "needs review". Sorry!



---

archive/issue_comments_078717.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-15T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78717",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078718.json:
```json
{
    "body": "There have been some changes in the underlying modules concerning finite fields in sage-4.4. By consequence, some import statements broke.\n\nThis is fixed by importing ``from sage.all`` whenever possible. I just posted the updated spkg.",
    "created_at": "2010-04-26T13:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78718",
    "user": "https://github.com/simon-king-jena"
}
```

There have been some changes in the underlying modules concerning finite fields in sage-4.4. By consequence, some import statements broke.

This is fixed by importing ``from sage.all`` whenever possible. I just posted the updated spkg.



---

archive/issue_comments_078719.json:
```json
{
    "body": "(1) Add an .hgignore file to the hg repo:\n\n\n```\n$  hg status \n? src/bin/checksum\n? src/bin/chop\n? src/bin/chop.o\n...\n```\n\n\n(2) In spkg-install, change\n\n```\n# building parallely is bad. Therefore, although it is probably bad style:\nMAKE=make; export MAKE;\n```\n\nto \n\n```\nunset MAKE\n```\n\n\nThe doctest coverage is excellent:\n\n```\nwstein@sage:~/build/referee/sage-4.5/spkg/build/p_group_cohomology-2.0/src/pGroupCohomology$ sage -coverage .\n__init__.py: 100% (6 of 6)\nbarcode.py: 100% (15 of 15)\ncochain.pyx: 95% (108 of 113)\ncohomology.pyx: 100% (92 of 92)\ndickson.pyx: 100% (4 of 4)\nmodular_cohomology.pyx: 100% (30 of 30)\nmtx.pyx: 100% (40 of 40)\nresolution.pyx: 95% (59 of 62)\n\nOverall weighted coverage score:  97.6%\nTotal number of functions:  362\nWe need    5 more function to get to 99% coverage.\n```\n\n\n\nThis package is amazing!  It's also an amazing example of how to make an optional Sage package that involves lots of serious Cython code, but isn't part of the Sage library. \n\nAnd, all tests pass (on sage.math). \n\nSo, positive review.  However, fix (1),(2) above at some point (this is a minor nitpick).",
    "created_at": "2010-07-22T09:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78719",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_078720.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-22T09:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78720",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078721.json:
```json
{
    "body": "MErged into optional package repo.",
    "created_at": "2010-07-22T09:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78721",
    "user": "https://github.com/williamstein"
}
```

MErged into optional package repo.



---

archive/issue_events_008841.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-07-22T09:14:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8667#event-8841"
}
```



---

archive/issue_comments_078722.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T09:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78722",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_078723.json:
```json
{
    "body": "WARNING: In the newest version of sage there is a \"Tab detection\" feature in doctesting, which makes SPKG_CHECK fail:\n\n```\n\npGroupCohomology.cohomology.COHO.bar_code resulted in\nsage -t -optional -long \"RecDoctest.py\"\n**********************************************************************\nError: TAB character found.\n\n         [9.4 s]\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -optional -long \"RecDoctest.py\"\nTotal time for all tests: 9.4 seconds  \n\n-------------------------------------------------------------\npGroupCohomology.mtx.MTX.lead resulted in\nsage -t -optional -long \"RecDoctest.py\"\n**********************************************************************\nError: TAB character found.\n\n         [2.5 s]\n```\n",
    "created_at": "2010-07-22T09:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78723",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_078724.json:
```json
{
    "body": "Replying to [comment:8 was]:\n> MErged into optional package repo.\n\nDear William,\n\nI tried `install_package('p_group_cohomology')` but it still tries to install 1.2, not 2.0. \n\nReplying to [comment:7 was]:\n> (1) Add an .hgignore file to the hg repo:\n> \n> {{{\n> $  hg status \n> ? src/bin/checksum\n> ? src/bin/chop\n> ? src/bin/chop.o\n> ...\n> }}}\n\nThe spkg at http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.0.spkg *does* have .hgignore, and `hg status` reports nothing. But wait: Did you perhaps install the package manually? Because, src/bin/ is an empty directory, and the files checksum, chop etc are created during build.\n\n> The doctest coverage is excellent:\n> ...\n> Overall weighted coverage score:  97.6%\n\nOUTCH! I thought this was 100%, and actually my spkg-check was supposed to complain if there was any untested method. I'll fix this in version 2.1, which should be out soon (although it is only a minor upgrade).\n\nI posted an updated package at http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.0.spkg\n\nIt has \"unset MAKE\" in the spkg-install, adds one doctest, and removes the tab keys.\n\nCheers,\nSimon",
    "created_at": "2010-07-26T22:46:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78724",
    "user": "https://github.com/simon-king-jena"
}
```

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

The spkg at http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.0.spkg *does* have .hgignore, and `hg status` reports nothing. But wait: Did you perhaps install the package manually? Because, src/bin/ is an empty directory, and the files checksum, chop etc are created during build.

> The doctest coverage is excellent:
> ...
> Overall weighted coverage score:  97.6%

OUTCH! I thought this was 100%, and actually my spkg-check was supposed to complain if there was any untested method. I'll fix this in version 2.1, which should be out soon (although it is only a minor upgrade).

I posted an updated package at http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.0.spkg

It has "unset MAKE" in the spkg-install, adds one doctest, and removes the tab keys.

Cheers,
Simon



---

archive/issue_comments_078725.json:
```json
{
    "body": "> I tried install_package('p_group_cohomology') but it still tries to install 1.2, not 2.0.\n\nI think that Sage first looks in SAGE_ROOT/spkg/optional/ for the spkg file, and if it finds it, it installs that one.  Maybe you have an old copy of the spkg there?",
    "created_at": "2010-07-26T23:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78725",
    "user": "https://github.com/jhpalmieri"
}
```

> I tried install_package('p_group_cohomology') but it still tries to install 1.2, not 2.0.

I think that Sage first looks in SAGE_ROOT/spkg/optional/ for the spkg file, and if it finds it, it installs that one.  Maybe you have an old copy of the spkg there?



---

archive/issue_comments_078726.json:
```json
{
    "body": "Replying to [comment:11 jhpalmieri]:\n> I think that Sage first looks in SAGE_ROOT/spkg/optional/ for the spkg file, and if it finds it, it installs that one.  Maybe you have an old copy of the spkg there?\n\nNo, it was a freshly built Sage, and I just tested again: Even when I removed SAGE_ROOT/spkg/optional/p_group*, still `install_package('p_group_cohomology')` lead to the old version.\n\nIndeed, `./sage -optional` yields p_group_cohomology-1.2.p0\n\nCheers,\nSimon",
    "created_at": "2010-07-27T00:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78726",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:11 jhpalmieri]:
> I think that Sage first looks in SAGE_ROOT/spkg/optional/ for the spkg file, and if it finds it, it installs that one.  Maybe you have an old copy of the spkg there?

No, it was a freshly built Sage, and I just tested again: Even when I removed SAGE_ROOT/spkg/optional/p_group*, still `install_package('p_group_cohomology')` lead to the old version.

Indeed, `./sage -optional` yields p_group_cohomology-1.2.p0

Cheers,
Simon



---

archive/issue_comments_078727.json:
```json
{
    "body": "Maybe your mirror hasn't been updated?  I see both versions when I do `sage -optional`.",
    "created_at": "2010-07-27T00:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78727",
    "user": "https://github.com/jhpalmieri"
}
```

Maybe your mirror hasn't been updated?  I see both versions when I do `sage -optional`.



---

archive/issue_comments_078728.json:
```json
{
    "body": "Replying to [comment:13 jhpalmieri]:\n> Maybe your mirror hasn't been updated?  I see both versions when I do `sage -optional`.\n\nI am referring here to sage.math.\n\nIf I do `sage -optional` with the system wide Sage, I get\n\n```\nSimonKing@sage:~$ sage -optional\nUsing SAGE Server http://www.sagemath.org//packages\nhttp://www.sagemath.org//packages/optional/list --> /usr/local/sage/tmp/list\n[Errno 13] Permission denied: '/usr/local/sage/tmp/list'\n\n\n\n********************************************************************************\n\n\n\nError contacting http://www.sagemath.org//packages/optional/list. Try using an alternative server.\nFor example, from the bash prompt try typing\n\n   export SAGE_SERVER=http://sage.scipy.org/sage/\n\nthen try again.\n```\n\n\nIf I do it with a Sage that I built myself on sage.math:/scratch/sking/, I indeed see version 2.0 installed and 1.2 not installed. But when one does \n\n```\nsage: install_package('package_name')\n```\n\nthen v1.2 gets installed, with not taking into account v2.0.\n\nI think `install_package('package_name')` should always try to install the latest available version of `package_name`. Instead, it installs the latest *uninstalled* version, even though a more recent version is already installed.\n\nSo, I think there is a bug in `install_package`.",
    "created_at": "2010-07-27T07:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78728",
    "user": "https://github.com/simon-king-jena"
}
```

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

I think `install_package('package_name')` should always try to install the latest available version of `package_name`. Instead, it installs the latest *uninstalled* version, even though a more recent version is already installed.

So, I think there is a bug in `install_package`.



---

archive/issue_comments_078729.json:
```json
{
    "body": "FYI, I've just updated two osx binaries and I've seen that this spkg was not properly mirrored out to the mirrors. install_package is just fine, the problem was on the server.",
    "created_at": "2010-07-29T09:02:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8667",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8667#issuecomment-78729",
    "user": "https://github.com/haraldschilly"
}
```

FYI, I've just updated two osx binaries and I've seen that this spkg was not properly mirrored out to the mirrors. install_package is just fine, the problem was on the server.
