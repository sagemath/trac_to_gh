# Issue 9546: bounded outdegree orientation

archive/issues_009546.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  jthurber\n\nGiven a Graph and a value associating an integer b(v) to each vertex v, this method computes an orientation of G such that each vertex has out_degree at most v, if it exists. \n\nThe method is to use a max flow, which is explained in the patch in several lines.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9546\n\n",
    "created_at": "2010-07-19T05:48:54Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "bounded outdegree orientation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9546",
    "user": "ncohen"
}
```
Assignee: jason, ncohen, rlm

CC:  jthurber

Given a Graph and a value associating an integer b(v) to each vertex v, this method computes an orientation of G such that each vertex has out_degree at most v, if it exists. 

The method is to use a max flow, which is explained in the patch in several lines.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9546





---

archive/issue_comments_092017.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-19T05:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92017",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092018.json:
```json
{
    "body": "\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t -long devel/sage-main/sage/graphs/graph.py # 7 doctests failed\n----------------------------------------------------------------------\n```\n\n\nThese all seem to be:\n\n\n```\nNameError: global name 'floor' is not defined\n```\n",
    "created_at": "2011-01-12T03:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92018",
    "user": "rlm"
}
```


```
----------------------------------------------------------------------

The following tests failed:

        sage -t -long devel/sage-main/sage/graphs/graph.py # 7 doctests failed
----------------------------------------------------------------------
```


These all seem to be:


```
NameError: global name 'floor' is not defined
```




---

archive/issue_comments_092019.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-12T03:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92019",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_092020.json:
```json
{
    "body": "Right O_o\n\nThe error comes from the ford_fulkerson algorithm. I replaced \"floor(x)\" by \"x // 1\".\n\nI know I wrote this code myself, but when I looked at it I could only think : why on earth is our implementation of flows in Python and not Cython ? O_o\n\nUpdated ! Sorry for the trouble !\n\nNathann",
    "created_at": "2011-01-12T09:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92020",
    "user": "ncohen"
}
```

Right O_o

The error comes from the ford_fulkerson algorithm. I replaced "floor(x)" by "x // 1".

I know I wrote this code myself, but when I looked at it I could only think : why on earth is our implementation of flows in Python and not Cython ? O_o

Updated ! Sorry for the trouble !

Nathann



---

archive/issue_comments_092021.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-12T09:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92021",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092022.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-12T09:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92022",
    "user": "ncohen"
}
```

Attachment



---

archive/issue_comments_092023.json:
```json
{
    "body": "Using floor division here might be nice, but I'm concerned about the coercion model:\n\n\n```\nsage: 1215.151//1\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/gbe/sage/dev/devel/sage-main/sage/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__floordiv__ (sage/rings/integer.c:11983)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.bin_op (sage/structure/element.c:17928)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.bin_op (sage/structure/element.c:17841)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6213)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6152)()\n\nTypeError: unsupported operand type(s) for //: 'sage.rings.real_mpfr.RealLiteral' and 'sage.rings.real_mpfr.RealNumber'\n```\n\n\nAlso, floor division doesn't seem to buy you any speedup:\n\n```\nsage: tests = [float(random()*10**randint(0,10)) for i in range(10)]\nsage: for i in tests:\n....:     timeit('floor(test)')\n\n625 loops, best of 3: 5.14 \u00b5s per loop\n625 loops, best of 3: 5.12 \u00b5s per loop\n625 loops, best of 3: 5.21 \u00b5s per loop\n625 loops, best of 3: 5.12 \u00b5s per loop\n625 loops, best of 3: 5.12 \u00b5s per loop\n625 loops, best of 3: 5.1 \u00b5s per loop\n625 loops, best of 3: 5.07 \u00b5s per loop\n625 loops, best of 3: 5.2 \u00b5s per loop\n625 loops, best of 3: 5.11 \u00b5s per loop\n625 loops, best of 3: 5.13 \u00b5s per loop\n\nsage: for i in tests:\n....:     timeit('test // 1')\n\n625 loops, best of 3: 9.33 \u00b5s per loop\n625 loops, best of 3: 9.47 \u00b5s per loop\n625 loops, best of 3: 9.4 \u00b5s per loop\n625 loops, best of 3: 9.44 \u00b5s per loop\n625 loops, best of 3: 9.4 \u00b5s per loop\n625 loops, best of 3: 9.4 \u00b5s per loop\n625 loops, best of 3: 9.35 \u00b5s per loop\n625 loops, best of 3: 9.31 \u00b5s per loop\n625 loops, best of 3: 9.3 \u00b5s per loop\n625 loops, best of 3: 9.4 \u00b5s per loop\n```\n\n\nAll in all I think the better solution is to just bring floor(x) into scope from functions/other.py, as I've done in the attached patch.",
    "created_at": "2011-01-12T23:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92023",
    "user": "gbe"
}
```

Using floor division here might be nice, but I'm concerned about the coercion model:


```
sage: 1215.151//1
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/gbe/sage/dev/devel/sage-main/sage/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__floordiv__ (sage/rings/integer.c:11983)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.bin_op (sage/structure/element.c:17928)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.bin_op (sage/structure/element.c:17841)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6213)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6152)()

TypeError: unsupported operand type(s) for //: 'sage.rings.real_mpfr.RealLiteral' and 'sage.rings.real_mpfr.RealNumber'
```


Also, floor division doesn't seem to buy you any speedup:

```
sage: tests = [float(random()*10**randint(0,10)) for i in range(10)]
sage: for i in tests:
....:     timeit('floor(test)')

625 loops, best of 3: 5.14 µs per loop
625 loops, best of 3: 5.12 µs per loop
625 loops, best of 3: 5.21 µs per loop
625 loops, best of 3: 5.12 µs per loop
625 loops, best of 3: 5.12 µs per loop
625 loops, best of 3: 5.1 µs per loop
625 loops, best of 3: 5.07 µs per loop
625 loops, best of 3: 5.2 µs per loop
625 loops, best of 3: 5.11 µs per loop
625 loops, best of 3: 5.13 µs per loop

sage: for i in tests:
....:     timeit('test // 1')

625 loops, best of 3: 9.33 µs per loop
625 loops, best of 3: 9.47 µs per loop
625 loops, best of 3: 9.4 µs per loop
625 loops, best of 3: 9.44 µs per loop
625 loops, best of 3: 9.4 µs per loop
625 loops, best of 3: 9.4 µs per loop
625 loops, best of 3: 9.35 µs per loop
625 loops, best of 3: 9.31 µs per loop
625 loops, best of 3: 9.3 µs per loop
625 loops, best of 3: 9.4 µs per loop
```


All in all I think the better solution is to just bring floor(x) into scope from functions/other.py, as I've done in the attached patch.



---

archive/issue_comments_092024.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-14T21:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92024",
    "user": "jthurber"
}
```

Attachment



---

archive/issue_comments_092025.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-14T21:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92025",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092026.json:
```json
{
    "body": "Attachment\n\napply all three patches",
    "created_at": "2011-01-14T21:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92026",
    "user": "rlm"
}
```

Attachment

apply all three patches



---

archive/issue_comments_092027.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9546#issuecomment-92027",
    "user": "jdemeyer"
}
```

Resolution: fixed
