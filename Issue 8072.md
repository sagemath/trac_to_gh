# Issue 8072: Kernels of matrices over integral domains are broken

Issue created by migration from https://trac.sagemath.org/ticket/8072

Original creator: rbeezer

Original creation time: 2010-01-26 06:53:06

Assignee: was

CC:  jason

Asking for a kernel of a matrix over an integral domain has a dedicated chunk of code that tries to create a submodule as a return value.  Only there is no support for submodules over domains (just PIDs and fields).

I'll be going after this as part of a larger overhaul of matrix kernels generally.


```
sage: R=ZZ['x']
sage: R.is_integral_domain()
True
sage: W=R^2
sage: W
Ambient free module of rank 2 over the integral domain Univariate Polynomial Ring in x over Integer Ring
sage: A=matrix(R,[1,2,3])
sage: A.right_kernel()
<snip>

/sage/dev/local/lib/python2.6/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.right_kernel (sage/matrix/matrix2.c:13840)()

AttributeError: 'FreeModule_ambient_domain' object has no attribute 'submodule'
```



---

Comment by jason created at 2010-01-26 09:42:14

Feel free to CC me on any linear algebra tickets.
