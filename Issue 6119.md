# Issue 6119: implement taylor series without maxima

archive/issues_006119.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman @rwst\n\nGinac has series about zero, it should be easy to shift to get the series about any point.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6119\n\n",
    "created_at": "2009-05-22T02:38:25Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "implement taylor series without maxima",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6119",
    "user": "https://github.com/robertwb"
}
```
Assignee: @burcin

CC:  @kcrisman @rwst

Ginac has series about zero, it should be easy to shift to get the series about any point.

Issue created by migration from https://trac.sagemath.org/ticket/6119





---

archive/issue_comments_048805.json:
```json
{
    "body": "From comment:6:ticket:9555:\n\n> The taylor() method is cruft left over from pre-pynac symbolics. We should deprecate it in favor of the series() method. It's perfectly acceptable to give Puiseux series as a result of a call to .series(). I expect this to be done in #6119, where we add an algorithm= option to .series(). The default behavior can be to call pynac and fall back to maxima if that returns an error.\n\nIn short, we should change this ticket to cover this transition. Series expansions in Pynac need more work to match what maxima does. That should be tracked on the pynac issue tracker:\n\nhttps://bitbucket.org/burcin/pynac/issues",
    "created_at": "2011-06-29T13:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6119#issuecomment-48805",
    "user": "https://github.com/burcin"
}
```

From comment:6:ticket:9555:

> The taylor() method is cruft left over from pre-pynac symbolics. We should deprecate it in favor of the series() method. It's perfectly acceptable to give Puiseux series as a result of a call to .series(). I expect this to be done in #6119, where we add an algorithm= option to .series(). The default behavior can be to call pynac and fall back to maxima if that returns an error.

In short, we should change this ticket to cover this transition. Series expansions in Pynac need more work to match what maxima does. That should be tracked on the pynac issue tracker:

https://bitbucket.org/burcin/pynac/issues



---

archive/issue_comments_048806.json:
```json
{
    "body": "As I say in #9555, I think that changing the `.taylor()` method so that it calls a suitably Taylor-only version of the `.series()` method is preferable, especially since the global name `taylor()` should really be kept.",
    "created_at": "2011-06-29T13:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6119#issuecomment-48806",
    "user": "https://github.com/kcrisman"
}
```

As I say in #9555, I think that changing the `.taylor()` method so that it calls a suitably Taylor-only version of the `.series()` method is preferable, especially since the global name `taylor()` should really be kept.



---

archive/issue_comments_048807.json:
```json
{
    "body": "See also http://sourceforge.net/p/maxima/bugs/2850/ where this comes up again.",
    "created_at": "2014-12-06T20:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6119#issuecomment-48807",
    "user": "https://github.com/kcrisman"
}
```

See also http://sourceforge.net/p/maxima/bugs/2850/ where this comes up again.



---

archive/issue_comments_048808.json:
```json
{
    "body": "> As I say in #9555, I think that changing the `.taylor()` method so that it calls a suitably Taylor-only version of the `.series()` method is preferable, especially since the global name `taylor()` should really be kept.\nAnd I'm quoted at [this SO comment](http://stackoverflow.com/questions/27288164/non-integral-exponent-for-taylor-expansion-using-sage/27297471) though I still have to think more about how we should solve this.",
    "created_at": "2014-12-08T14:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6119#issuecomment-48808",
    "user": "https://github.com/kcrisman"
}
```

> As I say in #9555, I think that changing the `.taylor()` method so that it calls a suitably Taylor-only version of the `.series()` method is preferable, especially since the global name `taylor()` should really be kept.
And I'm quoted at [this SO comment](http://stackoverflow.com/questions/27288164/non-integral-exponent-for-taylor-expansion-using-sage/27297471) though I still have to think more about how we should solve this.



---

archive/issue_comments_048809.json:
```json
{
    "body": "Is this deprecating or simply replacing?  Sorry for being confused.\n----\nNew commits:",
    "created_at": "2017-01-18T14:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6119#issuecomment-48809",
    "user": "https://github.com/kcrisman"
}
```

Is this deprecating or simply replacing?  Sorry for being confused.
----
New commits:



---

archive/issue_comments_048810.json:
```json
{
    "body": "Too fast. The deprecation part is upcoming. The Maxima replacement depends on a bugfix in upcoming pynac-0.7.4 for one doctest fail.",
    "created_at": "2017-01-18T14:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6119#issuecomment-48810",
    "user": "https://github.com/rwst"
}
```

Too fast. The deprecation part is upcoming. The Maxima replacement depends on a bugfix in upcoming pynac-0.7.4 for one doctest fail.



---

archive/issue_comments_048811.json:
```json
{
    "body": "Replying to [comment:3 kcrisman]:\n> As I say in #9555, I think that changing the `.taylor()` method so that it calls a suitably Taylor-only version of the `.series()` method is preferable, especially since the global name `taylor()` should really be kept.\n\nJust rereading. So maybe we already have finished the ticket? If so, please review.",
    "created_at": "2017-01-18T14:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6119#issuecomment-48811",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:3 kcrisman]:
> As I say in #9555, I think that changing the `.taylor()` method so that it calls a suitably Taylor-only version of the `.series()` method is preferable, especially since the global name `taylor()` should really be kept.

Just rereading. So maybe we already have finished the ticket? If so, please review.



---

archive/issue_comments_048812.json:
```json
{
    "body": "Nah, I think it is better to do *some* form of deprecation warning rather than a totally silent change, though I think that keeping taylor as giving taylor only would be plausible too.",
    "created_at": "2017-01-18T15:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6119#issuecomment-48812",
    "user": "https://github.com/kcrisman"
}
```

Nah, I think it is better to do *some* form of deprecation warning rather than a totally silent change, though I think that keeping taylor as giving taylor only would be plausible too.



---

archive/issue_comments_048813.json:
```json
{
    "body": "Maxima is still faster than GiNaC in the cases with irrational coefficients so we will have to use GiNaC/Pynac for both `series` and `taylor` only in the rational case.",
    "created_at": "2017-01-18T15:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6119",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6119#issuecomment-48813",
    "user": "https://github.com/rwst"
}
```

Maxima is still faster than GiNaC in the cases with irrational coefficients so we will have to use GiNaC/Pynac for both `series` and `taylor` only in the rational case.
