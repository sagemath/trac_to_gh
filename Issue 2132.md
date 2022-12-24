# Issue 2132: If plot.show() is called with a very large figsize, a segfault occurs. (And what are the units on figsize, anyway?)

archive/issues_002132.json:
```json
{
    "body": "Assignee: was\n\nHere are two examples of two different types of errors. If you have lots of memory, I suppose that you might need to make figsize bigger.\n\n(The following takes place on a 32-bit Core Duo with 2 gigs of ram.)\n\n\n```\nsage: P = plot(sin(x))\nsage: P.show(figsize=[200,200])\nterminate called after throwing an instance of 'std::bad_alloc'\n  what():  std::bad_alloc\n/home/bober/sage/local/bin/sage-sage: line 210: 12131 Aborted                 (core dumped) sage-ipython -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\nbober@bober:~/sage/misc$ \n```\n\n\n\n```\nbober@bober:~/sage/misc$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: graph_embeddings\nsage: P = plot(sin(x))\nsage: P.show(figsize[1000,1000])\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n---------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2132\n\n",
    "created_at": "2008-02-09T21:46:04Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "If plot.show() is called with a very large figsize, a segfault occurs. (And what are the units on figsize, anyway?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2132",
    "user": "bober"
}
```
Assignee: was

Here are two examples of two different types of errors. If you have lots of memory, I suppose that you might need to make figsize bigger.

(The following takes place on a 32-bit Core Duo with 2 gigs of ram.)


```
sage: P = plot(sin(x))
sage: P.show(figsize=[200,200])
terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc
/home/bober/sage/local/bin/sage-sage: line 210: 12131 Aborted                 (core dumped) sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$@"
bober@bober:~/sage/misc$ 
```



```
bober@bober:~/sage/misc$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: graph_embeddings
sage: P = plot(sin(x))
sage: P.show(figsize[1000,1000])
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
---------------------------------------
```


Issue created by migration from https://trac.sagemath.org/ticket/2132





---

archive/issue_comments_013982.json:
```json
{
    "body": "The problems occur in matplotlib.\n\nThe first example fails in backend_agg.cpp, around line 246, where some giant arrays fail to be allocated.\n\nThe second problem starts from somewhere in agg_pixfmt_rgba.h. For me it crashes on line 1708, which is\n\n                p = (value_type*)m_rbuf->next_row(p);\n\nI'm not sure where that memory is [not] allocated.",
    "created_at": "2008-02-09T22:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2132#issuecomment-13982",
    "user": "bober"
}
```

The problems occur in matplotlib.

The first example fails in backend_agg.cpp, around line 246, where some giant arrays fail to be allocated.

The second problem starts from somewhere in agg_pixfmt_rgba.h. For me it crashes on line 1708, which is

                p = (value_type*)m_rbuf->next_row(p);

I'm not sure where that memory is [not] allocated.



---

archive/issue_comments_013983.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2009-01-23T10:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2132#issuecomment-13983",
    "user": "boothby"
}
```

Resolution: worksforme



---

archive/issue_comments_013984.json:
```json
{
    "body": "I get\n\n```\n/home/boothby/sage/local/lib/python2.5/site-packages/matplotlib/backends/backend_agg.py in __init__(self, width, height, dpi)\n     60         self.height = height\n     61         if __debug__: verbose.report('RendererAgg.__init__ width=%s, height=%s'%(width, height), 'debug-annoying')\n---> 62         self._renderer = _RendererAgg(int(width), int(height), dpi, debug=False)\n     63         if __debug__: verbose.report('RendererAgg.__init__ _RendererAgg done',\n     64                                      'debug-annoying')\n\nValueError: width and height must each be below 32768\nsage: \n```\n",
    "created_at": "2009-01-23T10:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2132#issuecomment-13984",
    "user": "boothby"
}
```

I get

```
/home/boothby/sage/local/lib/python2.5/site-packages/matplotlib/backends/backend_agg.py in __init__(self, width, height, dpi)
     60         self.height = height
     61         if __debug__: verbose.report('RendererAgg.__init__ width=%s, height=%s'%(width, height), 'debug-annoying')
---> 62         self._renderer = _RendererAgg(int(width), int(height), dpi, debug=False)
     63         if __debug__: verbose.report('RendererAgg.__init__ _RendererAgg done',
     64                                      'debug-annoying')

ValueError: width and height must each be below 32768
sage: 
```




---

archive/issue_comments_013985.json:
```json
{
    "body": "The fix was due to an updated Matplotlib AFAIK.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2132#issuecomment-13985",
    "user": "mabshoff"
}
```

The fix was due to an updated Matplotlib AFAIK.

Cheers,

Michael
