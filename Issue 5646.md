# Issue 5646: vectors over CDF allow a coercion from scalars

archive/issues_005646.json:
```json
{
    "body": "Assignee: was\n\nCC:  robertwb mjo\n\nKeywords: complex vector coercion\n\nThese are incompatible and I claim the first one is wrong!\n\n\n```\nsage: (CDF^2)(1)\n(1.0, 1.0)\nsage: (CC^2)(1)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage/sage/functions/riemann_theta.py in <module>()\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in __ca\\\nll__(self, e, coerce, copy, check)\n   4394         except AttributeError:\n   4395             pass\n-> 4396         return FreeModule_generic_field.__call__(self,e)\n   4397\n   4398 ###############################################################################\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in __ca\\\nll__(self, x, coerce, copy, check)\n    813             except ArithmeticError:\n    814                 raise ValueError, \"element (= %s) is not in free module\"%(x,)\n--> 815         return self._element_class(self, x, coerce, copy)\n    816\n    817     def is_submodule(self, other):\n\n/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/modules/free_module_element.so \\\nin sage.modules.free_module_element.FreeModuleElement_generic_dense.__init__ (sage/modules/free_module_element.c:15739)()\n\nTypeError: entries (=1) must be a list\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5646\n\n",
    "created_at": "2009-03-30T23:59:39Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "vectors over CDF allow a coercion from scalars",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5646",
    "user": "ncalexan"
}
```
Assignee: was

CC:  robertwb mjo

Keywords: complex vector coercion

These are incompatible and I claim the first one is wrong!


```
sage: (CDF^2)(1)
(1.0, 1.0)
sage: (CC^2)(1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage/sage/functions/riemann_theta.py in <module>()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in __ca\
ll__(self, e, coerce, copy, check)
   4394         except AttributeError:
   4395             pass
-> 4396         return FreeModule_generic_field.__call__(self,e)
   4397
   4398 ###############################################################################

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in __ca\
ll__(self, x, coerce, copy, check)
    813             except ArithmeticError:
    814                 raise ValueError, "element (= %s) is not in free module"%(x,)
--> 815         return self._element_class(self, x, coerce, copy)
    816
    817     def is_submodule(self, other):

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/modules/free_module_element.so \
in sage.modules.free_module_element.FreeModuleElement_generic_dense.__init__ (sage/modules/free_module_element.c:15739)()

TypeError: entries (=1) must be a list
```


Issue created by migration from https://trac.sagemath.org/ticket/5646





---

archive/issue_comments_044091.json:
```json
{
    "body": "I second that the first one is wrong, but this is not a coercion issue. \n\n\n```\nsage: (CDF^2).has_coerce_map_from(CDF)\nFalse\n```\n",
    "created_at": "2009-03-31T00:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5646#issuecomment-44091",
    "user": "robertwb"
}
```

I second that the first one is wrong, but this is not a coercion issue. 


```
sage: (CDF^2).has_coerce_map_from(CDF)
False
```




---

archive/issue_comments_044092.json:
```json
{
    "body": "Attachment [trac_5646.patch](tarball://root/attachments/some-uuid/ticket5646/trac_5646.patch) by was created at 2010-01-18 13:44:04",
    "created_at": "2010-01-18T13:44:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5646#issuecomment-44092",
    "user": "was"
}
```

Attachment [trac_5646.patch](tarball://root/attachments/some-uuid/ticket5646/trac_5646.patch) by was created at 2010-01-18 13:44:04



---

archive/issue_comments_044093.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-09T04:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5646#issuecomment-44093",
    "user": "mjo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044094.json:
```json
{
    "body": "(I think this was left 'new' by mistake)\n\nWhy is an exception made for zero? Is it just convenience? We have `(CDF^2).zero()` which does the same thing as far as I can tell.",
    "created_at": "2012-01-09T04:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5646#issuecomment-44094",
    "user": "mjo"
}
```

(I think this was left 'new' by mistake)

Why is an exception made for zero? Is it just convenience? We have `(CDF^2).zero()` which does the same thing as far as I can tell.



---

archive/issue_comments_044095.json:
```json
{
    "body": "Every vector space has a zero element, which is denoted by 0.  There are generally no elements in a vector space denoted by 1.",
    "created_at": "2012-03-18T17:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5646#issuecomment-44095",
    "user": "johanbosman"
}
```

Every vector space has a zero element, which is denoted by 0.  There are generally no elements in a vector space denoted by 1.



---

archive/issue_comments_044096.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-18T17:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5646#issuecomment-44096",
    "user": "johanbosman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044097.json:
```json
{
    "body": "Attachment [trac_5646_rebased.patch](tarball://root/attachments/some-uuid/ticket5646/trac_5646_rebased.patch) by jdemeyer created at 2012-03-23 16:33:35",
    "created_at": "2012-03-23T16:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5646#issuecomment-44097",
    "user": "jdemeyer"
}
```

Attachment [trac_5646_rebased.patch](tarball://root/attachments/some-uuid/ticket5646/trac_5646_rebased.patch) by jdemeyer created at 2012-03-23 16:33:35



---

archive/issue_comments_044098.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-28T10:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5646#issuecomment-44098",
    "user": "jdemeyer"
}
```

Resolution: fixed
