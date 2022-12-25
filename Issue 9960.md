# Issue 9960: Allow assumptions on the dependent variable in desolve

archive/issues_009960.json:
```json
{
    "body": "Assignee: @burcin\n\nSage should be able to solve ODE\n\n```\nx*diff(y,x)-x*sqrt(y^2+x^2)-y == 0\n```\n\nunder assumptions \n\n```\nx>0,y>0\n```\n\n\nNow \n\n```\ny=function('y',x)\nassume(y>0)\n```\n\npasses\n\n```\nassume(y(x)>0)\n```\n\nto Maxima. As a consequence, Maxima asks on sign of y. This should be fixed,\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9961\n\n",
    "created_at": "2010-09-21T19:29:55Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Allow assumptions on the dependent variable in desolve",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9960",
    "user": "https://github.com/robert-marik"
}
```
Assignee: @burcin

Sage should be able to solve ODE

```
x*diff(y,x)-x*sqrt(y^2+x^2)-y == 0
```

under assumptions 

```
x>0,y>0
```


Now 

```
y=function('y',x)
assume(y>0)
```

passes

```
assume(y(x)>0)
```

to Maxima. As a consequence, Maxima asks on sign of y. This should be fixed,


Issue created by migration from https://trac.sagemath.org/ticket/9961





---

archive/issue_comments_099580.json:
```json
{
    "body": "The patch fixes the problem, but we use strings in new optional argument of desolve. Some better suggestions are wellcomed.",
    "created_at": "2010-09-21T19:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99580",
    "user": "https://github.com/robert-marik"
}
```

The patch fixes the problem, but we use strings in new optional argument of desolve. Some better suggestions are wellcomed.



---

archive/issue_comments_099581.json:
```json
{
    "body": "Attachment [trac_9961.patch](tarball://root/attachments/some-uuid/ticket9961/trac_9961.patch) by @robert-marik created at 2010-09-21 19:48:19",
    "created_at": "2010-09-21T19:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99581",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac_9961.patch](tarball://root/attachments/some-uuid/ticket9961/trac_9961.patch) by @robert-marik created at 2010-09-21 19:48:19



---

archive/issue_comments_099582.json:
```json
{
    "body": "The patch depends on #9961 which runs all commands in one Maxima session.",
    "created_at": "2010-09-21T19:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99582",
    "user": "https://github.com/robert-marik"
}
```

The patch depends on #9961 which runs all commands in one Maxima session.



---

archive/issue_comments_099583.json:
```json
{
    "body": "Oops, I mean #9835 :)\nReplying to [comment:2 robert.marik]:\n> The patch depends on #9961 which runs all commands in one Maxima session.",
    "created_at": "2010-09-21T20:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99583",
    "user": "https://github.com/robert-marik"
}
```

Oops, I mean #9835 :)
Replying to [comment:2 robert.marik]:
> The patch depends on #9961 which runs all commands in one Maxima session.



---

archive/issue_comments_099584.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-21T20:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99584",
    "user": "https://github.com/robert-marik"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099585.json:
```json
{
    "body": "I appreciate the sentiment and idea, but adding a keyword exposes us to backwards incompatibility if someone (me?) ever gets to making the assumption system better - at least, that's my gut reaction.  What do you think?",
    "created_at": "2010-09-21T20:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99585",
    "user": "https://github.com/kcrisman"
}
```

I appreciate the sentiment and idea, but adding a keyword exposes us to backwards incompatibility if someone (me?) ever gets to making the assumption system better - at least, that's my gut reaction.  What do you think?



---

archive/issue_comments_099586.json:
```json
{
    "body": "Attachment [trac_9961-assume_function.patch](tarball://root/attachments/some-uuid/ticket9961/trac_9961-assume_function.patch) by @burcin created at 2010-09-21 21:03:06\n\napply only this patch",
    "created_at": "2010-09-21T21:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99586",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9961-assume_function.patch](tarball://root/attachments/some-uuid/ticket9961/trac_9961-assume_function.patch) by @burcin created at 2010-09-21 21:03:06

apply only this patch



---

archive/issue_comments_099587.json:
```json
{
    "body": "I was just thinking the same thing about the extra option. If we go with that option, the documentation should state clearly that this is a temporary solution.\n\nOn the other hand, attachment:trac_9961-assume_function.patch might provide an alternative option. I don't have much time so I didn't run tests or anything. Feel free to finish it up if you think it makes sense.",
    "created_at": "2010-09-21T21:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99587",
    "user": "https://github.com/burcin"
}
```

I was just thinking the same thing about the extra option. If we go with that option, the documentation should state clearly that this is a temporary solution.

On the other hand, attachment:trac_9961-assume_function.patch might provide an alternative option. I don't have much time so I didn't run tests or anything. Feel free to finish it up if you think it makes sense.



---

archive/issue_comments_099588.json:
```json
{
    "body": "Attachment [trac_9961-assume_function.take2.patch](tarball://root/attachments/some-uuid/ticket9961/trac_9961-assume_function.take2.patch) by @burcin created at 2010-09-22 16:04:48\n\napply only this patch",
    "created_at": "2010-09-22T16:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99588",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9961-assume_function.take2.patch](tarball://root/attachments/some-uuid/ticket9961/trac_9961-assume_function.take2.patch) by @burcin created at 2010-09-22 16:04:48

apply only this patch



---

archive/issue_comments_099589.json:
```json
{
    "body": "I uploaded a new patch attachment:trac_9961-assume_function.take2.patch. The previous version caused doctest failures like:\n\n\n```\nFile \"/home/burcin/sage/sage-4.5.2.rc0/devel/sage-s/sage/calculus/wester.py\", line 386:\n    sage: assume(real(x) > 0, real(y) > 0)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[131]>\", line 1, in <module>\n        assume(real(x) > Integer(0), real(y) > Integer(0))###line 386:\n    sage: assume(real(x) > 0, real(y) > 0)\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/symbolic/assumptions.py\", line 357, in assume\n        x.assume()\n      File \"expression.pyx\", line 1214, in sage.symbolic.expression.Expression.assume (sage/symbolic/expression.cpp:6320)\n    ValueError: Assumption is redundant\n```\n\n\nor \n\n\n```\nFile \"/home/burcin/sage/sage-4.5.2.rc0/devel/sage-s/sage/symbolic/expression.pyx\", line 7691:\n    sage: (a*q^k).sum(k, 0, oo)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_170[21]>\", line 1, in <module>\n        (a*q**k).sum(k, Integer(0), oo)###line 7691:\n    sage: (a*q^k).sum(k, 0, oo)\n      File \"expression.pyx\", line 7717, in sage.symbolic.expression.Expression.sum (sage/symbolic/expression.cpp:30994)\n        Mathematica, so even if the chosen backend can perform the summation the\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/calculus/calculus.py\", line 503, in symbolic_sum\n        result = maxima.simplify_sum(sum)\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1387, in __call__\n        return self._parent.function_call(self._name, list(args), kwds)\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1322, in function_call\n        return self.new(s)\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1097, in new\n        return self(code)\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1032, in __call__\n        return cls(self, x, name=name)\n      File \"/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1457, in __init__\n        raise TypeError, x\n    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(abs(q)-1>0)' before integral or limit evaluation, for example):\n    Is  abs(q)-1  positive, negative, or zero?\n```\n\n\nThis patch restricts the special treatment to user defined functions.\n\nThis passes all the symbolics related doctests, I think it's ready for review.",
    "created_at": "2010-09-22T16:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99589",
    "user": "https://github.com/burcin"
}
```

I uploaded a new patch attachment:trac_9961-assume_function.take2.patch. The previous version caused doctest failures like:


```
File "/home/burcin/sage/sage-4.5.2.rc0/devel/sage-s/sage/calculus/wester.py", line 386:
    sage: assume(real(x) > 0, real(y) > 0)
Exception raised:
    Traceback (most recent call last):
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[131]>", line 1, in <module>
        assume(real(x) > Integer(0), real(y) > Integer(0))###line 386:
    sage: assume(real(x) > 0, real(y) > 0)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/symbolic/assumptions.py", line 357, in assume
        x.assume()
      File "expression.pyx", line 1214, in sage.symbolic.expression.Expression.assume (sage/symbolic/expression.cpp:6320)
    ValueError: Assumption is redundant
```


or 


```
File "/home/burcin/sage/sage-4.5.2.rc0/devel/sage-s/sage/symbolic/expression.pyx", line 7691:
    sage: (a*q^k).sum(k, 0, oo)
Exception raised:
    Traceback (most recent call last):
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_170[21]>", line 1, in <module>
        (a*q**k).sum(k, Integer(0), oo)###line 7691:
    sage: (a*q^k).sum(k, 0, oo)
      File "expression.pyx", line 7717, in sage.symbolic.expression.Expression.sum (sage/symbolic/expression.cpp:30994)
        Mathematica, so even if the chosen backend can perform the summation the
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/calculus/calculus.py", line 503, in symbolic_sum
        result = maxima.simplify_sum(sum)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1387, in __call__
        return self._parent.function_call(self._name, list(args), kwds)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1322, in function_call
        return self.new(s)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1097, in new
        return self(code)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1032, in __call__
        return cls(self, x, name=name)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1457, in __init__
        raise TypeError, x
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(abs(q)-1>0)' before integral or limit evaluation, for example):
    Is  abs(q)-1  positive, negative, or zero?
```


This patch restricts the special treatment to user defined functions.

This passes all the symbolics related doctests, I think it's ready for review.



---

archive/issue_comments_099590.json:
```json
{
    "body": "Looks good for me, all tests passes.\n\nApply only attachment:trac_9961-assume_function.take2.patch and apply it on the top of #9835 \n\nI would give positive review, but probably kcrisman should also look on the patch.",
    "created_at": "2010-09-23T15:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99590",
    "user": "https://github.com/robert-marik"
}
```

Looks good for me, all tests passes.

Apply only attachment:trac_9961-assume_function.take2.patch and apply it on the top of #9835 

I would give positive review, but probably kcrisman should also look on the patch.



---

archive/issue_comments_099591.json:
```json
{
    "body": "I don't have time to give testing this the TLC it deserves, so I think the two of you should decide if you approve of each other's contributions.    However, it probably would be nice if we checked in the patch whether #9961 was actually fixed, like it does in Robert's patch!  If you can think of any other way to doctest this it would be nice.  Does it slow anything up very much?",
    "created_at": "2010-09-23T17:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99591",
    "user": "https://github.com/kcrisman"
}
```

I don't have time to give testing this the TLC it deserves, so I think the two of you should decide if you approve of each other's contributions.    However, it probably would be nice if we checked in the patch whether #9961 was actually fixed, like it does in Robert's patch!  If you can think of any other way to doctest this it would be nice.  Does it slow anything up very much?



---

archive/issue_comments_099592.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-23T17:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99592",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099593.json:
```json
{
    "body": "Attachment [trac_9961-assume_function.take3.patch](tarball://root/attachments/some-uuid/ticket9961/trac_9961-assume_function.take3.patch) by @robert-marik created at 2010-09-23 17:40:19\n\nBurcin's patch with doctest. Apply only this patch.",
    "created_at": "2010-09-23T17:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99593",
    "user": "https://github.com/robert-marik"
}
```

Attachment [trac_9961-assume_function.take3.patch](tarball://root/attachments/some-uuid/ticket9961/trac_9961-assume_function.take3.patch) by @robert-marik created at 2010-09-23 17:40:19

Burcin's patch with doctest. Apply only this patch.



---

archive/issue_comments_099594.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-23T17:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99594",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099595.json:
```json
{
    "body": "Oops, I actually tested Burcin's patch with one doctest added. This new patch is \nattachment:trac_9961-assume_function.take3.patch\n\nAgree that each closed ticket must be doctested. Hope, everything is O.K. now. Burcin, can you review my changes in your patch?",
    "created_at": "2010-09-23T17:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99595",
    "user": "https://github.com/robert-marik"
}
```

Oops, I actually tested Burcin's patch with one doctest added. This new patch is 
attachment:trac_9961-assume_function.take3.patch

Agree that each closed ticket must be doctested. Hope, everything is O.K. now. Burcin, can you review my changes in your patch?



---

archive/issue_comments_099596.json:
```json
{
    "body": "Of course there should be a doctest for the issue reported. Thanks for catching that Karl-Dieter.\n\nRobert, thank you for fixing my patch and adding the doctest.\n\nI'm changing this to a positive review, in light of comment:7 from Robert Marik and comment:8 from Karl-Dieter Crisman.",
    "created_at": "2010-09-23T21:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99596",
    "user": "https://github.com/burcin"
}
```

Of course there should be a doctest for the issue reported. Thanks for catching that Karl-Dieter.

Robert, thank you for fixing my patch and adding the doctest.

I'm changing this to a positive review, in light of comment:7 from Robert Marik and comment:8 from Karl-Dieter Crisman.



---

archive/issue_comments_099597.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-23T21:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99597",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T09:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9960#issuecomment-99598",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_010088.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-28T09:11:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9960",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9960#event-10088"
}
```
