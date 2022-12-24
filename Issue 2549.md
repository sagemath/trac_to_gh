# Issue 2549: Implement VectorSpace over symbolic function ring

archive/issues_002549.json:
```json
{
    "body": "Assignee: cwitty\n\nI'd like to be able to create a vector space over a symbolic function ring:\n\n```\nvar('x,y,z');VS=VectorSpace(CallableSymbolicExpressionRing((x,y,z)),2)\n    raise TypeError, \"K must be a field\"\n<type 'exceptions.NotImplementedError'>:\n```\n\nI suppose the result of calling an element of K may be a field element or not, depending on what arguments are passed. Note that this is glossed-over in the case or SR, since `VectorSpace(SR,2)` works.\n\nPerhaps what is needed is a new type of object, a symbolic mapping whose signature is explicit, like:\n\n```\nf(x,y,z, RR)\n}}} or {{{\ng(x,y,z, (RR, RR, ZZ))\n```\n\nwhere the first syntax defines a mapping whose arguments are all in RR, the second a mapping with the last argument in ZZ.\n\nThis specifies the domain of the mapping but not the range. I suppose you could validate the output of the mapping to make sure that it was in (or coerced to?) the specified range (say RR or ZZ). Perhaps something like this is on the horizon, since it seems like a fairly deep architectural change?\n\nIssue created by migration from https://trac.sagemath.org/ticket/2549\n\n",
    "created_at": "2008-03-16T17:26:41Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Implement VectorSpace over symbolic function ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2549",
    "user": "edrex"
}
```
Assignee: cwitty

I'd like to be able to create a vector space over a symbolic function ring:

```
var('x,y,z');VS=VectorSpace(CallableSymbolicExpressionRing((x,y,z)),2)
    raise TypeError, "K must be a field"
<type 'exceptions.NotImplementedError'>:
```

I suppose the result of calling an element of K may be a field element or not, depending on what arguments are passed. Note that this is glossed-over in the case or SR, since `VectorSpace(SR,2)` works.

Perhaps what is needed is a new type of object, a symbolic mapping whose signature is explicit, like:

```
f(x,y,z, RR)
}}} or {{{
g(x,y,z, (RR, RR, ZZ))
```

where the first syntax defines a mapping whose arguments are all in RR, the second a mapping with the last argument in ZZ.

This specifies the domain of the mapping but not the range. I suppose you could validate the output of the mapping to make sure that it was in (or coerced to?) the specified range (say RR or ZZ). Perhaps something like this is on the horizon, since it seems like a fairly deep architectural change?

Issue created by migration from https://trac.sagemath.org/ticket/2549





---

archive/issue_comments_017406.json:
```json
{
    "body": "This is really a feature request for a type of object which can be used to represent a real vector field, which is effectively a mapping from R<sup>n</sup> to R<sup>n</sup>. The object should \n* have convenience methods for \n  * producing a quiver plot (via vector_field_plot)\n  * solving numerically (via ode_solver) and plotting solutions of the autonomous 1st-order differential equation represented by the vector field, with initial condition (x1,..,xn)\n* be callable (what is the vector at this point of the field?)\n* be have a fast float version which uses the fast-float versions of its component functions\n\nSince vector fields are just a special case of R<sup>m</sup> to R<sup>n</sup> maps (which are in turn special cases of ..., which is where my brain shuts off), perhaps VectorField should just be a special case/implementation of a more generic class of object.\n\nHere is the quick-n-dirty n-d VectorField class I have been using for my graduate-level diffeq hw, which implements the items above in a stand-alone, non-derived class: https://www.sagenb.org/home/pub/1745/",
    "created_at": "2008-03-20T23:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2549#issuecomment-17406",
    "user": "edrex"
}
```

This is really a feature request for a type of object which can be used to represent a real vector field, which is effectively a mapping from R<sup>n</sup> to R<sup>n</sup>. The object should 
* have convenience methods for 
  * producing a quiver plot (via vector_field_plot)
  * solving numerically (via ode_solver) and plotting solutions of the autonomous 1st-order differential equation represented by the vector field, with initial condition (x1,..,xn)
* be callable (what is the vector at this point of the field?)
* be have a fast float version which uses the fast-float versions of its component functions

Since vector fields are just a special case of R<sup>m</sup> to R<sup>n</sup> maps (which are in turn special cases of ..., which is where my brain shuts off), perhaps VectorField should just be a special case/implementation of a more generic class of object.

Here is the quick-n-dirty n-d VectorField class I have been using for my graduate-level diffeq hw, which implements the items above in a stand-alone, non-derived class: https://www.sagenb.org/home/pub/1745/



---

archive/issue_comments_017407.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-20T23:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2549#issuecomment-17407",
    "user": "edrex"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_017408.json:
```json
{
    "body": "See #2546 for a related ticket.",
    "created_at": "2009-02-13T17:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2549#issuecomment-17408",
    "user": "jason"
}
```

See #2546 for a related ticket.



---

archive/issue_comments_017409.json:
```json
{
    "body": "edrex, sagenb has been reset, which means your class is not available anymore.  Could you post it here so that whoever wants to tackle this ticket may have a place to start from?",
    "created_at": "2009-02-13T17:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2549#issuecomment-17409",
    "user": "jason"
}
```

edrex, sagenb has been reset, which means your class is not available anymore.  Could you post it here so that whoever wants to tackle this ticket may have a place to start from?



---

archive/issue_comments_017410.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-15T18:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2549#issuecomment-17410",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_017411.json:
```json
{
    "body": "Can this ticket be closed? The specific feature it was asking for now (sort of) exists:\n\n```\nsage: var('x,y,z');VS=VectorSpace(CallableSymbolicExpressionRing((x,y,z)),2)\n(x, y, z)\nsage: VS.an_element()\n(x, y, z) |--> (1, 0)\n```\n\nand work on various kinds of tensor fields is ongoing as part of SageManifolds (#14865, #15916).",
    "created_at": "2014-03-15T18:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2549#issuecomment-17411",
    "user": "mmezzarobba"
}
```

Can this ticket be closed? The specific feature it was asking for now (sort of) exists:

```
sage: var('x,y,z');VS=VectorSpace(CallableSymbolicExpressionRing((x,y,z)),2)
(x, y, z)
sage: VS.an_element()
(x, y, z) |--> (1, 0)
```

and work on various kinds of tensor fields is ongoing as part of SageManifolds (#14865, #15916).



---

archive/issue_comments_017412.json:
```json
{
    "body": "I agree that this can be closed.",
    "created_at": "2014-03-18T09:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2549#issuecomment-17412",
    "user": "chapoton"
}
```

I agree that this can be closed.



---

archive/issue_comments_017413.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-18T09:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2549#issuecomment-17413",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_017414.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-03-19T04:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2549#issuecomment-17414",
    "user": "vbraun"
}
```

Resolution: fixed
