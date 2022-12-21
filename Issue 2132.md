# Issue 2132: If plot.show() is called with a very large figsize, a segfault occurs. (And what are the units on figsize, anyway?)

Issue created by migration from Trac.

Original creator: bober

Original creation time: 2008-02-09 21:46:04

Assignee: was

Here are two examples of two different types of errors. If you have lots of memory, I suppose that you might need to make figsize bigger.

(The following takes place on a 32-bit Core Duo with 2 gigs of ram.)


```
sage: P = plot(sin(x))
sage: P.show(figsize=[200,200])
terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc
/home/bober/sage/local/bin/sage-sage: line 210: 12131 Aborted                 (core dumped) sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$`@`"
bober`@`bober:~/sage/misc$ 
```



```
bober`@`bober:~/sage/misc$ sage
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



---

Comment by bober created at 2008-02-09 22:54:31

The problems occur in matplotlib.

The first example fails in backend_agg.cpp, around line 246, where some giant arrays fail to be allocated.

The second problem starts from somewhere in agg_pixfmt_rgba.h. For me it crashes on line 1708, which is

                p = (value_type*)m_rbuf->next_row(p);

I'm not sure where that memory is [not] allocated.


---

Comment by boothby created at 2009-01-23 10:43:56

Resolution: worksforme


---

Comment by boothby created at 2009-01-23 10:43:56

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

Comment by mabshoff created at 2009-01-23 10:55:02

The fix was due to an updated Matplotlib AFAIK.

Cheers,

Michael
