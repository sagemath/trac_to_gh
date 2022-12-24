# Issue 3620: minpoly slow for finte fields

archive/issues_003620.json:
```json
{
    "body": "Assignee: tbd\n\nIt goes via pari calls, rather than invoking ntl directly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3620\n\n",
    "created_at": "2008-07-09T00:03:58Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "minpoly slow for finte fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3620",
    "user": "@robertwb"
}
```
Assignee: tbd

It goes via pari calls, rather than invoking ntl directly.

Issue created by migration from https://trac.sagemath.org/ticket/3620





---

archive/issue_comments_025550.json:
```json
{
    "body": "But note, we may want to use our own implementation since minpoly and charpoly of *matrices* over finite fields in sage is so fast.",
    "created_at": "2008-07-09T00:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25550",
    "user": "@williamstein"
}
```

But note, we may want to use our own implementation since minpoly and charpoly of *matrices* over finite fields in sage is so fast.



---

archive/issue_comments_025551.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-07-09T18:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25551",
    "user": "@williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_025552.json:
```json
{
    "body": "Here is an example that illustrates the difference:\n\n```\nsage: k.<a> = GF(2^100)\nsage: time g = k.random_element().charpoly()\nCPU times: user 1.17 s, sys: 0.02 s, total: 1.18 s\nWall time: 1.36 s\nsage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^100)));')\n'Time: 0.000'\n```\n\n\nHere's the sage code that does the charpoly computation:\n\n```\nsage: a.charpoly??\n        from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing\n        R = PolynomialRing(self.parent().prime_subfield(), var)\n        return R(self._pari_().charpoly('x').lift())\n```\n\n\nIt turns out that pari is just totally abysmal at computing charpolys of Mod's.\n\n```\nsage: f = k.random_element()._pari_()\nsage: time g = f.charpoly('x')\nCPU times: user 1.13 s, sys: 0.01 s, total: 1.14 s\nWall time: 1.26 s\nsage: f.type()\n't_POLMOD'\n```\n\n\nFortunately Sage matrices aren't quite as bad, though of course this is still vastly\nslower than Magma:\n\n```\nsage: time g = k.random_element().matrix().charpoly()\nCPU times: user 0.36 s, sys: 0.00 s, total: 0.36 s\nWall time: 0.37 s\n\n```\n\n\nAsymptotically though this is still vastly better than the current situation:\n\n```\nage: k.<a> = GF(2^200)\nsage: time g = k.random_element().matrix().charpoly()\nCPU times: user 2.21 s, sys: 0.03 s, total: 2.24 s\nWall time: 2.24 s\nsage: time g = k.random_element().charpoly()\nCPU times: user 14.14 s, sys: 0.08 s, total: 14.22 s\nWall time: 14.27 s\n```\n\n\nBut still this sucks compared to magma\n\n```\nsage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^200)));')\n'Time: 0.000'\nsage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^200)));')\n'Time: 0.000'\nsage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^300)));')\n'Time: 0.000'\nsage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^400)));')\n'Time: 0.010'\nsage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^600)));')\n'Time: 0.010'\nsage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^1000)));')\n'Time: 0.030'\n```\n\n\nI looked at NTL seems to have no functions at all for charpoly or minpoly\nof elements of GF(2^n).  :-(\n\nhttp://www.shoup.net/ntl/doc/GF2E.txt",
    "created_at": "2008-07-09T19:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25552",
    "user": "@williamstein"
}
```

Here is an example that illustrates the difference:

```
sage: k.<a> = GF(2^100)
sage: time g = k.random_element().charpoly()
CPU times: user 1.17 s, sys: 0.02 s, total: 1.18 s
Wall time: 1.36 s
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^100)));')
'Time: 0.000'
```


Here's the sage code that does the charpoly computation:

```
sage: a.charpoly??
        from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
        R = PolynomialRing(self.parent().prime_subfield(), var)
        return R(self._pari_().charpoly('x').lift())
```


It turns out that pari is just totally abysmal at computing charpolys of Mod's.

```
sage: f = k.random_element()._pari_()
sage: time g = f.charpoly('x')
CPU times: user 1.13 s, sys: 0.01 s, total: 1.14 s
Wall time: 1.26 s
sage: f.type()
't_POLMOD'
```


Fortunately Sage matrices aren't quite as bad, though of course this is still vastly
slower than Magma:

```
sage: time g = k.random_element().matrix().charpoly()
CPU times: user 0.36 s, sys: 0.00 s, total: 0.36 s
Wall time: 0.37 s

```


Asymptotically though this is still vastly better than the current situation:

```
age: k.<a> = GF(2^200)
sage: time g = k.random_element().matrix().charpoly()
CPU times: user 2.21 s, sys: 0.03 s, total: 2.24 s
Wall time: 2.24 s
sage: time g = k.random_element().charpoly()
CPU times: user 14.14 s, sys: 0.08 s, total: 14.22 s
Wall time: 14.27 s
```


But still this sucks compared to magma

```
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^200)));')
'Time: 0.000'
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^200)));')
'Time: 0.000'
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^300)));')
'Time: 0.000'
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^400)));')
'Time: 0.010'
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^600)));')
'Time: 0.010'
sage: magma.eval('time f := CharacteristicPolynomial(Random(GF(2^1000)));')
'Time: 0.030'
```


I looked at NTL seems to have no functions at all for charpoly or minpoly
of elements of GF(2^n).  :-(

http://www.shoup.net/ntl/doc/GF2E.txt



---

archive/issue_comments_025553.json:
```json
{
    "body": "also note:\n\n\n```\nsage: k.<a> = GF(2^500)\nsage: time g = k.random_element()\nCPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s\nWall time: 0.06 s\nsage: time m = g.matrix()\nCPU times: user 11.59 s, sys: 0.82 s, total: 12.41 s\nWall time: 12.41 s\nsage: time f = m.charpoly()\nCPU times: user 20.51 s, sys: 0.01 s, total: 20.52 s\nWall time: 20.51 s\n```\n",
    "created_at": "2008-07-09T19:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25553",
    "user": "dmharvey"
}
```

also note:


```
sage: k.<a> = GF(2^500)
sage: time g = k.random_element()
CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
Wall time: 0.06 s
sage: time m = g.matrix()
CPU times: user 11.59 s, sys: 0.82 s, total: 12.41 s
Wall time: 12.41 s
sage: time f = m.charpoly()
CPU times: user 20.51 s, sys: 0.01 s, total: 20.52 s
Wall time: 20.51 s
```




---

archive/issue_comments_025554.json:
```json
{
    "body": "Attachment [sage-3620.patch](tarball://root/attachments/some-uuid/ticket3620/sage-3620.patch) by @williamstein created at 2008-07-09 19:53:25",
    "created_at": "2008-07-09T19:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25554",
    "user": "@williamstein"
}
```

Attachment [sage-3620.patch](tarball://root/attachments/some-uuid/ticket3620/sage-3620.patch) by @williamstein created at 2008-07-09 19:53:25



---

archive/issue_comments_025555.json:
```json
{
    "body": "1. dmharvey -- i have no clue what the point of your remark is above.\n\n2. the point of my patch, by the way, is just to be a first tiny step.",
    "created_at": "2008-07-09T19:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25555",
    "user": "@williamstein"
}
```

1. dmharvey -- i have no clue what the point of your remark is above.

2. the point of my patch, by the way, is just to be a first tiny step.



---

archive/issue_comments_025556.json:
```json
{
    "body": "Looks good to me.  Should there be another ticket for improving this further.",
    "created_at": "2008-07-09T20:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25556",
    "user": "@mwhansen"
}
```

Looks good to me.  Should there be another ticket for improving this further.



---

archive/issue_comments_025557.json:
```json
{
    "body": "My point is just that computing the matrix and computing its charpoly both take non-negligble time.",
    "created_at": "2008-07-09T20:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25557",
    "user": "dmharvey"
}
```

My point is just that computing the matrix and computing its charpoly both take non-negligble time.



---

archive/issue_comments_025558.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-10T02:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25558",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025559.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc3",
    "created_at": "2008-07-10T02:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25559",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc3



---

archive/issue_comments_025560.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-07-10T06:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25560",
    "user": "@robertwb"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_025561.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-07-10T06:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25561",
    "user": "@robertwb"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_025562.json:
```json
{
    "body": "It looks like NTL does have minimal polynomial computations, though provided in http://www.shoup.net/ntl/doc/GF2X.txt rather than http://www.shoup.net/ntl/doc/GF2E.txt . We should probably use the proof flag to decide the algorithm. Trace could be wrapped as well. \n\nAlso, the computation of matrix() is using the completely generic code, which has got to be sub-optimal for manipulating elements of GF(2).",
    "created_at": "2008-07-10T06:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25562",
    "user": "@robertwb"
}
```

It looks like NTL does have minimal polynomial computations, though provided in http://www.shoup.net/ntl/doc/GF2X.txt rather than http://www.shoup.net/ntl/doc/GF2E.txt . We should probably use the proof flag to decide the algorithm. Trace could be wrapped as well. 

Also, the computation of matrix() is using the completely generic code, which has got to be sub-optimal for manipulating elements of GF(2).



---

archive/issue_comments_025563.json:
```json
{
    "body": "Robert,\n\nI see no reason to reason to reopen this ticket since what you describe seems to be an improvement/additional change. Please open another ticket since the attached patch has been merged in Sage 3.0.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-10T10:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25563",
    "user": "mabshoff"
}
```

Robert,

I see no reason to reason to reopen this ticket since what you describe seems to be an improvement/additional change. Please open another ticket since the attached patch has been merged in Sage 3.0.4.

Cheers,

Michael



---

archive/issue_comments_025564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-10T10:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3620#issuecomment-25564",
    "user": "mabshoff"
}
```

Resolution: fixed
