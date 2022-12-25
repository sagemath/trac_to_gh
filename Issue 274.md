# Issue 274: memory leak --- Polynomial arithmetic over finite field

archive/issues_000274.json:
```json
{
    "body": "Assignee: @williamstein\n\nLeaks like a bad ...\n\n\n```\n\nsage: get_memory_usage()\n'276M'\nsage: K = GF(10007^2, 'a')\nsage: X = PolynomialRing(K, 'x').gen()\nsage: for i in range(1000):\n    s = K.random_element(); t = K.random_element()\n    poly = s + t*X\n....:     \nsage: get_memory_usage()\n'281M'\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/274\n\n",
    "created_at": "2007-02-21T08:50:03Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "memory leak --- Polynomial arithmetic over finite field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/274",
    "user": "https://trac.sagemath.org/admin/accounts/users/ifti"
}
```
Assignee: @williamstein

Leaks like a bad ...


```

sage: get_memory_usage()
'276M'
sage: K = GF(10007^2, 'a')
sage: X = PolynomialRing(K, 'x').gen()
sage: for i in range(1000):
    s = K.random_element(); t = K.random_element()
    poly = s + t*X
....:     
sage: get_memory_usage()
'281M'

```


Issue created by migration from https://trac.sagemath.org/ticket/274





---

archive/issue_comments_001296.json:
```json
{
    "body": "This much simpler example also leaks:\n\n```\nsage: K = GF(10007^2, 'a')\nsage: X = PolynomialRing(K, 'x').gen()\nsage: s = K.random_element(); t = K.random_element()\nsage: for i in range(1000):\n    _ = t*X\n```\n",
    "created_at": "2007-08-18T16:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/274#issuecomment-1296",
    "user": "https://github.com/williamstein"
}
```

This much simpler example also leaks:

```
sage: K = GF(10007^2, 'a')
sage: X = PolynomialRing(K, 'x').gen()
sage: s = K.random_element(); t = K.random_element()
sage: for i in range(1000):
    _ = t*X
```




---

archive/issue_comments_001297.json:
```json
{
    "body": "\n```\n09:10 < was_> the problem is also *only* over GF(10007^2)\n09:10 < was_> not over GF(10007)\n09:10 < was_> so it's givaro, probably.\n```\n",
    "created_at": "2007-08-18T16:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/274#issuecomment-1297",
    "user": "https://github.com/williamstein"
}
```


```
09:10 < was_> the problem is also *only* over GF(10007^2)
09:10 < was_> not over GF(10007)
09:10 < was_> so it's givaro, probably.
```




---

archive/issue_comments_001298.json:
```json
{
    "body": "Not givaro, pari:\n\nsage: K = GF(10007^2, 'a')\nsage: type(K)\n<class 'sage.rings.finite_field.FiniteField_ext_pari'>",
    "created_at": "2007-08-18T16:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/274#issuecomment-1298",
    "user": "https://github.com/williamstein"
}
```

Not givaro, pari:

sage: K = GF(10007^2, 'a')
sage: type(K)
<class 'sage.rings.finite_field.FiniteField_ext_pari'>



---

archive/issue_comments_001299.json:
```json
{
    "body": "The problem is in polynomial creation.\n\n\n```\nK = GF(2^16, 'a')\nprint type(K)\nR.<x> = K[]\nprint type(R)\ns = K.random_element()\n\ndef leak(n):\n    m = get_memory_usage()\n    for i in range(n):\n        _ = R([1])\n    print get_memory_usage() - m\n\nleak(10000)\n```\n",
    "created_at": "2007-08-18T20:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/274#issuecomment-1299",
    "user": "https://github.com/williamstein"
}
```

The problem is in polynomial creation.


```
K = GF(2^16, 'a')
print type(K)
R.<x> = K[]
print type(R)
s = K.random_element()

def leak(n):
    m = get_memory_usage()
    for i in range(n):
        _ = R([1])
    print get_memory_usage() - m

leak(10000)
```




---

archive/issue_events_000612.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-18T21:21:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/274",
    "milestone": "sage-2.8.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/274#event-612"
}
```



---

archive/issue_comments_001300.json:
```json
{
    "body": "after much hunting, the bug appears to be in PARI gen __bool__ method, which currently is implemented as:\n\n\n```\ndef __bool__(gen self):\n   _sig_on\n   t = bool(self.g != stoi(0))\n   _sig_off\n   return t\n```\n\n\nwhich doesn't make a whole lot of sense.",
    "created_at": "2007-08-18T21:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/274#issuecomment-1300",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

after much hunting, the bug appears to be in PARI gen __bool__ method, which currently is implemented as:


```
def __bool__(gen self):
   _sig_on
   t = bool(self.g != stoi(0))
   _sig_off
   return t
```


which doesn't make a whole lot of sense.



---

archive/issue_comments_001301.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2007-08-19T01:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/274#issuecomment-1301",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to critical.



---

archive/issue_comments_001302.json:
```json
{
    "body": "This is really a symptom of some sort of much more general memory leak problem in the PARI C library interface, as the following bizarre example illustrates:\n\n\n```\nsage: n = pari('x')\nsage: m = pari(0)\nsage: s = get_memory_usage()\nsage: for i in range(2*10^5):\n...       _ = pari(0)\n...\nsage: print get_memory_usage() - s\n0.0\nsage: n = pari('x')\nsage: m = pari(0)\nsage: s = get_memory_usage()\nsage: for i in range(2*10^5):\n...       _ = n == m\n...\nsage: print get_memory_usage() - s\n0.0\nsage: n = pari('x')\nsage: m = pari(0)\nsage: s = get_memory_usage()\nsage: for i in range(2*10^5):\n...       _ = n == pari(0)\n...\nsage: print get_memory_usage() - s\n10.87109375\n```\n",
    "created_at": "2007-08-19T05:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/274#issuecomment-1302",
    "user": "https://github.com/williamstein"
}
```

This is really a symptom of some sort of much more general memory leak problem in the PARI C library interface, as the following bizarre example illustrates:


```
sage: n = pari('x')
sage: m = pari(0)
sage: s = get_memory_usage()
sage: for i in range(2*10^5):
...       _ = pari(0)
...
sage: print get_memory_usage() - s
0.0
sage: n = pari('x')
sage: m = pari(0)
sage: s = get_memory_usage()
sage: for i in range(2*10^5):
...       _ = n == m
...
sage: print get_memory_usage() - s
0.0
sage: n = pari('x')
sage: m = pari(0)
sage: s = get_memory_usage()
sage: for i in range(2*10^5):
...       _ = n == pari(0)
...
sage: print get_memory_usage() - s
10.87109375
```




---

archive/issue_comments_001303.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T08:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/274",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/274#issuecomment-1303",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000613.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-19T08:28:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/274",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/274#event-613"
}
```
