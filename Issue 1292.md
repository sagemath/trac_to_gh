# Issue 1292: bug in polynomial root finding mod n

archive/issues_001292.json:
```json
{
    "body": "Assignee: somebody\n\nThis was reported by michael to sage-devel on Nov 27, 2007.   It's a genuine\nbug which gives incorrect mathematical results (hence the critical marking). \n\n\n```\nR=IntegerModRing(3^2)\nA=PolynomialRing(R,'y')\ny=A.gen()\nf=10*y^2 - y^3 - 9;\nf.roots(multiplicities=false)\n///\n[1, 0]\n```\n\n\n\n```\nprint [k for k in R if f(k) == 0]\n///\n[0, 1, 3, 6]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1292\n\n",
    "created_at": "2007-11-27T15:18:21Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "bug in polynomial root finding mod n",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1292",
    "user": "was"
}
```
Assignee: somebody

This was reported by michael to sage-devel on Nov 27, 2007.   It's a genuine
bug which gives incorrect mathematical results (hence the critical marking). 


```
R=IntegerModRing(3^2)
A=PolynomialRing(R,'y')
y=A.gen()
f=10*y^2 - y^3 - 9;
f.roots(multiplicities=false)
///
[1, 0]
```



```
print [k for k in R if f(k) == 0]
///
[0, 1, 3, 6]
```



Issue created by migration from https://trac.sagemath.org/ticket/1292





---

archive/issue_comments_008107.json:
```json
{
    "body": "In this case, the roots method tries to factor f and extract roots from the factorization:\n\n```\nsage: factor(f)\n(8) * (y + 8) * y^2\n```\n\nI'm told that we need to check that the coefficient ring forms a unique factorization domain before using this strategy, but I don't know how to check that in Sage.",
    "created_at": "2007-11-27T15:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1292#issuecomment-8107",
    "user": "cwitty"
}
```

In this case, the roots method tries to factor f and extract roots from the factorization:

```
sage: factor(f)
(8) * (y + 8) * y^2
```

I'm told that we need to check that the coefficient ring forms a unique factorization domain before using this strategy, but I don't know how to check that in Sage.



---

archive/issue_comments_008108.json:
```json
{
    "body": "In this particular case, roots() is done by factoring modulo n then extracting\nthe roots from the linear factors.  That algorithm makes no sense directly\nin case of a non-integral domain (unique factorization is irrelevant -- what\nmatters if that a product is 0 then at least 1 factor is). Use {{{R.is_integral_domain()}.\n\n\n\n```\nsage: f.factor()\n(8) * (y + 8) * y^2\n```\n\n\nThere is presumably another algorithm for finding roots that works given\na factorization even over a non-integral domain.  Probably we should\nlist all zero-divisor products a*b = 0, then for each factor `g_i(x)` of the\npolynomial, find all y such `g_1(y) = a, g_2(y) = b`.   Also, worry about the\n8 factor out front!\n\nFor now a quick hack would be to just do a stupid for loop to find all roots\nin the non-integral-domain case -- at least that would be mathematically correct.",
    "created_at": "2007-11-27T16:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1292#issuecomment-8108",
    "user": "was"
}
```

In this particular case, roots() is done by factoring modulo n then extracting
the roots from the linear factors.  That algorithm makes no sense directly
in case of a non-integral domain (unique factorization is irrelevant -- what
matters if that a product is 0 then at least 1 factor is). Use {{{R.is_integral_domain()}.



```
sage: f.factor()
(8) * (y + 8) * y^2
```


There is presumably another algorithm for finding roots that works given
a factorization even over a non-integral domain.  Probably we should
list all zero-divisor products a*b = 0, then for each factor `g_i(x)` of the
polynomial, find all y such `g_1(y) = a, g_2(y) = b`.   Also, worry about the
8 factor out front!

For now a quick hack would be to just do a stupid for loop to find all roots
in the non-integral-domain case -- at least that would be mathematically correct.



---

archive/issue_comments_008109.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2007-11-27T16:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1292#issuecomment-8109",
    "user": "cwitty"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_008110.json:
```json
{
    "body": "For the IntegerModRing case, we could probably do something with http://www.shoup.net/ntl/doc/ZZ_pXFactoring.txt .",
    "created_at": "2007-11-27T20:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1292#issuecomment-8110",
    "user": "mhansen"
}
```

For the IntegerModRing case, we could probably do something with http://www.shoup.net/ntl/doc/ZZ_pXFactoring.txt .



---

archive/issue_comments_008111.json:
```json
{
    "body": "Attachment [1292.patch](tarball://root/attachments/some-uuid/ticket1292/1292.patch) by cwitty created at 2007-11-28 02:09:51\n\nI've attached a patch that only does root finding by factorization if the coefficient ring is an integral domain; so for this problem, it uses enumeration instead, and does find all four roots.  I think that using a non-stupid root-finding algorithm here should be a separate ticket; that's an enhancement request, instead of a critical bug fix.\n\nNOTE THAT THIS PATCH REQUIRES THAT PATCHES FROM #1270 AND #1273 ARE ALREADY APPLIED.  This is just because #1273 happens to touch the same paragraph in the docstring of roots() that I needed to change for this patch, so I had to choose between depending on #1273 or conflicting with #1273.  Since I hope and expect that #1273 will be applied for 2.8.15, I chose to depend on it; if #1273 is rejected, I'll upload a modified patch that doesn't depend on #1273.",
    "created_at": "2007-11-28T02:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1292#issuecomment-8111",
    "user": "cwitty"
}
```

Attachment [1292.patch](tarball://root/attachments/some-uuid/ticket1292/1292.patch) by cwitty created at 2007-11-28 02:09:51

I've attached a patch that only does root finding by factorization if the coefficient ring is an integral domain; so for this problem, it uses enumeration instead, and does find all four roots.  I think that using a non-stupid root-finding algorithm here should be a separate ticket; that's an enhancement request, instead of a critical bug fix.

NOTE THAT THIS PATCH REQUIRES THAT PATCHES FROM #1270 AND #1273 ARE ALREADY APPLIED.  This is just because #1273 happens to touch the same paragraph in the docstring of roots() that I needed to change for this patch, so I had to choose between depending on #1273 or conflicting with #1273.  Since I hope and expect that #1273 will be applied for 2.8.15, I chose to depend on it; if #1273 is rejected, I'll upload a modified patch that doesn't depend on #1273.



---

archive/issue_comments_008112.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2007-12-02T05:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1292#issuecomment-8112",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_008113.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T05:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1292#issuecomment-8113",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008114.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T05:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1292#issuecomment-8114",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha2.
