# Issue 8481: lift doesn't work for vector space homomorphisms

archive/issues_008481.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: V = QQ**2\nsage: W = QQ**2\nsage: f = V.hom([W.1, W.1])\nsage: f.lift(W.1)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Users/palmieri/<ipython console> in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/modules/free_module_morphism.pyc in lift(self, x)\n    337         x = self.codomain()(x)\n    338         A = self.matrix()\n--> 339         H, U = A.hermite_form(transformation=True,include_zero_rows=False)\n    340         Y = H.solve_left(vector(self.codomain().coordinates(x)))\n    341         C = Y*U\n\n...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8481\n\n",
    "created_at": "2010-03-07T22:49:07Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "lift doesn't work for vector space homomorphisms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8481",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @williamstein


```
sage: V = QQ**2
sage: W = QQ**2
sage: f = V.hom([W.1, W.1])
sage: f.lift(W.1)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/palmieri/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/modules/free_module_morphism.pyc in lift(self, x)
    337         x = self.codomain()(x)
    338         A = self.matrix()
--> 339         H, U = A.hermite_form(transformation=True,include_zero_rows=False)
    340         Y = H.solve_left(vector(self.codomain().coordinates(x)))
    341         C = Y*U

...
```


Issue created by migration from https://trac.sagemath.org/ticket/8481





---

archive/issue_comments_076308.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-08T23:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76308",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076309.json:
```json
{
    "body": "Attachment [trac_8481-lift.patch](tarball://root/attachments/some-uuid/ticket8481/trac_8481-lift.patch) by @jhpalmieri created at 2010-03-08 23:55:07",
    "created_at": "2010-03-08T23:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76309",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8481-lift.patch](tarball://root/attachments/some-uuid/ticket8481/trac_8481-lift.patch) by @jhpalmieri created at 2010-03-08 23:55:07



---

archive/issue_comments_076310.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-05T02:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76310",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076311.json:
```json
{
    "body": "1. Can you change this to only do check=True when the base ring is *not* a field:\n\n```\n        5408\t \t                    check=False, copy=False, coerce=False) \n \t5408\t                    check=True, copy=False, coerce=False) \n```\n\nOr, better yet, always do check=False unless the components of v are not all in the base ring.   The problem is that check=True could be *massively* expensive -- you could add hours to the runtimes of real-world computations with this one little change.  \n\n2. I'm happy with all the other code.  \n\nI'm running tests and will report in a moment.",
    "created_at": "2010-04-05T02:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76311",
    "user": "https://github.com/williamstein"
}
```

1. Can you change this to only do check=True when the base ring is *not* a field:

```
        5408	 	                    check=False, copy=False, coerce=False) 
 	5408	                    check=True, copy=False, coerce=False) 
```

Or, better yet, always do check=False unless the components of v are not all in the base ring.   The problem is that check=True could be *massively* expensive -- you could add hours to the runtimes of real-world computations with this one little change.  

2. I'm happy with all the other code.  

I'm running tests and will report in a moment.



---

archive/issue_comments_076312.json:
```json
{
    "body": "All doctests pass fine.",
    "created_at": "2010-04-05T03:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76312",
    "user": "https://github.com/williamstein"
}
```

All doctests pass fine.



---

archive/issue_comments_076313.json:
```json
{
    "body": "Attachment [trac_8481-lift.v2.patch](tarball://root/attachments/some-uuid/ticket8481/trac_8481-lift.v2.patch) by @jhpalmieri created at 2010-04-06 00:00:00\n\nHere's a new patch.  I hope the speed hit isn't too bad with this one.",
    "created_at": "2010-04-06T00:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76313",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8481-lift.v2.patch](tarball://root/attachments/some-uuid/ticket8481/trac_8481-lift.v2.patch) by @jhpalmieri created at 2010-04-06 00:00:00

Here's a new patch.  I hope the speed hit isn't too bad with this one.



---

archive/issue_comments_076314.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-06T00:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76314",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076315.json:
```json
{
    "body": "OK, looks good!",
    "created_at": "2010-04-06T05:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76315",
    "user": "https://github.com/williamstein"
}
```

OK, looks good!



---

archive/issue_comments_076316.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-06T05:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76316",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076317.json:
```json
{
    "body": "Merged \"trac_8481-lift.v2.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-15T23:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76317",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8481-lift.v2.patch" into 4.4.alpha0.



---

archive/issue_comments_076318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8481#issuecomment-76318",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
