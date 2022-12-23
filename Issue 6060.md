# Issue 6060: divmod fails when one argument is Integer and the other is a Python int

Issue created by migration from https://trac.sagemath.org/ticket/6060

Original creator: fredrik.johansson

Original creation time: 2009-05-18 03:18:52

Assignee: somebody


```
sage: divmod(10r,10)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/fredrik/sage-3.4.2-linux-Ubuntu_8.10-sse2-i686-Linux/<ipython console> in <module>()

/home/fredrik/sage-3.4.2-linux-Ubuntu_8.10-sse2-i686-Linux/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.EuclideanDomainElement.__divmod__ (sage/structure/element.c:13777)()

AttributeError: 'int' object has no attribute 'quo_rem'
```


Attaching a patch.


---

Attachment


---

Comment by mhansen created at 2009-05-19 04:38:55

All tests pass.  Looks good to me.


---

Comment by mabshoff created at 2009-05-19 18:24:51

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 18:24:51

Resolution: fixed
