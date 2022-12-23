# Issue 3915: [with patch, needs review] PolyBoRi interface improvements

archive/issues_003915.json:
```json
{
    "body": "Assignee: malb\n\nCC:  burcin\n\nKeywords: polybori\n\nThe attached patch\n* adds an `interpolation_polynomial` method to `BooleanPolynomialRing`\n* adds `reduce` methods to `BooleanPolynomial` and `BooleanPolynomialIdeal`\n* improves the documentation slightly\n* makes `f in I` work for f a `BooleanPolynomial`\n\nIssue created by migration from https://trac.sagemath.org/ticket/3915\n\n",
    "created_at": "2008-08-20T20:02:48Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] PolyBoRi interface improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3915",
    "user": "malb"
}
```
Assignee: malb

CC:  burcin

Keywords: polybori

The attached patch
* adds an `interpolation_polynomial` method to `BooleanPolynomialRing`
* adds `reduce` methods to `BooleanPolynomial` and `BooleanPolynomialIdeal`
* improves the documentation slightly
* makes `f in I` work for f a `BooleanPolynomial`

Issue created by migration from https://trac.sagemath.org/ticket/3915





---

archive/issue_comments_028000.json:
```json
{
    "body": "oh, it also adds a `_latex_` method to `BooleanPolynomial`",
    "created_at": "2008-08-20T20:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28000",
    "user": "malb"
}
```

oh, it also adds a `_latex_` method to `BooleanPolynomial`



---

archive/issue_comments_028001.json:
```json
{
    "body": "The line:\n\n```\ng.minimalizeAndTailReduce()\n```\n\nis nearly meaningless, as it ignores the result.\nFor having a reduced system set\nthe keyword\nredsb=True\nfor the groebner_basis call.\nFurthermore, your reduce implementation doesn't necessarily yield a unique (reduced) normal form.\nFor PolyBoRi >0.4 set\nstrat.optRedTail=True\nfor PolyBoRi <0.4\napply\np=red_tail(strat,p)\nto a normal form.\nMichael",
    "created_at": "2008-08-27T14:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28001",
    "user": "PolyBoRi"
}
```

The line:

```
g.minimalizeAndTailReduce()
```

is nearly meaningless, as it ignores the result.
For having a reduced system set
the keyword
redsb=True
for the groebner_basis call.
Furthermore, your reduce implementation doesn't necessarily yield a unique (reduced) normal form.
For PolyBoRi >0.4 set
strat.optRedTail=True
for PolyBoRi <0.4
apply
p=red_tail(strat,p)
to a normal form.
Michael



---

archive/issue_comments_028002.json:
```json
{
    "body": "Thanks for the review. The updated patch should address your comments.",
    "created_at": "2008-08-27T16:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28002",
    "user": "malb"
}
```

Thanks for the review. The updated patch should address your comments.



---

archive/issue_comments_028003.json:
```json
{
    "body": "Looks good,\nthere is still some minor thing, I detected.\nBut this is nothing about the patch, as it was buggy before:\n\nIt is possible to pass a deg_bound to\ngroebner_basis\n.\nSo the result is not garantied to be a GB.\nIn this case it looks strange to set\n\n```\nself.__gb = g\n```\n\n\nmaybe you can check this\nvia\n\n```\nif kwds.get(\"deg_bound\",False) is False:\n  self.__gb = g\n```\n\n\nThen I'll give it a positive review.\nMichael",
    "created_at": "2008-08-28T06:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28003",
    "user": "PolyBoRi"
}
```

Looks good,
there is still some minor thing, I detected.
But this is nothing about the patch, as it was buggy before:

It is possible to pass a deg_bound to
groebner_basis
.
So the result is not garantied to be a GB.
In this case it looks strange to set

```
self.__gb = g
```


maybe you can check this
via

```
if kwds.get("deg_bound",False) is False:
  self.__gb = g
```


Then I'll give it a positive review.
Michael



---

archive/issue_comments_028004.json:
```json
{
    "body": "ups: still, comments regarding the patch:\nThese are optional, as they only concern performance:\n\npbori.pyxline 3144\n\n```\n            s = sum([prod([x[i] for i in xrange(n) if v[i]],  \n\t            B.one_element()) for v in s],  \n                    B.zero_element()) \n            s = s.set()\n```\n\nshould be faster with\n\n```\n            s=BooleSet(sum([prod([x[i] for i in xrange(n) if v[i]],  \n\t            B.one_element()) for v in s]\n```\n\nHowever, you will have to handle the case of the empty set seperately(when there are no monomials) to make sure, that it is the right ring.\nI think, if we can make this easier upstream.\n\nFurthermore, if you really want to be clever: The use of prod is quite unoptimal here.\nIf you really want get these multiplications for variables fast, you should\nmultiply them in this way:\nx1*(x2*(x3*x4)))\nSo first use the indices behind. Note, that indices in PolyBoRi don't have to be identical to those in sage/Singular\nlex, degree lex: identical\ndp(dp_asc): reversed.\nBlocks of degree lexicographical: identical\nBlocks of degree reverse lex. : reversed in each block, so quite strange\n(if it is correctly implemented in sage)",
    "created_at": "2008-08-28T07:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28004",
    "user": "PolyBoRi"
}
```

ups: still, comments regarding the patch:
These are optional, as they only concern performance:

pbori.pyxline 3144

```
            s = sum([prod([x[i] for i in xrange(n) if v[i]],  
	            B.one_element()) for v in s],  
                    B.zero_element()) 
            s = s.set()
```

should be faster with

```
            s=BooleSet(sum([prod([x[i] for i in xrange(n) if v[i]],  
	            B.one_element()) for v in s]
```

However, you will have to handle the case of the empty set seperately(when there are no monomials) to make sure, that it is the right ring.
I think, if we can make this easier upstream.

Furthermore, if you really want to be clever: The use of prod is quite unoptimal here.
If you really want get these multiplications for variables fast, you should
multiply them in this way:
x1*(x2*(x3*x4)))
So first use the indices behind. Note, that indices in PolyBoRi don't have to be identical to those in sage/Singular
lex, degree lex: identical
dp(dp_asc): reversed.
Blocks of degree lexicographical: identical
Blocks of degree reverse lex. : reversed in each block, so quite strange
(if it is correctly implemented in sage)



---

archive/issue_comments_028005.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-28T10:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28005",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_028006.json:
```json
{
    "body": "Replying to [comment:4 PolyBoRi]:\n> It is possible to pass a deg_bound to groebner_basis.\n\nI check for `deg_bound` in the updated patch. Thanks a lot for your detailed criticism, it helps (me) a lot! I give the patch a positive review now, since you wrote:\n\n> Then I'll give it a positive review. Michael",
    "created_at": "2008-08-28T10:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28006",
    "user": "malb"
}
```

Replying to [comment:4 PolyBoRi]:
> It is possible to pass a deg_bound to groebner_basis.

I check for `deg_bound` in the updated patch. Thanks a lot for your detailed criticism, it helps (me) a lot! I give the patch a positive review now, since you wrote:

> Then I'll give it a positive review. Michael



---

archive/issue_comments_028007.json:
```json
{
    "body": "Replying to [comment:5 PolyBoRi]:\n> ups: still, comments regarding the patch:\n> These are optional, as they only concern performance:\n> \n> pbori.pyxline 3144\n> s=BooleSet(sum([prod([x[i] for i in xrange(n) if v[i]], B.one_element()) for v in s]\n\nIt seems we didn't implement BooleSet(BooleanPolynomial) in Sage. I'll check the upstream implementation and fix that.\n\n> If you really want get these multiplications for variables fast, you should\n> multiply them in this way:\n> x1*(x2*(x3*x4)))\n\nI don't do anything fancy for now, but I reversed the order of the product. This might be faster in the normal case which is lex if I understand your comment correctly.",
    "created_at": "2008-08-28T10:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28007",
    "user": "malb"
}
```

Replying to [comment:5 PolyBoRi]:
> ups: still, comments regarding the patch:
> These are optional, as they only concern performance:
> 
> pbori.pyxline 3144
> s=BooleSet(sum([prod([x[i] for i in xrange(n) if v[i]], B.one_element()) for v in s]

It seems we didn't implement BooleSet(BooleanPolynomial) in Sage. I'll check the upstream implementation and fix that.

> If you really want get these multiplications for variables fast, you should
> multiply them in this way:
> x1*(x2*(x3*x4)))

I don't do anything fancy for now, but I reversed the order of the product. This might be faster in the normal case which is lex if I understand your comment correctly.



---

archive/issue_comments_028008.json:
```json
{
    "body": "> \n> It seems we didn't implement BooleSet(BooleanPolynomial) in Sage. I'll check the upstream implementation and fix that.\n\nsorry, the line was long, without the sum:\njust\n\n```\nBooleSet([prod([x[i] for ...]\n```\n\n\nA BooleSet is a set of monomials.\nIt uses a more sophisticated addition.\n\n> \n> > If you really want get these multiplications for variables fast, you should\n> > multiply them in this way:\n> > x1*(x2*(x3*x4)))\n> \n> I don't do anything fancy for now, but I reversed the order of the product. This might be faster in the normal case which is lex if I understand your comment correctly.\n\nyes, it is much faster in Lex, even from a Python interpreter with boost::python calling overhead (in large examples, high degree monomials)\n\nYou have my positive review :-).",
    "created_at": "2008-08-28T10:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28008",
    "user": "PolyBoRi"
}
```

> 
> It seems we didn't implement BooleSet(BooleanPolynomial) in Sage. I'll check the upstream implementation and fix that.

sorry, the line was long, without the sum:
just

```
BooleSet([prod([x[i] for ...]
```


A BooleSet is a set of monomials.
It uses a more sophisticated addition.

> 
> > If you really want get these multiplications for variables fast, you should
> > multiply them in this way:
> > x1*(x2*(x3*x4)))
> 
> I don't do anything fancy for now, but I reversed the order of the product. This might be faster in the normal case which is lex if I understand your comment correctly.

yes, it is much faster in Lex, even from a Python interpreter with boost::python calling overhead (in large examples, high degree monomials)

You have my positive review :-).



---

archive/issue_comments_028009.json:
```json
{
    "body": "I am seeing slight merge issues with my current alpha2 tree:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/devel/sage$ patch -p1 < trac_3915_pbori_improvements.patch\npatching file sage/rings/polynomial/multi_polynomial_ideal.py\nHunk #1 FAILED at 391.\nHunk #2 succeeded at 1948 (offset 47 lines).\n1 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej\n```\n\nThe failing hunk deletes `contains`, so this should be easy to rebase.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-28T10:59:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28009",
    "user": "mabshoff"
}
```

I am seeing slight merge issues with my current alpha2 tree:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/devel/sage$ patch -p1 < trac_3915_pbori_improvements.patch
patching file sage/rings/polynomial/multi_polynomial_ideal.py
Hunk #1 FAILED at 391.
Hunk #2 succeeded at 1948 (offset 47 lines).
1 out of 2 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej
```

The failing hunk deletes `contains`, so this should be easy to rebase.

Cheers,

Michael



---

archive/issue_comments_028010.json:
```json
{
    "body": "Martin suggested in IRC just to delete the hunk that fails to apply manually. The reject is cause by some other code being applied in alpha2, so I will sort this out by posting an updated patch of Martin's patch and a second patch that deletes the hunk in question.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-28T22:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28010",
    "user": "mabshoff"
}
```

Martin suggested in IRC just to delete the hunk that fails to apply manually. The reject is cause by some other code being applied in alpha2, so I will sort this out by posting an updated patch of Martin's patch and a second patch that deletes the hunk in question.

Cheers,

Michael



---

archive/issue_comments_028011.json:
```json
{
    "body": "rebased patch of malb's - all that needed fixing was plot's parameter list",
    "created_at": "2008-08-29T01:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28011",
    "user": "mabshoff"
}
```

rebased patch of malb's - all that needed fixing was plot's parameter list



---

archive/issue_comments_028012.json:
```json
{
    "body": "Attachment\n\nMerged trac_3915_pbori_improvements.patch in Sage 3.1.2.alpha2",
    "created_at": "2008-08-29T01:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28012",
    "user": "mabshoff"
}
```

Attachment

Merged trac_3915_pbori_improvements.patch in Sage 3.1.2.alpha2



---

archive/issue_comments_028013.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T01:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3915",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3915#issuecomment-28013",
    "user": "mabshoff"
}
```

Resolution: fixed
