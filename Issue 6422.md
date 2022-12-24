# Issue 6422: [with patch, needs review] make sage.symbolic.expression.Expression.__init__ usable

archive/issues_006422.json:
```json
{
    "body": "From sage-support:\n\n\n```\nOn Fri, 26 Jun 2009 06:14:13 -0700 (PDT)\nNicolas <nicolas.fressengeas@gmail.com> wrote:\n\n> \n> I think there is definitely a bug in the __init__ method of the\n> Expression class.\n> Probably it has not been tracked down because this method is quasi\n> never used in the new version of symbolics. However, it raises\n> problems when one wants to derive a suclass from Expression.\n> \n> The bug is described in details here for the 4.0.1 version. It is\n> still present in the 4.0.2 :\n> \n> http://groups.google.com/group/sage-support/browse_thread/thread/d50dc3bc2bdbeab0/34798c0585fc034f?lnk=gst&q=nicolas#34798c0585fc034f\n> \n> Burcin provided a simple solution that works wonderfully, in the same\n> thread.\n> \n> Should we issue a ticket for this to be included in the future\n> versions ?\n```\n\n\nThe patch mentioned above is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6422\n\n",
    "created_at": "2009-06-26T14:13:50Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] make sage.symbolic.expression.Expression.__init__ usable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6422",
    "user": "burcin"
}
```
From sage-support:


```
On Fri, 26 Jun 2009 06:14:13 -0700 (PDT)
Nicolas <nicolas.fressengeas@gmail.com> wrote:

> 
> I think there is definitely a bug in the __init__ method of the
> Expression class.
> Probably it has not been tracked down because this method is quasi
> never used in the new version of symbolics. However, it raises
> problems when one wants to derive a suclass from Expression.
> 
> The bug is described in details here for the 4.0.1 version. It is
> still present in the 4.0.2 :
> 
> http://groups.google.com/group/sage-support/browse_thread/thread/d50dc3bc2bdbeab0/34798c0585fc034f?lnk=gst&q=nicolas#34798c0585fc034f
> 
> Burcin provided a simple solution that works wonderfully, in the same
> thread.
> 
> Should we issue a ticket for this to be included in the future
> versions ?
```


The patch mentioned above is attached.

Issue created by migration from https://trac.sagemath.org/ticket/6422





---

archive/issue_comments_051561.json:
```json
{
    "body": "Upon applying this to sage-4.1.alpha1 I get failures:\n\n```\nsage -t  devel/sage/sage/symbolic/expression.pyx\n/scratch/wstein/build/sage-4.1.alpha1/local/lib/python/site-packages/sage/misc/misc.py:1900: DeprecationWarning: functions overriding warnings.showwarning() must support the 'line' argument\n  warn(message, DeprecationWarning, stacklevel=3)\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.alpha1/devel/sage-main/sage/symbolic/expression.pyx\", line 219:\n    sage: sage.symbolic.expression.Expression(SR)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[2]>\", line 1, in <module>\n        sage.symbolic.expression.Expression(SR)###line 219:\n    sage: sage.symbolic.expression.Expression(SR)\n      File \"expression.pyx\", line 224, in sage.symbolic.expression.Expression.__init__ (sage/symbolic/expression.cpp:2761)\n        cdef Expression exp = self.coerce_in(x)\n      File \"expression.pyx\", line 1495, in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:9537)\n        return self._parent._coerce_(z)\n    AttributeError: 'NoneType' object has no attribute '_coerce_'\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.alpha1/devel/sage-main/sage/symbolic/expression.pyx\", line 221:\n    sage: sage.symbolic.expression.Expression(SR, 5)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[3]>\", line 1, in <module>\n        sage.symbolic.expression.Expression(SR, Integer(5))###line 221:\n    sage: sage.symbolic.expression.Expression(SR, 5)\n      File \"expression.pyx\", line 224, in sage.symbolic.expression.Expression.__init__ (sage/symbolic/expression.cpp:2761)\n        cdef Expression exp = self.coerce_in(x)\n      File \"expression.pyx\", line 1495, in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:9537)\n        return self._parent._coerce_(z)\n    AttributeError: 'NoneType' object has no attribute '_coerce_'\n**********************************************************************\n1 items had failures:\n   2 of   4 in __main__.example_4\n```\n",
    "created_at": "2009-06-26T15:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6422#issuecomment-51561",
    "user": "was"
}
```

Upon applying this to sage-4.1.alpha1 I get failures:

```
sage -t  devel/sage/sage/symbolic/expression.pyx
/scratch/wstein/build/sage-4.1.alpha1/local/lib/python/site-packages/sage/misc/misc.py:1900: DeprecationWarning: functions overriding warnings.showwarning() must support the 'line' argument
  warn(message, DeprecationWarning, stacklevel=3)
**********************************************************************
File "/scratch/wstein/build/sage-4.1.alpha1/devel/sage-main/sage/symbolic/expression.pyx", line 219:
    sage: sage.symbolic.expression.Expression(SR)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[2]>", line 1, in <module>
        sage.symbolic.expression.Expression(SR)###line 219:
    sage: sage.symbolic.expression.Expression(SR)
      File "expression.pyx", line 224, in sage.symbolic.expression.Expression.__init__ (sage/symbolic/expression.cpp:2761)
        cdef Expression exp = self.coerce_in(x)
      File "expression.pyx", line 1495, in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:9537)
        return self._parent._coerce_(z)
    AttributeError: 'NoneType' object has no attribute '_coerce_'
**********************************************************************
File "/scratch/wstein/build/sage-4.1.alpha1/devel/sage-main/sage/symbolic/expression.pyx", line 221:
    sage: sage.symbolic.expression.Expression(SR, 5)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        sage.symbolic.expression.Expression(SR, Integer(5))###line 221:
    sage: sage.symbolic.expression.Expression(SR, 5)
      File "expression.pyx", line 224, in sage.symbolic.expression.Expression.__init__ (sage/symbolic/expression.cpp:2761)
        cdef Expression exp = self.coerce_in(x)
      File "expression.pyx", line 1495, in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:9537)
        return self._parent._coerce_(z)
    AttributeError: 'NoneType' object has no attribute '_coerce_'
**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_4
```




---

archive/issue_comments_051562.json:
```json
{
    "body": "second try at fixing Expression.__init__",
    "created_at": "2009-06-27T15:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6422#issuecomment-51562",
    "user": "burcin"
}
```

second try at fixing Expression.__init__



---

archive/issue_comments_051563.json:
```json
{
    "body": "Attachment [trac_6422-expression_init.patch](tarball://root/attachments/some-uuid/ticket6422/trac_6422-expression_init.patch) by burcin created at 2009-06-27 15:24:53\n\nI attached a new patch which sets `self._parent` first, fixing the doctest problems above. I also added a new test for the problem reported by Nicolas in his initial message.",
    "created_at": "2009-06-27T15:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6422#issuecomment-51563",
    "user": "burcin"
}
```

Attachment [trac_6422-expression_init.patch](tarball://root/attachments/some-uuid/ticket6422/trac_6422-expression_init.patch) by burcin created at 2009-06-27 15:24:53

I attached a new patch which sets `self._parent` first, fixing the doctest problems above. I also added a new test for the problem reported by Nicolas in his initial message.



---

archive/issue_comments_051564.json:
```json
{
    "body": "Set assignee to burcin.",
    "created_at": "2009-06-27T15:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6422#issuecomment-51564",
    "user": "burcin"
}
```

Set assignee to burcin.



---

archive/issue_comments_051565.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-27T15:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6422#issuecomment-51565",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_051566.json:
```json
{
    "body": "Changing keywords from \"\" to \"expression init\".",
    "created_at": "2009-07-17T09:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6422#issuecomment-51566",
    "user": "AlexGhitza"
}
```

Changing keywords from "" to "expression init".



---

archive/issue_comments_051567.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-07-17T10:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6422#issuecomment-51567",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_051568.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-18T16:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6422#issuecomment-51568",
    "user": "mvngu"
}
```

Resolution: fixed
