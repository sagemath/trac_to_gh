# Issue 9032: no method numerical_approx for integers and rationals

archive/issues_009032.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @kcrisman\n\n\n```\nsage: a=8\nsage: a.n()\n8.00000000000000\nsage: a.numerical_approx()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/zimmerma/<ipython console> in <module>()\n\n/usr/local/sage-4.4.2/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2628)()\n\n/usr/local/sage-4.4.2/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2828)()\n\n/usr/local/sage-4.4.2/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2595)()\n\nAttributeError: 'sage.rings.integer.Integer' object has no attribute 'numerical_approx'\n```\n\nThe same holds for a=17/2 for example.\n\nSince `n` is a shortcut for `numerical_approx`,\nit should work with `numerical_approx` too. In addition,\nif one uses a variable `n` is a program, it would be more\nportable to use `numerical_approx`. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9032\n\n",
    "created_at": "2010-05-24T09:12:23Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "no method numerical_approx for integers and rationals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9032",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @aghitza

CC:  @kcrisman


```
sage: a=8
sage: a.n()
8.00000000000000
sage: a.numerical_approx()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/zimmerma/<ipython console> in <module>()

/usr/local/sage-4.4.2/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2628)()

/usr/local/sage-4.4.2/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2828)()

/usr/local/sage-4.4.2/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2595)()

AttributeError: 'sage.rings.integer.Integer' object has no attribute 'numerical_approx'
```

The same holds for a=17/2 for example.

Since `n` is a shortcut for `numerical_approx`,
it should work with `numerical_approx` too. In addition,
if one uses a variable `n` is a program, it would be more
portable to use `numerical_approx`. 

Issue created by migration from https://trac.sagemath.org/ticket/9032





---

archive/issue_comments_083450.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-05-26T15:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83450",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_083451.json:
```json
{
    "body": "Is there an example when a.numerical_approx() works?\n\nAfter reading the documentation on numerical_approx(), I don't think it can be used in this manner.  \n\nNote that a.N() does not work either for your example.",
    "created_at": "2011-01-08T22:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83451",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Is there an example when a.numerical_approx() works?

After reading the documentation on numerical_approx(), I don't think it can be used in this manner.  

Note that a.N() does not work either for your example.



---

archive/issue_comments_083452.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-10T04:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83452",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083453.json:
```json
{
    "body": "a.numerical_approx() needed to be defined in sage.misc.element.pyx. However n() already defined there calls and checks if the element type already has numerical_approx(). So this would cause an infinite loop. \n\nSo instead now it calls to see if it has _numerical_approx()\n\nI changed all the files where a specific type defined numerical_approx to _numerical_approx and defined an \"empty method\" numerical_approx, which just calls _numerical_approx.\n\nSo now every type should automatically have a numerical_approx. If a specific one is defined then that is called or it simply coerces it to be a real or complex approx.",
    "created_at": "2011-01-10T04:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83453",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

a.numerical_approx() needed to be defined in sage.misc.element.pyx. However n() already defined there calls and checks if the element type already has numerical_approx(). So this would cause an infinite loop. 

So instead now it calls to see if it has _numerical_approx()

I changed all the files where a specific type defined numerical_approx to _numerical_approx and defined an "empty method" numerical_approx, which just calls _numerical_approx.

So now every type should automatically have a numerical_approx. If a specific one is defined then that is called or it simply coerces it to be a real or complex approx.



---

archive/issue_comments_083454.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-01-10T09:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83454",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_083455.json:
```json
{
    "body": "hi, with Sage 4.6 I got an error while importing the patch:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: 9032\nsage: hg_sage.import_patch(\"/tmp/trac_9032.patch\")\ncd \"/usr/local/sage/devel/sage\" && hg status\ncd \"/usr/local/sage/devel/sage\" && hg status\ncd \"/usr/local/sage/devel/sage\" && hg import   \"/tmp/trac_9032.patch\"\napplying /tmp/trac_9032.patch\nabort: malformed patch a/sage/structure/element.pyx @@ -578,24 +580,26 @@\n```\n\nPaul",
    "created_at": "2011-01-10T09:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83455",
    "user": "https://github.com/zimmermann6"
}
```

hi, with Sage 4.6 I got an error while importing the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 9032
sage: hg_sage.import_patch("/tmp/trac_9032.patch")
cd "/usr/local/sage/devel/sage" && hg status
cd "/usr/local/sage/devel/sage" && hg status
cd "/usr/local/sage/devel/sage" && hg import   "/tmp/trac_9032.patch"
applying /tmp/trac_9032.patch
abort: malformed patch a/sage/structure/element.pyx @@ -578,24 +580,26 @@
```

Paul



---

archive/issue_comments_083456.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2011-01-10T10:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83456",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_083457.json:
```json
{
    "body": "sorry, I clicked on the wrong button.",
    "created_at": "2011-01-10T10:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83457",
    "user": "https://github.com/zimmermann6"
}
```

sorry, I clicked on the wrong button.



---

archive/issue_comments_083458.json:
```json
{
    "body": "ok another attempt. But this time, I made the changes much simpler, all elements matrix2, expression, heegner which had a numerical_approx, I just added _numerical_approx=numerical_approx. \n\nAdded numerical_approx and N =n in elements\n\nchanged functional line 1252 so it calls x._numerical_approx. So if we call numerical_approx for any element (for example integers) which does not have it explicitly defined it does not go into an infinite loop",
    "created_at": "2011-01-10T20:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83458",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

ok another attempt. But this time, I made the changes much simpler, all elements matrix2, expression, heegner which had a numerical_approx, I just added _numerical_approx=numerical_approx. 

Added numerical_approx and N =n in elements

changed functional line 1252 so it calls x._numerical_approx. So if we call numerical_approx for any element (for example integers) which does not have it explicitly defined it does not go into an infinite loop



---

archive/issue_comments_083459.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-10T20:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83459",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083460.json:
```json
{
    "body": "This needs a commit message.",
    "created_at": "2011-01-10T20:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83460",
    "user": "https://github.com/adeines"
}
```

This needs a commit message.



---

archive/issue_comments_083461.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-10T20:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83461",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083462.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-10T20:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83462",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083463.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-10T20:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83463",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083464.json:
```json
{
    "body": "A few minor points:\n\nYou can just rename `numerical_approx` to `_numerical_approx` in `matrix2.pyx` without keeping `numerical_approx` since `Matrix` is an `element` so it inherits the default implementation of `numerical_approx`. Same for `expression.pyx`.\n\n(On the other hand, `heegner.py` does need both.)\n\nI would change the docstrings in `structure/element.pyx` to something shorter than the full output. Maybe the following?\n\n\n```\n[..., 'is_idempotent', 'is_integral', ...]\n```\n\n\n\nIs the (capital) `N()` for consistency with something, or is that new?",
    "created_at": "2011-01-10T20:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83464",
    "user": "https://github.com/wjp"
}
```

A few minor points:

You can just rename `numerical_approx` to `_numerical_approx` in `matrix2.pyx` without keeping `numerical_approx` since `Matrix` is an `element` so it inherits the default implementation of `numerical_approx`. Same for `expression.pyx`.

(On the other hand, `heegner.py` does need both.)

I would change the docstrings in `structure/element.pyx` to something shorter than the full output. Maybe the following?


```
[..., 'is_idempotent', 'is_integral', ...]
```



Is the (capital) `N()` for consistency with something, or is that new?



---

archive/issue_comments_083465.json:
```json
{
    "body": "If I changed matrix2 and expression to not have numerical_approx then the documentation won't show up. \n\nchanged element.pyx\n\nAnd yes N() is for consistency, but I did remove them from expression since it is not needed.",
    "created_at": "2011-01-10T23:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83465",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

If I changed matrix2 and expression to not have numerical_approx then the documentation won't show up. 

changed element.pyx

And yes N() is for consistency, but I did remove them from expression since it is not needed.



---

archive/issue_comments_083466.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-10T23:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83466",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083467.json:
```json
{
    "body": "This patch won't apply since documentation for misc/functional.py and symbolic/integration/integral.py is changed in rc1. I will update the patch today after I download new version of rc1",
    "created_at": "2011-01-11T18:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83467",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

This patch won't apply since documentation for misc/functional.py and symbolic/integration/integral.py is changed in rc1. I will update the patch today after I download new version of rc1



---

archive/issue_comments_083468.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-11T18:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83468",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083469.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-12T18:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83469",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083470.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-12T19:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83470",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083471.json:
```json
{
    "body": "\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n\tsage -t  devel/sage/sage/symbolic/function.pyx # 2 doctests failed\n\tsage -t  devel/sage/sage/misc/randstate.pyx # Time out\n\tsage -t  devel/sage/sage/interfaces/sage0.py # Time out\n\tsage -t  devel/sage/sage/interfaces/psage.py # Time out\n\tsage -t  devel/sage/sage/plot/plot.py # Time out\n\tsage -t  devel/sage/sage/symbolic/function_factory.py # 1 doctests failed\n\tsage -t  devel/sage/sage/functions/min_max.py # 3 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/test.py # 0 doctests failed\n\tsage -t  devel/sage/sage/misc/sagedoc.py # Time out\n\tsage -t  devel/sage/sage/schemes/generic/toric_divisor.py # Time out\n\tsage -t  devel/sage/sage/tests/cmdline.py # Time out\n\tsage -t  devel/sage/sage/misc/trace.py # 2 doctests failed\n\tsage -t  devel/sage/sage/parallel/use_fork.py # 0 doctests failed\n\tsage -t  devel/sage/sage/symbolic/expression.pyx # Time out\n\tsage -t  devel/sage/sage/geometry/polyhedra.py # Time out\n\tsage -t  devel/sage/sage/tests/startup.py # 1 doctests failed\n----------------------------------------------------------------------\n```\n",
    "created_at": "2011-01-12T19:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83471",
    "user": "https://github.com/adeines"
}
```


```
----------------------------------------------------------------------

The following tests failed:

	sage -t  devel/sage/sage/symbolic/function.pyx # 2 doctests failed
	sage -t  devel/sage/sage/misc/randstate.pyx # Time out
	sage -t  devel/sage/sage/interfaces/sage0.py # Time out
	sage -t  devel/sage/sage/interfaces/psage.py # Time out
	sage -t  devel/sage/sage/plot/plot.py # Time out
	sage -t  devel/sage/sage/symbolic/function_factory.py # 1 doctests failed
	sage -t  devel/sage/sage/functions/min_max.py # 3 doctests failed
	sage -t  devel/sage/sage/modular/modform/test.py # 0 doctests failed
	sage -t  devel/sage/sage/misc/sagedoc.py # Time out
	sage -t  devel/sage/sage/schemes/generic/toric_divisor.py # Time out
	sage -t  devel/sage/sage/tests/cmdline.py # Time out
	sage -t  devel/sage/sage/misc/trace.py # 2 doctests failed
	sage -t  devel/sage/sage/parallel/use_fork.py # 0 doctests failed
	sage -t  devel/sage/sage/symbolic/expression.pyx # Time out
	sage -t  devel/sage/sage/geometry/polyhedra.py # Time out
	sage -t  devel/sage/sage/tests/startup.py # 1 doctests failed
----------------------------------------------------------------------
```




---

archive/issue_comments_083472.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-13T05:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83472",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_083473.json:
```json
{
    "body": "mhampton points out there isn't a patch attached.",
    "created_at": "2011-01-13T05:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83473",
    "user": "https://github.com/wjp"
}
```

mhampton points out there isn't a patch attached.



---

archive/issue_comments_083474.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-13T05:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83474",
    "user": "https://github.com/wjp"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083475.json:
```json
{
    "body": "Let's try this one more time. I promise this one is not empty. I am currently also running testall on rc1",
    "created_at": "2011-01-13T05:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83475",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Let's try this one more time. I promise this one is not empty. I am currently also running testall on rc1



---

archive/issue_comments_083476.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-13T05:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83476",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083477.json:
```json
{
    "body": "Everything finally passes.",
    "created_at": "2011-01-13T06:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83477",
    "user": "https://github.com/adeines"
}
```

Everything finally passes.



---

archive/issue_comments_083478.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-13T06:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83478",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083479.json:
```json
{
    "body": "Confirmed. (Leaving it as positive review after the patch was updated.)",
    "created_at": "2011-01-13T08:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83479",
    "user": "https://github.com/wjp"
}
```

Confirmed. (Leaving it as positive review after the patch was updated.)



---

archive/issue_comments_083480.json:
```json
{
    "body": "Replying to [comment:21 wjp]:\n> Confirmed. (Leaving it as positive review after the patch was updated.)\n\nExcept the commit message of the latest patch is somewhat mystifying.    O bureaucracy!  Maybe a friendly release manager can just update the patch with something like \"Ensures everything relevant can be numerically approximated and changes things to an underscore method in a few cases\"...",
    "created_at": "2011-01-13T15:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83480",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:21 wjp]:
> Confirmed. (Leaving it as positive review after the patch was updated.)

Except the commit message of the latest patch is somewhat mystifying.    O bureaucracy!  Maybe a friendly release manager can just update the patch with something like "Ensures everything relevant can be numerically approximated and changes things to an underscore method in a few cases"...



---

archive/issue_comments_083481.json:
```json
{
    "body": "Added commit message and comments to all changes. Plus added a couple more doctest (just so I don't wake up in the middle of the night afraid something went wrong). I am currently running all doctest to make sure it all still works. And the patch is nonempty, I checked. \n\nFor some reason, I can't change to needs_review.",
    "created_at": "2011-01-13T18:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83481",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Added commit message and comments to all changes. Plus added a couple more doctest (just so I don't wake up in the middle of the night afraid something went wrong). I am currently running all doctest to make sure it all still works. And the patch is nonempty, I checked. 

For some reason, I can't change to needs_review.



---

archive/issue_comments_083482.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-13T18:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83482",
    "user": "https://github.com/wjp"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083483.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-13T18:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83483",
    "user": "https://github.com/wjp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083484.json:
```json
{
    "body": "All tests pass, and I would positively review this patch, except for three\ndocumentation problems.\n\n1) The extraneous, pre-existing example line (\"a = 2/3\") should be removed \n(in structure/element.pyx). It is neither an example of the use of numerical \napproximation, nor used in the remaining part of the example.\n\n\n```\nsage: a = 8\nsage: a.numerical_approx?\n...\n    \n       Return a numerical approximation of x with at least prec bits of\n       precision.\n    \n       EXAMPLES:\n    \n          sage: (2/3).n()\n          0.666666666666667\n          sage: a = 2/3\n          sage: pi.n(digits=10)\n          3.141592654\n          sage: pi.n(prec=20)   # 20 bits\n          3.1416\n\n```\n\n\n2) Grammatical error in symbolic/expression.pyx:\n\n\n```\nsage: a = cos(3)\nsage: a.numerical_approx?\n...\n    \n       Return a numerical approximation this symbolic expression as either\n```\n\n\nShould be \"numerical approximation of this symbolic expression....\"\n                                   ^^\n\nI know these are trivial and not written by you. However, they're too trivial for their own \npatches, and would fit logically in yours.\n\n3) When I create a symbolic expression, I now get different docstrings for \"n\" \n(from element) and \"numerical_approx\" (from expression):\n\n\n```\nsage: a = cos(3)\nsage: type(a)\n<type 'sage.symbolic.expression.Expression'>\nsage: a.n?\n...\n       Return a numerical approximation of x with at least prec bits of\n       precision.\n    \n       EXAMPLES:\n    \n          sage: (2/3).n()\n          0.666666666666667\n...\n\nsage: a.numerical_approx?\n...    \n       Return a numerical approximation this symbolic expression as either\n       a real or complex number with at least the requested number of bits\n       or digits of precision.\n    \n       EXAMPLES:\n    \n          sage: sin(x).subs(x=5).n()\n          -0.958924274663138\n...\n\n```\n\n\nI believe that this happened when you removed the re-definition of method \"n\" in expression.\nHowever, that is the docstring that you want to be returned for a symbolic expression.",
    "created_at": "2011-01-14T01:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83484",
    "user": "https://trac.sagemath.org/admin/accounts/users/jgaski"
}
```

All tests pass, and I would positively review this patch, except for three
documentation problems.

1) The extraneous, pre-existing example line ("a = 2/3") should be removed 
(in structure/element.pyx). It is neither an example of the use of numerical 
approximation, nor used in the remaining part of the example.


```
sage: a = 8
sage: a.numerical_approx?
...
    
       Return a numerical approximation of x with at least prec bits of
       precision.
    
       EXAMPLES:
    
          sage: (2/3).n()
          0.666666666666667
          sage: a = 2/3
          sage: pi.n(digits=10)
          3.141592654
          sage: pi.n(prec=20)   # 20 bits
          3.1416

```


2) Grammatical error in symbolic/expression.pyx:


```
sage: a = cos(3)
sage: a.numerical_approx?
...
    
       Return a numerical approximation this symbolic expression as either
```


Should be "numerical approximation of this symbolic expression...."
                                   ^^

I know these are trivial and not written by you. However, they're too trivial for their own 
patches, and would fit logically in yours.

3) When I create a symbolic expression, I now get different docstrings for "n" 
(from element) and "numerical_approx" (from expression):


```
sage: a = cos(3)
sage: type(a)
<type 'sage.symbolic.expression.Expression'>
sage: a.n?
...
       Return a numerical approximation of x with at least prec bits of
       precision.
    
       EXAMPLES:
    
          sage: (2/3).n()
          0.666666666666667
...

sage: a.numerical_approx?
...    
       Return a numerical approximation this symbolic expression as either
       a real or complex number with at least the requested number of bits
       or digits of precision.
    
       EXAMPLES:
    
          sage: sin(x).subs(x=5).n()
          -0.958924274663138
...

```


I believe that this happened when you removed the re-definition of method "n" in expression.
However, that is the docstring that you want to be returned for a symbolic expression.



---

archive/issue_comments_083485.json:
```json
{
    "body": "Attachment [trac_9032.patch](tarball://root/attachments/some-uuid/ticket9032/trac_9032.patch) by gagansekhon created at 2011-01-16 22:10:17",
    "created_at": "2011-01-16T22:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83485",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

Attachment [trac_9032.patch](tarball://root/attachments/some-uuid/ticket9032/trac_9032.patch) by gagansekhon created at 2011-01-16 22:10:17



---

archive/issue_comments_083486.json:
```json
{
    "body": "I made the changes  jgaski suggested and ran all test. The patch passed.",
    "created_at": "2011-01-17T00:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83486",
    "user": "https://trac.sagemath.org/admin/accounts/users/gagansekhon"
}
```

I made the changes  jgaski suggested and ran all test. The patch passed.



---

archive/issue_comments_083487.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-17T01:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83487",
    "user": "https://trac.sagemath.org/admin/accounts/users/jgaski"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083488.json:
```json
{
    "body": "I think this is the full name of the last reviewer which I put in the reviewer section, but please advise if it's not correct.",
    "created_at": "2011-01-17T17:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83488",
    "user": "https://github.com/kcrisman"
}
```

I think this is the full name of the last reviewer which I put in the reviewer section, but please advise if it's not correct.



---

archive/issue_comments_083489.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83489",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_022109.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-25T08:14:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9032#event-22109"
}
```



---

archive/issue_comments_083490.json:
```json
{
    "body": "Hi!\n\nIs the alias N really needed? It pollutes the namespace of all elements, and broke some code on the Sage-Combinat queue (in that particular case, it was overwriting a field of a gap3 record element). Well, I guess we can find a workaround but still having n and N and numerical_approx seems like a waste.\n\nCheers,\n                        Nicolas",
    "created_at": "2011-03-23T21:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83490",
    "user": "https://github.com/nthiery"
}
```

Hi!

Is the alias N really needed? It pollutes the namespace of all elements, and broke some code on the Sage-Combinat queue (in that particular case, it was overwriting a field of a gap3 record element). Well, I guess we can find a workaround but still having n and N and numerical_approx seems like a waste.

Cheers,
                        Nicolas



---

archive/issue_comments_083491.json:
```json
{
    "body": "> Is the alias N really needed? It pollutes the namespace of all elements, and broke some code on the Sage-Combinat queue (in that particular case, it was overwriting a field of a gap3 record element). Well, I guess we can find a workaround but still having n and N and numerical_approx seems like a waste.\nN has been an alias for this for a long time, so this just making it consistent -  I think this added a method, not a global function.  In a Sage version nearly a year old:\n\n```\nsage: N(5)\n5.00000000000000\nsage: n(5)\n5.00000000000000\nsage: numerical_approx(5)\n5.00000000000000\nsage: a=5\nsage: a.N?\nObject `a.N` not found.\nsage: a.n\n<built-in method n of sage.rings.integer.Integer object at 0x1091154e0>\n```\n",
    "created_at": "2011-03-24T01:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83491",
    "user": "https://github.com/kcrisman"
}
```

> Is the alias N really needed? It pollutes the namespace of all elements, and broke some code on the Sage-Combinat queue (in that particular case, it was overwriting a field of a gap3 record element). Well, I guess we can find a workaround but still having n and N and numerical_approx seems like a waste.
N has been an alias for this for a long time, so this just making it consistent -  I think this added a method, not a global function.  In a Sage version nearly a year old:

```
sage: N(5)
5.00000000000000
sage: n(5)
5.00000000000000
sage: numerical_approx(5)
5.00000000000000
sage: a=5
sage: a.N?
Object `a.N` not found.
sage: a.n
<built-in method n of sage.rings.integer.Integer object at 0x1091154e0>
```




---

archive/issue_comments_083492.json:
```json
{
    "body": "Hi!\n\nReplying to [comment:32 kcrisman]:\n> N has been an alias for this for a long time, so this just making it consistent -  I think this added a method, not a global function.\n\nYes; I am precisely arguing about this method, and the pollution of the method namespace of all elements. We can't use anymore x.N to access an attribute called N in a gap record x (well, we can, but as x.__getattr__(\"N\") which is not very convenient).\n\nThanks,",
    "created_at": "2011-03-24T08:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83492",
    "user": "https://github.com/nthiery"
}
```

Hi!

Replying to [comment:32 kcrisman]:
> N has been an alias for this for a long time, so this just making it consistent -  I think this added a method, not a global function.

Yes; I am precisely arguing about this method, and the pollution of the method namespace of all elements. We can't use anymore x.N to access an attribute called N in a gap record x (well, we can, but as x.__getattr__("N") which is not very convenient).

Thanks,



---

archive/issue_comments_083493.json:
```json
{
    "body": "I see. Well, it's been merged, so the proper thing to do is to ask on sage-devel or open a ticket. I don't see why it wouldn't be possible to take this behavior away from structure/element and put it only on numerical types, though it would be a little more of a pain.\n\nI could imagine someone wanting numerical approx of e.g. GAP elements, though, and it's true that for consistency n and N should do the same thing as methods as as functions, so maybe this is worth raising on sage-devel. I wouldn't be surprised if no one much cared, though, as long as integers and rationals still had N and n.",
    "created_at": "2011-03-24T12:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83493",
    "user": "https://github.com/kcrisman"
}
```

I see. Well, it's been merged, so the proper thing to do is to ask on sage-devel or open a ticket. I don't see why it wouldn't be possible to take this behavior away from structure/element and put it only on numerical types, though it would be a little more of a pain.

I could imagine someone wanting numerical approx of e.g. GAP elements, though, and it's true that for consistency n and N should do the same thing as methods as as functions, so maybe this is worth raising on sage-devel. I wouldn't be surprised if no one much cared, though, as long as integers and rationals still had N and n.



---

archive/issue_comments_083494.json:
```json
{
    "body": "Replying to [comment:34 kcrisman]:\n> I see. Well, it's been merged, so the proper thing to do is to ask on sage-devel or open a ticket. I don't see why it wouldn't be possible to take this behavior away from structure/element and put it only on numerical types, though it would be a little more of a pain.\n> \n> I could imagine someone wanting numerical approx of e.g. GAP elements, though, and it's true that for consistency n and N should do the same thing as methods as as functions, so maybe this is worth raising on sage-devel. I wouldn't be surprised if no one much cared, though, as long as integers and rationals still had N and n.\n\nDo you mind running this discussion on sage-devel?\n\nI guess someone wanting a numerical approximation on a gap element (that could well be me :-)) can afford to use g.numerical_approx(), or just g.n().\n\nThanks!",
    "created_at": "2011-03-24T12:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9032",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9032#issuecomment-83494",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:34 kcrisman]:
> I see. Well, it's been merged, so the proper thing to do is to ask on sage-devel or open a ticket. I don't see why it wouldn't be possible to take this behavior away from structure/element and put it only on numerical types, though it would be a little more of a pain.
> 
> I could imagine someone wanting numerical approx of e.g. GAP elements, though, and it's true that for consistency n and N should do the same thing as methods as as functions, so maybe this is worth raising on sage-devel. I wouldn't be surprised if no one much cared, though, as long as integers and rationals still had N and n.

Do you mind running this discussion on sage-devel?

I guess someone wanting a numerical approximation on a gap element (that could well be me :-)) can afford to use g.numerical_approx(), or just g.n().

Thanks!
