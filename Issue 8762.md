# Issue 8762: the sparse=True flag is horribly broken for GF(p)[x]

archive/issues_008762.json:
```json
{
    "body": "Assignee: @aghitza\n\n\n```\nOn Apr 24, 2010, at 5:36 PM, Michael Rybalkin wrote:\n\nHow to get monomial with large exponent in the polynomial rings?\n\nFor example I hsave polynomial ring over large finite field:\np = next_prime(10^20)\nR.<x> = PolynomialRing(GF(p), sparse=True)\n\nMonomial x^(10^7) construction takes 2 seconds:\ntime tmp = x^(10^7)\n\nMonomial x^(10^8) construction uses all 6 Gb server memory and cannot\nfinish.\nAnd without 'sparse=True' option I cannot even get x^(10^6).\n\nWhat is the limitations for monomial exponents in polynomial rings?\nWhat can be done in my case? For example GAP handles this case without\nany problem.\n\nSeems like the sparse=True flag is horribly broken for GF(p)[x]:\n\nsage: p = next_prime(10^20)\nsage: R.<x> = PolynomialRing(GF(p), sparse=True)\nsage: type(x)\n<type 'sage.rings.polynomial.polynomial_zz_pex.Polynomial_ZZ_pEX'>\n\nsage: R.<x> = PolynomialRing(QQ, sparse=True)\nsage: x^(10^8)\nx^100000000\n\n\n- Robert Bradshaw\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8762\n\n",
    "created_at": "2010-04-25T07:17:01Z",
    "labels": [
        "algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "the sparse=True flag is horribly broken for GF(p)[x]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8762",
    "user": "@williamstein"
}
```
Assignee: @aghitza


```
On Apr 24, 2010, at 5:36 PM, Michael Rybalkin wrote:

How to get monomial with large exponent in the polynomial rings?

For example I hsave polynomial ring over large finite field:
p = next_prime(10^20)
R.<x> = PolynomialRing(GF(p), sparse=True)

Monomial x^(10^7) construction takes 2 seconds:
time tmp = x^(10^7)

Monomial x^(10^8) construction uses all 6 Gb server memory and cannot
finish.
And without 'sparse=True' option I cannot even get x^(10^6).

What is the limitations for monomial exponents in polynomial rings?
What can be done in my case? For example GAP handles this case without
any problem.

Seems like the sparse=True flag is horribly broken for GF(p)[x]:

sage: p = next_prime(10^20)
sage: R.<x> = PolynomialRing(GF(p), sparse=True)
sage: type(x)
<type 'sage.rings.polynomial.polynomial_zz_pex.Polynomial_ZZ_pEX'>

sage: R.<x> = PolynomialRing(QQ, sparse=True)
sage: x^(10^8)
x^100000000


- Robert Bradshaw
```


Issue created by migration from https://trac.sagemath.org/ticket/8762





---

archive/issue_comments_080162.json:
```json
{
    "body": "it also broken for pAdics. see `_single_variable` in `rings/polynomial/polynomial_ring.py` not taking care of the `sparse` argument.",
    "created_at": "2010-08-09T21:44:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8762#issuecomment-80162",
    "user": "ylchapuy"
}
```

it also broken for pAdics. see `_single_variable` in `rings/polynomial/polynomial_ring.py` not taking care of the `sparse` argument.



---

archive/issue_comments_080163.json:
```json
{
    "body": "I don't have the grand overview of this, but it seems that simply adding the condition to only use NTL whenever sparse=False works and was the original intention. I'm uploading the (simple) patch for this, so you can see what I mean.\n\nCheers\nJohan",
    "created_at": "2010-09-13T13:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8762#issuecomment-80163",
    "user": "@johanrosenkilde"
}
```

I don't have the grand overview of this, but it seems that simply adding the condition to only use NTL whenever sparse=False works and was the original intention. I'm uploading the (simple) patch for this, so you can see what I mean.

Cheers
Johan



---

archive/issue_comments_080164.json:
```json
{
    "body": "This patch seems ok to me, but could you please add some doctest to show the bug is gone?\n\nI also opened another ticket for the pAdics problem ( #9929 ).",
    "created_at": "2010-09-17T07:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8762#issuecomment-80164",
    "user": "ylchapuy"
}
```

This patch seems ok to me, but could you please add some doctest to show the bug is gone?

I also opened another ticket for the pAdics problem ( #9929 ).



---

archive/issue_comments_080165.json:
```json
{
    "body": "Sure - I should have done that to begin with.",
    "created_at": "2010-09-17T07:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8762#issuecomment-80165",
    "user": "@johanrosenkilde"
}
```

Sure - I should have done that to begin with.



---

archive/issue_comments_080166.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T07:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8762#issuecomment-80166",
    "user": "@johanrosenkilde"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080167.json:
```json
{
    "body": "Attachment [trac_8762_sparse_gfx.patch](tarball://root/attachments/some-uuid/ticket8762/trac_8762_sparse_gfx.patch) by @johanrosenkilde created at 2010-09-17 07:52:33\n\nOnly use NTL with non-sparse polynomial rings over finite fields. Now with doctest.",
    "created_at": "2010-09-17T07:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8762#issuecomment-80167",
    "user": "@johanrosenkilde"
}
```

Attachment [trac_8762_sparse_gfx.patch](tarball://root/attachments/some-uuid/ticket8762/trac_8762_sparse_gfx.patch) by @johanrosenkilde created at 2010-09-17 07:52:33

Only use NTL with non-sparse polynomial rings over finite fields. Now with doctest.



---

archive/issue_comments_080168.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-25T11:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8762#issuecomment-80168",
    "user": "ylchapuy"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080169.json:
```json
{
    "body": "Ok for me.",
    "created_at": "2010-09-25T11:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8762#issuecomment-80169",
    "user": "ylchapuy"
}
```

Ok for me.



---

archive/issue_comments_080170.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8762",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8762#issuecomment-80170",
    "user": "@qed777"
}
```

Resolution: fixed
