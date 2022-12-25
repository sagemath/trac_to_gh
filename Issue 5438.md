# Issue 5438: Incorrect documentation and/or functionality in plot filling

archive/issues_005438.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  whuss\n\nKeywords: plot fill\n\nThe following example from documentation seems to work:\n\n\n```\ndef b(n): return lambda x: bessel_J(n, x) + 0.5*(n-1)\nplot([b(c) for c in [1..5]], 0, 40, fill = dict([(i, i+1) for i in [0..3]]))\n```\n\nbut the behavior is the same as\n\n```\ndef b(n): return lambda x: bessel_J(n, x) + 0.5*(n-1)\nplot([b(c) for c in [1..5]], 0, 40, fill = dict([(i, 5) for i in [0..3]]))\n```\n\nor anything else that evaluates to True as the second element of the dict.  The proper behavior is \n\n```\ndef b(n): return lambda x: bessel_J(n, x) + 0.5*(n-1)\nplot([b(c) for c in [1..5]], 0, 40, fill = dict([(i, [i+1]) for i in [0..3]]))\n```\n\nwhich is incidentally quite beautiful.\n\nThere are a few other such misleading/wrong example, and the documentation for how to use a dictionary which is a little confusing for people not familiar with Python yet\n\nHowever, this is really related to a bug, namely that for some reason the option of plotting between a function and a line isn't parsing properly.  These should hopefully be easy to fix and are closely related enough that one ticket seemed appropriate.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5438\n\n",
    "created_at": "2009-03-04T17:31:01Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Incorrect documentation and/or functionality in plot filling",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5438",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @williamstein

CC:  whuss

Keywords: plot fill

The following example from documentation seems to work:


```
def b(n): return lambda x: bessel_J(n, x) + 0.5*(n-1)
plot([b(c) for c in [1..5]], 0, 40, fill = dict([(i, i+1) for i in [0..3]]))
```

but the behavior is the same as

```
def b(n): return lambda x: bessel_J(n, x) + 0.5*(n-1)
plot([b(c) for c in [1..5]], 0, 40, fill = dict([(i, 5) for i in [0..3]]))
```

or anything else that evaluates to True as the second element of the dict.  The proper behavior is 

```
def b(n): return lambda x: bessel_J(n, x) + 0.5*(n-1)
plot([b(c) for c in [1..5]], 0, 40, fill = dict([(i, [i+1]) for i in [0..3]]))
```

which is incidentally quite beautiful.

There are a few other such misleading/wrong example, and the documentation for how to use a dictionary which is a little confusing for people not familiar with Python yet

However, this is really related to a bug, namely that for some reason the option of plotting between a function and a line isn't parsing properly.  These should hopefully be easy to fix and are closely related enough that one ticket seemed appropriate.

Issue created by migration from https://trac.sagemath.org/ticket/5438





---

archive/issue_comments_041977.json:
```json
{
    "body": "Changing assignee from @williamstein to @kcrisman.",
    "created_at": "2009-03-04T17:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41977",
    "user": "https://github.com/kcrisman"
}
```

Changing assignee from @williamstein to @kcrisman.



---

archive/issue_comments_041978.json:
```json
{
    "body": "Problem is that the first check in fill is for \n\n```\n            if fill == 'axis' or fill == True:\n```\n\nand we have\n\n```\nsage: preparse('5==True')\n'Integer(5)==True'\nsage: 5==True\nTrue\n```\n\nA change to \n\n```\n            if fill == 'axis' or fill is True:\n```\n\nsolves the problem, and then improving doc is easy.  I should be able to do this within a day or two.",
    "created_at": "2009-03-04T17:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41978",
    "user": "https://github.com/kcrisman"
}
```

Problem is that the first check in fill is for 

```
            if fill == 'axis' or fill == True:
```

and we have

```
sage: preparse('5==True')
'Integer(5)==True'
sage: 5==True
True
```

A change to 

```
            if fill == 'axis' or fill is True:
```

solves the problem, and then improving doc is easy.  I should be able to do this within a day or two.



---

archive/issue_comments_041979.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-04T17:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41979",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041980.json:
```json
{
    "body": "In addition to changing \"==\" to \"is\", this patch fixes a lot of minor issues in plot that I discovered while fixing this issue, mostly around documentation of the adaptive refinement, but also some weird bugs in error handling that nobody noticed since who sets verbose=1 on a regular basis?\n\nI didn't add doctests for the change from (msg, x) to (msg, xi) since it refers to the line of code and I figured that is a big hassle to change every time the plot code is changed, but if a referee disagrees they may add some.  I also removed the final exceptions+=1 block in the generate_plot_points since it seemed to be redundant, but if that's wrong then bring it back.  Otherwise I think everything works.",
    "created_at": "2009-03-07T03:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41980",
    "user": "https://github.com/kcrisman"
}
```

In addition to changing "==" to "is", this patch fixes a lot of minor issues in plot that I discovered while fixing this issue, mostly around documentation of the adaptive refinement, but also some weird bugs in error handling that nobody noticed since who sets verbose=1 on a regular basis?

I didn't add doctests for the change from (msg, x) to (msg, xi) since it refers to the line of code and I figured that is a big hassle to change every time the plot code is changed, but if a referee disagrees they may add some.  I also removed the final exceptions+=1 block in the generate_plot_points since it seemed to be redundant, but if that's wrong then bring it back.  Otherwise I think everything works.



---

archive/issue_comments_041981.json:
```json
{
    "body": "REFEREE REPORT:\n\nApplies fine to Sage 3.4, and fixes the bug described in the ticket. The changes to the documentation also look solid. One thing I noticed is that plot.py fails two of its unit tests (related to generate_plot_points, on lines 3028 and 3031; maybe a modification to the adaptive refinement algorithm affected these tests?) -- but this problem is not related to the patch at hand, and is outstanding in the original version as well. By the way, that's a very pretty graph :).",
    "created_at": "2009-03-17T23:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41981",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

REFEREE REPORT:

Applies fine to Sage 3.4, and fixes the bug described in the ticket. The changes to the documentation also look solid. One thing I noticed is that plot.py fails two of its unit tests (related to generate_plot_points, on lines 3028 and 3031; maybe a modification to the adaptive refinement algorithm affected these tests?) -- but this problem is not related to the patch at hand, and is outstanding in the original version as well. By the way, that's a very pretty graph :).



---

archive/issue_comments_041982.json:
```json
{
    "body": "After applying the patch **trac_5438.patch**, both of the following commands\n\n```\nplot(sin(x), xmin=-2*pi, xmax=2*pi, fill=\"0.5\")\n```\n\nand\n\n```\nplot(sin(x), xmin=-2*pi, xmax=2*pi, fill=0.5)\n```\n\nproduce the same looking plot. Notice that in the first command, the value for the fill option is the string `\"0.5\"`. In the second command, the value for the fill option is the number `0.5`. So for the fill option, if its value is a number given as a string, then the string is parsed for its numeric value. Is that intended?",
    "created_at": "2009-03-19T01:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41982",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

After applying the patch **trac_5438.patch**, both of the following commands

```
plot(sin(x), xmin=-2*pi, xmax=2*pi, fill="0.5")
```

and

```
plot(sin(x), xmin=-2*pi, xmax=2*pi, fill=0.5)
```

produce the same looking plot. Notice that in the first command, the value for the fill option is the string `"0.5"`. In the second command, the value for the fill option is the number `0.5`. So for the fill option, if its value is a number given as a string, then the string is parsed for its numeric value. Is that intended?



---

archive/issue_comments_041983.json:
```json
{
    "body": "Replying to [comment:4 mvngu]:\n> produce the same looking plot. Notice that in the first command, the value for the fill option is the string `\"0.5\"`. In the second command, the value for the fill option is the number `0.5`. So for the fill option, if its value is a number given as a string, then the string is parsed for its numeric value. Is that intended?\n\nHmm, I would say that the answer is yes, because I didn't change that part of the code:\n\n```\nsage: from sage.ext.fast_eval import fast_float, fast_float_constant, is_fast_float\nsage: fill=3\nsage: hasattr(fill,'__call__')\nFalse\nsage: float(fill)\n3.0\nsage: fill='3'\nsage: hasattr(fill,'__call__')\nFalse\nsage: float(fill)\n3.0\n```\n\nSo since that string can be coerced to a float, apparently the original author intended this behavior (even if implicitly).  Which certainly seems reasonable to me; it's not clear that it should throw an exception, and I can't think of another reasonable legitimate interpretation.",
    "created_at": "2009-03-19T12:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41983",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:4 mvngu]:
> produce the same looking plot. Notice that in the first command, the value for the fill option is the string `"0.5"`. In the second command, the value for the fill option is the number `0.5`. So for the fill option, if its value is a number given as a string, then the string is parsed for its numeric value. Is that intended?

Hmm, I would say that the answer is yes, because I didn't change that part of the code:

```
sage: from sage.ext.fast_eval import fast_float, fast_float_constant, is_fast_float
sage: fill=3
sage: hasattr(fill,'__call__')
False
sage: float(fill)
3.0
sage: fill='3'
sage: hasattr(fill,'__call__')
False
sage: float(fill)
3.0
```

So since that string can be coerced to a float, apparently the original author intended this behavior (even if implicitly).  Which certainly seems reasonable to me; it's not clear that it should throw an exception, and I can't think of another reasonable legitimate interpretation.



---

archive/issue_comments_041984.json:
```json
{
    "body": "Replying to [comment:4 mvngu]:\n\nMy guess is there's a call to float(), intended to coerce numeric types, which inadvertently parses strings. Its common to do less extensive argument checking in a typeless language like Python, however, since the alternative would be infeasible. I doubt that the author intended this behavior, but it is relatively harmless.",
    "created_at": "2009-03-19T21:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41984",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:4 mvngu]:

My guess is there's a call to float(), intended to coerce numeric types, which inadvertently parses strings. Its common to do less extensive argument checking in a typeless language like Python, however, since the alternative would be infeasible. I doubt that the author intended this behavior, but it is relatively harmless.



---

archive/issue_comments_041985.json:
```json
{
    "body": "This doctest failure needs to be addressed:\n\n```\nsage -t -long devel/sage/sage/plot/plot.py\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py\", line 3037:\n    sage: [len(generate_plot_points(f, (-pi, pi), adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]\nExpected:\n    [42, 67, 104]\nGot:\n    [36, 65, 91]\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py\", line 3040:\n    sage: [len(generate_plot_points(f, (-pi, pi), adaptive_recursion=i)) for i in [5, 10, 15]]\nExpected:\n    [34, 144, 897]\nGot:\n    [33, 131, 900]\n**********************************************************************\n```\n\nIt is also unclear to me if the changes here do not degrade the default plot settings since the now the adaptive plotting seems to generate fewer points.\n\nBill: Do not give positive reviews to any patch that causes doctest failures.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T08:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41985",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This doctest failure needs to be addressed:

```
sage -t -long devel/sage/sage/plot/plot.py
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py", line 3037:
    sage: [len(generate_plot_points(f, (-pi, pi), adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
Expected:
    [42, 67, 104]
Got:
    [36, 65, 91]
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py", line 3040:
    sage: [len(generate_plot_points(f, (-pi, pi), adaptive_recursion=i)) for i in [5, 10, 15]]
Expected:
    [34, 144, 897]
Got:
    [33, 131, 900]
**********************************************************************
```

It is also unclear to me if the changes here do not degrade the default plot settings since the now the adaptive plotting seems to generate fewer points.

Bill: Do not give positive reviews to any patch that causes doctest failures.

Cheers,

Michael



---

archive/issue_comments_041986.json:
```json
{
    "body": "Replying to [comment:7 mabshoff]:\n> This doctest failure needs to be addressed:\n> {{{\n> sage -t -long devel/sage/sage/plot/plot.py\n> **********************************************************************\n> File \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py\", line 3037:\n>     sage: [len(generate_plot_points(f, (-pi, pi), adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]\n> Expected:\n>     [42, 67, 104]\n> Got:\n>     [36, 65, 91]\n> **********************************************************************\n> File \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py\", line 3040:\n>     sage: [len(generate_plot_points(f, (-pi, pi), adaptive_recursion=i)) for i in [5, 10, 15]]\n> Expected:\n>     [34, 144, 897]\n> Got:\n>     [33, 131, 900]\n> **********************************************************************\n> }}}\n> It is also unclear to me if the changes here do not degrade the default plot settings since the now the adaptive plotting seems to generate fewer points.\n> \n> Bill: Do not give positive reviews to any patch that causes doctest failures.\n> \n> Cheers,\n> \n> Michael\n\nFor some reason, I thought the bug in question was evident in the main branch as well, meaning it would have had nothing to do with this patch. I see now that this is not the case; I must have got branches confused. Thanks for catching my mistake :).\n\nkcrisman: Might this bug have something to do with line 3037?",
    "created_at": "2009-03-25T15:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41986",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Replying to [comment:7 mabshoff]:
> This doctest failure needs to be addressed:
> {{{
> sage -t -long devel/sage/sage/plot/plot.py
> **********************************************************************
> File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py", line 3037:
>     sage: [len(generate_plot_points(f, (-pi, pi), adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
> Expected:
>     [42, 67, 104]
> Got:
>     [36, 65, 91]
> **********************************************************************
> File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage-main/sage/plot/plot.py", line 3040:
>     sage: [len(generate_plot_points(f, (-pi, pi), adaptive_recursion=i)) for i in [5, 10, 15]]
> Expected:
>     [34, 144, 897]
> Got:
>     [33, 131, 900]
> **********************************************************************
> }}}
> It is also unclear to me if the changes here do not degrade the default plot settings since the now the adaptive plotting seems to generate fewer points.
> 
> Bill: Do not give positive reviews to any patch that causes doctest failures.
> 
> Cheers,
> 
> Michael

For some reason, I thought the bug in question was evident in the main branch as well, meaning it would have had nothing to do with this patch. I see now that this is not the case; I must have got branches confused. Thanks for catching my mistake :).

kcrisman: Might this bug have something to do with line 3037?



---

archive/issue_comments_041987.json:
```json
{
    "body": "Certainly line 3037 must be the issue.   This was done to be consistent with another place where a delta occurs, which after all had the correct *mathematical* version of delta (since the number of plot points is actually n+1 for the usual definition of n in Riemann sums etc.).  I am sorry I didn't catch this earlier, but my computer consistently times out testing both calculus.py and plot.py, so I literally cannot catch these types of failed tests en masse.  I should have tried them by hand, though.\n\nAnyway, I don't think it necessarily downgrades the adaptive plotting significantly.  Note that for i=15 in the second example it actually increases the plot_points by 3!  When I run the old code, incidentally, I get\n\n```\nsage: [len(generate_plot_points(f, (-pi, pi), adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]\n[35, 51, 112]\n```\n\nwhich is better for some, worse for others.  Also note that this shows the test is *random* so this should have been caught earlier, unless current_randstate().python_random().random is set earlier?  I'll set randomize=False for the test.\n\nBut really, this is all because of a missed typo on my part.  The original refactoring changed the default plot_points to 5 from 200 just for the sake of generate_plot_points, even though the plot_points from _plot is always passed to this in an actual plotting situation, with default remaining 200.  So I will have to go back in and clarify that anyway, in addition to fixing the doctest.  Yes, there will be a smaller number of points, but I think the randomness makes a big enough swing that it is better to be mathematically accurate and consistent.  E.g.:\n\nOld:\n\n```\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]\n[689, 1145, 1978]\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]\n[707, 1138, 2004]\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]\n[704, 1137, 2020]\n```\n\nNew:\n\n```\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]\n[704, 1091, 1949]\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]\n[679, 1148, 2015]\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]\n[704, 1121, 1981]\n```\n\nOld: \n\n```\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]\n[697, 3235, 18312]\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]\n[693, 3357, 17117]\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]\n[700, 3815, 25313]\n```\n\nNew:\n\n```\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]\n[691, 3054, 41501]\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]\n[692, 4039, 18385]\nsage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]\n[708, 3125, 31209]\n```\n\nThese differences seem negligible to me, given the wide variation in the randomness.  I'll try to get a new patch up soon clarifying all these things.",
    "created_at": "2009-03-25T16:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41987",
    "user": "https://github.com/kcrisman"
}
```

Certainly line 3037 must be the issue.   This was done to be consistent with another place where a delta occurs, which after all had the correct *mathematical* version of delta (since the number of plot points is actually n+1 for the usual definition of n in Riemann sums etc.).  I am sorry I didn't catch this earlier, but my computer consistently times out testing both calculus.py and plot.py, so I literally cannot catch these types of failed tests en masse.  I should have tried them by hand, though.

Anyway, I don't think it necessarily downgrades the adaptive plotting significantly.  Note that for i=15 in the second example it actually increases the plot_points by 3!  When I run the old code, incidentally, I get

```
sage: [len(generate_plot_points(f, (-pi, pi), adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[35, 51, 112]
```

which is better for some, worse for others.  Also note that this shows the test is *random* so this should have been caught earlier, unless current_randstate().python_random().random is set earlier?  I'll set randomize=False for the test.

But really, this is all because of a missed typo on my part.  The original refactoring changed the default plot_points to 5 from 200 just for the sake of generate_plot_points, even though the plot_points from _plot is always passed to this in an actual plotting situation, with default remaining 200.  So I will have to go back in and clarify that anyway, in addition to fixing the doctest.  Yes, there will be a smaller number of points, but I think the randomness makes a big enough swing that it is better to be mathematically accurate and consistent.  E.g.:

Old:

```
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[689, 1145, 1978]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[707, 1138, 2004]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[704, 1137, 2020]
```

New:

```
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[704, 1091, 1949]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[679, 1148, 2015]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_tolerance=i)) for i in [0.01, 0.001, 0.0001]]
[704, 1121, 1981]
```

Old: 

```
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[697, 3235, 18312]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[693, 3357, 17117]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[700, 3815, 25313]
```

New:

```
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[691, 3054, 41501]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[692, 4039, 18385]
sage: [len(generate_plot_points(f, (-pi, pi), 200, adaptive_recursion=i)) for i in [5, 10, 15]]
[708, 3125, 31209]
```

These differences seem negligible to me, given the wide variation in the randomness.  I'll try to get a new patch up soon clarifying all these things.



---

archive/issue_comments_041988.json:
```json
{
    "body": "Based on 3.4",
    "created_at": "2009-03-29T02:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41988",
    "user": "https://github.com/kcrisman"
}
```

Based on 3.4



---

archive/issue_comments_041989.json:
```json
{
    "body": "Attachment [trac_5438.patch](tarball://root/attachments/some-uuid/ticket5438/trac_5438.patch) by @kcrisman created at 2009-03-29 02:57:51\n\nThis has added doctest, clarified yet more stuff, changed f to f(x) in anticipation of the Pynac switch (since the doctests would happen outside of plotting), and also fixed one weird but inconsequential bug in the slope field plot (sqrt was imported twice, but only the second one counted - which was good, because symbolic is what you want there).  Hope this satisfies all concerns.",
    "created_at": "2009-03-29T02:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41989",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_5438.patch](tarball://root/attachments/some-uuid/ticket5438/trac_5438.patch) by @kcrisman created at 2009-03-29 02:57:51

This has added doctest, clarified yet more stuff, changed f to f(x) in anticipation of the Pynac switch (since the doctests would happen outside of plotting), and also fixed one weird but inconsequential bug in the slope field plot (sqrt was imported twice, but only the second one counted - which was good, because symbolic is what you want there).  Hope this satisfies all concerns.



---

archive/issue_comments_041990.json:
```json
{
    "body": "REFEREE REPORT:\n\nThese changes seem to address the problems. Looks good to me -- all doctests passed. Positive review.",
    "created_at": "2009-03-31T18:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41990",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

REFEREE REPORT:

These changes seem to address the problems. Looks good to me -- all doctests passed. Positive review.



---

archive/issue_comments_041991.json:
```json
{
    "body": "This patch has rejects when attempting to merge it into my 3.4.1.rc0 merge tree:\n\n```\nsage-3.4.1.rc0/devel/sage$ patch -p1 --dry-run < trac_5438.patch \npatching file sage/plot/plot.py\nHunk #6 succeeded at 2688 (offset 9 lines).\nHunk #7 succeeded at 2908 (offset 9 lines).\nHunk #8 FAILED at 2931.\nHunk #9 succeeded at 2945 (offset 9 lines).\nHunk #10 succeeded at 2977 (offset 9 lines).\nHunk #11 succeeded at 2987 (offset 9 lines).\nHunk #12 FAILED at 3031.\nHunk #13 succeeded at 3061 (offset 9 lines).\nHunk #14 succeeded at 3082 (offset 9 lines).\nHunk #15 succeeded at 3101 (offset 9 lines).\n2 out of 15 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\npatching file sage/plot/plot_field.py\n```\n\nOnce it is rebase the positive review can be restored provided it does pass doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T01:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41991",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch has rejects when attempting to merge it into my 3.4.1.rc0 merge tree:

```
sage-3.4.1.rc0/devel/sage$ patch -p1 --dry-run < trac_5438.patch 
patching file sage/plot/plot.py
Hunk #6 succeeded at 2688 (offset 9 lines).
Hunk #7 succeeded at 2908 (offset 9 lines).
Hunk #8 FAILED at 2931.
Hunk #9 succeeded at 2945 (offset 9 lines).
Hunk #10 succeeded at 2977 (offset 9 lines).
Hunk #11 succeeded at 2987 (offset 9 lines).
Hunk #12 FAILED at 3031.
Hunk #13 succeeded at 3061 (offset 9 lines).
Hunk #14 succeeded at 3082 (offset 9 lines).
Hunk #15 succeeded at 3101 (offset 9 lines).
2 out of 15 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
patching file sage/plot/plot_field.py
```

Once it is rebase the positive review can be restored provided it does pass doctests.

Cheers,

Michael



---

archive/issue_comments_041992.json:
```json
{
    "body": "Turns out somebody got to changing f to f(x) ahead of me, else all is same.",
    "created_at": "2009-04-28T01:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41992",
    "user": "https://github.com/kcrisman"
}
```

Turns out somebody got to changing f to f(x) ahead of me, else all is same.



---

archive/issue_comments_041993.json:
```json
{
    "body": "Based on 3.4.2.alpha0",
    "created_at": "2009-04-28T01:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41993",
    "user": "https://github.com/kcrisman"
}
```

Based on 3.4.2.alpha0



---

archive/issue_comments_041994.json:
```json
{
    "body": "Attachment [trac_5438-rebase.patch](tarball://root/attachments/some-uuid/ticket5438/trac_5438-rebase.patch) by mabshoff created at 2009-05-04 18:46:30\n\nOk, if someone does inspect a couple of the plots before and after I am happy to merge this given that the number of points before and after is close enough.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T18:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41994",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5438-rebase.patch](tarball://root/attachments/some-uuid/ticket5438/trac_5438-rebase.patch) by mabshoff created at 2009-05-04 18:46:30

Ok, if someone does inspect a couple of the plots before and after I am happy to merge this given that the number of points before and after is close enough.

Cheers,

Michael



---

archive/issue_comments_041995.json:
```json
{
    "body": "The plots look fine. This patch applies to Sage 3.4.2 and passes its doctests. Positive review.",
    "created_at": "2009-05-06T05:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41995",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

The plots look fine. This patch applies to Sage 3.4.2 and passes its doctests. Positive review.



---

archive/issue_comments_041996.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-14T06:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41996",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041997.json:
```json
{
    "body": "Merged trac_5438-rebase.patch  in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-14T06:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5438#issuecomment-41997",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5438-rebase.patch  in Sage 4.0.alpha0.

Cheers,

Michael
