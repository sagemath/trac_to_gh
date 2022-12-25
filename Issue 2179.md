# Issue 2179: [with patch] implementation mpoly factoring with coefficients in ZZ

archive/issues_002179.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan\n\nHere's a pure python implementation of an algorithm to factor polynomials over ZZ using kronecker's trick (specializing a variable to a large prime reduces you to a poly of fewer variables).  Note that this also fills in an implementation of factoring over ZZ[x,y] --- we don't have any implementation at all for this currently.  It's also faster than singular (over QQ) for some cases.\n\nHere's an example with my favorite trouble-maker for singular.\n\nthis patch:\n\n```\nsage: R.<p10,g0,g1,g2,g3,g4,X1,X2>=ZZ[]\nsage: t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1\nsage: time t.factor()\nCPU times: user 0.11 s, sys: 0.00 s, total: 0.12 s\nWall time: 0.12\n(-1) * (p10^8*X2 - 1) * (p10^8*X1 - 1) * (p10^18*X1*X2 - 1) * (p10^32*X2^4 + p10^24*X2^3 + p10^16*X2^2 + p10^8*X2 + 1) * (p10^32*X1^4 + p10^24*X1^3 + p10^16*X1^2 + p10^8*X1 + 1) * (p10^72*X1^4*X2^4 + p10^54*X1^3*X2^3 + p10^36*X1^2*X2^2 + p10^18*X1*X2 + 1)\n```\n\n\nsingular:\n\n```\nsage: R.<p10,g0,g1,g2,g3,g4,X1,X2>=QQ[]\nsage: t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1\nsage: time t.factor()\nCPU times: <longer than I wanted to wait>\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2179\n\n",
    "created_at": "2008-02-16T20:45:54Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch] implementation mpoly factoring with coefficients in ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2179",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: @williamstein

CC:  @ncalexan

Here's a pure python implementation of an algorithm to factor polynomials over ZZ using kronecker's trick (specializing a variable to a large prime reduces you to a poly of fewer variables).  Note that this also fills in an implementation of factoring over ZZ[x,y] --- we don't have any implementation at all for this currently.  It's also faster than singular (over QQ) for some cases.

Here's an example with my favorite trouble-maker for singular.

this patch:

```
sage: R.<p10,g0,g1,g2,g3,g4,X1,X2>=ZZ[]
sage: t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1
sage: time t.factor()
CPU times: user 0.11 s, sys: 0.00 s, total: 0.12 s
Wall time: 0.12
(-1) * (p10^8*X2 - 1) * (p10^8*X1 - 1) * (p10^18*X1*X2 - 1) * (p10^32*X2^4 + p10^24*X2^3 + p10^16*X2^2 + p10^8*X2 + 1) * (p10^32*X1^4 + p10^24*X1^3 + p10^16*X1^2 + p10^8*X1 + 1) * (p10^72*X1^4*X2^4 + p10^54*X1^3*X2^3 + p10^36*X1^2*X2^2 + p10^18*X1*X2 + 1)
```


singular:

```
sage: R.<p10,g0,g1,g2,g3,g4,X1,X2>=QQ[]
sage: t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1
sage: time t.factor()
CPU times: <longer than I wanted to wait>
```



Issue created by migration from https://trac.sagemath.org/ticket/2179





---

archive/issue_comments_014270.json:
```json
{
    "body": "Attachment [mpoly-factor.patch](tarball://root/attachments/some-uuid/ticket2179/mpoly-factor.patch) by jbmohler created at 2008-02-16 20:46:15",
    "created_at": "2008-02-16T20:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14270",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [mpoly-factor.patch](tarball://root/attachments/some-uuid/ticket2179/mpoly-factor.patch) by jbmohler created at 2008-02-16 20:46:15



---

archive/issue_comments_014271.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2008-02-16T20:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14271",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_014272.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2008-02-16T20:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14272",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_014273.json:
```json
{
    "body": "I am no expert on factoring algorithms, but this does seem to fill a needed hole, is reasonably implemented, and has some rudimentary doctests.\n\nI say apply.\n\nIsn't this whole area going to be addressed soon anyway, so that this code will likely be reviewed and enhanced shortly?",
    "created_at": "2008-02-18T19:44:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14273",
    "user": "https://github.com/ncalexan"
}
```

I am no expert on factoring algorithms, but this does seem to fill a needed hole, is reasonably implemented, and has some rudimentary doctests.

I say apply.

Isn't this whole area going to be addressed soon anyway, so that this code will likely be reviewed and enhanced shortly?



---

archive/issue_comments_014274.json:
```json
{
    "body": "REVIEW:\n\nThis absolutely should not be applied for the simple reason that the file `sage/rings/polynomial/multi_polynomial_factor.py`\nintroduces 7 new functions that have 0 docstrings and 0 doctests, and essentially 0 documentation.  My understanding, which I want to push very hard, is that no new code should go into Sage that reduces the overall doctest coverage score. \n\nJoel -- can you add doctests and docstrings for every single function `multi_polynomial_factor.py`?    I do that with *all* new code I write for Sage.",
    "created_at": "2008-02-19T14:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14274",
    "user": "https://github.com/williamstein"
}
```

REVIEW:

This absolutely should not be applied for the simple reason that the file `sage/rings/polynomial/multi_polynomial_factor.py`
introduces 7 new functions that have 0 docstrings and 0 doctests, and essentially 0 documentation.  My understanding, which I want to push very hard, is that no new code should go into Sage that reduces the overall doctest coverage score. 

Joel -- can you add doctests and docstrings for every single function `multi_polynomial_factor.py`?    I do that with *all* new code I write for Sage.



---

archive/issue_comments_014275.json:
```json
{
    "body": "I'm reviewing my own code today.  Expect a new patch to be submitted as of later today.  I just thought I'd mention that here in case someone was looking at this code today.",
    "created_at": "2008-02-25T17:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14275",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

I'm reviewing my own code today.  Expect a new patch to be submitted as of later today.  I just thought I'd mention that here in case someone was looking at this code today.



---

archive/issue_comments_014276.json:
```json
{
    "body": "I'm retracting this for the moment.  As expected, once I started looking at this code I found so many ways to improve it and totally got sucked in again and want to make it better.",
    "created_at": "2008-02-27T02:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14276",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

I'm retracting this for the moment.  As expected, once I started looking at this code I found so many ways to improve it and totally got sucked in again and want to make it better.



---

archive/issue_comments_014277.json:
```json
{
    "body": "Changing assignee from @malb to jbmohler.",
    "created_at": "2008-03-28T11:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14277",
    "user": "https://github.com/malb"
}
```

Changing assignee from @malb to jbmohler.



---

archive/issue_comments_014278.json:
```json
{
    "body": "Here is what Magma does, for the record:\n   http://magma.maths.usyd.edu.au/magma/htmlhelp/text315.htm\n\nAnd for GCD:\n   http://magma.maths.usyd.edu.au/magma/htmlhelp/text314.htm#1994",
    "created_at": "2008-04-01T05:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14278",
    "user": "https://github.com/williamstein"
}
```

Here is what Magma does, for the record:
   http://magma.maths.usyd.edu.au/magma/htmlhelp/text315.htm

And for GCD:
   http://magma.maths.usyd.edu.au/magma/htmlhelp/text314.htm#1994



---

archive/issue_comments_014279.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-20T04:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14279",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_014280.json:
```json
{
    "body": "Joel says he has an improved patch with various additional tricks to filter easy factors. I will wait for an updated patch to review this.",
    "created_at": "2008-07-04T17:32:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14280",
    "user": "https://github.com/burcin"
}
```

Joel says he has an improved patch with various additional tricks to filter easy factors. I will wait for an updated patch to review this.



---

archive/issue_comments_014281.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T23:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14281",
    "user": "https://github.com/malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_014282.json:
```json
{
    "body": "Related: #17840",
    "created_at": "2015-04-13T16:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14282",
    "user": "https://github.com/mezzarobba"
}
```

Related: #17840



---

archive/issue_comments_014283.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2015-05-24T09:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14283",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_014284.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-06-19T08:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2179#issuecomment-14284",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
