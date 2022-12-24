# Issue 6376: serious bug in _maxima_init_ method for formal derivatives with new symbolics

archive/issues_006376.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @golam-m-hossain @mwhansen\n\n\n```\nsage: f(x) = function('f',x)\nsage: g = f(-x).diff(x); g\n-D[0](f)(-x)\nsage: g._maxima_init_()\n\"(diff('f(x), x, 1))*(-1)\"\n```\n\n\nNotice that the `-x` inside f is totally ignored!  This is because of code in the derivative method around line 454 of `sage/symbolic/expression_conversion.py`\n\nChanging the line\n\n```\nargs = ex.args()\n```\n\n\nto \n\n```\nargs = ex.operands()\n```\n\n\n\"fixes\" the problem, in that a NotImplementedError gets raised, instead of a wrong result returned.  This is **way** better than the current situation, and we better fix this asap.  \n\nA better fix of course is to implement proper conversion. mhansen wrote this code, so maybe it would be easy for him.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6376\n\n",
    "created_at": "2009-06-21T14:13:14Z",
    "labels": [
        "calculus",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "serious bug in _maxima_init_ method for formal derivatives with new symbolics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6376",
    "user": "@williamstein"
}
```
Assignee: @burcin

CC:  @golam-m-hossain @mwhansen


```
sage: f(x) = function('f',x)
sage: g = f(-x).diff(x); g
-D[0](f)(-x)
sage: g._maxima_init_()
"(diff('f(x), x, 1))*(-1)"
```


Notice that the `-x` inside f is totally ignored!  This is because of code in the derivative method around line 454 of `sage/symbolic/expression_conversion.py`

Changing the line

```
args = ex.args()
```


to 

```
args = ex.operands()
```


"fixes" the problem, in that a NotImplementedError gets raised, instead of a wrong result returned.  This is **way** better than the current situation, and we better fix this asap.  

A better fix of course is to implement proper conversion. mhansen wrote this code, so maybe it would be easy for him.


Issue created by migration from https://trac.sagemath.org/ticket/6376





---

archive/issue_comments_051021.json:
```json
{
    "body": "Mike, do you have any time to look at this?\n\nThanks.\n\nBurcin",
    "created_at": "2009-08-05T08:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6376#issuecomment-51021",
    "user": "@burcin"
}
```

Mike, do you have any time to look at this?

Thanks.

Burcin



---

archive/issue_comments_051022.json:
```json
{
    "body": "fixed with patch at  #7401 which waits for review.\n\n\n```\nsage: f(x) = function('f',x)\nsage: g = f(-x).diff(x); g\n-D[0](f)(-x)\nsage: g._maxima_init_()\n\"(at(diff('f(dummy_var_der), dummy_var_der,1),dummy_var_der=-x))*(-1)\"\n```\n",
    "created_at": "2009-11-17T14:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6376#issuecomment-51022",
    "user": "@robert-marik"
}
```

fixed with patch at  #7401 which waits for review.


```
sage: f(x) = function('f',x)
sage: g = f(-x).diff(x); g
-D[0](f)(-x)
sage: g._maxima_init_()
"(at(diff('f(dummy_var_der), dummy_var_der,1),dummy_var_der=-x))*(-1)"
```




---

archive/issue_comments_051023.json:
```json
{
    "body": "The patch is attached to #7401\n\n#6376 is not doctested, since I did not know about this issue when finished patch for #7401. It could be easily doctested, but doctests in #7401 are equivalent to #6376.",
    "created_at": "2009-11-17T14:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6376#issuecomment-51023",
    "user": "@robert-marik"
}
```

The patch is attached to #7401

#6376 is not doctested, since I did not know about this issue when finished patch for #7401. It could be easily doctested, but doctests in #7401 are equivalent to #6376.



---

archive/issue_comments_051024.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-17T14:46:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6376#issuecomment-51024",
    "user": "@robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051025.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-17T16:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6376#issuecomment-51025",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051026.json:
```json
{
    "body": "Okay, this seems okay.  \n\nTo release manager: please close this as fixed once #6376 is merged.",
    "created_at": "2009-11-17T16:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6376#issuecomment-51026",
    "user": "@kcrisman"
}
```

Okay, this seems okay.  

To release manager: please close this as fixed once #6376 is merged.



---

archive/issue_comments_051027.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-11-19T17:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6376#issuecomment-51027",
    "user": "@mwhansen"
}
```

Resolution: duplicate
