# Issue 3556: [with patch, needs review] Bug in IntegerModRing(n) for very large n

archive/issues_003556.json:
```json
{
    "body": "Assignee: craigcitro\n\nNotice the following:\n\n\n```\nsage: IntegerModRing(next_prime(10^30)).unit_gens()\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n\n/home/craigcitro/<ipython console> in <module>()\n\n/home/was/s/local/lib/python2.5/site-packages/sage/rings/integer_mod_ring.py in unit_gens(self)\n    780             m = n/(p**r)\n    781             for g in self.__unit_gens_primepowercase(p, r):\n--> 782                 x = g.crt(integer_mod.Mod(1,m))\n    783                 self.__unit_gens.append(x)\n    784         return self.__unit_gens\n\n/home/craigcitro/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_abstract.crt (sage/rings/integer_mod.c:7044)()\n\n/home/craigcitro/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_gmp.__crt (sage/rings/integer_mod.c:8578)()\n\nZeroDivisionError: moduli must be coprime\nsage: \n```\n\n\nThe issue is that `crt` doesn't play well when one of the moduli is 1. The attached patch fixes it, and adds a few doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3556\n\n",
    "created_at": "2008-07-06T01:20:25Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Bug in IntegerModRing(n) for very large n",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3556",
    "user": "craigcitro"
}
```
Assignee: craigcitro

Notice the following:


```
sage: IntegerModRing(next_prime(10^30)).unit_gens()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/home/craigcitro/<ipython console> in <module>()

/home/was/s/local/lib/python2.5/site-packages/sage/rings/integer_mod_ring.py in unit_gens(self)
    780             m = n/(p**r)
    781             for g in self.__unit_gens_primepowercase(p, r):
--> 782                 x = g.crt(integer_mod.Mod(1,m))
    783                 self.__unit_gens.append(x)
    784         return self.__unit_gens

/home/craigcitro/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_abstract.crt (sage/rings/integer_mod.c:7044)()

/home/craigcitro/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_gmp.__crt (sage/rings/integer_mod.c:8578)()

ZeroDivisionError: moduli must be coprime
sage: 
```


The issue is that `crt` doesn't play well when one of the moduli is 1. The attached patch fixes it, and adds a few doctests.

Issue created by migration from https://trac.sagemath.org/ticket/3556





---

archive/issue_comments_025145.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-06T14:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3556#issuecomment-25145",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_025146.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T18:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3556#issuecomment-25146",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_025147.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T18:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3556#issuecomment-25147",
    "user": "mabshoff"
}
```

Resolution: fixed
