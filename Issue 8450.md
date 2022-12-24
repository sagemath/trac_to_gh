# Issue 8450: contour_plot chokes on function which involves imaginary numbers

archive/issues_008450.json:
```json
{
    "body": "Assignee: was\n\nCC:  mjo egourgoulhon @jungmath\n\nThis gives an error:\n\n\n```\ncontour_plot(real_part(log(x+y*I+.001)), (x,-3,3),(y,-3,3),fill=False)\n```\n\n\nbut this works:\n\n\n```\na(x,y)=real(log(x+y*I+.001))\nf=fast_callable(a,domain=CC)\ncontour_plot(f, (x,-3,3),(y,-3,3),fill=False)\n```\n\n\nand this works:\n\n\n```\ncontour_plot(imag(log(x+y*I+.001)), (x,-3,3),(y,-3,3),fill=False)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8450\n\n",
    "created_at": "2010-03-05T22:01:42Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.6",
    "title": "contour_plot chokes on function which involves imaginary numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8450",
    "user": "jason"
}
```
Assignee: was

CC:  mjo egourgoulhon @jungmath

This gives an error:


```
contour_plot(real_part(log(x+y*I+.001)), (x,-3,3),(y,-3,3),fill=False)
```


but this works:


```
a(x,y)=real(log(x+y*I+.001))
f=fast_callable(a,domain=CC)
contour_plot(f, (x,-3,3),(y,-3,3),fill=False)
```


and this works:


```
contour_plot(imag(log(x+y*I+.001)), (x,-3,3),(y,-3,3),fill=False)
```


Issue created by migration from https://trac.sagemath.org/ticket/8450





---

archive/issue_comments_075964.json:
```json
{
    "body": "#5572 will help solve this.",
    "created_at": "2010-04-26T11:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75964",
    "user": "jason"
}
```

#5572 will help solve this.



---

archive/issue_comments_075965.json:
```json
{
    "body": "As the Sage-8.8 release milestone is pending, we should delete the sage-8.8 milestone for tickets that are not actively being worked on or that still require significant work to move forward.  If you feel that this ticket should be included in the next Sage release at the soonest please set its milestone to the next release milestone (sage-8.9).",
    "created_at": "2019-06-14T14:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75965",
    "user": "embray"
}
```

As the Sage-8.8 release milestone is pending, we should delete the sage-8.8 milestone for tickets that are not actively being worked on or that still require significant work to move forward.  If you feel that this ticket should be included in the next Sage release at the soonest please set its milestone to the next release milestone (sage-8.9).



---

archive/issue_comments_075966.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2021-07-22T00:57:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75966",
    "user": "mkoeppe"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_075967.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2021-07-23T15:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75967",
    "user": "mjo"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_075968.json:
```json
{
    "body": "This is an \"easy fix\" but causes a cascade of other issues because removing `domain=float` turns a lot of things that used to be `Nan` into `TypeError`, `ValueError`, `ZeroDivisionError`, etc.\n\nI'm still running a ptestlong on this, but everything under `sage/plot` now passes. Here are some thoughts:\n\n1. Do we really want to support passing (for example) the integer zero as a function to be plotted? We have doctests that check things like `plot(ZZ(0), x, 0, 1)`. Supporting this requires special cases in the code, and IMO just perpetuates confusion about the difference between the integer 0 and the function const0.\n2. We now have \"try to evaluate this as a real number, and return NaN (or skip it) if we can't\" code in at least five places. Should this be made consistent, or (better yet) factored out? I've made it so that the doctests pass, but in some places we catch only e.g. `TypeError`, while in others we check for a nice long list.\n3. This needs a careful review, since it can change the appearance of plots. There was some other (now fixed) bug involved as you can see from the commit list, but for example, this fix accidentally broke `list_plot`.\n4. I don't really like using try/except in fast loops. Is there a better way to fix the doctest failures that the first commit caused and that the later ones fix?",
    "created_at": "2021-07-23T15:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75968",
    "user": "mjo"
}
```

This is an "easy fix" but causes a cascade of other issues because removing `domain=float` turns a lot of things that used to be `Nan` into `TypeError`, `ValueError`, `ZeroDivisionError`, etc.

I'm still running a ptestlong on this, but everything under `sage/plot` now passes. Here are some thoughts:

1. Do we really want to support passing (for example) the integer zero as a function to be plotted? We have doctests that check things like `plot(ZZ(0), x, 0, 1)`. Supporting this requires special cases in the code, and IMO just perpetuates confusion about the difference between the integer 0 and the function const0.
2. We now have "try to evaluate this as a real number, and return NaN (or skip it) if we can't" code in at least five places. Should this be made consistent, or (better yet) factored out? I've made it so that the doctests pass, but in some places we catch only e.g. `TypeError`, while in others we check for a nice long list.
3. This needs a careful review, since it can change the appearance of plots. There was some other (now fixed) bug involved as you can see from the commit list, but for example, this fix accidentally broke `list_plot`.
4. I don't really like using try/except in fast loops. Is there a better way to fix the doctest failures that the first commit caused and that the later ones fix?



---

archive/issue_comments_075969.json:
```json
{
    "body": "Replying to [comment:11 mjo]:\n> 1. Do we really want to support passing (for example) the integer zero as a function to be plotted? We have doctests that check things like `plot(ZZ(0), x, 0, 1)`. Supporting this requires special cases in the code, and IMO just perpetuates confusion about the difference between the integer 0 and the function const0.\n\nAllowing non-callables as input for `plot` is, I think, important to keep. Convenience for casual use is key. Given that `plot` takes variable names as part of its input, it's clear that there is some implicit construction of a symbolic or numerical function happening.",
    "created_at": "2021-07-23T16:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75969",
    "user": "mkoeppe"
}
```

Replying to [comment:11 mjo]:
> 1. Do we really want to support passing (for example) the integer zero as a function to be plotted? We have doctests that check things like `plot(ZZ(0), x, 0, 1)`. Supporting this requires special cases in the code, and IMO just perpetuates confusion about the difference between the integer 0 and the function const0.

Allowing non-callables as input for `plot` is, I think, important to keep. Convenience for casual use is key. Given that `plot` takes variable names as part of its input, it's clear that there is some implicit construction of a symbolic or numerical function happening.



---

archive/issue_comments_075970.json:
```json
{
    "body": "Replying to [comment:11 mjo]:\n> This is an \"easy fix\" but causes a cascade of other issues because removing `domain=float` turns a lot of things that used to be `Nan` into `TypeError`, `ValueError`, `ZeroDivisionError`, etc.\n\nSorry, where do you remove `domain=float`?",
    "created_at": "2021-07-23T16:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75970",
    "user": "mkoeppe"
}
```

Replying to [comment:11 mjo]:
> This is an "easy fix" but causes a cascade of other issues because removing `domain=float` turns a lot of things that used to be `Nan` into `TypeError`, `ValueError`, `ZeroDivisionError`, etc.

Sorry, where do you remove `domain=float`?



---

archive/issue_comments_075971.json:
```json
{
    "body": "Replying to [comment:13 mkoeppe]:\n> Replying to [comment:11 mjo]:\n> > This is an \"easy fix\" but causes a cascade of other issues because removing `domain=float` turns a lot of things that used to be `Nan` into `TypeError`, `ValueError`, `ZeroDivisionError`, etc.\n> \n> Sorry, where do you remove `domain=float`?\n\nThe first thing `fast_float()` tries is to use `fast_callable()` with `domain=float`:\n\n\n```python\ntry:\n    return fast_callable(f, vars=vars, domain=float,\n                         expect_one_var=expect_one_var)\n```\n\n\nWe're now using `fast_callable()` directly, and omit the `domain`.",
    "created_at": "2021-07-23T16:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75971",
    "user": "mjo"
}
```

Replying to [comment:13 mkoeppe]:
> Replying to [comment:11 mjo]:
> > This is an "easy fix" but causes a cascade of other issues because removing `domain=float` turns a lot of things that used to be `Nan` into `TypeError`, `ValueError`, `ZeroDivisionError`, etc.
> 
> Sorry, where do you remove `domain=float`?

The first thing `fast_float()` tries is to use `fast_callable()` with `domain=float`:


```python
try:
    return fast_callable(f, vars=vars, domain=float,
                         expect_one_var=expect_one_var)
```


We're now using `fast_callable()` directly, and omit the `domain`.



---

archive/issue_comments_075972.json:
```json
{
    "body": "Thanks.\n\nI have not looked at the details, nor done any timing. But it seems to me that a better solution may be to try `domain=float` first, then `domain=complex` (or whatever is needed to make `fast_callable` use `interp_cdf`); and only in the end fall back to the general interpreter.\n\n> 2. We now have \"try to evaluate this as a real number, and return NaN (or skip it) if we can't\" code in at least five places. Should this be made consistent, or (better yet) factored out? \n\nYes, I guess there would be value in a version of the general interpreter that catches errors and replaces them by NaN returns",
    "created_at": "2021-07-23T16:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75972",
    "user": "mkoeppe"
}
```

Thanks.

I have not looked at the details, nor done any timing. But it seems to me that a better solution may be to try `domain=float` first, then `domain=complex` (or whatever is needed to make `fast_callable` use `interp_cdf`); and only in the end fall back to the general interpreter.

> 2. We now have "try to evaluate this as a real number, and return NaN (or skip it) if we can't" code in at least five places. Should this be made consistent, or (better yet) factored out? 

Yes, I guess there would be value in a version of the general interpreter that catches errors and replaces them by NaN returns



---

archive/issue_comments_075973.json:
```json
{
    "body": "By the way, I just came across https://trac.sagemath.org/attachment/ticket/5572/improve_fast_callable.6.patch, which seems to have done a lot of what we're doing again now...",
    "created_at": "2021-07-23T17:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75973",
    "user": "mkoeppe"
}
```

By the way, I just came across https://trac.sagemath.org/attachment/ticket/5572/improve_fast_callable.6.patch, which seems to have done a lot of what we're doing again now...



---

archive/issue_comments_075974.json:
```json
{
    "body": "Replying to [comment:15 mkoeppe]:\n> Thanks.\n> \n> I have not looked at the details, nor done any timing. But it seems to me that a better solution may be to try `domain=float` first, then `domain=complex` (or whatever is needed to make `fast_callable` use `interp_cdf`); and only in the end fall back to the general interpreter.\n\nThis is tough because there are so many plotting interfaces, and the fast-callables aren't created near the point of failure. In this case, `setup_for_eval_on_grid()` is preprocessing some of the plotting args and returning them to some other function that orchestrates the plotting. Then the failure occurs in *another* function that actually computes the plot points. \n\nSome major refactoring would be needed to do this all more intelligently. (I think we would also need to generate some kind of custom exception to avoid wrapping ten layers of code in one big `except TypeError` block.)",
    "created_at": "2021-07-23T17:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75974",
    "user": "mjo"
}
```

Replying to [comment:15 mkoeppe]:
> Thanks.
> 
> I have not looked at the details, nor done any timing. But it seems to me that a better solution may be to try `domain=float` first, then `domain=complex` (or whatever is needed to make `fast_callable` use `interp_cdf`); and only in the end fall back to the general interpreter.

This is tough because there are so many plotting interfaces, and the fast-callables aren't created near the point of failure. In this case, `setup_for_eval_on_grid()` is preprocessing some of the plotting args and returning them to some other function that orchestrates the plotting. Then the failure occurs in *another* function that actually computes the plot points. 

Some major refactoring would be needed to do this all more intelligently. (I think we would also need to generate some kind of custom exception to avoid wrapping ten layers of code in one big `except TypeError` block.)



---

archive/issue_comments_075975.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2021-07-23T17:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75975",
    "user": "mkoeppe"
}
```

Changing priority from major to minor.



---

archive/issue_comments_075976.json:
```json
{
    "body": "OK, thanks for the explanation. Then I would suggest that we declare the issue of this ticket as \"minor\" and set it aside for later consideration.",
    "created_at": "2021-07-23T17:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75976",
    "user": "mkoeppe"
}
```

OK, thanks for the explanation. Then I would suggest that we declare the issue of this ticket as "minor" and set it aside for later consideration.



---

archive/issue_comments_075977.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2021-07-23T17:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75977",
    "user": "mkoeppe"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075978.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2021-07-26T14:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75978",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_075979.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-07-26T14:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75979",
    "user": "mjo"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075980.json:
```json
{
    "body": "Replying to [comment:18 mkoeppe]:\n> OK, thanks for the explanation. Then I would suggest that we declare the issue of this ticket as \"minor\" and set it aside for later consideration. \n\nI actually hold a grudge against this bug from back when I was generating plots programmatically and the random appearance of `0.000000000001*I` would kill the whole thing after an hour, so I haven't given up.\n\nI tried a few more things, described in the first of the recent commit messages, and discovered problems with all of them. I did however eventually find a solution that is both unobtrusive and fast: wrap fast-callable evaluation in a class that can force the result to a specific output type. With ``domain=<something complex>`` and ``output=<something real>``, we return `NaN` unless the imaginary part is trivial, in which case we return the real part. In all other situations we simply try to coerce the output to the given type.\n\nThis allows us to plot over CDF but convert the result to float (possibly NaN) only on the way out, without having to hack that conversion logic into a hundred plotting functions. It's probably as fast as any solution could be; complex (two-float) operations necessarily take longer than plain float computations, but the difference is small in my non-rigorous tests, less than 10%.\n\nAn output wrapper is not used unless it's needed, so this doesn't affect any other uses of `fast_callable()` in the tree.",
    "created_at": "2021-07-26T14:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75980",
    "user": "mjo"
}
```

Replying to [comment:18 mkoeppe]:
> OK, thanks for the explanation. Then I would suggest that we declare the issue of this ticket as "minor" and set it aside for later consideration. 

I actually hold a grudge against this bug from back when I was generating plots programmatically and the random appearance of `0.000000000001*I` would kill the whole thing after an hour, so I haven't given up.

I tried a few more things, described in the first of the recent commit messages, and discovered problems with all of them. I did however eventually find a solution that is both unobtrusive and fast: wrap fast-callable evaluation in a class that can force the result to a specific output type. With ``domain=<something complex>`` and ``output=<something real>``, we return `NaN` unless the imaginary part is trivial, in which case we return the real part. In all other situations we simply try to coerce the output to the given type.

This allows us to plot over CDF but convert the result to float (possibly NaN) only on the way out, without having to hack that conversion logic into a hundred plotting functions. It's probably as fast as any solution could be; complex (two-float) operations necessarily take longer than plain float computations, but the difference is small in my non-rigorous tests, less than 10%.

An output wrapper is not used unless it's needed, so this doesn't affect any other uses of `fast_callable()` in the tree.



---

archive/issue_comments_075981.json:
```json
{
    "body": "This looks like a fine approach. I won't have time before mid August to look at it in detail. Just a quick comment:\n\n```\n+        # This tolerance was not chosen for any particular reason.\n+        if abs(ipart) < 1e-8:\n+            return self._output(rpart)\n+        else:\n+            return self._output(\"nan\")\n```\n\nProbably best to make these tolerances user-configurable (as an optional init argument of OutputWrapper and optional argument of `fast_callable`).",
    "created_at": "2021-07-26T20:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75981",
    "user": "mkoeppe"
}
```

This looks like a fine approach. I won't have time before mid August to look at it in detail. Just a quick comment:

```
+        # This tolerance was not chosen for any particular reason.
+        if abs(ipart) < 1e-8:
+            return self._output(rpart)
+        else:
+            return self._output("nan")
```

Probably best to make these tolerances user-configurable (as an optional init argument of OutputWrapper and optional argument of `fast_callable`).



---

archive/issue_comments_075982.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2021-07-26T23:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75982",
    "user": "mjo"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075983.json:
```json
{
    "body": "Replying to [comment:22 mkoeppe]:\n> Probably best to make these tolerances user-configurable (as an optional init argument of OutputWrapper and optional argument of `fast_callable`).\n> \n\nI'm glad you brought this up. I swept it under the rug when I had fifteen things on my internal problem stack, but it's a code smell: using a fixed tolerance isn't right, but adding the argument to `fast_callable()` and trying to explain how it will be used exposes too many implementation details.\n\nI think I can simplify things even further.",
    "created_at": "2021-07-26T23:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75983",
    "user": "mjo"
}
```

Replying to [comment:22 mkoeppe]:
> Probably best to make these tolerances user-configurable (as an optional init argument of OutputWrapper and optional argument of `fast_callable`).
> 

I'm glad you brought this up. I swept it under the rug when I had fifteen things on my internal problem stack, but it's a code smell: using a fixed tolerance isn't right, but adding the argument to `fast_callable()` and trying to explain how it will be used exposes too many implementation details.

I think I can simplify things even further.



---

archive/issue_comments_075984.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. Last 10 new commits:",
    "created_at": "2021-07-27T14:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75984",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. Last 10 new commits:



---

archive/issue_comments_075985.json:
```json
{
    "body": "Much better now. There's no need to solve the output-conversion problem more generally; we need it only for plotting, and creating the wrapper under sage.plot.misc eliminates all of the problems with the previous iteration.",
    "created_at": "2021-07-27T14:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75985",
    "user": "mjo"
}
```

Much better now. There's no need to solve the output-conversion problem more generally; we need it only for plotting, and creating the wrapper under sage.plot.misc eliminates all of the problems with the previous iteration.



---

archive/issue_comments_075986.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-07-27T14:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75986",
    "user": "mjo"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075987.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. Last 10 new commits:",
    "created_at": "2021-07-27T21:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75987",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. Last 10 new commits:



---

archive/issue_comments_075988.json:
```json
{
    "body": "This is looking nice. Similar to what I said in comment:22, I think the imaginary tolerance should be customizable on the level of the plot functions -- in the same way that options such as `detect_poles`, `adaptive_tolerance` are offered.",
    "created_at": "2021-08-15T02:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75988",
    "user": "mkoeppe"
}
```

This is looking nice. Similar to what I said in comment:22, I think the imaginary tolerance should be customizable on the level of the plot functions -- in the same way that options such as `detect_poles`, `adaptive_tolerance` are offered.



---

archive/issue_comments_075989.json:
```json
{
    "body": "Replying to [comment:27 mkoeppe]:\n> This is looking nice. Similar to what I said in comment:22, I think the imaginary tolerance should be customizable on the level of the plot functions -- in the same way that options such as `detect_poles`, `adaptive_tolerance` are offered.\n\nThose only work for the `plot()` function, and not for anything else that calls `setup_for_eval_on_grid()`. But once #32234 gets reviewed, I guess I wouldn't mind adding `imaginary_tolerance` to `plot.options`. In that case, we should probably go back later and try to make the options to the various plotting functions consistent (in another ticket).",
    "created_at": "2021-08-19T13:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75989",
    "user": "mjo"
}
```

Replying to [comment:27 mkoeppe]:
> This is looking nice. Similar to what I said in comment:22, I think the imaginary tolerance should be customizable on the level of the plot functions -- in the same way that options such as `detect_poles`, `adaptive_tolerance` are offered.

Those only work for the `plot()` function, and not for anything else that calls `setup_for_eval_on_grid()`. But once #32234 gets reviewed, I guess I wouldn't mind adding `imaginary_tolerance` to `plot.options`. In that case, we should probably go back later and try to make the options to the various plotting functions consistent (in another ticket).



---

archive/issue_comments_075990.json:
```json
{
    "body": "Here's a rebase and the `plot.options` interface. I still need to look closer at what's going on with `real_nth_root()` though; what's there is a hack.\n----\nNew commits:",
    "created_at": "2021-10-21T00:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75990",
    "user": "mjo"
}
```

Here's a rebase and the `plot.options` interface. I still need to look closer at what's going on with `real_nth_root()` though; what's there is a hack.
----
New commits:



---

archive/issue_comments_075991.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2021-10-21T00:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75991",
    "user": "mjo"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075992.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2021-11-03T12:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75992",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_075993.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-11-03T12:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75993",
    "user": "mjo"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075994.json:
```json
{
    "body": "The `real_nth_root()` fix reveals a new issue that may arise in some cases: symbolic functions that are not prepared to receive \"real\" arguments of the form `x + 0*I`. But the fix is not so bad as you can see. And it should be rare, since most sage operations will try to coerce things to the expected domain (and no other doctests fail, of course). The \"mod\" operation in this cases is a bit special in that regard.",
    "created_at": "2021-11-03T12:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75994",
    "user": "mjo"
}
```

The `real_nth_root()` fix reveals a new issue that may arise in some cases: symbolic functions that are not prepared to receive "real" arguments of the form `x + 0*I`. But the fix is not so bad as you can see. And it should be rare, since most sage operations will try to coerce things to the expected domain (and no other doctests fail, of course). The "mod" operation in this cases is a bit special in that regard.



---

archive/issue_comments_075995.json:
```json
{
    "body": "rebased branch, with one `\"\"\" -> r\"\"\"` change\n----\nNew commits:",
    "created_at": "2021-12-03T10:14:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75995",
    "user": "dimpase"
}
```

rebased branch, with one `""" -> r"""` change
----
New commits:



---

archive/issue_comments_075996.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-12-03T10:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75996",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_075997.json:
```json
{
    "body": "Wanna test this more. The new branch works with 9.5.beta7",
    "created_at": "2021-12-03T10:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75997",
    "user": "dimpase"
}
```

Wanna test this more. The new branch works with 9.5.beta7



---

archive/issue_comments_075998.json:
```json
{
    "body": "off to the bots",
    "created_at": "2021-12-03T10:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75998",
    "user": "dimpase"
}
```

off to the bots



---

archive/issue_comments_075999.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-12-03T10:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-75999",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076000.json:
```json
{
    "body": "Don't patchbots usually give higher priority to\n\"needs review\" than \"positive review\"?",
    "created_at": "2021-12-03T12:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76000",
    "user": "slelievre"
}
```

Don't patchbots usually give higher priority to
"needs review" than "positive review"?



---

archive/issue_comments_076001.json:
```json
{
    "body": "Replying to [comment:37 slelievre]:\n> Don't patchbots usually give higher priority to\n> \"needs review\" than \"positive review\"?\nI meant buildbots",
    "created_at": "2021-12-03T13:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76001",
    "user": "dimpase"
}
```

Replying to [comment:37 slelievre]:
> Don't patchbots usually give higher priority to
> "needs review" than "positive review"?
I meant buildbots



---

archive/issue_comments_076002.json:
```json
{
    "body": "I missed that part of the developer guide.",
    "created_at": "2021-12-03T23:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76002",
    "user": "slelievre"
}
```

I missed that part of the developer guide.



---

archive/issue_comments_076003.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2021-12-27T13:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76003",
    "user": "dimpase"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_076004.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2022-01-04T22:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76004",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076005.json:
```json
{
    "body": "On OSX:\n\n```\n**********************************************************************\nFile \"src/sage/plot/plot.py\", line 3943, in sage.plot.plot.?\nFailed example:\n    generate_plot_points(sin(x).function(x), (-pi, pi), randomize=False)\nExpected:\n    [(-3.141592653589793, -1.2246...e-16), (-2.748893571891069,\n    -0.3826834323650899), (-2.356194490192345, -0.707106781186547...),\n    (-2.1598449493429825, -0.831469612302545...), (-1.9634954084936207,\n    -0.9238795325112867), (-1.7671458676442586, -0.9807852804032304),\n    (-1.5707963267948966, -1.0), (-1.3744467859455345,\n    -0.9807852804032304), (-1.1780972450961724, -0.9238795325112867),\n    (-0.9817477042468103, -0.831469612302545...), (-0.7853981633974483,\n    -0.707106781186547...), (-0.39269908169872414, -0.3826834323650898),\n    (0.0, 0.0), (0.39269908169872414, 0.3826834323650898),\n    (0.7853981633974483, 0.707106781186547...), (0.9817477042468103,\n    0.831469612302545...), (1.1780972450961724, 0.9238795325112867),\n    (1.3744467859455345, 0.9807852804032304), (1.5707963267948966, 1.0),\n    (1.7671458676442586, 0.9807852804032304), (1.9634954084936207,\n    0.9238795325112867), (2.1598449493429825, 0.831469612302545...),\n    (2.356194490192345, 0.707106781186547...), (2.748893571891069,\n    0.3826834323650899), (3.141592653589793, 1.2246...e-16)]\nGot:\n    [(-3.141592653589793, -1.2246467991473532e-16),\n     (-2.748893571891069, -0.38268343236508984),\n     (-2.356194490192345, -0.7071067811865476),\n     (-2.1598449493429825, -0.8314696123025455),\n     (-1.9634954084936207, -0.9238795325112867),\n     (-1.7671458676442586, -0.9807852804032304),\n     (-1.5707963267948966, -1.0),\n     (-1.3744467859455345, -0.9807852804032304),\n     (-1.1780972450961724, -0.9238795325112867),\n     (-0.9817477042468103, -0.8314696123025451),\n     (-0.7853981633974483, -0.7071067811865475),\n     (-0.39269908169872414, -0.3826834323650898),\n     (0.0, 0.0),\n     (0.39269908169872414, 0.3826834323650898),\n     (0.7853981633974483, 0.7071067811865475),\n     (0.9817477042468103, 0.8314696123025451),\n     (1.1780972450961724, 0.9238795325112867),\n     (1.3744467859455345, 0.9807852804032304),\n     (1.5707963267948966, 1.0),\n     (1.7671458676442586, 0.9807852804032304),\n     (1.9634954084936207, 0.9238795325112867),\n     (2.1598449493429825, 0.8314696123025455),\n     (2.356194490192345, 0.7071067811865476),\n     (2.748893571891069, 0.38268343236508984),\n     (3.141592653589793, 1.2246467991473532e-16)]\n**********************************************************************\n1 item had failures:\n   1 of  44 in sage.plot.plot.?\n    [464 tests, 1 failure, 64.40 s]\n----------------------------------------------------------------------\nsage -t --long --random-seed=70775727671966200967886888406969327388 src/sage/plot/plot.py  # 1 doctest failed\n----------------------------------------------------------------------\n```\n",
    "created_at": "2022-01-04T22:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76005",
    "user": "vbraun"
}
```

On OSX:

```
**********************************************************************
File "src/sage/plot/plot.py", line 3943, in sage.plot.plot.?
Failed example:
    generate_plot_points(sin(x).function(x), (-pi, pi), randomize=False)
Expected:
    [(-3.141592653589793, -1.2246...e-16), (-2.748893571891069,
    -0.3826834323650899), (-2.356194490192345, -0.707106781186547...),
    (-2.1598449493429825, -0.831469612302545...), (-1.9634954084936207,
    -0.9238795325112867), (-1.7671458676442586, -0.9807852804032304),
    (-1.5707963267948966, -1.0), (-1.3744467859455345,
    -0.9807852804032304), (-1.1780972450961724, -0.9238795325112867),
    (-0.9817477042468103, -0.831469612302545...), (-0.7853981633974483,
    -0.707106781186547...), (-0.39269908169872414, -0.3826834323650898),
    (0.0, 0.0), (0.39269908169872414, 0.3826834323650898),
    (0.7853981633974483, 0.707106781186547...), (0.9817477042468103,
    0.831469612302545...), (1.1780972450961724, 0.9238795325112867),
    (1.3744467859455345, 0.9807852804032304), (1.5707963267948966, 1.0),
    (1.7671458676442586, 0.9807852804032304), (1.9634954084936207,
    0.9238795325112867), (2.1598449493429825, 0.831469612302545...),
    (2.356194490192345, 0.707106781186547...), (2.748893571891069,
    0.3826834323650899), (3.141592653589793, 1.2246...e-16)]
Got:
    [(-3.141592653589793, -1.2246467991473532e-16),
     (-2.748893571891069, -0.38268343236508984),
     (-2.356194490192345, -0.7071067811865476),
     (-2.1598449493429825, -0.8314696123025455),
     (-1.9634954084936207, -0.9238795325112867),
     (-1.7671458676442586, -0.9807852804032304),
     (-1.5707963267948966, -1.0),
     (-1.3744467859455345, -0.9807852804032304),
     (-1.1780972450961724, -0.9238795325112867),
     (-0.9817477042468103, -0.8314696123025451),
     (-0.7853981633974483, -0.7071067811865475),
     (-0.39269908169872414, -0.3826834323650898),
     (0.0, 0.0),
     (0.39269908169872414, 0.3826834323650898),
     (0.7853981633974483, 0.7071067811865475),
     (0.9817477042468103, 0.8314696123025451),
     (1.1780972450961724, 0.9238795325112867),
     (1.3744467859455345, 0.9807852804032304),
     (1.5707963267948966, 1.0),
     (1.7671458676442586, 0.9807852804032304),
     (1.9634954084936207, 0.9238795325112867),
     (2.1598449493429825, 0.8314696123025455),
     (2.356194490192345, 0.7071067811865476),
     (2.748893571891069, 0.38268343236508984),
     (3.141592653589793, 1.2246467991473532e-16)]
**********************************************************************
1 item had failures:
   1 of  44 in sage.plot.plot.?
    [464 tests, 1 failure, 64.40 s]
----------------------------------------------------------------------
sage -t --long --random-seed=70775727671966200967886888406969327388 src/sage/plot/plot.py  # 1 doctest failed
----------------------------------------------------------------------
```




---

archive/issue_comments_076006.json:
```json
{
    "body": "How about adding `# abs tol 1e-16` or using\nthe following output for the doctest:\n\n```\n    [(-3.141592653589793, -1.2246...e-16),\n     (-2.748893571891069, -0.382683432365089...),\n     (-2.356194490192345, -0.707106781186547...),\n     (-2.1598449493429825, -0.831469612302545...),\n     (-1.9634954084936207, -0.9238795325112867),\n     (-1.7671458676442586, -0.9807852804032304),\n     (-1.5707963267948966, -1.0),\n     (-1.3744467859455345, -0.9807852804032304),\n     (-1.1780972450961724, -0.9238795325112867),\n     (-0.9817477042468103, -0.831469612302545...),\n     (-0.7853981633974483, -0.707106781186547...),\n     (-0.39269908169872414, -0.3826834323650898),\n     (0.0, 0.0),\n     (0.39269908169872414, 0.3826834323650898),\n     (0.7853981633974483, 0.707106781186547...),\n     (0.9817477042468103, 0.831469612302545...),\n     (1.1780972450961724, 0.9238795325112867),\n     (1.3744467859455345, 0.9807852804032304),\n     (1.5707963267948966, 1.0),\n     (1.7671458676442586, 0.9807852804032304),\n     (1.9634954084936207, 0.9238795325112867),\n     (2.1598449493429825, 0.831469612302545...),\n     (2.356194490192345, 0.707106781186547...),\n     (2.748893571891069, 0.382683432365089...),\n     (3.141592653589793, 1.2246...e-16)]\n```\n",
    "created_at": "2022-01-05T04:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76006",
    "user": "slelievre"
}
```

How about adding `# abs tol 1e-16` or using
the following output for the doctest:

```
    [(-3.141592653589793, -1.2246...e-16),
     (-2.748893571891069, -0.382683432365089...),
     (-2.356194490192345, -0.707106781186547...),
     (-2.1598449493429825, -0.831469612302545...),
     (-1.9634954084936207, -0.9238795325112867),
     (-1.7671458676442586, -0.9807852804032304),
     (-1.5707963267948966, -1.0),
     (-1.3744467859455345, -0.9807852804032304),
     (-1.1780972450961724, -0.9238795325112867),
     (-0.9817477042468103, -0.831469612302545...),
     (-0.7853981633974483, -0.707106781186547...),
     (-0.39269908169872414, -0.3826834323650898),
     (0.0, 0.0),
     (0.39269908169872414, 0.3826834323650898),
     (0.7853981633974483, 0.707106781186547...),
     (0.9817477042468103, 0.831469612302545...),
     (1.1780972450961724, 0.9238795325112867),
     (1.3744467859455345, 0.9807852804032304),
     (1.5707963267948966, 1.0),
     (1.7671458676442586, 0.9807852804032304),
     (1.9634954084936207, 0.9238795325112867),
     (2.1598449493429825, 0.831469612302545...),
     (2.356194490192345, 0.707106781186547...),
     (2.748893571891069, 0.382683432365089...),
     (3.141592653589793, 1.2246...e-16)]
```




---

archive/issue_comments_076007.json:
```json
{
    "body": "Also, the blank line after an example or test block\nis not needed if it ends a docstring.",
    "created_at": "2022-01-05T05:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76007",
    "user": "slelievre"
}
```

Also, the blank line after an example or test block
is not needed if it ends a docstring.



---

archive/issue_comments_076008.json:
```json
{
    "body": "I've reworked that doctest to check something useful (and added `abs tol`) instead of a specific blob of digits.\n----\nNew commits:",
    "created_at": "2022-01-05T15:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76008",
    "user": "mjo"
}
```

I've reworked that doctest to check something useful (and added `abs tol`) instead of a specific blob of digits.
----
New commits:



---

archive/issue_comments_076009.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2022-01-05T15:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76009",
    "user": "mjo"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076010.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-01-06T11:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76010",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076011.json:
```json
{
    "body": "lgtm",
    "created_at": "2022-01-06T11:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76011",
    "user": "dimpase"
}
```

lgtm



---

archive/issue_comments_076012.json:
```json
{
    "body": "Class `FastCallablePlotWrapper`, method `__call__`,\ntest block needs double-colon:\n\n\n```diff\n-        Evaluation never fails and always returns a ``float``:\n+        Evaluation never fails and always returns a ``float``::\n```\n\n\nIt might also be worth checking why all patchbots\nreport pyflakes errors.",
    "created_at": "2022-01-08T06:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76012",
    "user": "slelievre"
}
```

Class `FastCallablePlotWrapper`, method `__call__`,
test block needs double-colon:


```diff
-        Evaluation never fails and always returns a ``float``:
+        Evaluation never fails and always returns a ``float``::
```


It might also be worth checking why all patchbots
report pyflakes errors.



---

archive/issue_comments_076013.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2022-01-08T13:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76013",
    "user": "git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_076014.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2022-01-08T13:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76014",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_076015.json:
```json
{
    "body": "Thanks, setting back to positive review as the last commit is trivial.\n\nI looked at the pyflakes failures, but the logs all say that everything is OK.",
    "created_at": "2022-01-08T13:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76015",
    "user": "mjo"
}
```

Thanks, setting back to positive review as the last commit is trivial.

I looked at the pyflakes failures, but the logs all say that everything is OK.



---

archive/issue_comments_076016.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-01-08T13:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76016",
    "user": "mjo"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076017.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2022-01-08T15:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76017",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_076018.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2022-01-08T15:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76018",
    "user": "git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_076019.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-01-08T15:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76019",
    "user": "mjo"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076020.json:
```json
{
    "body": "Also deleted a `set_random_seed()` call from a doctest that we don't need to add any more.",
    "created_at": "2022-01-08T15:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76020",
    "user": "mjo"
}
```

Also deleted a `set_random_seed()` call from a doctest that we don't need to add any more.



---

archive/issue_comments_076021.json:
```json
{
    "body": "Setting milestone to 9.6 now that 9.5 is out.",
    "created_at": "2022-01-30T15:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76021",
    "user": "slelievre"
}
```

Setting milestone to 9.6 now that 9.5 is out.



---

archive/issue_comments_076022.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2022-01-31T23:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76022",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_076023.json:
```json
{
    "body": "Thanks for this fix, it will be very helpful!",
    "created_at": "2022-02-18T12:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8450#issuecomment-76023",
    "user": "kcrisman"
}
```

Thanks for this fix, it will be very helpful!
