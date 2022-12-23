# Issue 6750: [with spkg, needs review] New version of optional Group Cohomology spkg

Issue created by migration from https://trac.sagemath.org/ticket/6750

Original creator: SimonKing

Original creation time: 2009-08-14 21:34:34

Assignee: Simon King

CC:  david.green@uni-jena.de graham.ellis@nuigalway.ie mik@math.stanford.edu

Keywords: cohomology ring p-group

There is a new version 1.1 of our optional spkg for the computation of modular cohomology rings of finite p-groups. It can be installed by

```
> sage -i http://sage.math.washington.edu/home/SimonKing/p_group_cohomology-1.1.spkg
```


As usual, if you did `export SAGE_CHECK=1` before installation, a test suite is automatically executed.

__News and Changes__

There is now a basic implementation of the _Yoneda cocomplex_. This enables us to compute *Massey products*. These are higher structures on cohomology rings and related with Steenrod powers and Bockstein operation. See examples below.

Our repository of cohomology rings now also provides the cohomology rings of the Sylow 2-subgroup of the Higman-Sims group (order 512) and of the Sylow 2-subgroup of the third Conway group (order 1024). They can be retrieved by

```
sage: H = CohomologyRing.web_db('Syl2HS')
```

or

```
sage: H = CohomologyRing.web_db('Syl2Co3')
```

I tested downloading the Conway example, and it took more than 30 minutes; but this is certainly faster than a computation from scratch, which would be about 3 days.

__Massey products__

The Massey product of cohomology ring elements `c1,c2,...,cn` is a _set_ of cohomology ring elements; it may be empty or may contain different cocycles.

D. Kraines modified this notion in the case of the `p^i` fold Massey product of a cocylce with itself. I refer to this as the i-th restricted Massey power. It is either not defined or is a single cocycle.

The restricted Massey powers can be expressed in terms of a composition of Steenrod powers and Bockstein operation, and they can be used to distinguish isomorphic cohomology rings. In particular, on degree one cocycles, the 1st restricted Massey power is the same as minus the Bockstein operation.

Example:

```
sage: from pGroupCohomology import CohomologyRing
sage: H3 = CohomologyRing(3,1)
sage: H3.make()
sage: H9 = CohomologyRing(9,1)
sage: H9.make()
sage: print H3

Cohomology ring of Small Group number 1 of order 3 with coefficients in GF(3)

Computation complete
Minimal list of generators:
[c_2_0, a 2-Cochain in H^*(SmallGroup(3,1); GF(3)),
 a_1_0, a 1-Cochain in H^*(SmallGroup(3,1); GF(3))]
Minimal list of algebraic relations:
[]

sage: print H9

Cohomology ring of Small Group number 1 of order 9 with coefficients in GF(3)

Computation complete
Minimal list of generators:
[c_2_0, a 2-Cochain in H^*(SmallGroup(9,1); GF(3)),
 a_1_0, a 1-Cochain in H^*(SmallGroup(9,1); GF(3))]
Minimal list of algebraic relations:
[]
```


So, the cohomology rings of the cyclic groups of order 3 and order 9 coincide. Note that for p>2, any element in odd degree squares to zero (by graded commutativity). At some point in the past, I decided to not list such _obvious_ relations, but I might change my mind...

Now, we compute the 1st restricted Massey powers of the degree one generators:

```
sage: H3.cochain_to_polynomial(H3.2.massey_power())
-c_2_0, a 2-Cochain in H^*(SmallGroup(3,1); GF(3))
sage: H9.cochain_to_polynomial(H9.2.massey_power())
0, a 2-Cochain in H^*(SmallGroup(9,1); GF(3))
```


They are different! Note that the 2nd restricted Massey power of the degree one generator is non-trivial for the cyclic group of order 9:

```
sage: H9.cochain_to_polynomial(H9.2.massey_power(2))
-c_2_0, a 2-Cochain in H^*(SmallGroup(9,1); GF(3))
```


As I mentioned, the non-restricted Massey product is set valued. Indeed, for the cohomology ring of the elementary abelian group of order 9, we obtain:

```
sage: H3_3 = CohomologyRing(9,2)
sage: H3_3.make()
sage: H3_3.3
a_1_0, a 1-Cochain in H^*(SmallGroup(9,2); GF(3))
sage: H3_3.massey_products(H3_3.3,H3_3.3,H3_3.3)

set([-c_2_1, a 2-Cochain in H^*(SmallGroup(9,2); GF(3)),
     a_1_0*a_1_1-c_2_1, a 2-Cochain in H^*(SmallGroup(9,2); GF(3)),
     -a_1_0*a_1_1-c_2_1, a 2-Cochain in H^*(SmallGroup(9,2); GF(3))])
```


Or, with our default example, the Dihedral Group of order 8:

```
sage: H = CohomologyRing(8,3)
sage: H.make()
sage: print H

Cohomology ring of Dihedral group of order 8 with coefficients in GF(2)

Computation complete
Minimal list of generators:
[c_2_2, a 2-Cochain in H^*(D8; GF(2)),
 b_1_0, a 1-Cochain in H^*(D8; GF(2)),
 b_1_1, a 1-Cochain in H^*(D8; GF(2))]
Minimal list of algebraic relations:
[b_1_0*b_1_1]

sage: H.massey_products(H.2,H.3,H.2)
set([0, a 2-Cochain in H^*(D8; GF(2)), b_1_0^2, a 2-Cochain in H^*(D8; GF(2))])
sage: H.massey_products(H.3,H.2,H.3)
set([0, a 2-Cochain in H^*(D8; GF(2)), b_1_1^2, a 2-Cochain in H^*(D8; GF(2))])
```


__Notes for the reviewer(s)__

The new stuff is documented at [http://sage.math.washington.edu/home/SimonKing/Cohomology/cochain.html#pGroupCohomology.cochain.YCOCH](http://sage.math.washington.edu/home/SimonKing/Cohomology/cochain.html#pGroupCohomology.cochain.YCOCH), [http://sage.math.washington.edu/home/SimonKing/Cohomology/resolution.html#pGroupCohomology.resolution.MasseyDefiningSystems](http://sage.math.washington.edu/home/SimonKing/Cohomology/resolution.html#pGroupCohomology.resolution.MasseyDefiningSystems), [http://sage.math.washington.edu/home/SimonKing/Cohomology/cochain.html#pGroupCohomology.cochain.COCH.massey_power](http://sage.math.washington.edu/home/SimonKing/Cohomology/cochain.html#pGroupCohomology.cochain.COCH.massey_power) and [http://sage.math.washington.edu/home/SimonKing/Cohomology/cohomology.html#pGroupCohomology.cohomology.COHO.massey_products](http://sage.math.washington.edu/home/SimonKing/Cohomology/cohomology.html#pGroupCohomology.cohomology.COHO.massey_products) 

If you know about Steenrod powers and Bockstein operation and those things, you might be able to cook up some interesting examples, and in particular to do verifications. I would appreciate it!


---

Comment by wdj created at 2009-08-15 21:30:23

This applies fine to an intel macbook running 10.4.11 and sage 4.1.1.rc2. Positive test form me as an optional package.

I cannot vouch for the mathematics though (however, I believe some functions on the older version were checked against some other programs for an independent.

Does this need further testing or can this be changed to "positive review".


---

Comment by SimonKing created at 2009-08-15 22:40:44

Dear David,

thank you that you found the time (despite of teaching) to look into it!

Replying to [comment:4 wdj]:
> This applies fine to an intel macbook running 10.4.11 and sage 4.1.1.rc2. Positive test form me as an optional package.
> 
> I cannot vouch for the mathematics though (however, I believe some functions on the older version were checked against some other programs for an independent.

Yes. Of course, it is hardly possible to test different ring presentations for being isomorphic. So, what I did was to see if I get the same number of generators resp. of relations (sorted by degree), and the same Poincaré series. This was mainly done for 2-groups: All groups of order 64, checked against the independent results of David Green and of Jon F. Carlson, and the Sylow 2-subgroup of the Higman-Sims group (order 512), whose cohomology ring was previously computed by Jon F. Carlson et al. There are only few cohomology computations for p-groups with p>2 available, but the results are consistent as well. 

> Does this need further testing or can this be changed to "positive review".

The main part of the programs, namely the computation of the ring structure, wasn't touched, and was carefully tested in the past. William did extensive installation tests on a multitude of platforms with the first package version, and I don't think that the new code can be critical for certain machines. 

So, the only part that _really_ needs review is the computation of Massey products. 

I tried to be careful in my implementation, of course, and to the best of my knowledge the results agree with what I found in the literature. But I find independent tests and peer reviewing quite important. So, I would not feel comfortable with a positive review before some experts assert that some non-trivial computational results involving Massey products are at least plausible.

One might try systematic cross verifications with the CRIME package, which computes Massey products as well. It would be quite difficult though to do it in detail, because one would have to deal with different ring presentations, and there might also be some different sign conventions around. 
At least, CRIME agrees that the cohomology rings of C_3 and C_9 can be distinguished using Massey products.

I should certainly ask Marcus Bishop, the author of CRIME, but I haven't seen him recently. 

Best regards,
Simon


---

Comment by SimonKing created at 2009-08-16 08:40:15

Perhaps I should point out in more detail _why_ I believe that an expert for Steenrod actions  might be able to provide good examples.

There is a general result of David Kraines, "Higher Products", Bulletin of the AMS 72 (1966), Part 1:128-131.

 __Theorem A (page 131)__
  - Let p>2 be a prime.
  - Let P<sup>m</sup>: H<sup>q</sup>(X;Z/p)->H<sup>q+2m(p-1)</sup>(X;Z/p) be the Steenrod pth power operation.
  - Let \beta denote the Bockstein operator associated with the exact sequence of coefficient groups 0 —> Z/p -> Z/p<sup>2</sup> -> Z/p -> 0
  - Let u be an element of H<sup>2m+1</sup>(X;Z/p).
  - Let <u><sup>p</sup> denote the p-fold restricted Massey product of a cocycle u (as defined by Kraines, so it is a single cocycle, not a _set_ of cocycles).
 Then   <u><sup>p</sup> = - \beta P<sup>m</sup>(u)

In our spkg, one would compute this restricted p-fold Massey product by `u.massey_power()`

I don't know of general results in the case of cocycles of even degree, though.


---

Comment by SimonKing created at 2009-08-16 15:59:30

Changing status from new to assigned.


---

Comment by SimonKing created at 2009-08-16 15:59:30

Changing assignee from Simon King to SimonKing.


---

Comment by SimonKing created at 2009-08-17 13:13:54

I found some cases in which the method COHO.massey_products() raises errors when it shouldn't. 
So, I need to sort it out -- "with spkg, needs work".

Meanwhile I was talking with Mikael Vejdemo Johannson, and he might be able to provide me with good test cases.


---

Comment by SimonKing created at 2009-08-17 15:43:46

I'd like to add Mikael Vejdemo Johansson to the Cc list, hope he doesn't mind.

I fixed the bug that was uncovered when trying to do some computations that Mika asked me to do. 

The spkg is updated and passes doc tests on sage.math, so, "needs review" (and "still needs examples"...).

One of the examples that failed previously is added as (long) doc test. Now, the following works (but takes a while):

```
sage: from pGroupCohomology import CohomologyRing
sage: tmp_root = tmp_filename()
sage: CohomologyRing.set_user_db(tmp_root)
sage: H = CohomologyRing(16,2)
sage: H.make()
sage: H.massey_products(H.3*H.1,H.3,H.3*H.1)

set([0, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_1*c_2_2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_1^2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_1*c_2_2*c_1_0*c_1_1+c_2_1^2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2))])
sage: H.massey_products(H.3*H.2,H.3,H.3*H.1)

set([c_2_1^2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_2^2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_1*c_2_2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_2^2*c_1_0*c_1_1+c_2_1*c_2_2*c_1_0*c_1_1+c_2_1^2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_2^2*c_1_0*c_1_1+c_2_1^2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_2^2*c_1_0*c_1_1+c_2_1*c_2_2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     0, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_1*c_2_2*c_1_0*c_1_1+c_2_1^2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2))])
sage: H.massey_products(H.4*H.2,H.4,H.4*H.2)

set([0, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_2^2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_2^2*c_1_0*c_1_1+c_2_1*c_2_2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2)),
     c_2_1*c_2_2*c_1_0*c_1_1, a 6-Cochain in H^*(SmallGroup(16,2); GF(2))])
```


Mika said that C4xC4 (=`SmallGroup(16,2)`) is particularly interesting to him. But I don't know what results would be expected.


---

Comment by SimonKing created at 2009-08-18 11:55:07

Meanwhile I learned more about Steenrod actions (thanks to David Green) and was able to construct some non-trivial example. Unfortunately, it failed. 

So, I have to start a bug hunting, and it is "needs work". Sorry!


---

Comment by SimonKing created at 2009-08-21 20:07:42

The problem is fixed and the package is updated at http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.1.spkg 

Technical reason for the problem was: 
If Y is the composition of two Yoneda cochains Y1, Y2, I thought that for computing higher terms of the composition it suffices to compose the lowest terms and then lift Y, i.e., extend a certain (anti-)commutative diagram. This is in fact possible if one just wants to compute the cup product. But for computing higher Massey products, one must lift Y1, Y2 sufficiently, and then compose the higher terms.

I extended the documentation, and thanks to the help of David Green I am now able to present a non-trivial example, explicitly verifying D. Kraines result for a cocycle of degree 3 of the Extraspecial 3-group of order 27 and exponent 3. It is also part of the doc tests.

I think that the example indicates that my implementation makes sense, so, I hope that a positive review (after installation+doctests on a couple of platforms) is now possible.

The example works as follows.

__First step:__ Study elementary abelian groups.


```
sage: tmp_root = tmp_filename()
sage: from pGroupCohomology import CohomologyRing
sage: CohomologyRing.set_user_db(tmp_root)
sage: H = CohomologyRing.user_db(9,2)
sage: H.make()
sage: H.gens()
[1,
 c_2_1, a 2-Cochain in H^*(SmallGroup(9,2); GF(3)),
 c_2_2, a 2-Cochain in H^*(SmallGroup(9,2); GF(3)),
 a_1_0, a 1-Cochain in H^*(SmallGroup(9,2); GF(3)),
 a_1_1, a 1-Cochain in H^*(SmallGroup(9,2); GF(3))]
```


Of course, there is a sign involved when choosing the generators, but in fact `c_2_1, c_2_2` are the Bocksteins of `a_1_0, a_1_1`. So, the following agrees with Kraines' theorem:

```
sage: H.cochain_to_polynomial(H.3.massey_power())
-c_2_1, a 2-Cochain in H^*(SmallGroup(9,2); GF(3))
sage: H.cochain_to_polynomial(H.4.massey_power())
-c_2_2, a 2-Cochain in H^*(SmallGroup(9,2); GF(3))
```


Fortunately the cohomology rings of elementary abelian groups are very simple, and thus allow for a direct computation of Steenrod powers and Bocksteins in higher degree. We consider C = a_1_0*c_2_1_. By Cartan formula and since P<sup>0</sup> is the identity, we have 
  P<sup>1</sup>(C) = P<sup>1</sup>(a_1_0) c_2_1 + a_1_0 P(c_2_1). 

Since P<sup>1</sup> vanishes in degree one and acts as the p-th power in degree two, we get 
  P<sup>1</sup>(C) = a_1_0 c_2_1<sup>3</sup>. 

Applying the Bockstein operator \beta, we get 
  \beta P<sup>1</sup>(C) = c_2_1<sup>4</sup>, 
since \beta(c_2_1) = \beta<sup>2</sup>(a_1_0) = 0 and since \beta(xy)=\beta(x)y + (-1)^deg x^x\beta(y). 

Hence, according to Kraines, the first restricted Massey power of C should be  
  <C; 1> = - c_2_1<sup>4</sup>. 

And indeed:

```
sage: (H.1*H.3).massey_power()
<(c_2_1)*(a_1_0); 1>, a 8-Cochain in H^*(SmallGroup(9,2); GF(3))
sage: H.cochain_to_polynomial(_)
-c_2_1^4, a 8-Cochain in H^*(SmallGroup(9,2); GF(3))
```


__Second Step:__ Apply Kraines formula to the restrictions to maximal elementary abelian subgroups

This is the cohomology ring of the extraspecial 3-group of order 27 and exponent 3:

```
sage: H = CohomologyRing.user_db(27,3)
sage: H.make()
```


We want to compute the 1st Massey power of a generator in degree 3:

```
sage: C = H.8
sage: C
a_3_4, a 3-Cochain in H^*(E27; GF(3))
```


There are 4 maximal elementary abelian subgroups (all of order 9). We get the restriction maps and compute the restrictions of C:

```
sage: r1 = H.restriction_maps()[2][1]
sage: r1
Induced homomorphism of degree 0 from H^*(E27; GF(3)) to H^*(SmallGroup(9,2); GF(3))
sage: r2 = H.restriction_maps()[3][1]
sage: r3 = H.restriction_maps()[4][1]
sage: r4 = H.restriction_maps()[5][1]
sage: U = r1.codomain()
sage: U.cochain_to_polynomial(r1(C))
-c_2_2*a_1_0+c_2_1*a_1_1, a 3-Cochain in H^*(SmallGroup(9,2); GF(3))
sage: U.cochain_to_polynomial(r2(C))
0, a 3-Cochain in H^*(SmallGroup(9,2); GF(3))
sage: U.cochain_to_polynomial(r3(C))
-c_2_2*a_1_0+c_2_1*a_1_1, a 3-Cochain in H^*(SmallGroup(9,2); GF(3))
sage: U.cochain_to_polynomial(r4(C))
c_2_2*a_1_1+c_2_2*a_1_0-c_2_1*a_1_1, a 3-Cochain in H^*(SmallGroup(9,2); GF(3))
```


Hence, after computing Bockstein and Steenrod power in the maximal elementary abelian subgroups as above, and since Steenrod power and Bockstein commute with restriction maps, the theorem of Kraines tells us that <C; 1> should restrict to 
  * c_2_1 c_2_2<sup>3</sup> - c_2_1<sup>3</sup>c_2_2, 
  * 0, 
  * c_2_1 c_2_2<sup>3</sup> - c_2_1<sup>3</sup>c_2_2, and 
  * -c_2_2<sup>4</sup> - c_2_1 c_2_2<sup>3</sup> + c_2_1<sup>3</sup>c_2_2. 

This is indeed the case:

```
sage: CP = C.massey_power()
sage: U.cochain_to_polynomial(r1(CP))
c_2_1*c_2_2^3-c_2_1^3*c_2_2, a 8-Cochain in H^*(SmallGroup(9,2); GF(3))
sage: U.cochain_to_polynomial(r2(CP))
0, a 8-Cochain in H^*(SmallGroup(9,2); GF(3))
sage: U.cochain_to_polynomial(r3(CP))
c_2_1*c_2_2^3-c_2_1^3*c_2_2, a 8-Cochain in H^*(SmallGroup(9,2); GF(3))
sage: U.cochain_to_polynomial(r4(CP))
-c_2_2^4-c_2_1*c_2_2^3+c_2_1^3*c_2_2, a 8-Cochain in H^*(SmallGroup(9,2); GF(3))
```


It is known that for this group, a cocycle is uniquely determined by its restrictions to the maximal elementary abelian subgroups. Hence, we have verified the computation of the first restricted Massey power of C.


---

Comment by SimonKing created at 2009-08-21 20:38:05

PS: Concerning installation tests, I don't know if it suffices to do `sage -f http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.1.spkg` or if you first need to remove the copy of the old spkg in $SAGE_ROOT/spkg/optional/. 

So, please take care that you really get the updated version!


---

Comment by wdj created at 2009-08-21 22:25:40

This installs fine and passes all tests on an intel macbook running 10.4.11.


---

Comment by jhpalmieri created at 2009-08-25 16:06:53

A few installation issues: it requires database_gap, but if I download that spkg and install it from the downloaded version (that is, using "sage -i path_to/database_gap-4.4.10.spkg" rather than "sage -i database_gap-4.4.10", which downloads the file), then its installation is recorded in SAGE_ROOT/spkg/installed, but not in SAGE_ROOT/spkg/optional, which is where your spkg-install looks.

Second, it doesn't seem to install on my Intel Mac running 10.5, either 32-bit or 64-bit. I get this error:

```
ar rv /Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a os.o
ar rv /Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a profile.o
ar: /Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a: Resource temporarily unavailable
make[2]: *** [/Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a(profile.o)] Error 1
make[2]: *** Waiting for unfinished jobs....
a - os.o
rm -f os.o
make[1]: *** [all] Error 2
make: *** [all] Error 2
Error building pGroupCohomology.
```



---

Comment by SimonKing created at 2009-08-25 18:52:48

Hi John,

Replying to [comment:14 jhpalmieri]:
> A few installation issues: it requires database_gap, but if I download that spkg and install it from the downloaded version (that is, using "sage -i path_to/database_gap-4.4.10.spkg" rather than "sage -i database_gap-4.4.10", which downloads the file), then its installation is recorded in SAGE_ROOT/spkg/installed, but not in SAGE_ROOT/spkg/optional, which is where your spkg-install looks.

I didn't know that. IIRC, the part of spkg-install that checks for the presence of the database is more or less copied from the Developer's Guide. So, do you think I should look in both locations?

> Second, it doesn't seem to install on my Intel Mac running 10.5, either 32-bit or 64-bit. I get this error:
> ...
> ar: /Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a: Resource temporarily unavailable
> make[2]: *** [/Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a(profile.o)] Error 1
> make[2]: *** Waiting for unfinished jobs....
> ...
> }}}

This is bad. I have never seen this error message. In particular, I don't know what is meant by "Resource temporarily unavailable": Is there a race condition? 

If I am not mistaken, Intel Mac running 10.5 was one of the platforms where installation of the previous version worked. However, David Joyner said that in one case (I think on a MacBook) things only worked when trying to install for the second time, see [http://trac.sagemath.org/sage_trac/ticket/6491#comment:41](http://trac.sagemath.org/sage_trac/ticket/6491#comment:41) and the preceding comments. Of course, it would be good to understand why that happens sometimes. 

How could one try to sort out these problems? Unfortunately, I have no access to an Intel Mac.

Best regards,
Simon


---

Comment by SimonKing created at 2009-08-25 21:42:46

Replying to [comment:15 SimonKing]:
> Replying to [comment:14 jhpalmieri]:
> > A few installation issues: it requires database_gap, but if I download that spkg and install it from the downloaded version (that is, using "sage -i path_to/database_gap-4.4.10.spkg" rather than "sage -i database_gap-4.4.10", which downloads the file), then its installation is recorded in SAGE_ROOT/spkg/installed, but not in SAGE_ROOT/spkg/optional, which is where your spkg-install looks.
> 
> I didn't know that. IIRC, the part of spkg-install that checks for the presence of the database is more or less copied from the Developer's Guide. So, do you think I should look in both locations?

Definitely it does not suffice to look in SAGE_ROOT/spkg/installed _only_, which I just checked.

Do you think the following snipped would be fine for spkg-install?

```
SMALL_GROUPS=`cd $SAGE_ROOT/spkg/optional/; $SAGE_ROOT/spkg/standard/newest_version database_gap`
if [ "$SMALL_GROUPS" = "" ]; then
    SMALL_GROUPS=`cd $SAGE_ROOT/spkg/installed/; $SAGE_ROOT/spkg/standard/newest_version database_gap`
    if [ "$SMALL_GROUPS" = "" ]; then
        echo "Failed to find SmallGroups library.  Please install the database_gap spkg"
        exit 1
    fi
fi
```


Regards,
Simon


---

Comment by SimonKing created at 2009-08-25 22:08:56

Replying to [comment:14 jhpalmieri]:
...
> Second, it doesn't seem to install on my Intel Mac running 10.5, either 32-bit or 64-bit. I get this error:
> {{{
> ar rv /Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a os.o
> ar rv /Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a profile.o
> ar: /Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a: Resource temporarily unavailable
> make[2]: *** [/Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a(profile.o)] Error 1
> make[2]: *** Waiting for unfinished jobs....
> a - os.o
> rm -f os.o
> make[1]: *** [all] Error 2
> make: *** [all] Error 2
> Error building pGroupCohomology.
> }}}

Two things might be worth mentioning:

1. If I am not mistaken, C-MeatAxe still does not explicitly mention support for OS X. So, it is perhaps not a surprise that OS X isn't easy here.

2. Six months ago, it was a problem to build David Green's C-routines when linked against an optimized libmtx.a (i.e., using -O3). Therefore, I build libmtx.a twice: First with -O1, then I build David Green's programs, then I build libmtx.a again with a potentially higher optimization, and then I link my Cython code against the optimized libmtx.a. 

Could "2." be the reason for the problem that you met? 

I just tested that at least on my new machine (Intel Core Duo, openSuse 11.0) this nastiness is actually not needed, even when building with -O3. 

So, I suggest the following:

 * Search both SAGE_ROOT/spkg/optional and SAGE_ROOT/spkg/installed for database_gap.
 * Try using -O3 straight away. 

But I think in this case, a thorough build test is needed, similar to what William has done with the first version of the spkg.


---

Comment by jhpalmieri created at 2009-08-25 22:47:59

Replying to [comment:16 SimonKing]:
> Replying to [comment:15 SimonKing]:
> > Replying to [comment:14 jhpalmieri]:
> > > A few installation issues: it requires database_gap, but if I download that spkg and install it from the downloaded version (that is, using "sage -i path_to/database_gap-4.4.10.spkg" rather than "sage -i database_gap-4.4.10", which downloads the file), then its installation is recorded in SAGE_ROOT/spkg/installed, but not in SAGE_ROOT/spkg/optional, which is where your spkg-install looks.
> > 
> > I didn't know that. IIRC, the part of spkg-install that checks for the presence of the database is more or less copied from the Developer's Guide. So, do you think I should look in both locations?

I think the one in the Developer's Guide is checking for something in spkg/standard, which ought to be, well, more standard.  When checking for optional packages, maybe more care is needed?  Anyway, the code snippet looks okay to me.  It should be easy enough to test.

>So, I suggest the following:
> - Search both SAGE_ROOT/spkg/optional and SAGE_ROOT/spkg/installed for database_gap.
> - Try using -O3 straight away.

These sound good to me.


---

Comment by SimonKing created at 2009-08-25 23:27:40

Replying to [comment:18 jhpalmieri]:
> >So, I suggest the following:
> > - Search both SAGE_ROOT/spkg/optional and SAGE_ROOT/spkg/installed for database_gap.
> > - Try using -O3 straight away.
> 
> These sound good to me.

Unfortunately, the "-O3" option does not work, at least on sage.math.

So, I have to try to sort these build problems out in the next few days.


---

Comment by SimonKing created at 2009-08-26 08:45:02

I try to summarize how I came to the idea to build libmtx.a twice.

 - When I tried higher optimizations, I found out that at least one executable of David Green (purpose: Computation of a particularly nice basis of the group algebra) only works when linked against a version of libmtx.a that was build with at most -O1.
 - In order to have higher optimization available (and faster code?) I separated things, so, I had one libmtx.a for David Green's executables and another libmtx.a for the rest.

But after looking at my Makefile, I realize that in fact the second version of libmtx.a is using -O1 as well. I remember that I made performance tests with different optimizations, and it could be that in fact -O2 or -O3 does not yield faster code.  

Now, I suggest the following approach:

 1. I test -O1, -O2, -O3 on sage.math and another machine. 

 2. Should it turn out that -O1 is the fastest anyway then I build libmtx.a only once, an I reckon this would solve the problem.

 3. If -O2 or -O3 is faster, then I should probably stick with two versions of libmtx.a. But then I must find a way to work around the sporadic build problems on a MacBook.

John, I still  wonder about the error message in your report. Why can't libmtx.a be accessed? Is it perhaps the case that the MacBook tries a parallel build? If this is the case, how can I switch it off?

Cheers,
Simon


---

Comment by SimonKing created at 2009-08-26 22:32:46

It turned out that building libmtx.a twice was an artifact of my previous attempts to find a proper optimization. 

My test case: Compute the cohomology for all groups of order 64 from scratch, and compare with the known result.

I tested it with four different package versions. In all cases, I was first building libmtx.a with -O1, so that David's executables work. Then, I built libmtx.a again, with -O0, -O1, -O2, -O3, and -Os. Note that the Cython extensions are build with -O3 anyway. 

In Galway (Intel Core Duo) and on sage.math, I got the following CPU times:

 * -O0, Galway: 18.73 min, sage.math: 29.73 min
 * -O1, Galway: 18.32 min, sage.math: 27.76 min
 * -O2, Galway: 18.31 min, sage.math: 28.70 min
 * -O3, Galway: 18.48 min, sage.math: 29.20 min
 * -Os, Galway: 18.74 min, sage.math: not finished yet.

This indicates that indeed a thorough -O1 optimization is good, perhaps best. 

I got similar results a few months ago. So, the logical consequence should have been to build libmtx.a only once, namely with -O1. But then I forgot to remove the double build approach.

*Summary*

Updated spkg is at [http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.1.spkg](http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.1.spkg)

The build process is now probably cleaner, namely searching for database_gap both in spkg/optional and spkg/installed, and building libmtx.a only once. I hope that the problems on MacBook, where the resource libmtx.a wasn't available, are resolved by now.

I use this occasion for another change: The "public cohomology data base", that is shared by all users of a Sage install, is now located in SAGE_DATA/pGroupCohomology/, rather than in SAGE_ROOT/local/pGroupCohomology/db. William wrote on sage-devel that this is a better location. I guess so far I am the only user who really did extensive computations with the package. So, I think there is no need for a warning message concerning the potential need of relocating the user's data.

John, of course I'd appreciate if you could try it on your Intel Mac again. Since the build process changed, I am now asking William whether he thinks that a thorough test (on all machines in William's park) is needed.

Cheers,
Simon


---

Comment by jhpalmieri created at 2009-08-27 01:53:10

No luck with the new build.  What else can I try?


---

Comment by SimonKing created at 2009-08-27 13:52:11

Replying to [comment:22 jhpalmieri]:
> No luck with the new build.  What else can I try?

I don't know. 

On the one hand, this is strange, because I understood that William successfully tested building the first package version on all machines in his build park, and I thought this would also include an Intel Mac. And if I am not mistaken, I did not change our C-MeatAxe adaptation since then.

On the other hand, when I tried to build an earlier version (not yet spkg) on a Mac Book at the Sage Days in San Diego, C-MeatAxe was a problem as well, and in fact the C-MeatAxe web site does not explicitly mention support for OS X. From that point of view, I was positively surprised when David Joyner first reported a successful build on some OS X machine.

Do you still get the same error,

```
ar rv /Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a os.o
ar rv /Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a profile.o
ar: /Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a: Resource temporarily unavailable
make[2]: *** [/Applications/sage_builds/sage-4.1.1-binary/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a(profile.o)] Error 1
make[2]: *** Waiting for unfinished jobs....
a - os.o
```

?

But what does it mean that libmtx.a is temporarily unavailable? Of course, libmtx.a should eventually contain functions to link against. Can you see from the protocol output whether _some_ functions made it into libmtx.a? Or is os.o and provile.o the first thing that is tried?

What happens if you try to install older version, say, http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.0.1.spkg ?

There is an experimental meataxe spkg, "meataxe-2.4.3". Does this build on your Intel Mac? If this is the case, I may try to learn from its Makefile.

I think I will ask on sage-devel whether some Mac expert can help to hunt the error down.

Best regards,
Simon


---

Comment by SimonKing created at 2009-08-27 14:51:29

Replying to [comment:23 SimonKing]:
> Replying to [comment:22 jhpalmieri]:
> [...]
> What happens if you try to install older version, say, http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.0.1.spkg ?

Sorry, I meant to write "1.0.2". Since it is an optional package, it should be available in a sage session by

```
sage: install_package('p_group_cohomology')
```



---

Comment by jhpalmieri created at 2009-08-27 15:16:57

Note: Don't use "export MAKE='make -j2'"; that seems to be what's causing the problems.  (See [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/35c05ab37f77f888).)

If it's possible, the spkg-install file could check for this.


---

Comment by jhpalmieri created at 2009-08-27 15:26:52

This doesn't work with a 64-bit Mac OS X install.  It seems to install okay, although during the build process, I saw the message

"ld warning: in /Applications/sage/local/lib/libmtx.a, file is not of required architecture"

Then when I run it, I get

```
sage: from pGroupCohomology import CohomologyRing
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/Users/palmieri/.sage/temp/Macintosh.local/76717/_Users_palmieri__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.6/site-packages/pGroupCohomology/__init__.py in <module>()
   1073 from sage.rings.integer import Integer
   1074 from sage.interfaces.singular import singular
-> 1075 from pGroupCohomology.cohomology import COHO
   1076 from pGroupCohomology.resolution import OPTION
   1077 import re

ImportError: dlopen(/Applications/sage/local/lib/python2.6/site-packages/pGroupCohomology/cohomology.so, 2): Symbol not found: _LPR
  Referenced from: /Applications/sage/local/lib/python2.6/site-packages/pGroupCohomology/cohomology.so
  Expected in: dynamic lookup
```


It seems to work with a 32-bit Sage build, though, so that's some good news.


---

Comment by SimonKing created at 2009-08-27 16:11:10

How can I test whether "make -j2" is used? And what should be done _if_ "make -j2 is used? Exit with an error? Sorry, I am really not an expert for writing shell scripts.

Replying to [comment:26 jhpalmieri]:
> This doesn't work with a 64-bit Mac OS X install.  It seems to install okay, although during the build process, I saw the message
> 
> "ld warning: in /Applications/sage/local/lib/libmtx.a, file is not of required architecture"

OK, so something goes wrong.

> Then when I run it, I get
> {{{ [...]
> ImportError: dlopen(/Applications/sage/local/lib/python2.6/site-packages/pGroupCohomology/cohomology.so, 2): Symbol not found: _LPR
>   Referenced from: /Applications/sage/local/lib/python2.6/site-packages/pGroupCohomology/cohomology.so
>   Expected in: dynamic lookup
> }}}

This is very strange. There is the symbol "LPR" in libmtx.a, but no "_LPR". So, I wonder how this error message arose.


---

Comment by jhpalmieri created at 2009-08-27 16:30:25

Replying to [comment:27 SimonKing]:
> How can I test whether "make -j2" is used? And what should be done _if_ "make -j2 is used? Exit with an error? Sorry, I am really not an expert for writing shell scripts.

Me neither, sorry.

For the 64-bit issue, at one point I browsed through some spkgs to see what they did in 64-bit mode (in an attempt to solve the problem at #6681).  Givaro does this:

```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   echo "64 bit MacIntel"
   CFLAGS="-O2 -g -m64 "; export CFLAGS
   CPPFLAGS="-O2 -g -m64 "; export CPPFLAGS
   LDFLAGS="-m64"; export LDFLAGS
fi
```

I am not an expert at this by any stretch of the imagination, but this kind of thing seems more or less standard for 64-bit builds in Sage spkgs; the -m64 flag tells the compiler to build for 64-bit architecture.


---

Comment by SimonKing created at 2009-08-27 17:49:24

Replying to [comment:28 jhpalmieri]:
> For the 64-bit issue, at one point I browsed through some spkgs to see what they did in 64-bit mode (in an attempt to solve the problem at #6681).  Givaro does this:
> {{{
> if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
>    echo "64 bit MacIntel"
>    CFLAGS="-O2 -g -m64 "; export CFLAGS
>    CPPFLAGS="-O2 -g -m64 "; export CPPFLAGS
>    LDFLAGS="-m64"; export LDFLAGS
> fi
> }}}

OK, I tried to do something similar: spkg-install is defining DARWIN64, which is either "-m64" or "". It is exported, and subsequently used by the Makefiles of meataxe and of David Green's programs.

I updated the spkg at http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.1.spkg which is preliminary, since it does not yet test for parallel build. 

But it tries to deal with the 64 bit issue. John, can you please try again, with parallel build disabled? And could you please verify whether on the 64 bit machine the option "-m64" is really used?

Regards,
Simon


---

Comment by jhpalmieri created at 2009-08-27 18:43:24

Hi Simon,

"-m64" is used some of the time, but not always, and so the build fails.  For example:

```
gcc	 -Wall -DASM_MMX -g -O1 -m64 -DOS_DEFAULT -fPIC -o maketab /Applications/sage/spkg/build/p_group_cohomology-1.1/src/mtx2.2.4/src/maketab.c  /Applications/sage/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a
```

looks good.  On the other hand:

```
gcc -I/Applications/sage/spkg/build/p_group_cohomology-1.1/src/mtx2.2.4/src/ -Wall -g -fPIC -O1    -c -o mam.o /Applications/sage/spkg/build/p_group_cohomology-1.1/src/present/src/mam.c
```

As the build process fails:

```
gcc -L/Applications/sage/spkg/build/p_group_cohomology-1.1/src/lib -o makeActionMatrices mam.o pgroup.o perror.o -lmtx
ld warning: in /Applications/sage/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a, file is not of required architecture
Undefined symbols:
  "_tnull", referenced from:
      _tnull$non_lazy_ptr in pgroup.o
  "_matinv", referenced from:
      _makeBasisChangeMatrices in pgroup.o
  "_zalloc", referenced from:
      _allocateMatrixList in pgroup.o
      _basisChangeReg2Nontips in pgroup.o
      _changeActionMatricesReg2Nontips in pgroup.o
      _makeLeftActionMatrices in pgroup.o

[snip]

ld: symbol(s) not found
collect2: ld returned 1 exit status
make[1]: *** [makeActionMatrices] Error 1
```


I don't see DARWIN64 in


---

Comment by SimonKing created at 2009-08-27 18:59:11

Replying to [comment:30 jhpalmieri]:
> Hi Simon,
> 
> "-m64" is used some of the time, but not always, and so the build fails.  For example:
> [...]
> {{{
> gcc -L/Applications/sage/spkg/build/p_group_cohomology-1.1/src/lib -o makeActionMatrices mam.o pgroup.o perror.o -lmtx
> ld warning: in /Applications/sage/spkg/build/p_group_cohomology-1.1/src/lib/libmtx.a, file is not of required architecture
> [...]
> }}}
> 
> I don't see DARWIN64 in 

I think that's a progress, because this time we consider building of David Green's files, not of MeatAxe. 

Perhaps you downloaded the spkg 5 minutes too early, because I first forgot to modify `src/present/Makefile` as well. But meanwhile, it contains the lines 

```
CFLAGS=-I$(MTXSRC) -Wall -g -fPIC -O1 $(DARWIN64)
LFLAGS=-L$(MTXLIBDIR) $(DARWIN64)
LFLAGS2=-l$(MTXLIBNAME) $(DARWIN64)
```


Cheers,
Simon


---

Comment by SimonKing created at 2009-08-27 19:12:53

William answered on sage-devel how one might kill the parallel build problem (namely by setting MAKE=make).

I changed the spkg correspondingly (sorry if this created another "race condition" between John and me...)


---

Comment by jhpalmieri created at 2009-08-27 20:04:03

Okay, the 64-bit change looks good; I haven't looked at the "MAKE" vs. "make" change yet.  Builds on both 32- and 64-bit, and spkg-check works almost completely: with the 64-bit build, all tests pass, and with the 32-bit build, I get 

```
Testing the components of the package pGroupCohomology...
pGroupCohomology --> Error
```

and then everything else passes.  The log file says

```
sage -t -optional -long "RecDoctest.py"                     
**********************************************************************
File "/Users/palmieri/.sage/temp/Macintosh.local/90792/RecDoctest.py", line 399:
    sage: H0.massey_products(H0.2,H0.3,H0.2,H0.3)
Expected:
    set([c_2_2, a 2-Cochain in H^*(D8; GF(2)),
         b_1_0^2+c_2_2, a 2-Cochain in H^*(D8; GF(2)),
         b_1_1^2+b_1_0^2+c_2_2, a 2-Cochain in H^*(D8; GF(2)),
         b_1_1^2+c_2_2, a 2-Cochain in H^*(D8; GF(2))])
Got:
    set([b_1_0^2+c_2_2, a 2-Cochain in H^*(D8; GF(2)), c_2_2, a 2-Cochain in H^*(D8; GF(2)), b_1_1^2+c_2_2, a 2-Cochain in H^*(D8; GF(2)), b_1_1^2+b_1_0^2+c_2_2, a 2-Cochain in H^*(D8; GF(2))])
**********************************************************************
File "/Users/palmieri/.sage/temp/Macintosh.local/90792/RecDoctest.py", line 404:
    sage: H0.massey_products(H0.2*H0.1,H0.3*H0.1,H0.2*H0.1) # long time
Expected:
    set([c_2_2*b_1_0^6+c_2_2^2*b_1_0^4, a 8-Cochain in H^*(D8; GF(2)),
         c_2_2*b_1_0^6, a 8-Cochain in H^*(D8; GF(2)),
         c_2_2^3*b_1_0^2, a 8-Cochain in H^*(D8; GF(2)),
         c_2_2^2*b_1_0^4+c_2_2^3*b_1_0^2, a 8-Cochain in H^*(D8; GF(2)),
         c_2_2*b_1_0^6+c_2_2^2*b_1_0^4+c_2_2^3*b_1_0^2, a 8-Cochain in H^*(D8; GF(2)),
         c_2_2^2*b_1_0^4, a 8-Cochain in H^*(D8; GF(2)),
         0, a 8-Cochain in H^*(D8; GF(2)),
         c_2_2*b_1_0^6+c_2_2^3*b_1_0^2, a 8-Cochain in H^*(D8; GF(2))])
Got:
    set([c_2_2^2*b_1_0^4, a 8-Cochain in H^*(D8; GF(2)), c_2_2*b_1_0^6+c_2_2^2*b_1_0^4, a 8-Cochain in H^*(D8; GF(2)), c_2_2*b_1_0^6+c_2_2^2*b_1_0^4+c_2_2^3*b_1_0^2, a 8-Cochain in H^*(D8; GF(2)), c_2_2^2*b_1_0^4+c_2_2^3*b_1_0^2, a 8-Cochain in H^*(D8; GF(2)), 0, a 8-Cochain in H^*(D8; GF(2)), c_2_2*b_1_0^6+c_2_2^3*b_1_0^2, a 8-Cochain in H^*(D8; GF(2)), c_2_2*b_1_0^6, a 8-Cochain in H^*(D8; GF(2)), c_2_2^3*b_1_0^2, a 8-Cochain in H^*(D8; GF(2))])
```

I haven't check carefully, but these look like the same sets, just in different orders.

By the way, to be really nitpicky, could we change "a 8-cochain" to "an 8-cochain"?  (What other numbers need this: 11, 18, 80-89?)


---

Comment by jhpalmieri created at 2009-08-27 20:18:26

Okay, the newest version builds on both 32-bit and 64-bit, whether I have "MAKE" set to "make -j2" or not.


---

Comment by SimonKing created at 2009-08-28 09:50:53

Replying to [comment:34 jhpalmieri]:
> Okay, the newest version builds on both 32-bit and 64-bit, whether I have "MAKE" set to "make -j2" or not.

Great!

So, my homework for today is to try to find and fix the doc test that uses sets or dictionaries (there has been a remark of William on sage-devel or sage-support concerning doc tests that use dictionaries). Indeed you are right, in the failing doc test we have the same sets in different order.

Concerning "a 8-cochain" to "an 8-cochain": Normally I try to be grammatically correct (as much as possible for me, a non-native speaker). If you look at some of the doc-tests, you will see that I use 1st, 2nd, 3rd, 101st and so on, rather than always doing `"%d-th"%n`. But I would prefer to do this change in the next version.

Cheers,
Simon


---

Comment by SimonKing created at 2009-08-28 16:02:44

Hi John!

Again concerning "an 8-cochain" versus "a 8-cochain": What is the rule for having "an" rather than "a"? Would one say "an onehundred-cochain"? Or is "an" only in front of "a,e,i"? 

Perhaps the most elegant way out would be "a cochain of degree 8". But, as I said, I'd like to spare this for the next version, if you don't veto.

Meanwhile I fixed the doc tests, i.e., if there are sets or dictionaries left then they contain precisely one item, so that there is no problem with ambiguity, and in all other cases I used ordered lists.

I committed the changes in the spkg's hg repository, and put everything online. Hopefully all issues are fixed by now.

Best regards,
Simon


---

Comment by SimonKing created at 2009-08-29 16:26:57

Hi John,

Replying to [comment:34 jhpalmieri]:
> Okay, the newest version builds on both 32-bit and 64-bit, whether I have "MAKE" set to "make -j2" or not.

Thanks to William, I have now also access to a Darwin, apparently 32 bit, and the package builds and tests fine there. 

It also builds and tests fine on Intel Core Duo (openSuse 11.0) and on sage.math

sage.math is the slowest in that list. For whatever reason, our spkg seems to run quite good on Intel processors, although it was developed on AMD processors.

Perhaps now is the time to turn to mathematics: Do you think that my example of Massey products makes sense? I was informed by Marcus Bishop that his CRIME package returns "fail" (which it shouldn't) when computing the triple Massey product of a degree 3 cocycle of the cyclic group of order 3. So, we can not cross check the results of our package with the results of CRIME.


---

Comment by SimonKing created at 2009-09-09 10:47:51

Thanks to Mikael Vejdemo Johansson, I detected another bug in the computation of restricted Massey powers. In this example (cohomology of C_4 times C_4), the answers of COHO.massey_products() and of COCH.massey_power() were inconsistent. 

It is fixed, and used as a doc test, as follows:

```
sage: tmp_root = tmp_filename()
sage: from pGroupCohomology import CohomologyRing
sage: CohomologyRing.set_user_db(tmp_root)
sage: H = CohomologyRing.user_db(16,2)
sage: H.make()
sage: x,a,b,c,d = H.gens()
sage: c
c_1_0, a 1-Cochain in H^*(SmallGroup(16,2); GF(2))
sage: d
c_1_1, a 1-Cochain in H^*(SmallGroup(16,2); GF(2))
sage: H.cochain_to_polynomial(c.massey_power())
0, a 2-Cochain in H^*(SmallGroup(16,2); GF(2))
sage: H.cochain_to_polynomial(d.massey_power())
0, a 2-Cochain in H^*(SmallGroup(16,2); GF(2))
sage: H.cochain_to_polynomial(c.massey_power(2))
c_2_1, a 2-Cochain in H^*(SmallGroup(16,2); GF(2))
sage: H.cochain_to_polynomial(d.massey_power(2))
c_2_2, a 2-Cochain in H^*(SmallGroup(16,2); GF(2))
```

According to Mikael, this is what he expected (but in the previous version, a null cocycle was returned). The result is consistent with the set-valued Massey products:

```
sage: sorted(list(H.massey_products(c,c,c,c)))
[c_2_1, a 2-Cochain in H^*(SmallGroup(16,2); GF(2)),
 c_2_1+c_1_0*c_1_1, a 2-Cochain in H^*(SmallGroup(16,2); GF(2))]
sage: sorted(list(H.massey_products(d,d,d,d)))
[c_2_2, a 2-Cochain in H^*(SmallGroup(16,2); GF(2)),
 c_2_2+c_1_0*c_1_1, a 2-Cochain in H^*(SmallGroup(16,2); GF(2))]
```


The example that I gave previously (a degree 3 cocycle of SmallGroup(27,3)) is still in accordance with theoretical results, it did not change.


---

Comment by SimonKing created at 2009-09-09 13:03:30

Replying to [comment:38 SimonKing]:
> Thanks to Mikael Vejdemo Johansson, I detected another bug in the computation of restricted Massey powers. In this example (cohomology of C_4 times C_4), the answers of COHO.massey_products() and of COCH.massey_power() were inconsistent. 
> 
> It is fixed, ...

... and the technical problem was as follows: In COCH.massey_power() was a loop starting at 0, but it should have started at 1. By consequence, a cocycle (which in general would be non-zero) was added to itself, resulting in zero (in characteristic two). 

The only change in the code is to let this loop start at 1, and then of course there are new doc tests.

Just for the record...

Cheers, 
Simon


---

Comment by SimonKing created at 2009-09-10 11:45:04

I just had a chat with Mikael, and if I understood him correctly then the results of the current package version on the cohomology of C_4 times C_4 are what he expected.

Mikael, please correct me if the following contains too much nonsense.


```
sage: from pGroupCohomology import CohomologyRing
sage: H = CohomologyRing.user_db(16,2)
sage: H.make()
sage: x,a,b,c,d = H.gens()
sage: x,a,b,c,d

(1,
 c_2_1, a 2-Cochain in H^*(SmallGroup(16,2); GF(2)),
 c_2_2, a 2-Cochain in H^*(SmallGroup(16,2); GF(2)),
 c_1_0, a 1-Cochain in H^*(SmallGroup(16,2); GF(2)),
 c_1_1, a 1-Cochain in H^*(SmallGroup(16,2); GF(2)))
```


The Massey products allow to create the whole cohomology ring out of the degree-1-generators, c and d:

```
sage: H.massey_products(c,c,c,c,all=False)
set([c_2_1, a 2-Cochain in H^*(SmallGroup(16,2); GF(2))])
sage: H.massey_products(d,d,d,d,all=False)
set([c_2_2, a 2-Cochain in H^*(SmallGroup(16,2); GF(2))])
```


After fixing the previous bug, massey_power yields the same result:

```
sage: H.cochain_to_polynomial(c.massey_power(2))
c_2_1, a 2-Cochain in H^*(SmallGroup(16,2); GF(2))
sage: H.cochain_to_polynomial(d.massey_power(2))
c_2_2, a 2-Cochain in H^*(SmallGroup(16,2); GF(2))
```


Usually, the Massey products behave multiplicatively in the first and last position:

```
sage: H.massey_products(c*d,c,c,c,all=False)
set([c_2_1*c_1_1, a 3-Cochain in H^*(SmallGroup(16,2); GF(2))])
sage: H.massey_products(c,c,c,c*d,all=False)
set([c_2_1*c_1_1, a 3-Cochain in H^*(SmallGroup(16,2); GF(2))])
```


In this example, it is actually multiplicative in _all_ four positions:

```
sage: H.massey_products(c,c*d,c,c,all=False)
set([c_2_1*c_1_1, a 3-Cochain in H^*(SmallGroup(16,2); GF(2))])
sage: H.massey_products(c,c,c*d,c,all=False)
set([c_2_1*c_1_1, a 3-Cochain in H^*(SmallGroup(16,2); GF(2))])
```


By consequence, higher Massey products involving at least two factors `c*d` are either not defined or vanish:

```
sage: H.massey_products(c*d,c,c,c*d,c,all=False)
set()
```

This makes sense since `H.massey_products(c,c,c*d,c)` is non-zero, thus, the above fivefold product is not defined.


```
sage: H.massey_products(c*d,c*d,c*d,c*d,c*d,c*d,c*d,c*d,c*d,c,all=False)
set([0, a 11-Cochain in H^*(SmallGroup(16,2); GF(2))])
```

This makes sense since we can extract the `d` factors, but `d*d` is zero, so, the whole Massey product is zero.

David and John, do you think that this now seems stable enough for being an optional package? AFAIK the build problems on Intel Mac are resolved: Meanwhile William provided me with access to such machines, and it works both 32 and 64 bit. Actually, I did the above examples on Intel Mac 64 bit, since on my computer in Galway and on sage.math I meanwhile have a package version 2.0 minus epsilon.

Best regards,
Simon


---

Comment by SimonKing created at 2009-09-10 12:02:40

Here is a comment of Mikael:

Replying to [comment:40 SimonKing]:
> I just had a chat with Mikael, and if I understood him correctly then the results of the current package version on the cohomology of C_4 times C_4 are what he expected.
> 
> Mikael, please correct me if the following contains too much nonsense.
[...]
> Usually, the Massey products behave multiplicatively in the first and last position:
> ...

Mikael answered

"""

I would hesitate to say _usually_ without an actual argument backing  
it up. In what I have observed when computing on A-infinity  
structures, this seems very often to be the case.

"""

I misunderstood that there is a theorem for it. 

Anyway, here apparently it is the case.

Cheers,
Simon


---

Comment by jhpalmieri created at 2009-09-10 14:49:49

Replying to [comment:41 SimonKing]:
> Replying to [comment:40 SimonKing]:
> > I just had a chat with Mikael, and if I understood him correctly then the results of the current package version on the cohomology of C_4 times C_4 are what he expected.
> > 
> > Mikael, please correct me if the following contains too much nonsense.
> [...]
> > Usually, the Massey products behave multiplicatively in the first and last position:
> > 

[snip]

> I misunderstood that there is a theorem for it. 

There is a theorem for it.  Look in _Complex cobordism and stable homotopy groups of spheres_ by Ravenel, Appendix A1.4.  (You can download it [here](http://www.math.rochester.edu/people/faculty/doug/mu.html#repub)).  According to A1.4.6, up to a sign, b<x1, x2, ...> is contained in <bx1, x2, ...>, and similarly for the last position.  There is also an addition formula: see A1.4.5 in Ravenel.  If you can provide doctests for some of these in some examples, that would be great.


---

Comment by SimonKing created at 2009-09-10 16:48:21

Dear John,

Replying to [comment:42 jhpalmieri]:
> There is a theorem for it.  Look in _Complex cobordism and stable homotopy groups of spheres_ by Ravenel, Appendix A1.4.  
> According to A1.4.6, up to a sign, b<x1, x2, ...> is contained in <bx1, x2, ...>, and similarly for the last position. 

Thank you for your hint!

Ravenel says "In most cases the first page or two of the file is blank. These files are in the process of being revised and should not be quoted publicly." 

So, it seems that I can not cite the theorems from his book. Or is the numbering in the printed version the same?

> There is also an addition formula: see A1.4.5 in Ravenel.  If you can provide doctests for some of these in some examples, that would be great. 

This theorem refers to the matric Massey product. If I understand correctly (but I am not an expert) what I implemented is not the matric version of the Massey products. So, can you explain how I can create an example out of Addition Theorem?

But the Juggling Theorem works:

```
sage: from pGroupCohomology import CohomologyRing
sage: H = CohomologyRing.user_db(27,3)
sage: H.make()
sage: H.gens()
[1,
 b_2_0, a 2-Cochain in H^*(E27; GF(3)),
 b_2_1, a 2-Cochain in H^*(E27; GF(3)),
 b_2_2, a 2-Cochain in H^*(E27; GF(3)),
 b_2_3, a 2-Cochain in H^*(E27; GF(3)),
 c_6_8, a 6-Cochain in H^*(E27; GF(3)),
 a_1_0, a 1-Cochain in H^*(E27; GF(3)),
 a_1_1, a 1-Cochain in H^*(E27; GF(3)),
 a_3_4, a 3-Cochain in H^*(E27; GF(3)),
 a_3_5, a 3-Cochain in H^*(E27; GF(3))]
sage: H.massey_products(H.6,H.6,H.6,all=False)
set([-b_2_0, a 2-Cochain in H^*(E27; GF(3))])
sage: H.massey_products(H.1*H.6,H.6,H.6,all=False)
set([-b_2_0^2, a 4-Cochain in H^*(E27; GF(3))])
sage: H.massey_products(H.2*H.6,H.6,H.6,all=False)
set([-b_2_0*b_2_1, a 4-Cochain in H^*(E27; GF(3))])
sage: H.massey_products(H.3*H.6,H.6,H.6,all=False)
set([-b_2_0*b_2_2, a 4-Cochain in H^*(E27; GF(3))])
sage: H.massey_products(H.4*H.6,H.6,H.6,all=False)
set([-b_2_0*b_2_1, a 4-Cochain in H^*(E27; GF(3))])
```

There is no sign change, since we multiplied by cocycles of even degree. So far, so easy. 

But now comes the really interesting example:

```
sage: H.massey_products(H.6,H.6,H.6*H.5,all=False)
set([-b_2_0^2*a_1_1*a_3_5+b_2_0^2*a_1_0*a_3_5-b_2_0*c_6_8, a 8-Cochain in H^*(E27; GF(3))])
```


Is this fine?

Yes, it is!

Note that there is the summand `-b_2_0*c_6_8` that we would expect. There remains to show that the other summands belong to the indeterminacy of the Massey product. More precisely, I want to show that `-b_2_0<sup>2*a_1_1*a_3_5+b_2_0</sup>2*a_1_0*a_3_5` is a multiple of `H.6`.


```
sage: H.6*(2*H.8*H.2*H.2+2*H.8*H.1*H.2 + H.1^2*H.9) == H('-b_2_0^2*a_1_1*a_3_5+b_2_0^2*a_1_0*a_3_5')
True
```


I think this would be a nice example for the doc string of COHO.massey_products!


---

Comment by SimonKing created at 2009-09-10 18:04:43

Replying to [comment:43 SimonKing]:
[...]
> I think this would be a nice example for the doc string of COHO.massey_products!

Done! The package is updated, and the new test can be found at http://sage.math.washington.edu/home/SimonKing/Cohomology/cohomology.html#pGroupCohomology.cohomology.COHO.massey_products .

Doc tests pass, at least for Intel Mac 64 bit.

Cheers,
Simon


---

Comment by jhpalmieri created at 2009-09-10 20:41:00

Replying to [comment:43 SimonKing]:
> Dear John,
> 
> Replying to [comment:42 jhpalmieri]:
> > There is a theorem for it.  Look in _Complex cobordism and stable homotopy groups of spheres_ by Ravenel, Appendix A1.4.  
> > According to A1.4.6, up to a sign, b<x1, x2, ...> is contained in <bx1, x2, ...>, and similarly for the last position. 
> 
> Thank you for your hint!
> 
> Ravenel says "In most cases the first page or two of the file is blank. These files are in the process of being revised and should not be quoted publicly." 
> 
> So, it seems that I can not cite the theorems from his book. Or is the numbering in the printed version the same?

The numbering I gave you is from the first edition of the book; the numbering in the on-line version is from a pre-print of the second edition, which has now been published.  I would guess that the numbering is probably the same in the published version of the second edition, but you could also just say "Section A1.4".

> > There is also an addition formula: see A1.4.5 in Ravenel.  If you can provide doctests for some of these in some examples, that would be great. 
> 
> This theorem refers to the matric Massey product. If I understand correctly (but I am not an expert) what I implemented is not the matric version of the Massey products. So, can you explain how I can create an example out of Addition Theorem?

You're right, I'm not sure what to do with the matrices there.  But doctests for the juggling theorem are great -- thanks!

I'm not good enough with group cohomology to come up with other examples to test this out; I think your doctests (and the evidence of the success of the juggling theorems) is enough for me to give this a positive review.


---

Comment by SimonKing created at 2009-09-11 08:41:33

Trying to update some technical informations (milestone, reviewers). I hope I chose the right format (namely to give the real names, not the user names).

Question: Must the people listed as reviewers have a Trac account, or does it suffice if they contributed off list? Namely, working on examples suggested by David Green and Mikael Vejdemo Johansson resulted in fixing some bugs and creating new doc tests. So, can they be named in the reviewer list as well? I think I'll ask sage-devel.

If you agree and want to add their names, note that Mikael's family name has two parts _without_ hyphen, and Vejdemo is _not_ a middle name. So, AFAIK, he would neither like "Mikael V. Johansson" nor "Mikael Johansson"...


---

Comment by SimonKing created at 2009-09-11 13:10:24

On sage-devel, Minh said that it seems reasonable to mention David and Mikael as reviewers. I do it so.


---

Comment by SimonKing created at 2009-09-11 14:33:25

Minh elaborated on sage-devel that the "Author(s)" field of a ticket is not for the authors of the _ticket_ but for the authors of the _code_ that the ticket refers to. My misunderstanding was that naming the authors of the code in the code's documentation and in the Sage release tour is what really counts.

So, I am moving David Green from "Reviewer(s)" to "Author(s)".


---

Comment by mvngu created at 2009-09-11 17:51:49

Merged in the optional packages repository at

http://www.sagemath.org/packages/optional/

The updated optional package can be found at 

http://www.sagemath.org/packages/optional/p_group_cohomology-1.1.spkg


---

Comment by mvngu created at 2009-09-11 17:51:49

Resolution: fixed
