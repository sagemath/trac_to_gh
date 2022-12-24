# Issue 8072: Kernels of matrices over integral domains are broken

archive/issues_008072.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout\n\nAsking for a kernel of a matrix over an integral domain has a dedicated chunk of code that tries to create a submodule as a return value.  Only there is no support for submodules over domains (just PIDs and fields).\n\nI'll be going after this as part of a larger overhaul of matrix kernels generally.\n\n\n```\nsage: R=ZZ['x']\nsage: R.is_integral_domain()\nTrue\nsage: W=R^2\nsage: W\nAmbient free module of rank 2 over the integral domain Univariate Polynomial Ring in x over Integer Ring\nsage: A=matrix(R,[1,2,3])\nsage: A.right_kernel()\n<snip>\n\n/sage/dev/local/lib/python2.6/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.right_kernel (sage/matrix/matrix2.c:13840)()\n\nAttributeError: 'FreeModule_ambient_domain' object has no attribute 'submodule'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8072\n\n",
    "created_at": "2010-01-26T06:53:06Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Kernels of matrices over integral domains are broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8072",
    "user": "@rbeezer"
}
```
Assignee: @williamstein

CC:  @jasongrout

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


Issue created by migration from https://trac.sagemath.org/ticket/8072





---

archive/issue_comments_070738.json:
```json
{
    "body": "Feel free to CC me on any linear algebra tickets.",
    "created_at": "2010-01-26T09:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8072#issuecomment-70738",
    "user": "@jasongrout"
}
```

Feel free to CC me on any linear algebra tickets.
