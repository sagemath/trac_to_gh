# Issue 1284: G.subgroup([...]) for G an abelian group has at least one lame property

archive/issues_001284.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  fwclarke\n\n\n```\nFrancis Clarke to sage-support\n\nSubgroups of abelian groups:\n\nsage: G.<a, b> = AbelianGroup(2)\nsage: A = G.subgroup([a])\nsage: B = G.subgroup([b])\nsage: A == B\nTrue\n\nSurely not!\n\nOn the other hand for vector spaces:\n\nsage: W.<u, v> = QQ^2\nsage: U = W.subspace([u])\nsage: V = W.subspace([v])\nsage: U == V\nFalse\n\nAs expected.\n```\n\n\nI have verified this and I agree that this is stupid.\nThe problem is that the __cmp__ method is just comparing\nthe groups abstract structure:\n\n\n```\n        if not is_AbelianGroup(right):\n            return -1\n        return cmp(self.invariants(), right.invariants())\n```\n\n\nIt should also take into account the embedding. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1284\n\n",
    "created_at": "2007-11-26T21:04:14Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "G.subgroup([...]) for G an abelian group has at least one lame property",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1284",
    "user": "was"
}
```
Assignee: somebody

CC:  fwclarke


```
Francis Clarke to sage-support

Subgroups of abelian groups:

sage: G.<a, b> = AbelianGroup(2)
sage: A = G.subgroup([a])
sage: B = G.subgroup([b])
sage: A == B
True

Surely not!

On the other hand for vector spaces:

sage: W.<u, v> = QQ^2
sage: U = W.subspace([u])
sage: V = W.subspace([v])
sage: U == V
False

As expected.
```


I have verified this and I agree that this is stupid.
The problem is that the __cmp__ method is just comparing
the groups abstract structure:


```
        if not is_AbelianGroup(right):
            return -1
        return cmp(self.invariants(), right.invariants())
```


It should also take into account the embedding. 

Issue created by migration from https://trac.sagemath.org/ticket/1284





---

archive/issue_comments_008048.json:
```json
{
    "body": "Changing assignee from somebody to rlm.",
    "created_at": "2008-05-10T23:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8048",
    "user": "rlm"
}
```

Changing assignee from somebody to rlm.



---

archive/issue_comments_008049.json:
```json
{
    "body": "This fixes the bugs at #2272 and #3127 as well.\n\n\n```\nrank4:sage-3.0.1 rlmill$ ./sage -t devel/sage/sage/groups/\n...\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 183.2 seconds\n```\n",
    "created_at": "2008-05-10T23:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8049",
    "user": "rlm"
}
```

This fixes the bugs at #2272 and #3127 as well.


```
rank4:sage-3.0.1 rlmill$ ./sage -t devel/sage/sage/groups/
...
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 183.2 seconds
```




---

archive/issue_comments_008050.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-10T23:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8050",
    "user": "rlm"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008051.json:
```json
{
    "body": "Negative review:  if I understand the code for `__contains__` in the first patch correctly, it looks very inefficient.  There must be vastly better ways of handling finite abelian groups than this: the code is the equivalent of testing whether m divides n by repeated subtraction instead of division with remainder.\n\nOf course I may be wrong, and perhaps having an inefficient implementation temporarily is better than the wrong answers reported in the orginal posting.  Does the patch solve that, by the way?  It would be good to have a doctest which proced it but I did not see one.",
    "created_at": "2008-05-11T17:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8051",
    "user": "cremona"
}
```

Negative review:  if I understand the code for `__contains__` in the first patch correctly, it looks very inefficient.  There must be vastly better ways of handling finite abelian groups than this: the code is the equivalent of testing whether m divides n by repeated subtraction instead of division with remainder.

Of course I may be wrong, and perhaps having an inefficient implementation temporarily is better than the wrong answers reported in the orginal posting.  Does the patch solve that, by the way?  It would be good to have a doctest which proced it but I did not see one.



---

archive/issue_comments_008052.json:
```json
{
    "body": "John,\n\nYou're right about the efficiency part. I was just trying to take the code from not working to working. Will post another patch soon.",
    "created_at": "2008-05-11T17:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8052",
    "user": "rlm"
}
```

John,

You're right about the efficiency part. I was just trying to take the code from not working to working. Will post another patch soon.



---

archive/issue_comments_008053.json:
```json
{
    "body": "Hi John, Robert,\n\nI would even go so far and choose a working, but slow/sucky implementation over a future perfect one. Perfection is the enemy of the good. Since this issue has made it into trac three times I would like to have this ticket resolved in 3.0.2. So assuming this work let's merge it as is and open an enhancement ticket for a proper fast implementation. \n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T20:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8053",
    "user": "mabshoff"
}
```

Hi John, Robert,

I would even go so far and choose a working, but slow/sucky implementation over a future perfect one. Perfection is the enemy of the good. Since this issue has made it into trac three times I would like to have this ticket resolved in 3.0.2. So assuming this work let's merge it as is and open an enhancement ticket for a proper fast implementation. 

Thoughts?

Cheers,

Michael



---

archive/issue_comments_008054.json:
```json
{
    "body": "+1",
    "created_at": "2008-05-11T20:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8054",
    "user": "rlm"
}
```

+1



---

archive/issue_comments_008055.json:
```json
{
    "body": "Since Francis reported this bug initially let's get him uptodate on this ticket. I didn't look at the ticket in detail, but we should certainly add a doctest that test this specific bug for obvious reasons :)\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T20:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8055",
    "user": "mabshoff"
}
```

Since Francis reported this bug initially let's get him uptodate on this ticket. I didn't look at the ticket in detail, but we should certainly add a doctest that test this specific bug for obvious reasons :)

Cheers,

Michael



---

archive/issue_comments_008056.json:
```json
{
    "body": "Sorry for the missing doctest, however:\n\n```\nsage: G.<a,b> = AbelianGroup(2)\nsage: A = G.subgroup([a])\nsage: B = G.subgroup([b])\nsage: A == B\nFalse\n```\n",
    "created_at": "2008-05-11T20:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8056",
    "user": "rlm"
}
```

Sorry for the missing doctest, however:

```
sage: G.<a,b> = AbelianGroup(2)
sage: A = G.subgroup([a])
sage: B = G.subgroup([b])
sage: A == B
False
```




---

archive/issue_comments_008057.json:
```json
{
    "body": "Yes, the original problem is solved, but others remain. \n \nWith the two patches installed:\n\n```\nsage: G.<a, b> = AbelianGroup(2)\nsage: H.<c> = AbelianGroup(1)\nsage: H < G\nTrue\n```\n\nwhich is not what I would expect.  There is no reason to assume H is a subgroup of G.\n\nBut anyway `__cmp__` and `__contains__` are inconsistent.  For\n\n```\nsage: c in H\nTrue\nsage: c in G\nFalse\n```\n\n\nMoreover\n\n```\nsage: A = G.subgroup([a])\nsage: A == H\nFalse\nsage: H == A\nTrue\n```\n",
    "created_at": "2008-05-11T21:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8057",
    "user": "fwclarke"
}
```

Yes, the original problem is solved, but others remain. 
 
With the two patches installed:

```
sage: G.<a, b> = AbelianGroup(2)
sage: H.<c> = AbelianGroup(1)
sage: H < G
True
```

which is not what I would expect.  There is no reason to assume H is a subgroup of G.

But anyway `__cmp__` and `__contains__` are inconsistent.  For

```
sage: c in H
True
sage: c in G
False
```


Moreover

```
sage: A = G.subgroup([a])
sage: A == H
False
sage: H == A
True
```




---

archive/issue_comments_008058.json:
```json
{
    "body": "With this latest patch:\n\n```\nsage: G.<a, b> = AbelianGroup(2)\nsage: H.<c> = AbelianGroup(1)\nsage: H < G\nFalse\nsage: c in H\nTrue\nsage: c in G\nFalse\nsage: A = G.subgroup([a])\nsage: A == H\nFalse\nsage: H == A\nFalse\n```\n\n\nI know it's still missing some documentation, I just want to see if there is more work necessary.",
    "created_at": "2008-05-11T23:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8058",
    "user": "rlm"
}
```

With this latest patch:

```
sage: G.<a, b> = AbelianGroup(2)
sage: H.<c> = AbelianGroup(1)
sage: H < G
False
sage: c in H
True
sage: c in G
False
sage: A = G.subgroup([a])
sage: A == H
False
sage: H == A
False
```


I know it's still missing some documentation, I just want to see if there is more work necessary.



---

archive/issue_comments_008059.json:
```json
{
    "body": "I am beginning to think the problem is rather deeper.  There are many inconsistencies in the way that algebraic objects are implemented.  It should be possible for a user to learn the basic syntax for, say, rings, and then adopt most of the basics when working with vector spaces, or abelian groups, etc.\n\nSome examples of inconsistent behaviour follow.\n\n\n```\nsage: R.<r> = PolynomialRing(QQ)\nsage: S.<s> = PolynomialRing(QQ)\nsage: R == S\nFalse\nsage: R.ideal(r^2 - 1) < S\nTrue\n```\n\n\n\n```\nsage: U.<u1, u2> = QQ^2\nsage: V.<v1, v2> = QQ^2\nsage: U == V\nTrue\nsage: W = VectorSpace(QQ, 2)\nsage: U == W\nTrue\nsage: W.<w1, w2> = VectorSpace(QQ, 2)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/mafwc/<ipython console> in <module>()\n\n<type 'exceptions.TypeError'>: VectorSpace() got an unexpected keyword argument 'names'\n```\n\n\nIn my experience of doing calculations (rather than looking at the code) number fields have the best implementation of the algebraic objects which I have encountered .  But even so there are things that could be improved.  For example:\n\n```\nsage: K.subfield((theta^4 + 26*theta)/84)\n\n(Number Field in theta0 with defining polynomial x^3 - 2,\n Ring morphism:\n  From: Number Field in theta0 with defining polynomial x^3 - 2\n  To:   Number Field in theta with defining polynomial x^6 + 40*x^3 + 1372\n  Defn: theta0 |--> 1/84*theta^4 + 13/42*theta)\n```\n\nHere a subfield is generated by a single element.  There is no definition for a subfield generated by a list of elements; `K.subfield([(theta^4 + 26*theta)/84])` leads to a long, unhelpful error message.  In contrast, subgroups of abelian groups and subspaces of vector spaces **must** be generated by a list.  \n\nSurely `X.subobject([x,y,z])` should be standard, with `X.subobject(x)`equivalent to `X.subobject([x])`.  Ideals of rings work well in this respect:\n\n```\nsage: R.<r> = PolynomialRing(QQ)\nsage: R.ideal([r^2, r^3])\nPrincipal ideal (r^2) of Univariate Polynomial Ring in r over Rational Field\nsage: R.ideal(r^2 - 1)\nPrincipal ideal (r^2 - 1) of Univariate Polynomial Ring in r over Rational Field\nsage: R.ideal([r^2 - 1])\nPrincipal ideal (r^2 - 1) of Univariate Polynomial Ring in r over Rational Field\nsage: R.ideal([r^2 - 1, r - 1])\nPrincipal ideal (r - 1) of Univariate Polynomial Ring in r over Rational Field\n```\n\nBut\n\n```\nsage: R.ideal([r^2, r - 1])\nPrincipal ideal (1) of Univariate Polynomial Ring in r over Rational Field\nsage: R == R.ideal([r^2, r - 1])\nFalse\n```\n\nand at the moment there doesn't seem to be any subring construction, while `is_subring` restricts itself to 'natural' inclusions.\n\nOne thing that appears to be missing from most (all?) the algebraic objects is intersection of subobjects.\n\nProbably what is needed to to rethink, and eventually, rewrite all the standard algebraic categories in a consistent and standard way.",
    "created_at": "2008-05-12T08:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8059",
    "user": "fwclarke"
}
```

I am beginning to think the problem is rather deeper.  There are many inconsistencies in the way that algebraic objects are implemented.  It should be possible for a user to learn the basic syntax for, say, rings, and then adopt most of the basics when working with vector spaces, or abelian groups, etc.

Some examples of inconsistent behaviour follow.


```
sage: R.<r> = PolynomialRing(QQ)
sage: S.<s> = PolynomialRing(QQ)
sage: R == S
False
sage: R.ideal(r^2 - 1) < S
True
```



```
sage: U.<u1, u2> = QQ^2
sage: V.<v1, v2> = QQ^2
sage: U == V
True
sage: W = VectorSpace(QQ, 2)
sage: U == W
True
sage: W.<w1, w2> = VectorSpace(QQ, 2)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/mafwc/<ipython console> in <module>()

<type 'exceptions.TypeError'>: VectorSpace() got an unexpected keyword argument 'names'
```


In my experience of doing calculations (rather than looking at the code) number fields have the best implementation of the algebraic objects which I have encountered .  But even so there are things that could be improved.  For example:

```
sage: K.subfield((theta^4 + 26*theta)/84)

(Number Field in theta0 with defining polynomial x^3 - 2,
 Ring morphism:
  From: Number Field in theta0 with defining polynomial x^3 - 2
  To:   Number Field in theta with defining polynomial x^6 + 40*x^3 + 1372
  Defn: theta0 |--> 1/84*theta^4 + 13/42*theta)
```

Here a subfield is generated by a single element.  There is no definition for a subfield generated by a list of elements; `K.subfield([(theta^4 + 26*theta)/84])` leads to a long, unhelpful error message.  In contrast, subgroups of abelian groups and subspaces of vector spaces **must** be generated by a list.  

Surely `X.subobject([x,y,z])` should be standard, with `X.subobject(x)`equivalent to `X.subobject([x])`.  Ideals of rings work well in this respect:

```
sage: R.<r> = PolynomialRing(QQ)
sage: R.ideal([r^2, r^3])
Principal ideal (r^2) of Univariate Polynomial Ring in r over Rational Field
sage: R.ideal(r^2 - 1)
Principal ideal (r^2 - 1) of Univariate Polynomial Ring in r over Rational Field
sage: R.ideal([r^2 - 1])
Principal ideal (r^2 - 1) of Univariate Polynomial Ring in r over Rational Field
sage: R.ideal([r^2 - 1, r - 1])
Principal ideal (r - 1) of Univariate Polynomial Ring in r over Rational Field
```

But

```
sage: R.ideal([r^2, r - 1])
Principal ideal (1) of Univariate Polynomial Ring in r over Rational Field
sage: R == R.ideal([r^2, r - 1])
False
```

and at the moment there doesn't seem to be any subring construction, while `is_subring` restricts itself to 'natural' inclusions.

One thing that appears to be missing from most (all?) the algebraic objects is intersection of subobjects.

Probably what is needed to to rethink, and eventually, rewrite all the standard algebraic categories in a consistent and standard way.



---

archive/issue_comments_008060.json:
```json
{
    "body": "Changing component from basic arithmetic to algebra.",
    "created_at": "2008-05-12T08:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8060",
    "user": "fwclarke"
}
```

Changing component from basic arithmetic to algebra.



---

archive/issue_comments_008061.json:
```json
{
    "body": "I agree strongly with Francis on this.  There are serious issues here which cannot be dealt with by treating the problem as a small bug that can be fixed with a small patch.",
    "created_at": "2008-05-12T09:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8061",
    "user": "cremona"
}
```

I agree strongly with Francis on this.  There are serious issues here which cannot be dealt with by treating the problem as a small bug that can be fixed with a small patch.



---

archive/issue_comments_008062.json:
```json
{
    "body": "Actually, the issue I was treating with these patches was in fact a pretty deep bit of circular logic in the abelian group code. Perhaps we can close this ticket, open another for the division optimization, and move the discussion to sage-devel?",
    "created_at": "2008-05-12T13:54:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8062",
    "user": "rlm"
}
```

Actually, the issue I was treating with these patches was in fact a pretty deep bit of circular logic in the abelian group code. Perhaps we can close this ticket, open another for the division optimization, and move the discussion to sage-devel?



---

archive/issue_comments_008063.json:
```json
{
    "body": "John,\n\nI've addressed your concerns regarding efficiency. I think that the rest of Francis' complaints are not specific to abelian groups, so I say that this ticket is finished. We should move the rest of his complaints to another ticket. My guess is that in many cases people are implementing `__cmp__` for equality/inequality testing only, which gives adverse results for < and <=. The problem is that `__cmp__` assumes that exactly one of <, ==, or > holds, which isn't true unless the ordering is linear-- in particular this isn't the case in general for subobjects.",
    "created_at": "2008-05-12T19:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8063",
    "user": "rlm"
}
```

John,

I've addressed your concerns regarding efficiency. I think that the rest of Francis' complaints are not specific to abelian groups, so I say that this ticket is finished. We should move the rest of his complaints to another ticket. My guess is that in many cases people are implementing `__cmp__` for equality/inequality testing only, which gives adverse results for < and <=. The problem is that `__cmp__` assumes that exactly one of <, ==, or > holds, which isn't true unless the ordering is linear-- in particular this isn't the case in general for subobjects.



---

archive/issue_comments_008064.json:
```json
{
    "body": "OK.  But I haven't time right now to do any testing, so I haven't looked at patches 3 and 4 and haven't tested any of it so you'll need to find someone who has.",
    "created_at": "2008-05-12T19:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8064",
    "user": "cremona"
}
```

OK.  But I haven't time right now to do any testing, so I haven't looked at patches 3 and 4 and haven't tested any of it so you'll need to find someone who has.



---

archive/issue_comments_008065.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-14T20:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8065",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_008066.json:
```json
{
    "body": "See the thread:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/9e13b5c63e485f8f",
    "created_at": "2008-05-23T16:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8066",
    "user": "rlm"
}
```

See the thread:

http://groups.google.com/group/sage-devel/browse_thread/thread/9e13b5c63e485f8f



---

archive/issue_comments_008067.json:
```json
{
    "body": "On the above thread, it is nearly unanimous that `G<=H` should mean \"Is G a subgroup of H?\". Therefore, I propose we merge the patch as-is, and create a ticket to provide `is_subgroup` functionality.",
    "created_at": "2008-05-25T19:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8067",
    "user": "rlm"
}
```

On the above thread, it is nearly unanimous that `G<=H` should mean "Is G a subgroup of H?". Therefore, I propose we merge the patch as-is, and create a ticket to provide `is_subgroup` functionality.



---

archive/issue_comments_008068.json:
```json
{
    "body": "I agree with rlm. Could someone review trac1284-flattened.patch? Then we can take it from there with a new ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-25T19:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8068",
    "user": "mabshoff"
}
```

I agree with rlm. Could someone review trac1284-flattened.patch? Then we can take it from there with a new ticket.

Cheers,

Michael



---

archive/issue_comments_008069.json:
```json
{
    "body": "Sorry about this, but:  we all agreed that H<=G should mean \"H is a subgroup of G\" and have nothing to do with order-comparison.  But you still have H<G meaning such an order-comparison!  As a user I would expect H<G to mean \"H is a proper subgroup of G\" so that (H<=G) == ((H<G) or (H==G)) and (H<G) == ((H<=G) and not (H==G)).\n\nSo I would be happier if < and > were defined this way!",
    "created_at": "2008-05-25T20:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8069",
    "user": "cremona"
}
```

Sorry about this, but:  we all agreed that H<=G should mean "H is a subgroup of G" and have nothing to do with order-comparison.  But you still have H<G meaning such an order-comparison!  As a user I would expect H<G to mean "H is a proper subgroup of G" so that (H<=G) == ((H<G) or (H==G)) and (H<G) == ((H<=G) and not (H==G)).

So I would be happier if < and > were defined this way!



---

archive/issue_comments_008070.json:
```json
{
    "body": "Replying to [comment:20 cremona]:\n> Sorry about this, but:  we all agreed that H<=G should mean \"H is a subgroup of G\" and have nothing to do with order-comparison.  But you still have H<G meaning such an order-comparison!  As a user I would expect H<G to mean \"H is a proper subgroup of G\" so that (H<=G) == ((H<G) or (H==G)) and (H<G) == ((H<=G) and not (H==G)).\n> \n> So I would be happier if < and > were defined this way!\n\nLook more carefully: this is exactly what they *are* defined to do.",
    "created_at": "2008-05-25T20:38:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8070",
    "user": "rlm"
}
```

Replying to [comment:20 cremona]:
> Sorry about this, but:  we all agreed that H<=G should mean "H is a subgroup of G" and have nothing to do with order-comparison.  But you still have H<G meaning such an order-comparison!  As a user I would expect H<G to mean "H is a proper subgroup of G" so that (H<=G) == ((H<G) or (H==G)) and (H<G) == ((H<=G) and not (H==G)).
> 
> So I would be happier if < and > were defined this way!

Look more carefully: this is exactly what they *are* defined to do.



---

archive/issue_comments_008071.json:
```json
{
    "body": "Apologies -- you are right of course.  It's a bit late in the evening where I live.\nI'll test applying the patch to 3.0.2 on Monday, but the code does appear to do what we agree it should.",
    "created_at": "2008-05-25T21:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8071",
    "user": "cremona"
}
```

Apologies -- you are right of course.  It's a bit late in the evening where I live.
I'll test applying the patch to 3.0.2 on Monday, but the code does appear to do what we agree it should.



---

archive/issue_comments_008072.json:
```json
{
    "body": "The immediate problem with abelian groups has been solved, and all the group-related problems posted with this patch are dealt with by this patch, which I think can go ahead.\n\nThe wider problems raised by Frances are not touched by this and should somehow be preserved in a new patch.  I also believe that the whole f.g. abelian groups implementation would benefit from a rewrite using ultra-efficient matrix operations (HNF and SNF) to do everything;  but that would be a serious undertaking, and talk is cheap...",
    "created_at": "2008-05-26T10:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8072",
    "user": "cremona"
}
```

The immediate problem with abelian groups has been solved, and all the group-related problems posted with this patch are dealt with by this patch, which I think can go ahead.

The wider problems raised by Frances are not touched by this and should somehow be preserved in a new patch.  I also believe that the whole f.g. abelian groups implementation would benefit from a rewrite using ultra-efficient matrix operations (HNF and SNF) to do everything;  but that would be a serious undertaking, and talk is cheap...



---

archive/issue_comments_008073.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-26T16:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8073",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008074.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0. Somebody please open up a follow up ticket with the issues Frances described. \n\nCheers,\n\nMichael",
    "created_at": "2008-05-26T16:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1284#issuecomment-8074",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha0. Somebody please open up a follow up ticket with the issues Frances described. 

Cheers,

Michael
