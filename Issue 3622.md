# Issue 3622: numerical fast integration using fast float

archive/issues_003622.json:
```json
{
    "body": "Assignee: @robertwb\n\nWhen you create a symbolic expression and numerically integrate it, Sage should use\nthe fast_float framework to do this (a bazzilion times!) faster than it does right now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3622\n\n",
    "created_at": "2008-07-09T00:35:13Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "numerical fast integration using fast float",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3622",
    "user": "https://github.com/williamstein"
}
```
Assignee: @robertwb

When you create a symbolic expression and numerically integrate it, Sage should use
the fast_float framework to do this (a bazzilion times!) faster than it does right now.

Issue created by migration from https://trac.sagemath.org/ticket/3622





---

archive/issue_comments_025545.json:
```json
{
    "body": "Attachment [3622-fast_float_integration.patch](tarball://root/attachments/some-uuid/ticket3622/3622-fast_float_integration.patch) by @robertwb created at 2008-08-06 07:23:53",
    "created_at": "2008-08-06T07:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25545",
    "user": "https://github.com/robertwb"
}
```

Attachment [3622-fast_float_integration.patch](tarball://root/attachments/some-uuid/ticket3622/3622-fast_float_integration.patch) by @robertwb created at 2008-08-06 07:23:53



---

archive/issue_comments_025546.json:
```json
{
    "body": "I would like to see tests that show that functionality is not lost, such as\n\n```\nsage: numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)\n(3.333333333333333, 3.7007434154171883e-14)\nsage: numerical_integral(sin(x)^3 + sin(x),  0, pi)\n(3.333333333333333, 3.7007434154171883e-14)\n```\n\n\nAlso, this does not always win.  I think that it is worthwhile, but is there a heuristic that should be applied sometimes?\n\n\n```\nsage: timeit('numerical_integral(sin(x)^3 + sin(x),  0, pi)')\n25 loops, best of 3: 23.4 ms per loop\nsage: timeit('numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)')\n625 loops, best of 3: 900 \u00c2\u00b5s per loop\nsage: timeit('numerical_integral(cos(x)^7 + sin(x^11 + x),  0, pi)')\n25 loops, best of 3: 33.5 ms per loop\nsage: timeit('numerical_integral(lambda x: cos(x)^7 + sin(x^11 + x),  0, pi)')\n5 loops, best of 3: 164 ms per loop\n```\n\n\nFinally, the following is just wrong:\n\n\n```\nsage: timeit('numerical_integral(lambda x: 0,  0, pi)')\n625 loops, best of 3: 86.7 \u00c2\u00b5s per loop\nsage: timeit('numerical_integral(0,  0, pi)')\n'sage.rings.integer.Integer' object is not callable\n... repeated a few thousand times ...\n'sage.rings.integer.Integer' object is not callable\n5 loops, best of 3: 42.8 ms per loop\n```\n",
    "created_at": "2008-08-11T06:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25546",
    "user": "https://github.com/ncalexan"
}
```

I would like to see tests that show that functionality is not lost, such as

```
sage: numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)
(3.333333333333333, 3.7007434154171883e-14)
sage: numerical_integral(sin(x)^3 + sin(x),  0, pi)
(3.333333333333333, 3.7007434154171883e-14)
```


Also, this does not always win.  I think that it is worthwhile, but is there a heuristic that should be applied sometimes?


```
sage: timeit('numerical_integral(sin(x)^3 + sin(x),  0, pi)')
25 loops, best of 3: 23.4 ms per loop
sage: timeit('numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)')
625 loops, best of 3: 900 Âµs per loop
sage: timeit('numerical_integral(cos(x)^7 + sin(x^11 + x),  0, pi)')
25 loops, best of 3: 33.5 ms per loop
sage: timeit('numerical_integral(lambda x: cos(x)^7 + sin(x^11 + x),  0, pi)')
5 loops, best of 3: 164 ms per loop
```


Finally, the following is just wrong:


```
sage: timeit('numerical_integral(lambda x: 0,  0, pi)')
625 loops, best of 3: 86.7 Âµs per loop
sage: timeit('numerical_integral(0,  0, pi)')
'sage.rings.integer.Integer' object is not callable
... repeated a few thousand times ...
'sage.rings.integer.Integer' object is not callable
5 loops, best of 3: 42.8 ms per loop
```




---

archive/issue_comments_025547.json:
```json
{
    "body": "> I would like to see tests that show that functionality is not lost\n\nGood point. \n\n> Also, this does not always win...\n\n\n```\nsage: f = lambda x: sin(x)^3 + sin(x)\nsage: timeit('numerical_integral(f, 0, pi)')\n625 loops, best of 3: 856 \u00b5s per loop\nsage: f = sin(x)^3 + sin(x)\nsage: timeit('numerical_integral(f, 0, pi)')\n25 loops, best of 3: 15 ms per loop\nsage: f = f._fast_float_(x)\nsage: timeit('numerical_integral(f, 0, pi)')\n625 loops, best of 3: 126 \u00b5s per loop\n```\n\n\nI guess we'll have to optimize the fast_float construction... I'll look into this more. \n\n> Finally, the following is just wrong:\n\nHmm... I'll look into this.",
    "created_at": "2008-08-11T16:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25547",
    "user": "https://github.com/robertwb"
}
```

> I would like to see tests that show that functionality is not lost

Good point. 

> Also, this does not always win...


```
sage: f = lambda x: sin(x)^3 + sin(x)
sage: timeit('numerical_integral(f, 0, pi)')
625 loops, best of 3: 856 µs per loop
sage: f = sin(x)^3 + sin(x)
sage: timeit('numerical_integral(f, 0, pi)')
25 loops, best of 3: 15 ms per loop
sage: f = f._fast_float_(x)
sage: timeit('numerical_integral(f, 0, pi)')
625 loops, best of 3: 126 µs per loop
```


I guess we'll have to optimize the fast_float construction... I'll look into this more. 

> Finally, the following is just wrong:

Hmm... I'll look into this.



---

archive/issue_comments_025548.json:
```json
{
    "body": "This is a duplicate of #2881, although maybe we should keep this version since it has comments and a patch.",
    "created_at": "2008-08-31T14:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25548",
    "user": "https://github.com/jicama"
}
```

This is a duplicate of #2881, although maybe we should keep this version since it has comments and a patch.



---

archive/issue_comments_025549.json:
```json
{
    "body": "Attachment [3622-fast_float_integration.2.patch](tarball://root/attachments/some-uuid/ticket3622/3622-fast_float_integration.2.patch) by @robertwb created at 2008-09-02 03:40:30\n\nupdated",
    "created_at": "2008-09-02T03:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25549",
    "user": "https://github.com/robertwb"
}
```

Attachment [3622-fast_float_integration.2.patch](tarball://root/attachments/some-uuid/ticket3622/3622-fast_float_integration.2.patch) by @robertwb created at 2008-09-02 03:40:30

updated



---

archive/issue_comments_025550.json:
```json
{
    "body": "one more optimization",
    "created_at": "2008-09-02T03:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25550",
    "user": "https://github.com/robertwb"
}
```

one more optimization



---

archive/issue_comments_025551.json:
```json
{
    "body": "Attachment [3622-fast_float_integration.3.patch](tarball://root/attachments/some-uuid/ticket3622/3622-fast_float_integration.3.patch) by @robertwb created at 2008-09-02 03:54:32\n\nI added some more documentation to show that the old behavior is not lost. I also fixed it so constant functions work (that never worked before either, but it was an easy fix). \n\nFast float construction has been optimized in the meantime, so now it's always faster. \n\n\n```\nsage: f = lambda x: sin(x)^3 + sin(x)\nsage: timeit('numerical_integral(f, 0, pi)')\n625 loops, best of 3: 869 \u00b5s per loop\nsage: f = sin(x)^3 + sin(x)\nsage: timeit('numerical_integral(f, 0, pi)')\n5 loops, best of 3: 134 \u00b5s per loop\n```\n\n\n(Note that `timeit('numerical_integral(sin(x)^3 + sin(x),  0, pi)')` is a bit unfair because it constructs the symbolic expression every loop, but this isn't a typical use case anyways...)",
    "created_at": "2008-09-02T03:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25551",
    "user": "https://github.com/robertwb"
}
```

Attachment [3622-fast_float_integration.3.patch](tarball://root/attachments/some-uuid/ticket3622/3622-fast_float_integration.3.patch) by @robertwb created at 2008-09-02 03:54:32

I added some more documentation to show that the old behavior is not lost. I also fixed it so constant functions work (that never worked before either, but it was an easy fix). 

Fast float construction has been optimized in the meantime, so now it's always faster. 


```
sage: f = lambda x: sin(x)^3 + sin(x)
sage: timeit('numerical_integral(f, 0, pi)')
625 loops, best of 3: 869 µs per loop
sage: f = sin(x)^3 + sin(x)
sage: timeit('numerical_integral(f, 0, pi)')
5 loops, best of 3: 134 µs per loop
```


(Note that `timeit('numerical_integral(sin(x)^3 + sin(x),  0, pi)')` is a bit unfair because it constructs the symbolic expression every loop, but this isn't a typical use case anyways...)



---

archive/issue_comments_025552.json:
```json
{
    "body": "I'm curious how things compare when you put the lambda function in the loop vs putting the symbolic expression in the loop..  i.e.\n\n\n```\nsage: timeit('numerical_integral(lambda x: sin(x)^3 + sin(x), 0, pi)')\n# vs.\nsage: timeit('numerical_integral(sin(x)^3 + sin(x), 0, pi)')\n```\n\n\nIf the construction of the fast float takes a long time compared to doing the whole integral with a lambda function, then this might not be a win.",
    "created_at": "2008-09-02T04:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25552",
    "user": "https://github.com/jicama"
}
```

I'm curious how things compare when you put the lambda function in the loop vs putting the symbolic expression in the loop..  i.e.


```
sage: timeit('numerical_integral(lambda x: sin(x)^3 + sin(x), 0, pi)')
# vs.
sage: timeit('numerical_integral(sin(x)^3 + sin(x), 0, pi)')
```


If the construction of the fast float takes a long time compared to doing the whole integral with a lambda function, then this might not be a win.



---

archive/issue_comments_025553.json:
```json
{
    "body": "I applied the last patch and gave it a try.  Here are the results:\n\n\n```\nsage: timeit('numerical_integral(lambda x: sin(x)^3 + sin(x), 0, pi)')\n625 loops, best of 3: 1.09 ms per loop\nsage: timeit('numerical_integral(sin(x)^3 + sin(x), 0, pi)')\n5 loops, best of 3: 16.5 ms per loop\n```\n\n\nSo at least in this example, the time to construct the fast_float function actually swamps the whole calculation using the faster to create but slower to evaluate lambda function.",
    "created_at": "2008-09-02T04:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25553",
    "user": "https://github.com/jicama"
}
```

I applied the last patch and gave it a try.  Here are the results:


```
sage: timeit('numerical_integral(lambda x: sin(x)^3 + sin(x), 0, pi)')
625 loops, best of 3: 1.09 ms per loop
sage: timeit('numerical_integral(sin(x)^3 + sin(x), 0, pi)')
5 loops, best of 3: 16.5 ms per loop
```


So at least in this example, the time to construct the fast_float function actually swamps the whole calculation using the faster to create but slower to evaluate lambda function.



---

archive/issue_comments_025554.json:
```json
{
    "body": "The construction of the fast float object is now fast. This *is* included in the timings above (and is the bulk of the 134 microseconds). If we create the fast float item ahead of time we get \n\n\n```\nsage: f = sin(x)^3 + sin(x)\nsage: ff = f._fast_float_('x')\nsage: timeit('numerical_integral(ff, 0, pi)')\n625 loops, best of 3: 41.4 \u00b5s per loop\n```\n\n\nThe problem in the loop you give is that it is recreating the symbolic expression sin(x)^3 + sin(x) every time, which is taking all the time, but that's not a typical use case.",
    "created_at": "2008-09-02T04:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25554",
    "user": "https://github.com/robertwb"
}
```

The construction of the fast float object is now fast. This *is* included in the timings above (and is the bulk of the 134 microseconds). If we create the fast float item ahead of time we get 


```
sage: f = sin(x)^3 + sin(x)
sage: ff = f._fast_float_('x')
sage: timeit('numerical_integral(ff, 0, pi)')
625 loops, best of 3: 41.4 µs per loop
```


The problem in the loop you give is that it is recreating the symbolic expression sin(x)^3 + sin(x) every time, which is taking all the time, but that's not a typical use case.



---

archive/issue_comments_025555.json:
```json
{
    "body": "Okay, I get it now.  Sorry to make you explain again.  Here are some more timings:\n\n\n```\nsage: timeit('e = lambda x: sin(x)^3 + sin(x)')\n625 loops, best of 3: 288 ns per loop\nsage: timeit('e = sin(x)^3 + sin(x)')\n625 loops, best of 3: 103 \u00b5s per loop\nsage: timeit(\"e._fast_float_('x')\")\n625 loops, best of 3: 49 \u00b5s per loop\nsage: timeit('e._fast_float_()') #way slower\n5 loops, best of 3: 96.3 ms per loop\nsage: timeit(\"numerical_integral(e,0,pi)\")\n625 loops, best of 3: 111 \u00b5s per loop\nsage: timeit(\"numerical_integral(sin(x)^3 + sin(x),0,pi)\")\n25 loops, best of 3: 25.6 ms per loop\n```\n\n\nApparently it only takes 100 microseconds to create `sin(x)^3 + sin(x)`, 50 microseconds to turn it into a fast float, and 100 microseconds to execute the integration once that's done.  So when I put the function creation inside the loop, I would expect about 250 microseconds.  Where is the other 25.4 ms going?\n\nThat question aside, I'm now convinced this patch is a good idea, and the tests pass, so I gave it positive review.",
    "created_at": "2008-09-02T05:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25555",
    "user": "https://github.com/jicama"
}
```

Okay, I get it now.  Sorry to make you explain again.  Here are some more timings:


```
sage: timeit('e = lambda x: sin(x)^3 + sin(x)')
625 loops, best of 3: 288 ns per loop
sage: timeit('e = sin(x)^3 + sin(x)')
625 loops, best of 3: 103 µs per loop
sage: timeit("e._fast_float_('x')")
625 loops, best of 3: 49 µs per loop
sage: timeit('e._fast_float_()') #way slower
5 loops, best of 3: 96.3 ms per loop
sage: timeit("numerical_integral(e,0,pi)")
625 loops, best of 3: 111 µs per loop
sage: timeit("numerical_integral(sin(x)^3 + sin(x),0,pi)")
25 loops, best of 3: 25.6 ms per loop
```


Apparently it only takes 100 microseconds to create `sin(x)^3 + sin(x)`, 50 microseconds to turn it into a fast float, and 100 microseconds to execute the integration once that's done.  So when I put the function creation inside the loop, I would expect about 250 microseconds.  Where is the other 25.4 ms going?

That question aside, I'm now convinced this patch is a good idea, and the tests pass, so I gave it positive review.



---

archive/issue_comments_025556.json:
```json
{
    "body": "That is a really good question. It's probably because something, somewhere, is caching something (but I've looked in the obvious places and I don't see what). But, as you said, that's orthogonal to the patch. Thanks for looking into this.",
    "created_at": "2008-09-02T05:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25556",
    "user": "https://github.com/robertwb"
}
```

That is a really good question. It's probably because something, somewhere, is caching something (but I've looked in the obvious places and I don't see what). But, as you said, that's orthogonal to the patch. Thanks for looking into this.



---

archive/issue_comments_025557.json:
```json
{
    "body": "I think I found what is going on.  For a symbolic expression, the variables get cached after the first call to self.variables() or self.arguments().\n\n\n```\nsage: timeit('(sin(x)^3 + sin(x)).variables()')\n25 loops, best of 3: 16.9 ms per loop\nsage: f = sin(x)^3 + sin(x)\nsage: timeit('f.variables()')\n625 loops, best of 3: 6.61 \u00b5s per loop\n```\n\n\nI wonder if there's a way to speed up the first call to self.variables(), maybe in the special case that there is only one variable or something.",
    "created_at": "2008-09-02T05:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25557",
    "user": "https://github.com/jicama"
}
```

I think I found what is going on.  For a symbolic expression, the variables get cached after the first call to self.variables() or self.arguments().


```
sage: timeit('(sin(x)^3 + sin(x)).variables()')
25 loops, best of 3: 16.9 ms per loop
sage: f = sin(x)^3 + sin(x)
sage: timeit('f.variables()')
625 loops, best of 3: 6.61 µs per loop
```


I wonder if there's a way to speed up the first call to self.variables(), maybe in the special case that there is only one variable or something.



---

archive/issue_comments_025558.json:
```json
{
    "body": "I did a little bit more searching, and it looks like the slow part of the first call to variables() is that the expression must be simplified to know the variables, and the simplification is farmed out to maxima.  So possibly this will get a lot faster once pynac gets integrated and simplify calls can be routed there.",
    "created_at": "2008-09-02T06:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25558",
    "user": "https://github.com/jicama"
}
```

I did a little bit more searching, and it looks like the slow part of the first call to variables() is that the expression must be simplified to know the variables, and the simplification is farmed out to maxima.  So possibly this will get a lot faster once pynac gets integrated and simplify calls can be routed there.



---

archive/issue_comments_025559.json:
```json
{
    "body": "Excellent. When I saw it was a matter of milliseconds, maxima slowness went under the radar for me (it's often worse than that, going through pexpect and all), but it looks like you're right. And it's a relief that it'll get faster. Thanks for tracking this down.",
    "created_at": "2008-09-02T07:18:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25559",
    "user": "https://github.com/robertwb"
}
```

Excellent. When I saw it was a matter of milliseconds, maxima slowness went under the radar for me (it's often worse than that, going through pexpect and all), but it looks like you're right. And it's a relief that it'll get faster. Thanks for tracking this down.



---

archive/issue_comments_025560.json:
```json
{
    "body": "Merged 3622-fast_float_integration.3.patch  in Sage 3.1.2.alpha4",
    "created_at": "2008-09-02T10:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25560",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 3622-fast_float_integration.3.patch  in Sage 3.1.2.alpha4



---

archive/issue_comments_025561.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-02T10:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3622#issuecomment-25561",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
