# Issue 344: pari compare fails for some finite field elements

archive/issues_000344.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n# setup\nf = conway_polynomial(2,63)\nK.<a> = GF(2**63, name='a', modulus=f)\nn = f.degree()\nm = 3;\ne = (2^n - 1) / (2^m - 1)\nc = a^e\nconway = conway_polynomial(2,m)\n```\n\n\n\n```\n# element 1\nprint conway(c)   # says 0\nprint type(c)\nprint parent(c)\nprint c in K          # says True\n```\n\n\n\n```\n# element 2\nprint K(0)      # says 0\nprint type(K(0))\nprint parent(K(0))\n```\n\n\n\n```\nprint conway(c) == K(0)    # says False???\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/344\n\n",
    "created_at": "2007-04-03T11:33:12Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "pari compare fails for some finite field elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/344",
    "user": "https://github.com/malb"
}
```
Assignee: somebody


```
# setup
f = conway_polynomial(2,63)
K.<a> = GF(2**63, name='a', modulus=f)
n = f.degree()
m = 3;
e = (2^n - 1) / (2^m - 1)
c = a^e
conway = conway_polynomial(2,m)
```



```
# element 1
print conway(c)   # says 0
print type(c)
print parent(c)
print c in K          # says True
```



```
# element 2
print K(0)      # says 0
print type(K(0))
print parent(K(0))
```



```
print conway(c) == K(0)    # says False???
```


Issue created by migration from https://trac.sagemath.org/ticket/344





---

archive/issue_comments_001672.json:
```json
{
    "body": "More details:\n\n```\ne1 = conway(c)\ne2 = K(0)\ne1p = e1._FiniteField_ext_pariElement__value\ne2p = e2._FiniteField_ext_pariElement__value\ne1p._cmp(e2p)\n<class 'gen.PariError'>                   Traceback (most recent call last)\n/home/malb/<ipython console> in <module>()\n/home/malb/gen.pyx in gen._pari_trap()\n<class 'gen.PariError'>: incorrect type (20)\n```\n",
    "created_at": "2007-04-03T11:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/344#issuecomment-1672",
    "user": "https://github.com/malb"
}
```

More details:

```
e1 = conway(c)
e2 = K(0)
e1p = e1._FiniteField_ext_pariElement__value
e2p = e2._FiniteField_ext_pariElement__value
e1p._cmp(e2p)
<class 'gen.PariError'>                   Traceback (most recent call last)
/home/malb/<ipython console> in <module>()
/home/malb/gen.pyx in gen._pari_trap()
<class 'gen.PariError'>: incorrect type (20)
```




---

archive/issue_events_000368.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-08-14T07:48:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/344",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/344#event-368"
}
```



---

archive/issue_comments_001673.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-14T07:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/344#issuecomment-1673",
    "user": "https://github.com/malb"
}
```

Resolution: fixed



---

archive/issue_comments_001674.json:
```json
{
    "body": "Fixed for 2.8.1.",
    "created_at": "2007-08-14T07:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/344",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/344#issuecomment-1674",
    "user": "https://github.com/malb"
}
```

Fixed for 2.8.1.
