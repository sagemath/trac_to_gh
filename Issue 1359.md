# Issue 1359: implement cyclotomic norm residues

archive/issues_001359.json:
```json
{
    "body": "Assignee: @williamstein\n\nHere's the code, basically:\n\nbug day 6 -- #1342\nsystem:sage\n\n\n```\nK.<zeta> = CyclotomicField(7)\n```\n\n\n\n```\ndef norm_symbol_prime(a, P):\n     K = P.number_field()\n     zeta = K.gen()\n     n = K.zeta_order()\n     exponent = (1/n) * ( P.norm() - 1)\n     exponent = ZZ(exponent)\n     FF = K.residue_field(P)\n     aa = FF(a)\n     b = FF(a)^exponent\n     zeta_mod = FF(zeta)\n     # Find power m of zeta_mod that is equal to b, then\n     # return zeta^m\n     m = 0\n     w = FF(1)\n     while w != b:\n         w = w * zeta_mod\n         m += 1\n         assert m <= n, \"bug in norm_symbol_prime\"\n     return zeta^m\n\ndef norm_symbol(a, b):\n     F = K.fractional_ideal([b]).factor()\n     return prod([norm_symbol_prime(a, P)^e for P, e in F],\n               K(1))\n```\n\n\n\n```\nnorm_symbol(zeta^3, 13*zeta)\n///\n-zeta^5 - zeta^4 - zeta^3 - zeta^2 - zeta - 1\n```\n\n\n\n```\nnorm_symbol(zeta^7, K(11))\n///\n1\n```\n\n\n\n```\nnorm_symbol((1+zeta)^2, 23*zeta)\n///\nzeta^4\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1359\n\n",
    "created_at": "2007-12-02T02:52:02Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "implement cyclotomic norm residues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1359",
    "user": "@williamstein"
}
```
Assignee: @williamstein

Here's the code, basically:

bug day 6 -- #1342
system:sage


```
K.<zeta> = CyclotomicField(7)
```



```
def norm_symbol_prime(a, P):
     K = P.number_field()
     zeta = K.gen()
     n = K.zeta_order()
     exponent = (1/n) * ( P.norm() - 1)
     exponent = ZZ(exponent)
     FF = K.residue_field(P)
     aa = FF(a)
     b = FF(a)^exponent
     zeta_mod = FF(zeta)
     # Find power m of zeta_mod that is equal to b, then
     # return zeta^m
     m = 0
     w = FF(1)
     while w != b:
         w = w * zeta_mod
         m += 1
         assert m <= n, "bug in norm_symbol_prime"
     return zeta^m

def norm_symbol(a, b):
     F = K.fractional_ideal([b]).factor()
     return prod([norm_symbol_prime(a, P)^e for P, e in F],
               K(1))
```



```
norm_symbol(zeta^3, 13*zeta)
///
-zeta^5 - zeta^4 - zeta^3 - zeta^2 - zeta - 1
```



```
norm_symbol(zeta^7, K(11))
///
1
```



```
norm_symbol((1+zeta)^2, 23*zeta)
///
zeta^4
```



Issue created by migration from https://trac.sagemath.org/ticket/1359





---

archive/issue_comments_008689.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T20:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8689",
    "user": "@loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_008690.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T20:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8690",
    "user": "@loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_008691.json:
```json
{
    "body": "Please explain what are \"cyclotomic norm residues\".",
    "created_at": "2011-10-09T11:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8691",
    "user": "@jdemeyer"
}
```

Please explain what are "cyclotomic norm residues".



---

archive/issue_comments_008692.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-10-09T11:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8692",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_008693.json:
```json
{
    "body": "Changing keywords from \"\" to \"cyclotomic field\".",
    "created_at": "2014-04-14T20:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8693",
    "user": "@fchapoton"
}
```

Changing keywords from "" to "cyclotomic field".



---

archive/issue_comments_008694.json:
```json
{
    "body": "Here is a git branch. But some of the original tests do not work..\n----\nNew commits:",
    "created_at": "2014-04-14T20:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8694",
    "user": "@fchapoton"
}
```

Here is a git branch. But some of the original tests do not work..
----
New commits:



---

archive/issue_comments_008695.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-18T19:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8695",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008696.json:
```json
{
    "body": "Don't get caught out:\n\n```\nsage: K.<z> = CyclotomicField(7)\nsage: z^7\n1\nsage: z^6\n-z^5 - z^4 - z^3 - z^2 - z - 1\n```\n",
    "created_at": "2014-04-18T21:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8696",
    "user": "@JohnCremona"
}
```

Don't get caught out:

```
sage: K.<z> = CyclotomicField(7)
sage: z^7
1
sage: z^6
-z^5 - z^4 - z^3 - z^2 - z - 1
```




---

archive/issue_comments_008697.json:
```json
{
    "body": "Yes, sure. So indeed the original answers are powers of zeta. But are they correct ?",
    "created_at": "2014-04-19T06:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8697",
    "user": "@fchapoton"
}
```

Yes, sure. So indeed the original answers are powers of zeta. But are they correct ?



---

archive/issue_comments_008698.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-10T16:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8698",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008699.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-05-10T16:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8699",
    "user": "@fchapoton"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_008700.json:
```json
{
    "body": "This should be good. It takes some expert to check the mathematical correctness.",
    "created_at": "2014-05-10T16:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8700",
    "user": "@fchapoton"
}
```

This should be good. It takes some expert to check the mathematical correctness.



---

archive/issue_comments_008701.json:
```json
{
    "body": "This does not merge with 6.3.beta0, probably because of #11670.  Apart from that, the new code is definitely in need of documentation and references (see comment:2).",
    "created_at": "2014-05-11T23:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8701",
    "user": "@pjbruin"
}
```

This does not merge with 6.3.beta0, probably because of #11670.  Apart from that, the new code is definitely in need of documentation and references (see comment:2).



---

archive/issue_comments_008702.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-11T23:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8702",
    "user": "@pjbruin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_008703.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-16T12:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8703",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008704.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-25T19:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8704",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008705.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-01T11:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8705",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008706.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-06-10T18:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8706",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008707.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-08T19:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8707",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008708.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-09-13T18:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8708",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008709.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-08-11T19:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1359",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1359#issuecomment-8709",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:
