# Issue 5664: Bugs in PermutationGroup_subgroup.__cmp__

archive/issues_005664.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: comparison subgroup\n\nAt http://groups.google.com/group/sage-support/browse_thread/thread/533747d48a1f29eb?hl=en\nit was reported that comparision of subgroups of permutation groups does not work as expected:\n\n\n```\nsage: G = SymmetricGroup(4)\nsage: H = G.subgroup([G((1,2,3))])\nsage: K = G.subgroup([G((2,3,1))]) \nsage: G((1,2,3))==G((2,3,1))\nTrue\nsage: K==H\nFalse\n```\n\n\nEven worse, comparison may raise an error -- afaik, the Python specification says that `__cmp__` is not supposed to raise errors:\n\n```\nsage: G2=G.subgroup([G((1,2,3,4)),G((1,2))])\nsage: G==G2\nTrue\nsage: G2==G\nTraceback (most recent call last):\n...\nAttributeError: 'SymmetricGroup' object has no attribute 'ambient_group'\n```\n\n\nSo, `==` is not a symmetric relation.\n\nOf course, G==G2 invokes G.__cmp__(G2), which tests whether G and G2 are the same as PermutationGroup_generic.\nIn contrast, G2==G tests whether G2 and G are the same as PermutationGroup_subgroup.\n\nSo, what do people want?\n1. A symmetric relation? Then K.__cmp__() should invoke PermutationGroup_generic.__cmp__().\n2. Or should K.__cmp__(H) test whether K and H are subgroups of the same PermutationGroup, and then continue with testing whether K and H are subgroup of each other?\n\nNote that the with 1., == would test whether K and H are isomorphic abstract groups, which is the job of K.is_isomorphic(H). \n\nTherefore, I am in favour of 2. \n\nBut then: \n* What should be returned if neither H is a subgroup of K nor K is a subgroup of H?\n* What should be returned if H is subgroup of G1 and K is subgroup of G2, with H contained in K contained in G2 contained in G1? Currently, K.__cmp__(H) would  -1 in this case (hence, H<K although K is contained in H!). Example:\n {{{\nsage: G=SymmetricGroup(6)\nsage: G1=G.subgroup([G((1,2,3,4,5)),G((1,2))])\nsage: G2=G.subgroup([G((1,2,3,4)),G((1,2))])\nsage: K=G2.subgroup([G1((1,2,3))])\nsage: H=G1.subgroup([G2(())])\nsage: H<K\nFalse\nsage: K<H\nTrue\n}}}\n\nSo, the trivial group in G1 is considered greater than a non-trivial group in G2, because G1>G2.\n\nSo, before working on a patch, I'd like to get people's opinion on what is a good specification of 'comparison of subgroups'.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5664\n\n",
    "created_at": "2009-04-02T06:39:32Z",
    "labels": [
        "algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Bugs in PermutationGroup_subgroup.__cmp__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5664",
    "user": "@simon-king-jena"
}
```
Assignee: tbd

Keywords: comparison subgroup

At http://groups.google.com/group/sage-support/browse_thread/thread/533747d48a1f29eb?hl=en
it was reported that comparision of subgroups of permutation groups does not work as expected:


```
sage: G = SymmetricGroup(4)
sage: H = G.subgroup([G((1,2,3))])
sage: K = G.subgroup([G((2,3,1))]) 
sage: G((1,2,3))==G((2,3,1))
True
sage: K==H
False
```


Even worse, comparison may raise an error -- afaik, the Python specification says that `__cmp__` is not supposed to raise errors:

```
sage: G2=G.subgroup([G((1,2,3,4)),G((1,2))])
sage: G==G2
True
sage: G2==G
Traceback (most recent call last):
...
AttributeError: 'SymmetricGroup' object has no attribute 'ambient_group'
```


So, `==` is not a symmetric relation.

Of course, G==G2 invokes G.__cmp__(G2), which tests whether G and G2 are the same as PermutationGroup_generic.
In contrast, G2==G tests whether G2 and G are the same as PermutationGroup_subgroup.

So, what do people want?
1. A symmetric relation? Then K.__cmp__() should invoke PermutationGroup_generic.__cmp__().
2. Or should K.__cmp__(H) test whether K and H are subgroups of the same PermutationGroup, and then continue with testing whether K and H are subgroup of each other?

Note that the with 1., == would test whether K and H are isomorphic abstract groups, which is the job of K.is_isomorphic(H). 

Therefore, I am in favour of 2. 

But then: 
* What should be returned if neither H is a subgroup of K nor K is a subgroup of H?
* What should be returned if H is subgroup of G1 and K is subgroup of G2, with H contained in K contained in G2 contained in G1? Currently, K.__cmp__(H) would  -1 in this case (hence, H<K although K is contained in H!). Example:
 {{{
sage: G=SymmetricGroup(6)
sage: G1=G.subgroup([G((1,2,3,4,5)),G((1,2))])
sage: G2=G.subgroup([G((1,2,3,4)),G((1,2))])
sage: K=G2.subgroup([G1((1,2,3))])
sage: H=G1.subgroup([G2(())])
sage: H<K
False
sage: K<H
True
}}}

So, the trivial group in G1 is considered greater than a non-trivial group in G2, because G1>G2.

So, before working on a patch, I'd like to get people's opinion on what is a good specification of 'comparison of subgroups'.

Issue created by migration from https://trac.sagemath.org/ticket/5664





---

archive/issue_comments_044293.json:
```json
{
    "body": "Changing assignee from tbd to @simon-king-jena.",
    "created_at": "2009-04-02T06:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44293",
    "user": "@simon-king-jena"
}
```

Changing assignee from tbd to @simon-king-jena.



---

archive/issue_comments_044294.json:
```json
{
    "body": "Based on how I think mathematicians would most likely use this, I'm in favor of 1. \n\nIn any case, I don't agree that \"with 1., == would test whether K and H are isomorphic abstract groups\". The code is\n\n\n```\n        if not isinstance(right, PermutationGroup_generic):\n            return -1\n        return right._gap_().__cmp__(self._gap_())\n```\n\nwhich seems to be a wrapper for GAP's equality. Does that seem right to you?",
    "created_at": "2009-04-02T09:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44294",
    "user": "@wdjoyner"
}
```

Based on how I think mathematicians would most likely use this, I'm in favor of 1. 

In any case, I don't agree that "with 1., == would test whether K and H are isomorphic abstract groups". The code is


```
        if not isinstance(right, PermutationGroup_generic):
            return -1
        return right._gap_().__cmp__(self._gap_())
```

which seems to be a wrapper for GAP's equality. Does that seem right to you?



---

archive/issue_comments_044295.json:
```json
{
    "body": "Changing component from algebra to group_theory.",
    "created_at": "2009-04-02T09:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44295",
    "user": "@wdjoyner"
}
```

Changing component from algebra to group_theory.



---

archive/issue_comments_044296.json:
```json
{
    "body": "Hi,\n\nReplying to [comment:3 wdj]:\n> Based on how I think mathematicians would most likely use this, I'm in favor of 1. \n> \n> In any case, I don't agree that \"with 1., == would test whether K and H are isomorphic abstract groups\". The code is\n> \n> {{{\n>         if not isinstance(right, PermutationGroup_generic):\n>             return -1\n>         return right._gap_().__cmp__(self._gap_())\n> }}}\n> which seems to be a wrapper for GAP's equality. Does that seem right to you?\n\nRight. My (apparently wrong) assumption was that gap tests for isomorphism.\nSo, my reason for supporting 1. broke.\n\nHowever, who did implement (I guess overloaded) the `__cmp__` method of PermutationGroup_generic for PermutationGroup_subgroup? What was the original reason for taking into account the ambient group?\n\nCheers,\n    Simon",
    "created_at": "2009-04-02T09:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44296",
    "user": "@simon-king-jena"
}
```

Hi,

Replying to [comment:3 wdj]:
> Based on how I think mathematicians would most likely use this, I'm in favor of 1. 
> 
> In any case, I don't agree that "with 1., == would test whether K and H are isomorphic abstract groups". The code is
> 
> {{{
>         if not isinstance(right, PermutationGroup_generic):
>             return -1
>         return right._gap_().__cmp__(self._gap_())
> }}}
> which seems to be a wrapper for GAP's equality. Does that seem right to you?

Right. My (apparently wrong) assumption was that gap tests for isomorphism.
So, my reason for supporting 1. broke.

However, who did implement (I guess overloaded) the `__cmp__` method of PermutationGroup_generic for PermutationGroup_subgroup? What was the original reason for taking into account the ambient group?

Cheers,
    Simon



---

archive/issue_comments_044297.json:
```json
{
    "body": "> However, who did implement (I guess overloaded) the __cmp__ method of \n> PermutationGroup?_generic for PermutationGroup?_subgroup? What was the \n> original reason for taking into account the ambient group?\n\nI think that was my stupid idea. I don't remember what I was thinking, sorry.\nMaybe an {{{is_equal}} (as subgroups) was what I was thinking, though I'm\nnot sure how useful that is, given == and {{{ambient_group}} are existing methods.",
    "created_at": "2009-04-02T10:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44297",
    "user": "@wdjoyner"
}
```

> However, who did implement (I guess overloaded) the __cmp__ method of 
> PermutationGroup?_generic for PermutationGroup?_subgroup? What was the 
> original reason for taking into account the ambient group?

I think that was my stupid idea. I don't remember what I was thinking, sorry.
Maybe an {{{is_equal}} (as subgroups) was what I was thinking, though I'm
not sure how useful that is, given == and {{{ambient_group}} are existing methods.



---

archive/issue_comments_044298.json:
```json
{
    "body": "I just observed another detail that I found strange.\n\nNote that in `PermutationGroup_generic.__cmp__(self,right)`, the return value is `right._gap_().__cmp__(self._gap_())`, not `self._gap_().__cmp__(right._gap_())`.\n\nBy consequence, we have \n\n```\nsage: G = PermutationGroup([[(1,2)]])\nsage: H = PermutationGroup([[()]])\nsage: G<H\nTrue\n```\n\n\nIs this something that we want? I also ask on the mailing list, as this seems fundamental to me.",
    "created_at": "2009-04-02T12:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44298",
    "user": "@simon-king-jena"
}
```

I just observed another detail that I found strange.

Note that in `PermutationGroup_generic.__cmp__(self,right)`, the return value is `right._gap_().__cmp__(self._gap_())`, not `self._gap_().__cmp__(right._gap_())`.

By consequence, we have 

```
sage: G = PermutationGroup([[(1,2)]])
sage: H = PermutationGroup([[()]])
sage: G<H
True
```


Is this something that we want? I also ask on the mailing list, as this seems fundamental to me.



---

archive/issue_comments_044299.json:
```json
{
    "body": "I have a suggestion for a fix.\n\n1. For comparing PermutationGroup_generic, rely on gap, without reversion of the output.\n2. For ``PermutationGroup_subgroup.__cmp__(self,other)``:\n   a) Compare self and other as PermutationGroup_generic. If they are not equal, return the result.\n   b) Otherwise, return the comparison of the ambient group of self with the ambient group of other (or with other, itself, if it is not given as a subgroup).\n\nI had to modify the doc-test example of ``PermutationGroup_generic.__cmp__``. And then, we have:\n\n```\nsage: G=SymmetricGroup(6)\nsage: G1=G.subgroup([G((1,2,3,4,5)),G((1,2))])\nsage: G2=G.subgroup([G((1,2,3,4)),G((1,2))])\nsage: K=G2.subgroup([G2((1,2,3))])\nsage: H=G1.subgroup([G1(())])\nsage: H<K\nTrue\nsage: K<H\nFalse\nsage: H2=G2.subgroup([G2(())])\nsage: H<H2\nTrue     # because the ambient group of H is a subgroup of the ambient group of H2\n\nsage: G = PermutationGroup([[(1,2)]])\nsage: H = PermutationGroup([[()]])\nsage: G<H\nFalse\n\nsage: G = SymmetricGroup(4)\nsage: H = G.subgroup([G((1,2,3))])\nsage: K = G.subgroup([G((2,3,1))])\nsage: H==K\nTrue\n\n# Here comes an oddity\nsage: G = SymmetricGroup(4)\nsage: H = G.subgroup([G((1,2,3)),G((1,2))])\nsage: K = SymmetricGroup(3)\nsage: K < H\nFalse  # this is comparison as PermutationGroup_generic\nsage: K == H\nTrue\nsage: H < K\nFalse \nsage: H == K\nFalse\n```\n\nThe last example is comparison as PermutationGroup_subgroup, and comes from the fact that the ambient group of K (which is assumed to be K itself) is strictly smaller than the ambient group of H.\n\nDoes this way of comparison makes kind of sense?",
    "created_at": "2009-04-02T13:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44299",
    "user": "@simon-king-jena"
}
```

I have a suggestion for a fix.

1. For comparing PermutationGroup_generic, rely on gap, without reversion of the output.
2. For ``PermutationGroup_subgroup.__cmp__(self,other)``:
   a) Compare self and other as PermutationGroup_generic. If they are not equal, return the result.
   b) Otherwise, return the comparison of the ambient group of self with the ambient group of other (or with other, itself, if it is not given as a subgroup).

I had to modify the doc-test example of ``PermutationGroup_generic.__cmp__``. And then, we have:

```
sage: G=SymmetricGroup(6)
sage: G1=G.subgroup([G((1,2,3,4,5)),G((1,2))])
sage: G2=G.subgroup([G((1,2,3,4)),G((1,2))])
sage: K=G2.subgroup([G2((1,2,3))])
sage: H=G1.subgroup([G1(())])
sage: H<K
True
sage: K<H
False
sage: H2=G2.subgroup([G2(())])
sage: H<H2
True     # because the ambient group of H is a subgroup of the ambient group of H2

sage: G = PermutationGroup([[(1,2)]])
sage: H = PermutationGroup([[()]])
sage: G<H
False

sage: G = SymmetricGroup(4)
sage: H = G.subgroup([G((1,2,3))])
sage: K = G.subgroup([G((2,3,1))])
sage: H==K
True

# Here comes an oddity
sage: G = SymmetricGroup(4)
sage: H = G.subgroup([G((1,2,3)),G((1,2))])
sage: K = SymmetricGroup(3)
sage: K < H
False  # this is comparison as PermutationGroup_generic
sage: K == H
True
sage: H < K
False 
sage: H == K
False
```

The last example is comparison as PermutationGroup_subgroup, and comes from the fact that the ambient group of K (which is assumed to be K itself) is strictly smaller than the ambient group of H.

Does this way of comparison makes kind of sense?



---

archive/issue_comments_044300.json:
```json
{
    "body": "> Does this way of comparison makes kind of sense?\n\nNot in my opinion. If H, K are permutation groups, then\nH == K should return True iff H=k (as sets)\nH<K should return True iff H is a subset of K.\n\nDoes your patch do this?",
    "created_at": "2009-04-02T13:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44300",
    "user": "@wdjoyner"
}
```

> Does this way of comparison makes kind of sense?

Not in my opinion. If H, K are permutation groups, then
H == K should return True iff H=k (as sets)
H<K should return True iff H is a subset of K.

Does your patch do this?



---

archive/issue_comments_044301.json:
```json
{
    "body": "Replying to [comment:9 wdj]:\n> > Does this way of comparison makes kind of sense?\n> \n> Not in my opinion. If H, K are permutation groups, then\n> H == K should return True iff H=k (as sets)\n> H<K should return True iff H is a subset of K.\n> \n> Does your patch do this?\n\nApparently not.\n\nMy way of thinking was like this: The present implementation took into account that we do not talk about permutation groups but about *subgroups* of permutation groups. With this in mind, it is natural to have K==H if and only if K is the same permutation group as H, and *in addition* the ambient groups coincide.\n\nOne question on gap: Assume that K is a *proper* subgroup of H; would `K._gap_()<H._gap_()` return True?\n\nIf the answer to the preceding question is 'Yes' then my patch provides the following:\n* If K is a *proper* subgroup of H, then K<H.\n* If K and H coincide as permutation groups and the ambient group of K is a proper subgroup of the ambient group of H, then K<H\n* K==H only if K coincides with H (as permutation groups) and *in addition* the ambient groups coincide.\n\nBut of course it is also a very natural thing (and probably what algebraists would expect from K<H) to just test whether one group is subgroup of the other. If this is what `K._gap_()<H._gap_()` does, then it is easy to implement (tomorrow, when I'll have better internet access; now is about the 5th attempt to submit my comment...).",
    "created_at": "2009-04-02T21:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44301",
    "user": "@simon-king-jena"
}
```

Replying to [comment:9 wdj]:
> > Does this way of comparison makes kind of sense?
> 
> Not in my opinion. If H, K are permutation groups, then
> H == K should return True iff H=k (as sets)
> H<K should return True iff H is a subset of K.
> 
> Does your patch do this?

Apparently not.

My way of thinking was like this: The present implementation took into account that we do not talk about permutation groups but about *subgroups* of permutation groups. With this in mind, it is natural to have K==H if and only if K is the same permutation group as H, and *in addition* the ambient groups coincide.

One question on gap: Assume that K is a *proper* subgroup of H; would `K._gap_()<H._gap_()` return True?

If the answer to the preceding question is 'Yes' then my patch provides the following:
* If K is a *proper* subgroup of H, then K<H.
* If K and H coincide as permutation groups and the ambient group of K is a proper subgroup of the ambient group of H, then K<H
* K==H only if K coincides with H (as permutation groups) and *in addition* the ambient groups coincide.

But of course it is also a very natural thing (and probably what algebraists would expect from K<H) to just test whether one group is subgroup of the other. If this is what `K._gap_()<H._gap_()` does, then it is easy to implement (tomorrow, when I'll have better internet access; now is about the 5th attempt to submit my comment...).



---

archive/issue_comments_044302.json:
```json
{
    "body": "Almost a positive review.\n\nSeems to apply fine to 3.4 and test okay.\n\nThe problem is with the docstrings. The docstring for __cmp__\nin the subgroup class defines H but never uses it. Plase\n\n(a) improve the docstring for __cmp__\nin the subgroup class to include instances of the behavious discussed above\n\n(b) please add your name to the AUTHOR list at the top\n\nA positive review after that.",
    "created_at": "2009-04-04T17:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44302",
    "user": "@wdjoyner"
}
```

Almost a positive review.

Seems to apply fine to 3.4 and test okay.

The problem is with the docstrings. The docstring for __cmp__
in the subgroup class defines H but never uses it. Plase

(a) improve the docstring for __cmp__
in the subgroup class to include instances of the behavious discussed above

(b) please add your name to the AUTHOR list at the top

A positive review after that.



---

archive/issue_comments_044303.json:
```json
{
    "body": "The new version of the patch should apply to sage-3.4.1.rc3 -- it is formed by two change sets, I hope it works...\n\nI added myself to the list of authors, and I added more doc tests (similar to the things discussed above).\n\nCheers,\n    Simon",
    "created_at": "2009-04-18T14:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44303",
    "user": "@simon-king-jena"
}
```

The new version of the patch should apply to sage-3.4.1.rc3 -- it is formed by two change sets, I hope it works...

I added myself to the list of authors, and I added more doc tests (similar to the things discussed above).

Cheers,
    Simon



---

archive/issue_comments_044304.json:
```json
{
    "body": "How is this behaviour (after your patch is attached) explained?\n\n\n```\nsage: G1 = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])\nsage: G2 = PermutationGroup([[(1,2,3),(4,5)]])\nsage: G1 > G2\nFalse\nsage: G = SymmetricGroup(5)\nsage: G1 = G.subgroup([G([(1,2,3),(4,5)]),G((3,4))])\nsage: G2 = G.subgroup([G([(1,2,3),(4,5)])])\nsage: G1 > G2\nFalse\n```\n\n\n\nThe outout is True for both without your patch.",
    "created_at": "2009-04-19T00:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44304",
    "user": "@wdjoyner"
}
```

How is this behaviour (after your patch is attached) explained?


```
sage: G1 = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
sage: G2 = PermutationGroup([[(1,2,3),(4,5)]])
sage: G1 > G2
False
sage: G = SymmetricGroup(5)
sage: G1 = G.subgroup([G([(1,2,3),(4,5)]),G((3,4))])
sage: G2 = G.subgroup([G([(1,2,3),(4,5)])])
sage: G1 > G2
False
```



The outout is True for both without your patch.



---

archive/issue_comments_044305.json:
```json
{
    "body": "Replying to [comment:14 wdj]:\n> How is this behaviour (after your patch is attached) explained?\n\nThis is since comparison in gap apparently has nothing to do with the subgroup structure. \n\nWithout my patch, `PermutationGroup.__cmp__(self, right)` returns \n\n```\nright._gap_().__cmp__(self._gap_())\n```\n\nwhich means that the trivial group may be *bigger* than a non-trivial group:\n\n```\n# without my patch\nsage: G = PermutationGroup([[(1,2)]])\nsage: H = PermutationGroup([[()]])\nsage: G<H\nTrue\n```\n\n\nThis example is the reason why I suggested to let `PermutationGroup.__cmp__(self, right)` return\n\n```\nself._gap_().__cmp__(right._gap_())\n```\n\n\nBut then, your example gives a strange result. I think gap is to blame for this.\n\nSo, our choice is: \n* Either we want that the trivial group is *greater* than the cyclic group of order two; nasty!!\n* or `PermutationGroup([[(1,2,3),(4,5)],[(3,4)]]) < PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2,3),)](https://trac.sagemath.org/wiki/WikiMacros#-macro))`; nasty as well!\n* or `G.__cmp__(H)` for PermutationGroups should do the following:\n  1. Test if G is a subgroup of H; if yes, return -1\n  2. Test if H is a subgroup of G; if yes, return +1\n  3. Now, G and H are mutually not subgroups. Then, return whatever gap provides.\n\nThe last option seems best to me, from a mathematical point of view. However, the subgroup test might be long. \n\nWhat do you think?",
    "created_at": "2009-04-20T11:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44305",
    "user": "@simon-king-jena"
}
```

Replying to [comment:14 wdj]:
> How is this behaviour (after your patch is attached) explained?

This is since comparison in gap apparently has nothing to do with the subgroup structure. 

Without my patch, `PermutationGroup.__cmp__(self, right)` returns 

```
right._gap_().__cmp__(self._gap_())
```

which means that the trivial group may be *bigger* than a non-trivial group:

```
# without my patch
sage: G = PermutationGroup([[(1,2)]])
sage: H = PermutationGroup([[()]])
sage: G<H
True
```


This example is the reason why I suggested to let `PermutationGroup.__cmp__(self, right)` return

```
self._gap_().__cmp__(right._gap_())
```


But then, your example gives a strange result. I think gap is to blame for this.

So, our choice is: 
* Either we want that the trivial group is *greater* than the cyclic group of order two; nasty!!
* or `PermutationGroup([[(1,2,3),(4,5)],[(3,4)]]) < PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2,3),)](https://trac.sagemath.org/wiki/WikiMacros#-macro))`; nasty as well!
* or `G.__cmp__(H)` for PermutationGroups should do the following:
  1. Test if G is a subgroup of H; if yes, return -1
  2. Test if H is a subgroup of G; if yes, return +1
  3. Now, G and H are mutually not subgroups. Then, return whatever gap provides.

The last option seems best to me, from a mathematical point of view. However, the subgroup test might be long. 

What do you think?



---

archive/issue_comments_044306.json:
```json
{
    "body": "Is the previous behaviour (without the patch) only wrong in the special case of the\ntrivial group? If so, can't that case just be treated separately using an if/then\nstatement?\n\n\n```\nsage: G = PermutationGroup([[(1,2)]])\nsage: H = PermutationGroup([[(1,2)],[(2,3)]])\nsage: G<H1             # correct \nTrue\nsage: H2 = PermutationGroup([[(1,3)]])\nsage: G<H2             # correct \nFalse\nsage: H2 = PermutationGroup([[(1)]])\nsage: G<H2             # incorrect \nTrue\n```\n",
    "created_at": "2009-04-20T12:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44306",
    "user": "@wdjoyner"
}
```

Is the previous behaviour (without the patch) only wrong in the special case of the
trivial group? If so, can't that case just be treated separately using an if/then
statement?


```
sage: G = PermutationGroup([[(1,2)]])
sage: H = PermutationGroup([[(1,2)],[(2,3)]])
sage: G<H1             # correct 
True
sage: H2 = PermutationGroup([[(1,3)]])
sage: G<H2             # correct 
False
sage: H2 = PermutationGroup([[(1)]])
sage: G<H2             # incorrect 
True
```




---

archive/issue_comments_044307.json:
```json
{
    "body": "Replying to [comment:16 wdj]:\n> Is the previous behaviour (without the patch) only wrong in the special case of the\n> trivial group? If so, can't that case just be treated separately using an if/then\n> statement?\n\nWell, you know Gap better than I...\n\nWhat does the Gap reference say? I tried to find something, but there was no index entry that sounded relevant (the nearest was \"Comparison of Permutations\", but not \"Comparison of Permutation Groups\").",
    "created_at": "2009-04-20T12:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44307",
    "user": "@simon-king-jena"
}
```

Replying to [comment:16 wdj]:
> Is the previous behaviour (without the patch) only wrong in the special case of the
> trivial group? If so, can't that case just be treated separately using an if/then
> statement?

Well, you know Gap better than I...

What does the Gap reference say? I tried to find something, but there was no index entry that sounded relevant (the nearest was "Comparison of Permutations", but not "Comparison of Permutation Groups").



---

archive/issue_comments_044308.json:
```json
{
    "body": "I searched the Gap reference manual and couldn't find it either.\n(Emailed gap support though and will let you know...)\n\nMaybe we should just use IsSubgroup (I thought < called that method but I guess not):\n\n\n```\nsage: G = PermutationGroup([[(1,2)]])\nsage: gG = gap(G)\nsage: H1 = PermutationGroup([[(1,2)],[(2,3)]])\nsage: gH1 = gap(H1)\nsage: bool(gH1.IsSubgroup(gG))             # correct \nTrue\nsage: H2 = PermutationGroup([[(1,3)]])\nsage: bool(gH2.IsSubgroup(gG))             # correct \nFalse\nsage: H3 = PermutationGroup([[(1)]])\nsage: gH3 = gap(H3)\nsage: bool(gH3.IsSubgroup(gG))             # correct \nFalse\n```\n\n\nThoughts?",
    "created_at": "2009-04-20T13:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44308",
    "user": "@wdjoyner"
}
```

I searched the Gap reference manual and couldn't find it either.
(Emailed gap support though and will let you know...)

Maybe we should just use IsSubgroup (I thought < called that method but I guess not):


```
sage: G = PermutationGroup([[(1,2)]])
sage: gG = gap(G)
sage: H1 = PermutationGroup([[(1,2)],[(2,3)]])
sage: gH1 = gap(H1)
sage: bool(gH1.IsSubgroup(gG))             # correct 
True
sage: H2 = PermutationGroup([[(1,3)]])
sage: bool(gH2.IsSubgroup(gG))             # correct 
False
sage: H3 = PermutationGroup([[(1)]])
sage: gH3 = gap(H3)
sage: bool(gH3.IsSubgroup(gG))             # correct 
False
```


Thoughts?



---

archive/issue_comments_044309.json:
```json
{
    "body": "Replying to [comment:18 wdj]:\n> I searched the Gap reference manual and couldn't find it either.\n> (Emailed gap support though and will let you know...)\n\nSince, according to the email support, the comparison is by some lexicographic order of the list of elements, it is perhaps no surprise that the \"<\"-relation of Gap does not behave well with respect to subgroups.\n\n> Maybe we should just use IsSubgroup (I thought < called that method but I guess not):\n\nAs much as I understand the sorting of Gap, we would have \n G is proper subgroup of H <=> |G|<|H| and (G<H in Gap's '<'-order)\n\nSo, rather than calling IsSubgroup, we might consider to use Order(G); I guess this is cached and thus faster.\n\nWould this work (and is the cacheing-thing true)?\n\nCheers,\n    Simon",
    "created_at": "2009-04-20T19:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44309",
    "user": "@simon-king-jena"
}
```

Replying to [comment:18 wdj]:
> I searched the Gap reference manual and couldn't find it either.
> (Emailed gap support though and will let you know...)

Since, according to the email support, the comparison is by some lexicographic order of the list of elements, it is perhaps no surprise that the "<"-relation of Gap does not behave well with respect to subgroups.

> Maybe we should just use IsSubgroup (I thought < called that method but I guess not):

As much as I understand the sorting of Gap, we would have 
 G is proper subgroup of H <=> |G|<|H| and (G<H in Gap's '<'-order)

So, rather than calling IsSubgroup, we might consider to use Order(G); I guess this is cached and thus faster.

Would this work (and is the cacheing-thing true)?

Cheers,
    Simon



---

archive/issue_comments_044310.json:
```json
{
    "body": "Sorry, I was writing too quickly (have to leave office very soon...):\n\nReplying to [comment:19 SimonKing]:\n> Since, according to the email support, the comparison is by some lexicographic order of the list of elements, it is perhaps no surprise that the \"<\"-relation of Gap does not behave well with respect to subgroups.\n> \n...\n> As much as I understand the sorting of Gap, we would have \n>  G is proper subgroup of H <=> |G|<|H| and (G<H in Gap's '<'-order)\n\nOf course it is not!\n\nSo, I agree that IsSubgroup is the way to go.",
    "created_at": "2009-04-20T19:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44310",
    "user": "@simon-king-jena"
}
```

Sorry, I was writing too quickly (have to leave office very soon...):

Replying to [comment:19 SimonKing]:
> Since, according to the email support, the comparison is by some lexicographic order of the list of elements, it is perhaps no surprise that the "<"-relation of Gap does not behave well with respect to subgroups.
> 
...
> As much as I understand the sorting of Gap, we would have 
>  G is proper subgroup of H <=> |G|<|H| and (G<H in Gap's '<'-order)

Of course it is not!

So, I agree that IsSubgroup is the way to go.



---

archive/issue_comments_044311.json:
```json
{
    "body": "Attachment [PermutationGroup__cmp__.patch](tarball://root/attachments/some-uuid/ticket5664/PermutationGroup__cmp__.patch) by @simon-king-jena created at 2009-04-21 07:44:14\n\nBug fixes and doc tests for `PermutationGroup_generic.__cmp__` and `PermutationGroup_subgroup.__cmp__`",
    "created_at": "2009-04-21T07:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44311",
    "user": "@simon-king-jena"
}
```

Attachment [PermutationGroup__cmp__.patch](tarball://root/attachments/some-uuid/ticket5664/PermutationGroup__cmp__.patch) by @simon-king-jena created at 2009-04-21 07:44:14

Bug fixes and doc tests for `PermutationGroup_generic.__cmp__` and `PermutationGroup_subgroup.__cmp__`



---

archive/issue_comments_044312.json:
```json
{
    "body": "The new patch (relative to sage-3.4.1.rc3) now relies on gap's `IsSubgroup`.\n\nHence, the examples discussed above now work as expected, `__cmp___` extends the subgroup lattice:\n* If G is subgroup of H then G<H\n* If neither G is subgroup of H nor H is subgroup of G, then, in order to give any answer at all, return whatever gap suggests.\n\nHowever, there is a price to pay. The result is not an ordering!\n\n```\nsage: H1 = PermutationGroup([[(1,2)],[(5,6)]])\nsage: H2 = PermutationGroup([[(3,4)]])\nsage: H3 = PermutationGroup([[(1,2)]])\n# H1,H2 are mutually not subgroups, and H2,H3 are mutually not subgroups\nsage: H1 < H2 # according to Gap's ordering\nTrue\nsage: H2 < H3 # according to Gap's ordering\nTrue\nsage: H3 < H1 # since H3 is a subgroup of H1\nTrue\n```\n\n\nSo, really our choices are:\n1. Return gap's ordering -- which has nothing to do with subgroups. Nasty\n2. Do as suggested in my new patch -- then we don't have transitivity. Nasty\n3. Invest an enormous amount of work into finding a total ordering on permutation groups that extends the subgroup lattice.\n\nSince I doubt that 3. is mathematically possible (and even if it is, it would probably be unfeasible), I think we should chose 2.\n\nWhat do you think?\n\nSidenote:\nWorking on this patch, I found that the method `is_subgroup()` does not rely on gap's `IsSubgroup`. Instead, it tests if any element of the first group is element of the second group. \nAnd the element containment test (G.has_element(g)) also does not directly rely on Gap. Instead, the list of all elements of G is created (but not cached), and it is tested whether g is on this list.\n\nIt seems to me that `IsSubgroup` is much faster than {{{is_subgroup}}, hence I suggest that the latter should be rewritten. But this will be a different ticket.",
    "created_at": "2009-04-21T08:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44312",
    "user": "@simon-king-jena"
}
```

The new patch (relative to sage-3.4.1.rc3) now relies on gap's `IsSubgroup`.

Hence, the examples discussed above now work as expected, `__cmp___` extends the subgroup lattice:
* If G is subgroup of H then G<H
* If neither G is subgroup of H nor H is subgroup of G, then, in order to give any answer at all, return whatever gap suggests.

However, there is a price to pay. The result is not an ordering!

```
sage: H1 = PermutationGroup([[(1,2)],[(5,6)]])
sage: H2 = PermutationGroup([[(3,4)]])
sage: H3 = PermutationGroup([[(1,2)]])
# H1,H2 are mutually not subgroups, and H2,H3 are mutually not subgroups
sage: H1 < H2 # according to Gap's ordering
True
sage: H2 < H3 # according to Gap's ordering
True
sage: H3 < H1 # since H3 is a subgroup of H1
True
```


So, really our choices are:
1. Return gap's ordering -- which has nothing to do with subgroups. Nasty
2. Do as suggested in my new patch -- then we don't have transitivity. Nasty
3. Invest an enormous amount of work into finding a total ordering on permutation groups that extends the subgroup lattice.

Since I doubt that 3. is mathematically possible (and even if it is, it would probably be unfeasible), I think we should chose 2.

What do you think?

Sidenote:
Working on this patch, I found that the method `is_subgroup()` does not rely on gap's `IsSubgroup`. Instead, it tests if any element of the first group is element of the second group. 
And the element containment test (G.has_element(g)) also does not directly rely on Gap. Instead, the list of all elements of G is created (but not cached), and it is tested whether g is on this list.

It seems to me that `IsSubgroup` is much faster than {{{is_subgroup}}, hence I suggest that the latter should be rewritten. But this will be a different ticket.



---

archive/issue_comments_044313.json:
```json
{
    "body": "Replying to [comment:21 SimonKing]:\n> The new patch (relative to sage-3.4.1.rc3) now relies on gap's `IsSubgroup`.\n...\n> It seems to me that `IsSubgroup` is much faster than {{{is_subgroup}}, hence I suggest that the latter should be rewritten. But this will be a different ticket.\n\nDone, the ticket is #5844 -- [with patch, needs review], hint hint...\n\nTo my surprise, after applying #5844, `is_subgroup` seems *faster* then `IsSubgroup`. Hence, as soon as #5844 is merged, I suggest to change `IsSubgroup` into `is_subgroup` and avoid the call to Gap.\n\nI do not change the tag into [with patch, needs work], since the present patch fixes a bug and does *not* depend on #5844. The change after inclusion of #5844 is only about performance, and should probably be on a different ticket.",
    "created_at": "2009-04-21T09:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44313",
    "user": "@simon-king-jena"
}
```

Replying to [comment:21 SimonKing]:
> The new patch (relative to sage-3.4.1.rc3) now relies on gap's `IsSubgroup`.
...
> It seems to me that `IsSubgroup` is much faster than {{{is_subgroup}}, hence I suggest that the latter should be rewritten. But this will be a different ticket.

Done, the ticket is #5844 -- [with patch, needs review], hint hint...

To my surprise, after applying #5844, `is_subgroup` seems *faster* then `IsSubgroup`. Hence, as soon as #5844 is merged, I suggest to change `IsSubgroup` into `is_subgroup` and avoid the call to Gap.

I do not change the tag into [with patch, needs work], since the present patch fixes a bug and does *not* depend on #5844. The change after inclusion of #5844 is only about performance, and should probably be on a different ticket.



---

archive/issue_comments_044314.json:
```json
{
    "body": "Thanks. I'll look at both these, #5844 and #5664. Unfortunately I have a lot of grading to do first but hopefully will get to them today.",
    "created_at": "2009-04-21T10:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44314",
    "user": "@wdjoyner"
}
```

Thanks. I'll look at both these, #5844 and #5664. Unfortunately I have a lot of grading to do first but hopefully will get to them today.



---

archive/issue_comments_044315.json:
```json
{
    "body": "Applies in 3.4.1.rc3 on top of the patch from #5844. \nPasses tests (there were however a lot of unrelated failures)\nand does what it claims to do. Thanks for working \non this Simon!\n\nI will also run tests on this patch using 3.4.2.a0 and report back.",
    "created_at": "2009-04-25T12:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44315",
    "user": "@wdjoyner"
}
```

Applies in 3.4.1.rc3 on top of the patch from #5844. 
Passes tests (there were however a lot of unrelated failures)
and does what it claims to do. Thanks for working 
on this Simon!

I will also run tests on this patch using 3.4.2.a0 and report back.



---

archive/issue_comments_044316.json:
```json
{
    "body": "Applies to 3.4.2.a0 on a ubuntu amd64 8.10 machine and passes all tests.",
    "created_at": "2009-04-25T17:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44316",
    "user": "@wdjoyner"
}
```

Applies to 3.4.2.a0 on a ubuntu amd64 8.10 machine and passes all tests.



---

archive/issue_comments_044317.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-13T19:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44317",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_044318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-13T19:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5664",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5664#issuecomment-44318",
    "user": "mabshoff"
}
```

Resolution: fixed
