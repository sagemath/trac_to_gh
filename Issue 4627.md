# Issue 4627: CRT_list in HNF dominates computation

archive/issues_004627.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: hermite normal form hnf gcd\n\n\n```\nOn 4-Sep-08, at 3:57 PM, Clement Pernet wrote:\n\nHi,\n\nNo problem, the patch looks fine, and I will run some testings to check\nit. Nick, are you going to open a ticket?\n\n--\nCl\u00e9ment\n\nWilliam Stein a \u00e9crit :\nOn Wed, Sep 3, 2008 at 4:39 PM, Nick Alexander <ncalexander@gmail.com> wrote:\nHi William,\n\nThe attached patch prevents recomputing a CRT a number of times when doing a\nmulti modular Hermite normal form.  I was finding that this CRT computation\nwas taking *much* longer than the rest of the calculation of a midsize HNF\n(40 x 40).  Has this been addressed?\n\nNo.\n\n Should this be run by Clement and some\nrandomized testing?\n\nYes, definitely.   I've cc'd Clement and included the attachment.\n\n-- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4627\n\n",
    "created_at": "2008-11-26T19:06:10Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "CRT_list in HNF dominates computation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4627",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

Keywords: hermite normal form hnf gcd


```
On 4-Sep-08, at 3:57 PM, Clement Pernet wrote:

Hi,

No problem, the patch looks fine, and I will run some testings to check
it. Nick, are you going to open a ticket?

--
Clément

William Stein a écrit :
On Wed, Sep 3, 2008 at 4:39 PM, Nick Alexander <ncalexander@gmail.com> wrote:
Hi William,

The attached patch prevents recomputing a CRT a number of times when doing a
multi modular Hermite normal form.  I was finding that this CRT computation
was taking *much* longer than the rest of the calculation of a midsize HNF
(40 x 40).  Has this been addressed?

No.

 Should this be run by Clement and some
randomized testing?

Yes, definitely.   I've cc'd Clement and included the attachment.

-- William
```


Issue created by migration from https://trac.sagemath.org/ticket/4627





---

archive/issue_comments_034727.json:
```json
{
    "body": "Attachment [4627-ncalexan-hnf-crt-1.patch](tarball://root/attachments/some-uuid/ticket4627/4627-ncalexan-hnf-crt-1.patch) by mabshoff created at 2008-11-26 23:13:06\n\nWhat is the credit situation here?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-26T23:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4627#issuecomment-34727",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [4627-ncalexan-hnf-crt-1.patch](tarball://root/attachments/some-uuid/ticket4627/4627-ncalexan-hnf-crt-1.patch) by mabshoff created at 2008-11-26 23:13:06

What is the credit situation here?

Cheers,

Michael



---

archive/issue_comments_034728.json:
```json
{
    "body": "So this code looks fine to me, but I can't find any cases where it makes a significant change in runtime. For instance, taking a random 40x40 matrix over ZZ, the runtimes are the same before and after the patch. \n\nNick, what is a good test case to see the performance improvement?",
    "created_at": "2008-11-27T00:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4627#issuecomment-34728",
    "user": "https://github.com/craigcitro"
}
```

So this code looks fine to me, but I can't find any cases where it makes a significant change in runtime. For instance, taking a random 40x40 matrix over ZZ, the runtimes are the same before and after the patch. 

Nick, what is a good test case to see the performance improvement?



---

archive/issue_comments_034729.json:
```json
{
    "body": "Attachment [trac-4627-v2.patch](tarball://root/attachments/some-uuid/ticket4627/trac-4627-v2.patch) by @craigcitro created at 2008-11-27 04:18:30",
    "created_at": "2008-11-27T04:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4627#issuecomment-34729",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4627-v2.patch](tarball://root/attachments/some-uuid/ticket4627/trac-4627-v2.patch) by @craigcitro created at 2008-11-27 04:18:30



---

archive/issue_comments_034730.json:
```json
{
    "body": "Looks good! Nick pointed out a nice example of a test case:\n\nBEFORE:\n\n```\nsage: y = polygen(ZZ)\nsage: M.<a> = NumberField(y^20 - 2*y^19 + 10*y^17 - 15*y^16 + 40*y^14 - 64*y^13 + 46*y^12 + 8*y^11 - 32*y^10 + 8*y^9 + 46*y^8 - 64*y^7 + 40*y^6 - 15*y^4 + 10*y^3 - 2*y + 1)\nsage: time M.ideal(prod(prime_range(6000,6200))).free_module()\nCPU times: user 33.71 s, sys: 2.02 s, total: 35.73 s\nWall time: 36.06 s\n\nFree module of degree 20 and rank 20 over Integer Ring\nUser basis matrix:\n20 x 20 dense matrix over Rational Field\n```\n\n\nAFTER:\n\n```\nsage: y = polygen(ZZ)\nsage: M.<a> = NumberField(y^20 - 2*y^19 + 10*y^17 - 15*y^16 + 40*y^14 - 64*y^13 + 46*y^12 + 8*y^11 - 32*y^10 + 8*y^9 + 46*y^8 - 64*y^7 + 40*y^6 - 15*y^4 + 10*y^3 - 2*y + 1)\nsage: time M.ideal(prod(prime_range(6000,6200))).free_module()\nCPU times: user 0.65 s, sys: 0.05 s, total: 0.70 s\nWall time: 0.70 s\n\nFree module of degree 20 and rank 20 over Integer Ring\nUser basis matrix:\n20 x 20 dense matrix over Rational Field\n```\n\n\nSpeedup of 50X -- not too shabby! In particular, it seems to apply when you have really large coefficients compared to the size of the matrix. (This seems reasonable, given that for small entries, the CRT simply doesn't get applied that many times, since one has a bound on the size of the output.)\n\nI added another doctest (which really needs compared between versions with `%timeit`), and committed the patch in Nick's name.",
    "created_at": "2008-11-27T04:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4627#issuecomment-34730",
    "user": "https://github.com/craigcitro"
}
```

Looks good! Nick pointed out a nice example of a test case:

BEFORE:

```
sage: y = polygen(ZZ)
sage: M.<a> = NumberField(y^20 - 2*y^19 + 10*y^17 - 15*y^16 + 40*y^14 - 64*y^13 + 46*y^12 + 8*y^11 - 32*y^10 + 8*y^9 + 46*y^8 - 64*y^7 + 40*y^6 - 15*y^4 + 10*y^3 - 2*y + 1)
sage: time M.ideal(prod(prime_range(6000,6200))).free_module()
CPU times: user 33.71 s, sys: 2.02 s, total: 35.73 s
Wall time: 36.06 s

Free module of degree 20 and rank 20 over Integer Ring
User basis matrix:
20 x 20 dense matrix over Rational Field
```


AFTER:

```
sage: y = polygen(ZZ)
sage: M.<a> = NumberField(y^20 - 2*y^19 + 10*y^17 - 15*y^16 + 40*y^14 - 64*y^13 + 46*y^12 + 8*y^11 - 32*y^10 + 8*y^9 + 46*y^8 - 64*y^7 + 40*y^6 - 15*y^4 + 10*y^3 - 2*y + 1)
sage: time M.ideal(prod(prime_range(6000,6200))).free_module()
CPU times: user 0.65 s, sys: 0.05 s, total: 0.70 s
Wall time: 0.70 s

Free module of degree 20 and rank 20 over Integer Ring
User basis matrix:
20 x 20 dense matrix over Rational Field
```


Speedup of 50X -- not too shabby! In particular, it seems to apply when you have really large coefficients compared to the size of the matrix. (This seems reasonable, given that for small entries, the CRT simply doesn't get applied that many times, since one has a bound on the size of the output.)

I added another doctest (which really needs compared between versions with `%timeit`), and committed the patch in Nick's name.



---

archive/issue_comments_034731.json:
```json
{
    "body": "Merged trac-4627-v2.patch in Sage 3.2.1.alpha2",
    "created_at": "2008-11-27T04:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4627#issuecomment-34731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-4627-v2.patch in Sage 3.2.1.alpha2



---

archive/issue_comments_034732.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-27T04:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4627",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4627#issuecomment-34732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
