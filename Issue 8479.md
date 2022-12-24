# Issue 8479: [with patch, needs review] numpy support for more basic functions

archive/issues_008479.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  jason\n\nKeywords: numpy\n\nThe attached patch adds numpy support for the functions:\n\ncoth, sech, csch, arccoth, arcsech, arccsch, ceil, floor,\nsqrt, real_part, imag_part, sec, csc, cot, arccot, arccsc,\narcsec\n\nIssue created by migration from https://trac.sagemath.org/ticket/8479\n\n",
    "created_at": "2010-03-07T21:19:39Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "[with patch, needs review] numpy support for more basic functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8479",
    "user": "whuss"
}
```
Assignee: AlexGhitza

CC:  jason

Keywords: numpy

The attached patch adds numpy support for the functions:

coth, sech, csch, arccoth, arcsech, arccsch, ceil, floor,
sqrt, real_part, imag_part, sec, csc, cot, arccot, arccsc,
arcsec

Issue created by migration from https://trac.sagemath.org/ticket/8479





---

archive/issue_comments_076416.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76416",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_076417.json:
```json
{
    "body": "I hadn't seen this before! It's an enhancement to symbolic functions, so I'm changing the component to `symbolics`. \n\nWe don't use tags on the subject line to mark tickets for review anymore, see the `Action` options right above the `Submit` button.",
    "created_at": "2010-04-09T18:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76417",
    "user": "burcin"
}
```

I hadn't seen this before! It's an enhancement to symbolic functions, so I'm changing the component to `symbolics`. 

We don't use tags on the subject line to mark tickets for review anymore, see the `Action` options right above the `Submit` button.



---

archive/issue_comments_076418.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-09T18:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76418",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076419.json:
```json
{
    "body": "Changing component from basic arithmetic to symbolics.",
    "created_at": "2010-04-09T18:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76419",
    "user": "burcin"
}
```

Changing component from basic arithmetic to symbolics.



---

archive/issue_comments_076420.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-05-06T21:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76420",
    "user": "burcin"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_076421.json:
```json
{
    "body": "The patch looks really good and addresses an important problem. I have a few minor remarks/questions before I give a positive review:\n\n* Can we change the test in sage.functions.other.sqrt() to work without importing numpy? I didn't check the effects on performance, but `sqrt()` gets used a lot, so keeping it free of `numpy` unless absolutely necessary would be good.\n* All the examples in the doctests are for functions with a single argument. Is there any reason to move the check in `sage.symbolic.function.Function.__call__()` to try all arguments? We should also consider moving this check to `sage.symbolic.function.BuiltinFunction.__call__()`.",
    "created_at": "2010-05-06T21:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76421",
    "user": "burcin"
}
```

The patch looks really good and addresses an important problem. I have a few minor remarks/questions before I give a positive review:

* Can we change the test in sage.functions.other.sqrt() to work without importing numpy? I didn't check the effects on performance, but `sqrt()` gets used a lot, so keeping it free of `numpy` unless absolutely necessary would be good.
* All the examples in the doctests are for functions with a single argument. Is there any reason to move the check in `sage.symbolic.function.Function.__call__()` to try all arguments? We should also consider moving this check to `sage.symbolic.function.BuiltinFunction.__call__()`.



---

archive/issue_comments_076422.json:
```json
{
    "body": "Attachment [trac-8479-numpy_functions.patch](tarball://root/attachments/some-uuid/ticket8479/trac-8479-numpy_functions.patch) by whuss created at 2010-05-07 09:13:49",
    "created_at": "2010-05-07T09:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76422",
    "user": "whuss"
}
```

Attachment [trac-8479-numpy_functions.patch](tarball://root/attachments/some-uuid/ticket8479/trac-8479-numpy_functions.patch) by whuss created at 2010-05-07 09:13:49



---

archive/issue_comments_076423.json:
```json
{
    "body": "Replying to [comment:4 burcin]:\n\n> * Can we change the test in sage.functions.other.sqrt() to work without importing numpy?\n\ndone in the new patch\n\n> * All the examples in the doctests are for functions with a single argument. Is there any reason to move the check in `sage.symbolic.function.Function.__call__()` to try all arguments?\n\nIn the original patch I forgot to add tests for atan2, which also didn't work with numpy before. The tests are now included.\n\n> We should also consider moving this check to `sage.symbolic.function.BuiltinFunction.__call__()`.\n\nWhy would this be better? It currently does not have a `__call__` method.",
    "created_at": "2010-05-07T09:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76423",
    "user": "whuss"
}
```

Replying to [comment:4 burcin]:

> * Can we change the test in sage.functions.other.sqrt() to work without importing numpy?

done in the new patch

> * All the examples in the doctests are for functions with a single argument. Is there any reason to move the check in `sage.symbolic.function.Function.__call__()` to try all arguments?

In the original patch I forgot to add tests for atan2, which also didn't work with numpy before. The tests are now included.

> We should also consider moving this check to `sage.symbolic.function.BuiltinFunction.__call__()`.

Why would this be better? It currently does not have a `__call__` method.



---

archive/issue_comments_076424.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-05-07T09:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76424",
    "user": "whuss"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_076425.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2010-05-07T14:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76425",
    "user": "burcin"
}
```

apply only this patch



---

archive/issue_comments_076426.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-07T14:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76426",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076427.json:
```json
{
    "body": "Attachment [trac-8479-numpy_functions.take2.patch](tarball://root/attachments/some-uuid/ticket8479/trac-8479-numpy_functions.take2.patch) by burcin created at 2010-05-07 14:53:45\n\nThanks for the quick response.\n\nReplying to [comment:5 whuss]:\n> Replying to [comment:4 burcin]:\n> \n> > * Can we change the test in sage.functions.other.sqrt() to work without importing numpy?\n> \n> done in the new patch\n\nThanks!\n\n> > * All the examples in the doctests are for functions with a single argument. Is there any reason to move the check in `sage.symbolic.function.Function.__call__()` to try all arguments?\n> \n> In the original patch I forgot to add tests for atan2, which also didn't work with numpy before. The tests are now included.\n\nFair enough.\n\n> > We should also consider moving this check to `sage.symbolic.function.BuiltinFunction.__call__()`.\n> \n> Why would this be better? \n\nThis code path is speed critical since it gets called thousands of times for many applications like plotting. Checking the type of each argument introduces a penalty for functions with a single argument.\n\n> It currently does not have a `__call__` method.\n\nSorry about that. I confused it with the `__call__()` method of `GinacFunction`, which also checks if there is only one argument, and it has a method with the same name as the function. Now I wonder why isn't that in `BuiltinFunction`...\n\n\nYour patch was missing an empty line after line 165 in `sage/functions/other.py`. attachment:trac-8479-numpy_functions.take2.patch fixes this. Only attachment:trac-8479-numpy_functions.take2.patch should be applied.\n\n\nGreat work!",
    "created_at": "2010-05-07T14:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76427",
    "user": "burcin"
}
```

Attachment [trac-8479-numpy_functions.take2.patch](tarball://root/attachments/some-uuid/ticket8479/trac-8479-numpy_functions.take2.patch) by burcin created at 2010-05-07 14:53:45

Thanks for the quick response.

Replying to [comment:5 whuss]:
> Replying to [comment:4 burcin]:
> 
> > * Can we change the test in sage.functions.other.sqrt() to work without importing numpy?
> 
> done in the new patch

Thanks!

> > * All the examples in the doctests are for functions with a single argument. Is there any reason to move the check in `sage.symbolic.function.Function.__call__()` to try all arguments?
> 
> In the original patch I forgot to add tests for atan2, which also didn't work with numpy before. The tests are now included.

Fair enough.

> > We should also consider moving this check to `sage.symbolic.function.BuiltinFunction.__call__()`.
> 
> Why would this be better? 

This code path is speed critical since it gets called thousands of times for many applications like plotting. Checking the type of each argument introduces a penalty for functions with a single argument.

> It currently does not have a `__call__` method.

Sorry about that. I confused it with the `__call__()` method of `GinacFunction`, which also checks if there is only one argument, and it has a method with the same name as the function. Now I wonder why isn't that in `BuiltinFunction`...


Your patch was missing an empty line after line 165 in `sage/functions/other.py`. attachment:trac-8479-numpy_functions.take2.patch fixes this. Only attachment:trac-8479-numpy_functions.take2.patch should be applied.


Great work!



---

archive/issue_comments_076428.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T22:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76428",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_076429.json:
```json
{
    "body": "Merged [trac-8479-numpy_functions.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8479/trac-8479-numpy_functions.take2.patch).",
    "created_at": "2010-05-08T22:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8479#issuecomment-76429",
    "user": "mvngu"
}
```

Merged [trac-8479-numpy_functions.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8479/trac-8479-numpy_functions.take2.patch).
