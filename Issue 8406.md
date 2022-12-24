# Issue 8406: problem with duck typing in c_graph

archive/issues_008406.json:
```json
{
    "body": "Assignee: rlm\n\ntwo examples:\n\n```\nsage: G=Graph()\nsage: R.<a>=GF(3^3)\nsage: G.add_vertex(a^2)\nsage: G.vertices()\n[9]\n```\n\nThis should be `[a]`, but `int(a)=9`\n\n```\nsage: R.<x>=GF(3^3,'a')[]\nsage: G.add_vertex(x)\nValueError\n```\n\nThis should work as `x` is hashable.\n\n`int(x)` return a `ValueError`, but the code only tests for `TypeError`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8406\n\n",
    "created_at": "2010-03-01T08:28:27Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "problem with duck typing in c_graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8406",
    "user": "ylchapuy"
}
```
Assignee: rlm

two examples:

```
sage: G=Graph()
sage: R.<a>=GF(3^3)
sage: G.add_vertex(a^2)
sage: G.vertices()
[9]
```

This should be `[a]`, but `int(a)=9`

```
sage: R.<x>=GF(3^3,'a')[]
sage: G.add_vertex(x)
ValueError
```

This should work as `x` is hashable.

`int(x)` return a `ValueError`, but the code only tests for `TypeError`.

Issue created by migration from https://trac.sagemath.org/ticket/8406





---

archive/issue_comments_075310.json:
```json
{
    "body": "line 638 of c_graph.pyx, we find:\n\n\n```\ntry:\n    u_int = u\nexcept TypeError:\n    return -1\n```\n\n\nI think we should instead do an explicit test:\n\n```\nif isinstance(u,(int,long,Integer))\n```\n\nto avoid coercions.\n\nThoughts?",
    "created_at": "2010-03-01T08:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75310",
    "user": "ylchapuy"
}
```

line 638 of c_graph.pyx, we find:


```
try:
    u_int = u
except TypeError:
    return -1
```


I think we should instead do an explicit test:

```
if isinstance(u,(int,long,Integer))
```

to avoid coercions.

Thoughts?



---

archive/issue_comments_075311.json:
```json
{
    "body": "The only thing I could think of was that maybe this would effect the speed. To benchmark, I tried `g = graphs.CubeGraph(n)` for various `n`, since that calls the relevant function `2^n` times. There was no noticable change at all, so I say we definitely switch. Not to steal author credit, but here's what I tested:\n\n\n```\n-    try:\n+    \n+    if isinstance(u,(int,long,Integer)):\n         u_int = u\n-    except TypeError:\n+    else:\n         return -1\n-    if u_int < 0 or u_int >= G.active_vertices.size:\n-        return -1\n-    if u_int in vertex_labels:\n+    if u_int < 0 or u_int >= G.active_vertices.size or u_int in vertex_labels:\n```\n",
    "created_at": "2010-03-02T07:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75311",
    "user": "rlm"
}
```

The only thing I could think of was that maybe this would effect the speed. To benchmark, I tried `g = graphs.CubeGraph(n)` for various `n`, since that calls the relevant function `2^n` times. There was no noticable change at all, so I say we definitely switch. Not to steal author credit, but here's what I tested:


```
-    try:
+    
+    if isinstance(u,(int,long,Integer)):
         u_int = u
-    except TypeError:
+    else:
         return -1
-    if u_int < 0 or u_int >= G.active_vertices.size:
-        return -1
-    if u_int in vertex_labels:
+    if u_int < 0 or u_int >= G.active_vertices.size or u_int in vertex_labels:
```




---

archive/issue_comments_075312.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-02T08:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75312",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075313.json:
```json
{
    "body": "Attachment [trac_8406.patch](tarball://root/attachments/some-uuid/ticket8406/trac_8406.patch) by ylchapuy created at 2010-03-02 08:53:27",
    "created_at": "2010-03-02T08:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75313",
    "user": "ylchapuy"
}
```

Attachment [trac_8406.patch](tarball://root/attachments/some-uuid/ticket8406/trac_8406.patch) by ylchapuy created at 2010-03-02 08:53:27



---

archive/issue_comments_075314.json:
```json
{
    "body": "Every patch fixing a bug should include a doctest illustrating that bug. Can you make doctests for the two bugs you noted at the top of the page?",
    "created_at": "2010-03-06T21:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75314",
    "user": "rlm"
}
```

Every patch fixing a bug should include a doctest illustrating that bug. Can you make doctests for the two bugs you noted at the top of the page?



---

archive/issue_comments_075315.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-06T21:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75315",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075316.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-09T15:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75316",
    "user": "ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075317.json:
```json
{
    "body": "Attachment [trac_8406-doctests.patch](tarball://root/attachments/some-uuid/ticket8406/trac_8406-doctests.patch) by ylchapuy created at 2010-03-09 15:08:28\n\napply both patches in order.",
    "created_at": "2010-03-09T15:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75317",
    "user": "ylchapuy"
}
```

Attachment [trac_8406-doctests.patch](tarball://root/attachments/some-uuid/ticket8406/trac_8406-doctests.patch) by ylchapuy created at 2010-03-09 15:08:28

apply both patches in order.



---

archive/issue_comments_075318.json:
```json
{
    "body": "Thank you!",
    "created_at": "2010-03-09T16:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75318",
    "user": "rlm"
}
```

Thank you!



---

archive/issue_comments_075319.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-09T16:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75319",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-11T04:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75320",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_075321.json:
```json
{
    "body": "Merged in this order:\n\n1. [trac_8406.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8406/trac_8406.patch)\n2. [trac_8406-doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8406/trac_8406-doctests.patch)",
    "created_at": "2010-03-11T04:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75321",
    "user": "mvngu"
}
```

Merged in this order:

1. [trac_8406.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8406/trac_8406.patch)
2. [trac_8406-doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8406/trac_8406-doctests.patch)



---

archive/issue_comments_075322.json:
```json
{
    "body": "see #9610",
    "created_at": "2010-07-27T12:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8406#issuecomment-75322",
    "user": "rlm"
}
```

see #9610
