# Issue 2932: matrix.is_invertible() has inconsisten behavior over CDF

archive/issues_002932.json:
```json
{
    "body": "Assignee: was\n\nFrom Alex Ghitza:\n\n\n```\nsage: M = matrix(CDF, 2, 2, [(-1 - 2*I, 5 - 6*I), (-2 - 4*I, 10 - 12*I)])\nsage: M.is_invertible()\nTrue\nsage: M.determinant()\n5.3290705182e-15 + 1.7763568394e-15*I\nsage: M.inverse()\n[ 1.01330991616e+15 - 2.58956978574e+15*I -5.06654958079e+14 +\n1.29478489287e+15*I]\n[ 5.62949953421e+14 + 5.62949953421e+14*I -2.81474976711e+14 -\n2.81474976711e+14*I]\n\nSo because of roundoff errors, Sage thinks that we have an invertible\nmatrix.  But the code for echelon_form knows that it's not invertible:\n\nsage: M.echelon_form()\n[                                    1.0                             1.4\n+ 3.2*I]\n[-2.22044604925e-16 - 4.4408920985e-16*I\n~       0]\nsage: M.rank()\n1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2932\n\n",
    "created_at": "2008-04-15T14:52:28Z",
    "labels": [
        "linear algebra",
        "critical",
        "bug"
    ],
    "title": "matrix.is_invertible() has inconsisten behavior over CDF",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2932",
    "user": "dfdeshom"
}
```
Assignee: was

From Alex Ghitza:


```
sage: M = matrix(CDF, 2, 2, [(-1 - 2*I, 5 - 6*I), (-2 - 4*I, 10 - 12*I)])
sage: M.is_invertible()
True
sage: M.determinant()
5.3290705182e-15 + 1.7763568394e-15*I
sage: M.inverse()
[ 1.01330991616e+15 - 2.58956978574e+15*I -5.06654958079e+14 +
1.29478489287e+15*I]
[ 5.62949953421e+14 + 5.62949953421e+14*I -2.81474976711e+14 -
2.81474976711e+14*I]

So because of roundoff errors, Sage thinks that we have an invertible
matrix.  But the code for echelon_form knows that it's not invertible:

sage: M.echelon_form()
[                                    1.0                             1.4
+ 3.2*I]
[-2.22044604925e-16 - 4.4408920985e-16*I
~       0]
sage: M.rank()
1
```


Issue created by migration from https://trac.sagemath.org/ticket/2932





---

archive/issue_comments_020186.json:
```json
{
    "body": "Using numpy gives the following:\n\n\n```\nsage: M = matrix(CDF, 2, 2, [(-1 - 2*I, 5 - 6*I), (-2 - 4*I, 10 - 12*I)])\nsage: n=M.numpy()\nsage: import numpy\nsage: numpy.linalg.det(n)\n0.0\nsage: numpy.linalg.inv(n)\n---------------------------------------------------------------------------\n<class 'numpy.linalg.linalg.LinAlgError'> Traceback (most recent call last)\n\n/home/grout/sage/devel/sage-main/sage/misc/<ipython console> in <module>()\n\n/home/grout/sage/local/lib/python2.5/site-packages/numpy/linalg/linalg.py in inv(a)\n    244 def inv(a):\n    245     a, wrap = _makearray(a)\n--> 246     return wrap(solve(a, identity(a.shape[0], dtype=a.dtype)))\n    247\n    248 # Cholesky decomposition\n\n/home/grout/sage/local/lib/python2.5/site-packages/numpy/linalg/linalg.py in solve(a, b)\n    187     results = lapack_routine(n_eq, n_rhs, a, n_eq, pivots, b, n_eq, 0)\n    188     if results['info'] > 0:\n--> 189         raise LinAlgError, 'Singular matrix'\n    190     if one_eq:\n    191         return b.ravel().astype(result_t)\n\n<class 'numpy.linalg.linalg.LinAlgError'>: Singular matrix\n```\n",
    "created_at": "2008-04-15T23:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20186",
    "user": "jason"
}
```

Using numpy gives the following:


```
sage: M = matrix(CDF, 2, 2, [(-1 - 2*I, 5 - 6*I), (-2 - 4*I, 10 - 12*I)])
sage: n=M.numpy()
sage: import numpy
sage: numpy.linalg.det(n)
0.0
sage: numpy.linalg.inv(n)
---------------------------------------------------------------------------
<class 'numpy.linalg.linalg.LinAlgError'> Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/misc/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/numpy/linalg/linalg.py in inv(a)
    244 def inv(a):
    245     a, wrap = _makearray(a)
--> 246     return wrap(solve(a, identity(a.shape[0], dtype=a.dtype)))
    247
    248 # Cholesky decomposition

/home/grout/sage/local/lib/python2.5/site-packages/numpy/linalg/linalg.py in solve(a, b)
    187     results = lapack_routine(n_eq, n_rhs, a, n_eq, pivots, b, n_eq, 0)
    188     if results['info'] > 0:
--> 189         raise LinAlgError, 'Singular matrix'
    190     if one_eq:
    191         return b.ravel().astype(result_t)

<class 'numpy.linalg.linalg.LinAlgError'>: Singular matrix
```




---

archive/issue_comments_020187.json:
```json
{
    "body": "I propose that this code is working as intended - it cannot be expected that floating point calculations always provide the same results as would be obtained using precise calculations. It cannot either be assumed that two calculations that are equivalent using precise numbers are equivalent when using approximations. The attached patch adds docstring explanations of this to real and complex number classes and fields.\n\nOther than that, I get this using Sage version 3.0:\n\n\n```\nsage: M = matrix(CDF, 2, 2, [(-1 - 2*I, 5 - 6*I), (-2 - 4*I, 10 - 12*I)])\nsage: M.is_invertible()\nFalse\n```\n",
    "created_at": "2008-05-10T21:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20187",
    "user": "broune"
}
```

I propose that this code is working as intended - it cannot be expected that floating point calculations always provide the same results as would be obtained using precise calculations. It cannot either be assumed that two calculations that are equivalent using precise numbers are equivalent when using approximations. The attached patch adds docstring explanations of this to real and complex number classes and fields.

Other than that, I get this using Sage version 3.0:


```
sage: M = matrix(CDF, 2, 2, [(-1 - 2*I, 5 - 6*I), (-2 - 4*I, 10 - 12*I)])
sage: M.is_invertible()
False
```




---

archive/issue_comments_020188.json:
```json
{
    "body": "Changing priority from critical to major.",
    "created_at": "2008-05-10T21:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20188",
    "user": "broune"
}
```

Changing priority from critical to major.



---

archive/issue_comments_020189.json:
```json
{
    "body": "Changing assignee from was to broune.",
    "created_at": "2008-05-10T21:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20189",
    "user": "broune"
}
```

Changing assignee from was to broune.



---

archive/issue_comments_020190.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-10T21:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20190",
    "user": "broune"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020191.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-10T21:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20191",
    "user": "broune"
}
```

Attachment



---

archive/issue_comments_020192.json:
```json
{
    "body": "I am curious what algorithms are used for is_invertible and inverse().  Apparently determinant() uses GSL; how does GSL compare with numpy generally for numeric algorithms?  Numpy uses the standard blas libraries an awful lot; what does GSL do?\n\nIf is_invertible and inverse() do not use standard numerical linear algebra functions (e.g., use ATLAS), then why not?  If it's an issue of NotImplemented, then let's open a ticket.  I would probably get to it by sometime this summer, since we have a numerical linear algebra workshop where I'm at.",
    "created_at": "2008-05-11T01:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20192",
    "user": "jason"
}
```

I am curious what algorithms are used for is_invertible and inverse().  Apparently determinant() uses GSL; how does GSL compare with numpy generally for numeric algorithms?  Numpy uses the standard blas libraries an awful lot; what does GSL do?

If is_invertible and inverse() do not use standard numerical linear algebra functions (e.g., use ATLAS), then why not?  If it's an issue of NotImplemented, then let's open a ticket.  I would probably get to it by sometime this summer, since we have a numerical linear algebra workshop where I'm at.



---

archive/issue_comments_020193.json:
```json
{
    "body": "From IRC (with editing out of other unrelated conversation):\n\n\n```\n[20:15] <jason--> re: 2932; what algorithms are used for numerical linear algebra over CDF for inverse() and is_invertible()?\n[20:15] <jason--> I don't find those functions in matrix_complex_double_dense.pyx\n[20:16] <jason--> are they the generic algorithms in matrix*.pyx?\n[20:16] <wstein-3053> If they aren't in matrix_complex_double_dense then they are the generic ones.\n[20:17] <jason--> thanks; also, does anyone have any feelings for GSL compared to numpy for numerical linear algebra?\n[20:17] <wstein-3053> numpy is usually better.\n[20:18] <jason--> okay; do you mind if we switch the determinant function to numpy for matrices over CDF?\n[20:18] <wstein-3053> jason-- please do.\n[20:19] <jason--> okay; ticket coming right up.\n```\n",
    "created_at": "2008-05-11T01:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20193",
    "user": "jason"
}
```

From IRC (with editing out of other unrelated conversation):


```
[20:15] <jason--> re: 2932; what algorithms are used for numerical linear algebra over CDF for inverse() and is_invertible()?
[20:15] <jason--> I don't find those functions in matrix_complex_double_dense.pyx
[20:16] <jason--> are they the generic algorithms in matrix*.pyx?
[20:16] <wstein-3053> If they aren't in matrix_complex_double_dense then they are the generic ones.
[20:17] <jason--> thanks; also, does anyone have any feelings for GSL compared to numpy for numerical linear algebra?
[20:17] <wstein-3053> numpy is usually better.
[20:18] <jason--> okay; do you mind if we switch the determinant function to numpy for matrices over CDF?
[20:18] <wstein-3053> jason-- please do.
[20:19] <jason--> okay; ticket coming right up.
```




---

archive/issue_comments_020194.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_ncalexan\".",
    "created_at": "2008-06-15T21:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20194",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_ncalexan".



---

archive/issue_comments_020195.json:
```json
{
    "body": "Changing keywords from \"editor_ncalexan\" to \"editor_malb\".",
    "created_at": "2008-06-20T04:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20195",
    "user": "craigcitro"
}
```

Changing keywords from "editor_ncalexan" to "editor_malb".



---

archive/issue_comments_020196.json:
```json
{
    "body": "What is the current status of this ticket? I just to over being the editor for this ticket so please speak up :-)",
    "created_at": "2008-06-23T17:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20196",
    "user": "malb"
}
```

What is the current status of this ticket? I just to over being the editor for this ticket so please speak up :-)



---

archive/issue_comments_020197.json:
```json
{
    "body": "I just got back into town (been gone for a month).  I'd still like to make numpy the default backend for CDF and RDF and I'll probably work on that this week.",
    "created_at": "2008-06-23T22:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20197",
    "user": "jason"
}
```

I just got back into town (been gone for a month).  I'd still like to make numpy the default backend for CDF and RDF and I'll probably work on that this week.



---

archive/issue_comments_020198.json:
```json
{
    "body": "Since the patch is just documentation telling the user not to expect exact results, I like it.  +1 from me.  Even when I convert things to numpy, it would still be good to have such a disclaimer, I think.",
    "created_at": "2008-06-23T22:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20198",
    "user": "jason"
}
```

Since the patch is just documentation telling the user not to expect exact results, I like it.  +1 from me.  Even when I convert things to numpy, it would still be good to have such a disclaimer, I think.



---

archive/issue_comments_020199.json:
```json
{
    "body": "See ticket #3498 for switching the backend to numpy.",
    "created_at": "2008-06-23T22:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20199",
    "user": "jason"
}
```

See ticket #3498 for switching the backend to numpy.



---

archive/issue_comments_020200.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-25T07:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20200",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_comments_020201.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-25T07:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2932#issuecomment-20201",
    "user": "mabshoff"
}
```

Resolution: fixed
