# Issue 624: Inplace operators

archive/issues_000624.json:
```json
{
    "body": "Assignee: somebody\n\nDespite the potential speed increase (I've implemented some and it  \ncan be considerable), SAGE has avoided almost all use of inplace  \noperators due to the fact that elements are supposed to be immutable,  \ndespite the fact that one does not really need the \"old\" result  \nanymore. For example, if I type x^5 - 3*x + 1, the subexpressions  \n(x^5), (3*x), and (x^5-3*x) are all created and then discarded. This  \nalso shows up in places like the operation sum() which doesn't return  \nany of its intermediate results, or loops that increment variables in  \ncertain ways. The worry is that perhaps somewhere something else is  \nholding onto a given variable, and we don't want to mess it up.\n\nJust the other day, I realized that Python provides the perfect  \nsolution--by looking at the reference count of an object we can  \ndetect whether or not its safe to mutate it (i.e. nothing else is  \nholding onto it but the current call). If it is safe to mutate, then  \ndo so, otherwise create and return a new object. I propose adding  \n_iadd_c, _imul_c, etc. to the coercion hierarchy such that the  \ndefault __iadd__/__add__ detects whether or not inplace operations  \nare safe and calls the respective operation accordingly. One would  \nhave bold comments on functions that are not safe to call directly.\n\nThe only caveat is that it might make it a tiny bit slower for types  \nthat do not define inplace operations, and it would take a slight  \n(SAGE-specific and optional) tweak to Cython (specifically Cython  \nlocal function variables have a refcount one less than expected due  \nto their not being in any kind of a python \"scope\" container, so we  \nwould need an extra incref/decref them when performing arithmetic on  \nthem).\n\nIssue created by migration from https://trac.sagemath.org/ticket/624\n\n",
    "created_at": "2007-09-07T19:44:53Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "Inplace operators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/624",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

Despite the potential speed increase (I've implemented some and it  
can be considerable), SAGE has avoided almost all use of inplace  
operators due to the fact that elements are supposed to be immutable,  
despite the fact that one does not really need the "old" result  
anymore. For example, if I type x^5 - 3*x + 1, the subexpressions  
(x^5), (3*x), and (x^5-3*x) are all created and then discarded. This  
also shows up in places like the operation sum() which doesn't return  
any of its intermediate results, or loops that increment variables in  
certain ways. The worry is that perhaps somewhere something else is  
holding onto a given variable, and we don't want to mess it up.

Just the other day, I realized that Python provides the perfect  
solution--by looking at the reference count of an object we can  
detect whether or not its safe to mutate it (i.e. nothing else is  
holding onto it but the current call). If it is safe to mutate, then  
do so, otherwise create and return a new object. I propose adding  
_iadd_c, _imul_c, etc. to the coercion hierarchy such that the  
default __iadd__/__add__ detects whether or not inplace operations  
are safe and calls the respective operation accordingly. One would  
have bold comments on functions that are not safe to call directly.

The only caveat is that it might make it a tiny bit slower for types  
that do not define inplace operations, and it would take a slight  
(SAGE-specific and optional) tweak to Cython (specifically Cython  
local function variables have a refcount one less than expected due  
to their not being in any kind of a python "scope" container, so we  
would need an extra incref/decref them when performing arithmetic on  
them).

Issue created by migration from https://trac.sagemath.org/ticket/624





---

archive/issue_comments_003195.json:
```json
{
    "body": "Changing assignee from somebody to @robertwb.",
    "created_at": "2007-09-07T19:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/624#issuecomment-3195",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from somebody to @robertwb.



---

archive/issue_comments_003196.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-07T19:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/624#issuecomment-3196",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003197.json:
```json
{
    "body": "This has been implemented (along with various other coercion optimizations and cleanup). Patch at http://sage.math.washington.edu/home/robertwb/coerce/ with all doctests passing. The new cython spkg in that folder MUST be installed as well, with a sage -ba. \n\nInplace operations only defined for ZZ, QQ, RDF, and a couple of others (a bit in laurent/power series, generic polynomials)\n\nDownload and try it out.",
    "created_at": "2007-09-12T04:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/624#issuecomment-3197",
    "user": "https://github.com/robertwb"
}
```

This has been implemented (along with various other coercion optimizations and cleanup). Patch at http://sage.math.washington.edu/home/robertwb/coerce/ with all doctests passing. The new cython spkg in that folder MUST be installed as well, with a sage -ba. 

Inplace operations only defined for ZZ, QQ, RDF, and a couple of others (a bit in laurent/power series, generic polynomials)

Download and try it out.



---

archive/issue_comments_003198.json:
```json
{
    "body": "Without inplace operators:\n\n```\nsage: A = [Integer(n) for n in range(10^6)]\nsage: %time\nsage: time sum(A)\n499999500000\nCPU time: 0.26 s,  Wall time: 0.26 s\n\nsage: E = EllipticCurve('37a').change_ring(GF(5^6, 'a'))\nsage: P = E(0,0)\nsage: %time\nsage: for i in range(1000):\n...       Q = i*P\nCPU time: 1.46 s,  Wall time: 1.46 s\n\nsage: %cython\nsage: def get_address(o):\n...       return <Py_ssize_t>o\nsage: a = 20\nsage: get_address(a)\n278949184\nsage: a += 10\nsage: get_address(a)\n190804384\nsage: b = a\nsage: a += 10\nsage: get_address(a)\n278947360\nsage: del b\nsage: a += 10\nsage: get_address(a)\n278949184\n```\n",
    "created_at": "2007-09-13T18:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/624#issuecomment-3198",
    "user": "https://github.com/robertwb"
}
```

Without inplace operators:

```
sage: A = [Integer(n) for n in range(10^6)]
sage: %time
sage: time sum(A)
499999500000
CPU time: 0.26 s,  Wall time: 0.26 s

sage: E = EllipticCurve('37a').change_ring(GF(5^6, 'a'))
sage: P = E(0,0)
sage: %time
sage: for i in range(1000):
...       Q = i*P
CPU time: 1.46 s,  Wall time: 1.46 s

sage: %cython
sage: def get_address(o):
...       return <Py_ssize_t>o
sage: a = 20
sage: get_address(a)
278949184
sage: a += 10
sage: get_address(a)
190804384
sage: b = a
sage: a += 10
sage: get_address(a)
278947360
sage: del b
sage: a += 10
sage: get_address(a)
278949184
```




---

archive/issue_comments_003199.json:
```json
{
    "body": "With inplace operators: \n\n\n```\nsage: A = [Integer(n) for n in range(10^6)]\nsage: %time\nsage: sum(A)    # Note: I did not edit the sum function at all, just __add__\n499999500000\nCPU time: 0.11 s,  Wall time: 0.12 s\n\nsage: E = EllipticCurve('37a').change_ring(GF(5^6, 'a'))\nsage: P = E(0,0)\nsage: %time\nsage: for i in range(1000):\n...       Q = i*P\nCPU time: 0.28 s,  Wall time: 0.29 s\n\nsage: %cython\nsage: def get_address(o):\n...       return <Py_ssize_t>o\nsage: a = 20\nsage: get_address(a)\n343719648\nsage: a += 10\nsage: get_address(a)  # same as above => mutated\n343719648\nsage: b = a\nsage: a += 10\nsage: get_address(a)  # not mutated because we can still access the integer via b\n343719584\nsage: b = a\nsage: del b\nsage: a += 10\nsage: get_address(a)  # after b is gone, it is safe to mutate\n343719584\n```\n",
    "created_at": "2007-09-13T19:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/624#issuecomment-3199",
    "user": "https://github.com/robertwb"
}
```

With inplace operators: 


```
sage: A = [Integer(n) for n in range(10^6)]
sage: %time
sage: sum(A)    # Note: I did not edit the sum function at all, just __add__
499999500000
CPU time: 0.11 s,  Wall time: 0.12 s

sage: E = EllipticCurve('37a').change_ring(GF(5^6, 'a'))
sage: P = E(0,0)
sage: %time
sage: for i in range(1000):
...       Q = i*P
CPU time: 0.28 s,  Wall time: 0.29 s

sage: %cython
sage: def get_address(o):
...       return <Py_ssize_t>o
sage: a = 20
sage: get_address(a)
343719648
sage: a += 10
sage: get_address(a)  # same as above => mutated
343719648
sage: b = a
sage: a += 10
sage: get_address(a)  # not mutated because we can still access the integer via b
343719584
sage: b = a
sage: del b
sage: a += 10
sage: get_address(a)  # after b is gone, it is safe to mutate
343719584
```




---

archive/issue_comments_003200.json:
```json
{
    "body": "Another example without\n\n\n```\nsage: R.<t> = ZZ[]\nsage: S.<x> = LaurentSeriesRing(R)\nsage: type(x)\n<type 'sage.rings.laurent_series_ring_element.LaurentSeries'>\nsage: %time\nsage: for _ in range(1000):\n...       f = x^3 - t*x^2 + x\nCPU time: 1.42 s,  Wall time: 1.43 s\n```\n\n\nand with\n\n\n```\nsage: R.<t> = ZZ[]\nsage: S.<x> = LaurentSeriesRing(R)\nsage: type(x)\n<type 'sage.rings.laurent_series_ring_element.LaurentSeries'>\nsage: %time\nsage: for _ in range(1000):\n...       f = x^3 - t*x^2 + x\nCPU time: 0.88 s,  Wall time: 0.88 s\n```\n",
    "created_at": "2007-09-13T19:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/624#issuecomment-3200",
    "user": "https://github.com/robertwb"
}
```

Another example without


```
sage: R.<t> = ZZ[]
sage: S.<x> = LaurentSeriesRing(R)
sage: type(x)
<type 'sage.rings.laurent_series_ring_element.LaurentSeries'>
sage: %time
sage: for _ in range(1000):
...       f = x^3 - t*x^2 + x
CPU time: 1.42 s,  Wall time: 1.43 s
```


and with


```
sage: R.<t> = ZZ[]
sage: S.<x> = LaurentSeriesRing(R)
sage: type(x)
<type 'sage.rings.laurent_series_ring_element.LaurentSeries'>
sage: %time
sage: for _ in range(1000):
...       f = x^3 - t*x^2 + x
CPU time: 0.88 s,  Wall time: 0.88 s
```




---

archive/issue_comments_003201.json:
```json
{
    "body": "I believe this ticket can be closed because it seems to be included in the new coerce framework which has been merged.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-19T18:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/624#issuecomment-3201",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I believe this ticket can be closed because it seems to be included in the new coerce framework which has been merged.

Cheers,

Michael



---

archive/issue_events_000682.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T02:25:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/624",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/624#event-682"
}
```



---

archive/issue_comments_003202.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T02:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/624#issuecomment-3202",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
