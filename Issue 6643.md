# Issue 6643: vector function changes the ring of a vector for ZZ when possible

archive/issues_006643.json:
```json
{
    "body": "Assignee: slabbe\n\nThe following works fine, i.e vector function doesn't change the ring of the input vector :\n\n\n```\nsage: K.<sqrt3> = QuadraticField(3); K\nNumber Field in sqrt3 with defining polynomial x^2 - 3\nsage: v = vector(K, (1/2, sqrt3/2) ); v\n(1/2, 1/2*sqrt3)\nsage: v.parent()\nVector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3\nsage: vector(v).parent()\nVector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3\n```\n\n\nFor rationals coordinates, it is also OK :\n\n\n```\nsage: v2 = vector(K, (1/2, 3/2) ); v2\n(1/2, 3/2)\nsage: v2.parent()\nVector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3\nsage: vector(v2).parent()\nVector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3\n```\n\n\nBut, for integers, it changes the ring for ZZ :\n\n\n```\nsage: v3 = vector(K, (0, 1) )\nsage: v3.parent()\nVector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3\nsage: vector(v3).parent()\nAmbient free module of rank 2 over the principal ideal domain Integer Ring\n```\n\n\nwhich I doesn't like because I want to be able to add them (the addition of those vector appears to be unsupported yet by the coercion system...this could be another ticket...) :\n\n\n```\nsage: v + v3\n(1/2, 1/2*sqrt3 + 1)\nsage: vector(v) + vector(v3)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1052, 0))\n\nTraceback (most recent call last):\n...\n/home/slabbe/sage-4.1/local/lib/python2.6/site-packages/sage/modules/free_module.pyc in __cmp__(self, other)\n   3806             if not c: return c\n   3807             try:\n-> 3808                 if self.base_ring().is_subring(other.base_ring()):\n   3809                     return -1\n   3810                 elif other.base_ring().is_subring(self.base_ring()):\n\n/home/slabbe/sage-4.1/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.is_subring (sage/rings/ring.c:4724)()\n\nAttributeError: 'NotImplementedType' object has no attribute 'natural_map'\n```\n\n\nI will also ask on sage-devel if there is a reason why the vector function changes the ring of a vector for ZZ when possible.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6643\n\n",
    "created_at": "2009-07-27T19:40:35Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "vector function changes the ring of a vector for ZZ when possible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6643",
    "user": "slabbe"
}
```
Assignee: slabbe

The following works fine, i.e vector function doesn't change the ring of the input vector :


```
sage: K.<sqrt3> = QuadraticField(3); K
Number Field in sqrt3 with defining polynomial x^2 - 3
sage: v = vector(K, (1/2, sqrt3/2) ); v
(1/2, 1/2*sqrt3)
sage: v.parent()
Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3
sage: vector(v).parent()
Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3
```


For rationals coordinates, it is also OK :


```
sage: v2 = vector(K, (1/2, 3/2) ); v2
(1/2, 3/2)
sage: v2.parent()
Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3
sage: vector(v2).parent()
Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3
```


But, for integers, it changes the ring for ZZ :


```
sage: v3 = vector(K, (0, 1) )
sage: v3.parent()
Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3
sage: vector(v3).parent()
Ambient free module of rank 2 over the principal ideal domain Integer Ring
```


which I doesn't like because I want to be able to add them (the addition of those vector appears to be unsupported yet by the coercion system...this could be another ticket...) :


```
sage: v + v3
(1/2, 1/2*sqrt3 + 1)
sage: vector(v) + vector(v3)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1052, 0))

Traceback (most recent call last):
...
/home/slabbe/sage-4.1/local/lib/python2.6/site-packages/sage/modules/free_module.pyc in __cmp__(self, other)
   3806             if not c: return c
   3807             try:
-> 3808                 if self.base_ring().is_subring(other.base_ring()):
   3809                     return -1
   3810                 elif other.base_ring().is_subring(self.base_ring()):

/home/slabbe/sage-4.1/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.is_subring (sage/rings/ring.c:4724)()

AttributeError: 'NotImplementedType' object has no attribute 'natural_map'
```


I will also ask on sage-devel if there is a reason why the vector function changes the ring of a vector for ZZ when possible.

Issue created by migration from https://trac.sagemath.org/ticket/6643





---

archive/issue_comments_054482.json:
```json
{
    "body": "Attachment\n\nApplies on sage-4.1",
    "created_at": "2009-07-27T19:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6643#issuecomment-54482",
    "user": "slabbe"
}
```

Attachment

Applies on sage-4.1



---

archive/issue_comments_054483.json:
```json
{
    "body": "I posted my question on sage-devel :\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/dc142746f1aa8175",
    "created_at": "2009-07-27T20:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6643#issuecomment-54483",
    "user": "slabbe"
}
```

I posted my question on sage-devel :

http://groups.google.com/group/sage-devel/browse_thread/thread/dc142746f1aa8175



---

archive/issue_comments_054484.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-27T20:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6643#issuecomment-54484",
    "user": "slabbe"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054485.json:
```json
{
    "body": "Changing keywords from \"\" to \"vector\".",
    "created_at": "2009-07-27T20:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6643#issuecomment-54485",
    "user": "slabbe"
}
```

Changing keywords from "" to "vector".



---

archive/issue_comments_054486.json:
```json
{
    "body": "Performs as advertised, passes all tests, documentation builds without warnings.\n\nPositive review.",
    "created_at": "2009-08-17T06:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6643#issuecomment-54486",
    "user": "rbeezer"
}
```

Performs as advertised, passes all tests, documentation builds without warnings.

Positive review.



---

archive/issue_comments_054487.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T01:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6643",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6643#issuecomment-54487",
    "user": "mvngu"
}
```

Resolution: fixed
