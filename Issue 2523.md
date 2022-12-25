# Issue 2523: bug in modular symbols for GammaH subgroup

archive/issues_002523.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: ModularSymbols(GammaH(33,[1,2]),2).cuspidal_subspace()\nTraceback (most recent call last):\n...\nKeyError: 11\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2523\n\n",
    "created_at": "2008-03-15T00:01:36Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "bug in modular symbols for GammaH subgroup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2523",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: ModularSymbols(GammaH(33,[1,2]),2).cuspidal_subspace()
Traceback (most recent call last):
...
KeyError: 11
```


Issue created by migration from https://trac.sagemath.org/ticket/2523





---

archive/issue_comments_017169.json:
```json
{
    "body": "Changing component from number theory to modular forms.",
    "created_at": "2008-04-23T02:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2523#issuecomment-17169",
    "user": "https://github.com/aghitza"
}
```

Changing component from number theory to modular forms.



---

archive/issue_comments_017170.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-04-23T02:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2523#issuecomment-17170",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_017171.json:
```json
{
    "body": "I've done a bit of digging and gotten a bit closer to the source of the problem (which I think is actually in congroup.py):\n\n\n```\nsage: G = GammaH(6, [5])\nsage: M = ModularSymbols(G, 2)\nsage: B = M.boundary_space()\nsage: bas = M.basis(); bas\n((1,0), (3,2), (4,1))\nsage: B(bas[0])\n[Infinity] - [0]\nsage: B(bas[2])\n[0] - [-1/2]\nsage: B(bas[1])\nTraceback (most recent call last):\n...\nKeyError: 3\n```\n",
    "created_at": "2008-04-23T02:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2523#issuecomment-17171",
    "user": "https://github.com/aghitza"
}
```

I've done a bit of digging and gotten a bit closer to the source of the problem (which I think is actually in congroup.py):


```
sage: G = GammaH(6, [5])
sage: M = ModularSymbols(G, 2)
sage: B = M.boundary_space()
sage: bas = M.basis(); bas
((1,0), (3,2), (4,1))
sage: B(bas[0])
[Infinity] - [0]
sage: B(bas[2])
[0] - [-1/2]
sage: B(bas[1])
Traceback (most recent call last):
...
KeyError: 3
```




---

archive/issue_comments_017172.json:
```json
{
    "body": "I'm attaching a fix. The fix also cleans up a few related functions. The problem was in the `_coset_reduction_data` functions -- specifically, one of the functions only generated data up to the square root of the level. However, in use, one needs more data -- at the very least, one needs to generate all data up to where the gcd of the term with N is at most square root of N. In that case, it seems easier to just generate all the data.\n\nAdded some doctests, though I'm not completely satisfied with my doctests: in particular, I couldn't come up with a doctest for `_reduce_cusp` that would have `t == -1`. I'd be happy if someone came up with one and added it. \n\nI just noticed that this patch is actually in the tree where I'd already applied AlexGhitza's patch from #2995. Given that it's already been merged anyway, I'm just not going to worry about it.",
    "created_at": "2008-04-26T11:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2523#issuecomment-17172",
    "user": "https://github.com/craigcitro"
}
```

I'm attaching a fix. The fix also cleans up a few related functions. The problem was in the `_coset_reduction_data` functions -- specifically, one of the functions only generated data up to the square root of the level. However, in use, one needs more data -- at the very least, one needs to generate all data up to where the gcd of the term with N is at most square root of N. In that case, it seems easier to just generate all the data.

Added some doctests, though I'm not completely satisfied with my doctests: in particular, I couldn't come up with a doctest for `_reduce_cusp` that would have `t == -1`. I'd be happy if someone came up with one and added it. 

I just noticed that this patch is actually in the tree where I'd already applied AlexGhitza's patch from #2995. Given that it's already been merged anyway, I'm just not going to worry about it.



---

archive/issue_comments_017173.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-26T11:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2523#issuecomment-17173",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017174.json:
```json
{
    "body": "Attachment [trac-2523.patch](tarball://root/attachments/some-uuid/ticket2523/trac-2523.patch) by @ncalexan created at 2008-04-26 17:20:23\n\nThere are some typos, namely `specfically` in at least two places.\n\nI'm worried about the lack of `t==-1` doctest as well, but this looks good to me anyway.",
    "created_at": "2008-04-26T17:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2523#issuecomment-17174",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac-2523.patch](tarball://root/attachments/some-uuid/ticket2523/trac-2523.patch) by @ncalexan created at 2008-04-26 17:20:23

There are some typos, namely `specfically` in at least two places.

I'm worried about the lack of `t==-1` doctest as well, but this looks good to me anyway.



---

archive/issue_comments_017175.json:
```json
{
    "body": "Two comments:\n\n1. this patch is great; not only does it fix the current issue, but also fixes #2938.  Awesome!\n\n2. regarding t = -1: looking at the code, I notice that t = -1 is returned only if, towards the end, u > N_over_2; but before that u goes through a bunch of reductions modulo d, so u is at most d.  On the other hand, d=gcd(v,N), so the only way this can be bigger than half of N is if it's equal to N, i.e. if v = N.  Having run a lot of random examples, I don't think t is ever -1, but it would be nice to have a theoretical proof of this (maybe William or John know this, or maybe they know how to construct an example with t=-1).\n\nHaving said this, I think we should be grateful for point (1) and merge, and figure out point (2) later.",
    "created_at": "2008-04-26T17:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2523#issuecomment-17175",
    "user": "https://github.com/aghitza"
}
```

Two comments:

1. this patch is great; not only does it fix the current issue, but also fixes #2938.  Awesome!

2. regarding t = -1: looking at the code, I notice that t = -1 is returned only if, towards the end, u > N_over_2; but before that u goes through a bunch of reductions modulo d, so u is at most d.  On the other hand, d=gcd(v,N), so the only way this can be bigger than half of N is if it's equal to N, i.e. if v = N.  Having run a lot of random examples, I don't think t is ever -1, but it would be nice to have a theoretical proof of this (maybe William or John know this, or maybe they know how to construct an example with t=-1).

Having said this, I think we should be grateful for point (1) and merge, and figure out point (2) later.



---

archive/issue_comments_017176.json:
```json
{
    "body": "Attachment [trac-2523-pt2.patch](tarball://root/attachments/some-uuid/ticket2523/trac-2523-pt2.patch) by @craigcitro created at 2008-04-26 18:26:50\n\nAdded a small patch fixing the typos ncalexan pointed out. Also, I'm closing #2938 as fixed.",
    "created_at": "2008-04-26T18:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2523#issuecomment-17176",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2523-pt2.patch](tarball://root/attachments/some-uuid/ticket2523/trac-2523-pt2.patch) by @craigcitro created at 2008-04-26 18:26:50

Added a small patch fixing the typos ncalexan pointed out. Also, I'm closing #2938 as fixed.



---

archive/issue_comments_017177.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-26T21:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2523#issuecomment-17177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017178.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-04-26T21:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2523#issuecomment-17178",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha1
