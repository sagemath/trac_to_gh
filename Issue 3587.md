# Issue 3587: calculus -- implement symbolic summation

archive/issues_003587.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @burcin @jasongrout\n\nMaxima has good symbolic summation and it would be easy to wrap in the calculus package.\nWe are constantly getting stuff like this:\n\n```\n02:53 < nagyv> \ufeffhello! how can I represent a summation in sage? like sum_{x=1}^N x, I would like to take the limit as N goes to infinity\n03:02 < nagyv> what the heck is this? maxima.sum(1/x, x, 1, 2*N) gives 2*N/x! why?\n```\n\n\nProbably the only reason that this hasn't been done yet is the calculus rewrite by gfurnish.\nThat is *not* a good enough reason, and don't worry, the work won't be lost.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3587\n\n",
    "created_at": "2008-07-07T15:52:57Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "calculus -- implement symbolic summation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3587",
    "user": "@williamstein"
}
```
Assignee: @garyfurnish

CC:  @burcin @jasongrout

Maxima has good symbolic summation and it would be easy to wrap in the calculus package.
We are constantly getting stuff like this:

```
02:53 < nagyv> ﻿hello! how can I represent a summation in sage? like sum_{x=1}^N x, I would like to take the limit as N goes to infinity
03:02 < nagyv> what the heck is this? maxima.sum(1/x, x, 1, 2*N) gives 2*N/x! why?
```


Probably the only reason that this hasn't been done yet is the calculus rewrite by gfurnish.
That is *not* a good enough reason, and don't worry, the work won't be lost.

Issue created by migration from https://trac.sagemath.org/ticket/3587





---

archive/issue_comments_025318.json:
```json
{
    "body": "I would like to add a +1 to this proposal as I'm not planning on implementing symbolic summation anytime in the near (or far) future, so I would be really happy if someone would work on this.",
    "created_at": "2008-07-07T17:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25318",
    "user": "@garyfurnish"
}
```

I would like to add a +1 to this proposal as I'm not planning on implementing symbolic summation anytime in the near (or far) future, so I would be really happy if someone would work on this.



---

archive/issue_comments_025319.json:
```json
{
    "body": "\"sum\" is probably the most appropriate name for this, but we'd have to make sure that it behaves the same way as Python's sum.",
    "created_at": "2008-11-11T01:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25319",
    "user": "@mwhansen"
}
```

"sum" is probably the most appropriate name for this, but we'd have to make sure that it behaves the same way as Python's sum.



---

archive/issue_comments_025320.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-04T14:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25320",
    "user": "whuss"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025321.json:
```json
{
    "body": "The attached patch adds a summation command which wraps simplify_sum from maxima.",
    "created_at": "2009-06-04T14:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25321",
    "user": "whuss"
}
```

The attached patch adds a summation command which wraps simplify_sum from maxima.



---

archive/issue_comments_025322.json:
```json
{
    "body": "Changing assignee from @garyfurnish to whuss.",
    "created_at": "2009-06-04T14:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25322",
    "user": "whuss"
}
```

Changing assignee from @garyfurnish to whuss.



---

archive/issue_comments_025323.json:
```json
{
    "body": "Many thanks for the patch, this was long overdue. A few comments after reading your patch:\n\nYour patch replicates the way integrate/integral works perfectly. Though, as Mike wrote in comment:3, we should just call this `sum`. There is also a discussion about naming here:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/bd4eb3b613c98030\n\nI suggest putting a `sum()` function in `sage.misc.misc_c`, that calls python's `sum()` or your function based on the type/number of the arguments. Would you like to do this or should I?\n\nHere are some suggested changes:\n\n* rename all instances of the method to `sum` or `symbolic_sum`\n* you should import your function before the doctests in `calculus.py` to make sure you call the right function\n* it would be good to add a comment to #6197 pointing to the comment you have in `calculus.py`\n* you could add your code for converting MMA output back to Sage to a `_sage_()` method in `sage.interfaces.mathematica.MathematicaElement`, see the `MagmaElement` class in `sage.interfaces.magma` for an example, similarly for Maple output\n* In the last lines of the docstring for `sage.symbolic.expression.Expression.summation`, choosen -> chosen\n\n\nIn the long term, I would like to see `integral` and `sum` constructs as subclasses of `sage.symbolic.function.SFunction`, instead of the current thin wrappers around maxima functionality. I will take a look at the feasibility of doing this over the weekend. I don't want to hold your patch back for this though.",
    "created_at": "2009-06-05T13:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25323",
    "user": "@burcin"
}
```

Many thanks for the patch, this was long overdue. A few comments after reading your patch:

Your patch replicates the way integrate/integral works perfectly. Though, as Mike wrote in comment:3, we should just call this `sum`. There is also a discussion about naming here:

http://groups.google.com/group/sage-devel/browse_thread/thread/bd4eb3b613c98030

I suggest putting a `sum()` function in `sage.misc.misc_c`, that calls python's `sum()` or your function based on the type/number of the arguments. Would you like to do this or should I?

Here are some suggested changes:

* rename all instances of the method to `sum` or `symbolic_sum`
* you should import your function before the doctests in `calculus.py` to make sure you call the right function
* it would be good to add a comment to #6197 pointing to the comment you have in `calculus.py`
* you could add your code for converting MMA output back to Sage to a `_sage_()` method in `sage.interfaces.mathematica.MathematicaElement`, see the `MagmaElement` class in `sage.interfaces.magma` for an example, similarly for Maple output
* In the last lines of the docstring for `sage.symbolic.expression.Expression.summation`, choosen -> chosen


In the long term, I would like to see `integral` and `sum` constructs as subclasses of `sage.symbolic.function.SFunction`, instead of the current thin wrappers around maxima functionality. I will take a look at the feasibility of doing this over the weekend. I don't want to hold your patch back for this though.



---

archive/issue_comments_025324.json:
```json
{
    "body": "Replying to [comment:5 burcin]:\n> Many thanks for the patch, this was long overdue. A few comments after reading your patch:\n> \n> Your patch replicates the way integrate/integral works perfectly. Though, as Mike wrote in comment:3, we should just call this `sum`. There is also a discussion about naming here:\n> \n> http://groups.google.com/group/sage-devel/browse_thread/thread/bd4eb3b613c98030\n> \n> I suggest putting a `sum()` function in `sage.misc.misc_c`, that calls python's `sum()` or your function based on the type/number of the arguments. Would you like to do this or should I?\n\nIt would be great if you could do this.\n\n> Here are some suggested changes:\n> \n>  * rename all instances of the method to `sum` or `symbolic_sum`\n>  * you should import your function before the doctests in `calculus.py` to make sure you call the right function\n>  * it would be good to add a comment to #6197 pointing to the comment you have in `calculus.py`\n>  * you could add your code for converting MMA output back to Sage to a `_sage_()` method in `sage.interfaces.mathematica.MathematicaElement`, see the `MagmaElement` class in `sage.interfaces.magma` for an example, similarly for Maple output\n>  * In the last lines of the docstring for `sage.symbolic.expression.Expression.summation`, choosen -> chosen\n\nI will take care of these.\n \n> \n> In the long term, I would like to see `integral` and `sum` constructs as subclasses of `sage.symbolic.function.SFunction`, instead of the current thin wrappers around maxima functionality.\n\nThis is definitely necessary. Currently there is no way to interact with an unevaluated integral or sum.\n\n> I will take a look at the feasibility of doing this over the weekend. I don't want to hold your patch back for this though.",
    "created_at": "2009-06-06T17:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25324",
    "user": "whuss"
}
```

Replying to [comment:5 burcin]:
> Many thanks for the patch, this was long overdue. A few comments after reading your patch:
> 
> Your patch replicates the way integrate/integral works perfectly. Though, as Mike wrote in comment:3, we should just call this `sum`. There is also a discussion about naming here:
> 
> http://groups.google.com/group/sage-devel/browse_thread/thread/bd4eb3b613c98030
> 
> I suggest putting a `sum()` function in `sage.misc.misc_c`, that calls python's `sum()` or your function based on the type/number of the arguments. Would you like to do this or should I?

It would be great if you could do this.

> Here are some suggested changes:
> 
>  * rename all instances of the method to `sum` or `symbolic_sum`
>  * you should import your function before the doctests in `calculus.py` to make sure you call the right function
>  * it would be good to add a comment to #6197 pointing to the comment you have in `calculus.py`
>  * you could add your code for converting MMA output back to Sage to a `_sage_()` method in `sage.interfaces.mathematica.MathematicaElement`, see the `MagmaElement` class in `sage.interfaces.magma` for an example, similarly for Maple output
>  * In the last lines of the docstring for `sage.symbolic.expression.Expression.summation`, choosen -> chosen

I will take care of these.
 
> 
> In the long term, I would like to see `integral` and `sum` constructs as subclasses of `sage.symbolic.function.SFunction`, instead of the current thin wrappers around maxima functionality.

This is definitely necessary. Currently there is no way to interact with an unevaluated integral or sum.

> I will take a look at the feasibility of doing this over the weekend. I don't want to hold your patch back for this though.



---

archive/issue_comments_025325.json:
```json
{
    "body": "Attachment [summation.patch](tarball://root/attachments/some-uuid/ticket3587/summation.patch) by whuss created at 2009-06-07 12:16:53\n\nReplying to [comment:5 burcin]: \n> Here are some suggested changes:\n> \n>  * rename all instances of the method to `sum` or `symbolic_sum`\n>  * you should import your function before the doctests in `calculus.py` to make sure you call the right function\n>  * it would be good to add a comment to #6197 pointing to the comment you have in `calculus.py`\n>  * you could add your code for converting MMA output back to Sage to a `_sage_()` method in `sage.interfaces.mathematica.MathematicaElement`, see the `MagmaElement` class in `sage.interfaces.magma` for an example, similarly for Maple output\n>  * In the last lines of the docstring for `sage.symbolic.expression.Expression.summation`, choosen -> chosen\n\nI posted a new patch that takes care of these issues.\n\nThe second patch (sum.patch) renames summation to sum. This currently overwrites the python sum command.",
    "created_at": "2009-06-07T12:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25325",
    "user": "whuss"
}
```

Attachment [summation.patch](tarball://root/attachments/some-uuid/ticket3587/summation.patch) by whuss created at 2009-06-07 12:16:53

Replying to [comment:5 burcin]: 
> Here are some suggested changes:
> 
>  * rename all instances of the method to `sum` or `symbolic_sum`
>  * you should import your function before the doctests in `calculus.py` to make sure you call the right function
>  * it would be good to add a comment to #6197 pointing to the comment you have in `calculus.py`
>  * you could add your code for converting MMA output back to Sage to a `_sage_()` method in `sage.interfaces.mathematica.MathematicaElement`, see the `MagmaElement` class in `sage.interfaces.magma` for an example, similarly for Maple output
>  * In the last lines of the docstring for `sage.symbolic.expression.Expression.summation`, choosen -> chosen

I posted a new patch that takes care of these issues.

The second patch (sum.patch) renames summation to sum. This currently overwrites the python sum command.



---

archive/issue_comments_025326.json:
```json
{
    "body": "Attachment [sum.patch](tarball://root/attachments/some-uuid/ticket3587/sum.patch) by @mwhansen created at 2009-06-20 01:52:06",
    "created_at": "2009-06-20T01:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25326",
    "user": "@mwhansen"
}
```

Attachment [sum.patch](tarball://root/attachments/some-uuid/ticket3587/sum.patch) by @mwhansen created at 2009-06-20 01:52:06



---

archive/issue_comments_025327.json:
```json
{
    "body": "I updated sum.patch so that it's compatible with __builtin__.sum.\n\nBurcin, can you look at this?",
    "created_at": "2009-06-20T01:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25327",
    "user": "@mwhansen"
}
```

I updated sum.patch so that it's compatible with __builtin__.sum.

Burcin, can you look at this?



---

archive/issue_comments_025328.json:
```json
{
    "body": "I uploaded a new patch in attachment:trac_3587-maxima_simplify_sum.patch. This has both patches folded together, and renames `sum()` to `symbolic_sum()` in `sage/calculus/calculus.py` and `sage/misc/functional.py` eliminating the risk of people using the symbolic sum instead of sum in library code without realizing, and the need to import `__builtin__`.\n\nI am OK with the patch, and ready to give it a positive review. However, there is a problem, maxima returns wrong results in certain cases:\n\n\n```\nsage: sum(binomial(n,k), k, 1, n)\n2^n - 2\nsage: sum(binomial(n,k), k, 2, n)\n2^n - 2*n - 2\nsage: r=sum(binomial(n,k), k, 2, n-2)\nsage: r.simplify()\n2^n - 1/6*n^3 - 11/6*n - 2\n```\n\n\nIt seems that maxima doesn't handle definite sums with \"non natural\" bounds. I.e., in the examples above the bounds don't span the whole support of the expression, so one needs further processing to get the final result after calling Zeilberger's algorithm.\n\nIndefinite sums seem to be fine. In this case, we could check the inputs, and raise a warning if we have a definite sum. I'll try to do this, but don't count on me since I already signed up for a lot this week.",
    "created_at": "2009-06-23T21:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25328",
    "user": "@burcin"
}
```

I uploaded a new patch in attachment:trac_3587-maxima_simplify_sum.patch. This has both patches folded together, and renames `sum()` to `symbolic_sum()` in `sage/calculus/calculus.py` and `sage/misc/functional.py` eliminating the risk of people using the symbolic sum instead of sum in library code without realizing, and the need to import `__builtin__`.

I am OK with the patch, and ready to give it a positive review. However, there is a problem, maxima returns wrong results in certain cases:


```
sage: sum(binomial(n,k), k, 1, n)
2^n - 2
sage: sum(binomial(n,k), k, 2, n)
2^n - 2*n - 2
sage: r=sum(binomial(n,k), k, 2, n-2)
sage: r.simplify()
2^n - 1/6*n^3 - 11/6*n - 2
```


It seems that maxima doesn't handle definite sums with "non natural" bounds. I.e., in the examples above the bounds don't span the whole support of the expression, so one needs further processing to get the final result after calling Zeilberger's algorithm.

Indefinite sums seem to be fine. In this case, we could check the inputs, and raise a warning if we have a definite sum. I'll try to do this, but don't count on me since I already signed up for a lot this week.



---

archive/issue_comments_025329.json:
```json
{
    "body": "Attachment [trac_3587-maxima_simplify_sum.patch](tarball://root/attachments/some-uuid/ticket3587/trac_3587-maxima_simplify_sum.patch) by @burcin created at 2009-06-23 21:39:50",
    "created_at": "2009-06-23T21:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25329",
    "user": "@burcin"
}
```

Attachment [trac_3587-maxima_simplify_sum.patch](tarball://root/attachments/some-uuid/ticket3587/trac_3587-maxima_simplify_sum.patch) by @burcin created at 2009-06-23 21:39:50



---

archive/issue_comments_025330.json:
```json
{
    "body": "I installed this, but it does not seem to work as advertised.  Namely, \n\n```\nsage: var('n,k')\n(k, n)\nsage: sum(binomial(n,k),k,0,n)\nsimplify_sum(sum(binomial(n,k),k,0,n))\n```\n\nIt does behave as desired if I go to Maxima and load(simplify_sum) etc., but that's not the same.  Somehow it's staying symbolic for some reason.  This is off of 4.1.1 on Mac OSX.5.\n\n> I am OK with the patch, and ready to give it a positive review. However, there is a problem, maxima returns wrong results in certain cases:\n> \n> {{{\n> sage: sum(binomial(n,k), k, 1, n)\n> 2^n - 2\n> sage: sum(binomial(n,k), k, 2, n)\n> 2^n - 2*n - 2\n> sage: r=sum(binomial(n,k), k, 2, n-2)\n> sage: r.simplify()\n> 2^n - 1/6*n^3 - 11/6*n - 2\n> }}}\n> \n> It seems that maxima doesn't handle definite sums with \"non natural\" bounds. I.e., in the examples above the bounds don't span the whole support of the expression, so one needs further processing to get the final result after calling Zeilberger's algorithm.\n\nLooks like this problem is fixed in Maxima 5.19 (at least they work properly in 5.19.1), so this is another good reason to get that in Sage soon (there was an experimental spkg posted at [http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0/maxima-5.19.0.spkg](http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0/maxima-5.19.0.spkg) at one point).  Incidentally, apparently it never got to as heavy a hitter as Zeilberger, but I'm not sure where the problem was.",
    "created_at": "2009-08-28T20:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25330",
    "user": "@kcrisman"
}
```

I installed this, but it does not seem to work as advertised.  Namely, 

```
sage: var('n,k')
(k, n)
sage: sum(binomial(n,k),k,0,n)
simplify_sum(sum(binomial(n,k),k,0,n))
```

It does behave as desired if I go to Maxima and load(simplify_sum) etc., but that's not the same.  Somehow it's staying symbolic for some reason.  This is off of 4.1.1 on Mac OSX.5.

> I am OK with the patch, and ready to give it a positive review. However, there is a problem, maxima returns wrong results in certain cases:
> 
> {{{
> sage: sum(binomial(n,k), k, 1, n)
> 2^n - 2
> sage: sum(binomial(n,k), k, 2, n)
> 2^n - 2*n - 2
> sage: r=sum(binomial(n,k), k, 2, n-2)
> sage: r.simplify()
> 2^n - 1/6*n^3 - 11/6*n - 2
> }}}
> 
> It seems that maxima doesn't handle definite sums with "non natural" bounds. I.e., in the examples above the bounds don't span the whole support of the expression, so one needs further processing to get the final result after calling Zeilberger's algorithm.

Looks like this problem is fixed in Maxima 5.19 (at least they work properly in 5.19.1), so this is another good reason to get that in Sage soon (there was an experimental spkg posted at [http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0/maxima-5.19.0.spkg](http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0/maxima-5.19.0.spkg) at one point).  Incidentally, apparently it never got to as heavy a hitter as Zeilberger, but I'm not sure where the problem was.



---

archive/issue_comments_025331.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> I installed this, but it does not seem to work as advertised.  Namely, \n> {{{\n> sage: var('n,k')\n> (k, n)\n> sage: sum(binomial(n,k),k,0,n)\n> simplify_sum(sum(binomial(n,k),k,0,n))\n> }}}\n> It does behave as desired if I go to Maxima and load(simplify_sum) etc., but that's not the same.  Somehow it's staying symbolic for some reason.  This is off of 4.1.1 on Mac OSX.5.\n\nIt works for me on sage-4.1.1 on Linux. I don't have a Mac to check.",
    "created_at": "2009-08-31T11:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25331",
    "user": "whuss"
}
```

Replying to [comment:10 kcrisman]:
> I installed this, but it does not seem to work as advertised.  Namely, 
> {{{
> sage: var('n,k')
> (k, n)
> sage: sum(binomial(n,k),k,0,n)
> simplify_sum(sum(binomial(n,k),k,0,n))
> }}}
> It does behave as desired if I go to Maxima and load(simplify_sum) etc., but that's not the same.  Somehow it's staying symbolic for some reason.  This is off of 4.1.1 on Mac OSX.5.

It works for me on sage-4.1.1 on Linux. I don't have a Mac to check.



---

archive/issue_comments_025332.json:
```json
{
    "body": "The fix for my problem is to change\n\n```\nmaxima = Maxima(init_code = ['display2d:false; domain: complex; keepfloat: true; load(topoly_solver); load(simplify_sum)'],\n                script_subdirectory=None)\n```\n\nby\n\n```\nmaxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(topoly_solver)', 'load(simplify_sum)'],\n                script_subdirectory=None)\n```\n\nthe need for which perhaps does depend on the operating system.   Can someone check that this doesn't break Linux?",
    "created_at": "2009-09-02T18:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25332",
    "user": "@kcrisman"
}
```

The fix for my problem is to change

```
maxima = Maxima(init_code = ['display2d:false; domain: complex; keepfloat: true; load(topoly_solver); load(simplify_sum)'],
                script_subdirectory=None)
```

by

```
maxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(topoly_solver)', 'load(simplify_sum)'],
                script_subdirectory=None)
```

the need for which perhaps does depend on the operating system.   Can someone check that this doesn't break Linux?



---

archive/issue_comments_025333.json:
```json
{
    "body": "The latest .spkg in #6699 (and hence in 4.1.2.alpha0) should fix the problems Burcin mentions, and seems to handle all the sums properly.\n\n```\nsage: sum(binomial(n,k), k, 1, n)\n2^n - 2\nsage: sum(binomial(n,k), k, 2, n)\n2^n - 2*n - 2\n```\n\nare now\n\n```\nsage: var('k,n')\n(k, n)\nsage: sum(binomial(n,k),k,0,n)\n2^n\nsage: sum(binomial(n,k),k,1,n)\n2^n - 1\nsage: sum(binomial(n,k),k,2,n)\n2^n - n - 1\n```\n\nSo perhaps a new patch based on 4.1.2.alpha0 is in order, but then the review should be quite straightforward, with the fix above.",
    "created_at": "2009-09-02T19:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25333",
    "user": "@kcrisman"
}
```

The latest .spkg in #6699 (and hence in 4.1.2.alpha0) should fix the problems Burcin mentions, and seems to handle all the sums properly.

```
sage: sum(binomial(n,k), k, 1, n)
2^n - 2
sage: sum(binomial(n,k), k, 2, n)
2^n - 2*n - 2
```

are now

```
sage: var('k,n')
(k, n)
sage: sum(binomial(n,k),k,0,n)
2^n
sage: sum(binomial(n,k),k,1,n)
2^n - 1
sage: sum(binomial(n,k),k,2,n)
2^n - n - 1
```

So perhaps a new patch based on 4.1.2.alpha0 is in order, but then the review should be quite straightforward, with the fix above.



---

archive/issue_comments_025334.json:
```json
{
    "body": "This should fix all the outstanding issues. It is built off of 4.1.1, with #6564 and (then) #6699 applied, then this patch.  Several additional doctests/fixes to them are included beyond the previous patch, in addition to the Maxima init fix.  Should definitely be tested on Linux to make sure the fix for OSX didn't break Linux!",
    "created_at": "2009-09-02T20:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25334",
    "user": "@kcrisman"
}
```

This should fix all the outstanding issues. It is built off of 4.1.1, with #6564 and (then) #6699 applied, then this patch.  Several additional doctests/fixes to them are included beyond the previous patch, in addition to the Maxima init fix.  Should definitely be tested on Linux to make sure the fix for OSX didn't break Linux!



---

archive/issue_comments_025335.json:
```json
{
    "body": "I browsed through the patch---is it still easy to access the (fast) native python sum command, or will we have to import that into the namespace?  In other words, was the suggestion given above about calling the python sum vs. this new sum depending on the arguments implemented?  If not, I see a serious, far-reaching problem with backwards compatibility...",
    "created_at": "2009-09-02T22:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25335",
    "user": "@jasongrout"
}
```

I browsed through the patch---is it still easy to access the (fast) native python sum command, or will we have to import that into the namespace?  In other words, was the suggestion given above about calling the python sum vs. this new sum depending on the arguments implemented?  If not, I see a serious, far-reaching problem with backwards compatibility...



---

archive/issue_comments_025336.json:
```json
{
    "body": "Well, the following was identical with and without the patch:\n\n```\nsage: l = range(10^6)\nsage: time sum(l)\nCPU times: user 0.15 s, sys: 0.00 s, total: 0.15 s\nWall time: 0.15 s\n499999500000L\n```\n\nAnd the same with summing m = 5*l, both 0.79 s, and summing n = 100*m, both about 80 s.  And sum(l,3) returns the correct answer (without the L).  Also, earlier mhansen seems to indicate that it's still okay - I don't know exactly where in the code that happens, though.  Hope this helps.",
    "created_at": "2009-09-03T00:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25336",
    "user": "@kcrisman"
}
```

Well, the following was identical with and without the patch:

```
sage: l = range(10^6)
sage: time sum(l)
CPU times: user 0.15 s, sys: 0.00 s, total: 0.15 s
Wall time: 0.15 s
499999500000L
```

And the same with summing m = 5*l, both 0.79 s, and summing n = 100*m, both about 80 s.  And sum(l,3) returns the correct answer (without the L).  Also, earlier mhansen seems to indicate that it's still okay - I don't know exactly where in the code that happens, though.  Hope this helps.



---

archive/issue_comments_025337.json:
```json
{
    "body": "Fix this one broken doctest and this gets a positive review from me:\n\n```python\nwstein@sage:~/build/sage-4.1.2.alpha1$ ./sage -t devel/sage/sage/misc/functional.py \nsage -t  \"devel/sage/sage/misc/functional.py\"               \n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/misc/functional.py\", line 442:\n    sage: sum(k * binomial(n, k), k, 1, n)\nExpected:\n    1/2*2^n*n\nGot:\n    n*2^(n - 1)\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/misc/functional.py\", line 480:\n    sage: sum(a*q^k, k, 0, oo)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: Sum is divergent.\nGot:\n    -a/(q - 1)\n**********************************************************************\n1 items had failures:\n   2 of  20 in __main__.example_25\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-4.1.2.alpha1/tmp/.doctest_functional.py\n         [8.3 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/misc/functional.py\"\nTotal time for all tests: 8.3 seconds\nwstein@sage:~/build/sage-4.1.2.alpha1$ \n```\n\n\nThe above is just the result of changes in Maxima going from 5.16 to 5.19 in sage-4.1.2.\n\n  -- William",
    "created_at": "2009-09-13T01:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25337",
    "user": "@williamstein"
}
```

Fix this one broken doctest and this gets a positive review from me:

```python
wstein@sage:~/build/sage-4.1.2.alpha1$ ./sage -t devel/sage/sage/misc/functional.py 
sage -t  "devel/sage/sage/misc/functional.py"               
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/misc/functional.py", line 442:
    sage: sum(k * binomial(n, k), k, 1, n)
Expected:
    1/2*2^n*n
Got:
    n*2^(n - 1)
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/misc/functional.py", line 480:
    sage: sum(a*q^k, k, 0, oo)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Sum is divergent.
Got:
    -a/(q - 1)
**********************************************************************
1 items had failures:
   2 of  20 in __main__.example_25
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-4.1.2.alpha1/tmp/.doctest_functional.py
         [8.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/misc/functional.py"
Total time for all tests: 8.3 seconds
wstein@sage:~/build/sage-4.1.2.alpha1$ 
```


The above is just the result of changes in Maxima going from 5.16 to 5.19 in sage-4.1.2.

  -- William



---

archive/issue_comments_025338.json:
```json
{
    "body": "This is nice!\n\nJust a small note: Sphinx warns about the indentation of the new `note::` block in `expression.pyx`:\n\n```\n/home/apps/sage/devel/sage/doc/en/reference/sage/symbolic/expression.rst:: (ERROR/3) Content block expected for the \"note\" directive; none found.\n```\n",
    "created_at": "2009-09-13T01:55:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25338",
    "user": "@qed777"
}
```

This is nice!

Just a small note: Sphinx warns about the indentation of the new `note::` block in `expression.pyx`:

```
/home/apps/sage/devel/sage/doc/en/reference/sage/symbolic/expression.rst:: (ERROR/3) Content block expected for the "note" directive; none found.
```




---

archive/issue_comments_025339.json:
```json
{
    "body": "fixes the doctest errors reported by William",
    "created_at": "2009-09-14T14:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25339",
    "user": "whuss"
}
```

fixes the doctest errors reported by William



---

archive/issue_comments_025340.json:
```json
{
    "body": "Attachment [trac_3587-fix_doctests.patch](tarball://root/attachments/some-uuid/ticket3587/trac_3587-fix_doctests.patch) by @kcrisman created at 2009-09-14 14:10:38\n\nOkay, I fixed those tests; there were identical ones elsewhere I did fix but functional.py escaped me.  I also think I fixed the note issue.  \n\nSince #6197 is merged I also used the correct algorithm=maxima behavior.  I don't have Maple so I didn't feel comfortable changing the Maple behavior, but it would be easy to open a new ticket for that if the appropriate algorithm worked, which it certainly seems like it should post-#6197.\n\nI'm going to assume that the builtin sum is indeed okay - great!",
    "created_at": "2009-09-14T14:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25340",
    "user": "@kcrisman"
}
```

Attachment [trac_3587-fix_doctests.patch](tarball://root/attachments/some-uuid/ticket3587/trac_3587-fix_doctests.patch) by @kcrisman created at 2009-09-14 14:10:38

Okay, I fixed those tests; there were identical ones elsewhere I did fix but functional.py escaped me.  I also think I fixed the note issue.  

Since #6197 is merged I also used the correct algorithm=maxima behavior.  I don't have Maple so I didn't feel comfortable changing the Maple behavior, but it would be easy to open a new ticket for that if the appropriate algorithm worked, which it certainly seems like it should post-#6197.

I'm going to assume that the builtin sum is indeed okay - great!



---

archive/issue_comments_025341.json:
```json
{
    "body": "Use only the 5-19-1 patch.",
    "created_at": "2009-09-14T14:12:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25341",
    "user": "@kcrisman"
}
```

Use only the 5-19-1 patch.



---

archive/issue_comments_025342.json:
```json
{
    "body": "Attachment [trac_3587-binomial_workaround.patch](tarball://root/attachments/some-uuid/ticket3587/trac_3587-binomial_workaround.patch) by whuss created at 2009-09-14 14:13:00\n\nremoves the workaround for binomials. Depends on #6197",
    "created_at": "2009-09-14T14:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25342",
    "user": "whuss"
}
```

Attachment [trac_3587-binomial_workaround.patch](tarball://root/attachments/some-uuid/ticket3587/trac_3587-binomial_workaround.patch) by whuss created at 2009-09-14 14:13:00

removes the workaround for binomials. Depends on #6197



---

archive/issue_comments_025343.json:
```json
{
    "body": "Looks like I have been a little too late.\n\nI have checked that algorithm=maple also works without the workaround for #6197.\nI think it is save to remove it.",
    "created_at": "2009-09-14T14:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25343",
    "user": "whuss"
}
```

Looks like I have been a little too late.

I have checked that algorithm=maple also works without the workaround for #6197.
I think it is save to remove it.



---

archive/issue_comments_025344.json:
```json
{
    "body": "Great, I'll do that as well.",
    "created_at": "2009-09-14T15:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25344",
    "user": "@kcrisman"
}
```

Great, I'll do that as well.



---

archive/issue_comments_025345.json:
```json
{
    "body": "I get *tons* of doctest failures when I apply this patch, say to sage-4.1.2.alpha1:\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage/sage/misc/functional.py # 5 doctests failed\n        sage -t  devel/sage/sage/calculus/calculus.py # 10 doctests failed\n        sage -t  devel/sage/sage/symbolic/expression.pyx # 9 doctests failed\n```\n\n\nSee http://sage.math.washington.edu/home/wstein/build/sage-4.1.2.alpha1/test_3587.out",
    "created_at": "2009-09-22T14:26:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25345",
    "user": "@williamstein"
}
```

I get *tons* of doctest failures when I apply this patch, say to sage-4.1.2.alpha1:

```
The following tests failed:

        sage -t  devel/sage/sage/misc/functional.py # 5 doctests failed
        sage -t  devel/sage/sage/calculus/calculus.py # 10 doctests failed
        sage -t  devel/sage/sage/symbolic/expression.pyx # 9 doctests failed
```


See http://sage.math.washington.edu/home/wstein/build/sage-4.1.2.alpha1/test_3587.out



---

archive/issue_comments_025346.json:
```json
{
    "body": "Did you do #6197?",
    "created_at": "2009-09-22T14:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25346",
    "user": "@kcrisman"
}
```

Did you do #6197?



---

archive/issue_comments_025347.json:
```json
{
    "body": "This patch in fact applies cleanly to 4.1.2.alpha2, and none of the files above have doctest failures with it.  Please review.",
    "created_at": "2009-09-24T14:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25347",
    "user": "@kcrisman"
}
```

This patch in fact applies cleanly to 4.1.2.alpha2, and none of the files above have doctest failures with it.  Please review.



---

archive/issue_comments_025348.json:
```json
{
    "body": "Based on 4.2.1, apply only this patch",
    "created_at": "2009-11-17T20:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25348",
    "user": "@kcrisman"
}
```

Based on 4.2.1, apply only this patch



---

archive/issue_comments_025349.json:
```json
{
    "body": "Attachment [trac_3587-maxima_simplify_sum-with-maxima-5-19-1.patch](tarball://root/attachments/some-uuid/ticket3587/trac_3587-maxima_simplify_sum-with-maxima-5-19-1.patch) by @kcrisman created at 2009-11-17 20:13:41\n\nPlease someone (beyond myself and the author) review this!  It would be perfect for the big 4.3 release coming up!",
    "created_at": "2009-11-17T20:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25349",
    "user": "@kcrisman"
}
```

Attachment [trac_3587-maxima_simplify_sum-with-maxima-5-19-1.patch](tarball://root/attachments/some-uuid/ticket3587/trac_3587-maxima_simplify_sum-with-maxima-5-19-1.patch) by @kcrisman created at 2009-11-17 20:13:41

Please someone (beyond myself and the author) review this!  It would be perfect for the big 4.3 release coming up!



---

archive/issue_comments_025350.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T14:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25350",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_025351.json:
```json
{
    "body": "Positive review from me (by the way).",
    "created_at": "2009-11-29T14:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3587",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3587#issuecomment-25351",
    "user": "@mwhansen"
}
```

Positive review from me (by the way).
