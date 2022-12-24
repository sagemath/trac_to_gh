# Issue 9634: binomial does not accept variable when only in the lower argument

archive/issues_009634.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  kcrisman jpflori rws\n\n\n```\nsage: var('k')\nk \nsage: binomial(x,3)\n1/6*(x - 2)*(x - 1)*x\nsage: binomial(3,k)\n---------------------------------------------------------------------------\nTypeError: Either m or x-m must be an integer \n```\n\n\nFrom kcrisman:\nIs this a bug?  I would say yes, because\n\n```\nsage: binomial(x,k)\nbinomial(x, k)\n```\n\nworks, but maybe we want to have it be a specific integer if the top\nnumber is given?  Any input?\n\nIssue created by migration from https://trac.sagemath.org/ticket/9634\n\n",
    "created_at": "2010-07-29T07:29:28Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "binomial does not accept variable when only in the lower argument",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9634",
    "user": "Henryk.Trappmann"
}
```
Assignee: AlexGhitza

CC:  kcrisman jpflori rws


```
sage: var('k')
k 
sage: binomial(x,3)
1/6*(x - 2)*(x - 1)*x
sage: binomial(3,k)
---------------------------------------------------------------------------
TypeError: Either m or x-m must be an integer 
```


From kcrisman:
Is this a bug?  I would say yes, because

```
sage: binomial(x,k)
binomial(x, k)
```

works, but maybe we want to have it be a specific integer if the top
number is given?  Any input?

Issue created by migration from https://trac.sagemath.org/ticket/9634





---

archive/issue_comments_093367.json:
```json
{
    "body": "Changing component from basic arithmetic to symbolics.",
    "created_at": "2010-07-29T13:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93367",
    "user": "kcrisman"
}
```

Changing component from basic arithmetic to symbolics.



---

archive/issue_comments_093368.json:
```json
{
    "body": "Changing assignee from AlexGhitza to burcin.",
    "created_at": "2010-07-29T13:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93368",
    "user": "kcrisman"
}
```

Changing assignee from AlexGhitza to burcin.



---

archive/issue_comments_093369.json:
```json
{
    "body": "make the top level binomial() function symbolic",
    "created_at": "2010-10-11T15:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93369",
    "user": "burcin"
}
```

make the top level binomial() function symbolic



---

archive/issue_comments_093370.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-10-11T15:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93370",
    "user": "burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_093371.json:
```json
{
    "body": "Attachment [trac_9634-symbolic_binomial.patch](tarball://root/attachments/some-uuid/ticket9634/trac_9634-symbolic_binomial.patch) by burcin created at 2010-10-11 15:20:12\n\nattachment:trac_9634-symbolic_binomial.patch replaces the top level `binomial()` function with the one defined in `sage.functions.other`. This version can handle symbolic input, as opposed to the previous one from `sage.rings.arith`.\n\nThis still needs work, since the files `sage/functions/other.py` and `sage/rings/arith.py` don't pass doctests yet. We need to improve the speed of numerical approximation using the `gamma` trick from `sage.rings.arith.binomial` and change `sage.symbolic.pynac.py_binomial()` to handle large integers.",
    "created_at": "2010-10-11T15:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93371",
    "user": "burcin"
}
```

Attachment [trac_9634-symbolic_binomial.patch](tarball://root/attachments/some-uuid/ticket9634/trac_9634-symbolic_binomial.patch) by burcin created at 2010-10-11 15:20:12

attachment:trac_9634-symbolic_binomial.patch replaces the top level `binomial()` function with the one defined in `sage.functions.other`. This version can handle symbolic input, as opposed to the previous one from `sage.rings.arith`.

This still needs work, since the files `sage/functions/other.py` and `sage/rings/arith.py` don't pass doctests yet. We need to improve the speed of numerical approximation using the `gamma` trick from `sage.rings.arith.binomial` and change `sage.symbolic.pynac.py_binomial()` to handle large integers.



---

archive/issue_comments_093372.json:
```json
{
    "body": "Replying to [comment:2 burcin]:\n> attachment:trac_9634-symbolic_binomial.patch replaces the top level `binomial()` function with the one defined in `sage.functions.other`. This version can handle symbolic input, as opposed to the previous one from `sage.rings.arith`.\n> \n\nGood catch; I was pretty sure we had rewritten that at some point, but I have trouble following the imports.\n\n> This still needs work, since the files `sage/functions/other.py` and `sage/rings/arith.py` don't pass doctests yet. \n\n> We need to improve the speed of numerical approximation using the `gamma` trick from `sage.rings.arith.binomial` and change `sage.symbolic.pynac.py_binomial()` to handle large integers.\nIs that part of this ticket?  Are you saying that the numerical approximation has slowed down dramatically from the `rings.arith` version?",
    "created_at": "2011-04-25T15:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93372",
    "user": "kcrisman"
}
```

Replying to [comment:2 burcin]:
> attachment:trac_9634-symbolic_binomial.patch replaces the top level `binomial()` function with the one defined in `sage.functions.other`. This version can handle symbolic input, as opposed to the previous one from `sage.rings.arith`.
> 

Good catch; I was pretty sure we had rewritten that at some point, but I have trouble following the imports.

> This still needs work, since the files `sage/functions/other.py` and `sage/rings/arith.py` don't pass doctests yet. 

> We need to improve the speed of numerical approximation using the `gamma` trick from `sage.rings.arith.binomial` and change `sage.symbolic.pynac.py_binomial()` to handle large integers.
Is that part of this ticket?  Are you saying that the numerical approximation has slowed down dramatically from the `rings.arith` version?



---

archive/issue_comments_093373.json:
```json
{
    "body": "This very bug trips up many potential users.  Ping.   Let's fix it!!",
    "created_at": "2012-01-04T05:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93373",
    "user": "was"
}
```

This very bug trips up many potential users.  Ping.   Let's fix it!!



---

archive/issue_comments_093374.json:
```json
{
    "body": "Attachment [trac_9634-symbolic_binomial.take2.patch](tarball://root/attachments/some-uuid/ticket9634/trac_9634-symbolic_binomial.take2.patch) by burcin created at 2013-07-01 06:23:27\n\nI uploaded a new patch that fixes doctests as well. This meant reimplementing the `_eval_()` and `_evalf_()` methods to override those defined in pynac.\n\nPatchbot, apply only trac_9634-symbolic_binomial.take2.patch.",
    "created_at": "2013-07-01T06:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93374",
    "user": "burcin"
}
```

Attachment [trac_9634-symbolic_binomial.take2.patch](tarball://root/attachments/some-uuid/ticket9634/trac_9634-symbolic_binomial.take2.patch) by burcin created at 2013-07-01 06:23:27

I uploaded a new patch that fixes doctests as well. This meant reimplementing the `_eval_()` and `_evalf_()` methods to override those defined in pynac.

Patchbot, apply only trac_9634-symbolic_binomial.take2.patch.



---

archive/issue_comments_093375.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-01T06:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93375",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093376.json:
```json
{
    "body": "for the bot:\n\napply trac_9634-symbolic_binomial.take2.patch\u200b",
    "created_at": "2013-07-23T09:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93376",
    "user": "chapoton"
}
```

for the bot:

apply trac_9634-symbolic_binomial.take2.patch​



---

archive/issue_comments_093377.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-02-14T15:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93377",
    "user": "rws"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093378.json:
```json
{
    "body": "The patch2 does not apply cleanly, with two hunks failing, which I fixed manually, and push it to git. However:\n\n```\nsage -t src/sage/functions/other.py  # 18 doctests failed\nsage -t src/sage/combinat/partition.py  # 2 doctests failed\nsage -t src/sage/rings/arith.py  # 1 doctest failed\nsage -t src/sage/symbolic/expression.pyx  # 2 doctests failed\n```\n\n----\nNew commits:",
    "created_at": "2014-02-14T15:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93378",
    "user": "rws"
}
```

The patch2 does not apply cleanly, with two hunks failing, which I fixed manually, and push it to git. However:

```
sage -t src/sage/functions/other.py  # 18 doctests failed
sage -t src/sage/combinat/partition.py  # 2 doctests failed
sage -t src/sage/rings/arith.py  # 1 doctest failed
sage -t src/sage/symbolic/expression.pyx  # 2 doctests failed
```

----
New commits:



---

archive/issue_comments_093379.json:
```json
{
    "body": "Never mind, it's all fine, I had an incomplete installation.",
    "created_at": "2014-02-15T09:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93379",
    "user": "rws"
}
```

Never mind, it's all fine, I had an incomplete installation.



---

archive/issue_comments_093380.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-02-15T09:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93380",
    "user": "rws"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_093381.json:
```json
{
    "body": "merge conflict, please merge the latest beta into this branch.",
    "created_at": "2014-02-20T15:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93381",
    "user": "vbraun"
}
```

merge conflict, please merge the latest beta into this branch.



---

archive/issue_comments_093382.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2014-02-20T16:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93382",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_093383.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2014-02-20T16:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93383",
    "user": "git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_093384.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-20T16:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93384",
    "user": "rws"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093385.json:
```json
{
    "body": "OK I retested after merge, though only combinat. The number in that commit message is wrong, please ignore.",
    "created_at": "2014-02-20T16:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93385",
    "user": "rws"
}
```

OK I retested after merge, though only combinat. The number in that commit message is wrong, please ignore.



---

archive/issue_comments_093386.json:
```json
{
    "body": "The branch loses the \"Polynomial\" global which causes a number of doctest falures\n\n```\nsage -t --long src/sage/rings/polynomial/polynomial_element.pyx\n**********************************************************************\nFile \"src/sage/rings/polynomial/polynomial_element.pyx\", line 2592, in sage.rings.polynomial.polynomial_element.Polynomial.denominator\nFailed example:\n    isinstance(x.numerator() / x.denominator(), Polynomial)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/buildbot/sage/redhawk-1/sage_git/build/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 480, in _run\n        self.execute(example, compiled, test.globs)\n      File \"/scratch/buildbot/sage/redhawk-1/sage_git/build/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 839, in execute\n        exec compiled in globs\n      File \"<doctest sage.rings.polynomial.polynomial_element.Polynomial.denominator[13]>\", line 1, in <module>\n        isinstance(x.numerator() / x.denominator(), Polynomial)\n    NameError: name 'Polynomial' is not defined\n```\n",
    "created_at": "2014-02-21T14:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93386",
    "user": "vbraun"
}
```

The branch loses the "Polynomial" global which causes a number of doctest falures

```
sage -t --long src/sage/rings/polynomial/polynomial_element.pyx
**********************************************************************
File "src/sage/rings/polynomial/polynomial_element.pyx", line 2592, in sage.rings.polynomial.polynomial_element.Polynomial.denominator
Failed example:
    isinstance(x.numerator() / x.denominator(), Polynomial)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/buildbot/sage/redhawk-1/sage_git/build/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 480, in _run
        self.execute(example, compiled, test.globs)
      File "/scratch/buildbot/sage/redhawk-1/sage_git/build/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 839, in execute
        exec compiled in globs
      File "<doctest sage.rings.polynomial.polynomial_element.Polynomial.denominator[13]>", line 1, in <module>
        isinstance(x.numerator() / x.denominator(), Polynomial)
    NameError: name 'Polynomial' is not defined
```




---

archive/issue_comments_093387.json:
```json
{
    "body": "The funny thing is, it appears the global definition of `Polynomial` now missing is in `power_series_ring_element.pyx` which was indirectly and illogically imported in `polynomial_ring_element.pyx` before the author's patch.\n\nEvidently he should have submitted the import cleanup separately.\n\nOffhand, I'm not able to fix this, any takers?",
    "created_at": "2014-02-21T17:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93387",
    "user": "rws"
}
```

The funny thing is, it appears the global definition of `Polynomial` now missing is in `power_series_ring_element.pyx` which was indirectly and illogically imported in `polynomial_ring_element.pyx` before the author's patch.

Evidently he should have submitted the import cleanup separately.

Offhand, I'm not able to fix this, any takers?



---

archive/issue_comments_093388.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2014-02-21T17:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93388",
    "user": "rws"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093389.json:
```json
{
    "body": "Replying to [comment:17 rws]:\n> Evidently he should have submitted the import cleanup separately.\nIndeed.",
    "created_at": "2014-02-21T17:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93389",
    "user": "jdemeyer"
}
```

Replying to [comment:17 rws]:
> Evidently he should have submitted the import cleanup separately.
Indeed.



---

archive/issue_comments_093390.json:
```json
{
    "body": "In any case, Polynomial should just be imported into the global namespace in `src/sage/rings/polynomial/all.py`. The import cleanup is good, even though it should have been separate.",
    "created_at": "2014-02-21T20:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93390",
    "user": "vbraun"
}
```

In any case, Polynomial should just be imported into the global namespace in `src/sage/rings/polynomial/all.py`. The import cleanup is good, even though it should have been separate.



---

archive/issue_comments_093391.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-02-21T23:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93391",
    "user": "vbraun"
}
```

New commits:



---

archive/issue_comments_093392.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-02-21T23:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93392",
    "user": "vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093393.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-22T06:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93393",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_093394.json:
```json
{
    "body": "Please follow up in #16726",
    "created_at": "2014-08-01T14:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9634#issuecomment-93394",
    "user": "ppurka"
}
```

Please follow up in #16726
