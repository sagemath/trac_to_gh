# Issue 8198: p-adic precision in vector multiplication

archive/issues_008198.json:
```json
{
    "body": "Assignee: @roed314\n\nCC:  @nilesjohnson jpflori\n\nKeywords: padics vector\n\nTrying to resolve #4656, I found the following unpleasant bug.\n\nthis looks good :\n\n```\nsage: R = Qp(5,5)\nsage: x = R(5).add_bigoh(1)\nsage: x\nO(5)\nsage: x*R(1)\nO(5)\n```\n\n\nBut when multiplied with the identity matrix the precision is lost\n\n```\nsage: I = matrix(R, [[1,0],[0,1]])\nsage: v = vector([R(1),x])\nsage: v\n(1 + O(5^5), O(5))\nsage: v*I\n(1 + O(5^5), 0)\nsage: v[0]*I[1,0] + v[1]*I[1,1]\nO(5)\n```\n\n\nThis causes things like\n\n```\nsage: M = matrix(R,[[1,2],[3,4]])\nsage: M*v\n(1 + O(5^5), 3 + O(5^5))\nsage: v[0]*M[0,0] + v[1]*M[0,1]\n1 + O(5)\nsage: v[0]*M[1,0] + v[1]*M[1,1]\n3 + O(5)\n```\n\n\nThis is an even worse example, which could be a different bug\n\n```\nsage: vv = vector(x)\nsage: vv\n(0)\nsage: vv[0]\n0\nsage: x\nO(5)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8198\n\n",
    "created_at": "2010-02-05T22:52:30Z",
    "labels": [
        "component: padics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "p-adic precision in vector multiplication",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8198",
    "user": "https://github.com/categorie"
}
```
Assignee: @roed314

CC:  @nilesjohnson jpflori

Keywords: padics vector

Trying to resolve #4656, I found the following unpleasant bug.

this looks good :

```
sage: R = Qp(5,5)
sage: x = R(5).add_bigoh(1)
sage: x
O(5)
sage: x*R(1)
O(5)
```


But when multiplied with the identity matrix the precision is lost

```
sage: I = matrix(R, [[1,0],[0,1]])
sage: v = vector([R(1),x])
sage: v
(1 + O(5^5), O(5))
sage: v*I
(1 + O(5^5), 0)
sage: v[0]*I[1,0] + v[1]*I[1,1]
O(5)
```


This causes things like

```
sage: M = matrix(R,[[1,2],[3,4]])
sage: M*v
(1 + O(5^5), 3 + O(5^5))
sage: v[0]*M[0,0] + v[1]*M[0,1]
1 + O(5)
sage: v[0]*M[1,0] + v[1]*M[1,1]
3 + O(5)
```


This is an even worse example, which could be a different bug

```
sage: vv = vector(x)
sage: vv
(0)
sage: vv[0]
0
sage: x
O(5)
```


Issue created by migration from https://trac.sagemath.org/ticket/8198





---

archive/issue_comments_072172.json:
```json
{
    "body": "I must admit that I have not searched through the tracs to see if this is a duplicate. Sorry.\n\nResolving the bug would result in the resolution of #4656, too, I believe.",
    "created_at": "2010-02-05T22:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72172",
    "user": "https://github.com/categorie"
}
```

I must admit that I have not searched through the tracs to see if this is a duplicate. Sorry.

Resolving the bug would result in the resolution of #4656, too, I believe.



---

archive/issue_comments_072173.json:
```json
{
    "body": "I found this bug also, while working on #9457.  After a fair bit of struggling with elliptic curve code, I now think this is a significant part of the problem.\n\nI noticed the following also; I can't tell if it's the same bug or not.\n\n```\nsage: R = QQ.completion(5,5)\nsage: P.<T> = R[]\nsage: Q.<T> = R[[]]\nsage: P(R(0).add_bigoh(-1))\n(O(5^-1))\nsage: Q(R(0).add_bigoh(-1))\n0\nsage: P(R(0).add_bigoh(2))\n(O(5^2))\nsage: Q(R(0).add_bigoh(2))\n0\nsage: Q(R(1).add_bigoh(2))\n1 + O(5^2)\nsage: Q(R(1).add_bigoh(-1))\n0\nsage: Q(R(1/25).add_bigoh(-1))\n5^-2 + O(5^-1)\n```\n",
    "created_at": "2010-08-03T23:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72173",
    "user": "https://github.com/nilesjohnson"
}
```

I found this bug also, while working on #9457.  After a fair bit of struggling with elliptic curve code, I now think this is a significant part of the problem.

I noticed the following also; I can't tell if it's the same bug or not.

```
sage: R = QQ.completion(5,5)
sage: P.<T> = R[]
sage: Q.<T> = R[[]]
sage: P(R(0).add_bigoh(-1))
(O(5^-1))
sage: Q(R(0).add_bigoh(-1))
0
sage: P(R(0).add_bigoh(2))
(O(5^2))
sage: Q(R(0).add_bigoh(2))
0
sage: Q(R(1).add_bigoh(2))
1 + O(5^2)
sage: Q(R(1).add_bigoh(-1))
0
sage: Q(R(1/25).add_bigoh(-1))
5^-2 + O(5^-1)
```




---

archive/issue_comments_072174.json:
```json
{
    "body": "Replying to [comment:2 niles]:\n> I noticed the following also; I can't tell if it's the same bug or not.\n\noh, this seems to be the same as #4656",
    "created_at": "2010-08-03T23:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72174",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:2 niles]:
> I noticed the following also; I can't tell if it's the same bug or not.

oh, this seems to be the same as #4656



---

archive/issue_comments_072175.json:
```json
{
    "body": "I narrowed down the last issue above. (vector calls Sequence which calls list):\n\n\n```\nsage: R = Qp(5,5)\nsage: x = R(5).add_bigoh(1)\nsage: list(x)\n[0]\n```\n\n\nagain the element is set to zero. The problem here is different than the original case. In fact list(x) should raise an error, just like list(0) does. \n\n\n```\nsage: list([x,x]) \n[O(5), O(5)]\n```\n\n\nworks correctly. So this is really about matrix multiplication.",
    "created_at": "2011-01-27T11:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72175",
    "user": "https://github.com/categorie"
}
```

I narrowed down the last issue above. (vector calls Sequence which calls list):


```
sage: R = Qp(5,5)
sage: x = R(5).add_bigoh(1)
sage: list(x)
[0]
```


again the element is set to zero. The problem here is different than the original case. In fact list(x) should raise an error, just like list(0) does. 


```
sage: list([x,x]) 
[O(5), O(5)]
```


works correctly. So this is really about matrix multiplication.



---

archive/issue_events_019613.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8198#event-19613"
}
```



---

archive/issue_events_019614.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8198#event-19614"
}
```



---

archive/issue_events_019615.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8198#event-19615"
}
```



---

archive/issue_comments_072176.json:
```json
{
    "body": "Note the very last bug, is not longer a problem in 6.1 as `vv = vector(x)`\nraises the error\n `TypeError: this local element is not iterable`\nand that should be ok.",
    "created_at": "2014-02-02T15:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72176",
    "user": "https://github.com/categorie"
}
```

Note the very last bug, is not longer a problem in 6.1 as `vv = vector(x)`
raises the error
 `TypeError: this local element is not iterable`
and that should be ok.



---

archive/issue_comments_072177.json:
```json
{
    "body": "I don't even understand where vector * matrix multiplication is implemented...",
    "created_at": "2014-02-02T15:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72177",
    "user": "https://github.com/categorie"
}
```

I don't even understand where vector * matrix multiplication is implemented...



---

archive/issue_comments_072178.json:
```json
{
    "body": "Replying to [comment:8 wuthrich]:\n> I don't even understand where vector * matrix multiplication is implemented...\nIn `sage/matrix/matrix0.pyx` (I discovered this when working on #804).  It tries to be too smart for its own good and skips entries of the vector that are equal to 0...  I made a patch and am now testing it.",
    "created_at": "2014-04-11T01:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72178",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:8 wuthrich]:
> I don't even understand where vector * matrix multiplication is implemented...
In `sage/matrix/matrix0.pyx` (I discovered this when working on #804).  It tries to be too smart for its own good and skips entries of the vector that are equal to 0...  I made a patch and am now testing it.



---

archive/issue_comments_072179.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-11T01:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72179",
    "user": "https://github.com/pjbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072180.json:
```json
{
    "body": "Changing component from padics to linear algebra.",
    "created_at": "2014-04-11T01:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72180",
    "user": "https://github.com/pjbruin"
}
```

Changing component from padics to linear algebra.



---

archive/issue_comments_072181.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-04-11T16:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72181",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072182.json:
```json
{
    "body": "Good. All tests pass.\n\nI was not certain about the changes as I am not completely fluent in cython. Having read documentations, I think they make sense. I tested the speed in a few very limited cases and it does not seem to me that the new code is slower or faster (except of course when the field is Qp). \n\nThanks for the help.",
    "created_at": "2014-04-11T16:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72182",
    "user": "https://github.com/categorie"
}
```

Good. All tests pass.

I was not certain about the changes as I am not completely fluent in cython. Having read documentations, I think they make sense. I tested the speed in a few very limited cases and it does not seem to me that the new code is slower or faster (except of course when the field is Qp). 

Thanks for the help.



---

archive/issue_comments_072183.json:
```json
{
    "body": "Thanks; hopefully this goes some way towards being able to fix the related tickets #4656, #5075 and #9457...",
    "created_at": "2014-04-11T17:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72183",
    "user": "https://github.com/pjbruin"
}
```

Thanks; hopefully this goes some way towards being able to fix the related tickets #4656, #5075 and #9457...



---

archive/issue_comments_072184.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-04-13T19:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8198#issuecomment-72184",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_019616.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-04-13T19:33:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8198",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8198#event-19616"
}
```
