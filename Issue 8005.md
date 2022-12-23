# Issue 8005: powers of elements in a QuotientRing

archive/issues_008005.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nReported by Ronald van Luijk:\n\nThe following seems inconsistent:\n\n\n```\nsage: F = GF(5)\nsage: R.<x,y>=F[]\nsage: I=Ideal(R, [x, y])\nsage: S.<x1,y1>=QuotientRing(R,I)\nsage: print x1^2\nx1^2\nsage: print x1^3\nx1^3\nsage: print (x1^2)^2\nx1^4\nsage: print x1^4\nNotImplementedError\n```\n\n\nThe traceback is:\n\n\n```\nNotImplementedError                       Traceback (most recent call last)\n\n/home/wjp/.sage/<ipython console> in <module>()\n\n/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__pow__ (sage/structure/element.c:10708)()\n\n/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.generic_power_c (sage/structure/element.c:22501)()\n\n/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:6516)()\n\n/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:6398)()\n\n/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/rings/quotient_ring_element.pyc in __cmp__(self, other)\n    463             1\n    464         \"\"\"\n--> 465         if self.__rep == other.__rep or ((self.__rep - other.__rep) in self.parent().defining_ideal()):\n    466             return 0\n    467         return cmp(self.__rep, other.__rep)\n\n/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/rings/ideal.pyc in __contains__(self, x)\n    260     def __contains__(self, x):\n    261         try:\n--> 262             return self._contains_(self.__ring(x))\n    263         except TypeError:\n    264             return False\n\n/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/rings/ideal.pyc in _contains_(self, x)\n    266     def _contains_(self, x):\n    267         # check if x, which is assumed to be in the ambient ring, is actually in this ideal.\n--> 268         raise NotImplementedError\n    269 \n    270     def __nonzero__(self):\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8005\n\n",
    "created_at": "2010-01-19T23:56:52Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "powers of elements in a QuotientRing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8005",
    "user": "wjp"
}
```
Assignee: AlexGhitza

Reported by Ronald van Luijk:

The following seems inconsistent:


```
sage: F = GF(5)
sage: R.<x,y>=F[]
sage: I=Ideal(R, [x, y])
sage: S.<x1,y1>=QuotientRing(R,I)
sage: print x1^2
x1^2
sage: print x1^3
x1^3
sage: print (x1^2)^2
x1^4
sage: print x1^4
NotImplementedError
```


The traceback is:


```
NotImplementedError                       Traceback (most recent call last)

/home/wjp/.sage/<ipython console> in <module>()

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__pow__ (sage/structure/element.c:10708)()

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.generic_power_c (sage/structure/element.c:22501)()

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:6516)()

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:6398)()

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/rings/quotient_ring_element.pyc in __cmp__(self, other)
    463             1
    464         """
--> 465         if self.__rep == other.__rep or ((self.__rep - other.__rep) in self.parent().defining_ideal()):
    466             return 0
    467         return cmp(self.__rep, other.__rep)

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/rings/ideal.pyc in __contains__(self, x)
    260     def __contains__(self, x):
    261         try:
--> 262             return self._contains_(self.__ring(x))
    263         except TypeError:
    264             return False

/data/sage/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/rings/ideal.pyc in _contains_(self, x)
    266     def _contains_(self, x):
    267         # check if x, which is assumed to be in the ambient ring, is actually in this ideal.
--> 268         raise NotImplementedError
    269 
    270     def __nonzero__(self):
```


Issue created by migration from https://trac.sagemath.org/ticket/8005





---

archive/issue_comments_069951.json:
```json
{
    "body": "This bug no longer exists. Let's close this ticket",
    "created_at": "2013-01-27T08:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8005#issuecomment-69951",
    "user": "Bouillaguet"
}
```

This bug no longer exists. Let's close this ticket



---

archive/issue_comments_069952.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-27T08:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8005#issuecomment-69952",
    "user": "Bouillaguet"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069953.json:
```json
{
    "body": "This is with Sage 5.7beta0 where everything seems to work as expected:\n\n```\nsage: F = GF(5)\nsage: R.<x,y>=F[]\nsage: I=Ideal(R, [x, y])\nsage: S.<x1,y1>=QuotientRing(R,I)\nsage: print x1^2\n0\nsage: print (x1^2)^2\n0\nsage: print x1^4\n0\nsage: print x1\n0\nsage: S\nQuotient of Multivariate Polynomial Ring in x, y over Finite Field of size 5 by the ideal (x, y)\n```\n\nI wouldn't know how to create a meaningful doctest for this problem, so I'm giving the 'wontfix' a positive review.",
    "created_at": "2013-01-27T09:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8005#issuecomment-69953",
    "user": "cnassau"
}
```

This is with Sage 5.7beta0 where everything seems to work as expected:

```
sage: F = GF(5)
sage: R.<x,y>=F[]
sage: I=Ideal(R, [x, y])
sage: S.<x1,y1>=QuotientRing(R,I)
sage: print x1^2
0
sage: print (x1^2)^2
0
sage: print x1^4
0
sage: print x1
0
sage: S
Quotient of Multivariate Polynomial Ring in x, y over Finite Field of size 5 by the ideal (x, y)
```

I wouldn't know how to create a meaningful doctest for this problem, so I'm giving the 'wontfix' a positive review.



---

archive/issue_comments_069954.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-27T09:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8005#issuecomment-69954",
    "user": "cnassau"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069955.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-01-31T20:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8005#issuecomment-69955",
    "user": "jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_comments_069956.json:
```json
{
    "body": "Changing assignee from AlexGhitza to mjo.",
    "created_at": "2014-10-28T13:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8005#issuecomment-69956",
    "user": "mjo"
}
```

Changing assignee from AlexGhitza to mjo.



---

archive/issue_comments_069957.json:
```json
{
    "body": "Huh. This has been on my TODO list for quite a while I guess! It looks like this was fixed as part of #9138.\n\nI've added a doctest for it, and cleaned up a little.\n----\nNew commits:",
    "created_at": "2014-10-28T13:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8005#issuecomment-69957",
    "user": "mjo"
}
```

Huh. This has been on my TODO list for quite a while I guess! It looks like this was fixed as part of #9138.

I've added a doctest for it, and cleaned up a little.
----
New commits:



---

archive/issue_comments_069958.json:
```json
{
    "body": "Aaaannd I can't reopen the ticket. Sorry for the noise.",
    "created_at": "2014-10-28T14:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8005",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8005#issuecomment-69958",
    "user": "mjo"
}
```

Aaaannd I can't reopen the ticket. Sorry for the noise.
