# Issue 7837: modular symbols -- change boundary space B_k when k odd to have the right dimension

archive/issues_007837.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThe dimension is currently computed to be too big in some cases when k is odd. E.g., this B below should be reported to have dimension 2, not 3:\n\n```\nsage: ModularSymbols(Gamma1(4),7).boundary_map().codomain().dimension()\n3   # bad\n```\n\n\nHere's the email discussion of this:\n\n\n```\n> On Sun, 3 Jan 2010 13:51:19 -0800 (PST), Kilian:\n>> Hello,\n>>\n>> i have a problem with sage and modular symbols for Gamma1(4) and odd\n>> weight k, where the cusp 1/2 is irregular.\n>>\n>> According to Merel, there is (for k>2) an exact sequence:\n>>\n>> 0-> S_k -> M_k -> B_k -> 0\n>>\n>> Here B_k is the boundary space and S_k is the cuspidal subspace.\n>>\n>> Let the weight k be 7.\n>>\n>> If I compute the appropriate dimensions with SAGE,  I get 4,6 and 3\n>> which can't be.  Furthermore, computing the boundary map, gives a\n>> matrix which is definitely _not_ surjective.\n>>\n>> On the other hand, Merel explicitely states that the dimension of B_k\n>> is the number of cusps, i.e. 3, so the failure must already be in\n>> Merel's paper, or am I missing something?\n\nThe B_k in Merel's paper has dimension 2.   Merel does not state that dim(B_k) is the number of cusps in general.  That's only true when the weight is even. \n\nSage does have a very small bug, which is that it computes the correct space B_k but embeds it (trivially) in a bigger space.  There is no need to do this, and I can see how it could be confusing.    The correct relations are used, the correct map is computed, it's just that there are extra 0's tacked on.   For example, in your example we have the following matrix for the boundary map:\n\n[-1  0  0]\n[ 0 -1  0]\n[ 0 -1  0]\n[ 0 -1  0]\n[ 0  0  0]\n[ 0  1  0]\n\nnotice that the extra dimension -- the 0 in the last column -- isn't involved.\n\nThe fix for this bug is to remove all the cusp classes that are equivalent to 0 because of the relation\n    [Gamma(lambda u; lambda v)] ~ sign(lambda)^k[Gamma (u;v)]\n\nFor example, in your example that would be the class (u;v) = (1;2). \n\n>> I assume that 4 and 6 are correct, as a comparison with the usual\n>> dimension tables for modular forms suggest.\n\nYes.\n\n>> What is even more confusing is that Merel states that the isomorphism\n>> between the boundary space and the space B_k(Gamma) is an\n>> _isomorphism_, whereas in the SAGE sourcecode and in William Stein's\n>> book it is only stated that it's injective.\n\nInjectivity is all that is needed for the algorithm.  \n\n -- William\n\n>>\n>> Thanks in advance,\n>> Kilian.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7837\n\n",
    "created_at": "2010-01-03T23:44:04Z",
    "labels": [
        "component: modular forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "modular symbols -- change boundary space B_k when k odd to have the right dimension",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7837",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

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


Issue created by migration from https://trac.sagemath.org/ticket/7837





---

archive/issue_comments_067775.json:
```json
{
    "body": "This has some substantial overlap with #6072, where I reported the same problem for GammaH groups. (This problem comes up much more often in the GammaH case than Gamma1, since Gamma1(N) has no irregular cusps unless N = 4.)",
    "created_at": "2010-04-21T12:25:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7837#issuecomment-67775",
    "user": "https://github.com/loefflerd"
}
```

This has some substantial overlap with #6072, where I reported the same problem for GammaH groups. (This problem comes up much more often in the GammaH case than Gamma1, since Gamma1(N) has no irregular cusps unless N = 4.)



---

archive/issue_comments_067776.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-05-12T21:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7837#issuecomment-67776",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067777.json:
```json
{
    "body": "Fixed (and doctested) in the git branch I just uploaded at #6072. This ticket can be closed as duplicate when that gets merged.",
    "created_at": "2018-05-12T21:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7837#issuecomment-67777",
    "user": "https://github.com/loefflerd"
}
```

Fixed (and doctested) in the git branch I just uploaded at #6072. This ticket can be closed as duplicate when that gets merged.



---

archive/issue_comments_067778.json:
```json
{
    "body": "Setting to positive_review, as #6072 now has a positive review.",
    "created_at": "2018-05-13T13:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7837#issuecomment-67778",
    "user": "https://github.com/loefflerd"
}
```

Setting to positive_review, as #6072 now has a positive review.



---

archive/issue_comments_067779.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-05-13T13:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7837#issuecomment-67779",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067780.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7837#issuecomment-67780",
    "user": "https://github.com/videlec"
}
```

Resolution: wontfix



---

archive/issue_comments_067781.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7837#issuecomment-67781",
    "user": "https://github.com/videlec"
}
```

closing positively reviewed duplicates
