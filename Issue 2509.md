# Issue 2509: [with patch, needs review] showstopper in xgcd(f, 0)

archive/issues_002509.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @ncalexan\n\nThis is an absolute showstopper, but it's a little tricky to hit the right piece of code.\n\n\n```\nsage: x = GF(37**4, 'a')['x'].gen()\nsage: x.xgcd\n<built-in method xgcd of Polynomial_generic_dense_field object at 0xca59298>\nsage: x.xgcd(0)\n(1, 0, x)\nsage: 0.xgcd(x)\n(x, 0, 1)\nsage: x.xgcd(x)\n(x, 0, 1)\n```\n\n\nObserve that the first `xgcd` has the outputs in the wrong order.  This cost me hours of debugging the Cantor reduction algorithms in the hyperelliptic curves code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2509\n\n",
    "created_at": "2008-03-13T20:25:55Z",
    "labels": [
        "basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] showstopper in xgcd(f, 0)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2509",
    "user": "@ncalexan"
}
```
Assignee: somebody

CC:  @ncalexan

This is an absolute showstopper, but it's a little tricky to hit the right piece of code.


```
sage: x = GF(37**4, 'a')['x'].gen()
sage: x.xgcd
<built-in method xgcd of Polynomial_generic_dense_field object at 0xca59298>
sage: x.xgcd(0)
(1, 0, x)
sage: 0.xgcd(x)
(x, 0, 1)
sage: x.xgcd(x)
(x, 0, 1)
```


Observe that the first `xgcd` has the outputs in the wrong order.  This cost me hours of debugging the Cantor reduction algorithms in the hyperelliptic curves code.

Issue created by migration from https://trac.sagemath.org/ticket/2509





---

archive/issue_comments_017017.json:
```json
{
    "body": "Attachment [2509-ncalexan-xgcd.patch](tarball://root/attachments/some-uuid/ticket2509/2509-ncalexan-xgcd.patch) by @ncalexan created at 2008-03-13 20:27:27",
    "created_at": "2008-03-13T20:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2509#issuecomment-17017",
    "user": "@ncalexan"
}
```

Attachment [2509-ncalexan-xgcd.patch](tarball://root/attachments/some-uuid/ticket2509/2509-ncalexan-xgcd.patch) by @ncalexan created at 2008-03-13 20:27:27



---

archive/issue_comments_017018.json:
```json
{
    "body": "I am reviewing this right now and expect to give a positive review as soon as the doctests are finished...",
    "created_at": "2008-03-13T20:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2509#issuecomment-17018",
    "user": "dmharvey"
}
```

I am reviewing this right now and expect to give a positive review as soon as the doctests are finished...



---

archive/issue_comments_017019.json:
```json
{
    "body": "Well, there are two doctest failures. One was easy to fix (a broken doctest in `polynomial_integer_dense_ntl.pyx`), I have attached a patch.\n\nThe other one is really weird. In `sage/structure/factorization.py`, we have the following doctest:\n\n\n```\n        We create a polynomial over the real double field and factor it:                       \n            sage: x = polygen(RDF, 'x')                                                        \n            sage: F = factor(-2*x^2 - 1); F                                                    \n            (-2.0) * (1.0*x^2 - 1.82173070032e-16*x + 0.5) * (1.0*x^2 + 0.5)    # 32-bit       \n            (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)    # 64-bit       \n```\n\n\nThe 32-bit example gets a little changed with Nick's patch.\n\nBUT... look more closely at that doctest. WTF? 2 + 2 = 2?",
    "created_at": "2008-03-13T22:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2509#issuecomment-17019",
    "user": "dmharvey"
}
```

Well, there are two doctest failures. One was easy to fix (a broken doctest in `polynomial_integer_dense_ntl.pyx`), I have attached a patch.

The other one is really weird. In `sage/structure/factorization.py`, we have the following doctest:


```
        We create a polynomial over the real double field and factor it:                       
            sage: x = polygen(RDF, 'x')                                                        
            sage: F = factor(-2*x^2 - 1); F                                                    
            (-2.0) * (1.0*x^2 - 1.82173070032e-16*x + 0.5) * (1.0*x^2 + 0.5)    # 32-bit       
            (-2.0) * (1.0*x^2 - 2.22044604925e-16*x + 0.5) * (1.0*x^2 + 0.5)    # 64-bit       
```


The 32-bit example gets a little changed with Nick's patch.

BUT... look more closely at that doctest. WTF? 2 + 2 = 2?



---

archive/issue_comments_017020.json:
```json
{
    "body": "Attachment [2509-ncalexan-xgcd-2.patch](tarball://root/attachments/some-uuid/ticket2509/2509-ncalexan-xgcd-2.patch) by dmharvey created at 2008-03-13 22:16:32",
    "created_at": "2008-03-13T22:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2509#issuecomment-17020",
    "user": "dmharvey"
}
```

Attachment [2509-ncalexan-xgcd-2.patch](tarball://root/attachments/some-uuid/ticket2509/2509-ncalexan-xgcd-2.patch) by dmharvey created at 2008-03-13 22:16:32



---

archive/issue_comments_017021.json:
```json
{
    "body": "The fact that another doctest broke shows that the doctest is not testing the correct code... or there is another bug there.  However, on closer inspection, everything looks okay to me.\n\nThe bug you are reporting about numerical noise is well-known and there is a fix that will be applied in 2.10.4.  It's independent of this patch.\n\nThanks!\nNick",
    "created_at": "2008-03-13T22:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2509#issuecomment-17021",
    "user": "@ncalexan"
}
```

The fact that another doctest broke shows that the doctest is not testing the correct code... or there is another bug there.  However, on closer inspection, everything looks okay to me.

The bug you are reporting about numerical noise is well-known and there is a fix that will be applied in 2.10.4.  It's independent of this patch.

Thanks!
Nick



---

archive/issue_comments_017022.json:
```json
{
    "body": "nick: yes ok I agree. The stuff in `polynomial_integer_dense` is happening because it's a special case that's falling back on generic code. (Possibly it shouldn't be doing that, but that's for another day.)\n\nI'll take your word for it that the factoring thing is unrelated.\n\nThumbs up for this patch.",
    "created_at": "2008-03-14T00:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2509#issuecomment-17022",
    "user": "dmharvey"
}
```

nick: yes ok I agree. The stuff in `polynomial_integer_dense` is happening because it's a special case that's falling back on generic code. (Possibly it shouldn't be doing that, but that's for another day.)

I'll take your word for it that the factoring thing is unrelated.

Thumbs up for this patch.



---

archive/issue_comments_017023.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T01:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2509#issuecomment-17023",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017024.json:
```json
{
    "body": "Both patches merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T01:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2509",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2509#issuecomment-17024",
    "user": "mabshoff"
}
```

Both patches merged in Sage 2.10.4.alpha0
