# Issue 6358: use numpy to optimize RDF and CDF solve_right functions

archive/issues_006358.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @rbeezer\n\n\n```\n> Does sage have a way to use a numeric method (such as Jacobi, or Gauss-\n> Sidel) to solve matrix equations of the form A*x = b? (CDF matrices by\n> the way). the A.solve_right(b) method is too slow.\n>\n> Thanks,\n> Ethan\n\nHere is an example of how to convert back/forth to numpy to solve A*x\n# b very quickly.  Below we do this with A a 1000x1000 matrix, and it\ntakes about a half second.   It would be *great* if somebody made it\nso this would work in Sage automatically without having to explicitly\nuse numpy like I've done before.  But for you, I bet this is a minor\ninconvenience.\n\nsage: n = 1000\nsage: a = random_matrix(CDF,n); v = random_matrix(CDF,n,1)\nsage: aa = a.numpy(); vv = v.numpy()\nsage: import numpy\nsage: time ww = numpy.linalg.solve(aa, vv)\nTime: CPU 0.57 s, Wall: 0.41 s\nsage: w = matrix(CDF, ww)\nsage: max([abs(z) for z in a*w - v])\n5.46740430707e-12 + 8.431033649e-13*I\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6358\n\n",
    "created_at": "2009-06-18T19:44:09Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "use numpy to optimize RDF and CDF solve_right functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6358",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @rbeezer


```
> Does sage have a way to use a numeric method (such as Jacobi, or Gauss-
> Sidel) to solve matrix equations of the form A*x = b? (CDF matrices by
> the way). the A.solve_right(b) method is too slow.
>
> Thanks,
> Ethan

Here is an example of how to convert back/forth to numpy to solve A*x
# b very quickly.  Below we do this with A a 1000x1000 matrix, and it
takes about a half second.   It would be *great* if somebody made it
so this would work in Sage automatically without having to explicitly
use numpy like I've done before.  But for you, I bet this is a minor
inconvenience.

sage: n = 1000
sage: a = random_matrix(CDF,n); v = random_matrix(CDF,n,1)
sage: aa = a.numpy(); vv = v.numpy()
sage: import numpy
sage: time ww = numpy.linalg.solve(aa, vv)
Time: CPU 0.57 s, Wall: 0.41 s
sage: w = matrix(CDF, ww)
sage: max([abs(z) for z in a*w - v])
5.46740430707e-12 + 8.431033649e-13*I
```


Issue created by migration from https://trac.sagemath.org/ticket/6358





---

archive/issue_comments_050844.json:
```json
{
    "body": "This already works.  The problem is that it is backwardly-named solve_left.  The solve_right function incurs the overhead of a matrix copy (but then solves the backwards equation, since solve_left is backwards).\n\nTo fix all this:\n\n1. Rename the matrix_double_dense.pyx solve_left to solve_right\n2. implement a matrix_double_dense.pyx solve_left that takes the transpose and then calls solve_right\n\n\nEventually, we also need to fix the lu solve.  There is another trac ticket for this somewhere.  The problem is that the function does not deal correctly with the output of the scipy lu decomposition.",
    "created_at": "2009-06-19T02:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6358#issuecomment-50844",
    "user": "@jasongrout"
}
```

This already works.  The problem is that it is backwardly-named solve_left.  The solve_right function incurs the overhead of a matrix copy (but then solves the backwards equation, since solve_left is backwards).

To fix all this:

1. Rename the matrix_double_dense.pyx solve_left to solve_right
2. implement a matrix_double_dense.pyx solve_left that takes the transpose and then calls solve_right


Eventually, we also need to fix the lu solve.  There is another trac ticket for this somewhere.  The problem is that the function does not deal correctly with the output of the scipy lu decomposition.



---

archive/issue_comments_050845.json:
```json
{
    "body": "rbeezer: Ideally, we should also make sure the solve_* functionality mimics how you did the kernel_* functionality (i.e., that a person can define either or both in a matrix subclass and the right thing is done to make the other function make sense).",
    "created_at": "2009-06-21T06:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6358#issuecomment-50845",
    "user": "@jasongrout"
}
```

rbeezer: Ideally, we should also make sure the solve_* functionality mimics how you did the kernel_* functionality (i.e., that a person can define either or both in a matrix subclass and the right thing is done to make the other function make sense).



---

archive/issue_comments_050846.json:
```json
{
    "body": "`solve_left` and `solve_right` already use `scipy` currently...",
    "created_at": "2016-03-31T12:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6358#issuecomment-50846",
    "user": "@jdemeyer"
}
```

`solve_left` and `solve_right` already use `scipy` currently...



---

archive/issue_comments_050847.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-03-31T12:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6358#issuecomment-50847",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050848.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-03-31T12:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6358#issuecomment-50848",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050849.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6358#issuecomment-50849",
    "user": "@vbraun"
}
```

Resolution: fixed
