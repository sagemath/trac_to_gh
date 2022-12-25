# Issue 2468: inverting a non-invertible matrix over RDF returns weird results

archive/issues_002468.json:
```json
{
    "body": "Assignee: @williamstein\n\nCheck this out:\n\n```\nsage: A = Matrix(RDF, [[1, 0], [0, 0]])\nsage: A.inverse()\n\n[nan nan]\n[nan inf]\n```\n\nThis is, to say the least, weird.  This should throw a ZeroDivisionError instead.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2468\n\n",
    "created_at": "2008-03-11T02:46:35Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "inverting a non-invertible matrix over RDF returns weird results",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2468",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

Check this out:

```
sage: A = Matrix(RDF, [[1, 0], [0, 0]])
sage: A.inverse()

[nan nan]
[nan inf]
```

This is, to say the least, weird.  This should throw a ZeroDivisionError instead.


Issue created by migration from https://trac.sagemath.org/ticket/2468





---

archive/issue_events_005817.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-11T02:51:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2468#event-5817"
}
```



---

archive/issue_comments_016681.json:
```json
{
    "body": "I don't see why a ZeroDivisionError should be thrown. Note that Matlab doesn't complain either:\n\n```\n>> a = [1 0; 0 0];\n>> inv(a)\nWarning: Matrix is singular to working precision.\n\nans =\n\n   Inf   Inf\n   Inf   Inf\n```",
    "created_at": "2008-03-13T03:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2468#issuecomment-16681",
    "user": "https://github.com/dfdeshom"
}
```

I don't see why a ZeroDivisionError should be thrown. Note that Matlab doesn't complain either:

```
>> a = [1 0; 0 0];
>> inv(a)
Warning: Matrix is singular to working precision.

ans =

   Inf   Inf
   Inf   Inf
```



---

archive/issue_comments_016682.json:
```json
{
    "body": "I agree with dfdeshom.  The relevant code that does the inverse is\n\n```\nresult_invert = gsl_linalg_LU_invert(self._LU,self._p,M._matrix)\n```\n\nNote that 1/RDF(0) also doesn't give ZeroDivisionError:\n\n```\nsage: 1/RDF(0)\ninf\n```\n\nSo I think that (1) this ticket should be resolved with a patch\nthat simply adds a doctest with this nan/inf behavior and says\nwhat the deal is in the docs.",
    "created_at": "2008-03-13T03:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2468#issuecomment-16682",
    "user": "https://github.com/williamstein"
}
```

I agree with dfdeshom.  The relevant code that does the inverse is

```
result_invert = gsl_linalg_LU_invert(self._LU,self._p,M._matrix)
```

Note that 1/RDF(0) also doesn't give ZeroDivisionError:

```
sage: 1/RDF(0)
inf
```

So I think that (1) this ticket should be resolved with a patch
that simply adds a doctest with this nan/inf behavior and says
what the deal is in the docs.



---

archive/issue_comments_016683.json:
```json
{
    "body": "I've added a patch that, in addition:\n\n* adds some doctests to this file\n* corrects a bug where subtraction of RDF matrices would always throw an error",
    "created_at": "2008-03-14T05:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2468#issuecomment-16683",
    "user": "https://github.com/dfdeshom"
}
```

I've added a patch that, in addition:

* adds some doctests to this file
* corrects a bug where subtraction of RDF matrices would always throw an error



---

archive/issue_comments_016684.json:
```json
{
    "body": "Attachment [2468.hg](tarball://root/attachments/some-uuid/ticket2468/2468.hg) by @dfdeshom created at 2008-03-14 05:34:49\n\ncorrect a small typo in patch",
    "created_at": "2008-03-14T05:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2468#issuecomment-16684",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2468.hg](tarball://root/attachments/some-uuid/ticket2468/2468.hg) by @dfdeshom created at 2008-03-14 05:34:49

correct a small typo in patch



---

archive/issue_comments_016685.json:
```json
{
    "body": "Replying to [comment:4 dfdeshom]:\n> I've added a patch that, in addition:\n> \n> * adds some doctests to this file\n> * corrects a bug where subtraction of RDF matrices would always throw an error\n\n\nVery nice! Before the patch:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.4, Release Date: 2008-03-16                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: m = Matrix(RDF, [[1,2],[3,4]])\nsage: n=m^2\nsage: n+m\n\n[ 8.0 12.0]\n[18.0 26.0]\nsage: n-m\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/scratch/mabshoff/release-cycle/sage-2.11.alpha0/<ipython console> in <module>()\n\n/scratch/mabshoff/release-cycle/sage-2.11.alpha0/element.pyx in sage.structure.element.ModuleElement.__sub__()\n\n/scratch/mabshoff/release-cycle/sage-2.11.alpha0/coerce.pxi in sage.structure.element._sub_c()\n\n/scratch/mabshoff/release-cycle/sage-2.11.alpha0/matrix_real_double_dense.pyx in sage.matrix.matrix_real_double_dense.Matrix_real_double_dense._sub_c_impl()\n\n<type 'exceptions.ValueError'>: GSL routine had an error\nsage:\n```\nI will add a doctest patch for this bug since it is currently missing.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-18T02:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2468#issuecomment-16685",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 dfdeshom]:
> I've added a patch that, in addition:
> 
> * adds some doctests to this file
> * corrects a bug where subtraction of RDF matrices would always throw an error


Very nice! Before the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.4, Release Date: 2008-03-16                      |
| Type notebook() for the GUI, and license() for information.        |
sage: m = Matrix(RDF, [[1,2],[3,4]])
sage: n=m^2
sage: n+m

[ 8.0 12.0]
[18.0 26.0]
sage: n-m
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-2.11.alpha0/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-2.11.alpha0/element.pyx in sage.structure.element.ModuleElement.__sub__()

/scratch/mabshoff/release-cycle/sage-2.11.alpha0/coerce.pxi in sage.structure.element._sub_c()

/scratch/mabshoff/release-cycle/sage-2.11.alpha0/matrix_real_double_dense.pyx in sage.matrix.matrix_real_double_dense.Matrix_real_double_dense._sub_c_impl()

<type 'exceptions.ValueError'>: GSL routine had an error
sage:
```
I will add a doctest patch for this bug since it is currently missing.

Cheers,

Michael



---

archive/issue_comments_016686.json:
```json
{
    "body": "Ok, I now figured out that you also added a doctest for the bug you fixed. So disregard my comment about adding a doctest.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-18T03:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2468#issuecomment-16686",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I now figured out that you also added a doctest for the bug you fixed. So disregard my comment about adding a doctest.

Cheers,

Michael



---

archive/issue_events_005818.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-18T03:22:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2468#event-5818"
}
```



---

archive/issue_comments_016687.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-18T03:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2468#issuecomment-16687",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0



---

archive/issue_events_005819.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-18T03:22:49Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2468#event-5819"
}
```



---

archive/issue_events_005820.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-18T03:22:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2468#event-5820"
}
```



---

archive/issue_comments_016688.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T03:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2468#issuecomment-16688",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
