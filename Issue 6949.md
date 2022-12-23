# Issue 6949: add symbolic max and min functions

archive/issues_006949.json:
```json
{
    "body": "CC:  jason\n\nMatt Riesler wrote on sage-support:\n\n\n```\nIs it possible to have max behave as you would expect with a symbolic\nexpression, i.e. wait until you evaluate it or restrict the domain  to\ncheck what is the maximum of the two or more values.\n```\n\n\nThen kcrisman:\n\n\n```\nMight there be a way to do something that doesn't conflict with the\nbuiltin max function in the same way as the (nearly reviewed) #3587\nseems to avoid conflict with the builtin sum function?  This would be\npretty useful, as currently:\n\nsage: var('x,y')\n(x, y)\nsage: max(x,y)\nx\nsage: f(x)=1+x;g(x)=2-x\nsage: max(f,g)\nx |--> x + 1\n\nwhich last result is... debatable.\n```\n\n\nHere is a the thread, which has a simple minded implementation for symbolic max:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/aead15de586984d8\n\n\nWe should make sure the symbolic implementations don't slow down the current builtin python `max()` and `min()` too much. If they do, these functions should still be available under a different name.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6949\n\n",
    "created_at": "2009-09-17T14:04:24Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "title": "add symbolic max and min functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6949",
    "user": "burcin"
}
```
CC:  jason

Matt Riesler wrote on sage-support:


```
Is it possible to have max behave as you would expect with a symbolic
expression, i.e. wait until you evaluate it or restrict the domain  to
check what is the maximum of the two or more values.
```


Then kcrisman:


```
Might there be a way to do something that doesn't conflict with the
builtin max function in the same way as the (nearly reviewed) #3587
seems to avoid conflict with the builtin sum function?  This would be
pretty useful, as currently:

sage: var('x,y')
(x, y)
sage: max(x,y)
x
sage: f(x)=1+x;g(x)=2-x
sage: max(f,g)
x |--> x + 1

which last result is... debatable.
```


Here is a the thread, which has a simple minded implementation for symbolic max:

http://groups.google.com/group/sage-support/browse_thread/thread/aead15de586984d8


We should make sure the symbolic implementations don't slow down the current builtin python `max()` and `min()` too much. If they do, these functions should still be available under a different name.

Issue created by migration from https://trac.sagemath.org/ticket/6949





---

archive/issue_comments_057455.json:
```json
{
    "body": "see also #8508",
    "created_at": "2010-03-12T19:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57455",
    "user": "zimmerma"
}
```

see also #8508



---

archive/issue_comments_057456.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-02T21:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57456",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057457.json:
```json
{
    "body": "attachment:trac_6949-symbolic_min_max.patch provides basic implementations of `max_symbolic()` and `min_symbolic()` functions that work as expected when the input contains symbolic expressions.\n\nThe symbolic versions are significantly slower than Python's builtin `min()` and `max()`, so replacing the builtin functions with these is not possible at this point.",
    "created_at": "2010-04-02T21:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57457",
    "user": "burcin"
}
```

attachment:trac_6949-symbolic_min_max.patch provides basic implementations of `max_symbolic()` and `min_symbolic()` functions that work as expected when the input contains symbolic expressions.

The symbolic versions are significantly slower than Python's builtin `min()` and `max()`, so replacing the builtin functions with these is not possible at this point.



---

archive/issue_comments_057458.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-06T15:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57458",
    "user": "burcin"
}
```

Attachment



---

archive/issue_comments_057459.json:
```json
{
    "body": "Set assignee to burcin.",
    "created_at": "2010-04-06T15:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57459",
    "user": "burcin"
}
```

Set assignee to burcin.



---

archive/issue_comments_057460.json:
```json
{
    "body": "I updated attachment:trac_6949-symbolic_min_max.patch to fix a minor doctest error in sage/symbolic/ring.pyx.",
    "created_at": "2010-04-06T15:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57460",
    "user": "burcin"
}
```

I updated attachment:trac_6949-symbolic_min_max.patch to fix a minor doctest error in sage/symbolic/ring.pyx.



---

archive/issue_comments_057461.json:
```json
{
    "body": "I applied the patch on top of 4.3.5:\n\n```\nsage: f(x) = max_symbolic(sin(x), cos(x))\nsage: f(0)\n1\nsage: f\nx |--> max(sin(x), cos(x))\nsage: f(1)\nmax(sin(1), cos(1))\n```\n\nSo far, so good. But:\n\n```\nsage: N(f(1))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/opt/sage-4.3.5/<ipython console> in <module>()\n\n/opt/sage-4.3.5/local/lib/python2.6/site-packages/sage/misc/functional.pyc in numerical_approx(x, prec, digits)\n   1161             prec = int((digits+1) * 3.32192) + 1\n   1162     try:\n-> 1163         return x.numerical_approx(prec)\n   1164     except AttributeError:\n   1165         from sage.rings.complex_double import is_ComplexDoubleElement\n\n/opt/sage-4.3.5/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17043)()\n\nTypeError: cannot evaluate symbolic expression numerically\n```\n",
    "created_at": "2010-04-29T13:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57461",
    "user": "lfousse"
}
```

I applied the patch on top of 4.3.5:

```
sage: f(x) = max_symbolic(sin(x), cos(x))
sage: f(0)
1
sage: f
x |--> max(sin(x), cos(x))
sage: f(1)
max(sin(1), cos(1))
```

So far, so good. But:

```
sage: N(f(1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-4.3.5/<ipython console> in <module>()

/opt/sage-4.3.5/local/lib/python2.6/site-packages/sage/misc/functional.pyc in numerical_approx(x, prec, digits)
   1161             prec = int((digits+1) * 3.32192) + 1
   1162     try:
-> 1163         return x.numerical_approx(prec)
   1164     except AttributeError:
   1165         from sage.rings.complex_double import is_ComplexDoubleElement

/opt/sage-4.3.5/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17043)()

TypeError: cannot evaluate symbolic expression numerically
```




---

archive/issue_comments_057462.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-29T13:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57462",
    "user": "lfousse"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_057463.json:
```json
{
    "body": "add evalf methods, put common eval and __call__ methods to base class",
    "created_at": "2010-05-05T04:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57463",
    "user": "burcin"
}
```

add evalf methods, put common eval and __call__ methods to base class



---

archive/issue_comments_057464.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-05T04:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57464",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057465.json:
```json
{
    "body": "Attachment\n\nThanks for the review.\n\nThe new patch attachment:trac_6949-symbolic_min_max.take2.patch replaces the previous one, and implements `_evalf_()` methods for numeric evaluation. I also created a base class with the common code from `__call__()` and `_eval_()` methods.\n\nCan you take another look?",
    "created_at": "2010-05-05T04:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57465",
    "user": "burcin"
}
```

Attachment

Thanks for the review.

The new patch attachment:trac_6949-symbolic_min_max.take2.patch replaces the previous one, and implements `_evalf_()` methods for numeric evaluation. I also created a base class with the common code from `__call__()` and `_eval_()` methods.

Can you take another look?



---

archive/issue_comments_057466.json:
```json
{
    "body": "Thanks for the updated patch. I applied it on top of 4.4. I can verify the previously reported problem for numerical evaluation works. I have however a new problem:\n\n```\nsage: f(x) = max_symbolic(sin(x), cos(x))\nsage: N(integral(f, x, 0, 1))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/opt/sage-4.4/<ipython console> in <module>()\n\n/opt/sage-4.4/local/lib/python2.6/site-packages/sage/misc/functional.pyc in numerical_approx(x, prec, digits)\n   1163             prec = int((digits+1) * 3.32192) + 1\n   1164     try:\n-> 1165         return x.numerical_approx(prec)\n   1166     except AttributeError:\n   1167         from sage.rings.complex_double import is_ComplexDoubleElement\n\n/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:16928)()\n\n/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._convert (sage/symbolic/expression.cpp:4677)()\n\n/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in _evalf_(self, *args, **kwds)\n    155             TypeError: cannot evaluate symbolic expression numerically\n    156         \"\"\"\n--> 157         return max_symbolic(args)\n    158\n    159 max_symbolic = MaxSymbolic()\n\n/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in __call__(self, *args, **kwds)\n     79                 return args\n     80\n---> 81         return BuiltinFunction.__call__(self, *args, **kwds)\n     82\n     83 class MaxSymbolic(MinMax_base):\n\n/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4359)()\n\n/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in _eval_(self, *args)\n    136             ValueError: number of arguments must be > 0\n    137         \"\"\"\n--> 138         return self.eval_helper(max_symbolic, builtin_max, None, args)\n    139\n    140     def _evalf_(self, *args, **kwds):\n\n/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in eval_helper(self, this_f, builtin_f, initial_val, args)\n     51\n     52         symb_args.append(res)\n---> 53         return this_f(*symb_args)\n     54\n     55     def __call__(self, *args, **kwds):\n\n/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in __call__(self, *args, **kwds)\n     79                 return args\n     80\n---> 81         return BuiltinFunction.__call__(self, *args, **kwds)\n     82\n     83 class MaxSymbolic(MinMax_base):\n\n/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4192)()\n\nTypeError: cannot coerce arguments: no canonical coercion from <type 'NoneType'> to Symbolic Ring\n```\n\nI don't know if the problem is with integrate or max_symbolic.",
    "created_at": "2010-05-05T07:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57466",
    "user": "lfousse"
}
```

Thanks for the updated patch. I applied it on top of 4.4. I can verify the previously reported problem for numerical evaluation works. I have however a new problem:

```
sage: f(x) = max_symbolic(sin(x), cos(x))
sage: N(integral(f, x, 0, 1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-4.4/<ipython console> in <module>()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/misc/functional.pyc in numerical_approx(x, prec, digits)
   1163             prec = int((digits+1) * 3.32192) + 1
   1164     try:
-> 1165         return x.numerical_approx(prec)
   1166     except AttributeError:
   1167         from sage.rings.complex_double import is_ComplexDoubleElement

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:16928)()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._convert (sage/symbolic/expression.cpp:4677)()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in _evalf_(self, *args, **kwds)
    155             TypeError: cannot evaluate symbolic expression numerically
    156         """
--> 157         return max_symbolic(args)
    158
    159 max_symbolic = MaxSymbolic()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in __call__(self, *args, **kwds)
     79                 return args
     80
---> 81         return BuiltinFunction.__call__(self, *args, **kwds)
     82
     83 class MaxSymbolic(MinMax_base):

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4359)()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in _eval_(self, *args)
    136             ValueError: number of arguments must be > 0
    137         """
--> 138         return self.eval_helper(max_symbolic, builtin_max, None, args)
    139
    140     def _evalf_(self, *args, **kwds):

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in eval_helper(self, this_f, builtin_f, initial_val, args)
     51
     52         symb_args.append(res)
---> 53         return this_f(*symb_args)
     54
     55     def __call__(self, *args, **kwds):

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in __call__(self, *args, **kwds)
     79                 return args
     80
---> 81         return BuiltinFunction.__call__(self, *args, **kwds)
     82
     83 class MaxSymbolic(MinMax_base):

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4192)()

TypeError: cannot coerce arguments: no canonical coercion from <type 'NoneType'> to Symbolic Ring
```

I don't know if the problem is with integrate or max_symbolic.



---

archive/issue_comments_057467.json:
```json
{
    "body": "Attachment\n\napply only this patch",
    "created_at": "2010-05-05T15:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57467",
    "user": "burcin"
}
```

Attachment

apply only this patch



---

archive/issue_comments_057468.json:
```json
{
    "body": "Thanks a lot for testing this. I uploaded a new patch in attachment:trac_6949-symbolic_min_max.take3.patch which should cover many corner cases not handled properly before. The aim is to make `{max,min}_symbolic()` behave almost identical to the builtin `min()` and `max()`.\n\nCan you try and break it again? :)",
    "created_at": "2010-05-05T15:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57468",
    "user": "burcin"
}
```

Thanks a lot for testing this. I uploaded a new patch in attachment:trac_6949-symbolic_min_max.take3.patch which should cover many corner cases not handled properly before. The aim is to make `{max,min}_symbolic()` behave almost identical to the builtin `min()` and `max()`.

Can you try and break it again? :)



---

archive/issue_comments_057469.json:
```json
{
    "body": "Applied on top of 4.4.1 this time. I could not break it with my tests, and I also checked -testall, -coverage etc. as per the patch review guidelines. So that would be a positive review. Thanks!",
    "created_at": "2010-05-06T05:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57469",
    "user": "lfousse"
}
```

Applied on top of 4.4.1 this time. I could not break it with my tests, and I also checked -testall, -coverage etc. as per the patch review guidelines. So that would be a positive review. Thanks!



---

archive/issue_comments_057470.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-06T05:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57470",
    "user": "lfousse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T22:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57471",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057472.json:
```json
{
    "body": "Merged [trac_6949-symbolic_min_max.take3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6949/trac_6949-symbolic_min_max.take3.patch).",
    "created_at": "2010-05-08T22:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57472",
    "user": "mvngu"
}
```

Merged [trac_6949-symbolic_min_max.take3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6949/trac_6949-symbolic_min_max.take3.patch).



---

archive/issue_comments_057473.json:
```json
{
    "body": "See #13857 for adding this to the reference manual, which somehow never happened but would be worthy considering how many emails we still get about this situation.",
    "created_at": "2012-12-21T14:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6949#issuecomment-57473",
    "user": "kcrisman"
}
```

See #13857 for adding this to the reference manual, which somehow never happened but would be worthy considering how many emails we still get about this situation.
