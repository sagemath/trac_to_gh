# Issue 2601: problem with change_ring

archive/issues_002601.json:
```json
{
    "body": "Assignee: malb\n\nKeywords: ideal, change_ring\n\nThe following produces errors:\n\n\n```\nsage: testR.<a,b,c> = PolynomialRing(QQ,3)\nsage: id_ringA = ideal([a^2-b,b^2-c,c^2-a])\nsage: id_ringB = ideal(id_ringA.gens()).change_ring(PolynomialRing(QQ,'c,b,a')) \n```\n\n\nalthough this does not:\n\n```\nsage: testR.<a,b,c> = PolynomialRing(QQ,3)\nsage: id_ringA = ideal([a^2-b,b^2-c,c^2-a])\nsage: id_ringB = ideal(id_ringA.gens()).change_ring(PolynomialRing(QQ,'c,a,b')) \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2601\n\n",
    "created_at": "2008-03-19T19:14:33Z",
    "labels": [
        "commutative algebra",
        "minor",
        "bug"
    ],
    "title": "problem with change_ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2601",
    "user": "mhampton"
}
```
Assignee: malb

Keywords: ideal, change_ring

The following produces errors:


```
sage: testR.<a,b,c> = PolynomialRing(QQ,3)
sage: id_ringA = ideal([a^2-b,b^2-c,c^2-a])
sage: id_ringB = ideal(id_ringA.gens()).change_ring(PolynomialRing(QQ,'c,b,a')) 
```


although this does not:

```
sage: testR.<a,b,c> = PolynomialRing(QQ,3)
sage: id_ringA = ideal([a^2-b,b^2-c,c^2-a])
sage: id_ringB = ideal(id_ringA.gens()).change_ring(PolynomialRing(QQ,'c,a,b')) 
```


Issue created by migration from https://trac.sagemath.org/ticket/2601





---

archive/issue_comments_017798.json:
```json
{
    "body": "I don't know what's happening, but maybe the following simpler example will help someone figure it out:\n\n\n```\nsage: R.<a,b,c> = PolynomialRing(QQ, 3)\nsage: P = PolynomialRing(QQ, 'c, b, a')\nsage: Q = PolynomialRing(QQ, 'c, a, b')\nsage: Q(a)\na\nsage: P(a)\n...\n<type 'exceptions.IndexError'>: list assignment index out of range\n```\n\n\nNote also that out of the 6 permutations of 'a, b, c', only 'c, b, a' and 'b, c, a' throw this exception; the other 4 seem to work properly.",
    "created_at": "2008-03-20T01:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2601#issuecomment-17798",
    "user": "AlexGhitza"
}
```

I don't know what's happening, but maybe the following simpler example will help someone figure it out:


```
sage: R.<a,b,c> = PolynomialRing(QQ, 3)
sage: P = PolynomialRing(QQ, 'c, b, a')
sage: Q = PolynomialRing(QQ, 'c, a, b')
sage: Q(a)
a
sage: P(a)
...
<type 'exceptions.IndexError'>: list assignment index out of range
```


Note also that out of the 6 permutations of 'a, b, c', only 'c, b, a' and 'b, c, a' throw this exception; the other 4 seem to work properly.



---

archive/issue_comments_017799.json:
```json
{
    "body": "I believe the problem is in _mpoly_dict_recursive() in multi_polynomial.pyx:\n\n\n```\nsage: R.<a,b,c> = PolynomialRing(QQ, 3)\nsage: a._mpoly_dict_recursive(['c', 'b', 'a'])\n---------------------------------------------------------------------------\n<type 'exceptions.IndexError'>            Traceback (most recent call last)\n\n/root/<ipython console> in <module>()\n\n/root/multi_polynomial.pyx in sage.rings.polynomial.multi_polynomial.MPolynomial._mpoly_dict_recursive()\n\n<type 'exceptions.IndexError'>: list assignment index out of range\n```\n\n\nThis should return {(0, 0, 1): 1}.  I'm having trouble understanding exactly how the code works so I'm giving up on trying to fix this.  Someone familiar with the code should be able to do this properly, and much faster than me.",
    "created_at": "2008-03-28T00:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2601#issuecomment-17799",
    "user": "AlexGhitza"
}
```

I believe the problem is in _mpoly_dict_recursive() in multi_polynomial.pyx:


```
sage: R.<a,b,c> = PolynomialRing(QQ, 3)
sage: a._mpoly_dict_recursive(['c', 'b', 'a'])
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/root/<ipython console> in <module>()

/root/multi_polynomial.pyx in sage.rings.polynomial.multi_polynomial.MPolynomial._mpoly_dict_recursive()

<type 'exceptions.IndexError'>: list assignment index out of range
```


This should return {(0, 0, 1): 1}.  I'm having trouble understanding exactly how the code works so I'm giving up on trying to fix this.  Someone familiar with the code should be able to do this properly, and much faster than me.



---

archive/issue_comments_017800.json:
```json
{
    "body": "Attachment [trac_2601.patch](tarball://root/attachments/some-uuid/ticket2601/trac_2601.patch) by was created at 2009-01-24 10:19:17",
    "created_at": "2009-01-24T10:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2601#issuecomment-17800",
    "user": "was"
}
```

Attachment [trac_2601.patch](tarball://root/attachments/some-uuid/ticket2601/trac_2601.patch) by was created at 2009-01-24 10:19:17



---

archive/issue_comments_017801.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-01-27T06:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2601#issuecomment-17801",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_017802.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3",
    "created_at": "2009-01-28T12:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2601#issuecomment-17802",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3



---

archive/issue_comments_017803.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T12:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2601#issuecomment-17803",
    "user": "mabshoff"
}
```

Resolution: fixed
