# Issue 2768: add comparison operators to the fast_float mechanism

archive/issues_002768.json:
```json
{
    "body": "Assignee: @williamstein\n\nmake it so that comparisons work too: return 0.0 if false, 1.0 if true.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2768\n\n",
    "created_at": "2008-04-02T05:47:22Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "add comparison operators to the fast_float mechanism",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2768",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

make it so that comparisons work too: return 0.0 if false, 1.0 if true.

Issue created by migration from https://trac.sagemath.org/ticket/2768





---

archive/issue_comments_018973.json:
```json
{
    "body": "Some timings:\n\noriginal\n\n```\nsage: var('x y')\n(x, y)\nsage: eq=x<y\nsage: %timeit eq(x=2, y=3)\n10 loops, best of 3: 54.6 \u00b5s per loop\n```\n\nfast_float (after applying patch)\n\n```\nsage: var('x y')\n(x, y)\nsage: eq=x<y\nsage: f=eq._fast_float_('x','y')\nsage: %timeit f(2,3)\n1000000 loops, best of 3: 422 ns per loop\n```\nand even with the overhead of converting back to bool\n\n```\nsage: %timeit bool(f(2,3))\n1000000 loops, best of 3: 721 ns per loop\n```",
    "created_at": "2008-04-02T06:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18973",
    "user": "https://github.com/jasongrout"
}
```

Some timings:

original

```
sage: var('x y')
(x, y)
sage: eq=x<y
sage: %timeit eq(x=2, y=3)
10 loops, best of 3: 54.6 µs per loop
```

fast_float (after applying patch)

```
sage: var('x y')
(x, y)
sage: eq=x<y
sage: f=eq._fast_float_('x','y')
sage: %timeit f(2,3)
1000000 loops, best of 3: 422 ns per loop
```
and even with the overhead of converting back to bool

```
sage: %timeit bool(f(2,3))
1000000 loops, best of 3: 721 ns per loop
```



---

archive/issue_comments_018974.json:
```json
{
    "body": "One more comparison:\n\n```\nsage: var('x y')\n(x, y)\nsage: x._fast_float_('x')\n<sage.ext.fast_eval.FastDoubleFunc object at 0xa02a95c>\nsage: f=x._fast_float_('x')\nsage: g=y._fast_float_('y')\nsage: f(2)<g(3)\nTrue\nsage: %timeit f(2)<g(3)\n1000000 loops, best of 3: 723 ns per loop\n```\n\nSo this could have been implemented without touching the fast_float code.  However, if I want just the floating point 0.0 and 1.0 values, this patch still wins.",
    "created_at": "2008-04-02T06:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18974",
    "user": "https://github.com/jasongrout"
}
```

One more comparison:

```
sage: var('x y')
(x, y)
sage: x._fast_float_('x')
<sage.ext.fast_eval.FastDoubleFunc object at 0xa02a95c>
sage: f=x._fast_float_('x')
sage: g=y._fast_float_('y')
sage: f(2)<g(3)
True
sage: %timeit f(2)<g(3)
1000000 loops, best of 3: 723 ns per loop
```

So this could have been implemented without touching the fast_float code.  However, if I want just the floating point 0.0 and 1.0 values, this patch still wins.



---

archive/issue_comments_018975.json:
```json
{
    "body": "More timings:\n\n```\nsage: sage: var('x y')\n(x, y)\nsage: sage: eq=x<y\nsage: sage: f=eq._fast_float_('x','y')\nsage: sage: %timeit f(2,3)\n1000000 loops, best of 3: 438 ns per loop\nsage: xin=RDF(2); yin=RDF(2)\nsage: sage: %timeit f(xin,yin)\n1000000 loops, best of 3: 499 ns per loop\nsage: xin=float(2); yin=float(2);\nsage: sage: %timeit f(xin,yin)\n1000000 loops, best of 3: 389 ns per loop\n```",
    "created_at": "2008-04-02T06:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18975",
    "user": "https://github.com/jasongrout"
}
```

More timings:

```
sage: sage: var('x y')
(x, y)
sage: sage: eq=x<y
sage: sage: f=eq._fast_float_('x','y')
sage: sage: %timeit f(2,3)
1000000 loops, best of 3: 438 ns per loop
sage: xin=RDF(2); yin=RDF(2)
sage: sage: %timeit f(xin,yin)
1000000 loops, best of 3: 499 ns per loop
sage: xin=float(2); yin=float(2);
sage: sage: %timeit f(xin,yin)
1000000 loops, best of 3: 389 ns per loop
```



---

archive/issue_comments_018976.json:
```json
{
    "body": "Attachment [trac-2768-fast-float-cmp.patch](tarball://root/attachments/some-uuid/ticket2768/trac-2768-fast-float-cmp.patch) by @jasongrout created at 2008-04-02 06:53:15",
    "created_at": "2008-04-02T06:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18976",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-2768-fast-float-cmp.patch](tarball://root/attachments/some-uuid/ticket2768/trac-2768-fast-float-cmp.patch) by @jasongrout created at 2008-04-02 06:53:15



---

archive/issue_comments_018977.json:
```json
{
    "body": "For a nice example of this patch being used, see #2770.",
    "created_at": "2008-04-02T08:04:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18977",
    "user": "https://github.com/jasongrout"
}
```

For a nice example of this patch being used, see #2770.



---

archive/issue_comments_018978.json:
```json
{
    "body": "The code is nice and clean, but I don't think it should be applied. Expressions and equations are not interchangeable, and this can lead to some strange results. \n\n```\nsage: f = (x == 1)\nsage: g = (1 == x)\nsage: bool(f+g)\nTrue\nsage: ff = f._fast_float_('x') + g._fast_float_('x')\nsage: ff(0)\n0.0\nsage: ff(1)\n2.0\nsage: ff(2)\n0.0\nsage: list(ff)\n['load 0', 'push 1.0', 'eq', 'push 1.0', 'load 0', 'eq', 'add']\n```\n\nReally, I think what should be implemented is piecewise functions for fast float, which would allow one to do things like #2770 nicely. One could also create a specialized wrapper that could handle the semantics of the two sides of the equations correctly (and maybe even do short-circuiting on the first false expression).",
    "created_at": "2008-04-02T17:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18978",
    "user": "https://github.com/robertwb"
}
```

The code is nice and clean, but I don't think it should be applied. Expressions and equations are not interchangeable, and this can lead to some strange results. 

```
sage: f = (x == 1)
sage: g = (1 == x)
sage: bool(f+g)
True
sage: ff = f._fast_float_('x') + g._fast_float_('x')
sage: ff(0)
0.0
sage: ff(1)
2.0
sage: ff(2)
0.0
sage: list(ff)
['load 0', 'push 1.0', 'eq', 'push 1.0', 'load 0', 'eq', 'add']
```

Really, I think what should be implemented is piecewise functions for fast float, which would allow one to do things like #2770 nicely. One could also create a specialized wrapper that could handle the semantics of the two sides of the equations correctly (and maybe even do short-circuiting on the first false expression).



---

archive/issue_comments_018979.json:
```json
{
    "body": "What's happening with this ticket? It's been asleep for a month. Is there still further discussion, or is that code being withdrawn?",
    "created_at": "2008-05-01T06:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18979",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

What's happening with this ticket? It's been asleep for a month. Is there still further discussion, or is that code being withdrawn?



---

archive/issue_comments_018980.json:
```json
{
    "body": "I've been busy and it's still on my todo list.  If someone wants to take it up, feel free.  Robert Bradshaw and I agreed on a compromise on sage-devel.",
    "created_at": "2008-05-01T12:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18980",
    "user": "https://github.com/jasongrout"
}
```

I've been busy and it's still on my todo list.  If someone wants to take it up, feel free.  Robert Bradshaw and I agreed on a compromise on sage-devel.



---

archive/issue_comments_018981.json:
```json
{
    "body": "See http://groups.google.com/group/sage-devel/browse_thread/thread/861d35160afebfe6/14226ae55d50b7be?lnk=gst&q=fast_float#14226ae55d50b7be for Robert's approval, modulo removing the code from symbolic things.",
    "created_at": "2008-05-06T23:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18981",
    "user": "https://github.com/jasongrout"
}
```

See http://groups.google.com/group/sage-devel/browse_thread/thread/861d35160afebfe6/14226ae55d50b7be?lnk=gst&q=fast_float#14226ae55d50b7be for Robert's approval, modulo removing the code from symbolic things.



---

archive/issue_comments_018982.json:
```json
{
    "body": "Apply instead of the previous patch",
    "created_at": "2008-05-06T23:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18982",
    "user": "https://github.com/jasongrout"
}
```

Apply instead of the previous patch



---

archive/issue_comments_018983.json:
```json
{
    "body": "Attachment [trac-2768-fast-float-cmp-2.patch](tarball://root/attachments/some-uuid/ticket2768/trac-2768-fast-float-cmp-2.patch) by @jasongrout created at 2008-05-06 23:45:37\n\nI updated the patch to remove the code in equations.py, per Robert's request.  Eventually it would be nice to have a SymbolicProposition class or something like that that would allow for easy characteristic functions (using this code to efficiently test for set membership up to certain numerical precision).",
    "created_at": "2008-05-06T23:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18983",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-2768-fast-float-cmp-2.patch](tarball://root/attachments/some-uuid/ticket2768/trac-2768-fast-float-cmp-2.patch) by @jasongrout created at 2008-05-06 23:45:37

I updated the patch to remove the code in equations.py, per Robert's request.  Eventually it would be nice to have a SymbolicProposition class or something like that that would allow for easy characteristic functions (using this code to efficiently test for set membership up to certain numerical precision).



---

archive/issue_comments_018984.json:
```json
{
    "body": "Yep, this looks good.",
    "created_at": "2008-05-07T02:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18984",
    "user": "https://github.com/robertwb"
}
```

Yep, this looks good.



---

archive/issue_comments_018985.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-07T08:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18985",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006403.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-07T08:35:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2768#event-6403"
}
```



---

archive/issue_comments_018986.json:
```json
{
    "body": "Merged trac-2768-fast-float-cmp-2.patch in Sage 3.0.2.alpha0",
    "created_at": "2008-05-07T08:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2768#issuecomment-18986",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-2768-fast-float-cmp-2.patch in Sage 3.0.2.alpha0
