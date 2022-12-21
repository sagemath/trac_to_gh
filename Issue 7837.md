# Issue 7837: modular symbols -- change boundary space B_k when k odd to have the right dimension

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-01-03 23:44:04

Assignee: craigcitro

The dimension is currently computed to be too big in some cases when k is odd. E.g., this B below should be reported to have dimension 2, not 3:

```
sage: ModularSymbols(Gamma1(4),7).boundary_map().codomain().dimension()
3   # bad
```


Here's the email discussion of this:


```
> On Sun, 3 Jan 2010 13:51:19 -0800 (PST), Kilian:
>> Hello,
>>
>> i have a problem with sage and modular symbols for Gamma1(4) and odd
>> weight k, where the cusp 1/2 is irregular.
>>
>> According to Merel, there is (for k>2) an exact sequence:
>>
>> 0-> S_k -> M_k -> B_k -> 0
>>
>> Here B_k is the boundary space and S_k is the cuspidal subspace.
>>
>> Let the weight k be 7.
>>
>> If I compute the appropriate dimensions with SAGE,  I get 4,6 and 3
>> which can't be.  Furthermore, computing the boundary map, gives a
>> matrix which is definitely _not_ surjective.
>>
>> On the other hand, Merel explicitely states that the dimension of B_k
>> is the number of cusps, i.e. 3, so the failure must already be in
>> Merel's paper, or am I missing something?

The B_k in Merel's paper has dimension 2.   Merel does not state that dim(B_k) is the number of cusps in general.  That's only true when the weight is even. 

Sage does have a very small bug, which is that it computes the correct space B_k but embeds it (trivially) in a bigger space.  There is no need to do this, and I can see how it could be confusing.    The correct relations are used, the correct map is computed, it's just that there are extra 0's tacked on.   For example, in your example we have the following matrix for the boundary map:

[-1  0  0]
[ 0 -1  0]
[ 0 -1  0]
[ 0 -1  0]
[ 0  0  0]
[ 0  1  0]

notice that the extra dimension -- the 0 in the last column -- isn't involved.

The fix for this bug is to remove all the cusp classes that are equivalent to 0 because of the relation
    [Gamma(lambda u; lambda v)] ~ sign(lambda)^k[Gamma (u;v)]

For example, in your example that would be the class (u;v) = (1;2). 

>> I assume that 4 and 6 are correct, as a comparison with the usual
>> dimension tables for modular forms suggest.

Yes.

>> What is even more confusing is that Merel states that the isomorphism
>> between the boundary space and the space B_k(Gamma) is an
>> _isomorphism_, whereas in the SAGE sourcecode and in William Stein's
>> book it is only stated that it's injective.

Injectivity is all that is needed for the algorithm.  

 -- William

>>
>> Thanks in advance,
>> Kilian.
```



---

Comment by davidloeffler created at 2010-04-21 12:25:23

This has some substantial overlap with #6072, where I reported the same problem for GammaH groups. (This problem comes up much more often in the GammaH case than Gamma1, since Gamma1(N) has no irregular cusps unless N = 4.)


---

Comment by davidloeffler created at 2018-05-12 21:39:16

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2018-05-12 21:39:16

Fixed (and doctested) in the git branch I just uploaded at #6072. This ticket can be closed as duplicate when that gets merged.


---

Comment by davidloeffler created at 2018-05-13 13:46:52

Setting to positive_review, as #6072 now has a positive review.


---

Comment by davidloeffler created at 2018-05-13 13:46:52

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates
