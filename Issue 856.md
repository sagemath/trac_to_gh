# Issue 856: strange behaviour when converting a numpy matrix to a sage one

archive/issues_000856.json:
```json
{
    "body": "Assignee: @mwhansen\n\n\n```\nsage: import numpy\nsage: numpy.array([[1,2,3],[4,5,6],[7,8,9]],'f')\n\narray([[ 1.,  2.,  3.],\n      [ 4.,  5.,  6.],\n      [ 7.,  8.,  9.]], dtype=float32)\nsage: a=numpy.array([[1,2,3],[4,5,6],[7,8,9]],'f')\nsage: matrix(a)\n\n[     2.00000047311      512.000122547       8192.0019722]\n[     131072.031677 9.87267348858e-312 1.48958728182e-263]\n[6.36598737141e-314  6.6976282025e-316 3.40280828847e-313]\nsage:\n\n```\n\n\n------------------------------------\nAre you running a 64-bit machine?\n\nI looked at the code, and the problem seems to come from the fact that\nit is doing a naive check on the type of the numpy array; it is\ncurrently assuming that your float32 array is a float64 array which is\nwhy you are getting the strange results you are.  See below:\n\n\n```\nsage: a = numpy.array([[1,2,3],[4,5,6],[7,8,9]],float)\nsage: a.dtype\ndtype('float64')\nsage: matrix(a)\n\n[1.0 2.0 3.0]\n[4.0 5.0 6.0]\n[7.0 8.0 9.0]\nsage: a = numpy.array([[1,2,3],[4,5,6],[7,8,9]],'float64')\nsage: a.dtype\ndtype('float64')\nsage: matrix(a)\n\n[1.0 2.0 3.0]\n[4.0 5.0 6.0]\n[7.0 8.0 9.0]\nsage: a = numpy.array([[1,2,3],[4,5,6],[7,8,9]],'float32')\nsage: a.dtype\ndtype('float32')\nsage: matrix(a)\n\n[     2.00000047311      512.000122547       8192.0019722]\n[     131072.031677 2.34082748762e-310                0.0]\n[3.16202013338e-322 4.74797085653e-321 4.94065645841e-324]\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/856\n\n",
    "created_at": "2007-10-12T02:43:28Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "strange behaviour when converting a numpy matrix to a sage one",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/856",
    "user": "@mwhansen"
}
```
Assignee: @mwhansen


```
sage: import numpy
sage: numpy.array([[1,2,3],[4,5,6],[7,8,9]],'f')

array([[ 1.,  2.,  3.],
      [ 4.,  5.,  6.],
      [ 7.,  8.,  9.]], dtype=float32)
sage: a=numpy.array([[1,2,3],[4,5,6],[7,8,9]],'f')
sage: matrix(a)

[     2.00000047311      512.000122547       8192.0019722]
[     131072.031677 9.87267348858e-312 1.48958728182e-263]
[6.36598737141e-314  6.6976282025e-316 3.40280828847e-313]
sage:

```


------------------------------------
Are you running a 64-bit machine?

I looked at the code, and the problem seems to come from the fact that
it is doing a naive check on the type of the numpy array; it is
currently assuming that your float32 array is a float64 array which is
why you are getting the strange results you are.  See below:


```
sage: a = numpy.array([[1,2,3],[4,5,6],[7,8,9]],float)
sage: a.dtype
dtype('float64')
sage: matrix(a)

[1.0 2.0 3.0]
[4.0 5.0 6.0]
[7.0 8.0 9.0]
sage: a = numpy.array([[1,2,3],[4,5,6],[7,8,9]],'float64')
sage: a.dtype
dtype('float64')
sage: matrix(a)

[1.0 2.0 3.0]
[4.0 5.0 6.0]
[7.0 8.0 9.0]
sage: a = numpy.array([[1,2,3],[4,5,6],[7,8,9]],'float32')
sage: a.dtype
dtype('float32')
sage: matrix(a)

[     2.00000047311      512.000122547       8192.0019722]
[     131072.031677 2.34082748762e-310                0.0]
[3.16202013338e-322 4.74797085653e-321 4.94065645841e-324]

```


Issue created by migration from https://trac.sagemath.org/ticket/856





---

archive/issue_comments_005303.json:
```json
{
    "body": "Attachment [856.patch](tarball://root/attachments/some-uuid/ticket856/856.patch) by @mwhansen created at 2007-10-12 04:47:45\n\npatch needs testing on 32-bit machines",
    "created_at": "2007-10-12T04:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/856#issuecomment-5303",
    "user": "@mwhansen"
}
```

Attachment [856.patch](tarball://root/attachments/some-uuid/ticket856/856.patch) by @mwhansen created at 2007-10-12 04:47:45

patch needs testing on 32-bit machines



---

archive/issue_comments_005304.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-12T04:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/856#issuecomment-5304",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005305.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/856#issuecomment-5305",
    "user": "@williamstein"
}
```

Resolution: fixed
